---
name: project-handover
description: Prepare an existing project for reliable continuation by another coding agent, especially a handover from Claude Code to local Qwen/OpenCode.
---

# Project Handover

Use this skill when transferring responsibility for an existing project to a
different coding agent.

## Inspect before documenting

1. Read repository guidance first (`AGENTS.md`, `CLAUDE.md`, README, build and
   test configuration, and any existing `HANDOFF.md`).
2. Inspect the source tree, current branch, working-tree status, recent commits,
   and the commands actually used to build, test, lint, format, and run it.
3. Verify claims against the source and commands. Clearly distinguish confirmed
   facts from assumptions or unverified risks.

## Create or refresh handover material

Create or update `HANDOFF.md` with:

- project purpose and high-level architecture;
- current state, completed work, and unfinished work;
- how to set up, build, test, and run the project;
- important module boundaries, invariants, conventions, and data formats;
- fragile areas, known bugs, risks, and relevant validation results;
- the next concrete task(s), including useful files and commands.

Create or refresh `AGENTS.md` only for durable repository-wide instructions:
coding conventions, validation expectations, safety constraints, and recurring
project commands. Do not put transient task status there.

## Baseline and readiness

1. Run the relevant available validation commands and record their outcomes.
2. Remove only clearly disposable generated artifacts; do not discard user work.
3. If authorized, make a focused baseline commit containing the handover
   documentation and any intended cleanup. Otherwise report what remains
   uncommitted.
4. End with a short receiver-oriented brief: what to read first, what works,
   what is uncertain, and the safest next step.

Do not claim the project is ready until the repository state, instructions, and
validation status have been checked.
