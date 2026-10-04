---
name: bonsai-debug
description: Reproduce and fix an authorized Python/C defect using a causal hypothesis, regression test and minimal change.
---

# Debug
Read `bonsai-core` and the relevant language skill.
1. Record expected behavior, failing input, exact command, environment, exit status and error. Inspect existing diffs before attributing a failure to current work. Establish a narrow baseline.
2. Before any harness, inspect real argument shapes, result types and existing fixtures. Use the project interpreter; invoke the public command or pass only argument text to an internal parser. Check nested payload fields. Trace the failing path. State one hypothesis and choose one check that can disprove it. Observe the result before choosing another. After two checks without progress, summarize evidence and choose a different approach; do not repeat the same attempt.
3. Add a regression exercising the real path. Run it before the fix and verify failure for the defect, not an import/setup error. If reproduction is unavailable, label the diagnosis unverified and explain the limit.
4. Apply the smallest authorized fix. Run the regression, affected tests and required project checks. Classify remaining failures as baseline, introduced, or unknown using evidence.
5. Review the diff. Report symptom, causal chain, fix, commands/results and unresolved risks. Use sign-off only within the authorized scope.
Do not suppress exceptions, silence warnings or change tests merely to obtain green output.

Work one acceptance criterion at a time. Default to an initial 12-call investigation budget, excluding skill loads. After that, either proceed with the evidenced, authorized fix or report the blocker; do not continue speculative exploration. This budget does not replace required implementation validation.
