---
name: bonsai-signoff
description: Review completed changes, validation, documentation and task-owned diffs; commit only when authorized.
---

# Sign-off
Read `bonsai-core` first.
1. Compare acceptance criteria with final code, tests and interfaces. Verify new assertions access actual return types and distinguish incorrect behavior; inspect tested input paths rather than relying on a green count. Review unstaged and staged diffs against the initial working-tree snapshot. Identify task-owned hunks and unrelated work.
2. Verify checks cover the changed behavior. Reuse current results; rerun only after relevant edits or unresolved failures. Record exact commands, exit status, failures and checks not run. Never claim full-suite or target validation from a subset or host build.
3. Update only docs affected by the change. Put durable commands/invariants in repository guidance; put transient status in handover. Check the intended diff for secrets, debug output and accidental generated files. Remove only your confirmed disposable artifacts.
4. If committing is authorized, stage explicit task-owned paths/hunks, inspect the staged diff, commit and verify status. If mixed changes cannot be separated safely, leave them unstaged and explain. Never use `git add .` or `git commit -a` to sweep up work.
5. Otherwise leave the reviewed changes available and suggest a commit message. Report behavior, validation, remaining changes and blockers. Do not push, publish or release without authorization.
A passing test subset is not proof that the entire project is ready.
