# Shape: decision record

This shape keeps one design decision after it is taken. Its reader comes later, a maintainer or a model, and asks
why the system is as it is. The record answers that in a page: what was decided, in what context, which options lost
and why, and what follows from it. It is the record that a [design document](design-document.md) leads to, and the
two stay linked.

## When to use it

- When a decision about structure, an interface or a dependency is taken, and someone may later ask why.
- When a design document is accepted or rejected: the record keeps the outcome; the proposal keeps the debate.
- Not for a decision anyone can undo in minutes: the commit message is enough.
- Not to argue a choice before it is made: that is a design document.

## How each part maps to the evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Number and title | a short noun phrase, numbered in order | Nygard 2011 | convention, the most used in open source (Buchgeher 2023, secondary) |
| Decision first | the decision in one sentence, under the title | a summary that the plain Nygard record lacks; added here after overview first | convention, untested |
| Status and date | proposed, accepted, rejected or superseded, with a link to what supersedes it | Nygard 2011; supersede rather than rewrite (GOV.UK 2025; Microsoft 2026) | convention, adopted |
| Context | the situation and forces the decision responds to | Nygard 2011; MADR 2024 calls them drivers | convention, adopted |
| Options | every option considered, with its consequences and why it lost | MADR 2024 adds them to Nygard; participants found MADR's rationale deeper and slower to write (Nogueira 2026) | convention; one writer-side experiment |
| Consequences | what follows, good and bad, and what must stay true | Nygard 2011 | convention, adopted |
| Link to the proposal | where the debate is, so the record stays short | the design-decisions baseline's variant: proposal and record as two linked documents | convention, untested |

- Why keep rationale at all: in one laboratory experiment it made later decisions more effective when requirements
  changed (Falessi 2010, measured, 50 students).
- Why keep it short: cost of capture is the longest-named barrier to recording rationale (Lee 1997; Tang 2006).
- How records are used in practice: they are tried more than kept. About half of repositories with records hold one
  to five (Buchgeher 2023, secondary), and about 63% of 5,800 records were opened already accepted (Santana 2026,
  secondary).
- Whether a record helps a maintainer recover why is untested on the maintainer; the
  [baseline](../evidence/design-decisions/baseline.md) gives the comparison it should face.

## The principles it applies

| Part | Principle |
|---|---|
| The decision in one sentence first | [overview first](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/principles/document/overview-first.md) |
| Record and proposal as two documents | [one mode per document](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/principles/document/one-mode-per-document.md) |
| The debate linked, not copied | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/principles/collection/one-place-per-fact.md) |
| Options as a table | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/6d4e324157b17862aa5c5158fde0ba02db992729/principles/page/signal-the-structure.md) |

## The skeleton

```markdown
# <NNNN>. <Short noun phrase naming the decision>

**Decision.** <One sentence: what was decided.>

- **Shape:** [decision record](<path to this shape>).
- **Status:** <proposed | accepted | rejected | superseded by NNNN>, <date>.
- **Proposed in:** <link to the design document, if any>.

## Context
- <The situation, the forces and constraints the decision responds to.>

## Options
| Option | Consequences | Outcome |
|---|---|---|
| <option> | <what it would bring, good and bad> | <chosen, or rejected: why> |

## Consequences
- Good: <...>
- Bad: <...>
- To keep it true: <what must be done, and when>.
```

## The rules

1. One decision per record, numbered in order, in a `decisions/` folder beside the code or text it governs.
2. The decision comes first, in one sentence; a reader who stops there knows what holds.
3. A line under it names this shape by a link, so a reader, or a check, knows what the record follows.
4. Every option considered appears, the chosen one included, with why the others lost.
5. Consequences include the bad ones and what must be done to keep the decision true.
6. An accepted record is not rewritten. A new record supersedes it, and the old one's status links forward.
7. Keep it to about a page; the debate belongs to the design document it links.

## Worked example

- The worked example is this repository's first record:
  [0001. Pin links to reader-ergonomics at its release commit](../decisions/0001-pin-links-at-the-release-commit.md).
- Its proposal is the worked example of the [design document](design-document.md#worked-example), so both shapes
  can be compared on one decision.
