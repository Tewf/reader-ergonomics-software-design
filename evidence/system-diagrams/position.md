# Position

This file says what is known about system diagrams, what is not, and what this repository adds.

## Known

- Layout quality and diagram size change how fast and how well readers answer, with the largest effect on novices and on large diagrams (Störrle 2011, 2014).
- UML helps on complex maintenance tasks, not on speed (Arisholm 2006).
- Practitioners draw informally and short-lived (Cherubini 2007, Baltes 2014).
- A theory of notations exists and is applied without much verification (van der Linden 2019).

## Not known (this search did not find it)

- Whether the C4 rules (key, labels, technology) raise accuracy.
- Whether icon sets help or distract.
- Whether diagrams as code change readers' outcomes, apart from keeping source and picture together.
- Effects of sequence-diagram conventions (lifelines order, activation bars).
- Anything for readers who are language models.

## Where practice runs ahead of evidence

- C4 and cloud icon guidance spread by owner publication; no trial found.
- Mermaid and PlantUML adoption is counted in stars and downloads, not outcomes.
- Threat-model DFDs are standard practice; one small experiment found (Schneider 2024).

## Where evidence is ignored by practice

- Size limits (Störrle 2014) appear in no tool or guide found here.
- The finding that graph-drawing rules transfer only partly is absent from tool defaults (not checked in detail).

## What this repository adds

- It states a drawing checklist (baseline.md) traced to named sources, each marked by strength of evidence.
- It keeps adopted rules apart from measured ones.
