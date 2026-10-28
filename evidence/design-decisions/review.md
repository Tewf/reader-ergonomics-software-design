# Review

This file reads the literature on documents that propose or record design decisions. Strands run from existing reviews to surveys, seminal work, studies, mining and practice.
"(secondary)" marks a number read in an abstract or summary, not in the paper. Quality scores for grey sources are in [sources](sources.md); a source under 10 of 20 is named "example only".

## 0. Existing reviews

- Tofan 2014 (read in full): systematic mapping of architectural decisions, 2002-01 to 2012-01; six databases, 28,895 first hits, 144 papers.
  - 83% (120) propose some form of documentation approach; 52 include tool support.
  - Experiments are the least used method: 4% of papers, six in all, one with fourteen architects.
  - It asks for evidence on the real-world benefit of documenting, and for the right amount of documentation.
- Bhat 2020: semi-systematic review of 218 papers over four decades on architectural design decisions; tool support, human aspects and group decision making; a getting-started guide (abstract only).
- Razavian 2019: classifies empirical studies of architecture decision making by logic, purpose, method and process; asks for social-science methods (abstract partly read).
- Hyun 2023: systematic mapping on tracing decisions to artifacts; the knowledge is rarely documented explicitly and no standard for documenting exists (journal page only).
- Harhio 2022 (read in full): the closest, a multivocal review by a master's student.
  - Web of Science and Google; from 2016; 36 scientific papers and 19 grey sources; method after Garousi 2019.
  - Scientific papers mostly propose tools, extraction tools above all; 12 of 19 grey sources concern ADR templates, which the scientific papers do not mention.
  - Benefits are low cost and concise content; drawbacks are high effort and badly organised content.
- Located by title only: Tang 2017, Weinreich 2014, Alexeeva 2016, Li 2013.
- How this review differs:
  - it is about the document, not decision making or tools: the proposal read before adoption and the record read after, as two readers (frame.md);
  - it adds proposal processes (PEP, Rust, Kubernetes, Go, Swift), which none of the above covers;
  - it keeps reader-task evidence apart from writer-side evidence, and most-adopted apart from best-evidence;
  - it adds sources from 2022 to 2026 and scores each grey source on 20 criteria, where Harhio 2022 used a simplified checklist.

## 1. Surveys and maps of the field

- Lee 1997: seven technical and business issues; current systems fail on practical concerns such as cost-effective use and smooth integration (secondary).
- Buckingham Shum 1994: asks what argumentation-based rationale is worth at what cost (title and venue only).
- Regli 2000: groups rationale systems into argumentation-based, descriptive and process-based, by representation, capture and retrieval (secondary).
- Dutoit 2006: the edited volume that fixes the software-engineering vocabulary, **rationale management**; it holds a chapter on barriers (Horner 2006, read by title only).
- Shahin 2009: compares architectural decision models and tools; all agree on the essence of a decision (secondary).
- Capilla 2016: ten-year retrospective on architectural knowledge management ([defined](../architecture-descriptions/frame.md)); the cost of capture hampers wide adoption (secondary).

## 2. Seminal work on representing rationale

- **IBIS**, the issue-based information system, is an early rationale method for large, complex design problems (Conklin 1988); its original 1970 working paper was not located by this search.
- Conklin 1988 (gIBIS): early experiments suggest the method is still incomplete (secondary).
- MacLean 1991 (QOC): questions, options and criteria; a design space analysis is a coproduct of design, not a record made afterwards (secondary).
- Karsenty 1996: an empirical evaluation of rationale documents (CHI); the abstract was not retrieved, so no result is claimed.
- Tyree 2005: a template for documenting architecture decisions explicitly (secondary); its field list was not read.
- Jansen 2005: names knowledge vaporization and views architecture as a set of explicit decisions (secondary).
- Zdun 2013: the source the ADR community cites for the **Y-statement** (ADR 2026).

## 3. Practitioner surveys and interviews

- Tang 2006: survey, 81 valid responses; practitioners value rationale and report barriers to documenting it (secondary).
- Weinreich 2015: 25 architects, leads and senior developers from 22 companies in 10 countries (secondary).
- Groher 2015: the same 25 interviews; individual and cultural factors weigh as much as business ones (secondary).
- Borowa 2023: questionnaire of 63 and 13 interviews; architects favour known or fast-to-build solutions (secondary).
- Ding 2014b: of 2,000 open source projects, 108 had any architecture documentation (secondary).
- Wan 2023: interviews with 32 practitioners from 21 organisations; documentation is among the central challenges (secondary).
- Gebreweld 2023: 34-question survey of 45 architects at one Dutch bank on how architecture knowledge is represented and communicated; a preprint, abstract only.

## 4. Experiments with a reader task

