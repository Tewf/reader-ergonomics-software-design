"""Design documents: a document declaring the design-document shape opens with the decision asked, has its parts, and
names how it fails.

A document is in scope when its `**Shape:**` line links shapes/design-document.md. A run with no error guarantees, for
each such document:
- the first labelled part after the title is the Decision asked (principle: the decision asked comes first);
- the parts Motivation, Goals and non-goals, Design, Alternatives, Consequences, Feasibility and plan and Open
  questions are present, as headings;
- the Alternatives hold a table, the options that lost with why (principle: keep the options that lost).
It warns, as a heuristic, when the Consequences never mention a failure, a risk or an error: the principle "design
the failure paths" asks that they be named. Whether the failure handling is adequate is judgment.
Time O(documents x size).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _shapes import declared, labels, section  # noqa: E402
from framework.check_api import Finding, files_in_scope  # noqa: E402

NAME = "design-docs"
EXACT = True

PARTS = ["Motivation", "Goals and non-goals", "Design", "Alternatives", "Consequences", "Feasibility and plan", "Open questions"]
FAILURE_WORDS = re.compile(r"\b(fail\w*|risk\w*|error\w*|outage\w*|break\w*|crash\w*)\b", re.IGNORECASE)


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in declared(root, files_in_scope(root, config, {".md", ".qmd"}), "design-document.md"):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        first = next((n for n, line in enumerate(lines, 1)
                      if re.match(r"\s*(-\s*)?(\*\*[^*]+[.:]\*\*|#{2,}\s)", line)), 0)
        if not first or not re.search(r"decision asked", lines[first - 1], re.IGNORECASE):
            findings.append(Finding(NAME, path, first or 1, "the first part after the title should be the Decision asked"))
        where = labels(text, PARTS)
        missing = [part for part in PARTS if part not in where]
        if missing:
            findings.append(Finding(NAME, path, 1, f"a design document lacks {', '.join(missing)}"))
        stops = list(where.values())
        if "Alternatives" in where and not any(line.strip().startswith("|") for line in section(text, where["Alternatives"], stops)):
            findings.append(Finding(NAME, path, where["Alternatives"], "the Alternatives hold no table of the options and why each lost"))
        if "Consequences" in where and not FAILURE_WORDS.search("\n".join(section(text, where["Consequences"], stops))):
            findings.append(Finding(NAME, path, where["Consequences"], "the Consequences name no failure, risk or error: say how it fails", "warning"))
    return findings
