# 0012: Move to reader-ergonomics v1.13.0, and hand it the standard-links check

**Decision:** This repository checks against reader-ergonomics v1.13.0 (commit `7a76cc6`), whose standard-links
check replaces the local one written here.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** the open question of the design-document example, answered here and adopted by reader-ergonomics.

## Context

- Record 0001 pins every link into the standard at the release CI checks against. The links moved with the pin by
  hand, and a check held only the workflows to one commit.
- This repository wrote standard-links: a link into the standard must name the pinned commit or the release tag the
  workflow names. Run on the family, it found two stale links in a sibling, since fixed.
- v1.13.0 adopts it unchanged, so the same check would otherwise run twice.

## Decision

The pin in CI and every text link move to v1.13.0. The local `standard_links.py` and its tests go; the standard's
check of that name runs instead.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.12.0 with the local check | no change; the check lives here only | rejected: every extension would copy it |
| Move, and keep the local check | the same check twice, once under each tier | rejected: one fact in two places |
| Move, and drop the local check | one check in the standard, run by the whole family | chosen |

## Consequences

- Good: a link left behind at a pin move fails CI in every repository of the family, not only here.
- Bad: a change to the check is now made in the standard, at its release pace.
- To keep it true: raise the workflows and the links in one commit; both pin checks then pass together.

## See also

- The [decisions](README.md) of this repository; [record 0011](0011-move-to-reader-ergonomics-1-12-0.md), the move
  before this one.
