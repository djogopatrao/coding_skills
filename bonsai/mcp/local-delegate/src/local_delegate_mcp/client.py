import json
import os
from dataclasses import dataclass
from typing import TypeVar

import httpx
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class LocalModelError(RuntimeError):
    pass


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("LLAMA_CPP_BASE_URL", "http://127.0.0.1:8080/v1")
    model: str = os.getenv("LLAMA_CPP_MODEL", "local-model")
    timeout_seconds: float = float(os.getenv("LLAMA_CPP_TIMEOUT", "180"))
    max_input_chars: int = int(os.getenv("LOCAL_DELEGATE_MAX_INPUT_CHARS", "400000"))
    max_output_tokens: int = int(os.getenv("LOCAL_DELEGATE_MAX_OUTPUT_TOKENS", "4096"))
    temperature: float = float(os.getenv("LOCAL_DELEGATE_TEMPERATURE", "0.1"))


class LlamaCppClient:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()

    def _guard_input(self, text: str, context: str) -> None:
        total = len(text) + len(context)
        if not text.strip():
            raise ValueError("input_text must not be empty")
        if total > self.settings.max_input_chars:
            raise ValueError(
                f"delegated input is {total} characters; limit is {self.settings.max_input_chars}"
            )

    async def status(self) -> dict:
        url = f"{self.settings.base_url.rstrip('/')}/models"
        try:
            async with httpx.AsyncClient(timeout=self.settings.timeout_seconds) as client:
                response = await client.get(url)
                response.raise_for_status()
                payload = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise LocalModelError(f"llama.cpp status check failed: {exc}") from exc
        return {"reachable": True, "base_url": self.settings.base_url, "models": payload.get("data", [])}

    async def generate(
        self,
        *,
        task: str,
        system_prompt: str,
        task_prompt: str,
        input_text: str,
        context: str,
        output_model: type[T],
    ) -> T:
        self._guard_input(input_text, context)
        schema = output_model.model_json_schema()
        user_prompt = (
            f"TASK: {task}\n\nINSTRUCTIONS:\n{task_prompt}\n\n"
            f"CONTEXT:\n{context or '(none)'}\n\nINPUT:\n{input_text}"
        )
        payload = {
            "model": self.settings.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self.settings.temperature,
            "max_tokens": self.settings.max_output_tokens,
            "response_format": {"type": "json_schema", "schema": schema},
        }
        url = f"{self.settings.base_url.rstrip('/')}/chat/completions"
        try:
            async with httpx.AsyncClient(timeout=self.settings.timeout_seconds) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                body = response.json()
            content = body["choices"][0]["message"]["content"]
            if isinstance(content, dict):
                return output_model.model_validate(content)
            if not isinstance(content, str):
                raise LocalModelError("llama.cpp returned a non-text chat completion")
            return output_model.model_validate_json(content)
        except (httpx.HTTPError, KeyError, IndexError, json.JSONDecodeError) as exc:
            raise LocalModelError(f"llama.cpp request failed: {exc}") from exc
        except Exception as exc:
            if isinstance(exc, LocalModelError):
                raise
            raise LocalModelError(f"local model output failed validation: {exc}") from exc
