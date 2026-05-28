# Vercel demo — Self-Hosted Sandboxes

Same webhook → drain-queue → per-session runner shape as the Modal, Daytona,
and Cloudflare demos, but the runner is a **Vercel Sandbox running the TS
`EnvironmentWorker.handleItem()`** with the SDK's `betaAgentToolset20260401()` against the
sandbox's real filesystem (`bash` / `read` / `write` / `edit` / `glob` / `grep`).

The webhook function (`api/webhook.ts`) is a wake-up signal only. It verifies
the Standard Webhooks signature with `client.beta.webhooks.unwrap()`, drains
`work.poll()` until empty (capped at 25), and per item: acks, creates a Vercel
Sandbox, uploads `runner/runner.mjs`, and starts it detached. A bad work item is
logged and skipped — it stays un-acked and reclaims on the next webhook, so it
can't wedge the rest of the queue.

Idle policy is the SDK default: the dispatcher exits 60s after
`session.status_idle` with `stop_reason: end_turn`; any other event — including
`requires_action` idle, where the agent is blocked on the sandbox — resets the
clock.

No org API key anywhere: the webhook polls with the environment key, and the
runner authenticates with that same environment key — the single credential for
both the control plane and the per-session calls.

## Files

- `api/webhook.ts` — Vercel Function: verify sig → drain → spawn sandbox per item.
- `runner/runner.mjs` — runs inside the sandbox: `EnvironmentWorker.handleItem()` —
  builds the per-session `AgentToolContext`, downloads the agent's skills, runs a
  `SessionToolRunner` while heartbeating, force-stops the work item on exit.

## Prerequisites

- `npm`, the [Vercel CLI](https://vercel.com/docs/cli) (`npm i -g vercel`)
- A Vercel project linked (`vercel link`)
- A registered self-hosted environment + its environment key

## Configure

```sh
npm install
vercel link
vercel env add ANTHROPIC_WEBHOOK_SECRET   # placeholder for now
vercel env add ANTHROPIC_ENVIRONMENT_ID
vercel env add ANTHROPIC_ENVIRONMENT_KEY
```

## Deploy

```sh
vercel deploy --prod
```

This prints a `https://<project>.vercel.app` URL. Register
`https://<project>.vercel.app/api/webhook` as a webhook for
`session.status_run_started` in Console (or via the API), copy the issued
secret, then update:

```sh
vercel env rm ANTHROPIC_WEBHOOK_SECRET production
vercel env add ANTHROPIC_WEBHOOK_SECRET production
vercel deploy --prod
```

## Test

Create a session pointing at your environment id and send it a message:

```py
session = client.beta.sessions.create(agent=agent_id, environment_id=ENVIRONMENT_ID)
client.beta.sessions.events.send(session.id, events=[{"type": "user.message", "content": "ls -la"}])
```

You should see, in order:

```
vercel logs <project>.vercel.app
# [webhook] event=session.status_run_started session_id=...
# [webhook] acked work=... session=... sandbox=sbx_... (created)
```

Sandbox stdout/stderr (the `[runner]` lines) shows under the project's
**Observability → Sandboxes** tab in the Vercel dashboard.

## Notes

- `Sandbox.create()` + `writeFiles()` + `npm install` is ~15–25s before the
  function responds; `vercel.json` sets `maxDuration: 60`. The runner itself is
  `detached`. The function also mirrors the runner's first ~30s of output into
  the function log so it's debuggable from `vercel logs` without the Sandboxes
  observability tab.
- **Sandbox reuse** — Vercel Sandbox has no native tag/label/get-by-name API, so
  reuse needs external state. If a [Vercel KV](https://vercel.com/storage/kv)
  store is attached (`KV_REST_API_URL`/`KV_REST_API_TOKEN` are set), the webhook
  records `session_id → sandbox_id` and reuses a running sandbox on the next
  `run_started`, calling `extendTimeout()` so an active session keeps its VM
  alive across turns. Without KV, every delivery creates a fresh sandbox —
  `SessionToolRunner` dedups via `seen`/`answered` so a duplicate runner is
  wasteful, not wrong.
- **Working dirs** — the webhook creates `/mnt/session` and `/workspace` at
  sandbox start and uses `/workspace` as the dispatch workdir, matching the
  Modal/CF demos (skills download to `/workspace/skills/<name>/`). These are
  plain ephemeral directories, *not* persistent volumes — Vercel Sandbox has no
  volume API. The agent's working tree is gone when the sandbox stops.
- `npm install` runs inside the sandbox at spawn time so this demo has no build
  step. To shave ~10s off cold start, pre-bundle `runner/runner.mjs` with
  esbuild and upload the bundle instead.
