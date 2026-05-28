# Linear × Claude Managed Agents bridge

Stateless webhook bridge: Linear `AgentSessionEvent` → CMA session (with routing metadata) → `session.status_idled` webhook → `createAgentActivity` reply.

## When the user asks to set this up, get it working, or debug it

1. **Invoke `/claude-api` first.** That skill loads the full Managed Agents API reference (agents, sessions, environments, events, webhooks, outcomes, multiagent, vaults, memory stores). Use it as the source of truth for any SDK call you write or edit — don't guess field names.
2. **Read `./skill.md`** and walk the user through it step by step. It has the ordered checklist, every gotcha (workspace-scoped webhooks, `actor=app` OAuth, 10s ack rule, retrieve-then-filter), and the debugging table.
3. **After the base bridge works, offer extensions.** Ask the user which (if any) they want, then edit `setup/create-agent.ts` and/or `src/agent.ts` accordingly:
   - **GitHub repo** — mount a repo into the session container (`resources: [{type: "github_repository", ...}]` on `sessions.create`)
   - **MCP tools** — e.g. Linear or GitHub MCP so the agent can act, not just reply (`mcp_servers` + `mcp_toolset` on the agent; credentials via a vault, `vault_ids` on the session)
   - **Outcomes** — rubric-graded iterate loop (`user.define_outcome` event instead of `user.message`)
   - **Multiagent** — coordinator + subagent roster (`multiagent: {type: "coordinator", agents: [...]}` on the agent)
   - **Memory store** — cross-session persistence (`resources: [{type: "memory_store", ...}]`)
   - **Custom tools** — host-side execution via `agent.custom_tool_use` / `user.custom_tool_result`

   Pull exact shapes from the `/claude-api` skill's `shared/managed-agents-*.md` docs.

Run the server with `bun run dev`. One-time agent provisioning is `bun run setup`.
