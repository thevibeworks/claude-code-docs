# Setup tips & tricks — Linear × CMA webhook bridge

Things that aren't obvious from the docs and tend to cost debugging time.

---

## Mental model

### A webhook is "call me when something happens"

It's just an HTTP POST a service sends to a URL you gave it, with a small JSON body describing an event. You register the URL once; the service calls it whenever the event fires. No polling, no held-open connections.

### The bridge is mandatory (today)

Linear's Agent Platform and CMA don't share a wire format or credentials. Something has to translate "Linear @mention" → "CMA user.message" on the way in, and "CMA idle" → "Linear comment" on the way out, while holding both sets of keys. That's the bridge.

### Two webhooks, one bridge

- **Linear → bridge** fires on @mention. Payload carries `agentSession.id`, `organizationId`, and issue context.
- **Anthropic → bridge** fires on session idle. Payload carries **only** the CMA session ID.

Neither carries a "callback URL." Neither carries the agent's output. Both are just *signals* with IDs.

### The webhook is a doorbell, not a delivery

Anthropic's `session.status_idled` payload is deliberately thin — `{type, id}`. You always follow up with `sessions.retrieve(id)` (to get metadata) and `sessions.events.list(id)` (to get the output). Push the signal, pull the data. Retries stay cheap; data is never stale.

### `metadata` is the entire routing state

When the bridge creates the CMA session it sets `metadata: {linear_session_id, linear_org_id}`. When the idle webhook arrives later with only a session ID, the bridge retrieves the session, reads those keys back, and knows exactly where to reply — with nothing stored in the bridge itself. This is what makes it stateless.

---

## Gotchas

### Anthropic webhooks are workspace-scoped

The endpoint you register in Console only receives events for sessions **in that same workspace**. If your `ANTHROPIC_API_KEY` belongs to workspace A but you registered the endpoint in workspace B, you get **zero deliveries, silently**. Check the Workspace column on your API key and make sure it matches the workspace picker in the Console's Webhooks page.

### A workspace webhook fires for *every* session in the workspace

Not just yours. If the Anthropic workspace is shared with other agents, scripts, or teammates, every `session.status_idled` in that workspace hits your endpoint. Your handler **must** filter: `sessions.retrieve(id)` → check for your `metadata` keys → return 204 for anything that isn't yours. Also catch 404/403 on `sessions.retrieve` — sessions created under other API keys in the same workspace aren't readable by yours.

Corollaries: subscribe only to the event types you need (`session.status_idled`, `session.status_terminated`), not "All events"; and for production, consider a dedicated Anthropic workspace so there are no unrelated sessions to discard.

### Linear OAuth apps are workspace-admin-only

OAuth apps live at `linear.app/<your-workspace>/settings/api` — in the sidebar it's **Administration → API**, then the **OAuth Applications** section. If you're not an admin of your company workspace, spin up a free personal workspace for testing — takes two minutes and you won't install an experimental agent into production.

When creating the app, the **Developer URL** field is required but cosmetic (it's just a link shown on the consent screen) — any real `https://` URL is fine.

### `actor=app` is the load-bearing OAuth parameter

`scope=app:assignable,app:mentionable` + `actor=app` is what creates an **app user** in the Linear workspace that shows up in the @-picker. A personal `LINEAR_API_KEY` won't do this — the bridge must post back *as the app*, via the OAuth token.

### Linear's 10-second ack rule

The bridge must post *some* `agentActivity` (a `{type: "thought"}` is enough) within 10 seconds of receiving the `AgentSessionEvent`, or Linear marks the session failed. Do this *before* creating the CMA session.

### `event.id` is your idempotency key

Anthropic retries failed deliveries with the **same** top-level `event.id`. Dedupe on it. Return 2xx once you've either handled it or decided to ignore it — anything else triggers a retry, and ~20 consecutive failures auto-disables your endpoint.

### Signature header names

The docs say `X-Webhook-Signature`; the wire uses `Webhook-Signature` / `Webhook-Id` / `Webhook-Timestamp` (Standard Webhooks spec). The SDK's `webhooks.unwrap()` handles this — only matters if you're verifying by hand.

---

## Local dev checklist

1. `ngrok http 3000` (or `cloudflared tunnel`) → note the public URL. Everything below uses it.
2. `bun run setup` → copy `CLAUDE_AGENT_ID` / `CLAUDE_ENVIRONMENT_ID` into `.env.local`.
3. Linear OAuth app (**Administration → API → OAuth Applications → Create new**): Developer URL = any real `https://` URL (cosmetic); callback `<url>/oauth/callback`; webhook `<url>/linear-webhook`, events = Agent session events → copy client ID/secret + webhook secret.
4. Anthropic Console → Webhooks: `<url>/cma-webhook`, events = `session.status_idled` + `session.status_terminated` → copy `whsec_...`. **Same workspace as your API key.**
5. Fill `.env.local`, `bun run dev`.
6. Visit `<url>/oauth/authorize` → approve → "Agent installed."
7. @mention it in an issue.

### Debugging a silent failure

- **"Thinking…" never appears** → Linear webhook isn't reaching you. Check the Linear app's webhook URL and that ngrok is up.
- **"Thinking…" appears but no reply** → check `curl localhost:4040/api/requests/http` (ngrok's request log). If no POST to `/cma-webhook`: workspace mismatch on the Anthropic side, or endpoint not saved. If POST arrives with 401: signing key mismatch.
- **Reply is empty** → `sessions.events.list` may be paginated; iterate if the agent produced many events.

---

## Production notes

- Replace ngrok with a real deploy (Cloudflare Workers, Fly, etc.). Nothing else changes.
- Replace the in-memory `seenEventIds` Set with Redis or a DB for multi-instance idempotency.
- Replace the `.linear-tokens.json` file with a real secret store.
- Narrow the Anthropic endpoint's event subscription to exactly what you handle.
