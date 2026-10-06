# Ternary Bonsai 2 27B skills — v1.1

## Evaluation setup

The local Ternary Bonsai 2 27B PQ2_0 model runs through **llama.cpp**, with **OpenCode** as the coding agent and a configured context window of **131,072 tokens**.

Hardware: NVIDIA GeForce RTX 3060 with 12 GB VRAM, AMD Ryzen 7 7700, and 64 GB system RAM.

These settings are user-reported. Context capacity is not actual session token usage. Timing observations apply to this setup; inference throughput, runtime versions and GPU offload settings were not measured in these reviews.

Compact OpenCode instructions for bounded Python/C work. The observed trials used Ternary Bonsai 2 27B PQ2_0. These instructions address its observed workflow failures; they are not a guarantee of model reliability or a benchmark against other models.

## Suitable tasks and limits

| Task | Suggested use |
|---|---|
| Explain a function, trace a short path, locate behavior | Good candidate; require exact source evidence. |
| Summarize a diff or prepare handover | Useful with verification of state and claims. |
| Fix one reproducible Python defect or implement a small conventional feature | Supervised use; explicit acceptance criteria, real regression tests and independent diff review. |
| Draft tests or inspect coverage | Review parser inputs, fixture types and assertions that distinguish incorrect behavior. |
| Whole-repository audit, broad refactor or long autonomous project | Split into bounded tasks; do not delegate scope and readiness decisions. |
| Subtle concurrency, protocol or state-machine failures | Low reliance; require decisive experiments and independent review. |
| C memory safety, ABI or embedded/cross-compiled correctness | Unproven by these trials; use actual toolchain and target validation. |
| Security, sensitive-data handling, migrations or destructive operations | Assistance only; keep final authority with a reviewer. |

Read [recommendations.md](recommendations.md) for the full assessment and usage tips, and [the repository overview](../README.md#how-the-bonsai-skills-were-developed) for the baseline/test/revision method.

## Skills

| Skill | Role |
|---|---|
| bonsai-core | Shared scope, evidence, context, test integrity and working-tree rules. |
| bonsai-audit | Read-only audit; defaults to 6 relevant files, 12 post-load calls and 2 reproduction attempts. |
| bonsai-debug | Causal diagnosis, actual-interface checks, regression and minimal fix. |
| bonsai-implement | Acceptance criteria, focused TDD and verified behavior. |
| bonsai-signoff | Review code/tests/docs, validation and task-owned changes; authorized commits only. |
| bonsai-handover | Compact state/evidence/next-step brief; preserve mode and remaining budget. |
| bonsai-python | Existing environment, versions, interfaces, resource handling and test conventions. |
| bonsai-c | Existing compiler/target, types, ownership, ABI and target validation. |

Load core, one workflow and the relevant language guidance. Defaults are starting limits, overridden by the task's explicit constraints. The audit requires a baseline within the first four post-load calls when feasible and delivery at the limit. Debugging/implementation bound initial diagnosis without dropping required validation. Prompt budgets are not mechanically enforced.

## Hosted-agent delegation through MCP

The repository also includes a [local delegation MCP server](mcp/local-delegate/README.md) for Claude Code, Codex, or another MCP-capable hosted agent to offload bounded work to the local llama.cpp/Bonsai model.

The gateway intentionally exposes narrow tasks rather than a generic prompt endpoint. Local outputs are schema-constrained and marked as candidate work; the hosted agent remains responsible for source verification, running tests, security-sensitive judgment, architecture, destructive operations, and final sign-off.

This is intended to reduce hosted-model usage when validating a local result costs less than having the hosted model perform the entire subtask.

## Install

From the repository root, copy the chosen folders into your project's skills directory:

```bash
mkdir -p <project>/.opencode/skills
cp -R bonsai/skills/opencode/bonsai-core <project>/.opencode/skills/
cp -R bonsai/skills/opencode/bonsai-audit <project>/.opencode/skills/
cp -R bonsai/skills/opencode/bonsai-python <project>/.opencode/skills/
```

Replace `<project>` with your project path. Review existing same-name skills before copying. When updating from v1.0, retain the same folder names and replace only the eight intended `SKILL.md` files after checking local customizations. No model configuration change is required.

Start a fresh session and explicitly ask OpenCode to load the named skills. Verify actual skill-loading calls. Example:

> Load bonsai-core, bonsai-audit and bonsai-python. Audit only [observable question]. Stay read-only and preserve existing changes. Use the audit budget. Run the relevant offline baseline early. Inspect actual APIs before reproducing. Deliver verdict, evidence, test coverage, proposed fix/regression and uncertainties at the limit.

For changes, use debugging or implementation instead and state acceptance criteria. Authorize implementation, committing and publishing separately as needed. Stop repetitive investigation by requesting the evidence and current verdict.

## Validation status

The eight skills are 201–330 words each and have valid name/description frontmatter. Revision 1.1 was checked structurally; its adherence on the local model remains untested. Earlier bounded trials support trying these constraints but did not establish reliable patch correctness. Re-test on the same repository state and compare scope, baseline timing, evidence quality, harness correctness and completed deliverables.
