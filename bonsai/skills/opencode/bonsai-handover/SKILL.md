---
name: bonsai-handover
description: Write a compact handover or resume from one while verifying repository state and preserving the original scope.
---

# Handover
Read `bonsai-core` first.
For writing, create/update `HANDOFF.md` only when documentation changes are authorized. Otherwise return the same brief in the response. Target 250–400 words:
- Objective and mode: original request, acceptance criteria, explicit exclusions.
- State: branch/revision, task changes, pre-existing staged/unstaged/untracked work; mark unknown ownership.
- Evidence: confirmed behavior and exact commands/results. Keep hypotheses and blocked checks separate. Include unresolved failures and baseline status.
- Map: at most six relevant paths/symbols, verified environment/build/test commands, important target constraints.
- Next: one immediate action plus at most two subsequent steps and their stopping condition.
Do not copy the transcript, speculative bug catalog, credentials or personal machine paths. Use repository-relative paths and environment placeholders. Keep durable rules separate from transient status.
For resuming, read the brief, repository instructions and current status/diffs. Preserve remaining investigation budget and stopping rules; do not reset them after compaction. Treat a failed harness as unverified, not completed reproduction. Verify key claims against source and recent results; record discrepancies. Read only the next action's files. Resume the original mode; a handover or blank message does not authorize fixes, commits or broader work.
