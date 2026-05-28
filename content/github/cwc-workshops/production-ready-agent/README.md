# Deal Desk — a Claude Managed Agents workshop

Workshop sample code. Not maintained and not accepting contributions.

A chat-first UI over a multi-agent M&A research team, built on the Claude
Managed Agents API. A coordinator agent delegates to four research sub-agents
in parallel, reads prior-deal lessons from a memory store, can reach Linear
via MCP + Vault, and emits a graded investment thesis. The UI streams every
event, lets you confirm gated tool calls, define outcomes inline, and tab
into each sub-agent's thread.

All companies and financials are fictitious.

## Repo layout

```
starter/      The app you build during the workshop. The UI, event reducer,
              and provisioning are done — the API route handlers are stubbed
              with TODOs. Start here.
solution/     The finished reference. Diff against starter/ when stuck.
seed/         Shared workshop assets: agent configs, sandbox env, memory
              entries, fictional target CSVs, the outcome rubric.
bin/          Idempotent provisioning scripts that hit the Managed Agents API
              once and write IDs into .env. Both apps read the same .env.
```

`starter/` and `solution/` are identical Next.js apps; the only difference is
whether the route handlers in `app/api/` are filled in. Diff them any time:

```bash
diff -ru starter/app/api solution/app/api
```

## Prerequisites

- An Anthropic API key with the Managed Agents beta enabled
- The [`ant` CLI](https://platform.claude.com/docs/en/managed-agents/quickstart):
  `brew install anthropics/tap/ant` on macOS, or see the
  [quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart)
  for Linux and other platforms
- [bun](https://bun.sh) and `jq`

## Setup

Provision once — both apps share the resources:

```bash
cp .env.example .env
# Fill in ANTHROPIC_API_KEY.

./bin/setup.sh               # provisions environment, sub-agents, coordinator
                             # (v1, no roster), memory store, files; writes
                             # the IDs back into .env and copies it into each app
./bin/enable-multiagent.sh   # adds the sub-agent roster to the coordinator → v2
                             # (you'll run this mid-workshop, but it's safe now)

cd starter && bun install
```

`setup.sh` is idempotent — re-running reuses existing IDs instead of creating
duplicates. The coordinator is the exception: it is recreated fresh at v1 each
time, because `agents.update` cannot remove an existing `multiagent` block.
Sessions always use the latest agent version, so once `enable-multiagent.sh`
has run, new sessions get the sub-agent roster.

## Run

```bash
cd starter && bun dev
# open http://localhost:3000
```

Each app reads its own `.env` (synced from the repo-root `.env` by `setup.sh`).
`lib/anthropic.ts` reads the file directly so a shell-exported
`ANTHROPIC_API_KEY` won't shadow it.

## What you'll build

`starter/README.md` walks the seven exercises. In short:

| TODO | File | API surface |
| --- | --- | --- |
| 1. List sessions | `app/api/sessions/route.ts` | `sessions.list` |
| 2. Create a session | `app/api/sessions/route.ts` | `sessions.create` — agent, environment, resource mounts, vault |
| 3. Send messages and outcomes | `app/api/steer/[id]/route.ts` | `sessions.events.send` — `user.message`, `user.define_outcome` |
| 4. Retrieve a session | `app/api/session/[id]/route.ts` | `sessions.retrieve` |
| 5. Bridge the event stream | `app/api/stream/[id]/route.ts` | `sessions.events.list` + `sessions.events.stream` → SSE |
| 6. Confirm gated tool calls | `app/api/confirm/[id]/route.ts` | `sessions.events.send` — `user.tool_confirmation` |
| 7. Delete a session | `app/api/session/[id]/route.ts` | `sessions.delete` |

Already done for you and worth reading:

| Feature | Where |
| --- | --- |
| Per-thread event streams | `app/api/stream/[id]/thread/[threadId]/route.ts` |
| List sub-agent threads (`threads.list`) | `app/api/session/[id]/threads/route.ts` |
| SSE encoder / dedup / error bridge | `lib/sse.ts` |
| Event → chat message reducer | `lib/chat.ts` |
| Agent + sub-agent definitions | `seed/agents/*.yaml` |
| Sandbox config | `seed/environments/research.yaml` |
| UI | `components/ChatPanel.tsx`, `SessionRail.tsx`, `ai/*` |

## Optional: MCP + Vault via Linear

The coordinator can read open diligence issues from Linear over MCP, with the
end-user's Linear token held in a Vault. To exercise it, fill `LINEAR_API_KEY`
and `LINEAR_TEAM_ID` in `.env`, run `./bin/seed-linear.sh` to create some
fictional diligence issues, and create a Vault holding the same token. Set
`VAULT_ID` and toggle "MCP" on in the New Session modal.
