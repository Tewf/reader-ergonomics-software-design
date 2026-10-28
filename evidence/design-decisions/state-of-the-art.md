# State of the art, per sub-question

Two records are kept apart: **most adopted** (what people use) and **best evidence** (what a study measured).

| Sub-question | Most adopted | Best evidence | Measured how |
|---|---|---|---|
| What a decision record holds | Nygard 2011 (title, status, context, decision, consequences) | Nogueira 2026, writer-side, 33 students | crossover, weighted score |
| Whether recorded rationale helps later decisions | ADR practice | Falessi 2010 (the 2006 experiment); van Heesch 2013 | 50 students, effectiveness under changed requirements; four student teams over seven weeks |
| How a proposal is structured | PEP 12 (Goodger 2002), Rust RFC template (Rust 2026b), KEP template (Kubernetes 2026), Google design doc, Swift proposal template (Swift 2026) | none found | descriptive comparison of templates only |
| How a proposal is judged | Rust final comment period (Rust 2026a), Steering Council (Warsaw 2000), SIG approvers (KEP template), Go weekly review group (Go 2026), Swift review manager and workgroup (Swift 2026) | Kondo 2025 (Go) | 1,095 classic proposals, coded decline reasons |
| Whether people adopt ADRs | Nygard's template in open source | Buchgeher 2023 | repository mining |
| Why rationale is not captured | cost, effort | Lee 1997; Tang 2006; Ahmeti 2024; Tofan 2014 asks for the right amount | argument, survey of 81, one action study |
| How much research exists on documenting decisions | n/a (a research record) | Tofan 2014: 83% of 144 papers propose documentation; 4% use experiments (counts not checked) | systematic mapping, 2002-2012 |
| Which rationales drive decisions | decision drivers in MADR 2024 | Weinreich 2015; Borowa 2023 | 25 interviews; 63 answers and 13 interviews |
| Which documentation practice practitioners write about | ADR templates: 12 of 19 grey sources (Harhio 2022) | none found | review of grey sources, 2016 onward |

## Adoption counts, descriptive, taken 2026-10-28

| Count | Value | Caveat |
|---|---|---|
| merged Rust RFC files | 652 | numbers reach 3999 because they follow pull request numbers |
| PEP files | 746 | highest is 8107 |
| KEP folders with a kep.yaml | 643 | |
| Go design documents in the proposal repository | 91 | proposals themselves are issues; Kondo 2025 counted 1,095 classic ones |
| RFC Editor index | numbers to 9999 | a script count gave 8,995 numbered entries, 122 marked Not Issued; the gap was not investigated |
| repositories tagged adr | 875 | self-tagged, includes tools |
| repositories tagged architecture-decision-records | 488 | overlap with the line above unknown |
| stars: adr-tools, MADR, the ADR collection repository | 5,747; 2,595; 17,342 | interest, not use |

- The counts come from public repository listings and the GitHub API; the API search totals are approximate.
- A count of records says nothing about whether they were read (GitHub 2026).

## What the templates share

| Part | Nygard | MADR | PEP | Rust RFC | KEP | Google doc | HashiCorp (example only) |
|---|---|---|---|---|---|---|---|
| status | yes | optional | header | no | yes | no | yes |
| context or motivation | yes | yes | yes | yes | yes | yes | yes |
| goals and non-goals | no | drivers | no | no | yes | yes | no |
| decision or proposal | yes | yes | specification | reference-level | design details | design | proposal |
| alternatives | no | options, pros and cons | rejected ideas | rationale and alternatives | alternatives | alternatives | abandoned ideas |
| consequences or drawbacks | yes | optional | backwards compatibility | drawbacks | risks, drawbacks | cross-cutting | no |
| open questions | no | no | open issues | unresolved questions | no | no | no |

- "no" means the section is not among those the template or guide lists. The table is read from the templates (Nygard 2011; MADR; PEP 12; Rust RFC template; KEP template; Ubl 2020; HashiCorp 2026, example only).
- Among these seven, only the Rust RFC template asks for prior art and only the KEP template asks for a production readiness review.
- Nygard 2011 has no alternatives section; MADR added one, which participants in Nogueira 2026 saw as better for rationale depth and slower to fill in.
- ADR guidance treats an accepted record as immutable: write a new record that supersedes the old (GDS 2026; Microsoft 2026; AWS 2026c, example only).
- PEPs carry a change history (PEP 12) and published RFDs may be updated (Oxide RFD 1, Frazelle 2026).

## Upper bounds (achieved)

- Rationale documentation raised decision effectiveness under changed requirements in a lab (Falessi 2010).
- Decision viewpoints made student teams more systematic in weighing options, in one multiple-case study (van Heesch 2013).
- ADR template comparison has a first controlled experiment (Nogueira 2026).
- Research volume on documenting decisions is mapped (Tofan 2014) and the grey side has a first review (Harhio 2022).
- Decline reasons for design proposals have a coded taxonomy (Kondo 2025).
- ADR use has been counted in open source (Buchgeher 2023; Santana 2026).

## Lower bounds (not yet shown)

- This search did not find a study where reviewers judge a design proposal in two document forms.
- This search did not find a study that ties a proposal template to the quality of the decision made.
- No evidence was found that Nygard's or MADR's shape helps a maintainer recover why, as opposed to helping the writer write.
- No study of the effect of the "rejected alternatives" section on repeated debate was found.
- Bratthall 2000 and Karsenty 1996 may hold relevant results; their text was not read.
- Q/A sites (searched 2026-10-28) hold no report of how a proposal is judged (Q4) or whether a team keeps ADRs (Q5).
