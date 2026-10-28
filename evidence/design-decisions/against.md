# Against: controversies, limits and failed assumptions

This file gathers the evidence against the rules on design documents and decision records: null results, disputed studies, and practice that a study contradicts.

## Whether capturing rationale pays

- Lee 1997 argued rationale systems failed on cost and integration; Capilla 2016 says the cost still limits adoption (both secondary).
- The one lab gain is effectiveness; efficiency did not improve (Falessi 2010), so the reader gets better answers at the same speed, not faster ones.
- The payoff comes later and to someone else, so the writer's incentive is weak (an argument in Lee 1997, not a measurement).
- Ahmeti 2024 found practitioners worry about documenting too much or too little, and about where the record lives.

## Whether one template fits

- Falessi 2008 found the utility of the same information changes with its purpose (secondary).
- Nogueira 2026 concludes template choice should not be one-size-fits-all.
- Attentive 2026 (example only, 9 of 20), a company account of its own experience, says RFC processes decay when documents grow heavy and reviews turn performative.
- Nygard 2011 asks for one or two pages; Ubl 2020 asks for 10 to 20 pages for large designs; both are practitioners' judgment.

## Weaknesses of the strongest study

- Nogueira 2026 is a preprint.
- The subjects are 33 undergraduates.
- The shortlist of two templates came from the two authors scoring five templates themselves.
- The score weights usability, mostly time and perceived objectivity, highest, and weights field identification lowest, so a short template wins by construction in part.
- The task is writing one decision, not reading one.
- Falessi 2010 rests on 50 master students and one system, and says it used students rather than professionals.

## Whether records are proposals

- About 63% of 5,800 ADRs were opened already accepted (Santana 2026, secondary).
- A record written after the decision cannot help anyone judge it first.
- AWS 2026c (example only) and Microsoft 2026 describe both roles; the research above measures neither.

## Whether the document is the lever

- Go proposals are declined most often for poor feasibility (22.8% of declined proposals), obsolescence (18.1%), limited use cases (13.2%) and conflict with principles (11.4%) (Kondo 2025).
- None of these is a writing defect, and the paper does not examine proposal structure or text quality.
- This suggests substance may dominate form in what gets accepted; it is a reading of one project's data, not a result.
- Enacted processes differ from the advertised ones (Keertipati 2016), so a template may describe a process nobody follows.

## Limits of the practice evidence

- Company pages report their owners' own success: Amazon 2021 calls its method central to its success; Nygard 2011 reports his own use since 2011-08.
- Vendor pages (AWS 2026c, Microsoft 2026, Google Cloud 2024) give guidance, not outcomes; AWS 2026c and Google Cloud 2024 score under 10.
- Pragmatic Engineer 2022 lists companies from reader replies; its author notes that the documents are mostly internal and the list rests on public posts and anecdote.
- Repository stars and tag counts measure interest, not reading (GitHub 2026).
- Buchgeher 2023 and Santana 2026 were read in abstract form only.

## Limits of the reviews and of the grey evidence

- Harhio 2022 is a master's thesis with one database (Web of Science) and one engine (Google); its author notes that Google results change between runs.
- Tofan 2014 stops at 2012-01, before ADRs spread; it cannot speak to them.
- Bhat 2020 is a getting-started guide by its own account, not a test of any form.
- Eight of 46 scored grey sources fall below 10 of 20 (sources.md); all eight are used only as examples of practice.
- Perkins 2020 (GitHub's blog) offers no measurement, and Runde 2018 reports two years of use with no metrics: both are experience, not evidence of effect.
- Practitioner advice agrees across sources (one decision per record, record alternatives); agreement among blogs that copy one another is not independent confirmation.
- Reddit was not reached. Software Engineering Stack Exchange and Stack Overflow were searched on 2026-10-28; their threads are opinion with no data (next section).

## What the Q/A threads add against

- Detailed design documents are rarely read and out of date at delivery (SESE 2010d). Keep a short summary of the high-level decisions (SO 2009b), stay at high level and let tests guide the detail (SO 2009a), and document at a coarse grain so the text rarely changes (SESE 2012d). These agree with the cost caveats above; they are practitioners' opinions.
- An ADR is written when a technology or procedure is introduced after assessment, and revised each quarter (SO 2022a; one answer, 2 votes).
- Whether records are proposals: SESE 2015c separates the proposal (future tense) from the design document that replaces it (present tense), which bears on the 63% of ADRs opened already accepted.

## Failed or missing replications

- This search found no replication of Falessi 2006.
- This search found no replication of Nogueira 2026.
- Bratthall 2000 asked the same question as Falessi 2006; its result was not retrieved here, so agreement between the two is not known.
