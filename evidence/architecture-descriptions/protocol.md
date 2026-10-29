# Protocol: how the pool of sources was built

This file records the search for the review of architecture descriptions. A reader can repeat the search from it. The review is a multivocal literature review (MLR, Garousi 2019).

Grey literature, which the review includes, is defined in the [design-decisions frame](../design-decisions/frame.md). All searches of the review were run on 2026-10-28 by one reviewer.

## 1. Why grey literature

Garousi 2019 Table 4: one "yes" suggests including grey literature. All seven answers are yes for this topic.

| # | Question | Answer for this topic |
|---|---|---|
| 1 | Is the subject complex and not solvable by the formal literature alone? | Yes: the templates in use (arc42, C4, ARCHITECTURE.md) come from practice. |
| 2 | Is volume or quality of evidence lacking? | Yes: one controlled comparison of formats (Ernst 2023). |
| 3 | Is context important? | Yes: readers, system size and team differ. |
| 4 | Is the goal to corroborate research with practice? | Yes: reader surveys against vendor surveys. |
| 5 | Is the goal to challenge practice with research? | Yes: templates are taught without trials. |
| 6 | Would a synthesis serve both communities? | Yes. |
| 7 | Do many practitioner sources exist? | Yes: templates, blogs, project guides. |

## 2. Questions

- Q0: which reviews of this field exist, and what do they cover?
- Q1: how is a description divided (views, sections)?
- Q2: what does a reader see first?
- Q3: how many levels of abstraction?
- Q4: one document, or one per task?
- Q5: how does a reader find information in it?
- Q6: how is it kept true?
- Q7: what is its effect on understanding?
- Q8: what do projects have?
- Q9: what do machine readers need?

## 3. Existing reviews (Garousi Guideline 2)

Searched before anything else; each is placed in strand 0 of the [review](review.md).

- Strings F6, F4, W1, W2 and O1 below, plus the reviews that appeared as citing papers.
- 19 secondary studies were kept; none has as its subject the organisation of a description for its reader.
- None was read in full: ten through an abstract or a search summary, nine by title only. The review marks each.

## 4. Formal search

Engines: the Semantic Scholar bulk search (Boolean syntax: `|` or, `+` and, quotes for phrases, `*` truncation; results sorted by citation count), the arXiv API, and Crossref for checking every DOI.

OpenAlex was tried first and gave a count for no string: its shared daily budget was used up (HTTP 429). To repeat a count there, use `https://api.openalex.org/works?filter=title_and_abstract.search:<terms>&per_page=1` and read `meta.count`.

Strings as run (hit counts in [sources](sources.md)):

```text
F1  "architecture documentation" | "architectural documentation" | "software architecture documentation"
F2  ("architecture description" | "architecture descriptions") + (42010 | stakeholder* | viewpoint*)
F3  ("architectural views" | "architecture views" | "viewpoints") + "software architecture"
F4  ("architectural knowledge" | "architecture knowledge") + (retrieval | search | documentation | management)
F5  "docs as code" | "documentation as code" | "docs-as-code"
F5b docs as code documentation software      (relevance-ranked endpoint)
F6  ("systematic literature review" | "systematic mapping" | "systematic review" | "mapping study" | "multivocal literature review") + ("architecture documentation" | "architectural documentation" | "architecture description" | "architectural knowledge")
F7  (newcomer* | onboarding) + "architecture documentation"
F8  "C4 model" | "arc42"
F9  "multivocal" + "software architecture"
F10 "architecture documentation" + (readability | comprehension | understandability | usability)
F11 ("software architecture" | "architecture description") + (grey | "grey literature" | practitioners) + (documentation | description)
F12 "C4 model" + "software architecture"
F13 "arc42"
F14 "architecture documentation" + (survey | interview* | practitioners)
F15 ("ARCHITECTURE.md" | "architecture overview") + "open source" + (newcomers | contributors)
A1  ti:"architecture documentation" OR ti:"architectural documentation" OR ti:"architecture description" OR ti:"architecture descriptions"   (arXiv)
A2  abs:"architecture documentation" AND (abs:newcomer OR abs:onboarding OR abs:developers)   (arXiv)
```

