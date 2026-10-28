# Review

Surveys first, then the seminal work, then the empirical studies, then practice.
"(secondary)" marks a number read in an abstract or summary, not in the paper.

## 1. Surveys and maps of the field

- Lee 1997: seven technical and business issues; current systems fail on practical concerns such as cost-effective use and smooth integration (secondary).
- Regli 2000: groups rationale systems into argumentation-based, descriptive and process-based, by representation, capture and retrieval (secondary).
- Dutoit 2006: the edited volume that fixes the software-engineering vocabulary, **rationale management**; it holds a chapter on barriers (Horner 2006, read by title only).
- Shahin 2009: compares architectural decision models and tools; finds all agree on the essence of a decision (secondary).
- Capilla 2016: ten-year retrospective on architectural knowledge management ([defined](../architecture-descriptions/frame.md)); the cost of capture hampers wide adoption (secondary).

## 2. Seminal work on representing rationale

- **IBIS**, the issue-based information system, is an early rationale method, developed for large, complex design problems (Conklin 1988); its original 1970 working paper was not located by this search.
- Conklin 1988 (gIBIS): early experiments suggest the IBIS method is still incomplete (secondary).
- MacLean 1991 (QOC): questions, options and criteria; a design space analysis is a coproduct of design, not a record made afterwards (secondary).
- Karsenty 1996: an empirical evaluation of rationale documents (CHI); the abstract was not retrieved, so no result is claimed here.
- Tyree 2005: a template for documenting architecture decisions explicitly, to make rationale visible to all stakeholders (secondary); its field list was not read.
- Jansen 2005: names knowledge vaporization and views architecture as a set of explicit decisions (secondary).
- Zdun 2013: sustainable decisions; the source the ADR community cites for the **Y-statement** (adr.github.io, ADR 2026).

## 3. Practitioner surveys and interviews

- Tang 2006: survey, 81 valid responses; practitioners value rationale and report barriers to documenting it (secondary).
- Weinreich 2015: 25 architects, leads and senior developers from 22 companies in 10 countries, interviewed on kinds and documentation of decisions (secondary).
- Groher 2015: the same 25 interviews, read for how decisions are organised; individual and cultural factors weigh as much as business ones (secondary).
- Borowa 2023: questionnaire of 63 and 13 interviews on which rationales drive decisions; architects favour known or fast-to-build solutions (secondary).
- Ding 2014b: of 2,000 open source projects, 108 had any architecture documentation (secondary).
- Wan 2023: interviews with 32 practitioners from 21 organisations; documentation is among the central challenges (secondary).

## 4. Experiments with a reader task

- Bratthall 2000: controlled experiment on predicting change impact with and without design rationale; the result was not retrieved.
- Falessi 2010 reports the Falessi 2006 experiment: 50 master students, decisions on an ambient-intelligence prototype, requirements change.
  - With rationale documented (the DGA method), effectiveness rose for individuals and teams.
  - Efficiency did not change.
  - The authors say only one earlier study measured performance in a controlled setting.
- Falessi 2008: a second experiment; the value of the same information depends on its purpose, so documentation should be tailored (secondary).
- Nogueira 2026: crossover experiment, 33 undergraduates documenting one decision per template, Nygard against MADR 2024.
  - Measure: a weighted score of field identifiability, time, objectivity and recommendation.
  - Nygard scored higher: Wilcoxon W = 84.0, p = 0.002, Cliff's delta 0.64 (large).
  - The score measures the writer's side; reader comprehension is only whether key fields can be found.
  - Status: preprint.

## 5. Mining of repositories and proposal processes

- Buchgeher 2023: ADRs in open source GitHub repositories; adoption low but growing, about half hold one to five records, Nygard's template dominates (secondary).
- Santana 2026: 921 repositories, 5,800 ADRs; about 63% were opened already accepted, skipping deliberation (secondary, conference page).
- Ahmeti 2024: action research at one company; 7 interviews, 6 survey answers, two teams, three months; ADRs helped culture and knowledge transfer, not distributed-system documentation.
- Keertipati 2016 and Sharma 2022: process mining of PEPs; the enacted process is richer than the advertised one (48 new activities, 199 pathways, 6 stages in Sharma 2022) (secondary).
- Kondo 2025: 1,095 Go proposals; 448 declined, 337 accepted; reasons are about feasibility, use cases and principles, not document form.
- Viviani 2021: a classifier finds design discussion in pull requests (AUC 0.87), because design documents are often missing (secondary).

## 6. Adjacent: reading a design to judge it

- Parnas 1987: "active design reviews", a design review technique (title and venue only; abstract not retrieved).
- Basili 1996: perspective-based reading, an empirically investigated reading technique (abstract not retrieved).
- Aurum 2002: review of software inspection processes and their experiments.
- This search did not find a reading-technique experiment on design proposals.
- Zanaty 2018: design discussions in code review (abstract states little is known of their extent).

## 7. Practice

| Who | Since | Form | Evidence of use |
|---|---|---|---|
| Nygard 2011 | 2011 | five-part ADR | own report: 3 months, 6-10 developers |
| ThoughtWorks Radar | 2016 | lightweight ADRs: Trial, then Adopt in 2017 | the owner's assessment |
| MADR, adr.github.io | 2018 | ADR template family | repository counts (state-of-the-art.md) |
| AWS, Microsoft | AWS undated (AWS 2026c); Microsoft page updated 2026 | ADR process and content guidance | vendor guidance |
| GOV.UK | 2025 | ADR framework for the public sector | published guidance |
| Python | date not checked | PEP 1 (Warsaw 2000), PEP 12 (Goodger 2002) | 746 PEP files |
| Rust | 2014 | RFC template, FCP | 652 merged RFCs |
| Kubernetes | date not checked | KEP template (Kubernetes 2026) with production readiness review | 643 KEP folders |
| Google | 2020 | design doc, goals and non-goals | personal account of company practice |
| Oxide, HashiCorp, Uber | date not checked | RFD, RFC with status | company pages and press |
| Amazon | 2004 | six-pager, PR/FAQ | owners' own account |
| IETF | 2014 | RFC style guide | RFC numbers to 9999 |
