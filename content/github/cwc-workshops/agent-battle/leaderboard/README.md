# Agent Battle leaderboard

Live cast-mode leaderboard for the Agent Battle workshop.

**Stack:** static HTML/JS + Netlify Functions + Supabase.

## How scoring works

```
score = achievement_points - (tokens / 100) - (turns × 2)
```

Achievement points are assigned per-item so the sum equals Matt's formula
`(iron ? 1000 : milestone_idx×200) + (bonus_milestones×200) + (quests×100)`:

| Achievement | Kind | Points |
|---|---|---|
| wooden_pickaxe | milestone | 200 |
| stone_pickaxe | milestone | 200 |
| furnace | milestone | 200 |
| **iron_ingot** | **milestone** | **400** ← cumulative 1000 here |
| iron_pickaxe | milestone (bonus) | 200 |
| diamond | milestone (bonus) | 200 |
| first_block, chat_to_player, meet_a_friend, home_builder, light_it_up, deep_diver | quest | 100 each |

Calibration: 30k tokens = 300-point penalty.

## One-time setup (facilitator)

1. **Supabase**: create a project, open SQL Editor, run `supabase-setup.sql`
   then `supabase-minecraft.sql`. Insert one workshop row:
   ```sql
   INSERT INTO workshops (alias) VALUES ('minecraft-2026') RETURNING id;
   ```
   Note the returned UUID — that's `WORKSHOP_ID`.

2. **Netlify**: deploy this `leaderboard/` directory. Set env vars:
   | Var | Value |
   |---|---|
   | `SUPABASE_URL` | from Supabase project settings |
   | `SUPABASE_SERVICE_KEY` | from Supabase API keys |
   | `WORKSHOP_ID` | the UUID from step 1 |
   | `WORKSHOP_KEY` | any shared secret, e.g. `openssl rand -hex 16` |
   | `JWT_SECRET` | `openssl rand -base64 32` |
   | `ADMIN_PASSWORD` | facilitator's choice |

3. **Cast view**: open `https://<your-deploy>.netlify.app/?workshop=minecraft-2026`,
   click Leaderboard → Cast Mode, put it on the projector.

## Per-participant setup

Each participant sets two env vars before launching their bot:

```bash
export PARTICIPANT="alice"
export LEADERBOARD_URL="https://<deploy>.netlify.app/api"
export LEADERBOARD_KEY="<the WORKSHOP_KEY value>"
./bot/run.sh
```

That's it. `bot.js` auto-reports every milestone and side quest to
`$LEADERBOARD_URL/achievement` as it happens. `my_agent.py` (or
`harness.agent` for the Messages-API reference path) reports token+turn
counts to `$LEADERBOARD_URL/cost` every few turns and once more on exit.

## Endpoints

| Path | Method | Auth | Body |
|---|---|---|---|
| `/api/achievement` | POST | `x-workshop-key` header | `{participant, kind, id, ts}` |
| `/api/cost` | POST | `x-workshop-key` header | `{participant, tokens, turns, run_id?}` |
| `/api/leaderboard?workshop=<alias>` | GET | none | — |
| `/api/login`, `/api/tasks/*`, `/api/admin/*` | — | inherited from upstream | — |

## Local dev

```bash
cd leaderboard
npm install
node dev-server.mjs   # http://localhost:3000
```

Set the same env vars in a `.env` file at `leaderboard/.env`.
