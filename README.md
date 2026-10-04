# Coding skills for local models

A collection of concise coding-agent instructions organized by the model they were developed for. Skills guide scope, investigation, testing, implementation and handover; they do not change model weights or guarantee correctness.

The first directory level identifies the intended model family. Runtime-specific folders inside each model section indicate where its skills are used.

| Directory | Intended model | Contents |
|---|---|---|
| [qwen/](qwen/README.md) | Local Qwen through OpenCode | Original Claude-to-Qwen workflow: handover, onboarding, implementation, debugging and sign-off. |
| [bonsai/](bonsai/README.md) | Ternary Bonsai 2 27B; trials used PQ2_0 | Revised v1.1 Python/C skills, practical suitability guidance and evaluation history. |

## Structure

```text
qwen/
  README.md
  LICENSE
  SECURITY.md
  scripts/check_public_content.py
  skills/
    claude/project-handover/SKILL.md
    opencode/
      project-onboarding/SKILL.md
      project-implementation/SKILL.md
      project-debugging/SKILL.md
      project-signoff/SKILL.md
bonsai/
  README.md
  recommendations.md
  skills/opencode/
    bonsai-core/SKILL.md
    bonsai-audit/SKILL.md
    bonsai-debug/SKILL.md
    bonsai-implement/SKILL.md
    bonsai-signoff/SKILL.md
    bonsai-handover/SKILL.md
    bonsai-python/SKILL.md
    bonsai-c/SKILL.md
```

The original repository was moved intact into `qwen/` before the Bonsai section was added. The Claude handover skill belongs there because it prepares work for the Qwen workflow; its runtime is Claude Code, not its destination model. Existing installation paths changed: use `qwen/skills/...` from the repository root.

Choose the model section first, then follow its README. Do not install both collections indiscriminately or load every workflow into one session.

## How the Bonsai skills were developed

1. **Start with an actual problem.** A local Ternary Bonsai 2 27B PQ2_0 agent in OpenCode was asked to audit a Python source-debugger codebase. The baseline prompt requested architecture, likely bugs/design risks, and five concrete improvements with detailed reasoning. No skills were applied.
2. **Review the baseline with a stronger AI.** The complete exported session was reviewed in ChatGPT against the original request, tool calls, edits, test outputs and final answer. The model found useful defects and eventually showed 448 passing offline tests, but used 81 tool calls, drifted into unrequested edits and left the requested analysis incomplete. Recorded assistant durations summed to about 94 minutes; this is not a standardized inference benchmark.
3. **Create a compact package.** Retain the earlier Qwen workflow's separation between process and language guidance, plus test integrity. Add a shared core and dedicated audit skill. Focus on evidence, minimal context, working-tree safety, scoped debugging/implementation, sign-off and compact handover.
4. **Test with the skills loaded.** A fresh broad audit explicitly loaded core, audit and Python guidance. It checked the working tree and test baseline early and made no production/test edits, but still entered long speculative loops. The supplied transcript had 51 calls and roughly 75 minutes of recorded assistant durations, ending without a final report.
5. **Introduce a narrow, discriminating test.** Audit one command: whether a requested source filename is respected when it differs from the program counter's file. Set limits of six relevant files, twelve post-load calls and two reproduction attempts. Require a verdict, evidence, test-coverage assessment and proposed fix; forbid implementation.
6. **Review the new output.** The bounded run delivered at exactly twelve calls in about fourteen minutes. Source inspection supported a defect. However, tests ran late, a reproduction harness failed, parser/payload interfaces were guessed, and proposed code introduced unverified semantics. Its passing baseline did not prove the reproduction or proposed fix correct.
7. **Revise from observed failures.** Version 1.1 adds default audit budgets, an early-test deadline, failed-harness attempt counting, actual-interface inspection, direct test execution, explicit evidence labels and mandatory reporting at the limit. Debugging and implementation retain their validation requirements while bounding initial investigation.

This is an iterative workflow: problem → baseline output → stronger-AI review → skill creation → local trial → output review → revision. Reviews are also fallible. The trials varied in prompt, scope and repository state; they are not controlled proof that skills caused all improvements. Version 1.1 has been structurally validated but has not yet been evaluated on the target model. C target correctness was not demonstrated by these Python trials.

## Contributing and publication

Add new model-specific collections under a model directory, with one named folder and `SKILL.md` per skill. Keep instructions concise and separate observed results from predictions. Record model/quantization, scope, validation and unresolved limitations when claiming improvements.

Follow [the public-content policy](qwen/SECURITY.md). From the repository root, run:

```bash
python3 qwen/scripts/check_public_content.py
git diff --cached --check
```

Do not publish raw session transcripts, personal machine paths, credentials or account details. The original license is preserved at [qwen/LICENSE](qwen/LICENSE); additions use the same license.
