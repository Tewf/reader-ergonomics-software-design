# 0009: Move to reader-ergonomics v1.10.0

**Decision:** This repository checks against reader-ergonomics v1.10.0 (commit `c08433c`), which adopts the family's
four figure checks; nothing here changes but the pin.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; the family's figure review, released by reader-ergonomics.

## Context

- v1.10.0 gathers the family's figure checks in the standard:
  - `typed-figure` warns on a figure drawn in characters;
  - `figure-alt` fails an image without a text alternative;
  - `figure-contrast` fails a line under 3:1 against its ground;
  - `figure-source` fails an SVG drawn from a `.dot` without the stamp of its source.
- Run on this repository before the move, the release found no error and no warning. The card's SVG already carries
  its stamp (record 0007), and the flow diagrams have their alt text and solid strokes.

## Decision

The pin in CI and every text link move to v1.10.0. No file is redrawn and the config is unchanged.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.9.0 | no change; a figure that loses its alt text or contrast goes unnoticed | rejected |
| Move to v1.10.0 | the figure rules are checked on every push | chosen |

## Consequences

- Good: every figure here is checked for its text alternative, its contrast and its source on each push.
- Bad: the contrast floor and the dark ground are PROVISIONAL in the standard; a change there may ask for a redraw.
- Bad: the flow diagrams are drawn by a script kept outside this repository, so a failure there is fixed in that
  script first.
- To keep it true: the next pin move repeats the link move, as records 0001 and 0008 ask.

## See also

- The [decisions](README.md) of this repository; [record 0008](0008-move-to-reader-ergonomics-1-9-0.md), the move
  before this one.
