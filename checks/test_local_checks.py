"""Tests of checks/local/judgment_citations.py: it fails where an answer is not about its file, and stays silent
where it is.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""),
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
SPEC = importlib.util.spec_from_file_location("judgment_citations",
                                              REPOSITORY / "checks" / "local" / "judgment_citations.py")
citations = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(citations)

NOTE = "# A note\n\nThe pool of sources is counted and scored.\nA second line.\n"


def answer(path: str, text: str, root: Path | None = None, stale: bool = False) -> str:
    """One [[answer]] block; its hash is the file's own unless the answer is meant to be stale."""
    file = "000000000000"
    if root is not None and not stale:
        file = citations.current_hash(root / path)
    return (f'[[answer]]\ncheck = "logical-lines"\npath = "{path}"\nquestion = "q"\nfile = "{file}"\n'
            f'answer = "{text}"\n\n')


class JudgmentCitations(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        (self.root / "evidence").mkdir()
        (self.root / "checks").mkdir()
        (self.root / "evidence" / "note.md").write_text(NOTE, encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def run_with(self, *answers: str) -> list[str]:
        (self.root / "checks" / "judgments.toml").write_text("".join(answers), encoding="utf-8")
        return [finding.message for finding in citations.check(self.root, {})]

    def test_a_quotation_found_in_the_file_passes(self) -> None:
        self.assertEqual(self.run_with(answer("evidence/note.md", root=self.root, text="One role: `counted and scored`. It stays whole.")), [])

    def test_the_match_ignores_case_and_white_space(self) -> None:
        self.assertEqual(self.run_with(answer("evidence/note.md", root=self.root, text="Yes: `THE  POOL of sources`.")), [])

    def test_an_answer_with_no_quotation_fails(self) -> None:
        found = self.run_with(answer("evidence/note.md", root=self.root, text="One role: the pool. It stays whole."))
        self.assertEqual(len(found), 1)
        self.assertIn("quotes nothing", found[0])

    def test_a_quotation_absent_from_the_file_fails(self) -> None:
        found = self.run_with(answer("evidence/note.md", root=self.root, text="Reference: `design, specify, check, decide`."))
        self.assertEqual(len(found), 1)
        self.assertIn("not in that file", found[0])

    def test_a_line_past_the_end_fails(self) -> None:
        found = self.run_with(answer("evidence/note.md", root=self.root, text="See line 99: `A second line`."))
        self.assertEqual(len(found), 1)
        self.assertIn("cites line 99", found[0])

    def test_a_folder_answer_may_name_an_entry(self) -> None:
        self.assertEqual(self.run_with(answer("evidence", root=self.root, text="It stays: it holds `note.md`.")), [])

    def test_an_answer_for_a_vanished_file_is_skipped(self) -> None:
        self.assertEqual(self.run_with(answer("evidence/gone.md", "No quotation at all.")), [])

    def test_an_invalid_answers_file_is_reported_not_skipped(self) -> None:
        found = self.run_with("[[answer]\nbroken")
        self.assertEqual(len(found), 1)
        self.assertIn("not valid TOML", found[0])

    def test_a_stale_answer_is_skipped(self) -> None:
        self.assertEqual(self.run_with(answer("evidence/note.md", "Quotes `nothing that is there`.", self.root, stale=True)), [])

    def test_no_answers_file_means_nothing_to_check(self) -> None:
        self.assertEqual([f.message for f in citations.check(self.root, {})], [])


SPEC_RECORDS = importlib.util.spec_from_file_location("decision_records",
                                                      REPOSITORY / "checks" / "local" / "decision_records.py")
records = importlib.util.module_from_spec(SPEC_RECORDS)
SPEC_RECORDS.loader.exec_module(records)

GOOD_RECORD = ("# 0001. Pin the links\n\n**Decision.** Links name the commit.\n\n"
               "- **Shape:** [decision record](../shapes/decision-record.md).\n- **Status:** accepted, 2026-10-29.\n")


class DecisionRecords(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        (self.root / "decisions").mkdir()

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def found(self, name: str, text: str) -> list[str]:
        (self.root / "decisions" / name).write_text(text, encoding="utf-8")
        return [finding.message for finding in records.check(self.root, {})]

    def test_a_complete_record_passes(self) -> None:
        self.assertEqual(self.found("0001-pin-the-links.md", GOOD_RECORD), [])

    def test_the_readme_is_not_a_record(self) -> None:
        self.assertEqual(self.found("README.md", "# Decisions\n"), [])

    def test_a_title_with_another_number_fails(self) -> None:
        found = self.found("0002-pin-the-links.md", GOOD_RECORD)
        self.assertEqual(len(found), 1)
        self.assertIn("'# 0002. '", found[0])

    def test_a_record_without_its_shape_line_fails(self) -> None:
        found = self.found("0001-pin-the-links.md", GOOD_RECORD.replace("- **Shape:** [decision record](../shapes/decision-record.md).\n", ""))
        self.assertEqual(len(found), 1)
        self.assertIn("names its shape", found[0])

    def test_a_record_without_decision_or_status_fails_twice(self) -> None:
        text = GOOD_RECORD.replace("**Decision.**", "Decision:").replace("**Status:**", "Status:")
        self.assertEqual(len(self.found("0001-pin-the-links.md", text)), 2)

    def test_no_decisions_folder_means_nothing_to_check(self) -> None:
        shutil.rmtree(self.root / "decisions")
        self.assertEqual(records.check(self.root, {}), [])


if __name__ == "__main__":
    unittest.main()
