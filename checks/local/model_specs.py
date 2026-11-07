"""Model specifications: a document declaring the model-specification shape has its parts, in order.

A document is in scope when its `**Shape:**` line links shapes/model-specification.md. A run with no error
guarantees, for each such document:
- the parts Problem, Sets and data, Variables, Objective, Constraints, Relaxation, Examples, Properties and Plan are
  all present, as a heading or a bold label;
- the Variables come before the Constraints (principle: define before use);
- every constraint line carries a quoted sentence, the rule of the statement it stands for (rule 1 of the shape);
- the Relaxation says exact or not exact (rule 3);
- the Examples hold a table with at least one row of instance and optimum.
It warns, as a heuristic, when the Examples have fewer than three rows, since the small cases come first and are
several. It does not judge that a constraint matches its sentence, that the relaxation's reason holds or that the
optimum is right. Time O(documents x size).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _shapes import declared, labels, section  # noqa: E402
from framework.check_api import Finding, files_in_scope  # noqa: E402

NAME = "model-specs"
EXACT = True

PARTS = ["Problem", "Sets and data", "Variables", "Objective", "Constraints", "Relaxation", "Examples", "Properties", "Plan"]
MIN_EXAMPLE_ROWS = 3  # PROVISIONAL: an empty instance, one element and an ordinary case at the least
SENTENCE = re.compile(r"[\"“«]")  # a constraint's sentence is quoted
VERDICT = re.compile(r"\b(not exact|exact)\b", re.IGNORECASE)


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in declared(root, files_in_scope(root, config, {".md", ".qmd"}), "model-specification.md"):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        where = labels(text, PARTS)
        missing = [part for part in PARTS if part not in where]
        if missing:
            findings.append(Finding(NAME, path, 1, f"a model specification lacks {', '.join(missing)}"))
        if "Variables" in where and "Constraints" in where and where["Variables"] > where["Constraints"]:
            findings.append(Finding(NAME, path, where["Variables"], "the Variables come after the Constraints: define them first"))
        stops = list(where.values())
        if "Constraints" in where:
            body = section(text, where["Constraints"], stops)[1:]
            items = [line for line in body if line.lstrip().startswith(("-", "*", "+"))]
            unsaid = [line for line in items if not SENTENCE.search(line)]
            if not items:
                findings.append(Finding(NAME, path, where["Constraints"], "the Constraints hold no list: one family per rule, each on its line"))
            elif unsaid:
                findings.append(Finding(NAME, path, where["Constraints"], f"{len(unsaid)} constraint(s) carry no quoted sentence: say which rule of the statement each stands for"))
        if "Relaxation" in where:
            body = " ".join(section(text, where["Relaxation"], stops))
            if not VERDICT.search(body):
                findings.append(Finding(NAME, path, where["Relaxation"], "the Relaxation says neither exact nor not exact"))
        if "Examples" in where:
            rows = [line for line in section(text, where["Examples"], stops)[1:] if line.strip().startswith("|")]
            data = [row for row in rows[2:]] if len(rows) >= 2 and set(rows[1].replace("|", "").strip()) <= set("-: ") else rows
            if not data:
                findings.append(Finding(NAME, path, where["Examples"], "the Examples hold no table of instances and optima"))
            elif len(data) < MIN_EXAMPLE_ROWS:
                findings.append(Finding(NAME, path, where["Examples"], f"only {len(data)} example(s): start with the small cases", "warning"))
    return findings
