# Road trip planner (Claude Managed Agents + Next.js)

A Next.js chat built directly on a Managed Agent session: no chat framework,
the event log is the app state. Teaches session event streaming
(`event_deltas`), vault credential `injection_location`, per-session
`agent_with_overrides`, and `multiagent` coordinator rosters. The planner
calls the National Park Service and Windy APIs with keys it never holds,
then hands its draft to a second agent - an Opus reviewer running as a
session thread - for a quick critique.

## When the user asks to set this up, run it, or debug it

1. **Invoke `/claude-api` first.** It loads the Managed Agents API reference
   (agents, environments, sessions, events, vaults, credentials, webhooks).
   Use it as the source of truth for any SDK call you write or edit here.
   Don't guess field names.
2. **Read [`./skill.md`](./skill.md)** and walk the user through it in order.
   It has the key signups, the provisioning step, a pointer to the four
   README beats, and the debugging table.
3. The two files worth reading before changing anything are
   `src/lib/use-managed-agent-session.ts` (the client runtime: one EventSource, the
   SDK accumulator, the re-sync-on-connect habit) and `setup/create.ts`
   (where `injection_location` and the `multiagent` roster are set).
   `src/lib/transcript.ts` is the one fold both first paint and live
   streaming render through.

## Invariants to preserve when editing

- The stream is a tail, not a replay, and previews are never persisted: every
  EventSource (re)connect re-fetches the event log (via `/api/session`)
  before trusting the tail. Do not "optimize" that fetch away. It is the
  entire resume story.
- Previews are speculative. The accumulator's snapshot retires when the
  buffered `agent.message` with the same id lands in the log, an orphan
  `event_delta` (attached mid-generation) is dropped, and an errored
  `span.model_request_end` discards the open snapshot.
- One fold (`transcript.ts`) renders both history and live state. If a new
  event type should render, it goes in the fold, not in a second mapping.
- `web_search` and `web_fetch` stay disabled on the agent. With them on, the
  model answers from the open web and the vault demo proves nothing.
- The reviewer stays tool-free: its toolset is deny-by-default
  (`default_config: { enabled: false }`), and the prompt says the same. The
  review must come from the draft alone - a poisoned draft must have no tool
  to reach, and the rail must not fill with a second agent's curls.
- The handoff is prompt-triggered. The planner's "Review step" prompt
  section decides when to message the reviewer; the user never asks and the
  app sends nothing. Weaken that section and beat 4 silently disappears.
- The environment's `allowed_hosts` and each credential's `allowed_hosts`
  both list the vendor host. Drop either and the calls fail differently.
- The header's model picker shows `session.agent.model` from the API
  response, never client state. An override must be visible as the resolved
  snapshot or the demo proves nothing.
- No database. If a change needs one, it does not belong in this cookbook.
