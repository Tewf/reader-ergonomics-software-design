# Protocol: how the pool of sources on system diagrams was built

This file records every search, count, rule and limit of this multivocal literature review, following Garousi 2019, so the pool can be rebuilt. The pool itself is in [sources](sources.md).

## 1. Why grey literature (Garousi 2019, Table 4)

| # | Question | Answer for system diagrams |
|---|---|---|
| 1 | Subject complex, not solvable by formal literature alone? | Yes: research studies UML, practice draws C4, cloud icons and diagrams as code |
| 2 | Lack of volume, quality or consensus in formal evidence? | Yes: mostly students, one lead group for layout |
| 3 | Context important? | Yes: reader, task and diagram type change the result |
| 4 | Goal to corroborate science with practice? | Yes |
| 5 | Goal to challenge practice with science, or the reverse? | Yes: size limits are absent from tools |
| 6 | Synthesis useful to both communities? | Yes |
| 7 | Many practitioner sources? | Yes: vendors, tool projects and blogs publish drawing rules |

## 2. Review questions

- Q1: does notation (UML, C4, data-flow, informal boxes) change how well readers extract structure?
- Q2: do layout and diagram size change accuracy and speed?
- Q3: what do practitioners draw, and what rules do their guides give?
- Q4: do keys, labels, icon sets or text-defined sources change reader outcomes?
- Q5: which baseline must a new drawing rule beat?

## 3. Existing reviews (Guideline 2)

- Searched first: strings 1 to 4, 15 and 16 below, three general web searches for reviews, then the citations of Budgen 2011.
- Sixteen reviews were found (two already cited) and are placed in [review](review.md) strand 0; none is an MLR on diagrams.

## 4. Formal search, run 2026-10-28

| Id | String as run (Semantic Scholar bulk search, title and abstract) | Hits | Screened |
|---|---|---|---|
| 1 | "systematic review" + UML + comprehension | 3 | 3 |
| 2 | "systematic literature review" + UML + diagram | 44 | 20 |
| 3 | "mapping study" + UML | 36 | 20 |
| 4 | "systematic mapping" + "software architecture" + visualization | 3 | 3 |
| 5 | "physics of notations" | 79 | 12 |
| 6 | "visual notation" + "cognitive effectiveness" | 20 | 20 |
| 7 | UML + layout + comprehension + experiment | 8 | 8 |
| 8 | "diagram layout" + UML + understanding | 6 | 6 |
| 9 | "architecture diagram" + readability | 13 | 13 |
| 10 | "UML" + "eye tracking" | 18 | 18 |
| 11 | "data flow diagram" + security + experiment | 7 | 7 |
| 12 | "diagrams as code" | 298 | 12 |
| 13 | "C4 model" + architecture | 35 | 20 |
| 14 | sketches + "software design" + practice | 24 | 20 |
| 15 | "multivocal" + diagram | 1 | 1 |
| 16 | "multivocal" + "architecture documentation" | 0 | 0 |
| 17 | "software architecture" + diagram + practitioners + survey | 5 | 5 |

- Second database, OpenAlex, `title_and_abstract.search`, strings 1 to 8 only: 2, 49, 41, 5, 55, 25, 7, 3 hits. Its daily quota ended there, so strings 9 to 17 have one database.
- Screening: all hits when 20 or fewer; otherwise the top 20 by citation count (top 12 for strings 5 and 12).
- Zero hits on string 16 was read as a weak query, not as absence: strings 4 and 17 cover the topic.
- A quick check on arXiv (abstract field) gave 3 hits for "physics of notations", 5 for "C4 model" and 2 for "architecture diagrams" with "practitioners".
- The strict arXiv queries for "multivocal" with "diagram" and for "eye tracking" with "UML" returned 0. They were read as weak queries and covered by strings 10, 15 and 16.
- Backward snowballing: the review lists of Dikici 2018, Störrle 2016b and Nicacio 2022.
- Forward snowballing: citing papers of Störrle 2011 (59), Budgen 2011 (153) and Moody 2009a (1000 listed, the most the service returned), by title keywords.

## 5. Grey search, run 2026-10-28

