---
name: project-debugging
description: Debug a defect systematically: reproduce it, gather evidence, identify root cause, add a regression test, make a minimal fix, and validate it.
---

# Project Debugging

## Establish facts

1. Read repository instructions and inspect the affected code and tests.
2. Reproduce the failure whenever practical. Record the command, inputs,
   observed result, expected result, environment, and error output.
3. Gather evidence with targeted logs, traces, assertions, or minimal examples.
   Do not guess a cause from the symptom alone.

## Diagnose and fix

1. Trace the evidence to the root cause and explain the causal chain.
2. Add a focused regression test (**RED**) that fails before the fix for the
   observed defect.
3. Apply the smallest correct fix (**GREEN**).
4. Refactor only when it improves the fix and validation remains green.

Preserve test integrity: do not remove, weaken, skip, trivialize, or alter an
expectation merely to hide the failure. Modify a test only if the requirement
changed or evidence shows it was wrong, and document that reason.

## Validate and report

- Run the regression test and the relevant broader test/build checks.
- Inspect the final diff for unrelated changes and generated artifacts.
- Report reproduction, evidence, root cause, fix, validation, and any remaining
  uncertainty. If reproduction was impossible, say so and explain the evidence
  supporting the diagnosis.
