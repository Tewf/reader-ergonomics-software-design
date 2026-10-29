"""Tests of checks/local/decision_records.py: it fails where a record lacks a part the shape asks for, and stays
silent where it has them all.

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
