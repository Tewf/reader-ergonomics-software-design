"""Algorithm specifications: a document declaring the algorithm-specification shape has its parts, in order.

A document is in scope when its `**Shape:**` line links shapes/algorithm-specification.md. A run with no error
guarantees, for each such document:
- the parts Problem, Interface, Contract, Technique, Steps, Invariants, Cost, Examples, Properties and Plan are all
  present, as a heading or a bold label;
- the Contract comes before the Steps (principle: contract before steps);
- the Steps hold code-like text, a fenced or an indented block, not prose only (principle: code-like steps);
- the Examples hold a table with at least one row of input and expected output (principle: examples and properties
  as tests).
It warns, as a heuristic, when the Examples have fewer than three rows, since edge cases come first and are several.
It does not judge that the contract is right, that the invariant holds or that the examples cover the edge cases.
Time O(documents x size).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _shapes import declared, labels, section  # noqa: E402
from framework.check_api import Finding, files_in_scope  # noqa: E402

NAME = "algorithm-specs"
EXACT = True

PARTS = ["Problem", "Interface", "Contract", "Technique", "Steps", "Invariants", "Cost", "Examples", "Properties", "Plan"]
MIN_EXAMPLE_ROWS = 3  # PROVISIONAL: empty input, a boundary and an ordinary case at the least


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in declared(root, files_in_scope(root, config, {".md", ".qmd"}), "algorithm-specification.md"):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        where = labels(text, PARTS)
        missing = [part for part in PARTS if part not in where]
        if missing:
            findings.append(Finding(NAME, path, 1, f"an algorithm specification lacks {', '.join(missing)}"))
        if "Contract" in where and "Steps" in where and where["Contract"] > where["Steps"]:
            findings.append(Finding(NAME, path, where["Contract"], "the Contract comes after the Steps: state it first"))
        stops = list(where.values())
        if "Steps" in where:
            body = section(text, where["Steps"], stops)[1:]
            if not any(line.startswith(("    ", "\t", "```", "~~~")) for line in body):
                findings.append(Finding(NAME, path, where["Steps"], "the Steps hold no code-like block: give them as constrained pseudocode"))
        if "Examples" in where:
            rows = [line for line in section(text, where["Examples"], stops)[1:] if line.strip().startswith("|")]
            data = [row for row in rows[2:]] if len(rows) >= 2 and set(rows[1].replace("|", "").strip()) <= set("-: ") else rows
            if not data:
                findings.append(Finding(NAME, path, where["Examples"], "the Examples hold no table of inputs and expected outputs"))
            elif len(data) < MIN_EXAMPLE_ROWS:
                findings.append(Finding(NAME, path, where["Examples"], f"only {len(data)} example(s): start with the edge cases", "warning"))
    return findings
