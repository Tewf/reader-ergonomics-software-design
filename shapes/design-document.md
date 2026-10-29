# Shape: design document

This shape proposes one design before it is built. Its first reader is a reviewer who must decide whether to adopt
it; its second is whoever later asks why the system is as it is. It opens with the decision asked for, then says why
the change is needed, what it does and does not aim at, the design, the alternatives that lost, and what it costs.
Once a decision is taken, a decision record keeps it, and links back here.

## When to use it

- Before building a change that others must agree to, or that is costly to undo.
- When there is more than one reasonable design, so the losing ones need writing down.
- Not for one algorithm: that is an [algorithm specification](algorithm-specification.md), which the design section
  may link.
- Not for the record of a decision already taken: that is a decision record, the shape planned next.
- Not for a small, reversible change: its commit message is enough.

## How each part maps to the evidence

| Part | What it does | Evidence | Grade |
|---|---|---|---|
| Decision asked | one sentence: what the reviewer must decide, and by when | the candidate variant named by the [design-decisions baseline](../evidence/design-decisions/baseline.md) | convention, untested (a hypothesis to test) |
| Status | proposed, accepted, rejected or superseded, with a date | Nygard 2011; PEP 1 (Warsaw 2000); KEP template (Kubernetes 2026) | convention, adopted |
| Summary | the whole proposal in a few lines | the abstract of PEP 12 (Goodger 2002) | convention, adopted |
| Motivation and use cases | why the present state does not suffice, shown on cases | every template compared has it ([state of the art](../evidence/design-decisions/state-of-the-art.md)); Go proposals were declined most often for feasibility, use cases and principles, not for form (Kondo 2025) | convention, adopted; descriptive for the decline reasons, one project |
| Goals and non-goals | what the design aims at, and what it deliberately leaves out | the KEP template; Ubl 2020 | convention, adopted by two of seven templates |
| Design | the change itself, at the level a reviewer can judge | every template; the reference-level section of the Rust RFC template (Rust 2026b) | convention, adopted |
| Alternatives | each option that lost, with its consequences and why it lost | PEP 12 rejected ideas, Rust RFC, KEP, Ubl 2020; with options and their pros and cons, rationale was judged deeper and writing slower (Nogueira 2026) | convention, adopted; one writer-side experiment |
| Consequences | drawbacks, risks, compatibility and security | PEP 12 (backwards compatibility, security); Rust RFC drawbacks; KEP risks | convention, adopted |
| Feasibility and plan | how it was shown to work, and how it is tested and rolled out | feasibility leads the decline reasons (Kondo 2025); the KEP template's test plan and production readiness review | descriptive; convention |
| Open questions | what is still undecided | PEP 12 open issues; Rust RFC unresolved questions | convention, adopted |

In one laboratory experiment, recorded rationale made later decisions more effective when requirements changed
(Falessi 2010, measured, 50 students). That is why the alternatives and consequences stay in the document.
Whether this shape helps a reviewer find flaws is untested. No experiment was found in which reviewers judged a
proposal in two forms; the [baseline](../evidence/design-decisions/baseline.md) gives the comparison it should face.

## The principles it applies

