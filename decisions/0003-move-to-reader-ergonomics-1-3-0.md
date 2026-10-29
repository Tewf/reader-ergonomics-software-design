# 0003: Move to reader-ergonomics v1.3.0 and extend its decision record

**Decision:** This repository checks against reader-ergonomics v1.3.0 (commit `d408349`), and its decision-record
shape extends the standard's general one instead of standing alone.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** no proposal; agreed among the sessions that maintain reader-ergonomics, its topic extension and this repository.

## Context

- Three repositories of the family kept decision records, each with its own form: the standard, the topic extension
  and this one.
- The general form belongs in the standard, which no extension links up from; reader-ergonomics took it into v1.3.0,
  with its evidence copied from this repository's design-decisions review.
- The standard's config declares that form for `decisions/0*.md`, and an extension inherits that config.

## Decision

The pin and every text link move to v1.3.0. The decision-record shape here keeps only what a design decision adds:
the Options table and the Proposed in link. Records 0001 and 0002 take the general form, as a correction of wording
that the general shape allows. The conformance check requires Options here, beside the general parts.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Stay on v1.2.0 with a standalone shape | no change; two forms of one record in the family | rejected: one fact in two places |
| Move, and drop this repository's shape | one form; design records lose the options that lost, which the review keeps | rejected |
| Move, and extend the general shape with Options and Proposed in | one general form, plus what the genre adds | chosen |

## Consequences

- Good: a record reads the same across the family, and this repository's records add only the options and the link.
- Bad: the two earlier records changed form after acceptance; their decisions and reasons did not change.
- To keep it true: the next pin move repeats the link move, as records 0001 and 0002 ask.

## See also

- The [decisions](README.md) of this repository; the [decision-record shape](../shapes/decision-record.md).
