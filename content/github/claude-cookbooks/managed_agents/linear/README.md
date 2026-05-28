# Linear × Claude Managed Agents

`@mention` a Claude [Managed Agent](https://platform.claude.com/docs/en/managed-agents/overview) in a Linear issue and get the reply as a comment.

```
Linear @mention ──▶ /linear-webhook ──▶ sessions.create (+ metadata) ──▶ 200
                                                 │
                               Claude runs to idle on Anthropic infra
                                                 │
/cma-webhook ◀── session.status_idled ◀──────────┘
      │
      └──▶ sessions.retrieve → read metadata → createAgentActivity
```

The CMA session's `metadata` (`linear_session_id`, `linear_org_id`) is the entire routing state.

## Quickstart

```bash
cd managed_agents/linear
bun install
claude
```

Then ask: **"walk me through setting this up."** Claude reads [`skill.md`](./skill.md) and drives the config — Linear OAuth app, Anthropic agent + webhook, env vars, `bun run dev` — in the order that actually works.

## Files

| | |
|---|---|
| `setup/create-agent.ts` | One-time: `agents.create` + `environments.create` |
| `src/main.ts` | Bun server, routes |
| `src/oauth.ts` | Linear OAuth (`actor=app`) + token store |
| `src/agent.ts` | `sessions.create` + `user.message` with routing metadata |
| `src/cma-webhook.ts` | `beta.webhooks.unwrap` → filter by metadata → post reply |
| `skill.md` | Setup walkthrough, gotchas, debugging |

Requires `@anthropic-ai/sdk` ≥ 0.95.1.
