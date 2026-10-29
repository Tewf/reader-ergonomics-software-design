# Every diagram has a key, every arrow a label

**Claim:** every diagram of a system has a key, and every arrow says what it carries, in the direction it points.

- **Grade:** convention, untested.
- **Evidence:** [system-diagrams review](../../evidence/system-diagrams/review.md); [position](../../evidence/system-diagrams/position.md); [baseline](../../evidence/system-diagrams/baseline.md).
- **Check:** `diagram-keys` (exact): each Mermaid diagram is followed by a Key table, and each flowchart arrow carries a label.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- Under every diagram, a table that says what each shape, line and colour means.
- On every arrow, what flows and how, as a short label.
- The diagram's source as text beside the picture, so both change together.

## Why

- Readers ask what an arrow means, in questions on data-flow, component and flowchart diagrams with thousands of
  views.
- The C4 rules ask for a key and labelled one-way arrows (Brown 2026b, an example of practice).
- With a key present, a clearer symbol set gave no gain in accuracy or speed, in 57 novices (Santos 2018): the key may
  matter more than the symbols.

## Limits

- No study compares a diagram with a key and the same diagram without one.
- The check reads Mermaid flowcharts only; other diagrams are checked for their key alone.
- Layout flaws weigh more than size on readers (Störrle 2016b, measured, one group); that rule is in the
  [system diagram](../../shapes/system-diagram.md) shape, since no program here measures layout.
