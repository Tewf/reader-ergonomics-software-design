# 0006: Move to reader-ergonomics v1.6.0, and hand it the decision-records check

**Decision:** This repository checks against reader-ergonomics v1.6.0 (commit `7fa4af5`), whose decision-records
check replaces the local one, and joins the family's key check.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; the family audit of decision records, and reader-ergonomics decision 0003.

## Context

- The family audit found that the standard checked a record's headings only. This repository extended its local
  check to the shape's four rules, and the standard adopted it in v1.6.0 with its tests. Two checks of one name
  cannot both run.
- v1.5.0 adds bibliography-keys: a key names one work across the family. An extension lists its siblings, and CI
  must clone them beside it for the check to read their bibliographies.
- v1.6.0 also lists `decisions/` in the generated `llms.txt`, and tests three checks that had no test.

## Decision

The pin in CI and every text link move to v1.6.0. With the move, the standard's decision-records replaces the local
`decision_records.py` and its tests, and runs with `ask_costs` on, since every record here labels a bad consequence.
The move also joins the key check: the config names the five other repositories of the family and one shared link,
and CI clones that family before the checks.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.4.3 with the local check | no change; the family's key clashes stay invisible here | rejected |
| Move, and keep the local check under another name | the same rules in two places | rejected: one fact in two places |
| Move, drop the local check, join the key check | one check in the standard; keys compared across the family | chosen |

## Consequences

- Good: the rules of a record are checked in every repository of the family, and keys are compared at each push.
- Bad: each push clones five repositories, a few seconds; a renamed or private sibling turns into a warning.
- Bad: a key clash now surfaces here when another repository adds a row, not only when this one does.
- To keep it true: a new repository of the family is added to `family`; a link two works share on purpose goes in
  `shared_links` with its reason.

## See also

- The [decisions](README.md) of this repository; [record 0005](0005-move-to-reader-ergonomics-1-4-3.md), the move
  before this one.
