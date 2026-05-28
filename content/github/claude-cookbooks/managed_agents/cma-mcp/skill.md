# Setup tips & tricks — CMA as an MCP server

Things that aren't obvious from the docs and tend to cost debugging time.

---

## Mental model

### Claude Desktop is the frontend, CMA is the backend

The Claude you're typing to in Desktop is a **relay**. It calls `send_message` with your words, calls `wait_for_idle` to block until the CMA agent finishes, then shows you the reply. The actual work — tool use, code execution, repo edits — happens in the CMA session, not in Desktop.

### Eight 1:1 tools, one shim

`list_agents`, `get_agent`, `create_session`, `send_message`, `interrupt`, `get_session`, `list_events`, `archive_session` are straight endpoint wrappers. `wait_for_idle` is the only editorial: MCP is request/response and CMA completion is SSE, so something has to stream-to-idle inside a tool call.

### `session_id` is the only state, and Claude holds it

`create_session` returns it; Claude passes it to every subsequent call. The MCP server itself is stateless.

### Two transports, one tool set

`src/tools.ts` registers the nine tools. `src/server.ts` wraps it in stdio (Claude Desktop spawns it as a subprocess); `src/server-http.ts` wraps it in Streamable HTTP (claude.ai web reaches it over the network). Pick one.

---

## Setup — Claude Desktop (stdio, local)

1. **Environment** (one-time — sessions need an `environment_id`):
   ```bash
   ant beta:environments create --name cma-mcp \
     --config '{type: cloud, networking: {type: unrestricted}}' --transform id -r
   ```
2. **Agents**: this server doesn't create agents — it drives the ones already in your workspace. Create/update them via the `ant` CLI or the Console.
3. **`.env.local`**:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   CLAUDE_ENVIRONMENT_ID=env_...
   ```
4. **Register with Claude Desktop** — add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) and restart Desktop:
   ```json
   {
     "mcpServers": {
       "cma": {
         "command": "bun",
         "args": ["run", "/absolute/path/to/managed_agents/cma-mcp/src/server.ts"],
         "env": {
           "ANTHROPIC_API_KEY": "sk-ant-...",
           "CLAUDE_ENVIRONMENT_ID": "env_..."
         }
       }
     }
   }
   ```
5. **Test**: in a new Desktop chat, ask *"list my managed agents, start a session with the first one, and relay this message to it: hello."*

---

## Setup — claude.ai web (Streamable HTTP, remote)

Same tools, but the server runs at a public URL and claude.ai connects to it as a custom Connector.

1. **Token** — generate and keep it; anyone with this token can drive your agents:
   ```bash
   export CMA_MCP_TOKEN=$(openssl rand -hex 32)
   ```
2. **Run locally first** (ngrok/cloudflared for a public URL while testing):
   ```bash
   bun run http   # → :3000/mcp
   ```
3. **Deploy** — the `Dockerfile` targets Fly / Railway / Render; set `ANTHROPIC_API_KEY`, `CLAUDE_ENVIRONMENT_ID`, `CMA_MCP_TOKEN` as secrets. (Cloudflare Workers also works — `WebStandardStreamableHTTPServerTransport` is fetch-native; swap `process.env` → `env` and `Bun.serve` → `export default { fetch }`.)
4. **claude.ai → Settings → Connectors → Add custom connector**:

   | Field | Value |
   |---|---|
   | Name | `CMA` |
   | URL | `https://<your-deploy>/mcp` |
   | Authentication | Bearer token → your `CMA_MCP_TOKEN` |

   > **Team / Enterprise orgs:** adding a connector by URL is typically **org-admin only** — individual users see a curated directory, not a URL field. An admin adds the URL + token once in org settings; it then appears in every member's Connectors list to enable. (This is the shape you want for rolling out to non-technical users anyway.)

5. **Test**: new chat → enable the `CMA` connector → same prompt as above.

---

## Relay mode (recommended Project instructions)

Without guidance, Desktop Claude will try to answer the user itself instead of relaying. Put this in a Project's custom instructions:

> You are a frontend for a backend Managed Agent reached via the `cma` MCP tools. On the first user turn: `list_agents` (if needed) → `create_session` → `send_message(user text verbatim)` → `wait_for_idle` → return the `reply` verbatim. On subsequent turns: `send_message` → `wait_for_idle`. Do not answer from your own knowledge; do not paraphrase the backend's reply. If `wait_for_idle` returns `status: "timeout"`, tell the user it's still running and offer to keep waiting.

---

## Gotchas

### stdio = Desktop only; HTTP = the internet

Browser claude.ai can't spawn a local process, so stdio only works with Claude Desktop / Claude Code. The HTTP path gets you claude.ai web, but now the URL is public — the **bearer token is the only gate** in front of your `ANTHROPIC_API_KEY`'s CMA quota. Don't deploy without it, don't log it, rotate it like any API key.

### Long turns vs tool timeout

`wait_for_idle` blocks. If the CMA agent runs for minutes (big repo clone, many tool calls), the MCP client may time out the tool call. Mitigations: pass a smaller `timeout_sec` and loop (`wait_for_idle` returns `status: "timeout"` + `last_event_id`; call again), or have Claude poll `get_session` + `list_events(after_id=...)` instead.

### Billing

All CMA usage bills to the `ANTHROPIC_API_KEY` baked into the server config — not to the Desktop user's account. That's the point (non-technical users, no keys), but size the key's workspace limits accordingly.

### Deliberately not exposed

| Endpoint | Why not |
|---|---|
| `agents.archive` | Permanent, no undo — one bad tool call bricks a prod agent |
| `agents.create` / `update` | Authoring belongs in the `ant` CLI / Console, not a chat turn |
| `sessions.delete`, `environments.*` | Destructive infra ops |
| `vaults.*`, `credentials.*` | Secrets |
| `sessions.resources.add` | Needs tokens/file IDs the chat user won't have |

Adding any of these is a few lines in `src/cma.ts` + `src/server.ts` if your use case needs them.

---

## Debugging

| Symptom | Check |
|---|---|
| Desktop shows no `cma` tools | Config path wrong, or `bun` not on PATH for the Desktop process (use an absolute path to `bun`). Check Desktop's MCP logs. |
| `CLAUDE_ENVIRONMENT_ID is required` | Env block missing from the Desktop config — stdio servers don't read your shell's env. |
| `wait_for_idle` returns empty `reply` | Agent went idle without emitting text (e.g. only tool calls). `list_events` shows the full log. |
| Every turn starts a new session | Claude isn't threading `session_id`. Tighten the Project instructions. |
| claude.ai Connector shows "couldn't connect" | URL wrong, server not reachable, or token mismatch (check server logs for 401). |
| HTTP server returns 401 locally | `CMA_MCP_TOKEN` not exported in the shell you ran `bun run http` from. |
