# Agent Battle event server

One process that provides everything an event needs:

| Path | What it is |
|---|---|
| `/` | Cast view — leaderboard + bot chat + how-to-join panel (put this on the projector) |
| `/admin` | Web admin panel — open/close scoring window, reset board, see connected bots |
| `/api/*` | Leaderboard API (achievements, costs, narration) |
| `/wiki/mcp` | Minecraft-wiki MCP server (the opt-in participant lever) |
| `/p/<key>/mcp` | Per-participant bot MCP, relayed over the bot's outbound WebSocket |
| `/relay/ws` | WebSocket endpoint participant bots dial out to |
| `/healthz` | Liveness probe |

Participants never create tunnels: their bots make an **outbound**
WebSocket connection to this server, and the cloud agent reaches each
bot at `/p/<key>/mcp`. The event server is the only thing that needs a
public URL.

## Configuration (env vars)

| Var | Required | What |
|---|---|---|
| `WORKSHOP_KEY` | recommended | Shared secret participants' bots use to POST scores and register with the relay (`LEADERBOARD_KEY` in `.env.event`). Unset = open. |
| `ADMIN_KEY` | **yes** | Facilitator key for `/admin` and `/api/admin/*`. Keep private and distinct from `WORKSHOP_KEY`. If unset while `WORKSHOP_KEY` is set, the server generates an unguessable ephemeral one (admin panel unreachable until you set it explicitly) — it never falls back to the workshop key. |
| `MC_SEED` | yes | The event's shared world seed. |
| `EVENT_NAME` | no | Display name on the cast view, e.g. `"Agent Battle — Tokyo"`. |
| `PUBLIC_URL` | recommended | This server's own public base URL (used in the join panel + share block). |
| `PORT` | no | Listen port (default 8888). |
| `DATA_DIR` | no | Where the board snapshot lives (default `./data`). Mount a volume here. |
| `REPO_URL` / `REPO_DIR` | no | Shown on the join panel + QR code. |

## Hosting option A — Fly.io (recommended)

Stable URL, ~$5/mo, deploys in minutes, dashboard restart button,
Tokyo region available. From this directory:

```bash
fly launch --copy-config --no-deploy        # pick an app name; uses fly.toml
fly volumes create event_data --size 1 --region nrt
fly secrets set \
  WORKSHOP_KEY=$(openssl rand -hex 16) \
  ADMIN_KEY=$(openssl rand -hex 16) \
  MC_SEED=611578087908456433 \
  EVENT_NAME="Agent Battle — Tokyo" \
  PUBLIC_URL=https://<app-name>.fly.dev
fly deploy
# Save both generated keys: WORKSHOP_KEY goes into the repo's .env.event
# (as LEADERBOARD_KEY) for participants; ADMIN_KEY stays with the presenter.
```

Then put `EVENT_URL='https://<app-name>.fly.dev'` in the repo's
`.env.event` and push. Done — the URL never changes, restarts are a
button in the Fly dashboard, and the board snapshot lives on the volume.

## Hosting option B — Google Cloud Run

Uses GCP (no new vendor). Note: Cloud Run has no persistent disk, so
use the admin panel's **Download backup** button as your safety net,
and keep `min/max-instances=1` (board state is in memory + local disk).

```bash
gcloud run deploy agent-battle \
  --source . \
  --region asia-northeast1 \
  --allow-unauthenticated \
  --min-instances 1 --max-instances 1 \
  --set-env-vars WORKSHOP_KEY=$(openssl rand -hex 16),MC_SEED=611578087908456433,EVENT_NAME="Agent Battle — Tokyo" \
  --set-env-vars ADMIN_KEY=$(openssl rand -hex 16)
# Save both generated keys (echo them first if needed): WORKSHOP_KEY goes
# into the repo's .env.event for participants; ADMIN_KEY stays private.
# note the printed URL, then:
gcloud run services update agent-battle --region asia-northeast1 \
  --set-env-vars PUBLIC_URL=https://<printed-url>
```

WebSocket connections on Cloud Run are capped at 60 minutes; bots
reconnect automatically when that happens (a few seconds of
"bot offline" if it lands mid-run).

## Hosting option C — any Docker host

```bash
WORKSHOP_KEY=devkey ADMIN_KEY=$(openssl rand -hex 16) docker compose up -d
```

Front it with anything that terminates HTTPS (Caddy, an ALB, a
cloudflared *named* tunnel) and set `PUBLIC_URL`.

## Hosting option D — no cloud account at all (fallback)

`../host.sh` runs this server on the current machine behind a
cloudflared **quick-tunnel**. It works, but the URL changes if the
tunnel ever dies — that's the failure mode that this whole architecture
exists to avoid. Use it for practice or as a day-of emergency fallback.

## Presenter ops (during the event)

Everything is in the web admin panel — `<EVENT_URL>/admin`, sign in
with `ADMIN_KEY`:

- **Open window** at GO (scores only count while the window is open)
- **Close window** to freeze the board for the prize ceremony
- **Reset board** between cohorts/sessions
- **Download backup** before anything risky; **Restore** if needed
- **Connected bots** table → who's actually up, live

Nothing during an event requires shell access or a redeploy.

## Local dev

```bash
cd event && npm install && node server.mjs
# cast view:    http://localhost:8888
# admin panel:  http://localhost:8888/admin   (no keys set = open access)
node test/smoke.mjs   # full API/relay/MCP test suite
```

## Scale

A single small instance comfortably handles a 100-participant event:
each bot holds one WebSocket; tool calls are small JSON messages
(~1-10/min per running agent); browsers poll the cast view every 2-10s.
