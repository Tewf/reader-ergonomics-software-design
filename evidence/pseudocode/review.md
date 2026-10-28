# Review

Surveys first, then the seminal experiments, then forward citations, then practice.

## 1. Format comparisons: flowchart, PDL, pseudocode, prose

Surveys:

- Waddel 1988: a survey of empirical studies of graphical representations of algorithms. Its abstract reads the flowchart evidence as questionable and, in some studies, a hindrance (secondary).
- Wyrich 2023: a mapping study of 95 code comprehension experiments, 1979-2019. It is the map of how such studies are built (see section 2).
- Boehm-Davis 1983: a four-year programme report that summarises four experiments on documentation formats.

Seminal experiments:

- Shneiderman 1977: controlled experiments on detailed flowcharts for composing, understanding, debugging and modifying programs. No significant difference between flowchart and no-flowchart groups (abstract; secondary).
- Brooke 1980: flowcharts did not raise the number of correct fault identifications; they may clarify conditionals without improving understanding of the logic (abstract; secondary).
- Boehm-Davis 1983, symbology (prose, constrained language, ideogram) crossed with spatial arrangement (sequential, branching, hierarchical):
  - Experiment 1: 72 professional programmers answered tracing questions from documentation alone. Forward and backward tracing were faster from PDL or ideograms than from prose. Input-output questions showed no difference.
  - Experiment 2: 36 professionals completed about fifteen missing lines of code. Mean time was 29.7 minutes from prose, 20.5 from PDL, 23.9 from ideograms. Mean errors were 2.4, 0.8 and 1.4.
  - Experiment 3: 36 professionals found three seeded errors per program. Mean time was 18.7 minutes from prose, 14.5 from PDL, 14.2 from ideograms.
  - Experiment 4 replaced ideograms with abbreviated English that used the code's variable names. The prose penalty shrank, so part of it was variable naming, not form.
  - Preference: PDL was the most preferred symbology; branching was the most preferred arrangement.
- Ramsey 1983: PDL against flowcharts for detailed design. PDL designs were more detailed; flowchart designs were more abbreviated. When equivalent designs were shown in both forms, comprehension did not differ (abstract; secondary).
- Scanlan 1989: structured flowcharts against pseudocode on three algorithms, five measures (time, errors, confidence, answering time, looks). The abstract reports flowcharts ahead, even on the simplest algorithm (secondary).
- Scanlan 1988: six replications with 193 data structures students; preference for flowcharts ranged from 75.1% to 89.1% (abstract; secondary).

Forward citations of these:

- Glorfeld 1988: novices composing an algorithm with pseudocode more often produced a working one than with flowcharts (abstract; secondary).
- Andrzejewska 2015: eye tracking of pseudocode and flowchart variants; formal programming-language notation was a practical difficulty even for simple tasks (abstract; secondary).
- Katona 2022: interpreting a flowchart gave longer fixations, more fixations and larger pupils than a Nassi-Shneiderman diagram (abstract; secondary).
- Hendrix 2002: control structure diagrams added to source code improved student comprehension of one module (abstract; secondary).
- Ensmenger 2016: a history of the flowchart as a negotiated design document.
- Curtis 1989: named in the brief as a documentation-format study. This search found no abstract and the paper was not read.

## 2. Notation theory, layout and the shape of the evidence

- Green 1996: the cognitive dimensions framework, a vocabulary for comparing notations (title and framing only; the paper was not read).
- Green 1992: visual programs were not uniformly easier than textual ones; the structure of the information mattered (abstract only).
- Petre 1995: the differences lie less in textual against visual than in how far a notation supports conventions experts expect (abstract; secondary).
- Soloway 1984: a paper on the programming knowledge of experts, cited here for the idea of discourse rules (not read; secondary).
- Shaft 2006: cognitive fit between representation and task (title only; not read).
- Larkin 1987: diagrams help when they make inferences easy to see; the general principle is linked in the README.
- Wyrich 2023 numbers:
  - 53.7% of the 95 experiments used only students.
  - The authors found one replication that met their inclusion criteria.
  - Pseudocode appears once in the tally of stimulus languages.
