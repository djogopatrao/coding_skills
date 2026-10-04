# Public-repository security policy

This repository is public by design. Every tracked file and every commit must
be safe to publish without access restrictions.

## Never commit

- passwords, API keys, tokens, cookies, SSH keys, certificates, private keys,
  connection strings, or credential files;
- personal information such as names tied to private context, email addresses,
  telephone numbers, government identifiers, addresses, or account details;
- internal hostnames, private IP addresses, private repository URLs, local
  filesystem paths, infrastructure identifiers, or private configuration;
- copied terminal output, screenshots, logs, database extracts, or chat
  transcripts unless they have been deliberately redacted and reviewed.

Use clearly fictional placeholders instead, for example `YOUR_API_KEY`,
`example.invalid`, `<project>`, and `<email-placeholder>`.

## Required check before committing or publishing

Run the repository check and inspect the staged diff:

```bash
python3 scripts/check_public_content.py
git diff --cached --check
git diff --cached
```

The automated check catches common credential patterns and prohibited filenames.
It is a safety net, not a substitute for human review. If there is any doubt
about whether a detail is private, do not commit it.

## If sensitive content is committed

Stop before pushing. Remove the content from the file and rewrite the affected
local commit(s) before publication. If it has already been pushed, revoke the
credential immediately and follow the hosting provider's guidance for removing
the exposed history.
