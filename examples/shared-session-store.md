# Keep login sessions in a shared store

- **Decision asked.** Should the shop's web app keep its login sessions in one Redis instance shared by its servers,
  instead of in each server's memory? The answer is needed before the next release adds a third server.
- **Status.** Proposed, 2026-10-29.
- **Shape:** [design document](../shapes/design-document.md)

An illustration: the shop and its numbers are invented for this example; the reasoning is the part to copy.

**Summary.** The app runs on two servers behind a load balancer, and each keeps its users' sessions in its own memory.
A deployment or a crash on one server logs out half the users, and the balancer must send each user back to the same
server. Sessions move to one Redis instance that every server reads. Then any server can answer any request, and a
restart logs out no one.

## Motivation

The balancer's sticky routing keeps a user on the server that holds their session, so load is uneven and a server
cannot be drained without logging its users out.

- Use case: a customer at the checkout is logged out by a deployment and must log in again before paying.
- Use case: an operator restarts one server to apply a patch, and half the users must log in again.

## Goals and non-goals

- Goal: any server can serve any request of a logged-in user.
- Goal: a deployment or the restart of one server logs no one out.
- Non-goal: moving the basket or the orders, which already live in the database.
- Non-goal: single sign-on across the company's other sites.

## Design

- The session middleware reads and writes sessions in Redis under `session:<id>`, with the same 30-minute expiry it
  uses today; the cookie keeps only the session id.
- Each read or write times out after 50 ms. On a timeout or a refused connection, the request is answered with a 503
  and a Retry-After of 5 seconds: the user is not logged out, and no request runs as someone else.
- Sticky routing is switched off once every server reads from Redis.

## Alternatives

| Option | Consequences | Why it lost |
|---|---|---|
| Keep sessions in memory, with sticky routing | nothing to build; uneven load, and every restart logs users out | it is the problem this solves |
| Sessions in a signed cookie | no store to run; a session cannot be revoked before it expires, and the cookie grows with each field | logout must take effect at once |
| Sessions in the main database | no new service; every request adds a write to the busiest database | the database is already the bottleneck |
| One shared Redis instance (chosen) | any server serves any user; one more service to run and watch | the cost is a service the team already runs for its cache |

## Consequences

- Drawbacks: one more service on the request path, and a few milliseconds per request.
- Risks: if Redis fails, logged-in requests fail with a 503 until it is back; that outage is accepted, because the
  alternative is serving a request without knowing who sent it. A full Redis would evict sessions: memory is sized for
  twice the peak count of sessions, and an alert fires at 70%.
- Compatibility: sessions held in memory on the day of the switch are lost once, so the switch is made at night.
- Security: session ids stay random and unguessable; Redis listens on the private network only, behind a password.

## Feasibility and plan

- Shown to work by: the same Redis already serves the product cache, and a branch of the middleware passes the
  existing tests against it.
- Tested by: a test for each failure path (Redis stopped, slower than 50 ms, full), each expecting a 503 and no
  logout. A load test replays the peak hour on one server, with sticky routing off.
- Rolled out by: one server first, then the second, then sticky routing off; rollback is the previous release.

## Open questions

- Should a Redis replica be added, so that a single failure no longer fails logged-in requests?