- Layout of the text itself:
  - Bauer 2019: 22 participants, Java snippets, no indentation effect found; a non-exact replication of an earlier study.
  - Hanenberg 2024: 27 participants, a large effect of indentation on reading time of if-statements (non-indented took 2.13 times as long).

## 3. Design languages and refinement

- Caine 1975: PDL, the design language for describing a program before coding it.
- Wirth 1971: stepwise refinement; the program text is refined from prose-like steps to code.
- Boehm-Davis 1983 and Ramsey 1983 (section 1) are the experimental tests of the PDL idea.

## 4. Education and exam boards

- AP Computer Science Principles (College Board 2025): a reference sheet defines the text notation, with an arrow for assignment, 1-based lists, and a block twin for each text statement.
- OCR GCSE J277 (OCR 2026):
  - All code in papers uses the OCR Exam Reference Language.
  - Where a code answer is required, answers in pseudocode or natural English get no marks.
  - Design questions may be answered in pseudocode, flowcharts or prose; minor syntax errors are not penalised.
- Cambridge International AS and A Level 9618 (Cambridge 2024): a pseudocode guide fixes monospaced font, three-space indentation, upper-case keywords, mixed-case identifiers and angle-bracket meta-variables.
- AQA A-level 7517 (AQA 2023): the specification requires expressing a solution as pseudo-code with sequence, assignment, selection and iteration, and converting pseudo-code to code. The specification text read here defines no syntax.
- Rheault 2023: 226 CS1 and CS2 students did better and preferred compile-and-run prompts to pseudocode prompts (abstract; secondary).
- Obaidellah 2020: eye tracking of 51 students ordering pseudocode statements; regressions grew with difficulty (abstract; secondary).

## 5. Pseudocode in papers, reproducibility and datasets

- Toksoz 2024: 2.29 million arXiv papers scanned; a random sample of 1000 found pseudocode in 101. About 323 thousand algorithm blocks were extracted from LaTeX sources.
- Gundersen 2018: 400 AI conference papers scored on documentation variables; the method factor includes a pseudo-code variable. The authors advise pseudo-code with an explanation of parameters to decrease ambiguity. The per-variable share was not read here.
- Kulal 2019: SPoC, 18,356 C++ programs with human-written pseudocode per line; one pseudocode line maps to about one or two code lines.
- Oda 2015: generated line-level pseudo-code from Python; the authors report it is largely accurate and aids code understanding (abstract; secondary).
- Chen 2026: 9,690 translation tasks, five language models; pseudocode as an intermediate step complements direct translation. Readers that are models are reviewed in the LLM readers review.

## 6. Practice: textbooks, typesetting, wikis and industry

- Cormen 2003: the textbook authors ship their own typesetting package for the second edition's pseudocode. It has line numbers, an arrow for assignment, small-capital procedure names and a comment symbol.
- Wikipedia 2026a: states that no broad standard for pseudocode syntax exists, and that limited standards exist for academic assessment.
- CTAN 2026: algorithm2e (version 5.2), algorithmicx and clrscode are listed as separate packages for typesetting algorithms. The pages give no usage counts.
- Newcombe 2015: Amazon engineers describe TLA+ and PlusCal, with PlusCal intended as a direct replacement for pseudocode (company report on itself).
- Bogli 2024: a systematic review of a decade of industrial TLA+ practice; the abstract was not available here.
- Helwer 2023: one practitioner translated a published 1980 pseudocode algorithm to Python and PlusCal and found bugs with tests and a model checker (one case, self-reported).
- Rosetta Code 2026: a site that shows the same task in many languages; it states 1,362 tasks and 1,016 known languages. It is a collection, not a study.

## 7. Literate programs and notebooks

- Knuth 1984: literate programming, a program as an essay with code in the order the reader needs.
- Shum 1994: a course used literate programming; the abstract reports more documentation, not better comprehension.
- Rule 2018: of over one million GitHub notebooks, one in four had no explanatory text.
- Wang 2020: in a sample of 936 published notebooks, 73% would not be reproducible with straightforward approaches.
- Pimentel 2021: a study of 1.4 million notebooks and a tool to find reproducibility issues.
- No sibling review in this repository covers notebooks; link one here if it appears.
