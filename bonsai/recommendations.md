# Ternary Bonsai 2 27B PQ2_0: recommended uses and usage tips

## Runtime and hardware context

| Model | Inference runtime | Coding agent | Configured context window |
|---|---|---|---|
| Qwen | Ollama | OpenCode | 131,072 tokens |
| Ternary Bonsai 2 27B PQ2_0 | llama.cpp | OpenCode | 131,072 tokens |

Hardware: NVIDIA GeForce RTX 3060 with 12 GB VRAM, AMD Ryzen 7 7700, and 64 GB system RAM.

The setup is user-reported. The assessments below concern the Bonsai/OpenCode sessions; they are not a controlled comparison with Qwen. Context capacity does not establish actual session usage or explain the reasoning failures by itself. Recorded durations depend on the local setup and are not standardized performance measurements.

**Use Ternary Bonsai 2 27B PQ2_0 for small, verifiable tasks with clear boundaries and human review.** Our results show useful code inspection and debugging ability, but inconsistent reasoning, weak reproduction scripts, and a tendency to keep investigating instead of delivering.

This assessment applies to the **model, quantization and OpenCode setup tested here**. We have not isolated which component causes each weakness.

| Session | What it demonstrated |
|---|---|
| Broad task, no skills | Found useful defects and eventually passed 448 offline tests, but edited code during an analysis request and left the requested report incomplete. |
| Broad task, with skills | Loaded the skills, inspected existing changes and ran tests early. Avoided production edits, but continued speculative loops; the supplied transcript ended without a report. |
| Narrow task, with skills and explicit budget | Finished in about 14 minutes, respected the 12-call limit and delivered a supported static finding. Its reproduction failed, and its proposed patch/test contained mistakes. |

**The strongest evidence is for controlling task size and requiring a deliverable.** Skills improved observable discipline, but loading them did not ensure compliance. The sessions also used different prompts and repository states, so we cannot attribute every improvement to skills.

| Problem type | Recommended reliance |
|---|---|
| Explain a function or trace a short call path | **Good candidate.** Require source references and distinguish facts from assumptions. |
| Locate code responsible for a known behavior | **Good candidate.** Give the symptom and a small search boundary. |
| Summarize an existing diff or prepare a handover | **Useful with verification.** Check commands, status and claims against the repository. |
| Investigate one reproducible Python defect | **Suitable with supervision.** Supply the failing command; require a regression and a minimal patch. |
| Implement a small feature following an existing pattern | **Conditional.** Define acceptance criteria and review the diff and tests. |
| Suggest tests or review test coverage | **Useful as a draft.** Verify fixtures, actual payload types and whether assertions distinguish wrong behavior. |
| Audit an entire repository or design a broad refactor | **Low reliance.** Split into separate questions; use another reviewer for synthesis. |
| Diagnose subtle concurrency, state-machine or protocol failures | **Low reliance.** Require decisive experiments and independent review. |
| C memory safety, ABI, undefined behavior or embedded target correctness | **Not established by these trials.** Validate with the actual compiler, target and tests. |
| Security, clinical-data handling, migrations or destructive operations | **Do not delegate final authority.** Use it to assist inspection and drafting, with explicit human review. |

For your Python/C workflow, I would use these practices:

1. **Give one observable problem per session.** “Does `list FILE` respect a different filename?” worked much better than “analyze the codebase.”
2. **Load the core, one workflow and the relevant language skill.** Confirm the skill-loading calls appeared.
3. **Define the output and stopping condition.** For a narrow audit, start with roughly 6 relevant files, 12 tool calls and at most 2 reproduction attempts. These are starting limits, not universal limits.
4. **Provide the project’s exact interpreter and test command.** Require tests early and preserve their exit status. Passing tests support only the behavior they exercise.
5. **Require evidence labels:** reproduced, established by source inspection, hypothesis, or blocked. A broken reproduction harness is not evidence of a product defect.
6. **Make it inspect interfaces before writing harnesses or tests.** Several failures came from guessed parser inputs and payload attributes.
7. **Keep analysis, implementation and sign-off separate.** Authorize each transition explicitly, especially commits and operations affecting existing work.
8. **Interrupt repetition.** If it reconsiders the same question after decisive evidence, request the current conclusion, remaining uncertainty and report immediately.
9. **Review proposed patches independently.** A correct diagnosis did not consistently produce a correct fix or regression test.

A useful default request is:

> Load bonsai-core, bonsai-debug and bonsai-python. Investigate this single failure: [command and output]. Acceptance criteria: [observable behavior]. Preserve existing changes. Inspect actual interfaces before writing a reproduction. Run the baseline early. Make the smallest fix and a regression test; do not commit. If two diagnostic attempts fail, report the evidence and blocker before continuing.

For now, I would trust it to **produce bounded, reviewable work**, and let tests plus your review determine acceptance. I would not trust it to independently decide scope, prove readiness, or manage a long development effort.
