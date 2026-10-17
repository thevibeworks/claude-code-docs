# INC-2190: inventory p99 latency (2026-03-03)

Root cause: redis restart during maintenance emptied the SKU availability cache. Every lookup fell through to the ledger aggregate on db-inventory, which takes 200 to 500ms uncached.

How we spotted it: `cache_hit` lines dropped to zero and `sku_stock` queries went from almost none to about 1/s on every request.

Fix: the cache refilled on its own in about six minutes.

Lesson: SKU availability is only fast because of the cache. Anything that bypasses it turns a 40ms endpoint into a 500ms one. No errors, just slow, so it is easy to miss.
