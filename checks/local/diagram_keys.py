"""Diagram keys: every diagram drawn as text has a key, and every arrow in it a label.

A diagram is a top-level fenced block whose info string is `mermaid` or `{mermaid}`, in any markdown file in scope; a
diagram inside another fence, such as a shape's skeleton, is not one. A run with no error guarantees, for each:
- a table whose first header cell is `Key` follows it, before the next heading;
- each arrow of a flowchart (`-->`, `---`, `-.->`, `==>`) carries a label, as `-->|label|` or `-- label -->`.
It does not judge that the key is complete or the labels clear (judgment), and reads only flowchart arrows; other
Mermaid diagram types are checked for their key alone. Time O(text).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import Finding, files_in_scope
from framework.prose import blocks

NAME = "diagram-keys"
EXACT = True

ARROW = re.compile(r"(-->|---|-\.->|==>)")
LABELLED = re.compile(r"(-->|---|-\.->|==>)\s*\|[^|]+\||--\s+[^->]+\s+-->|==\s+[^=>]+\s+==>|-\.\s+[^.]+\s+\.->")


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in files_in_scope(root, config, {".md", ".qmd"}):
        found = blocks((root / path).read_text(encoding="utf-8", errors="replace"))
        for index, block in enumerate(found):
            if block.kind != "fence" or block.info.strip().strip("{}") != "mermaid":
                continue
            after = []
            for later in found[index + 1:]:
                if later.kind == "heading":
                    break
                after.append(later)
            if not any(b.kind == "table" and re.match(r"\|\s*Key\s*\|", b.text.splitlines()[0], re.IGNORECASE) for b in after):
                findings.append(Finding(NAME, path, block.line, "a diagram with no key: add a table whose first header is Key"))
            if block.text.lstrip().startswith(("flowchart", "graph")):
                for offset, line in enumerate(block.text.splitlines(), 1):
                    if ARROW.search(line) and not LABELLED.search(line):
                        findings.append(Finding(NAME, path, block.line + offset, "an arrow with no label: say what it carries"))
    return findings
