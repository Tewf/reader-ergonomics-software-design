"""Judgment citations: every answer in checks/judgments.toml quotes its own file, and every quote is really there.

Why: on 2026-10-29 this repository's 68 answers were found to be written one per kind of question, so an answer
could give a reason that was absent from the file it answered for. A program cannot judge an answer, but it can
check that the answer is about the file: an answer must hold at least one quotation, in double quotes or backticks,
and each quotation must occur in the answered file, or name an entry of the answered folder.

What a run with no error guarantees, for every [[answer]] whose file still exists:
- the answer holds at least one quotation of two characters or more;
- each quotation occurs in the file's text (ignoring case and runs of white space), or, for a folder, names one of
  its entries, or names a file that exists beside the answered file or at the repository's root;
- each "line N" it cites is a line of the file.

What it does not guarantee: that the quotation supports the answer, or that the answer is right (judgment).
An answer whose file is gone is skipped: the standard's judgment step already asks its question again.
Time O(answers x file size).
"""
from __future__ import annotations

import re
import tomllib
from pathlib import Path

from framework.check_api import Finding

NAME = "judgment-citations"
EXACT = True

QUOTE = re.compile(r'"([^"\n]{2,})"|`([^`\n]{2,})`|“([^”\n]{2,})”')
LINE_REF = re.compile(r"\bline (\d+)\b")


def normalised(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def answer_lines(text: str) -> list[int]:
    """The line of each [[answer]] header, in file order, so a finding points at its block."""
    return [n for n, line in enumerate(text.splitlines(), 1) if line.strip() == "[[answer]]"]


def quote_found(quote: str, target: Path, root: Path) -> bool:
    if target.is_dir():
        if any(entry.name == quote for entry in target.iterdir()):
            return True
    else:
        if normalised(quote) in normalised(target.read_text(encoding="utf-8", errors="replace")):
            return True
    beside = target if target.is_dir() else target.parent
    return (beside / quote).exists() or (root / quote).exists()


def check(root: Path, config: dict) -> list[Finding]:
    answers_path = config.get("judgment", {}).get("answers", "checks/judgments.toml")
    file = root / answers_path
    if not file.is_file():
        return []
    text = file.read_text(encoding="utf-8")
    try:
        answers = tomllib.loads(text).get("answer", [])
    except tomllib.TOMLDecodeError as error:
        return [Finding(NAME, answers_path, 1, f"the answers file is not valid TOML: {error}")]
    lines = answer_lines(text)
    findings = []
    for index, answer in enumerate(answers):
        line = lines[index] if index < len(lines) else 1
        target = root / answer.get("path", "")
        if not answer.get("path") or not target.exists():
            continue
        reply = answer.get("answer", "")
        quotes = [next(group for group in match.groups() if group) for match in QUOTE.finditer(reply)]
        if not quotes:
            findings.append(Finding(NAME, answers_path, line,
                                    f"the answer for {answer['path']} quotes nothing from it: cite a phrase in quotes or backticks"))
            continue
        for quote in quotes:
            if not quote_found(quote, target, root):
                findings.append(Finding(NAME, answers_path, line,
                                        f"the answer for {answer['path']} quotes {quote!r}, which is not in that file"))
        if target.is_file():
            length = len(target.read_text(encoding="utf-8", errors="replace").splitlines())
            for number in LINE_REF.findall(reply):
                if not 1 <= int(number) <= length:
                    findings.append(Finding(NAME, answers_path, line,
                                            f"the answer for {answer['path']} cites line {number}; the file has {length}"))
    return findings
