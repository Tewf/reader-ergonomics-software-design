# Protocol: how the pool of sources was built

This file records how the algorithm-design review was searched, screened and scored, for a reviewer who wants to repeat it. The rules every review shares are in the [evidence method](../README.md#method). Every search of this review ran on 2026-10-29. Two neighbouring reviews cover the rest: pseudocode and flowcharts are in [pseudocode](../pseudocode/frame.md) and decision records are in [design decisions](../design-decisions/frame.md).

## 1. Why grey literature

Garousi 2019 Table 4 asks seven questions, and one yes is enough to add grey literature ([the rule](../README.md#method)). Here all seven are yes.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: specification styles come from languages and tools |
| 2 | Lack of volume or quality of evidence? | yes: 17 controlled trials among 94 papers on teaching algorithm design (Liu 2024) |
| 3 | Context important? | yes: safety-critical work and a web service ask different things of a specification |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: spec-driven tools run ahead of any effect study (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 143,670 stars on one spec-driven tool; 9,114 on a property-testing library (sources.md) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | Which design techniques are taught and used, and is their taxonomy sound? |
| Q2 | Does problem solving instruction improve the algorithms people produce? |
| Q3 | Which ways of stating intended behaviour exist? |
| Q4 | Do specifications improve correctness, and at what cost? |
| Q5 | Are formal notations readable? |
| Q6 | What does practice use? |
| Q7 | How are algorithms engineered and evaluated by experiment? |
| Q8 | Does a specification or a plan given to a model improve its code? |

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by eight web searches (R1 to R8) on the first result page, about ten results each.
  - R1 teaching algorithm design techniques, systematic review.
  - R2 formal specification, mapping study, empirical evidence, cost.
  - R3 language models for code generation, planning and specification, survey.
  - R4 design by contract and run-time assertion checking, systematic review.
  - R5 property-based testing, mapping study or review (two result lists).
  - R6 formal methods education, systematic review.
  - R7 programming problem solving and planning for novices, systematic review (two result lists).
  - R8 language models and formal specification, survey.
- Found: 9 reviews, maps and surveys; 1 read in part (Liu 2024), 2 by abstract (Okumus 2025, Beg 2025), the rest by abstract summary or title. They are in review.md strand 0.
- R5 found no review of property-based testing; R7 found no review of planning strategies on novice outcomes.

## 4. Formal search

Count sources: the Semantic Scholar bulk title-and-abstract search (no key) and the arXiv search API (all fields). OpenAlex was not called: its anonymous daily budget is spent until 00:00 UTC on 2026-10-30, so its counts are absent and are added afterwards by script from the strings in the file openalex.tsv. Semantic Scholar and arXiv match words, not phrases, so counts are noisy upper bounds. Semantic Scholar lists were ordered by citations.

| Id | String as run (Semantic Scholar syntax) | Semantic Scholar | arXiv |
|---|---|---|---|
| F1 | "algorithm design techniques" or "algorithm design paradigms" or "algorithm design strategies" | 325 | 34 |
| F2 | "algorithmic problem solving" +students | 175 | 15 |
| F3 | "design recipe" +programming | 33 | 3 |
| F4 | "programming plans" or "plan composition" +novice | 80 | 30 |
| F5 | "correctness by construction" +program | 619 | 334 |
| F6 | "design by contract" or "programming by contract" | 3,341 | 84 |
| F7 | "loop invariants" | 1,044 | 161 |
| F8 | "formal specification" +empirical +(experiment or survey or "case study") | 76 | 45 |
| F9 | "formal methods" +industry +(survey or practice or adoption) | 366 | 9 |
| F10 | "property-based testing" | 439 | 97 |
| F11 | "algorithm engineering" or "experimental algorithmics" | 1,046 | 128 |
| F12 | "formal specification" +(readability or comprehension or understandability or notation) | 1,780 | 46 |
| F13 | "large language models" +code +generation +(specification or postcondition or "formal specification") | 607 | 19 |
| F14 | planning +"code generation" +"language models" | 351 | 226 |
| F15 | "test-driven" +"language models" +"code generation" | 48 | 30 |
| F16 | "specification-driven development" or "spec-driven development" | 40 | 20 |
| F17 | "refinement calculus" or "program derivation" or "program calculation" | 2,447 | 75 |
| F18 | Dafny +verification +"language models" | 28 | 22 |

- The arXiv form of each string is in the same order; F1 to F3 hit a rate limit on the first pass and were rerun later the same day.
- Screened by title: the 10 most cited of every Semantic Scholar list (180 titles). The arXiv sets were counted, not screened.
- Cited-first lists are noisy: F6, F9, F13 and F17 returned chemistry, economics and imaging in the first ten. A short string would have cut the noise; it was kept so that the counts repeat.
- Leads named in the commissioning brief were looked up one by one in Crossref (no identity sent) or, for a DOI Crossref lacks, in DataCite; an arXiv identifier was checked on its abstract page. A lead whose title, year and first author did not match was dropped or corrected.
  - Dropped: a 1997 workshop paper on why formal methods are not used more widely (no resolvable record).
  - Corrected: the contracts-in-the-wild study is by Dietrich, Pearce, Jezek and Brada, not the authors first recalled.
- Snowballing, backward: the references of Liu 2024 section 5.1 gave Ginat 2003 and Bennedsen 2008. Forward: not run.

## 5. Grey search

- Types and producers, chosen because spec-driven work is mostly vendor and practitioner material and committees publish papers:
  - tool repositories and vendor documentation (Spec Kit, Kiro, Hypothesis);
  - a practitioner radar (Thoughtworks);
  - a standards committee paper (C++ contracts);
  - a textbook preface (HtDP);
  - a practitioner essay (Wayne);
  - Q/A sites.
- Engine: a general web search, first result page per string (about ten results). Results personalise and change.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | spec-driven development GitHub Spec Kit Kiro Thoughtworks Technology Radar | 10 | 3 |
| G2 | C++26 contracts P2900 working draft status | 10 | 1 |
| G3 | formal specification, design by contract, practitioner blog on why not used | 10 | 1 |
| G4 | Skiena and Kleinberg Tardos, publisher pages | 19 | 2 (books) |
| G5 | Dafny at a cloud provider, production authorization | 10 | 1 (formal) |
| P | direct visits: Kiro docs, Spec Kit readme, HtDP preface, Thoughtworks radar page, committee paper, essay page, repository API, download statistics | 8 | 2 new (HtDP preface; repository and download counts); the rest re-read sources found by G1 to G3 |

- Reddit, forums and social media were not searched.
- Second pass, 2026-10-29: web searches ran for three things.
  - The abstract of Levitin 1999 and its taxonomy (G6; this found the 2000 magazine article).
  - The published comment on Sobel 2002 (G7), and the findings of Pfleeger 1997 (G8).
  - Open copies of Estler 2014, Gleirscher 2020, Sanders 2009 and Johnson 2002 (G9). The Screened row of sources.md counts the first pass only.
- Second pass, open copies read by script output only, none saved. They were Pfleeger 1997 on an author's site, Berry 2003 on an author's university page, Estler 2014 and Gleirscher 2020 on arXiv, and Garavel 2020 in a national open archive. Woodcock 2009 was read earlier.
- Machine summaries (a one-sentence "tldr" returned by the Semantic Scholar record) were used where no abstract could be read; they are marked "machine summary; secondary" and support no number.

### Q/A sites

Strings AL1 to AL15 ran on 2026-10-29, one reviewer, grey tier 2 (outlet score 0.5). The stopping parameters, the API call, the way threads are opened and scored, and the limits common to the reviews are in the [architecture-descriptions protocol](../architecture-descriptions/protocol.md#q-a-sites).

**Strings as run**

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| AL1 | `q=algorithm design technique` | SESE; CS; CS Educators | 53 | 1 | 1 |
| AL2 | `title=design by contract` | SESE; SO | 43 | 6 | 6 |
| AL3 | `title=postconditions` | SESE; SO; CS | 35 | 0 | 0 |
| AL4 | `title=loop invariant` | CS; SO | 60 | 0 | 0 |
| AL5 | `q=formal specification` | SESE; CS | 60 | 3 | 3 |
| AL6 | `title=formal methods` | SESE; CS | 6 | 3 | 3 |
| AL7 | `title=property-based testing` | SESE; SO | 33 | 3 | 2 |
| AL8 | `q=teach algorithm design` | CS Educators; CS | 10 | 0 | 0 |
| AL9 | `title=design recipe` | CS Educators; SO | 0 | 0 | 0 |
| AL10 | `q=specification before coding` | SESE | 30 | 1 | 1 |
| AL11 | `title=algorithm engineering` | CS; SESE | 1 | 0 | 0 |
| AL12 | `title=specification` | SESE | 30 | 2 | 0 |
| AL13 | `title=Alloy` | SESE; CS; SO | 31 | 0 | 0 |
| AL14 | `title=Event-B` | SESE; CS; SO | 22 | 0 | 0 |
| AL15 | `title=problem solving algorithm` | CS Educators; CS | 0 | 0 | 0 |
| Total | 15 strings | | 414 | 16 (distinct) | 16 |

Site names: SESE Software Engineering Stack Exchange; CS Computer Science Stack Exchange; CS Educators Computer Science Educators Stack Exchange; SO Stack Overflow.

**Selection and scoring**

- Opening, inclusion and scoring follow the [shared rules](../architecture-descriptions/protocol.md#q-a-sites). Beyond them, threads about requirements or documentation in general, and threads of another topic, were excluded after reading.
- Below the threshold: 2 (CS 2020b, CS 2012a); they stay as examples of practice only.

**Stopping point**

- The run ended after AL15: every term of the field named in the brief had been run in some form. String AL10 was the last to add a new included thread (1 new); AL11 to AL15 added none.
- A string that returned 0 to 6 results counts as a weak query, not as proof of absence.
- A string with a very broad word (AL1, AL10, AL12) returned popular threads unrelated to the topic; the `title` form was added for precision.

**Limits specific to this search**

- Votes, views and reputation are those of 2026-10-29; the other shared limits apply.
- Computer Science Educators and Stack Overflow were searched only with the strings that name the topic.

## 6. Stopping rule

- Fixed before searching: effort bounded at N = 10 results per string, with saturation at k = 5. Five consecutive results that add no new concept end a string; G2 and G3 ended this way, since the next results repeated known sources.
- Formal: effort bounded (top 10 per string), plus evidence exhaustion for the small sets (F3, F15, F16, F18, under 50).
- Q/A sites: the parameters are in the subsection above.

## 7. Selection

- Include: a source on designing an algorithm, on stating what it must do, on the evidence of effect or cost, or on handing either to a model; English; readable on the search date.
- Exclude:
  - verification tools and test generators with no bearing on the question (adjacent only);
  - sources on pseudocode, flowcharts, diagrams, decision records and distributed-system design, which other topics own;
  - vendor posts selling a product with no practice content;
  - sources whose abstract could not be read and whose title does not settle relevance.
- Grey sources must also pass section 8.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- The 20 criteria, the tier scale and the threshold of 10 of 20 are those of the [evidence method](../README.md#method).
- Tiers as applied here: tier 1 is books, magazines, theses, standards and committee documents and vendor guidance pages. Tier 2 is presentations, project documentation, repository pages and wiki and Q/A pages. Tier 3 is blogs.
- Impact is judged from stars, downloads, citations, views or votes, as the source allows.
- A source below the threshold stays only an **example of practice**, never support for a claim.
- Scores, with subtotals, are in sources.md.

## 9. Extraction and synthesis

- Extraction and synthesis follow the [evidence method](../README.md#method); the synthesis runs by question, Q1 to Q8.
- A grey source never raises a claim above convention; it shows adoption, with the number, its source and its date.

## 10. Limits

- The limits shared by every review are in the [evidence method](../README.md#method).
- One reviewer, no second rater, no inter-rater agreement.
- OpenAlex counts are missing and the lists are ordered by citations. Forward snowballing was not run; backward covered one review.
- Sources read by title only support no claim.
- Sobel 2002 was not read as a paper, only through its published comment; Levitin 1999 was read in full later, through a library.
- The main books (Polya, Gries, Kourie, Abrial, Back, McGeoch, Kleinberg, Skiena) were not opened.
- Benchmarks of models age within months; the numbers in strand 7 are those of the abstracts.
- This search did not find a controlled study of specification against none on algorithms people write, nor a test of a taxonomy of design techniques; that is not proof none exists.
- Q/A threads: one scorer, no second rater.
