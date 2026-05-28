# Setup tips & tricks — Slack × CMA webhook bridge

Things that aren't obvious from the docs and tend to cost debugging time.

---

## Mental model

### Two webhooks, one bridge

- **Slack → bridge** (`/slack/events`) fires on @mention. Payload carries `channel`, `ts`, `thread_ts`, `user`, `text`.
- **Anthropic → bridge** (`/cma-webhook`) fires on session idle. Payload carries **only** the CMA session ID.

Neither carries the agent's output. Both are just *signals* with IDs.

### The webhook is a doorbell, not a delivery

Anthropic's `session.status_idled` payload is deliberately thin — `{type, id}`. You follow up with `sessions.retrieve(id)` (metadata) and `sessions.events.list(id)` (output). Push the signal, pull the data.

### `metadata` is the entire routing state

On kickoff, set `metadata: {slack_channel, slack_thread_ts, slack_team}`. When the idle webhook arrives later with only a session ID, retrieve the session, read those keys back, and `chat.postMessage` to exactly the right thread — with nothing stored in the bridge itself. This is what makes it stateless.

### Slack's 3-second ack window

Slack retries any event that doesn't get a 2xx within 3 seconds. The bridge **must** return before the CMA session finishes. So: verify the signature, dedupe on `event_id`, fire `kickoffAgentSession()` without awaiting it, and return 204 immediately.

---

## Gotchas

### Use a developer sandbox, not your company workspace

Slack's [Developer Program sandboxes](https://api.slack.com/developer-program/sandboxes) give you a free Enterprise Grid org to test in — admin rights, fake users/channels, no risk of installing a half-built bot into production. This is **not** the "agent quickstart" — it's **Developer Program → Sandboxes**:

1. Join the [Slack Developer Program](https://api.slack.com/developer-program) → activate via email → accept ToS.
2. From the program dashboard: **Provision Sandbox** → pick empty or pre-loaded with fake users/channels → click again.
3. Finish setup from the email invite — you become Primary Org Owner; name the org and create at least one workspace inside it.
4. Create your app against that sandbox workspace and develop normally.

### OAuth scope ≠ event subscription

Adding `app_mentions:read` under **OAuth & Permissions → Bot Token Scopes** grants *permission* to see mentions. It does **not** cause Slack to deliver them. You must *also* go to **Event Subscriptions**, toggle it **On**, set the Request URL, and add `app_mention` under "Subscribe to bot events." Two separate pages. Miss the second one and you get zero deliveries with no error anywhere.

### `xoxb-` vs `xapp-` — two tokens, two pages, easy to grab the wrong one

| Token | Prefix | Page | Used for |
|---|---|---|---|
| Bot User OAuth Token | `xoxb-` | OAuth & Permissions (after install) | `chat.postMessage` — **this is the one you want** |
| App-Level Token | `xapp-` | Basic Information → App-Level Tokens | Socket Mode WebSocket only |

`chat.postMessage` with an `xapp-` token fails with `invalid_auth`. The `xoxb-` token only exists after you've added at least one bot scope **and** clicked Install/Reinstall to Workspace.

### Bridge must be running before you save the Request URL

Saving the Event Subscriptions URL triggers an immediate `url_verification` POST. If nothing is listening on the tunnel you get "Your URL didn't respond" and the URL won't save. Start `bun run dev` first, *then* paste the URL.

### Anthropic webhooks are workspace-scoped

The endpoint you register in Console only receives events for sessions **in that same workspace**. If your `ANTHROPIC_API_KEY` is from workspace A but you registered the endpoint in workspace B: zero deliveries, silently. Match the workspace picker on the Webhooks page to the Workspace column on your API key.

### A workspace webhook fires for *every* session in the workspace

Not just yours. If the Anthropic workspace is shared with other agents, scripts, or teammates, **every** `session.status_idled` in that workspace hits your endpoint. Your handler has to filter:

- **Retrieve-then-filter, always first.** `sessions.retrieve(id)` → check for your `slack_channel` metadata key → bail with 204 if absent. Do this *before* `events.list()` or any other work; otherwise unrelated sessions throw 404 deeper in the handler.
- **Catch 404/403 on `sessions.retrieve`** — sessions created under other API keys in the same workspace aren't readable by yours.
- **For production, use a dedicated Anthropic workspace.** Each unrelated session costs one `retrieve()` call just to discard it; a workspace that only contains this agent's sessions avoids that entirely.

### `unwrap()` needs a plain header map

`client.beta.webhooks.unwrap(body, {headers})` (SDK ≥ 0.95.1) wants `Record<string, string>`, not a fetch `Headers` object. Pass `Object.fromEntries(req.headers)`.

### `event.id` is your idempotency key

Anthropic retries failed deliveries with the **same** top-level `event.id`. Slack retries with the same `event_id` inside the body. Dedupe on both. Return 2xx once you've either handled or ignored the event — anything else triggers a retry, and ~20 consecutive Anthropic failures auto-disables your endpoint.

---

## Local dev checklist

1. `ngrok http 3000` → note the public URL.
2. `bun run setup` → copy `CLAUDE_AGENT_ID` / `CLAUDE_ENVIRONMENT_ID` into `.env.local`. **Don't overwrite them later** when you paste in the Slack secrets.
3. Slack app → **OAuth & Permissions** → Bot Token Scopes: `app_mentions:read`, `chat:write` (+ `im:history` for DMs) → **Install to Workspace** → copy `xoxb-…` → `SLACK_BOT_TOKEN`.
4. Slack app → **Basic Information** → copy **Signing Secret** → `SLACK_SIGNING_SECRET`.
5. Anthropic Console → **Manage → Webhooks**: `<url>/cma-webhook`, subscribe `session.status_idled` + `session.status_terminated` → copy `whsec_…` → `ANTHROPIC_WEBHOOK_SIGNING_KEY`. **Same workspace as your API key.**
6. `bun run dev` — server must be up *before* step 7.
7. Slack app → **Event Subscriptions** → On → Request URL `<url>/slack/events` → Verified ✓ → add bot event `app_mention` → **Save Changes** → reinstall if prompted.
8. In Slack: `/invite @your-bot` to a channel, then `@your-bot hello`.

### Debugging a silent failure

- **Nothing in the bridge log at all** → Slack isn't reaching you. Check `curl localhost:4040/api/requests/http` (ngrok's request log). No `/slack/events` POSTs = Event Subscriptions not saved, or Socket Mode is on.
- **`[agent] kickoff` logged but no reply** → ngrok log shows `/cma-webhook` POSTs? If none: Anthropic workspace mismatch or endpoint not saved. If 401: `ANTHROPIC_WEBHOOK_SIGNING_KEY` mismatch. If 204 but no Slack post: `SLACK_BOT_TOKEN` is wrong (check for `xapp-`) or missing `chat:write` scope.
- **`400 Invalid agent ID`** → `.env.local` still has the `agent_...` placeholder. Re-paste the real ID from `bun run setup`.
- **`not_in_channel`** from `chat.postMessage` → `/invite @your-bot` to the channel first.

---

## Production notes

- Replace ngrok with a real deploy. Nothing else changes.
- Replace the in-memory `seenEventIds` Sets with Redis/DB for multi-instance idempotency.
- For a distributed (multi-workspace) Slack app, swap the static `SLACK_BOT_TOKEN` for a per-team store keyed on `metadata.slack_team`; add the Slack OAuth flow.
- Each @mention starts a fresh CMA session (no memory across turns). For threaded conversations, cache `thread_ts → session_id` and send follow-ups via `sessions.events.send` instead of `sessions.create`.
