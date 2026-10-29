# 0002: Move to reader-ergonomics v1.2.0 and drop the local judgment check

**Decision:** This repository checks against reader-ergonomics v1.2.0 (commit `6d4e324`). Its own
judgment-citations check is deleted: the standard's judgment-quotes now does the same work.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; it follows [0001](0001-pin-links-at-the-release-commit.md), whose rule moves the links with the pin.

## Context

- On 2026-10-29 the judgment answers here, and in the topic extension, were found written one per kind of question,
  with reasons absent from their files. Each repository wrote a check that an answer quotes its own file.
- The same check in two extensions is one fact in two places. The standard took it into v1.2.0 as judgment-quotes,
  from both, with this repository's folder-entry quotes, stale-answer skip and line check.
- Its default leaves path questions (co-change, tree-shape) unquoted, so that no extension breaks on moving its pin.

## Decision

The pin moves to v1.2.0, with every text link, as record 0001 asks. The local check `judgment_citations.py` and its tests are deleted. `checks/config.toml` sets `[judgment_quotes] optional = []`, so path answers must quote their file too.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.0.0 and keep the local check | no change needed; the check lives in two places and drifts | rejected |
| Move to v1.2.0 with its default | path answers may quote nothing again | rejected: that is how answers became templates |
| Move to v1.2.0, delete the local check, require a quote on every answer (`optional = []`) | one check in one place, and the strict rule kept | chosen |

## Consequences

- Good: one check, maintained in the standard; this repository keeps only `decision_records.py`, which is particular
  to it.
- Good: every text link moved with the pin, as record 0001 asks (63 links, each target confirmed at the commit).
- Bad: the stricter setting must be kept in `checks/config.toml` by hand.
- To keep it true: the next pin move repeats the link move and reruns every tier before pushing.

## See also

- The [decisions](README.md) of this repository.
- `checks/config.toml`, which keeps the strict setting.
