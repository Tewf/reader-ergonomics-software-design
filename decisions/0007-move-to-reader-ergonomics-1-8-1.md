# 0007: Move to reader-ergonomics v1.8.1, and draw the card's figure as the standard does

**Decision:** This repository checks against reader-ergonomics v1.8.1 (commit `539aaf7`). As on the standard's own
card, the flow figure becomes an SVG drawn from a Graphviz source, with the source inline beside it.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; the figure was redrawn by reader-ergonomics-presentations, the family's visual standard.

## Context

- v1.7.0 adds shape-example: each shape shows a filled example of itself. The five shapes here each have one.
- v1.8.0 draws the standard's figures as SVG from their Graphviz source. Its card embeds the SVG and keeps the source
  inline, in a `dot` block, since every agent reads that file as text.
- Presentations redrew this card's typed figure in the same palette. The card was to follow the standard's own when it
  moved, and it has moved.

## Decision

The pin in CI and every text link move to v1.8.1. The card's figure is `standard-how-to-use.svg`, rendered by
presentations' `render_figure.py` and stamped with its source's hash. The card embeds it with a text alternative, and
keeps the source inline in a `dot` block, beside `standard-how-to-use.dot`.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Keep the typed figure | readable as text everywhere; the card differs from the standard's | rejected: the cards of the family part ways |
| SVG only | the site gains; an agent reading the card as text loses the figure | rejected |
| SVG with its source inline, as the standard's card | both readers keep it | chosen |

## Consequences

- Good: on the site the figure is drawn, in the family's palette; as text, the source shows the same graph.
- Bad: the figure lives in three places, the SVG, the `.dot` file and the inline block; a change must be made in the
  file, rendered, and copied inline.
- Bad: rendering needs Graphviz and presentations' script; no check here yet compares the SVG with its source.
- To keep it true: edit `standard-how-to-use.dot`, render it, and replace the inline block in the same commit.

## See also

- The [decisions](README.md) of this repository; [record 0006](0006-move-to-reader-ergonomics-1-6-0.md), the move
  before this one.
