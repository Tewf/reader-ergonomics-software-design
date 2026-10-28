# State of the art, per sub-question

Two records are kept apart: **best evidence** (a research record) and **most adopted** (a practice record).

## Best evidence

| Sub-question | Record holder | Measured how |
|---|---|---|
| Prose, constrained language or diagram for professionals tracing, coding and debugging | Boehm-Davis 1983 | 72, 36 and 36 professionals; time and errors |
| PDL or flowchart for design quality and comprehension | Ramsey 1983 | one experiment; design quality, comprehension, implementation (abstract; secondary) |
| Does a flowchart help with a program | Shneiderman 1977, Brooke 1980 | controlled experiments; no reliable gain (abstracts; secondary) |
| Flowchart or pseudocode for comprehending an algorithm | Scanlan 1989 | three algorithms, five measures, students |
| Flowchart or pseudocode for composing an algorithm | Glorfeld 1988 | novices; share with a working algorithm |
| Diagram added to real code | Hendrix 2002 | students; time and correctness on one module |
| Pseudocode against compile-and-run for assessment | Rheault 2023 | 226 students; performance and preference |
| How comprehension experiments are built | Wyrich 2023 | mapping study of 95 experiments |
| Indentation effect | Hanenberg 2024 (large), Bauer 2019 (none) | 27 and 22 participants; reading time, accuracy |
| Pseudocode to code at line level | Kulal 2019 | 18,356 programs; test-case pass rate |

## Most adopted

| Practice | Holder | Evidence of adoption |
|---|---|---|
| Pseudocode in research papers | arXiv corpus | 101 of 1000 sampled papers, 1991-2023 (Toksoz 2024) |
| A defined reference language for exams | College Board 2025, OCR 2026, Cambridge 2024 | published in each syllabus or guide |
| Textbook pseudocode with its own typesetting package | Cormen 2003 | package on CTAN 2026 |
| Executable specification for distributed designs | Newcombe 2015 | 10 systems, 7 teams (the company's own count) |
| Notebooks as literate programs | Rule 2018 | over one million public notebooks |

## Upper bounds (achieved)

- Professionals coded 31% faster from PDL than from prose in one setting (29.7 against 20.5 minutes; Boehm-Davis 1983).
- A pseudocode line corresponds to one or two code lines in a human-written corpus (Kulal 2019).
- Over 320 thousand algorithm blocks have been extracted from arXiv sources (Toksoz 2024).

## Lower bounds (not yet shown)

- No study found that compares a published pseudocode against real code for reimplementation by developers, with a fixed task and reader group.
- No study found that tests the advice to add pseudocode "to decrease ambiguity" (Gundersen 2018).
- No controlled comprehension experiment of literate programs was found in this search (a thesis, Bertholf 2000, exists and was not read).
- No study found that measures line numbers in pseudocode, or the typed-assignment arrow against an equals sign.
