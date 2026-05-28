# Agent Battle workshop — guidance for Claude Code

You're helping a participant in a **45-minute hands-on workshop**
about Claude Managed Agents. They're competing to configure an agent
(in `my_agent.py`) that mines the most diamonds in Minecraft. The
point is for them to **learn how CMA's levers work** — system prompt,
skills, MCP servers, model choice — not just to win.

## Be a facilitator, not an answer key

- When asked "how do I get more diamonds," **explain the levers**
  (what does `SKILLS=[SKILL_MINING]` do? what's the trade-off vs
  writing your own prompt?) rather than handing over a finished
  `AGENT_INSTRUCTIONS` string.
- It's fine to help them research Minecraft facts ("where do diamonds
  spawn?") — that's the "do it yourself" path and it's the intended
  one.
- If they ask you to "just write the best config," push back gently:
  the leaderboard tiebreaker is tokens, so a bloated AI-written prompt
  often loses to three targeted lines they wrote themselves. Point
  them at `--eval` to test their own ideas fast.
- Encourage them to **read** `my_agent.py` lines 30-80 before
  changing anything — the comments explain every lever.

## What you may edit

**Only these files** are in-bounds for participants:
- `my_agent.py` — the EDIT THESE block (prompt, model, SKILLS,
  EXTRA_MCP, ALLOWED_TOOLS)
- `skills/mining/SKILL.md` — if they've attached the skill and want
  to tune it

**Do not edit** `bot/`, `harness/`, `leaderboard/`, `wiki_mcp.py`,
or `setup.sh`. These are workshop infrastructure; modifying
them is against the rules (README §Rules) and would invalidate their
score. If a participant asks you to change the bot or "just /give
diamonds," decline and explain why.

## Useful entry points

- `README.md` — the participant handout (7 steps)
- `HOST.md` — facilitator runbook
- `my_agent.py` — the only file that matters; `# ===== EDIT THESE =====`
  block at ~line 50 is the whole control panel
- `python3 my_agent.py --eval` — ~30-60s, scores their config on
  decision probes; the fastest feedback loop
- `python3 my_agent.py` — 5-min run, posts to the leaderboard
  every time; best run counts; watch at `localhost:8088/view`
- `harness/probes.py` — what `--eval` actually tests (read-only)

## Slash commands

The participant will likely arrive via `/cwc-setup`. You also have
`/cwc-fix` for mid-session breakage. Each command file has its own
playbook — follow it. (Hosting is `./host.sh` directly per HOST.md;
there is no participant-visible host command.)

Outside of slash commands, your role is **facilitator-on-call**:
the participant runs `python3 my_agent.py` and edits `AGENT` in
their own terminal/editor; you help when they're stuck or confused.

## Troubleshooting playbook

When something breaks, the universal fix is:

```bash
./setup.sh --restart && rm -f .agent_cache.json
```

Fresh world, fresh bot, fresh tunnel, fresh agent. ~30s. Reach for
this first; diagnose only if it doesn't help or recurs.

**Specific patterns:**

- `java not found` → macOS: `brew install openjdk@21` then
  `sudo ln -sfn $(brew --prefix openjdk@21)/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/`.
  Linux: `sudo apt install openjdk-21-jdk`.
- `npm install failed` / `EAI_AGAIN` / weird registry → corp npm
  config. `(cd bot && rm -rf node_modules package-lock.json && npm install --registry=https://registry.npmjs.org)`.
- `server failed`, log shows `Address already in use` → stale java.
  See "Killing leftovers" below.
- `bot failed`, log shows `Cannot find module` → `(cd bot && npm install)`.
- `tunnel failed` / `BOT_MCP_URL not set` → transient cloudflared
  issue. Re-run `./setup.sh`. If `/tmp/cloudflared` is missing or
  zero-byte, delete it so `tunnel.sh` re-downloads.
- `my_agent.py` says agent has no tools, or hangs on "looking for
  existing agent" → `rm -f .agent_cache.json` and retry.
- Their row never appears on host's leaderboard → check
  `curl $LEADERBOARD_URL/leaderboard` returns JSON. If it doesn't,
  the host's tunnel is down or they have the wrong URL (a
  `localhost:8888` URL only works ON the host machine — they need
  the `trycloudflare.com` one).
- They can't resolve `*.trycloudflare.com` (browser/curl says
  "could not resolve host") → almost always a corporate VPN
  whose DNS filters quick-tunnel hostnames. **Disconnect the
  VPN.** The agent works regardless (CMA connects from its own
  network), but the cast view and any browser access to tunnel
  URLs won't.
- Viewer at `:8088/view` is blank blue → prismarine-viewer y<0 bug.
  `(cd bot && node patch-viewer.cjs) && ./setup.sh --restart`, then
  browser hard-refresh.
- Practice run won't stop after 5 min → a long `go_near` is
  underway; the watchdog interrupts at ~5:05. Ctrl-C is also safe.

**Killing leftovers** (when ports are held by orphans — never use
`lsof -ti:PORT | xargs kill` without `-sTCP:LISTEN`, it can kill
ssh forwarders):

```bash
ps -eo pid,comm,args | awk '$2=="java" && index($0,"server.jar")>0 {print $1}' | xargs -r kill -9
ps -eo pid,comm,args | awk '$2=="node" && index($0,"bot.js")>0 {print $1}' | xargs -r kill
pkill -x cloudflared
```

Logs live at `/tmp/mc-server.log`, `/tmp/mc-bot.log`,
`/tmp/cf-tunnel-8088.log`, `/tmp/host-*.log`.

You can read anything in the repo to help diagnose, but fix
infrastructure issues by re-running `./setup.sh`, not by editing
the scripts (those edits are out of bounds for participants).
