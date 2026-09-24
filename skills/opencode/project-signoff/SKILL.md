---
name: project-signoff
description: Finish a coding task responsibly by checking consistency, validating the result, preserving reusable knowledge, and creating a focused commit.
---

# Project Sign-off

Use after implementation or debugging is complete.

## Check the work

1. Inspect the task scope, changed files, and final diff. Confirm the code,
   tests, docs, configuration, and public interfaces are consistent.
2. Run the relevant build, test, lint, format, or smoke-test commands. Record
   commands and outcomes; do not claim checks that were not run.
3. Remove only generated or temporary artifacts that are clearly safe to remove.
   Preserve user changes and unrelated work.
4. Check that no secrets, credentials, local paths, debug output, or accidental
   generated files are being committed.

## Preserve reusable knowledge

Promote durable, repository-wide knowledge to `AGENTS.md`: recurring commands,
constraints, conventions, or safety rules. Put current state, validation, open
risks, and next steps in `HANDOFF.md` when that context helps a future agent.
Avoid duplicating transient information in permanent guidance.

## Commit cleanly

1. Stage only files belonging to the completed task.
2. Review the staged diff.
3. Create a concise commit whose message describes the behavioral outcome.
4. Verify repository status after committing and report any remaining changes.

If committing is not authorized, complete every other sign-off step and provide
the precise files and commit message you would use.
