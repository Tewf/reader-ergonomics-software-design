# Review

Order: surveys, standards and models, readers and their needs, experiments, what projects write, then practice.
A number marked (secondary) was read in an abstract or a summary only; the others were read in the paper.

## 1. Surveys

- Ding 2014a: systematic review of 60 studies on knowledge-based approaches in software documentation, with an emphasis on architecture documentation (secondary). Architecture understanding is the top benefit found; the cost of retrieving information from documents is the main concern.
- Steinmacher 2015: systematic review of barriers faced by newcomers to open-source projects, 20 primary studies, 15 barriers in five categories, one of them documentation (secondary).
- Malavolta 2013: interviews with 48 practitioners from 40 companies in 15 countries about architectural languages (secondary). Practitioners were satisfied with design features and not with analysis; the languages used mostly came from industry, not research.
- Aghajani 2019 mined 878 documentation artefacts into a taxonomy of documentation issues (secondary).
- Aghajani 2020 surveyed 146 practitioners on issues and on which documentation types help which tasks, software structure and architecture design among the tasks (secondary).
- This search did not find a systematic review whose subject is the organisation of an architecture description for its reader.

## 2. Standards and models

- Perry 1992 opened the field. Soni 1995 surveyed industrial systems and found four structures: conceptual, module interconnection, execution, code (secondary).
- Kruchten 1995 proposed five concurrent views: logical, process, development, physical, and scenarios that tie them together.
- Clements 2010 (Views and Beyond): document by views of three kinds (module, component-and-connector, allocation) plus information that applies across views. The SEI template opens with a roadmap and ends with mappings between views, referenced material and a glossary (outline read in a summary, secondary).
- Rozanski 2011: a catalogue of viewpoints (context and six core ones) and cross-cutting perspectives. It argues against one overloaded model.
- ISO 2022 (42010, second edition): a conforming description identifies stakeholders and concerns, and defines viewpoints that frame them. It gives views, records correspondences between views, and gives rationale for key decisions (requirements as listed for the 2011 edition, ISO 2022 FAQ).
- The second edition (2022) adds stakeholder perspectives, architecture aspects, and entity of interest in place of system of interest.
- 42010 defines no required viewpoint and no format; its authors do not claim that conformance gives better systems, only more understandable descriptions.
- Emery 2009: every description needs a framework, meaning the conventions that choose the viewpoints.
- Grade of all of the above: convention, untested for reader outcomes.

## 3. Readers and their needs

- Lethbridge 2003 (three studies, one a survey of 48 engineers at a telecom company, 25 answering the timing question):
  - Documentation is often not updated; stale documentation is still useful (81% agreed, 45 respondents).
  - The more abstract a document, the more engineers trusted it; accuracy and consultation correlated at 0.41 for architectural documents (p < .05).
  - 61% rated documentation effective for learning a system, 46% for big-picture information, 35% for maintaining one.
  - In observation they consulted documentation in 12 of 357 logged events (3%), far below self-report.
- Rost 2013: survey of 147 industrial participants (46% developers, 23% architects, 20% managers).
  - Overall quality rated average by 48%, good by 29%, poor by 18% (N=106).
  - Most frequent complaint in open answers: unclear structure (13 of 42 answers).
  - Wishes: up to date (19 mentions), in sync with code (18), specific to stakeholder and task (14), a system overview (11), rationale (10).
  - Natural language and UML dominate; formal languages are rare; information is usually scattered across documents.
- Dagenais 2010: grounded theory from 18 newcomers in 18 projects (secondary). Newcomers sought the architecture mostly for a broader view and to see where their task fitted (quoted in Ernst 2023).
- de Dieu 2022: survey of 103 developers on searching for architectural information (secondary). The top difficulties were dispersion and abundance of sources.
- Rukmono 2026: interviews with 17 professionals (9 explainers, 8 explainees) show that written documentation is incomplete, so teams explain orally; a good explanation fits the explainee's role, experience and goal.
- Grade: supported with caveat; all are perceptions, and the one behavioural number (3%) is below the stated use.

## 4. Experiments and field trials

