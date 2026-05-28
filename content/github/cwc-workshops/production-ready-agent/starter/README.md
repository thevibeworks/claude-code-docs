# Deal Desk — starter

This is the app you'll build during the workshop. The UI, the event reducer,
the agent definitions, and the provisioning scripts are done. The route
handlers in `app/api/` are stubbed with TODOs; you'll fill them in
one at a time, watching the app come alive as you go.

If you haven't run setup yet, see the [root README](../README.md#setup).

```bash
bun install && bun dev
# open http://localhost:3000
```

Anything stubbed shows up as a red error block in the UI (and a 501 in the
dev-server log) telling you which TODO to go fill in. The errors clear on
their own once a route works — the rails poll, so there's no need to refresh.

## How the stubs work

Each stubbed route handler already parses the request and ends with
`return stub("TODO n", "...")`, which 501s with a message the UI surfaces. A
comment above it sketches the SDK call. Add your code between the comment and
the stub line — `return stub(...)` becomes unreachable once your code returns:

```ts
export async function GET() {
  // TODO 1 — list sessions for the left rail.
  //
  //   const page = await client.beta.sessions.list({ limit: 30 });
  //   return Response.json(page.data);

  const page = await client.beta.sessions.list({ limit: 30 });   // ← your code
  return Response.json(page.data);

  return stub("TODO 1", "client.beta.sessions.list()");          // ← now unreachable
}
```

The stream route (TODO 5) is the one exception: the SSE plumbing lives in
`lib/sse.ts` and hands you a `write(event)` callback; you fill in the loop and
delete the `throw`.

The Managed Agents API surface is documented at
[platform.claude.com/docs/en/managed-agents](https://platform.claude.com/docs/en/managed-agents/quickstart).

## The TODOs

### 1 — list sessions · `app/api/sessions/route.ts`

`client.beta.sessions.list()`. Smallest possible call. The left rail polls
this, so once it works you'll see sessions appear.

### 2 — create a session · `app/api/sessions/route.ts`

`client.beta.sessions.create()`. The "New Session" modal POSTs here. The
big one: you'll wire up the agent, the sandboxed environment, memory and file
mounts, and (when toggled on) the vault for MCP credentials. The modal toggles
map to params:

| Toggle | Param |
| --- | --- |
| Memory on | `resources` includes `{ type: "memory_store", memory_store_id: ids.memoryStore, access: "read_only" }` |
| Files (always) | `resources` includes `{ type: "file", file_id, mount_path: "targets/0.csv" }` per `ids.files` |
| MCP on | `vault_ids: [ids.vault]` |

The agent is always `ids.agent` (latest version). Multiagent is enabled by
running `bin/enable-multiagent.sh`, which adds the sub-agent roster as a new
agent version — new sessions pick it up automatically.

### 3 — send messages and outcomes · `app/api/steer/[id]/route.ts`

`client.beta.sessions.events.send()`. The chat input POSTs here. Build a
`user.message` or a `user.define_outcome` event from the request body and
append it. The first `user.message` flips the session from idle → running. A
`user.define_outcome` declares what done looks like — the grader emits
`agent.outcome_evaluated` events, which the UI renders as the graded thesis.

### 4 — retrieve a session · `app/api/session/[id]/route.ts`

`client.beta.sessions.retrieve(id)`. The right rail polls this for status,
agent config, tools, and outcome evaluations. After TODO 3, you can watch the
session you just messaged flip to `running`.

### 5 — bridge the event stream · `app/api/stream/[id]/route.ts`

`client.beta.sessions.events.list()` + `.stream()`. The chat panel opens an
`EventSource` here. `lib/sse.ts` handles the SSE protocol and dedup; you write
the loop. Open the live tail first, backfill from history, write `READY`, then
tail. Sub-agent thread tabs (and their per-thread streams) show up for free
once this works — same shape, look at `stream/[id]/thread/[threadId]`.

### 6 — confirm gated tool calls · `app/api/confirm/[id]/route.ts`

`client.beta.sessions.events.send()` again, with a `user.tool_confirmation`
event. Tools with an `always_ask` permission policy pause the run and surface
Allow / Deny buttons; this resolves them.

### 7 — delete a session · `app/api/session/[id]/route.ts`

`client.beta.sessions.delete(id)`. The Delete button (with a confirm step)
calls this.

## Stuck?

Diff your route against the reference:

```bash
diff -u app/api/sessions/route.ts ../solution/app/api/sessions/route.ts
```

## Stretch ideas

- Mid-run steering — send a follow-up `user.message` while the agent is
  running and watch it incorporate the new instruction.
- Pause / resume — `sessions.events.send()` accepts `session.pause` and
  `session.resume` events.
- Scheduled deployments — `client.beta.deployments.create()` with a cron
  schedule re-runs the agent on a cadence; great for a daily portfolio
  re-evaluation.
- Tighten the outcome rubric in `seed/outcomes/outcome-schema.json` and watch
  the grader get pickier.
