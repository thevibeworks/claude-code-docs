# INC-2101: cart p99 latency (2026-02-11)

Root cause: commit 5d0c7aa, a refactor that moved a batched `cart_items` query inside a per-cart loop. One query per request became one query per item.

How we spotted it: the same `SELECT ... WHERE cart_id = ?` line repeated 10 to 20 times per request id, starting at the deploy timestamp.

Fix: reverted the commit. Recovery took four minutes.

Follow-up that never shipped: a query-count regression test in CI for the checkout and cart handlers (owner: storefront). Still open as of April.
