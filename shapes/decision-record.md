# Shape: decision record for a design decision

reader-ergonomics has a general
[decision record](https://github.com/Tewf/reader-ergonomics/blob/7a76cc6a86b7a5c1e451e4416534d113abd0f594/shapes/decision-record.md):
the parts every record has, with their evidence. This shape extends it, since a decision about the design of
software adds two parts:

- the options that lost, each with why it lost;
- a link to the design document where the decision was argued.

## When to use it

- When a decision about structure, an interface or a dependency is taken, and someone may later ask why.
- When a [design document](design-document.md) is accepted or rejected: the record keeps the outcome, and the
  proposal keeps the debate.
- Not for a decision anyone can undo in minutes: the commit message is enough.
- Not to argue a choice before it is made: that is a design document.

## What this shape adds, and its evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Options, after Decision | every option considered, the chosen one included, with its consequences and why the others lost | MADR 2024 adds them to Nygard's record; participants found MADR's rationale deeper and slower to write (Nogueira 2026, a preprint, 33 undergraduates) | convention; one writer-side experiment |
| Proposed in | links the design document where the decision was argued, so the record stays short | the design-decisions baseline's variant: proposal and record as two linked documents | convention, untested |

- How records are used in software projects: they are tried more than kept. About half of repositories with records
  hold one to five (Buchgeher 2023, secondary), and about 63% of 5,800 records were opened already accepted (Santana
  2026, secondary).
- The evidence for the general parts, and its grades, is in the general shape and is not repeated here.

## The skeleton

```markdown
# <NNNN>: <the choice, as a short phrase>

**Decision:** <the choice in one sentence>

**Status:** <proposed | accepted | superseded by NNNN | withdrawn>, <date>. **Shape:** [decision record](<path to this shape>). **Proposed in:** <link to the design document, or "no proposal">.

## Context
<The situation that made a choice necessary, and the facts it rests on.>

## Decision
<What was chosen, in full sentences.>

## Options
| Option | Consequences | Outcome |
|---|---|---|
| <option> | <what it would bring, good and bad> | <chosen, or rejected: why> |

## Consequences
<What follows, good and bad, and what must stay true.>

## See also
<The decisions folder, and the work the choice concerns.>
```

## The rules it adds

1. Options list every option considered, the chosen one included, each with why it won or lost.
2. A decision that was argued in a design document links it under "Proposed in"; the debate stays there.
3. The Shape line links this shape, which extends the general one, so a check knows to require Options.
4. Consequences label their lines Good, Bad and To keep it true, so a check can see that a bad one is named.

The general shape's rules hold as written. Each record holds one decision, stated first, with its bad consequences;
an accepted record is superseded, not changed in place.

## Checked by

- `shape-conformance` of reader-ergonomics, declared in this repository's `checks/config.toml`: a record holds
  Context, Decision, Options, Consequences and See also.
- `decision-records` of reader-ergonomics, for the general shape's four rules. The records are numbered in order and
  linked from the README, and each opens with its decision. Its status has a word and a date, and links forward when
  superseded, and its Shape line links this shape. A record with no Consequences line labelled Bad becomes a judgment
  question, which this repository turns on with `ask_costs` in `checks/config.toml`.

## Worked example

- The worked example is this repository's first record:
  [0001: Pin links to reader-ergonomics at its release commit](../decisions/0001-pin-links-at-the-release-commit.md).
- Its proposal is a [design document](../examples/pin-links-at-the-release-commit.md) in `examples/`, so both shapes
  can be compared on one decision.
