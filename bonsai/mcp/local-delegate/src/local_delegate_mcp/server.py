from mcp.server import MCPServer

from .client import LlamaCppClient
from .prompts import BASE_SYSTEM_PROMPT, TASK_PROMPTS
from .schemas import (
    AnalysisOutput,
    ClassificationOutput,
    DocumentationOutput,
    RequirementsOutput,
    SummaryOutput,
    TestDraftOutput,
    TestReviewOutput,
)

mcp = MCPServer("local-delegate")


async def _delegate(task: str, input_text: str, context: str, output_model):
    client = LlamaCppClient()
    result = await client.generate(
        task=task,
        system_prompt=BASE_SYSTEM_PROMPT,
        task_prompt=TASK_PROMPTS[task],
        input_text=input_text,
        context=context,
        output_model=output_model,
    )
    return {
        "task": task,
        "model": client.settings.model,
        "result": result.model_dump(),
        "acceptance": "candidate_only",
        "validation_required": True,
    }


@mcp.tool()
async def local_llm_status() -> dict:
    """Check whether the configured local llama.cpp OpenAI-compatible endpoint is reachable."""
    return await LlamaCppClient().status()


@mcp.tool()
async def summarize_code(input_text: str, context: str = "") -> dict:
    """Delegate bounded code/diff summarization. Treat the result as untrusted candidate analysis."""
    return await _delegate("summarize_code", input_text, context, SummaryOutput)


@mcp.tool()
async def analyze_function(input_text: str, context: str = "") -> dict:
    """Delegate analysis of one supplied function/module. Verify findings against source before use."""
    return await _delegate("analyze_function", input_text, context, AnalysisOutput)


@mcp.tool()
async def generate_tests(input_text: str, context: str = "") -> dict:
    """Draft tests for supplied code/requirements. Caller must review and execute tests before acceptance."""
    return await _delegate("generate_tests", input_text, context, TestDraftOutput)


@mcp.tool()
async def review_tests(input_text: str, context: str = "") -> dict:
    """Review supplied tests for integrity and coverage. Caller retains final authority."""
    return await _delegate("review_tests", input_text, context, TestReviewOutput)


@mcp.tool()
async def classify_issue(input_text: str, context: str = "") -> dict:
    """Classify a bounded issue/log to reduce expensive hosted-model triage."""
    return await _delegate("classify_issue", input_text, context, ClassificationOutput)


@mcp.tool()
async def extract_requirements(input_text: str, context: str = "") -> dict:
    """Extract explicit requirements from supplied text. Verify extracted requirements before implementation."""
    return await _delegate("extract_requirements", input_text, context, RequirementsOutput)


@mcp.tool()
async def draft_documentation(input_text: str, context: str = "") -> dict:
    """Draft technical documentation from supplied facts. Verify facts_to_verify before publishing."""
    return await _delegate("draft_documentation", input_text, context, DocumentationOutput)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
