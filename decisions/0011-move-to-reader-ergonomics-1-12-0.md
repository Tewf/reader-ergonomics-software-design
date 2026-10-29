# 0011: Move to reader-ergonomics v1.12.0

**Decision:** This repository checks against reader-ergonomics v1.12.0 (commit `adb53c5`), whose standard-pin check
holds every workflow that checks out the standard to one commit.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; a release of the standard, after a sibling's site was found loading an older stylesheet.

## Context

- A sibling's pin moves had raised its checks workflow alone, so its site kept loading the stylesheet of an older
  release.
- Here the three checkouts already named one commit: each move raised them together. v1.12.0 makes that a check,
  standard-pin, which found nothing here before the move.

## Decision

The pin in the checks workflow, both its jobs, and in the site workflow moves to v1.12.0, with every text link and
the system-diagram example. Nothing else changes.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.11.0 | the three refs stay equal by habit only | rejected |
| Move to v1.12.0 | a ref left behind at the next move fails CI | chosen |

## Consequences

- Good: a pin move that forgets one workflow is caught on its own push.
- Bad: one more pin move, with 67 links rewritten and the answers on those files carried again.
- To keep it true: raise all three refs and the links in one commit, as records 0001 and 0010 ask.

## See also

- The [decisions](README.md) of this repository; [record 0010](0010-move-to-reader-ergonomics-1-11-0.md), the move
  before this one.