- Ernst 2023: 65 students at two universities read about 1,000 words on a 10 kSLOC system, in 75 minutes, in one of two formats, then answered four questions from Bloom level I to VI.
  - Formats: Views and Beyond (9 headers, 13 list items, 6 links) against an essay (no headers); same content, three diagrams each.
  - Result: no significant association between format and score. Prior exposure to the code was the dominant factor (+0.95 points, 95% credible interval 0.28 to 1.68, on a four-point scale).
  - Navigability was rated favourable by 80% with the structured format and 55% with the essay; not significant.
  - Authors' reading: the essay may suit overviews and the structured format coding tasks.
- de Graaf 2016: two industrial case studies compared file and directory organisation with an ontology and wiki organisation. Better organisation correlated with retrieval efficiency and effectiveness (secondary).
- Kazman 2016: the authors wrote and publicised an architecture document for the Hadoop file system and tracked its effects. Results were mixed by measure; the issue tracker already held architectural discussion; newcomers and adopters still needed explicit documentation (secondary).
- Arisholm 2006 and Dzidek 2008 (UML design documents in maintenance, a different object from an overview): correctness improved on complex tasks. Dzidek reports +54% functional correctness and +14% time, the time difference not significant (secondary).
- Robillard 2016: interviews with 18 authors of essay chapters on open-source architecture, on what shapes their content (secondary).

## 5. What projects actually write

- Ding 2014b: of 2,000 open-source projects, 108 had some architecture documentation (secondary); natural language was the usual form.
- Muszynski 2022: six open-source systems; mostly natural language on websites and wikis; most stayed at the first maturity level (secondary).
- Migliorini 2024: 15 thousand architecture views from 12.2 thousand repositories.
  - Most projects keep one view; 96% of 373 sampled views are informal, 7% of the views with colour carry a legend.
  - 75% of views are never updated; over 92% have one contributor.
  - 53% show the whole system and 53% are at a coarse granularity; deployment and control flow are the common viewpoints.

## 6. Practice (industry)

All entries in this section are owners' claims about themselves unless stated; the grade is convention, untested, and an adoption count is measured, descriptive.

- **arc42** (Starke 2026; since 2005 by its own account): twelve sections. They run from Introduction and Goals through Constraints, Context and Scope, Solution Strategy, Building Block View, Runtime View, Deployment View, Crosscutting Concepts, Decisions, Quality Requirements, Risks, to Glossary. It offers lean and thorough tips and a one-page canvas. No adoption count found.
- **C4** (Brown): four levels of abstraction (system, container, component, code), plus landscape, dynamic and deployment diagrams; notation and tooling independent.
  - A vendor survey (IcePanel 2025, 75 respondents, vendor of C4 tooling): 70% moderately or very confident with C4; context diagrams used by 81%, containers 79%, components 41%; keeping documentation current was the top challenge.
  - Jongeling 2025: one embedded-software company, C4 in text diagrams beside the code; most of 48 respondents were positive two years on (secondary).
- **ARCHITECTURE.md** (matklad 2021): for projects of 10 to 200 thousand lines. A bird's-eye overview, a codemap that answers where the thing that does X lives, named invariants, boundaries, cross-cutting concerns; keep it short and to stable facts. The claim that finding the place to change costs ten times more for an outsider is the author's anecdote.
- **Docs as code**: Backstage 2020 says its documentation plugin accounts for about 20% of Spotify's internal portal traffic and credits docs kept as Markdown beside the code (owner's claim). Thoughtworks 2020 put diagrams as code at Trial.
- **Agent context files**: Chatlatanagulchai 2025 (2,303 files, 1,925 repositories) found architecture content in 68.1%. Zarzycki 2026 found such files in 26.3% of 22,854 popular repositories; architecture in about 70% of instruction sets and a system overview in about 48% (corrected estimates).
- Gloaguen 2026 tested context files on coding agents: no general gain in task success, over 20% more cost; repository overviews were not helpful. See also the LLM-reader evidence in reader-ergonomics.
- Forward citations: Rost 2013 is cited by the OSS and view studies above (Ding 2014b, Migliorini 2024) and by de Graaf 2016. Ernst 2023 has 16 citing papers in a citation index, and this search found none that replicates it.
