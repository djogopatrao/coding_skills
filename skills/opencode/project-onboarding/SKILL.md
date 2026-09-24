---
name: project-onboarding
description: Take over an existing project from a Claude Code handover by verifying repository reality, absorbing durable context, and preparing a safe first task in OpenCode.
---

# Project Onboarding

Use this skill when beginning work in OpenCode after Claude Code, another
agent, or a previous session prepared the project for handover.

## Establish the repository facts

1. Read `AGENTS.md`, `HANDOFF.md`, README, architecture notes, build and test
   configuration, and any task-specific documents named by the handover.
2. Inspect the current branch, working-tree status, recent commits, source
   tree, tests, and relevant interfaces. Preserve unrelated or uncommitted
   work; do not clean or reset it merely to create a tidy starting point.
3. Identify the actual commands for setup, build, test, lint, format, and run.
   Prefer commands verified from project configuration over instructions that
   have not been checked recently.

## Audit the handover against reality

1. Treat `HANDOFF.md` as useful evidence, not as unquestioned truth. Verify
   its claims about architecture, completed work, unfinished work, invariants,
   data formats, risks, and named files against the repository.
2. Run the smallest relevant validation commands before editing when practical.
   Record what passed, failed, or could not be run and why.
3. Look for discrepancies: uncommitted changes, missing files, stale commands,
   broken tests, undocumented configuration, or a next task that conflicts
   with the current code.
4. Clearly separate confirmed facts, reasonable inferences, and open
   questions. Do not invent missing context or silently continue through a
   design-critical uncertainty.

## Form the first safe task

1. Summarize the verified project state, current task, relevant boundaries,
   validation baseline, risks, and the smallest safe next step.
2. If the handover is stale or incomplete, update `HANDOFF.md` only with
   source-backed corrections that will help the next agent. Put durable,
   repository-wide instructions in `AGENTS.md`, not transient task state.
3. Ask for direction when a discrepancy materially changes the design or the
   intended next task. Otherwise proceed with `project-implementation` or
   `project-debugging` as appropriate.

## Handover boundary

The Claude-side `project-handover` skill prepares and documents the transfer.
This OpenCode skill receives it: it audits the evidence, establishes a trusted
baseline, and prevents the new agent from treating stale documentation as fact.

Do not begin production edits until the relevant handover claims, repository
state, and validation baseline have been checked.
