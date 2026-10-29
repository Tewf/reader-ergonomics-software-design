# Design the failure paths

**Claim:** a design names how each part fails and how each failure is handled, and its plan tests those paths.

- **Grade:** measured, descriptive (failure studies), for where failures come from; convention, untested for the document that names them.
- **Evidence:** [system-design review, strand 3](../../evidence/system-design/review.md); [state of the art](../../evidence/system-design/state-of-the-art.md).
- **Check:** `design-docs` (warns): the Consequences name a failure, a risk or an error; whether the handling is adequate is judgment.
- **Reader styles:** none particular to this genre yet; the reader-ergonomics styles hold.

## What it asks

- In the Consequences, list the ways the design can fail: a part down, a network partition, a slow dependency.
- For each, say how it is detected and handled, and whether data can be lost.
- In the plan, test the error paths, not only the main path.

## Why

- In five distributed systems, 92% of 48 catastrophic failures came from incorrect handling of non-fatal errors, and
  58% of them could have been caught by simple tests (Yuan 2014).
- Of 136 failures under network partitions, 80% were catastrophic and 90% silent (Alquraan 2018).
- Of the 88 taken from issue trackers, 47% needed a redesigned mechanism, and design flaws took 2.5 times longer to
  fix (Alquraan 2018).

## Limits

- The studies cover distributed data systems; other kinds of software were not studied the same way.
- They describe failures; no trial shows that writing the failure paths down prevents them.
