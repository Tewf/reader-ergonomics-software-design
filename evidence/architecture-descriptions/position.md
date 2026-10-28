# Position

This file says what is known about architecture descriptions, what is not, and what this repository adds.

## Against the existing reviews

- Nineteen secondary studies were found (review.md 0). Their subjects are:
  - notations and description languages (Júnior 2019, Viglioni 2024);
  - knowledge-management tools and approaches (Weinreich 2016, Ding 2014a);
  - documentation in general (Zhi 2015, Theunissen 2022, Islam 2023);
  - mined information (de Dieu 2024) and decision records (Harhio 2022).
- What they cover that this review does not: tools, approaches and the volume of research on them.
- What this review adds to them: the organisation and entry of a description as the one subject; a score for every grey source; practice read beside research; a named baseline.
- Where they agree with this review: documentation is outdated and costly to retrieve from (Ding 2014a, Theunissen 2022); capture and maintenance are the weak activities (Weinreich 2016).
- This search did not find a review that answers the sub-questions in state-of-the-art.md.

## Known

- Developers find architecture documentation outdated, scattered and one-size-fits-all (Rost 2013).
- Abstract documentation is trusted longer than detailed documentation (Lethbridge 2003).
- Newcomers seek the broad view of the architecture first (Dagenais 2010).
- In one experiment the format, structured or essay, did not change newcomer scores; familiarity with the code did (Ernst 2023).
- Most open-source projects have little architecture documentation, and what exists is informal, single and rarely updated (Ding 2014b, Migliorini 2024).
- Developers with one task are poorly served by a description split by concern, on a position and a later validation (Rost 2016, secondary).
- Standards and templates agree on a shared skeleton: purpose and stakeholders, context, building blocks, runtime, deployment, cross-cutting concerns, glossary (see baseline.md).

## Not known

- Whether any view scheme, template or number of levels improves reader outcomes.
- Whether an entry page changes time to first correct answer.
- How reviewers and operators use an architecture description; this search did not find a study of them as readers.
- Whether the null result of Ernst 2023 holds for larger systems, for professionals or for other formats such as arc42 (Starke 2026).
- Whether a description that is kept short and stable (the Lethbridge finding, the matklad rule) outperforms a complete one.

## Where practice runs ahead of the evidence

- arc42, C4 and ARCHITECTURE.md are used and taught widely, with no comparative trial found.
- arc42's authors say they know no adoption numbers (Starke 2026b). Eight of the 41 grey sources scored below 10 of 20 (sources.md).
- 42010 defines what conformance is; its own authors do not claim better systems from it, and no study of readers was found.
- Docs as code is credited by its owners for use, not shown to improve understanding.
- Agent context files carry architecture sections in about 70% of cases while two test settings find overviews unhelpful.

## Where evidence is ignored by practice

- Readers ask for task-specific content (Rost 2013); arc42 is one template for all readers, with lean and thorough paths as its only tailoring found here.
- The format may matter little in one setting (Ernst 2023); arc42 and C4 are taught and tooled as formats.
- Staleness is the first wish or challenge in two surveys (Rost 2013, IcePanel 2025), and 75% of mined views are never updated (Migliorini 2024; figure not checked).

## Where practice and research agree without citing each other

- Lethbridge 2003 advises simple, powerful formats that hold what stays valid; matklad 2021 advises recording only what rarely changes. This review found no citation between them.
- One place per fact has a boundary that practice states on its own. SESE 2010a asks whether an architecture description breaks the DRY principle. The answers: it is a different level of description that the code cannot give, and DRY is a reason to weigh. Duplicating the same fact at the same level is the cost; a description at another level is not. The repository's own rule should read "same fact, same level".
- Keeping a description true (Q6), experience only: SESE 2012b (a champion who grows a shared document organically) and SESE 2019a (modelling a built distributed system in full is almost impossible).

## What this repository adds

- A baseline and a checklist that tie each rule to a reader task and a source (baseline.md).
- A score for each practice source, so a claim about practice states how far to trust it.
- A measurement plan that reuses the Ernst 2023 instrument, so a result can be compared with a published one.
- A distinction between the artefact (the description) and the architecture it describes, which the standards make and many templates blur.
