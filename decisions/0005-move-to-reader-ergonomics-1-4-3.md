# 0005: Move to reader-ergonomics v1.4.3

**Decision:** This repository checks against reader-ergonomics v1.4.3 (commit `d48ffbe`). The release adds the
figure-width check and corrects two sources; nothing in this repository's config changes.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; the standard's releases v1.4.0 to v1.4.3.

## Context

- v1.4.0 adds figure-width, which warns when a figure drawn in characters is wider than 60 columns. Three blocks here
  were wider, and were fixed before the move: the card's flow figure, and two blocks of search strings that are now
  tables.
- v1.4.2 says what Tang 2006 measured, read in full. This repository had the same wrong sentence in a principle and
  corrected it from the same reading.
- The extension contract is redrawn but unchanged: links, local checks and config work as before.

## Decision

The pin in CI and every text link move to v1.4.3, with the commit in the system-diagram example. The config keeps
what it had: the default width of 60 columns fits every figure here.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.3.2 | no change; the text links cite Tang 2006 with the wording both repositories dropped | rejected: the text and the standard disagree |
| Move, and run figure-width as a local check | the same check written twice | rejected: one fact in two places |
| Move to v1.4.3 | the width check runs from the standard, and the links show the corrected sources | chosen |

## Consequences

- Good: CI now warns on a figure that a phone would cut off, without a local copy of the check.
- Bad: the width of 60 columns is PROVISIONAL in the standard; if it changes, figures here may need redrawing.
- To keep it true: the next pin move repeats the link move, as records 0001 and 0004 ask.

## See also

- The [decisions](README.md) of this repository; [record 0004](0004-move-to-reader-ergonomics-1-3-2.md), the move
  before this one.
