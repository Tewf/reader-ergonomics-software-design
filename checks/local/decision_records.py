"""Decision records: every record in decisions/ has the parts the decision-record shape asks for.

A record is a file `decisions/NNNN-<name>.md`. A run with no error guarantees, for each record:
- its title is `# NNNN. <title>`, with the number of its file name;
- it states the decision in a line opening `**Decision.**`;
- it names its shape in a line `**Shape:**` that links `shapes/decision-record.md`;
- it has a `**Status:**` line.

It does not check that the decision is right, that the options are complete, or that a superseded record links
forward (judgment). Files in decisions/ not named NNNN-*.md (the folder's README) are not records. Time O(records).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import Finding

NAME = "decision-records"
EXACT = True

RECORD = re.compile(r"^(\d{4})-[a-z0-9-]+\.md$")
SHAPE_LINK = re.compile(r"\*\*Shape:\*\*\s*\[[^\]]+\]\([^)]*shapes/decision-record\.md\)")


def check(root: Path, config: dict) -> list[Finding]:
    folder = root / "decisions"
    if not folder.is_dir():
        return []
    findings = []
    for path in sorted(folder.iterdir()):
        match = RECORD.match(path.name)
        if not match:
            continue
        where = f"decisions/{path.name}"
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        title = next((line for line in lines if line.strip()), "")
        if not title.startswith(f"# {match.group(1)}. "):
            findings.append(Finding(NAME, where, 1, f"the title should open '# {match.group(1)}. ', the record's number"))
        text = "\n".join(lines)
        for part, pattern in (("a '**Decision.**' line", r"^\*\*Decision\.\*\*"), ("a '**Status:**' line", r"\*\*Status:\*\*")):
            if not re.search(pattern, text, re.MULTILINE):
                findings.append(Finding(NAME, where, 1, f"a decision record needs {part}"))
        if not SHAPE_LINK.search(text):
            findings.append(Finding(NAME, where, 1, "a decision record names its shape: a '**Shape:**' line linking shapes/decision-record.md"))
    return findings
