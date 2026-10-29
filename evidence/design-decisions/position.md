# Position

Each "not known" below is a statement about this search, not about the world.

## Against the existing reviews

- Tofan 2014 and Bhat 2020 map research on architectural decisions.
- Tofan 2014 (full text read) counts documentation approaches: 83% of 144 papers. Bhat 2020 was read by abstract only.
- This search found no comparison of document forms or readers in either.
- Harhio 2022 is the nearest: a multivocal review of documentation methods since 2016. It finds practice centred on ADR templates and research centred on tools.
- This review adds: proposals before adoption beside records after; reader-task evidence kept apart from writer-side evidence; adoption counts; sources from 2022 to 2026; a 20-criterion score for every grey source.
- This search did not find an earlier multivocal review that covers proposal processes such as PEP, RFC and KEP.
- Tofan 2014 asked for the right amount of documentation; the question is still open in this search (Not known, below).

## Known

- Practitioners say design rationale matters and report barriers to writing it (Tang 2006; Weinreich 2015).
- The barrier named longest is cost: capture effort, integration, and a payoff that falls on someone else later (Lee 1997; Capilla 2016).
- One laboratory experiment found rationale documentation raised decision effectiveness when requirements changed, with no gain in efficiency (Falessi 2010).
- The value of the same rationale depends on its intended use (Falessi 2008).
- ADRs are tried more than kept: about half of repositories with ADRs hold one to five (Buchgeher 2023).
- Proposal templates in Python, Rust, Kubernetes, Google (Ubl 2020) and, as an example only, HashiCorp 2026 share a core: motivation, design, alternatives, drawbacks (state-of-the-art.md).
- Go proposals are declined most often for feasibility, obsolescence, use cases and principles, not for document form (Kondo 2025).
- A first controlled comparison of two ADR templates exists, on the writer's side (Nogueira 2026).

## Not known

- Whether practitioners use the decision-record vocabulary at all. On Software Engineering Stack Exchange and Stack Overflow it is almost absent (9 and 30 results for `architecture decision record`, one about ADRs). The problem appears as forgetting why (SESE 2016a). This is a statement about two sites searched on 2026-10-28.
- Whether any proposal template helps a reviewer find flaws: this search found no such experiment.
- Whether any decision record helps a maintainer recover why, measured on the maintainer.
- Whether length matters: Nygard 2011 asks for one or two pages, Ubl 2020 for 10 to 20 for large designs, with no comparison.
- Whether a rejected-alternatives section reduces repeated debate; PEP 1 (Warsaw 2000) claims so, and HashiCorp 2026 (example only) repeats it.
- Whether immutable records beat editable ones for recovery.
- Whether reading techniques proven for code and requirements (Basili 1996, Parnas 1987) transfer to proposals.

## Where practice runs ahead of the evidence

- ADRs reached Adopt on the ThoughtWorks Radar in 2017 (ThoughtWorks 2018); the one controlled comparison appeared in 2026 and is a preprint.
- Nygard's template is the default in open source (Buchgeher 2023, secondary) and is suggested in GDS internal guidance (GOV.UK 2025, secondary); its evidence is its author's report of use since 2011-08.
- Sections added by process owners, such as prior art (Rust RFC template, Rust 2026b) or a production readiness review (KEP template, Kubernetes 2026), have no measured effect on review.
- Alternatives considered is called one of the most important sections (Ubl 2020), untested.
- Silent reading before a review meeting (Amazon 2021, secondary) is untested.
- Practitioner advice (one decision per record, write while the reasoning is fresh, never edit an accepted record) is repeated across blogs without data (Polishchuk 2026 and Taylor 2025, example only).

## Where evidence is ignored by practice

- Rationale should be tailored to its use (Falessi 2008); practice ships one template for every reader.
- Tofan 2014 found experiments are rare in this field (4% of 144 papers); practice did not wait for them.
- Records are written after the fact: about 63% of 5,800 ADRs were opened already accepted (Santana 2026, secondary), so the Proposed state that GDS 2026 describes is often skipped (an inference).
- Enacted proposal processes differ from advertised ones (Keertipati 2016; Sharma 2022), yet templates describe the advertised one.

## What this repository adds

- It reads the problem from the reader's side: two moments, two tasks (frame.md), where the literature mostly measures the writer.
- It states a named baseline and how to compare against it (baseline.md).
- It offers candidate rules for the shapes of a proposal and a record, each a hypothesis graded **convention, untested**:
  - open with the decision asked for, its status and what the reviewer must decide ([overview first](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/document/overview-first.md));
  - keep each rejected option with the reason it lost;
  - list consequences for every option, not only the chosen one;
  - keep proposal and record as two documents of one mode each ([one mode per document](https://github.com/Tewf/reader-ergonomics/blob/6980fa64583912922d6f5b5c01316749d654345f/principles/document/one-mode-per-document.md)), linked both ways.
- It does not claim a new result or the state of the art.
