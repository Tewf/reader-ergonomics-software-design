# 0008: Move to reader-ergonomics v1.9.0, and fold the figure's source

**Decision:** This repository checks against reader-ergonomics v1.9.0 (commit `e886447`). The card's Graphviz source
now sits folded under its figure, closed until clicked, by the family rule this release checks.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; a family rule set by Mohamed, carried by reader-ergonomics v1.9.0.

## Context

- Record 0007 drew the card's flow figure as an SVG and kept its Graphviz source inline, open, under it.
- Mohamed set a rule for the family: a figure is there to be read, so its source sits under it in a `<details>`
  fold, for whoever wants to reuse it.
- v1.9.0 checks it with figure-source-inline: a figure with no folded source warns, and a copy that differs from its
  `.dot` file is an error. This repository had one warning, on that figure.

## Decision

The pin in CI and every text link move to v1.9.0. The inline `dot` block under the card's figure goes inside
`<details>` with the summary "Graphviz source", as on the standard's own card.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.8.1 | the source stays open, against the family rule | rejected |
| Move, and drop the inline copy | the file reads as a bare image to an agent | rejected: the copy is why 0007 kept it |
| Move, and fold the inline copy | the figure first; the source one click away, and checked against its file | chosen |

## Consequences

- Good: a reader meets the figure, not forty lines of source; an agent reading the file still finds the graph.
- Good: the gap record 0007 named is half closed, since a stale inline copy is now an error. Nothing yet compares the
  SVG with its source here.
- Bad: on a renderer that ignores `<details>`, the source shows open, as before.
- To keep it true: edit the `.dot` file, render it, and replace the folded copy in the same commit.

## See also

- The [decisions](README.md) of this repository; [record 0007](0007-move-to-reader-ergonomics-1-8-1.md), which this
  one amends.
