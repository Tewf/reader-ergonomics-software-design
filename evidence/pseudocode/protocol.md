# Protocol: how the pool of sources was built

This file records how the literature on presenting algorithms was searched, screened and scored, following Garousi 2019. The literature is formal and grey (defined in [frame](frame.md)). These records let the pool of that literature in [sources](sources.md) be rebuilt. The method of the search is summarised in the [evidence README](../README.md#method).

## 1. Why grey literature

Garousi 2019 Table 4 asks seven questions; one "yes" suggests including grey literature ([the rule](../README.md#method)). All seven are "yes" here.

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
- OpenAlex then refused further calls (a shared daily budget was spent). The remaining formal strings were run on the arXiv API (field `totalResults`) and on a general web search that returns academic pages. Counts from different engines are not comparable. Seven strings were counted on OpenAlex on 2026-10-29, in the table OpenAlex counts below; F1 to F3 gave the same counts as on the day.
- Every string, its count and its screening are in sources.md.
- Snowballing on 2026-10-28, through the Semantic Scholar graph API:
  - Forward from Shneiderman 1977, Ramsey 1983, Scanlan 1989, Wyrich 2023, Andrzejewska 2022 and Ulate-Caballero 2021 (caps of 60 or 100 apply).
  - Backward from Andrzejewska 2022 and Wyrich 2023 (reference lists as indexed there).

### OpenAlex counts (2026-10-29)

Counted as the [method](../README.md#method) describes; exact for each query as written.

| Id | OpenAlex query as run | Count |
|---|---|---|
| F1 | `"pseudocode" AND ("systematic review" OR "mapping study" OR "literature review")` | 35 |
| F2 | `pseudocode AND comprehension` | 50 |
| F3 | `flowchart AND (pseudocode OR "program comprehension")` | 232 |
| F4 | `pseudocode` | 3,858 |
| F7 | `pseudocode AND reproducibility` | 263 |
| F8 | `"pseudocode" AND "flowchart"` | 229 |
| F9 | `"literate programming"` | 541 |

## 5. Grey search

Types and producers chosen, with the reason:

| Type | Producer | Why |
|---|---|---|
| Standards-like documents | exam boards | they fix a reference language that millions of candidates read |
| Package documentation | CTAN, TeX FAQ, package authors | they fix how pseudocode is typeset in papers |
| Textbooks and their sites | Cormen, Sedgewick, Knuth, McConnell | they set the baseline most authors copy |
| Course handouts | universities | they state rules for writing pseudocode |
| Blogs and newsletters | educators and practitioners | they carry the executable-code debate |
| Wiki | Wikipedia, Rosetta Code | they state what is commonly believed |
| Q/A sites | Software Engineering, Computer Science, Computer Science Educators and Stack Overflow | practitioners and teachers state what they do and why; searched through the Stack Exchange API, see the subsection Q/A sites below |

- Engine: a general web search, standard mode, 2026-10-28. Strings G1 to G12 are in sources.md.
- Not searched: videos, tweets, e-mail lists (low tier, no way to apply the criteria).

### Q/A sites

One reviewer ran PS1 to PS8 on 2026-10-28 as grey tier 2. The [architecture-descriptions protocol](../architecture-descriptions/protocol.md#q-a-sites) gives N and k, the fixed API parameters, the scoring rules and the general limits of the search.

**Strings as run, pseudocode**

| Id (pseudocode) | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| PS1 | `q=pseudocode` | Software Engineering Stack Exchange; Computer Science Stack Exchange; Computer Science Educators Stack Exchange | 69 | 10 | 10 |
| PS2 | `title=pseudocode` | Software Engineering Stack Exchange; Computer Science Stack Exchange; Computer Science Educators Stack Exchange; Stack Overflow | 77 | 17 | 9 |
| PS3 | `title=flowchart` | Software Engineering Stack Exchange; Computer Science Stack Exchange; Computer Science Educators Stack Exchange | 24 | 2 | 1 |
| PS4 | `q=pseudocode flowchart` | Software Engineering Stack Exchange; Computer Science Stack Exchange; Computer Science Educators Stack Exchange; Stack Overflow | 37 | 3 | 1 |
| PS5 | `title=pseudo code` | Software Engineering Stack Exchange; Computer Science Stack Exchange; Computer Science Educators Stack Exchange | 30 | 5 | 4 |
| PS6 | `title=describe algorithm` | Software Engineering Stack Exchange; Computer Science Stack Exchange; Computer Science Educators Stack Exchange | 0 | 0 | 0 |
| PS7 | `title=algorithm notation` | Computer Science Stack Exchange; Software Engineering Stack Exchange; Computer Science Educators Stack Exchange | 2 | 0 | 0 |
| PS8 | `q=pseudocode conventions style` | Computer Science Stack Exchange; Computer Science Educators Stack Exchange; Software Engineering Stack Exchange | 2 | 1 | 0 |
| Total | 8 strings | | 241 | 26 (distinct) | 25 |

**Selection and scoring**

- Opening, inclusion, exclusion and scoring rules: as in the shared rules.
- Included: 26. Scored on the 20 criteria of Garousi 2019 Table 7 (section 8), threshold 10 of 20. Below the threshold: 1; they stay as examples of practice only.

**Stopping point**

- The run ended after string PS8. The last string that added a new included thread was PS5 (4 new).

**Limits specific to this search**

- Limits common to all four searches: as in the shared rules.
- Thread 3884 (Nassi-Shneiderman diagrams) was found by the system-diagrams string SD3 and fits here as a flowchart variant.
- String PS1 was not run on Stack Overflow; PS2 and PS4 were.

## 6. Stopping rule

Stated before searching:

- Effort bounded: the top N = 10 results per string (the engine returned about 10 per call; no second page was requested).
- Saturation: a string family stops after k = 3 consecutive results that add no concept not already in the list C1 to C7.
- Concepts: C1 reference language per board; C2 no common standard; C3 typesetting packages; C4 executable code against pseudocode; C5 pseudocode as a design step; C6 handout rules; C7 textbook conventions.
- Applied: strings G8, G11 and G12 added no new concept, so the grey search stopped there.
- Q/A sites: see the subsection Q/A sites; the search stopped after string PS8.

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
- OpenAlex counts exist for seven strings: three on the day, all seven on 2026-10-29.
- Several papers were read at abstract level; each is marked "(abstract; secondary)".
- Printed Knuth and the printed conventions of Cormen et al. were not read.
- Q/A threads of pseudocode: one scorer, no second rater.