| Part | Principle |
|---|---|
| Decision asked and summary first | [overview first](https://github.com/Tewf/reader-ergonomics/blob/c08433c4d868d9b38ac1441f58ae7602c399db6d/principles/document/overview-first.md) |
| Proposal and record kept as two documents | [one mode per document](https://github.com/Tewf/reader-ergonomics/blob/c08433c4d868d9b38ac1441f58ae7602c399db6d/principles/document/one-mode-per-document.md) |
| Fixed sections, alternatives as a table | [signal the structure](https://github.com/Tewf/reader-ergonomics/blob/c08433c4d868d9b38ac1441f58ae7602c399db6d/principles/page/signal-the-structure.md) |
| An algorithm linked, not restated | [one place per fact](https://github.com/Tewf/reader-ergonomics/blob/c08433c4d868d9b38ac1441f58ae7602c399db6d/principles/collection/one-place-per-fact.md) |

## The skeleton

```markdown
# <Short noun phrase naming the change>

**Decision asked.** <One sentence: what the reviewer must decide, and by when.>
**Status.** <proposed | accepted | rejected | superseded by ...>, <date>.

**Summary.** <The proposal in three to five lines.>

## Motivation
<Why the present state does not suffice.>
- Use case: <who needs what, and what happens today>.

## Goals and non-goals
- Goal: <what the design must achieve>.
- Non-goal: <what it deliberately does not do>.

## Design
<The change, at the level a reviewer can judge. Link an algorithm specification rather than restating it.>

## Alternatives
| Option | Consequences | Why it lost |
|---|---|---|

## Consequences
- Drawbacks: <...>. Risks: <...>. Compatibility: <...>. Security: <...>.

## Feasibility and plan
- Shown to work by: <a prototype, a measurement, a precedent>.
- Tested by: <...>. Rolled out by: <...>.

## Open questions
- <Each question, or "None.">
```

## The rules

1. The decision asked comes first: a reviewer should know what is wanted before reading why.
2. Every alternative that a reviewer could reasonably propose is listed, with why it lost; a missing one is the
   question the review will ask.
3. A non-goal is as explicit as a goal: it is what stops the review from growing the scope.
4. Consequences include the bad ones; a design with no drawback has not been looked at closely.
5. Feasibility is shown, not asserted: name the prototype, the measurement or the precedent.
6. The design links what has its own document, an algorithm specification or an earlier decision, and does not
   restate it.
7. Once decided, the status changes and a decision record is written; the design document is not rewritten to look
   as if the outcome were always obvious.

## Worked example

# Pin the links to reader-ergonomics at its release commit

- **Decision asked.** Should this repository's links into reader-ergonomics name the release's commit instead of
  `master`? The answer is needed before the next push.
- **Status.** Accepted on 2026-10-29, in commit fb7e1f4.

**Summary.** CI checks this repository against reader-ergonomics at commit `40cd9fb`, but 43 links in the text pointed
at its `master`. A rename there would break them silently, and the text could cite a rule that CI does not run. The
links now name the same commit as CI, and move with it.

## Motivation
The extension contract pins a release by its commit, for the checks only; the text was left out.
- Use case: a reader follows a link to a principle and lands on the version the repository was checked against.
- Use case: a maintainer raises the pin, and the text moves in the same commit.

## Goals and non-goals
- Goal: the text and CI cite the same version of reader-ergonomics.
- Goal: no link breaks because a file is renamed upstream.
- Non-goal: links into the other extensions, whose names change on their own schedule.
- Non-goal: showing readers the newest wording of a principle before the pin moves.

## Design
Every `github.com/Tewf/reader-ergonomics/blob/master/` and `tree/master/` link becomes
`blob/40cd9fb3ed21a01a8913788edc46ade9562a797d/` (and `tree/...`). When CI's pin is raised, the links are raised in the
same commit.

## Alternatives
| Option | Consequences | Why it lost |
|---|---|---|
| Keep `master` | the newest text; breaks on any rename; text and CI can disagree | the disagreement is silent |
| The tag `v1.0.0` | short and readable | a tag can be moved, so the contract pins by commit |
| The commit `40cd9fb...` (chosen) | stable, and the same as CI | long addresses |

## Consequences
- Drawbacks: long addresses; readers see a rule as of the release, not later fixes.
- Risks: forgetting the links when the pin moves; one command finds them all.
- Compatibility: every target was confirmed to exist at the commit. Security: none.

## Feasibility and plan
- Shown to work by: the topic extension pins this way already.
- Tested by: a search finds no `blob/master` link to reader-ergonomics left, and each new target exists at the commit.
- Rolled out by: one commit replacing the 43 links.

## Open questions
- Should a check of this repository fail on a `master` link into reader-ergonomics, so the rule cannot drift?
