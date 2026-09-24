# AI Skills

A small, curated collection of portable coding-agent skills for projects that
move between Claude Code and local Qwen/OpenCode.

The repository intentionally favors a compact workflow over a large generic
skill catalogue:

1. **Handover** prepares an existing project for a different coding agent.
2. **Implementation** delivers focused changes with meaningful tests.
3. **Debugging** finds and fixes defects from evidence.
4. **Sign-off** validates completed work, preserves reusable context, and
   creates a focused commit.

## Repository layout

```text
skills/
├── claude/
│   └── project-handover/
│       └── SKILL.md
└── opencode/
    ├── project-debugging/
    │   └── SKILL.md
    ├── project-implementation/
    │   └── SKILL.md
    └── project-signoff/
        └── SKILL.md
```

## Install in a project

Copy the desired skill directory into the target project's runtime-specific
skills directory. Keep each directory name and its `SKILL.md` unchanged.

```bash
# Claude Code
cp -R skills/claude/project-handover <project>/.claude/skills/

# Local Qwen through OpenCode
cp -R skills/opencode/project-implementation <project>/.opencode/skills/
cp -R skills/opencode/project-debugging <project>/.opencode/skills/
cp -R skills/opencode/project-signoff <project>/.opencode/skills/
```

For reusable personal skills rather than project-local ones, install them in
the equivalent global skills directory configured by the runtime.

## Contributing a skill

- One skill per directory, with the entry point named `SKILL.md`.
- Start every skill with YAML front matter containing a unique `name` and a
  concise `description` that makes its activation intent clear.
- Keep instructions specific, testable, and independent of a particular
  project unless the target runtime requires otherwise.
- Validate Markdown and front matter before committing.

## Public repository safety

This repository is intended to be public. Do not commit personal information,
account details, credentials, API keys, tokens, private URLs, local hostnames,
or copied logs and configuration from a real environment. Review
[SECURITY.md](SECURITY.md) before contributing and run:

```bash
python3 scripts/check_public_content.py
```

## Status

This repository currently contains the first Claude-to-local-Qwen workflow.
Additional skills should be added only when they address a recurring task that
is not already covered by this compact set.
