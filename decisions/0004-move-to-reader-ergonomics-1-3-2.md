# 0004: Move to reader-ergonomics v1.3.2 and drop the settings it now holds

**Decision:** This repository checks against reader-ergonomics v1.3.2 (commit `a90b02e`). The standard now exempts
`checks/judgments.toml` from co-change and the line ceiling. This repository's config no longer repeats it.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; reported to reader-ergonomics by this repository, which fixed it in v1.3.2.

## Context

- The answers file `checks/judgments.toml` changes whenever an answer is written. Under co-change it asked for its
  own answer, and past 500 lines the ceiling asked again: each answer reopened a question about the file holding it.
- This repository had stopped the loop in its own config, with `[co_change]` and `[logical_lines]` tables, and
  reported the loop upstream.
- reader-ergonomics v1.3.2 exempts the answers file from both checks by default, with a test that pins both
  exemptions. Its co-change list holds every path this repository listed.

## Decision

The pin in CI and every text link move to v1.3.2, with the commit in the system-diagram example. The `[co_change]`
and `[logical_lines]` tables leave `checks/config.toml`: the standard's defaults now say the same thing.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.3.0 with the local tables | no change; the loop fix lives in this repository only | rejected: every extension would repeat it |
| Move, and keep the local tables | works; the same exemption is written in two places | rejected: one fact in two places |
| Move, and drop the local tables | the config says only what differs from the standard | chosen |

## Consequences

- Good: the config is shorter, and holds only what this repository changes.
- Bad: should the standard drop an exemption, the loop comes back here without a change to this repository. The
  standard's test of both exemptions is what guards it.
- To keep it true: the next pin move repeats the link move, as records 0001 and 0003 ask.

## See also

- The [decisions](README.md) of this repository; [record 0003](0003-move-to-reader-ergonomics-1-3-0.md), the move
  before this one.