- Known limit of the engine: it matched loosely on some strings, so F5 and F8 returned unrelated hits (plant biology, genomics). Their counts are reported but carry no weight.
- Snowballing, forward: the papers citing Rost 2013, Ernst 2023, Dagenais 2010, Lethbridge 2003, Ding 2014a and de Graaf 2016 were listed and screened by title (the first 200 per seed).
- Snowballing, backward: the 45 references of Ernst 2023 were screened. The references of Rost 2013 and Weinreich 2016 could not be listed in time.

## 5. Grey search

Grey types chosen, with the reason:

| Type | Tier | Why |
|---|---|---|
| Standards and standards-body pages | 1 | 42010 defines what a description is |
| Books and theses | 1 | the view-based methods are books; theses carry reviews and case studies |
| Template projects (arc42, C4) and their FAQs | 2 | the most used templates |
| Project documents on GitHub (README, ARCHITECTURE.md) | 2 | the form practice takes |
| Practitioner panels and magazine articles | 2 | InfoQ, Technology Radar |
| Vendor surveys | 2 | the only adoption data in practice |
| Company and consultancy blogs | 3 | how teams say they work |
| Q/A sites | 2 | read through the Stack Exchange API, see the subsection Q/A sites below |

Web queries as run (about 10 results each, one web search engine):

```text
G1  how to document software architecture
G2  software architecture documentation best practices
G3  ARCHITECTURE.md file in repository overview for new contributors
G4  docs as code architecture documentation
G5  softwareengineering.stackexchange how to document software architecture for new team members
G6  Simon Brown talk visualise document explore software architecture C4 InfoQ
G7  onboarding new developers architecture overview documentation engineering blog
G8  Diátaxis documentation framework tutorials how-to reference explanation
G9  architecture documentation views presentation   (restricted to infoq.com, martinfowler.com, thoughtworks.com)
G10 arc42 template adoption survey companies using arc42 architecture documentation
G11 state of software architecture survey architects how they document architecture percent respondents
W1  systematic mapping study OR literature review software architecture documentation practitioners
W2  multivocal literature review software architecture documentation grey literature
O1  architecture documentation methods scientific and grey sources Helsinki   (the one OpenAlex query that returned, before the budget ran out)
```

Besides the strings, nine title lookups were run to read the abstract of a review already found; they are counted in [sources](sources.md).

A Q/A query restricted to stackoverflow.com was refused by the web engine, and the Software Engineering Stack Exchange pages could not be fetched that way. The two sites were therefore searched through their public API on 2026-10-28; the subsection Q/A sites states the strings, the stopping rule and the scoring.

### Q/A sites

The search ran on 2026-10-28, with one reviewer. The grey type searched is question-and-answer sites, tier 2 (outlet score 0.5). For these sites, the four reviews of this repository share the stopping parameters, the reading and scoring rules and the limits below; the other three protocols link here for them.

**Stopping rule, stated before searching**

- Effort bounded: the top N = 30 results by votes per string per site.
- Saturation: stop a string after k = 10 consecutive results that add no new concept.
- Fixed parameters of every call: `order=desc&sort=votes&pagesize=30&filter=withbody` on the Stack Exchange API, version 2.3, endpoint `search/advanced`, no key and no login.

**Strings as run**

Date of every call: 2026-10-28.

- "Returned" is what the API sent (at most 30 per site).
- "Screened" equals returned, since every title was read.
- "Included" is the number of this topic's included threads among them.
- "New" is the number first met in that string.

