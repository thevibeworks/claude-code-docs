# Cloudflare demo — Self-Hosted Sandboxes (pure-Worker variant)

Same webhook → drain-queue → per-session runner shape as `../cf/`, but the runner is a **Durable Object running the TS `client.beta.sessions.events.toolRunner()`** (`src/runner.ts`) with an **in-isolate fake filesystem** (`src/tools.ts`) instead of a real container. `read`/`write`/`edit`/`glob`/`grep` operate on a `Map<string,string>` held in the DO; `bash` returns a not-available stub.

Idle policy is the SDK default: the dispatcher exits 60s after `session.status_idle` with `stop_reason: end_turn`; any other event resets the clock.

This is the TS library-usage reference for the lower-level `SessionToolRunner` (custom tools, the DO owns the heartbeat + force-stop). For a real shell — and for `EnvironmentWorker`, which composes the whole work-item lifecycle but pulls in the Node-only `agent-toolset/node` module that a Workers isolate can't run — use the Container or Vercel/Modal demos.

No org API key anywhere: the webhook polls with the environment key, and the runner DO authenticates with that same environment key — the single credential for both the control plane and the per-session calls.

```sh
npm i
wrangler secret put ANTHROPIC_WEBHOOK_SECRET
wrangler secret put ANTHROPIC_ENVIRONMENT_KEY
# edit ANTHROPIC_ENVIRONMENT_ID in wrangler.toml, then:
wrangler deploy
```
