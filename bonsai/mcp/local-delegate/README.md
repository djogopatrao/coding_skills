# Local delegation MCP for llama.cpp

A deliberately narrow MCP server that lets a stronger coding agent delegate bounded, low-risk work to a local-network llama.cpp model while retaining validation and final authority in the hosted agent.

## Why this is narrow

The MCP does **not** expose a generic `ask_local_llm` tool. Each tool has a defined task, a task-specific prompt, schema-constrained output, and an explicit `candidate_only` acceptance marker. This makes delegation predictable and reduces the chance that a hosted agent blindly accepts local output.

Current tools:

- `summarize_code`
- `analyze_function`
- `generate_tests`
- `review_tests`
- `classify_issue`
- `extract_requirements`
- `draft_documentation`
- `local_llm_status`

## Delegation policy

Use the local model when the cost of validating its answer is lower than doing the task with the hosted model.

Good candidates: bounded summarization, requirement extraction, issue/log classification, candidate tests, test review, documentation drafts, and analysis of a supplied function or short module.

Do not delegate final architectural decisions, security decisions, migrations/destructive operations, subtle concurrency/protocol correctness, final sign-off, or acceptance of code without independent validation.

### Required validation

| Local result | Hosted-agent validation |
|---|---|
| Summary / analysis | Compare claims to supplied source; reject unsupported claims. |
| Generated tests | Review test integrity, then run the tests against the real project. |
| Test review | Inspect the cited test/code evidence before acting. |
| Classification | Check decisive log/source signals; do not treat confidence as proof. |
| Requirements | Compare every requirement to source material and resolve ambiguities. |
| Documentation | Verify `facts_to_verify`; never publish them as facts. |

## Install

Python 3.11+ is required.

```bash
cd bonsai/mcp/local-delegate
python -m venv .venv
. .venv/bin/activate
pip install -e '.[test]'
```

Configure the endpoint in the environment that launches the MCP process:

```bash
export LLAMA_CPP_BASE_URL=http://192.168.1.50:8080/v1
export LLAMA_CPP_MODEL=local-model
```

The repository contains only placeholders/examples; do not commit credentials, private hostnames, or private addresses specific to your environment.

## Test

```bash
pytest
```

Then verify connectivity through the MCP tool `local_llm_status` or directly:

```bash
curl "$LLAMA_CPP_BASE_URL/models"
```

## Run over stdio

```bash
local-delegate-mcp
```

The default MCP transport is stdio. The MCP process itself connects over HTTP to the llama.cpp server on the LAN.

## Claude Code

From this directory, using the project virtual environment:

```bash
claude mcp add --transport stdio --scope user local-delegate -- \
  "$PWD/.venv/bin/local-delegate-mcp"
claude mcp list
```

Keep the llama.cpp environment variables available to the process Claude launches. Prefer a small wrapper script or your shell/session environment rather than putting sensitive values into repository files.

Suggested `CLAUDE.md` policy:

```text
Use local-delegate MCP for bounded summarization, extraction, classification, candidate tests,
test review, documentation drafts, and single-function/module analysis when validation is cheaper
than doing the work yourself. Treat every local result as untrusted candidate work. Verify source
claims and run relevant tests before using it. Never delegate final architecture, security-sensitive
judgment, destructive changes, or sign-off.
```

## Codex CLI

Codex and its IDE extension share MCP configuration. Add a stdio MCP server in `~/.codex/config.toml` using the installed executable and environment required to reach llama.cpp. If you prefer the CLI, use `codex mcp add` and verify with `codex mcp list`.

Suggested `AGENTS.md` policy is the same as the Claude policy above.

## Configuration

| Variable | Default | Purpose |
|---|---:|---|
| `LLAMA_CPP_BASE_URL` | `http://127.0.0.1:8080/v1` | OpenAI-compatible llama.cpp base URL. |
| `LLAMA_CPP_MODEL` | `local-model` | Model identifier sent to llama.cpp. |
| `LLAMA_CPP_TIMEOUT` | `180` | HTTP timeout in seconds. |
| `LOCAL_DELEGATE_MAX_INPUT_CHARS` | `400000` | Hard request-size guard before sending local work. |
| `LOCAL_DELEGATE_MAX_OUTPUT_TOKENS` | `4096` | Maximum generated tokens. |
| `LOCAL_DELEGATE_TEMPERATURE` | `0.1` | Low temperature for repeatable engineering work. |

The character limit is a safety guard, not a token estimator. Keep the agent's delegated material comfortably below the model's actual context budget.

## Security and trust boundary

- The MCP server performs no filesystem reads and executes no shell commands.
- It sends only the text explicitly passed by the calling agent to the configured llama.cpp endpoint.
- The endpoint is configurable; review it before sending proprietary source or logs.
- No API key is required by a default llama.cpp server, but if you place a proxy/auth layer in front of it, keep credentials outside this repository.
- Local output is structurally validated, not semantically trusted.
