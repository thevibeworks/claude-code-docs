# Cloudflare demo — Self-Hosted Sandboxes (Container variant)

The Worker (`src/index.ts`) verifies the `session.status_run_started` webhook with `client.beta.webhooks.unwrap()`, then **drains the environment work queue** (poll → ack until empty) so any single delivery recovers earlier missed ones. Per work item it starts a per-session **Cloudflare Container** (`src/container.ts`) whose entrypoint is `ant beta:worker run` — the CLI handles heartbeat, backlog reconcile, SSE, the default tool set (`bash`/`read`/`write`/`edit`/`glob`/`grep`), and the work-item force-stop on exit.

The CLI owns the idle policy (`--max-idle 60s` after `session.status_idle` with `stop_reason: end_turn`; any other event resets the clock). The DO owns the *Cloudflare* container lifetime: it streams session status to renew `sleepAfter` so CF doesn't reclaim the VM out from under a live `ant beta:worker run`.

No org API key reaches the runner: the container authenticates with the environment key — the single credential `ant beta:worker run` uses for the event stream, the lease heartbeat, and the work-item force-stop.

See `../cf-worker/` for the pure-Worker variant that runs the TS `SessionToolRunner` with an in-isolate fake filesystem instead of a real container.

```sh
npm i
wrangler secret put ANTHROPIC_WEBHOOK_SECRET
wrangler secret put ANTHROPIC_ENVIRONMENT_KEY
# edit ANTHROPIC_ENVIRONMENT_ID in wrangler.toml, then:
wrangler deploy
```
