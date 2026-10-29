# Pin the links to reader-ergonomics at its release commit

- **Decision asked.** Should this repository's links into reader-ergonomics name the release's commit instead of
  `master`? The answer is needed before the next push.
- **Status.** Accepted on 2026-10-29, in commit fb7e1f4.
- **Shape:** [design document](../shapes/design-document.md)

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
  Answered later: yes. The check `standard-links`, written here and now in reader-ergonomics, fails a link that names
  neither the pinned commit nor its release tag.