- Bratthall 2000: controlled experiment on predicting change impact with and without design rationale; the result was not retrieved.
- Falessi 2010 reports the Falessi 2006 experiment: 50 master students, decisions on an ambient-intelligence prototype, requirements change.
  - With rationale documented (the DGA method), effectiveness rose for individuals and teams; efficiency did not change.
  - The authors say only one earlier study measured performance in a controlled setting.
- Falessi 2008: the value of the same information depends on its purpose (secondary).
- van Heesch 2013: four student teams over seven weeks, two documenting with decision viewpoints (secondary, abstract in a search summary).
  - The documenting teams explored and evaluated options more systematically.
  - The viewpoints did not help with requirements or complexity.
- Nogueira 2026: crossover, 33 undergraduates documenting one decision per template, Nygard against MADR 2024.
  - Nygard scored higher on a weighted writer-side score: W = 84.0, p = 0.002, Cliff's delta 0.64 (large).
  - Reader comprehension is only whether key fields can be found. Status: preprint.

## 5. Mining of repositories and proposal processes

- Buchgeher 2023: ADRs in open source repositories; adoption low but growing, about half hold one to five records, Nygard's template dominates (secondary).
- Santana 2026: 921 repositories, 5,800 ADRs; about 63% were opened already accepted (secondary, conference page).
- Ahmeti 2024: action research at one company; ADRs helped culture and knowledge transfer, not distributed-system documentation.
- Keertipati 2016 and Sharma 2022: process mining of PEPs; the enacted process is richer than the advertised one (secondary).
- Kondo 2025: 1,095 Go proposals; 448 declined, 337 accepted; reasons are feasibility, use cases and principles, not document form.
- Nakashima 2026: links declined Go proposals to source code, on the premise that their discussions hold design rationale; abstract only.
- Viviani 2021: a classifier finds design discussion in pull requests (AUC 0.87), because design documents are often missing (secondary).
- Adjacent: Gupta 2026 tests LLM generation of ADRs from 750 repositories; three to five prior records worked best as context (abstract only). Whether such records help a reader is not tested there.

## 6. Adjacent: reading a design to judge it

- Parnas 1987: "active design reviews" (title and venue only).
- Basili 1996: perspective-based reading (abstract not retrieved).
- Aurum 2002: review of software inspection processes and their experiments.
- This search did not find a reading-technique experiment on design proposals.
- Zanaty 2018: design discussions in code review (abstract states little is known of their extent).

## 7. Practice

| Who | Since | Form | Evidence of use |
|---|---|---|---|
| Nygard 2011 | 2011 | five-part ADR | own report: 3 months, 6-10 developers |
| ThoughtWorks Radar | 2016 | lightweight ADRs: Trial, then Adopt in 2017 | the owner's assessment |
| MADR, adr.github.io | 2018 | ADR template family | repository counts (state-of-the-art.md) |
| Arc42 2026b | undated | decision section, Nygard-style, significant decisions only | project documentation |
| IBM Watson Discovery | 2018 talk | ADRs in markdown beside the code (Runde 2018) | two years of the speakers' use, no metrics |
| GitHub mobile team | 2020 | ADRs, argued for the author's future self (Perkins 2020) | no measurement; blog |
| AWS, Microsoft, Google Cloud | AWS undated; Microsoft 2026; Google Cloud 2024 | ADR process and content guidance | vendor guidance; AWS and Google Cloud example only |
| GOV.UK, GDS Way | 2025; reviewed 2026 | ADR framework; fields, store with code, supersede not rewrite | published guidance |
| Bitwarden | undated | MADR-based ADRs, pull request review | company page, example only |
| Python | date not checked | PEP 1 (Warsaw 2000), PEP 12 (Goodger 2002) | 746 PEP files |
| Rust | 2014 | RFC template, FCP | 652 merged RFCs |
| Kubernetes | date not checked | KEP template with production readiness review | 643 KEP folders |
| Go | date not checked | issue, then design doc if concerns arise, weekly review group (Go 2026) | 91 design documents; 1,095 proposals (Kondo 2025) |
| Swift | date not checked | pitch, pull request, open review of at least ten days, workgroup decides (Swift 2026) | process page |
| Google | 2020 | design doc, goals and non-goals | personal account of company practice |
| Oxide, HashiCorp, Uber | date not checked | RFD, RFC with status | company pages and press; Oxide and HashiCorp example only |
| Amazon | 2004 | six-pager, PR/FAQ | owners' own account |
| IETF | 2014 | RFC style guide | RFC numbers to 9999 |

- Practitioner articles repeat the same advice: one decision per record, never edit an accepted record, write while the reasoning is fresh, record the alternatives.
- Sources: Polishchuk 2026 and Taylor 2025 (both example only), Kashitsyn 2024 for design docs. None reports data.
