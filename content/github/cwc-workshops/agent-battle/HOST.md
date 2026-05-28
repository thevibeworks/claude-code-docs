# Hosting — operational runbook

One machine runs `./host.sh` (the **host**) and serves the
shared leaderboard + wiki MCP. Pick something always-on — a
VM or dev box, not a laptop that sleeps. Everything below runs
on that machine, in the cloned repo directory. The
facilitator's own laptop is just another participant.

## Status check (any time)

```bash
cat .host-state/host-urls.env                # the SHARE block
curl -s localhost:8888/api/leaderboard | python3 -m json.tool
ps -eo pid,etime,args | grep cloudflared     # tunnel uptime
```

Cast view (projector): `<LEADERBOARD_URL without /api>/?cast=1`

## Before each session

```bash
./host.sh --reset                  # empty board, SAME tunnel URLs
DURATION=3600 ./host.sh --open     # open scoring window (seconds)
cat .host-state/host-urls.env      # paste this SHARE block to participants
```

## During the session

Nothing. Participants follow `README.md`. Watch the cast view.

## End of session

```bash
./host.sh --close                  # freeze the board
```

**Don't run `./host.sh --stop`** until after the last event day —
that kills the tunnels and changes the URLs for everyone.

## If the host machine reboots mid-event

Scores and `MC_SEED` survive (`.host-state/` is on persistent
disk). Tunnel **URLs change** — quick-tunnels can't survive a
process restart. Recover:

```bash
cd <this repo>
. .host-state/host-urls.env        # recovers the original MC_SEED
MC_SEED="$MC_SEED" ./host.sh       # restarts; prints NEW tunnel URLs
DURATION=3600 ./host.sh --open
cat .host-state/host-urls.env      # NEW share block
```

Tell participants: re-export `LEADERBOARD_URL` and `WIKI_MCP_URL`
to the new values, re-run `/cwc-setup`. Their local stack and
seed are unaffected; their existing scores are still on the board.

## If the host machine is unreachable

Last resort: run `./host.sh` on the facilitator's laptop
(disconnect any corporate VPN first). Same commands. Less stable (laptop can
sleep) but functional. The facilitator is then both host and
participant on one machine — use the localhost block for their
own participant exports, the trycloudflare block for everyone
else.

## Why participants can't do this

There is no participant-facing host command. `./host.sh
--open|--close` authenticate with `.host-state/admin-key`,
which only exists on the machine that ran `./host.sh`. The
`LEADERBOARD_KEY` in the SHARE block authorizes score POSTs
only — a participant who curls `/admin/session` with it gets
401.

## First-time host setup

```bash
git clone https://github.com/anthropics/cwc-workshops
cd cwc-workshops/agent-battle
./host.sh
```

Starts leaderboard (`:8888`) + wiki MCP (`:8077`) + cloudflared
quick-tunnels for both, generates `.host-state/admin-key`, and
prints the SHARE block.
