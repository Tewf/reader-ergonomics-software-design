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

GOOD_RECORD = ("# 0001: Pin the links\n\n**Decision:** Links name the commit.\n\n"
               "**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md).\n")


class DecisionRecords(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        (self.root / "decisions").mkdir()
        self.index("0001-pin-the-links.md", "0002-move-the-pin.md")

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def index(self, *names: str) -> None:
        rows = "".join(f"| [{name[:4]}]({name}) |\n" for name in names)
        (self.root / "decisions" / "README.md").write_text(f"# Decisions\n\n{rows}", encoding="utf-8")

    def found(self, name: str, text: str, kind: str = "") -> list[str]:
        (self.root / "decisions" / name).write_text(text, encoding="utf-8")
        return [finding.message for finding in records.check(self.root, {}) if not kind or finding.kind == kind]

    def test_a_complete_record_passes(self) -> None:
        self.assertEqual(self.found("0001-pin-the-links.md", GOOD_RECORD), [])

    def test_the_readme_is_not_a_record(self) -> None:
        self.assertEqual(self.found("README.md", "# Decisions\n"), [])

    def test_a_title_with_another_number_fails(self) -> None:
        found = self.found("0001-pin-the-links.md", GOOD_RECORD.replace("# 0001:", "# 0002:"))
        self.assertEqual(len(found), 1)
        self.assertIn("'# 0001: '", found[0])

    def test_a_gap_in_the_numbers_fails(self) -> None:
        found = self.found("0002-move-the-pin.md", GOOD_RECORD.replace("# 0001:", "# 0002:"))
        self.assertEqual(len(found), 1)
        self.assertIn("0001 was due", found[0])

    def test_a_record_the_readme_does_not_link_fails(self) -> None:
        self.index("0002-move-the-pin.md")
        found = self.found("0001-pin-the-links.md", GOOD_RECORD)
        self.assertEqual(found, ["the README does not link 0001-pin-the-links.md"])

    def test_a_folder_without_a_readme_fails(self) -> None:
        (self.root / "decisions" / "README.md").unlink()
        found = self.found("0001-pin-the-links.md", GOOD_RECORD)
        self.assertEqual(len(found), 1)
        self.assertIn("needs a README", found[0])

    def test_a_decision_not_first_fails(self) -> None:
        text = GOOD_RECORD.replace("**Decision:** Links name the commit.\n\n", "Some context first.\n\n**Decision:** Links name the commit.\n\n")
        found = self.found("0001-pin-the-links.md", text)
        self.assertEqual(len(found), 1)
        self.assertIn("rule 2", found[0])

    def test_a_status_without_its_word_or_date_fails_twice(self) -> None:
        found = self.found("0001-pin-the-links.md", GOOD_RECORD.replace("accepted, 2026-10-29.", "in force."))
        self.assertEqual(len(found), 2)

    def test_a_superseded_record_without_its_successor_fails(self) -> None:
        found = self.found("0001-pin-the-links.md", GOOD_RECORD.replace("accepted, 2026-10-29.", "superseded, 2026-10-29."))
        self.assertEqual(len(found), 1)
        self.assertIn("rule 4", found[0])

    def test_a_status_linking_a_missing_record_fails(self) -> None:
        text = GOOD_RECORD.replace("accepted, 2026-10-29.", "superseded by [0002](0002-move-the-pin.md), 2026-10-29.")
        found = self.found("0001-pin-the-links.md", text)
        self.assertEqual(found, ["the status links 0002-move-the-pin.md, which is not in decisions/"])

    def test_consequences_without_a_bad_line_ask_a_question(self) -> None:
        text = GOOD_RECORD + "\n## Consequences\n\n- Good: the links hold.\n\n## See also\n"
        self.assertEqual(self.found("0001-pin-the-links.md", text, "error"), [])
        asked = self.found("0001-pin-the-links.md", text, "judgment")
        self.assertEqual(len(asked), 1)
        self.assertIn("rule 3", asked[0])

    def test_consequences_with_a_bad_line_ask_nothing(self) -> None:
        text = GOOD_RECORD + "\n## Consequences\n\n- Good: the links hold.\n- Bad: long addresses.\n\n## See also\n"
        self.assertEqual(self.found("0001-pin-the-links.md", text), [])

    def test_a_record_without_its_shape_line_fails(self) -> None:
        found = self.found("0001-pin-the-links.md", GOOD_RECORD.replace(" **Shape:** [decision record](../shapes/decision-record.md).", ""))
        self.assertEqual(len(found), 1)
        self.assertIn("names its shape", found[0])

    def test_a_record_without_decision_or_status_fails_twice(self) -> None:
        text = GOOD_RECORD.replace("**Decision:**", "Decision:").replace("**Status:**", "Status:")
        self.assertEqual(len(self.found("0001-pin-the-links.md", text)), 2)

    def test_no_decisions_folder_means_nothing_to_check(self) -> None:
        shutil.rmtree(self.root / "decisions")
        self.assertEqual(records.check(self.root, {}), [])


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPOSITORY / "checks" / "local" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


specs, docs, keys = load("algorithm_specs"), load("design_docs"), load("diagram_keys")

SPEC = """# Lower bound

**Problem.** Find the first position.

- **Shape:** [algorithm specification](../shapes/algorithm-specification.md).

**Interface.** a, x.

**Contract.** Precondition: sorted.

**Technique.** Decrease and conquer.

**Steps.**

    lo <- 0
    return lo

**Invariants.** lo <= hi.

**Cost.** O(log n).

**Examples.**

| Input | Expected |
|---|---|
| [], 5 | 0 |
| [1], 0 | 0 |
| [1], 2 | 1 |

**Properties.** i counts the smaller values.

**Plan.** Tests first.
"""

DOC = """# Pin the links

- **Decision asked.** Should the links name the commit?
- **Status.** Accepted.
- **Shape:** [design document](../shapes/design-document.md).

## Motivation
Links break.
## Goals and non-goals
Goal: agree.
## Design
Name the commit.
## Alternatives
| Option | Consequences | Why it lost |
|---|---|---|
| master | breaks | silent |
## Consequences
- Risks: forgetting the links.
## Feasibility and plan
One commit.
## Open questions
None.
"""

DIAGRAM = """# A view

```mermaid
flowchart LR
    a["Push"] -->|"triggers"| b["Checks"]
```

| Key | Meaning |
|---|---|
| box | a job |
"""


class LocalShapeChecks(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def run_check(self, module, name: str, text: str) -> list[tuple[str, str]]:
        (self.root / name).write_text(text, encoding="utf-8")
        return [(finding.kind, finding.message) for finding in module.check(self.root, {})]

    def test_a_complete_specification_passes(self) -> None:
        self.assertEqual(self.run_check(specs, "spec.md", SPEC), [])

    def test_a_document_without_the_shape_line_is_not_checked(self) -> None:
        self.assertEqual(self.run_check(specs, "spec.md", SPEC.replace("**Shape:**", "Shape:")), [])

    def test_steps_before_the_contract_fail(self) -> None:
        moved = SPEC.replace("**Contract.** Precondition: sorted.\n\n", "").replace("**Plan.**", "**Contract.** Precondition: sorted.\n\n**Plan.**")
        self.assertTrue(any("comes after the Steps" in m for _, m in self.run_check(specs, "spec.md", moved)))

    def test_prose_steps_fail(self) -> None:
        prose = SPEC.replace("    lo <- 0\n    return lo\n", "Set lo to zero and return it.\n")
        self.assertTrue(any("no code-like block" in m for _, m in self.run_check(specs, "spec.md", prose)))

    def test_too_few_examples_warn(self) -> None:
        few = SPEC.replace("| [1], 0 | 0 |\n| [1], 2 | 1 |\n", "")
        self.assertIn(("warning", "only 1 example(s): start with the edge cases"), self.run_check(specs, "spec.md", few))

    def test_a_complete_design_document_passes(self) -> None:
        self.assertEqual(self.run_check(docs, "doc.md", DOC), [])

    def test_a_design_document_not_opening_with_the_decision_asked_fails(self) -> None:
        swapped = DOC.replace("- **Decision asked.** Should the links name the commit?\n", "")
        self.assertTrue(any("Decision asked" in m for _, m in self.run_check(docs, "doc.md", swapped)))

    def test_consequences_without_a_failure_warn(self) -> None:
        calm = DOC.replace("- Risks: forgetting the links.", "- Good: stable links.")
        self.assertIn("warning", [kind for kind, _ in self.run_check(docs, "doc.md", calm)])

    def test_alternatives_without_a_table_fail(self) -> None:
        bare = DOC.replace("| Option | Consequences | Why it lost |\n|---|---|---|\n| master | breaks | silent |\n", "Master breaks.\n")
        self.assertTrue(any("no table" in m for _, m in self.run_check(docs, "doc.md", bare)))

    def test_a_keyed_labelled_diagram_passes(self) -> None:
        self.assertEqual(self.run_check(keys, "view.md", DIAGRAM), [])

    def test_a_diagram_without_a_key_fails(self) -> None:
        bare = DIAGRAM.split("| Key |")[0]
        self.assertTrue(any("no key" in m for _, m in self.run_check(keys, "view.md", bare)))

    def test_an_unlabelled_arrow_fails(self) -> None:
        unlabelled = DIAGRAM.replace('-->|"triggers"|', "-->")
        self.assertTrue(any("no label" in m for _, m in self.run_check(keys, "view.md", unlabelled)))

    def test_a_diagram_inside_a_skeleton_fence_is_not_checked(self) -> None:
        skeleton = "# Shape\n\n````markdown\n```mermaid\nflowchart LR\n    a --> b\n```\n````\n"
        self.assertEqual(self.run_check(keys, "shape.md", skeleton), [])


if __name__ == "__main__":
    unittest.main()
