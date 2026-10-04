---
name: bonsai-implement
description: Implement a scoped Python/C feature or behavior change with focused tests, existing conventions and verified results.
---

# Implement
Read `bonsai-core` and the relevant language skill.
1. Define observable acceptance criteria, touched interfaces and exclusions. Establish unknown semantics from the contract; never invent defaults merely because they make a patch easy. Ask only when missing information changes behavior or risks user work; resolve routine choices from local conventions.
2. Inspect the affected call path and existing tests. Run a narrow baseline before changing behavior. Keep unrelated failures separate; do not broaden the task to repair them automatically.
3. For a behavior change, add a meaningful test and run it RED for the intended reason. Implement the smallest GREEN change. If test-first is infeasible, explain why and perform the strongest available behavior check. Avoid tests that merely duplicate implementation.
4. Preserve APIs, architecture, dependency policy and formatting. Refactor only what the requested change needs; avoid unrelated cleanup and whole-file formatting.
5. Run focused tests, affected integration/build checks and mandatory repository checks. Inspect the final diff and report acceptance criteria met, actual results and limitations.
Stop when the requested behavior is validated. Use `bonsai-signoff` for final review; do not infer commit or release permission from implementation permission.

Work one acceptance criterion at a time. Default to an initial 12-call investigation budget, excluding skill loads. After that, either proceed with the evidenced, authorized fix or report the blocker; do not continue speculative exploration. This budget does not replace required implementation validation.
