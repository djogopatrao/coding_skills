#!/usr/bin/env python3
"""Fail when tracked repository content looks unsafe for public publication."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


FORBIDDEN_FILENAMES = {
    ".env",
    "id_ed25519",
    "id_rsa",
    ".netrc",
    "credentials.json",
    "service-account.json",
}

FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}

PATTERNS = {
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(
        r"\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"
    ),
    "OpenAI API key": re.compile(r"\bsk(?:-proj)?-[A-Za-z0-9_-]{20,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "private key block": re.compile(r"-----BEGIN(?: [A-Z]+)* PRIVATE KEY-----"),
    "credential-bearing connection string": re.compile(
        r"\b(?:mongodb(?:\+srv)?|postgres(?:ql)?|mysql|redis)://[^\s/:@]+:[^\s@]+@"
    ),
    "likely assigned secret": re.compile(
        r"\b(?:api[_-]?key|api[_-]?token|secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}"
    ),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "Brazilian CPF": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], check=True, capture_output=True
    )
    return [Path(item.decode()) for item in result.stdout.split(b"\0") if item]


def main() -> int:
    findings: list[str] = []
    for path in tracked_files():
        name = path.name.lower()
        if name in FORBIDDEN_FILENAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"{path}: prohibited credential-like filename")
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{path}: non-text tracked file requires manual review")
            continue

        for line_number, line in enumerate(content.splitlines(), start=1):
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append(f"{path}:{line_number}: possible {label}")

    if findings:
        print("Public-repository safety check failed:", file=sys.stderr)
        print("\n".join(findings), file=sys.stderr)
        return 1

    print("Public-repository safety check passed: no prohibited files or common sensitive patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
