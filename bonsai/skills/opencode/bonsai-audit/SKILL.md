---
name: bonsai-audit
description: Analyze architecture, inspect likely defects, or compare a handover with code without editing production files.
---

# Bounded audit
Read `bonsai-core`. Stay read-only in the repository; use scratch for reproduction files.
1. Name the exact question and report structure. For a narrow audit, default to 6 distinct relevant source/test files, 12 post-load tool calls and 2 reproduction attempts total, including failed harnesses. Count shell calls and search/read calls; do not hide broad exploration in one shell call. User limits override defaults. For a broad audit, inspect a representative slice and disclose coverage gaps.
2. Check repository state, instructions and runner. Run relevant offline tests within the first 4 post-load calls when feasible; otherwise state the blocker. Example, only for a pytest project:
   `.venv/bin/python -m pytest tests/test_feature.py -q`
   Run directly; capture the tool exit status. Do not pipe into `tail`.
3. Trace parser/entry point, handler, return shape and relevant tests before writing a harness. Reuse fixtures. Exercise the real behavior with inputs that distinguish correct from incorrect output; inspect nested payload fields before asserting them.
4. Separate source-established defects from successful reproductions. Evaluate existing tests by their assertions, not passing counts. Drop disproven suspicions. Do not invent expected behavior: consult the contract, or label unresolved semantics.
5. Reserve the last 2 calls for one decisive check and any necessary final state verification. Stop sooner when evidence answers the question. At the limit, deliver: verdict, paths/symbols and commands/results, test coverage, smallest proposed fix/regression, and uncertainties. No extra call to polish a failed harness.
Keep patch proposals conceptual if interfaces or semantics are unverified. Do not implement, install dependencies or expand into adjacent defects.