| Id | String as run | Site | Returned = screened | Included | New |
|---|---|---|---|---|---|
| AD1 | `q=architecture documentation` | Software Engineering Stack Exchange; Stack Overflow | 60 | 4 | 4 |
| AD2 | `q="architecture documentation" (quoted)` | Software Engineering Stack Exchange; Stack Overflow | 29 | 0 | 0 |
| AD3 | `title=document software architecture` | Software Engineering Stack Exchange; Stack Overflow | 0 | 0 | 0 |
| AD4 | `q=arc42` | Software Engineering Stack Exchange; Stack Overflow | 11 | 2 | 2 |
| AD5 | `q=C4 model` | Software Engineering Stack Exchange; Stack Overflow | 36 | 1 | 1 |
| AD6 | `title=software architecture document` | Software Engineering Stack Exchange; Stack Overflow | 4 | 2 | 2 |
| AD7 | `tagged=documentation&q=architecture` | Software Engineering Stack Exchange; Stack Overflow | 48 | 10 | 9 |
| AD8 | `q=how to document software architecture` | Software Engineering Stack Exchange | 30 | 2 | 0 |
| AD9 | `tagged=architecture;documentation` | Software Engineering Stack Exchange; Stack Overflow | 43 | 10 | 0 |
| AD10 | `q=architectural views viewpoints 4+1` | Software Engineering Stack Exchange | 1 | 0 | 0 |
| AD11 | `q=onboarding new developers architecture overview` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AD12 | `q=architecture documentation C4 arc42` | Software Engineering Stack Exchange | 0 | 0 | 0 |
| AD13 | `q=architectural views` | Software Engineering Stack Exchange | 30 | 1 | 1 |
| AD14 | `q=onboarding architecture` | Software Engineering Stack Exchange | 6 | 0 | 0 |
| AD15 | `q=UML architecture documentation` | Software Engineering Stack Exchange | 13 | 2 | 1 |
| Total | 15 strings | | 311 | 21 (distinct) | 20 |

**Selection and scoring**

- Opened: every thread whose title bore on a question of the topic, with the question and its top answers read. Included: the thread answers one of the topic's questions with an argument or an experience, not only a how-to or a lookup. Excluded after reading: how-to questions, product-specific questions, threads about documentation in general (the topic's exclusion E7), and threads that belong to another topic.
- Included: 21. Scored on the 20 criteria of Garousi 2019 Table 7 (see the protocol of the topic), threshold 10 of 20. Below the threshold: 3; they stay as examples of practice only.
- Rules used to score a Q/A thread:
  - A1 is 0.5 for a moderated, peer-voted site.
  - A3 is 1 when the top answerer's reputation is at least 20,000 and 0.5 at 5,000. The reputation is read on the day, as a proxy for public work.
  - A2 and A4 come from a role, or a cited standard or book, in the answer.
  - M2 is 0.5 when the answer says it rests on the answerer's experience, and 1 when it describes cases.
  - I is 1 for at least 20,000 views or a top answer of at least 30 votes, and 0.5 for 3,000 views or 10 votes.
  - T is 0.5 (tier 2). D is 1, since every thread is dated.

**Stopping point**

- The run ended after string AD15, when each term of the field named in the brief had been run in at least one form. The last string that added a new included thread was AD15 (1 new); the strings after it, if any, added none. Saturation was applied in this way across strings; inside a string all returned titles were read, so the k = 10 rule never cut a list short.
- Strings that returned 0 to 6 results (phrase or multi-word queries) were read as weak queries, not as absence; they were followed by a title or tag form of the same words.

**Limits specific to this search**

- The `q` parameter matches words anywhere in a question and ranks by votes, so broad words return unrelated popular threads (a list of 30 may hold two relevant ones). The `title` and `tagged` parameters were added for precision; they miss threads whose title uses other words.
- Votes, views and answer counts are those of 2026-10-28 and change. Reputation is the top answerer's on that day.
- Stack Overflow was searched only with the strings that name the topic; cs and cseducators only for pseudocode, as asked.
- The service refused calls for a while on the day (HTTP 429 with a wait of 145 seconds) after a burst; no result was lost, since the data already read was kept.
- Display names are not recorded; threads are cited by title and number.