- **Types chosen and why:**
  - standards bodies (OMG), because UML is the research baseline;
  - method owners (C4 site) and vendor guidance (AWS, Microsoft), because they set what practitioners draw;
  - diagram-as-code documentation and platform announcements, because adoption is claimed there;
  - threat-modelling guidance (OWASP, Microsoft Learn), because data-flow diagrams are standard there;
  - project style guides (Fuchsia, GitLab), as public internal practice;
  - conference talks and company blogs.
- Books and Q/A threads were sought and not obtained (see limits).

| Id | String (general web search engine) | Results | Screened | Included |
|---|---|---|---|---|
| G1 | software architecture diagram best practices guidelines | 10 | 10 | 0 |
| G2 | common mistakes software architecture diagrams "box and line" ambiguity | 10 | 10 | 1 |
| G3 | cloud architecture diagram guidelines official icons Azure Google Cloud architecture center how to draw | 19 | 19 | 1 |
| G4 | data flow diagram threat modeling guidance trust boundaries OWASP Microsoft | 9 | 9 | 1 |
| G5 | documentation style guide diagrams Mermaid text-based diagrams recommended accessibility alt text | 9 | 9 | 2 |
| G6 | Simon Brown "Software Architecture for Developers" diagrams sketches talk "boxes and lines" C4 | 10 | 10 | 0 |
| G7 | OWASP Threat Modeling Cheat Sheet data flow diagram guidance | 9 | 9 | 1 |
| G8 | Google Cloud architecture diagramming guidelines icons "architecture diagrams" Cloud Architecture Center | 9 | 9 | 0 |
| G9 | softwareengineering.stackexchange architecture diagram UML or boxes and lines | 10 | 10 | 1 |
| G10 | architecture diagrams industry practice grey literature "diagrams as code" | 18 | 18 | 1 |

- Also included: eleven sources cited by the earlier narrative pass (nine pages and the PlantUML and D2 star counts; re-read and scored) and two found by following links (the C4 checklist, the Mermaid introduction).

## 6. Stopping rule, stated before searching

- **Effort bounded:** the top 10 results of each grey string (the engine returns about 10).
- **Saturation:** stop after 5 consecutive screened results that add no new concept.
- Applied: the concepts (title, key, labelled arrows, icon rules, trust boundary, drift, alt text) were all seen by G7; G8 to G10 (37 results) added none, so the grey search stopped.
- Formal search used evidence exhaustion for strings with 20 hits or fewer, and the cap above otherwise.

## 7. Selection

- Include: a study or document about diagrams of a software system drawn for a reader, with a stated or checkable claim; English; any year.
- Exclude: diagram generation or code generation without a reader outcome; teaching tools; test generation; pages that repeat another source; pages not readable by the reviewer.
- A source whose abstract or page could not be read is listed as found, not read, and supports no claim.

## 8. Quality of grey sources (Garousi 2019, Table 7)

- Twenty questions, each 1, 0.5 or 0, in eight groups: authority (4), methodology (6), objectivity (4), date (1), position among related sources (1), novelty (2), impact (1), outlet tier (1).
- Tier 1 (1 point): books, standards and white papers. Tier 2 (0.5): company documentation, wikis, talks, Q/A sites, repository pages. Tier 3 (0): blogs.
- Threshold 10 of 20. A source below it stays only as an example of practice, and the text that leans on it says so.
- A platform count (stars, downloads) has no author; authority was scored on the platform and project.

## 9. Extraction and synthesis

- Extracted: design, sample, diagram type, outcome, effect size, and for grey sources the rule or claim.
- Synthesis is narrative by question; each claim is traceable to a row of [sources](sources.md).

## 10. Limits

- A second rater re-scored 5 of this topic's grey sources blind ([method](../README.md#method)): 4 of 5 decisions agree. The GitLab style guide scores 8 and 13.5, partly because the second rater read the whole guide; it stays an example of practice. Brown 2021 and D2 2026 sit at exactly 10 for both.
- Search engines personalise and change; every date is 2026-10-28.
- Several abstracts and full texts were behind paywalls (Springer, IEEE); they are marked.
- Books, conference talk recordings and Q/A threads were not read; a talk is represented by its abstract page.
