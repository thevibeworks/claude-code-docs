# Hosting an Agent Battle event — presenter runbook

You need exactly **one thing** to run this event: the **event server**
deployed somewhere with a stable public URL. Everything else (open the
scoring window, reset the board, watch who's connected) happens in a
**web admin panel** — no shell, no SSH, no on-call engineer.

```
participants' laptops                 event server (one URL)            Anthropic cloud
┌─────────────────────┐    outbound   ┌──────────────────────┐    MCP   ┌──────────────┐
│ Minecraft + bot     │──WebSocket──▶ │ /relay/ws            │◀────────│ Managed Agent │
│ (nothing exposed)   │               │ /p/<key>/mcp         │          │ (per player)  │
└─────────────────────┘               │ /api  (leaderboard)  │          └──────────────┘
                                      │ /     (cast view)    │
        projector ──────────────────▶ │ /admin (you)         │
                                      └──────────────────────┘
```

Participants never create tunnels — their bots dial **out** to the
event server. That's what makes this work on venue wifi.

## 1. Before the event (~30 min, once)

### Deploy the event server

Follow [`event/README.md`](event/README.md). Recommended: **Fly.io**
(stable URL, restart button, Tokyo region). Alternatives: Cloud Run,
any Docker host. The deploy gives you:

- `EVENT_URL` — e.g. `https://agent-battle-tokyo.fly.dev`
- `ADMIN_KEY` — you chose it during deploy; **keep it private**

Sanity check: open `EVENT_URL/admin`, sign in with the admin key, and
confirm the status cards load.

### Point the repo at your event

Edit `.env.event` in the **public repo** (`cwc-workshops/agent-battle`):

```bash
EVENT_URL='https://agent-battle-tokyo.fly.dev'
LEADERBOARD_KEY='devkey'
MC_SEED='611578087908456433'        # any number; same for everyone
```

Commit and push. Participants who clone the repo now get everything
automatically — they only export their own `ANTHROPIC_API_KEY`,
`PARTICIPANT` name, and `MINECRAFT_EULA=accept`.

### Dry-run as a participant

On your own laptop (off any corporate VPN), follow `README.md` steps
1-4. You should reach `▸ ready` and see your bot in the admin panel's
"Connected bots" table within ~2 minutes.

## 2. Day of the event

| When | What you do | Where |
|---|---|---|
| Doors open | Put the **cast view** (`EVENT_URL/`) on the projector. It shows the join QR + steps until people start scoring. | projector |
| People set up | Watch **Connected bots** count climb. Anyone stuck → they type `/cwc-fix` in Claude Code. | `/admin` |
| GO | Click **Open window** (pick duration). Scores only count while it's open. | `/admin` |
| During | Nothing. The board and chat update live. | — |
| Wrap-up | Click **Close window** — the board freezes for the prize ceremony. | `/admin` |
| Between cohorts | **Download backup** (if you want the results), then **Reset board**. Re-open the window for the next group. | `/admin` |

## 3. If something goes wrong

| Symptom | Fix |
|---|---|
| A participant's row never appears | Their problem, not yours: have them type `/cwc-fix` in Claude Code. The usual causes are a dead bot or a wrong `PARTICIPANT` name. |
| One bot shows ⚫ disconnected in `/admin` | It reconnects automatically. If it stays down >1 min, that participant runs `./setup.sh --restart`. |
| Cast view stops updating | Refresh the browser tab. If it still fails, check `EVENT_URL/api/config`. |
| `EVENT_URL/api/config` doesn't respond | Restart the service from your hosting dashboard (Fly: `fly apps restart <app>` or the web UI button). Bots reconnect within seconds; **scores are not lost** (snapshot on disk/volume). |
| You opened the window too early/late | Just open it again — **Open window** restarts the clock from now. Note: re-opening drops scores posted before the new window started. |
| Board has junk/test rows before the event | **Reset board** in `/admin`. |
| Whole platform region outage (last resort) | Run the fallback: clone the repo on any machine, `./host.sh`. It prints a new `EVENT_URL` (quick-tunnel). Update `.env.event`, push; participants run `git pull && ./setup.sh --restart`. |

## 4. After the event

- **Download backup** in `/admin` — that JSON is the final standings.
- Top-3 verification (prizes): see `harness/verify.py` — replay the
  winners' run logs against their claimed scores.
- Reset the board, or just leave it; the next event's reset clears it.

## What you do NOT need

- Anyone's homespace, laptop, or VPN
- SSH access to anything
- cloudflared, tunnels, or URL re-sharing mid-event
- The person who deployed the event server (unless the hosting account
  itself needs attention)
