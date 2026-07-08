# Setup walkthrough

Work top to bottom. Every step has a verification before the next one starts.

## 1. Keys

| key | where | notes |
|---|---|---|
| `ANTHROPIC_API_KEY` | <https://console.anthropic.com/settings/keys> | or skip it and sign in once with `ant auth login`. The org needs Managed Agents access |
| `NATIONAL_PARK_SERVICE_API_KEY` | <https://www.nps.gov/subjects/developer/get-started.htm> | free, emailed instantly |
| `WINDY_API_KEY` | <https://api.windy.com/point-forecast/docs> | free tier, point-forecast product |

```bash
cp .env.example .env.local   # then fill in the three keys
```

Verify the vendor keys from your own machine before involving the sandbox:

```bash
curl -sS "https://developer.nps.gov/api/v1/alerts?parkCode=acad&limit=1" -H "X-Api-Key: $NATIONAL_PARK_SERVICE_API_KEY" | head -c 300
curl -sS -X POST "https://api.windy.com/api/point-forecast/v2" \
  -H "Content-Type: application/json" \
  -d '{"lat":44.35,"lon":-68.21,"model":"gfs","parameters":["temp"],"levels":["surface"],"key":"'"$WINDY_API_KEY"'"}' | head -c 300
```

Both return JSON. A 403 here is a key problem, not a cookbook problem.

## 2. Provision

```bash
npm install
npm run setup
```

Creates the environment (networking limited to `developer.nps.gov` and `api.windy.com`), the reviewer agent (Opus, review-only prompt), the planner agent (bash on, `web_search`/`web_fetch` off, a `multiagent` coordinator roster naming the reviewer), the vault, and two `environment_variable` credentials with the `injection_location` each vendor documents hardcoded (NPS: header, Windy: body). Writes six `ROADTRIP_PLANNER_*` ids into `.env.local`. Re-running is a no-op while the agent exists (it does demand `--force` if the stored planner predates the reviewer roster), and `--force` provisions a fresh copy.

## 3. Run

```bash
npm run dev
```

Open <http://localhost:3000>. The page creates one session per browser on load (cookie `roadtrip_planner_session_id`), so the sandbox is warm before the first question. Then do the four beats in [README.md](./README.md#four-things-to-do-with-it), in order. Beat 2 is the vault story and it only lands after a real conversation exists. Beat 3 is the `agent_with_overrides` model picker. Beat 4 is the multi-agent review: it needs a full itinerary ask, not a one-fact question.

## Debugging

| symptom | cause | fix |
|---|---|---|
| `npm run setup` 404s on `/v1/environments` | org not enrolled in Managed Agents | request access, or switch orgs |
| `tsc` rejects `event_deltas`, `injection_location`, or the `lib/sessions/accumulate` import | installed SDK predates the 2026-07-01 Managed Agents update | upgrade `@anthropic-ai/sdk` |
| replies arrive whole, no token-by-token rendering | the org's streaming gate is closed (`event_deltas` is silently ignored when ungated), or an older SDK's stream parser drops the `event_start` / `event_delta` events it does not recognize | confirm the org is enrolled in the update; upgrade `@anthropic-ai/sdk` |
| picking a model 400s with "Agent must be a non-empty Agent ID or agent_reference" (or the older "Extra inputs are not permitted") | the org's gate for `agent_with_overrides` is not open yet (a closed gate rejects the selector as an unknown agent shape) | use the default model until the org is enrolled in the update |
| picking a model 400s with `agent_field_not_overridable` | the selector carried a key that is not overridable (the gate is open; only `model`, `system`, `tools`, `mcp_servers`, `skills` may be overridden) | only happens if you edited `createTripSession`: remove the extra key |
| boot screen says `Missing ROADTRIP_PLANNER_AGENT_ID` | `.env.local` not written or dev server started before setup | run `npm run setup`, restart `npm run dev` |
| events arrive only in end-of-turn bursts | a proxy is buffering the SSE response | use `next dev` directly on localhost first |
| answer cites no tool calls | the agent answered from priors | the prompt demands API evidence per claim: re-run `npm run setup -- --force` if you weakened it |
| itinerary arrives with no review handoff (no thread events in the rail) | the stored planner predates the reviewer roster (provisioned before the multiagent change), or the question was small enough that the prompt's "skip the review" branch applied | re-run `npm run setup -- --force`; ask for a full multi-day itinerary |
| `npm run setup` 400s creating the planner, naming `multiagent` | the org is not enrolled in the Managed Agents update that ships coordinator rosters | use a single-agent copy (delete the `multiagent` line in `setup/create.ts`) until the org is enrolled |
| every NPS call 403s with header injection on | the National Park Service key itself is bad | re-run the step 1 curl from your machine |
| `session.error` `credential_host_unreachable_error` | the credential allows a host the environment's networking does not | both `allowed_hosts` lists must name the vendor host |
| the chat resets to an empty trip after a teardown | the cookie pointed at an archived session, so a fresh one was created | expected: archived sessions cannot take another message |

## Reset

```bash
npm run teardown            # archive sessions, both agents, vault, credentials, environment
npm run setup -- --force    # provision a fresh copy
```
