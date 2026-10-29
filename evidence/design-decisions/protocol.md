# Protocol: how the pool of sources was built

This file states how another reviewer can repeat the search, screening and scoring of the design-decisions review. It follows Garousi 2019, a multivocal literature review (MLR): formal and grey literature in one pool. All searches of the review ran on 2026-10-28. The architecture terms it uses (viewpoint, architectural knowledge) are defined in [architecture-descriptions](../architecture-descriptions/frame.md).

## 1. Why grey literature

Garousi 2019 Table 4: one "yes" suggests including grey literature. All seven answers here are yes.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the main forms (ADR, design doc, RFC) come from practice |
| 2 | Lack of volume or quality of evidence? | yes: two controlled experiments on documents in 20 years of work (Tofan 2014; Nogueira 2026) |
| 3 | Context important? | yes: company size and process decide which form fits |
| 4 | Corroborate research with practice? | yes |
| 5 | Challenge practice with research, or the reverse? | yes: practice runs ahead of the evidence (position.md) |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: 875 repositories tagged adr (state-of-the-art.md) |

## 2. Questions

| Id | Question |
|---|---|
| Q1 | What does a decision record hold? |
| Q2 | Does recorded rationale help later decisions? |
| Q3 | How is a proposal structured? |
| Q4 | How is a proposal judged, and why is it declined? |
| Q5 | Do people adopt and keep ADRs? |
| Q6 | Why is rationale not captured? |
| Q7 | Which rationales drive decisions? |

## 3. Existing reviews (Garousi Guideline 2)

- Searched first, by three web searches (R1 to R3) and by the lead the commissioner named.
- R1: "systematic mapping study architectural decisions" or "past and future of software architectural decisions".
- R2: "architecture decision records systematic literature review OR mapping study".
- R3: "multivocal literature review architecture decision documentation" (formal side: strings F2, F6).
- Found: 9 reviews and maps; 2 read in full, 3 by abstract or page summary, 4 by title only. They are placed in review.md strand 0.

## 4. Formal search

Count source: the Semantic Scholar bulk title-and-abstract search, and the arXiv search API (all fields). OpenAlex, the intended source, refused every request on the day (daily budget exhausted), so its counts are absent; Semantic Scholar matches words, not phrases, so counts are noisy upper bounds.

| Id | String as run | Semantic Scholar | arXiv |
|---|---|---|---|
| F1 | "design rationale" +software | 672 | 30 |
| F2 | "architecture decision records" | 34 | 13 |
| F3 | "architectural decision records" | 34 (same set as F2) | 13 |
| F4 | "architectural design decisions" | 663 | 38 |
| F5 | "architectural knowledge" +decision | 374 | 22 |
| F6 | "decision documentation" +architecture | 29 | not run |
| F7 | "design document" +software +review | 97 | 5 |
| F8 | "request for comments" +design +software | 25 | 4 |
| F9 | "enhancement proposals" | 164 | 19 |
| F10 | "architecture decision" AND (documentation OR rationale) | not run | 31 |

- Screened by title: all hits of F2, F3, F6; the 15 most cited of F1, F4, F5, F7, F8; the first 12 arXiv hits of each arXiv string. F9 was too noisy to screen on Semantic Scholar (physics, imaging); its arXiv set gave one lead.
- Snowballing, backward: the reference lists of Tofan 2014 and Harhio 2022 were read for further reviews. Forward: Semantic Scholar citations of Tofan 2014 were listed (first page only). Both are partial.

## 5. Grey search

- Types and producers, chosen because Harhio 2022 found practitioners write mostly about ADRs, and Pragmatic Engineer 2022 lists RFC users:
  - template and community projects (MADR, arc42, adr.github.io);
  - open-source proposal processes (Rust, Python, Kubernetes, Go, Swift);
  - company engineering blogs and public guides (GitHub, Attentive);
  - vendor and government guidance (AWS, Microsoft, Google Cloud, GOV.UK);
  - talks, practitioner articles and magazines.
- Engine: a general web search engine, first result page per string (about 10 results). Results personalise and change.
- Q/A sites: Software Engineering Stack Exchange and Stack Overflow, searched through their public API on 2026-10-28 (subsection Q/A sites, below). Reddit was blocked for the search tool and is not covered.

| Id | String as run (abridged) | Screened | Included |
|---|---|---|---|
| G1 | architecture decision records lessons learned pitfalls team practice | 10 | 3 |
| G2 | "design doc" template how engineering teams write design documents blog | 9 | 1 |
| G3 | "RFC process" engineering team company lessons learned design review | 9 | 0 new |
| G4 | architecture decision record Google Cloud OR Spotify OR GitHub blog why we write ADRs | 10 | 2 |
| G5 | InfoQ architecture decision records talk Nygard Keeling presentation | 10 | 0 |
| G6 | architecture decision record how to document why decisions (Q/A sites) | 9 | 1 |
| G7 | design docs OR technical design review proposal alternatives considered non-goals, named companies | 9 | 0 new |
| G8 | Keeling OR Richards and Ford books, architecture decision records chapter | 9 | 0 (books not read) |
| P | direct visits to named producers: Go, Swift, arc42, Google Cloud, Kafka | 5 | 4 (Kafka page unreadable) |

