# State of the art, per sub-question

Two records are kept apart: **best evidence** (a research record) and **most adopted** (a practice record).

## Best evidence

| Sub-question | Record holder | Measured how |
|---|---|---|
| Prose, constrained language or diagram for professionals tracing, coding and debugging | Boehm-Davis 1983 | 72, 36 and 36 professionals; time and errors |
| PDL or flowchart for design quality and comprehension | Ramsey 1983 | one experiment; design quality, comprehension, implementation (abstract) |
| Does a flowchart help with a program | Shneiderman 1977, Brooke 1980 | controlled experiments; no reliable gain (abstracts; secondary) |
| Flowchart or pseudocode for comprehending an algorithm | Andrzejewska 2022 (largest), Scanlan 1989 | 114 participants, eye tracking, time, errors, confidence; Scanlan: three algorithms, five measures, students |
| Flowchart or pseudocode for composing an algorithm | Glorfeld 1988 | novices; share with a working algorithm |
| Diagram added to real code | Hendrix 2002 | students; time and correctness on one module |
| Pseudocode against compile-and-run for assessment | Rheault 2023 | 226 students; performance and preference |
| Flowchart environment against Python as first language | Coffman 2026 | 1,083 students, cluster-randomised; achievement, later courses (abstract) |
| Naming the implemented algorithm next to code | Neumüller 2025 | 56 participants; comprehension score, time (abstract) |
| How comprehension experiments are built | Wyrich 2023 | mapping study of 95 experiments |
| Indentation effect | Hanenberg 2024 (large), Bauer 2019 (none) | 27 and 22 participants; reading time, accuracy |
| Pseudocode to code at line level | Kulal 2019 | 18,356 programs; test-case pass rate |

## Most adopted

| Practice | Holder | Evidence of adoption |
|---|---|---|
| Pseudocode in research papers | arXiv corpus | 101 of 1000 sampled papers, 1991-2023 (Toksoz 2024) |
| A defined reference language for exams | College Board 2025, OCR 2026, Cambridge 2024, AQA 2024, Pearson 2018 | published in each syllabus or guide; the five disagree on assignment symbol and index base |
| Textbook pseudocode with its own typesetting package | Cormen 2003 | package on CTAN 2026 |
| Executable specification for distributed designs | Newcombe 2015 | 10 systems, 7 teams (the company's own count) |
| Pseudocode as a design step before code | McConnell 2004 | a chapter of a widely read book (not read here) |
| Notebooks as literate programs | Rule 2018 | over one million public notebooks |

## Upper bounds (achieved)

- Flowcharts were read faster, with fewer errors, at all three complexity levels, with few exceptions, in 114 participants (Andrzejewska 2022; abstract).
- Professionals coded 31% faster from PDL than from prose in one setting (29.7 against 20.5 minutes; Boehm-Davis 1983).
- A pseudocode line corresponds to one or two code lines in a human-written corpus (Kulal 2019).
- Over 320 thousand algorithm blocks have been extracted from arXiv sources (Toksoz 2024).

## Lower bounds (not yet shown)

- No study found that compares a published pseudocode against real code for reimplementation by developers, with a fixed task and reader group.
- No study found that tests the advice to add pseudocode "to decrease ambiguity" (Gundersen 2018).
- No controlled comprehension experiment of literate programs was found in this search (a thesis, Bertholf 2000, exists and was not read).
- No study found that measures line numbers in pseudocode, or the typed-assignment arrow against an equals sign, although the boards use arrow, equals sign and SET ... TO.
- No study found that compares the pseudocode of Cormen, Knuth and Sedgewick side by side; Sedgewick's 4th edition ships Java, so the contrast is also pseudocode against code.
