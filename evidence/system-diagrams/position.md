# Position

This file says what is known about system diagrams, what is not, where this review sits among existing reviews, and what this repository adds.

## Against existing reviews

- Sixteen reviews exist (review.md strand 0). They cover UML evidence (Budgen 2011, Fernández-Sáez 2013), UML use (Koç 2021), notation theory (van der Linden 2019), process-model understandability (Dikici 2018), architecture visualisation (Shahin 2014) and visualisation evaluation (Merino 2018).
- This search found none that isolates reader outcomes of diagrams of a software system, none that includes grey literature, and none that sets practice beside evidence.
- Their shared conclusion agrees with ours: studies are few and small, and each calls for more with realistic participants and settings (Fernández-Sáez 2013, Merino 2018, Dikici 2018).
- This review differs by returning to the primary papers, which showed that the layout and size results come from one group's data (Störrle 2016b).

## Known

- Layout quality and diagram size change how fast and how well readers answer, with the largest effect on novices and on large diagrams (Störrle 2011, 2014, 2016b); the evidence is one group's.
- Flaws in the layout weigh more than the number of elements (Störrle 2016b).
- UML helps on complex maintenance tasks, not on speed (Arisholm 2006).
- Practitioners draw informally and short-lived (Cherubini 2007, Baltes 2014).
- A theory of notations exists and is applied without much verification (van der Linden 2019); its principles are hard to apply objectively (Störrle 2013).
- Respondents found published architecture diagrams missing expected elements (Nicacio 2022, 34 respondents).
- The meaning of an arrow is the recurring confusion in practitioner questions:
  - SO 2021b (20 votes, 18,334 views on the day): there is no rule for the direction of an arrow; show the data flow in an overview and the dependency in a detail view.
  - SESE 2024a: arrows in a data-flow diagram are not dependency arrows. SO 2009d (136,074 views) and SO 2010b: flowchart arrows carry control, data-flow arrows carry data.
  - SO 2014c (example only): one two-way arrow and two arrows are said to mean the same.
  - The guides in the pool (C4: labelled one-way arrows; IcePanel 2023: label every line) already say to label lines. The threads show readers asking what an arrow means, in several forms, so a rule "say what an arrow means in a key" has demand behind it. No study counts the confusion.
- No accepted standard for component types exists (SO 2012a, borderline at 10 of 20); the 4+1 model is offered instead.
- Data-flow diagrams are still used for a high-level view because they de-emphasise control flow and link data stores to the object model (SO 2011c, SO 2010b, SESE 2024a). This agrees with the threat-modelling use in the pool (OWASP 2026, Microsoft 2023) and with Schneider 2024; it adds no evidence on readers.

## Not known (this search did not find it)

- Whether the C4 rules (key, labels, technology) raise accuracy; the only industrial study reports perceptions (Jongeling 2025).
- Whether icon sets help or distract.
- Whether diagrams as code change readers' outcomes, apart from keeping source and picture together.
- Effects of sequence-diagram conventions (lifelines order, activation bars).
- Whether a key helps at all: it was present in both arms of the one test found (Santos 2018).
- Anything for readers who are language models.

## Where practice runs ahead of evidence

- C4 and cloud icon guidance spread by owner publication; no trial found, and the C4 pages score below the quality threshold.
- Mermaid and PlantUML adoption is counted in stars and downloads, not outcomes.
- Threat-model DFDs are standard practice; one small experiment found (Schneider 2024) and one planned (Mbaka 2024).
- Five producers (IcePanel 2023, Brown 2026d, GitLab 2026, Fuchsia 2025, AWS 2026b) converge on labels, a title and consistent shapes; agreement among them is not a test.

## Where evidence is ignored by practice

- Size and flaw limits (Störrle 2016b) appear in no tool or guide found here.
- The finding that graph-drawing rules transfer only partly is absent from tool defaults (not checked in detail).
- Layout control is what engineers miss in text-defined diagrams (Jongeling 2025), and layout is what the experiments measure.

## What this repository adds

- It states a drawing checklist (baseline.md) traced to named sources, each marked by strength of evidence and by whether its source passes the grey quality threshold.
- It keeps adopted rules apart from measured ones.
