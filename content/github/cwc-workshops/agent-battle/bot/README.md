# Claude Plays Minecraft — Layer 1: bot server

A mineflayer bot connected to a vanilla Minecraft server, with an HTTP seam
(`GET /state`, `POST /action`) that a Claude tool-use loop will drive.
Open-source so audience members can join the same server during demos.

## Five commands from clone to moving bot

```bash
# 1. install java 21 (host) and node deps
sudo apt-get install -y openjdk-21-jre-headless && cd bot && npm install

# 2. start the Minecraft server (downloads jar on first run, ~50 MB)
./server.sh &

# 3. start the bot (connects as "claude", viewer on :3007)
node bot.js &

# 4. peek at state
curl -s localhost:8088/state | jq .

# 5. tell the bot to do something
curl -s -XPOST localhost:8088/action \
  -H 'content-type: application/json' \
  -d '{"name":"chat","args":{"text":"hello world"}}'
```

## Layout

```
bot/
  server.sh       # downloads + launches MC 1.20.4 server, offline-mode
  bot.js          # mineflayer bot + Express on :8088 + viewer on :3007
  package.json
  server/         # created on first run (jar, world, eula.txt)
  README.md       # this file
```

## API

`GET /state` → JSON snapshot. Top-level fields:

```jsonc
{
  "connected": true,
  "position": {"x","y","z"},
  "health": 20, "food": 20,
  "time_of_day": 6000,
  "dimension": "minecraft:overworld",
  "inventory": [{"name","count","slot"}],
  "equipped":  {"hand", "armor": {"head","torso","legs","feet"}},
  "nearby_blocks":   [{"name","pos","distance"}],   // within 16, dedup by name (nearest)
  "nearby_entities": [{"name","type","pos","distance"}],
  "busy": false,
  "last_error": null
}
```

`POST /action` body `{"name": "...", "args": {...}}` →
`{"ok":true,...}` or `{"ok":false,"error":"reason"}`. Only one action runs at
a time; concurrent calls return HTTP 409 with `{ok:false,error:"busy"}`.

| Action | Args |
|---|---|
| `mine_block` | `{name, max?}` |
| `craft_item` | `{name, count?}` |
| `smelt` | `{input, fuel, count?}` |
| `go_near` | `{block_name?, entity_name?, pos?}` |
| `place_block` | `{name, against?}` |
| `equip` | `{name, destination?}` |
| `drop` | `{name, count?}` |
| `chat` | `{text}` |

## Acceptance test

```bash
./bot/server.sh &
node bot/bot.js &
sleep 30   # wait for world gen + bot spawn

curl -s :8088/state | jq .inventory                                    # → []
curl -s -XPOST :8088/action -H 'content-type: application/json' \
  -d '{"name":"mine_block","args":{"name":"oak_log","max":3}}'
# watch http://localhost:3007 — bot walks to tree, punches
curl -s :8088/state | jq .inventory                                    # → oak_log x3
curl -s -XPOST :8088/action -H 'content-type: application/json' \
  -d '{"name":"craft_item","args":{"name":"oak_planks"}}'
curl -s :8088/state | jq .inventory                                    # → oak_planks present
```

## Notes

- `online-mode=false` in `server/server.properties` is load-bearing: it
  removes the Mojang auth requirement so audience members can join with any
  username, no Microsoft account needed.
- Server version is pinned to 1.20.4 in `server.sh` to match what current
  mineflayer (4.20.x) supports cleanly. Bumping the MC version usually means
  bumping mineflayer too.
- The bot reconnects automatically with a 3s backoff if the server restarts.
- `nearby_blocks` is deduped to one entry per block-type (the nearest) so the
  state payload doesn't blow up with hundreds of stone entries.