### Q/A sites

Strings DD1 to DD18 ran on 2026-10-28, one reviewer, grey tier 2. The stopping parameters, the API call, how threads are read and scored, and the shared limits are in the [architecture-descriptions protocol](../architecture-descriptions/protocol.md#q-a-sites).

**Strings as run, design-decisions**

| Id (design-decisions) | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| DD1 | `q=architecture decision record` | Software Engineering Stack Exchange; Stack Overflow | 39 | 1 | 1 |
| DD2 | `title=decision record` | Software Engineering Stack Exchange; Stack Overflow | 2 | 1 | 0 |
| DD3 | `q=design document` | Software Engineering Stack Exchange | 30 | 1 | 1 |
| DD4 | `q=document design decisions rationale` | Software Engineering Stack Exchange; Stack Overflow | 14 | 2 | 2 |
| DD5 | `title=design document` | Software Engineering Stack Exchange; Stack Overflow | 43 | 6 | 5 |
| DD6 | `title=design doc` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| DD7 | `title=rationale` | Software Engineering Stack Exchange | 24 | 1 | 0 |
| DD8 | `title=RFC` | Software Engineering Stack Exchange | 10 | 0 | 0 |
| DD9 | `title=design decisions` | Software Engineering Stack Exchange; Stack Overflow | 44 | 3 | 2 |
| DD10 | `title=design review` | Software Engineering Stack Exchange | 13 | 0 | 0 |
| DD11 | `title=architecture decisions` | Software Engineering Stack Exchange; Stack Overflow | 9 | 0 | 0 |
| DD12 | `title=document decisions` | Software Engineering Stack Exchange; Stack Overflow | 0 | 0 | 0 |
| DD13 | `title=technical specification` | Software Engineering Stack Exchange | 3 | 0 | 0 |
| DD14 | `title=design proposal` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| DD15 | `title=ADR` | Software Engineering Stack Exchange; Stack Overflow | 30 | 1 | 0 |
| DD16 | `tagged=documentation&q=decisions` | Software Engineering Stack Exchange | 19 | 5 | 2 |
| DD17 | `tagged=architecture&q=rationale` | Software Engineering Stack Exchange | 10 | 0 | 0 |
| DD18 | `title=decisions` | Software Engineering Stack Exchange | 30 | 4 | 2 |
| Total | 18 strings | | 320 | 15 (distinct) | 15 |

**Selection and scoring**

- Opening, inclusion, exclusion and scoring rules: as in the shared rules.
- Included: 15. Scored on the 20 criteria of Garousi 2019 Table 7 (section 8), threshold 10 of 20. Below the threshold: 0; they stay as examples of practice only.

**Stopping point**

- The run ended after string DD18. The last string that added a new included thread was DD18 (2 new).

**Limits specific to this search**

- Limits common to all four searches: as in the shared rules.

## 6. Stopping rule

- Stated before searching: effort bounded, N = 10 results per string, with saturation, k = 5.
- Saturation means: stop a string after 5 consecutive results that add no new concept. G3, G5 and G7 stopped this way, since they returned only known sources or off-topic pages.
- Formal: evidence exhaustion for F2, F3, F6 (small sets); effort bounded (top 15) for the rest.
- Q/A sites: see the subsection Q/A sites; the search stopped after string DD18.

## 7. Selection

- Include: a source on the form, content, use or adoption of documents that propose or record software design decisions; English; readable on the search date.
- Exclude:
  - tools or LLM generators with no bearing on document form (adjacent only, Gupta 2026);
  - vendor posts selling a documentation product;
  - duplicates and non-software design review;
  - sources whose abstract could not be read and whose title does not settle relevance (kept as "located only").
- Grey sources must also pass section 8.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

- 20 criteria, each 1, 0.5 or 0: authority of the producer (4), methodology (6), objectivity (4), date (1), position with respect to related sources (1), novelty (2), impact (1), outlet type (1).
- Outlet tier: books, magazines, theses, government and standards documents, vendor guidance pages = tier 1 (1); presentations, project documentation, wiki pages = tier 2 (0.5); blogs = tier 3 (0).
- Impact is judged from stars, citations or the size of the user base, as the source allows.
- Threshold: 10 of 20. Below it a source stays only as an **example of practice**, never as support for a claim; the text that cites it says so.
- Scores, with subtotals, are in sources.md.

## 9. Extraction and synthesis

- Extracted per source: kind, year, the claim, the evidence offered, any number (marked "(secondary)" if not read in the primary).
- Synthesis is narrative, by question Q1 to Q7, and every claim traces to a row of sources.md.

## 10. Limits

- A second rater re-scored 7 of this topic's grey sources blind ([method](../README.md#method)): all 7 decisions agree. The second scores were equal or higher, so the scores of exactly 10 (Microsoft 2026, Rust 2026b) sit near the threshold on one side only.
- Search engines personalise and change; counts will differ on a repeat.
- OpenAlex counts are missing; Semantic Scholar and arXiv counts are not phrase-exact.
- Forward snowballing was one page; backward snowballing covered two works.
- Many formal sources were read by abstract only; sources.md says which.
- This search did not find a study that measures reviewers reading proposals; that is not proof none exists.
- Q/A threads of design-decisions: one scorer, no second rater.
