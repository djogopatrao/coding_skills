---
name: project-implementation
description: Implement a requested change in an existing project using focused TDD, existing conventions, and final validation.
---

# Project Implementation

## Understand first

1. Read project instructions and inspect the relevant source, tests, interfaces,
   and recent changes before editing.
2. Confirm the requested behavior, affected boundaries, and available validation
   commands. If the requirement is ambiguous enough to change the design, ask.
3. Follow the actual codebase rather than an outdated plan. Preserve its
   architecture, naming, types, error handling, memory strategy, and module
   boundaries.

## Use TDD: RED → GREEN → REFACTOR

1. **RED:** add or adjust a meaningful test that expresses the required behavior
   or regression, and confirm it fails for the intended reason.
2. **GREEN:** make the smallest production change that makes it pass.
3. **REFACTOR:** improve clarity only while the relevant tests remain green.

## Test integrity

Tests define required behavior and must not be manipulated merely to obtain a
passing result.

Never delete a failing test because production code does not satisfy it; weaken
an assertion without a behavioral reason; replace meaningful assertions with
trivial ones; skip or mark a test expected-to-fail to complete the task; mock the
behavior under test instead of exercising it; or change expected values merely
to match incorrect implementation output.

Change a test only when the requirement changed or inspection proves the test is
incorrect. State why.

## Implementation discipline

- Keep changes focused; avoid opportunistic rewrites and unrelated formatting.
- For C or systems code, explicitly check type widths and conversions, bounds,
  lifetimes, buffer sizes, bit masks, overflow, and ownership. Avoid unnecessary
  allocations, dependencies, or expensive algorithms.
- Build and run the relevant tests. Fix errors introduced by the change.
- Inspect the final diff for scope, correctness, and accidental artifacts.

## Report

State the behavior implemented, files changed, tests/commands run and their
results, plus any remaining risks or follow-up work. Code being written is not
completion; validated behavior is.
