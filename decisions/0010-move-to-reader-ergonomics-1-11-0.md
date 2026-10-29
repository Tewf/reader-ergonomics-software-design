# 0010: Move to reader-ergonomics v1.11.0, and key two Microsoft pages by a word

**Decision:** This repository checks against reader-ergonomics v1.11.0 (commit `6980fa6`). Its two keys for Microsoft
pages take the title word the release allows an organisation: `Microsoft 2026 icons` and `Microsoft 2026 ADR`.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** this repository's view on the family's key rule, adopted as reader-ergonomics decision 0004.

## Context

- A key names one work across the family. A work that lost a shared key took the next free letter.
- So this repository held `Microsoft 2026b`, the Azure icons page, and `Microsoft 2026c`, the page on keeping an
  architecture decision record.
- A letter says nothing about the page. This repository suggested that an organisation, which publishes many pages a
  year, carry one title word instead; the standard adopted it in v1.11.0, for organisations only.
- The citations check joins the word to the key only when the bibliography holds that exact longer key, so prose
  after a plain key still reads as before.

## Decision

The pin in CI and every text link move to v1.11.0, in this commit. The next commit renames the two keys in the
bibliography and in the text together: a key renamed in one place only fails the citations check.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Move, and keep the letters | no rename; the keys stay opaque | rejected: the rule exists for these two keys |
| Move, and rename every organisation key with a letter | AWS and others change too, beyond what was asked | rejected for now: each rename is a choice of word |
| Move, and rename the two Microsoft keys | the keys name their pages | chosen |

## Consequences

- Good: a reader can tell the icons page from the decision-record page by the key alone.
- Bad: two keys change after their pages were cited, so an answer that quotes one reopens.
- Bad: a word must stay unique for its organisation and year across the family; bibliography-keys checks it.
- To keep it true: the next pin move repeats the link move, as records 0001 and 0009 ask.

## See also

- The [decisions](README.md) of this repository; [record 0009](0009-move-to-reader-ergonomics-1-10-0.md), the move
  before this one.
