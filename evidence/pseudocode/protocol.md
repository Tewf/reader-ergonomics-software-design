# Protocol: how the pool of sources was built

This file records how the formal and grey literature (defined in [frame](frame.md)) on presenting algorithms was searched, screened and scored, following Garousi 2019, so that the pool in [sources](sources.md) can be rebuilt. The method is summarised in the [evidence README](../README.md#method).

## 1. Why grey literature

Garousi 2019 Table 4 asks seven questions; one "yes" suggests including grey literature. All seven are "yes" here.

| # | Question | Answer for pseudocode |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | Yes: notation, layout, tooling and teaching all matter |
| 2 | Lack of volume, quality or consensus in formal evidence? | Yes: 95 comprehension experiments in 40 years, pseudocode in one (Wyrich 2023) |
| 3 | Is context important? | Yes: exam, paper, design and teaching settings differ |
| 4 | Validate research with practice? | Yes: conventions are fixed by boards, books and packages |
| 5 | Challenge practice with research, or the reverse? | Yes: see position.md |
| 6 | Would a synthesis help both communities? | Yes |
| 7 | Is there a large volume of practitioner sources? | Yes: boards, packages, course handouts, blogs |

## 2. Review questions

- Q1: Which notation (prose, design language, pseudocode, flowchart, code) helps a reader trace, implement, find a bug or compose an algorithm?
- Q2: Do layout and typesetting choices change comprehension?
- Q3: Which conventions does practice fix, and do they agree?
- Q4: Does pseudocode reduce ambiguity compared with an executable form?
- Q5: What is measured in teaching, and with what outcome?

## 3. Existing reviews (Garousi Guideline 2)

Searched first, with strings F1 and R1 to R5 (sources.md). Seven secondary studies were found and read in part; none reviews how an algorithm is presented to a human reader. They are placed in review.md strand 0.

## 4. Formal search

- Database: OpenAlex, filter `title_and_abstract.search`, field `meta.count`, run 2026-10-28.
- OpenAlex then refused further calls (a shared daily budget was spent). The remaining formal strings were run on the arXiv API (field `totalResults`) and on a general web search that returns academic pages. Counts from different engines are not comparable.
- Every string, its count and its screening are in sources.md.
- Snowballing on 2026-10-28, through the Semantic Scholar graph API:
  - Forward from Shneiderman 1977, Ramsey 1983, Scanlan 1989, Wyrich 2023, Andrzejewska 2022 and Ulate-Caballero 2021 (caps of 60 or 100 apply).
  - Backward from Andrzejewska 2022 and Wyrich 2023 (reference lists as indexed there).

## 5. Grey search

Types and producers chosen, with the reason:

| Type | Producer | Why |
|---|---|---|
| Standards-like documents | exam boards | they fix a reference language that millions of candidates read |
| Package documentation | CTAN, TeX FAQ, package authors | they fix how pseudocode is typeset in papers |
| Textbooks and their sites | Cormen, Sedgewick, Knuth, McConnell | they set the baseline most authors copy |
| Course handouts | universities | they state rules for writing pseudocode |
| Blogs and newsletters | educators and practitioners | they carry the executable-code debate |
| Wiki and Q/A | Wikipedia, Rosetta Code | they state what is commonly believed |

- Engine: a general web search, standard mode, 2026-10-28. Strings G1 to G12 are in sources.md.
- Not searched: videos, tweets, e-mail lists (low tier, no way to apply the criteria).

## 6. Stopping rule

Stated before searching:

- Effort bounded: the top N = 10 results per string (the engine returned about 10 per call; no second page was requested).
- Saturation: a string family stops after k = 3 consecutive results that add no concept not already in the list C1 to C7.
- Concepts: C1 reference language per board; C2 no common standard; C3 typesetting packages; C4 executable code against pseudocode; C5 pseudocode as a design step; C6 handout rules; C7 textbook conventions.
- Applied: strings G8, G11 and G12 added no new concept, so the grey search stopped there.

## 7. Selection

- Include: the source states or measures how an algorithm is presented, or fixes a notation used by readers.
- Exclude: generic tutorials with no author or date; pages behind a login; documents that could not be read; student-made copies of an official document when the official one was read.
- Quality gate: grey sources are scored (section 8); a formal source is graded by its evidence grade.

## 8. Quality of grey sources

Garousi Table 7, 20 criteria, each 1, 0.5 or 0:

| Criterion | Items | Scored 1 when |
|---|---|---|
| Authority | 4 | reputable producer; author with a reputable affiliation; other work in the field; expertise |
| Methodology | 6 | clear aim; stated method; contemporary references; limits stated; specific question; named population or case |
| Objectivity | 4 | balanced; objective; no vested interest; conclusions supported |
| Date | 1 | a date is stated |
| Position | 1 | related sources are linked or discussed |
| Novelty | 2 | adds something unique; strengthens or refutes a position |
| Impact | 1 | a use metric seen in this review shows wide use (0.5 for some sign, 0 for none seen) |
| Outlet | 1 | tier 1 = 1, tier 2 = 0.5, tier 3 = 0 |

- Threshold: 10 of 20. Below it, the source stays only as an example of practice, and any sentence that leans on it says so.
- Scores for documents that are specifications (boards) are high on authority and objectivity and low on methodology, since they are not studies.
- McConnell 2004 was scored from secondary descriptions, not from the book.

## 9. Extraction and synthesis

- Extracted: design, sample size, task, outcome, effect, and for practice sources the symbols they fix.
- Synthesis is narrative by question; each claim traces to a row in sources.md.

## 10. Limits

- A second rater re-scored 5 of this topic's grey sources blind ([method](../README.md#method)): all 5 decisions agree, the forum post kept as an example included (4 and 6 of 20).
- Search engines personalise and change; all searches were run on one day.
- OpenAlex counts exist for three strings only.
- Several papers were read at abstract level; each is marked "(abstract; secondary)".
- Printed Knuth and the printed conventions of Cormen et al. were not read.
