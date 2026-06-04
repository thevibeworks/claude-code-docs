# Agent Battle — Claude plays Minecraft

> **Workshop demo.** Not maintained and not accepting
> contributions. Report security issues to
> security@anthropic.com; we do not commit to fixes or
> timelines.
>
> Not an official Minecraft event. Anthropic is not affiliated
> with, endorsed by, or sponsored by Microsoft / Mojang. The
> Minecraft trademarks, characters, and game are the property
> of Microsoft / Mojang.

A 45-minute hands-on workshop on **Claude Managed Agents**.
You configure an agent (model + system prompt + skills + MCP tools);
Anthropic's cloud runs it and drives a local Minecraft bot over
MCP. Most diamonds wins; fewest tokens breaks ties. Best single
run counts.

Your bot connects **outbound** to the event server, and the cloud
agent reaches it through that connection — nothing on your machine
is exposed to the internet and no tunnels are created.

> Hosting a session? See [`HOST.md`](HOST.md). Everyone else,
> read on.

## 1. Clone

```bash
git clone https://github.com/anthropics/cwc-workshops
cd cwc-workshops/agent-battle
```

## 2. Set your env (in the same terminal)

```bash
export ANTHROPIC_API_KEY="sk-ant-..."     # console.anthropic.com → API Keys
                                          # (optional if your environment has
                                          #  OAuth / workload-identity SDK auth)
export PARTICIPANT="<your-unique-name>"
export MINECRAFT_EULA=accept              # you have read https://www.minecraft.net/eula and agree
```

The event server URL and world seed come from `.env.event` in
this directory — `setup.sh` reads it automatically. If the host
announces a new URL mid-session, `git pull` picks it up (or you
can `export EVENT_URL=...` to override).

These must be exported **before** launching Claude Code so it
inherits them.

## 3. Setup

```bash
claude --permission-mode acceptEdits
```

At the Claude Code prompt, type:

```
/cwc-setup
```

Claude installs deps, starts your local Minecraft server + bot,
connects the bot to the event relay, and fixes whatever breaks on
your machine (Java, npm, ports, PEP-668, stale processes). Ends
with `▸ ready`. ~90s on a cold first run, ~25s after.

> The `--permission-mode acceptEdits` flag lets `/cwc-setup` run
> its shell steps without a y/n prompt for each. If Claude Code
> itself errors (e.g. *"previous_message_id must be from a prior
> response"*), that's a transient CC hiccup — Ctrl-C and relaunch.
> If your CC normally uses subscription auth and the workshop
> `ANTHROPIC_API_KEY` confuses it, launch CC first (it'll use its
> stored auth), then export the key after for `my_agent.py`.
>
> No Claude Code? Run `./setup.sh` instead — same script, you
> just troubleshoot it yourself.

## 4. Run

```bash
python3 my_agent.py
```

**Every run is 5 minutes and posts to the leaderboard.** Open
`http://localhost:8088/view` — your bot's first-person camera
with a live 💎 counter and inventory. (Fallback: `localhost:3007`.)

Run as many times as you want — **only your best 5-minute run
counts**, runs don't sum. The 5-minute cap and the start position
are fixed by the bot and enforced by the leaderboard, not by
anything in `my_agent.py`.

## 5. Iterate

Open `my_agent.py` → the `AGENT = dict(...)` block. Write `system`.
Re-run step 4. Repeat.

For feedback faster than 5 minutes:
```bash
python3 my_agent.py --eval
```
~30-60s. Scores your config on a set of single-turn decision
probes and tells you which ones it gets wrong — no Minecraft run,
no vein luck.

## 6. If anything breaks

In Claude Code: **`/cwc-fix`**. Or the blunt instrument:

```bash
./setup.sh --restart && rm -f .agent_cache.json
```

---

## What to expect

The bot starts at y=-40 with an iron pickaxe and spare materials.
Even with an empty `system`, Claude gets diamonds — it knows
Minecraft. The competition is **efficiency**: more diamonds per
token in a 5-minute run. The default agent chats too much, polls
state redundantly, and doesn't relocate after veins; a tuned
`system` fixes those.

Worth discovering yourself: attaching the wiki MCP *without* a
prompt nudge gives the agent a `lookup()` tool it never calls; a
from-scratch prompt that ignores the start_kit inventory can send
the agent crafting things it already has. Both are real lessons
about agent composition.

## Known issues

**Viewer is blank blue underground** → prismarine-viewer issue
#250 (doesn't render y<0). `npm install` runs a postinstall patch;
if you have an old `node_modules`,
`(cd bot && node patch-viewer.cjs) && ./setup.sh --restart` then
hard-refresh (Cmd-Shift-R). The HUD overlay works regardless.

**"Cannot GET /view"** → a stale bot from an earlier clone is
holding port 8088. `./setup.sh --restart` (or `/cwc-fix`).

**"bot is not connected to the relay"** → your bot lost its
connection to the event server; it reconnects automatically within
seconds. If it persists, `./setup.sh --restart`.

## Layout

```
my_agent.py        the AGENT = dict(...) block — your whole interface
setup.sh           participant launcher (deps, server, bot, relay)
host.sh            facilitator: self-hosted event server (fallback path)
HOST.md            facilitator runbook
CLAUDE.md          troubleshooting playbook (Claude Code reads this)
.claude/commands/  /cwc-setup, /cwc-fix
skills/            opt-in mining skill (a lever)
bot/               mineflayer bot, MC server, relay client
harness/           logging, --eval probes, verify.py, Messages-API reference
event/             the shared event server (leaderboard + wiki MCP + bot
                   relay + admin panel) — facilitators deploy this; you
                   don't run it (setup.sh starts a local one in solo mode)
```

## License

Apache 2.0 — see [`LICENSE`](../LICENSE).
