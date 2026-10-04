---
name: bonsai-core
description: Apply shared scope, evidence, context, test-integrity and working-tree rules to every Python/C audit, debugging, implementation, sign-off or handover task.
---

# Core contract
1. State outcome, mode and acceptance criteria. Analysis stays read-only; proposals, blank messages and compaction do not authorize implementation. Load this core, one workflow and only relevant language guidance.
2. Check root, branch, status and relevant staged/unstaged diffs. Preserve existing work; do not guess ownership. Never reset, clean, restore, stash or rewrite history as cleanup. Ask only about blocking ambiguity or conflicting edits.
3. Read applicable repository rules and task-local configuration once. Search specific symbols with `rg`; read bounded slices along one call path. Do not dump the repository or reread unchanged files.
4. Label evidence: reproduced, established by source inspection, hypothesis, or blocked. Inspect actual definitions before assuming API inputs, return types or nested fields. A harness failure does not reproduce a product bug.
5. Check one hypothesis with one decisive experiment; use a second only if inconclusive. Accept observed evidence. If memory disagrees, inspect the relevant implementation once; do not invent version differences. After two failed diagnostic/harness attempts, report evidence and blocker.
6. Never delete, weaken, trivialize, skip, xfail or change expectations to hide test failures. Mock external boundaries, never the behavior under test. Change tests only for changed requirements or proven test defects; explain why.
7. Use the existing environment. Run commands directly; never pipe tests into `tail`. Save verbose output to a fresh temporary log if needed, preserving the command's status before reading it. Timeout means incomplete. Check actual state before retrying a mutation with unknown outcome.
8. Follow the workflow budget. When exhausted, deliver known results and limitations; do not silently reset the budget. Keep updates to finding, next check or blocker. Commit/push/release only when authorized; stage only task-owned hunks. Keep secrets out of artifacts.
Finish with outcome, actual checks, limitations and any necessary next action. Do not claim completion from code written or a passing subset alone.
