"""Tests of the local checks in checks/local/: each fails where a document lacks a part its shape asks for, and stays
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

    def test_a_shape_line_inside_a_skeleton_fence_declares_nothing(self) -> None:
        skeleton = "# Shape: algorithm specification\n\n```markdown\n# <Name>\n\n**Shape:** [algorithm specification](shapes/algorithm-specification.md)\n```\n"
        self.assertEqual(self.run_check(specs, "shape.md", skeleton), [])

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
