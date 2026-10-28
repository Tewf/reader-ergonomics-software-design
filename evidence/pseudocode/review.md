# Review

This file lists what the literature says about presenting an algorithm, by strand: existing reviews, format comparisons, notation theory, design languages, education, papers, practice, and literate programs.

Pool and method: [protocol](protocol.md), [sources](sources.md). A grey source scored under 10 of 20 is marked "(example only)".

## 0. Existing reviews

| Review | Covered | How | Found | Difference from this review |
|---|---|---|---|---|
| Waddel 1988 | graphical representations of algorithms | survey of empirical studies | flowchart evidence questionable, in places a hindrance (abstract; secondary) | old; no practice sources |
| Wyrich 2023 | code comprehension experiments, 1979-2019 | mapping study, 95 experiments | design options and their deficiencies; pseudocode is a stimulus language once | maps how experiments are built, not which notation wins |
| Noone 2018 | visual against textual languages for learning to program | SLR; 5,106 hits, 661 after titles, 124 after abstracts, 54 accepted (the text also says 53) | visual or hybrid languages help interest and retention (authors' conclusion) | its text mentions flowchart languages and a pseudo-code course only in passing; outcome is learning, not reading an algorithm |
| Ulate-Caballero 2021 | notations and tools for testing concurrent and distributed pseudocode | SLR | few publications; 5 tools interpret such pseudocode, 2 verify it | asks how to test pseudocode, not how readers fare |
| Dehaerne 2022 | machine-learning code generation | SLR, 37 publications | three paradigms, one of them description-to-code | machines write code; no human reader |
| Alharbi 2025 | automatic code generation techniques | SLR, 76 primary studies (secondary) | techniques grouped by input and intermediate form | same |
| Tiwari 2023 | titled a review of pseudocode-to-Python models | abstract (second-hand) describes one proposed model | not a review by its abstract | same |

- This search did not find a systematic review, mapping study or MLR of how an algorithm is presented to a human reader.
- This review differs in four ways: the outcome is a reader's task; formats are compared (prose, design language, pseudocode, flowchart, code); practice sources are included and scored; the baseline is named.

## 1. Format comparisons: flowchart, PDL, pseudocode, prose

Seminal experiments:

- Shneiderman 1977: detailed flowcharts for composing, understanding, debugging and modifying programs gave no significant difference (abstract; secondary).
- Brooke 1980: flowcharts did not raise correct fault identifications (abstract; secondary).
- Boehm-Davis 1983 crossed symbology (prose, constrained language, ideogram) with spatial arrangement (sequential, branching, hierarchical):

| Experiment | Task | Participants | Prose | PDL | Ideogram |
|---|---|---|---|---|---|
| 1 | tracing questions | 72 professionals | slower | faster | faster |
| 2 | complete about fifteen lines, minutes | 36 professionals | 29.7 | 20.5 | 23.9 |
| 2 | errors | same | 2.4 | 0.8 | 1.4 |
| 3 | find three seeded errors, minutes | 36 professionals | 18.7 | 14.5 | 14.2 |

- Experiment 1 found no difference on input-output questions.
- Experiment 4 gave prose the code's variable names; the prose penalty shrank, so part of it was naming.
- PDL was the most preferred symbology; branching the most preferred arrangement.
- Ramsey 1983: PDL designs were more detailed; with equivalent designs, comprehension did not differ (abstract).
- Scanlan 1989: structured flowcharts beat pseudocode on three algorithms and five measures (abstract; secondary).
- Scanlan 1988: six replications, 193 students, 75.1% to 89.1% preferred flowcharts (abstract; secondary).
- Andrzejewska 2022: 114 participants, eye tracking; flowcharts were read faster, with fewer errors and higher confidence, at all three complexity levels, with few exceptions (abstract). It comes from a group independent of Scanlan's and agrees with his direction.

Forward citations:

- Glorfeld 1988: novices composing an algorithm more often produced a working one with pseudocode (abstract; secondary).
- Andrzejewska 2015: formal notation was hard in both variants (abstract; secondary).
- Katona 2022: a flowchart cost more fixations and pupil size than a Nassi-Shneiderman diagram (abstract; secondary).
- Hendrix 2002: control structure diagrams added to source code helped students on one module (abstract; secondary).
- Ensmenger 2016: a history of the flowchart as a negotiated design document.
- Curtis 1989: a documentation-format study; no abstract was found and it was not read.

## 2. Notation theory, layout and the shape of the evidence

- Green 1996: the cognitive dimensions framework (title and framing only).
- Green 1992: visual programs were not uniformly easier than textual ones (abstract only).
- Petre 1995: the difference lies in how far a notation supports the conventions experts expect (abstract; secondary).
- Soloway 1984 (not read; secondary), Shaft 2006 (title only), Larkin 1987 (linked in the README).
- Wyrich 2023: 53.7% of 95 experiments used only students; one replication met its inclusion rule; pseudocode appears once.
- Bauer 2019: 22 participants, no indentation effect. Hanenberg 2024: 27 participants, non-indented if-statements took 2.13 times as long.
- Neumüller 2025: labelling the algorithm that a piece of code implements raised comprehension (56 participants, p=0.040, median gain about 23%, no change in time; abstract).

## 3. Design languages and refinement

- Caine 1975: PDL, a design language for describing a program before coding.
- Wirth 1971: stepwise refinement.
- Boehm-Davis 1983 and Ramsey 1983 test the PDL idea.

## 4. Education and exam boards

- Julaihi 2026: 95 first-year students, a perception survey; no significant difference between flowcharts and pseudocode (abstract).
- Cabo 2018: skill with flowcharts predicted skill in Python (r-squared 0.68, correlational); 63% found flowcharting easier (abstract).
- Coffman 2026: 1,083 students, cluster-randomised; a flowchart environment and Python gave similar overall performance (one demographic group did worse with Python), and students judged Python more valuable (abstract).
- Andrzejewska 2020: over six months the dominant form students analysed shifted from flowchart to code (abstract).
- López-García 2025: 405 first-year students; a pseudocode with keywords in their own language was designed from a survey (abstract read in part).
- Chida 2024: a work-in-progress study of pseudocode reading and writing in an algorithms course.
- Rheault 2023: 226 students did better with, and preferred, compile-and-run prompts to pseudocode prompts (abstract).
- Obaidellah 2020: 51 students ordering pseudocode statements regressed more as difficulty grew (abstract).

Exam boards, read in the primary documents (the boards decide what candidates must write):

| Board | Candidate must use it? | Assignment | Comment | Index base |
|---|---|---|---|---|
| College Board 2025 | reference sheet notation | arrow | not read | 1 |
| OCR 2026 | yes for code answers, no marks otherwise; free for design questions | = | // | 0 |
| Cambridge 2024 | guide fixes style | arrow | // | generally 1 |
| AQA 2024 (GCSE) | no, but clear and consistent | arrow | # | 0 |
| Pearson 2018 (IGCSE) | no, any valid method | SET ... TO | # | 0 |

- AQA 2023 (A-level) requires pseudo-code but its specification defines no syntax.
- Cambridge 2024 also fixes monospaced font and upper-case keywords, and usually indents by three spaces.

## 5. Pseudocode in papers, reproducibility and datasets

- Toksoz 2024: 2.29 million arXiv papers scanned; 101 of a random 1000 had pseudocode; about 323 thousand algorithm blocks extracted.
- Gundersen 2018: 400 AI papers scored; a pseudo-code variable is part of the method factor; the per-variable share was not read.
- Ince 2012: argues that computed results need their source code released, since prose leaves exact reproduction uncertain (page synopsis and a search summary only).
- Kulal 2019: SPoC, 18,356 C++ programs with line-level pseudocode.
- Oda 2015: line-level pseudo-code from Python, judged largely accurate (abstract; secondary).
- Chen 2026: 9,690 translation tasks, five models; pseudocode as a step complements direct translation.

## 6. Practice: textbooks, typesetting, wikis, blogs and industry

- Cormen 2003: the textbook authors ship a package for their pseudocode (numbered lines, arrow, small-capital names, comment symbol). The printed conventions section was not read.
- Sedgewick 2026: the booksite lists Java code of the book's algorithms; the authors state no reason (example only).
- Forum 2026: a transcription of Knuth's Algorithm E shows labelled steps E1 to E3 with bracketed titles (example only; Knuth's printed text was not read).
- McConnell 2004: pseudocode as a design step before code, kept high enough for the domain and low enough to translate almost mechanically (secondary descriptions).
- TeX FAQ 2026: no consensus on how to typeset pseudocode; many packages are named, none called perfect.
- CTAN 2026: algorithm2e 5.2, algorithmicx and clrscode are separate packages; no usage counts.
- Kreher 2026: a package for a textbook's Pascal-like pseudocode.
- UW 2023: a course handout: a competent classmate must be able to implement it, use code idioms and named variables (example only).
- UH 2026: a course asks for pseudocode that is valid Python 3 (example only).
- Wikipedia 2026a: no broad standard exists (example only; TeX FAQ 2026 says the same).
- Newcombe 2015: Amazon engineers present PlusCal as a replacement for pseudocode (company report on itself).
- Bogli 2024: a systematic review of a decade of industrial TLA+ practice; abstract not read.
- Helwer 2023, Davis 2023: executable code is better than pseudocode (practitioner blogs; one case in the first).
- Sun 2024: pseudocode is more accessible than code (an opinion post).
- Rosetta Code 2026: 1,362 tasks in 1,016 languages (example only).

## 7. Literate programs and notebooks

- Knuth 1984: a program as an essay.
- Shum 1994: a course using literate programming produced more documentation, not shown to be better comprehended.
- Rule 2018: of over one million notebooks, one in four had no explanatory text.
- Wang 2020: 73% of 936 notebooks would not be reproducible straightforwardly.
- Pimentel 2021: a large study of notebooks (the 1.4 million figure was not checked against this paper).
- Bertholf 2000, a thesis on literate-program comprehension, was not read.
