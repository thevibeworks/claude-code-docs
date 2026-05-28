# Deal Desk — solution

The finished reference for the workshop. Same app as `starter/`, with all the
route handlers in `app/api/` fully implemented. See the
[root README](../README.md) for setup and the
[starter README](../starter/README.md) for the exercise walkthrough.

```bash
bun install && bun dev
# open http://localhost:3000
```

## Map

| Surface | File |
| --- | --- |
| `sessions.list` / `sessions.create` (agent, env, resources, vault) | `app/api/sessions/route.ts` |
| `sessions.retrieve` / `sessions.delete` | `app/api/session/[id]/route.ts` |
| `sessions.events.list` + `events.stream` → SSE | `app/api/stream/[id]/route.ts` |
| Per-thread `threads.events.*` → SSE | `app/api/stream/[id]/thread/[threadId]/route.ts` |
| SSE encoder / dedup / error-event bridge | `lib/sse.ts` |
| `events.send` (`user.message`, `user.define_outcome`) | `app/api/steer/[id]/route.ts` |
| `events.send` (`user.tool_confirmation`) | `app/api/confirm/[id]/route.ts` |
| List sub-agent threads (`threads.list`) for the tab row | `app/api/session/[id]/threads/route.ts` |
| Event → chat message reducer | `lib/chat.ts` |
| Anthropic client + ID lookup from `.env` | `lib/anthropic.ts` |

When comparing against `starter/`, only the route handlers under `app/api`
differ — the UI, lib, and config are identical:

```bash
diff -ru ../starter/app/api app/api
```
