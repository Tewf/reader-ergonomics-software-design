"""Shared by the local checks: which documents declare which shape, and where a document's labelled parts start.

A document follows a shape of this repository when it carries a line `**Shape:**` linking the shape's file, as the
decision records do. The checks below find their documents that way, so they apply wherever the shapes are used. A
Shape line inside fenced code, as in a shape's skeleton, declares nothing.
This module has no NAME, so the runner loads it and skips it; each check puts its folder on sys.path to import it.
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import prose_only

SHAPE_LINE = re.compile(r"\*\*Shape:\*\*\s*\[[^\]]*\]\(([^)\s]+)\)")


def declared(root: Path, paths: list[str], shape_file: str) -> list[str]:
    """The markdown paths whose Shape line links shapes/<shape_file>."""
    found = []
    for path in paths:
        if not path.endswith((".md", ".qmd")):
            continue
        text = prose_only((root / path).read_text(encoding="utf-8", errors="replace"))  # a skeleton's line is not a declaration
        if any(link.split("#")[0].endswith(f"shapes/{shape_file}") or link.split("#")[0] == shape_file
               for link in SHAPE_LINE.findall(text)):
            found.append(path)
    return found


def labels(text: str, names: list[str]) -> dict[str, int]:
    """The first line of each named part: a heading '## Name' or a bold label '**Name.**' or '**Name:**'."""
    where = {}
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip().lstrip("- ").strip()
        for name in names:
            if name in where:
                continue
            if re.match(rf"#+\s*{re.escape(name)}\b", stripped, re.IGNORECASE) or \
               re.match(rf"\*\*{re.escape(name)}[.:]\*\*", stripped, re.IGNORECASE):
                where[name] = number
    return where


def section(text: str, start: int, stops: list[int]) -> list[str]:
    """The lines from a part's first line up to the next part."""
    lines = text.splitlines()
    end = min([stop for stop in stops if stop > start] or [len(lines) + 1])
    return lines[start - 1:end - 1]