- Strings AD10 to AD12 were multi-word and returned 1, 0 and 0 results; only the counts were kept.
- Thread 233099 was found by the system-diagrams string SD6, not by a string of this topic.

## 6. Stopping rule

Stated before searching.

- **Formal:** effort bounded. The first 25 results of the review string (F6) and the first 8 to 14 of every other string, sorted by citations; snowballing stops after one pass that adds no new work on the questions.
- **Grey:** effort bounded at N = 10 results per query, with saturation at k = 3. A query stops being read after 3 consecutive results that add no new concept; vendor blogs repeat each other.
- Q/A sites: effort bounded at N = 30 results by votes per string and site, with saturation at k = 10; stated in the subsection Q/A sites, where the search stopped after string AD15.
- Named producers (arc42, C4, the SEI books) are read to exhaustion, since the pool is small.

## 7. Selection

Include if all hold:

- The subject is how a description of a system's architecture is organised, entered or read, or a review of that.
- The source states who wrote it and when, or can be dated.
- It is in English.
- Its content was read in full, or the review says which part was read.

Exclude if one holds:

- E1: notation and architecture description languages (review system-diagrams).
- E2: decision records (review design-decisions).
- E3: enterprise architecture documentation, another object.
- E4: marketing with no architecture content.
- E5: a figure no one could trace to a source.
- E6: the source could not be read (paywall or bot protection); it is listed as found, not read.
- E7: documentation in general, with no architecture content.
- E8: tools that generate or recover documentation, with no evaluation by readers.
- E9: reviews whose subject is another architecture topic (evolution, evaluation, analysis).

Formal sources carry the evidence grade of the standard (measured, supported with caveat, convention). Grey sources are scored in section 8.

## 8. Quality of grey sources (Garousi Guideline 11, Table 7)

Twenty criteria, each scored 1, 0.5 or 0, in eight groups:

| Group | Criteria | Max |
|---|---|---|
| A authority of the producer | reputable publisher; author tied to a reputable organisation; author's other work; expertise | 4 |
| M methodology | clear aim; stated method; authoritative references; limits stated; specific question; particular case | 6 |
| O objectivity | balanced; objective; no vested interest; conclusions follow the data | 4 |
| D date | clearly stated date | 1 |
| P position | related sources linked or discussed | 1 |
| N novelty | adds something; strengthens or refutes a position | 2 |
| I impact | citations, backlinks, adoption signals, aggregated | 1 |
| T outlet type | tier 1 = 1, tier 2 = 0.5, tier 3 = 0 | 1 |

- Threshold: 10 of 20 to include.
- A source below it is kept only as an example of practice, never as support for a claim; [sources](sources.md) says which, and the text that names it says so.
- A part of a source that was not seen scores 0 on its criteria.

## 9. Extraction and synthesis

- Extracted per source: kind, what it covers, numbers (read in the primary or marked secondary), stated limits, grade.
- Synthesis is narrative by question, traceable through the "used in" column of [sources](sources.md).
- A vendor or owner page is read as its owner's claim about itself.

## 10. Limits

- A second rater re-scored 4 of this topic's grey sources blind ([method](../README.md#method)): 3 of 4 decisions agree; the arc42 site (Starke 2026) scores 9.5 and 12 and stays an example of practice.
- Search engines rank and personalise results and change over time; the dates above are the only anchor.
- The formal engine matched loosely and the counts are not those of a curated database.
- The Helsinki thesis and the Gothenburg essay were read through their abstracts only (bot protection blocked the full text).
- Some reviews were read through abstracts or search summaries and are marked (secondary).
- Recorded talks were not watched.
- Q/A threads of architecture-descriptions: one scorer, no second rater.
