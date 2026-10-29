# 0001: Pin links to reader-ergonomics at its release commit

**Decision:** Every link from this repository into reader-ergonomics names the commit of the release CI checks
against, and moves with CI's pin in the same commit.

**Status:** accepted, 2026-10-29, and applied in commit fb7e1f4. **Shape:** [decision record](../shapes/decision-record.md). **Proposed in:** [Pin the links to reader-ergonomics at its release commit](../examples/pin-links-at-the-release-commit.md), a design document.

## Context

- CI runs reader-ergonomics' checks at commit `40cd9fb3ed21a01a8913788edc46ade9562a797d` (release v1.0.0), as its
  extension contract asks: a release is pinned by its commit, since a tag can be moved.
- The text was outside that rule: 43 links pointed at reader-ergonomics' `master`.
- A rename upstream would have broken them without any check noticing, and the text could cite a rule CI did not run.

## Decision

Every link into reader-ergonomics names the 40-character commit of the release that CI checks against. When CI's pin is raised, the links are raised in the same commit, after confirming that each target exists at the new commit.

## Options

| Option | Consequences | Outcome |
|---|---|---|
| Keep `master` | the newest text; breaks on a rename; text and CI can disagree in silence | rejected: the disagreement is silent |
| The tag `v1.0.0` | short addresses | rejected: a tag can be moved |
| The release commit | stable, and the same version as CI; long addresses | chosen |

## Consequences

- Good: a reader lands on the version of a principle the repository was checked against.
- Good: no link can break through a rename upstream.
- Bad: long addresses, and a fix to a principle reaches readers only when the pin moves.
- To keep it true: when CI's pin is raised, the links are raised in the same commit.
- Open: whether a check of this repository should fail on any `master` link into reader-ergonomics.

## See also

- The [decisions](README.md) of this repository.
- The workflows `.github/workflows/checks.yml` and `pages.yml`, which carry the pin.
