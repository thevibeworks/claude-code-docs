# Upgrading "Running a self-hosted worker"

This guide takes the **previous** version of the doc — the one whose library
examples use `anthropic.lib.runner`, `tool_dispatcher` / `toolDispatcher`,
`default_tools` / `defaultTools`, a per-work-item `secret` / `sessions_token`,
and `ant worker poll` / `ant worker dispatch` — to the **released** SDK builds.
Work top to bottom; each step is independent.

| Component | Old | New (released) |
|---|---|---|
| Python SDK | `f05960786cb8cc64687c412a854c12a74e8d7d14` (`0.101.0`, prerelease build) | [`anthropic` `0.103.0`](https://pypi.org/project/anthropic/) on PyPI |
| TypeScript SDK | `95eb73baf081255be96ba0e81b6adbed997a8cd0` (prerelease build) | [`@anthropic-ai/sdk` `0.97.0`](https://www.npmjs.com/package/@anthropic-ai/sdk) on npm |
| `ant` CLI | `ab077f895de18a8d09d6bcd3d65e269333f6870c` (prerelease build) | GitHub release [`v1.9.0`](https://github.com/anthropics/anthropic-cli/releases/tag/v1.9.0) |

There are **three** kinds of change: a new auth model, a renamed CLI command,
and a reshaped library. They're independent — do them in any order.

---

## Change 1 — One credential, the environment key

The doc's whole auth story collapses to a single credential.

**Before:** a "service key" authorized `work.poll` *only*, and each claimed work
item carried a `secret` you decoded into a per-work-item `sessions_token` that
authenticated everything session-scoped (event stream, heartbeat, force-stop,
skill download).

**After:** a single **environment key** authenticates *all* of it. There is no
per-work secret in the worker flow — construct the SDK client with the
environment key and it flows everywhere. `decodeWorkSecret` is not exported;
`sessions_token` is gone.

| Old | New |
|---|---|
| `ENVIRONMENT_SERVICE_KEY` / `ANTHROPIC_ENV_KEY` | `ANTHROPIC_ENVIRONMENT_KEY` |
| `service_key=` / `serviceKey:` (SDK) | `environment_key=` / `environmentKey:` |
| `secret` / `sessions_token` / `decodeWorkSecret` | *(removed from the worker flow)* |
| Console: "Generate **service key**" | "Generate **environment key**" |

Doc edits: §1 "Generate an environment service key" → "Generate the environment
key", `ENVIRONMENT_SERVICE_KEY` → `ANTHROPIC_ENVIRONMENT_KEY`, and "authorizes
`work.poll`" → "authenticates the whole worker flow — poll, ack, stop,
heartbeat, the session event stream, skill download". §2 `ANTHROPIC_ENV_KEY` →
`ANTHROPIC_ENVIRONMENT_KEY`.

## Change 2 — The `ant` CLI: `worker` → `beta:worker`, `dispatch` → `run`

This is new in the released CLI and the previous doc gets it wrong everywhere.

| Old | New |
|---|---|
| `ant worker poll` | `ant beta:worker poll` |
| `ant worker dispatch` | `ant beta:worker run` |
| `--service-key` / `ANTHROPIC_ENV_KEY` | `--environment-key` / `ANTHROPIC_ENVIRONMENT_KEY` |
| `--session-token` flag | *(removed — `run` uses `--environment-key`)* |
| `--allow-absolute-paths` | `--unrestricted-paths` |
| `ANTHROPIC_SESSION_TOKEN` env var | `ANTHROPIC_ENVIRONMENT_KEY` |

Why: in the released CLI the `beta:`-prefixed entries are the API-resource
commands (`beta:environments:work`, `beta:sessions`, …); the self-hosted worker
moved under the same prefix as `beta:worker`, and its container-entrypoint
subcommand was renamed `dispatch` → `run`. The `run` env contract is
`ANTHROPIC_{SESSION_ID,ENVIRONMENT_KEY,WORK_ID,ENVIRONMENT_ID,BASE_URL}`.

Doc edits:
- **§3 "Start the worker":** `ant worker poll` → `ant beta:worker poll`; the
  zero-flag example's `ANTHROPIC_ENV_KEY=…` → `ANTHROPIC_ENVIRONMENT_KEY=…`.
- **§ "Spawning your own process per work item":** the `--on-work` env list and
  the `docker run -e …` example — drop `ANTHROPIC_SESSION_TOKEN`, add
  `ANTHROPIC_ENVIRONMENT_KEY`; `ant worker dispatch` → `ant beta:worker run`.
- **§ "Running the dispatcher as a container entrypoint":** the Dockerfile
  `ENTRYPOINT ["ant", "worker", "dispatch"]` → `["ant", "beta:worker", "run"]`;
  switch `ARG ANT_SHA` (Stainless `dist.zip`) to `ARG ANT_VERSION=1.9.0` with
  the GitHub-release `.tar.gz`; drop `ANTHROPIC_SESSION_TOKEN` from the
  "Pass … as container env vars" line, add `ANTHROPIC_ENVIRONMENT_KEY`.
- **§ "Alternative: run the dispatcher directly":** `ant worker dispatch` →
  `ant beta:worker run`; `--session-token "$SESSION_TOKEN"` →
  `--environment-key "$ANTHROPIC_ENVIRONMENT_KEY"`; in the env-vars-only form,
  `ANTHROPIC_SESSION_TOKEN` → `ANTHROPIC_ENVIRONMENT_KEY`.
- **§ "Flags" table:**
  - `--service-key | ANTHROPIC_ENV_KEY | required for poll` →
    `--environment-key | ANTHROPIC_ENVIRONMENT_KEY | required`
  - `--allow-absolute-paths` → `--unrestricted-paths`
  - Everything else (`--environment-id`, `--on-work`, `--worker-id`,
    `--workdir`, `--max-idle`, `--log-format`, `--base-url`) is unchanged.
- **§0 / install snippets:** drop the prerelease Stainless URLs entirely —
  install the published packages: `pip install anthropic` / `npm i
  @anthropic-ai/sdk` for the SDKs, and the `ant` CLI from the GitHub release
  `v1.9.0` `.tar.gz` (the versions in the table above).

```diff
- ant worker dispatch \
+ ant beta:worker run \
    --session-id "sesn_..." \
-   --session-token "$SESSION_TOKEN" \
+   --environment-key "$ANTHROPIC_ENVIRONMENT_KEY" \
    --work-id "work_..." \
    --environment-id "env_..." \
-   --workdir "/workspace"
+   --workdir "/workspace" --unrestricted-paths
```

## Change 3 — The "Library usage" section

`anthropic.lib.runner` (Python) and `@anthropic-ai/sdk/helpers/beta/runner` (TS)
**no longer exist.** Three things changed: modules moved, symbols were renamed,
and the dispatcher was split in two.

### 3a. Module paths

| What | Python | TypeScript |
|---|---|---|
| The worker composition / poller / runner | `anthropic.lib.environments` | `@anthropic-ai/sdk/helpers/beta/environments` |
| Tool implementations + skill download | `anthropic.lib.tools.agent_toolset` | `@anthropic-ai/sdk/tools/agent-toolset/node` |

### 3b. Symbol renames

| Old | New (Python) | New (TypeScript) |
|---|---|---|
| `ToolEnv` | `AgentToolContext` | `AgentToolContext` |
| `default_tools` / `defaultTools` | `beta_agent_toolset_20260401` | `betaAgentToolset20260401` |
| `bash_tool`, `read_tool`, … | `beta_bash_tool`, `beta_read_tool`, … | `betaBashTool`, `betaReadTool`, … |
| `tool_dispatcher` / `toolDispatcher` | `tool_runner` | `toolRunner` |
| `decodeWorkSecret` | *(removed)* | *(removed)* |
| `service_key=` / `serviceKey:` | `environment_key=` | `environmentKey:` |

Also new in the released TS SDK: **`toolRunner` / `SessionToolRunner` take
`sessionId` positionally** — `toolRunner({ sessionId, tools })` →
`toolRunner(sessionId, { tools })`. And the per-call tool `run(args, context)`
context object (`BetaToolRunContext`) renamed its `toolUseBlock` field to
`toolUse` (`toolUseBlock` kept as a deprecated alias).

### 3c. The dispatcher split — `tool_dispatcher` → `SessionToolRunner` + `EnvironmentWorker`

The old `tool_dispatcher` / `toolDispatcher` took `work_id` + `environment_id` +
`session_token` and **owned the whole work-item lifecycle** — heartbeat,
reconcile, event stream, result posting, *and* the force-stop on exit.

That's now split:

- **`SessionToolRunner`** (`client.beta.sessions.events.tool_runner(...)` /
  `.toolRunner(...)`) is **dispatch-only**: event stream + tool execution +
  result posting. It takes `session_id` + `tools` (Python also accepts an
  optional `environment_key`; the TS `toolRunner` reads auth from the client) —
  **no `work_id`, no `environment_id`**. It does *not* heartbeat or force-stop.
- **`EnvironmentWorker`** is the full composition: poll → set up the workdir +
  download skills → run a `SessionToolRunner` while heartbeating the lease →
  force-stop on exit → loop. Build it with the factory
  **`client.beta.environments.work.worker(...)`** (now in **both** the Python
  and TS SDKs) or `EnvironmentWorker(...)` / `new EnvironmentWorker({...})`
  directly.

**For almost every reader, the upgrade is: replace the manual
`poller` + `tool_dispatcher` loop with `client.beta.environments.work.worker(...)`.**

### 3d. Rewrite the "Library usage" bullet list

- **`EnvironmentWorker`** (`client.beta.environments.work.worker(...)`) — the
  full composition: poll → workdir + skills → `SessionToolRunner` + heartbeat →
  force-stop → loop. `.run()` is the long-lived poll loop; `.handle_item()` /
  `.handleItem()` is the per-item flow (a webhook handler, `ant beta:worker poll
  --on-work`) — with no arguments it reads the `ANTHROPIC_*` env vars.
- **`client.beta.environments.work.poller(...)`** — control-plane only:
  long-polls, acks each item, yields the work item (`BetaSelfHostedWork`). No
  more `(work, secret)` / `{ work, secret }`. Argument `service_key` →
  `environment_key` / `environmentKey`.
- **`client.beta.sessions.events.tool_runner(...)` / `.toolRunner(...)`** —
  dispatch only; the work-item lifecycle (heartbeat, force-stop) is the
  caller's. TS: `toolRunner(sessionId, opts)` (positional `sessionId`).
- **`client.beta.webhooks.unwrap(...)`** — unchanged.

### 3e. Python example — before / after

```python
# BEFORE
import anyio, os
from anthropic import AsyncAnthropic
from anthropic.lib.runner import ToolEnv, default_tools

client = AsyncAnthropic()

async def main() -> None:
    async for work, secret in client.beta.environments.work.poller(
        environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
        service_key=os.environ["ANTHROPIC_ENV_KEY"],
    ):
        if work.data.type != "session":
            continue
        async with ToolEnv(workdir="/workspace") as env:
            async with client.beta.sessions.events.tool_dispatcher(
                session_id=work.data.id, work_id=work.id,
                environment_id=work.environment_id,
                session_token=secret.sessions_token,
                tools=default_tools(env),
            ) as calls:
                async for call in calls:
                    print(call.name)

anyio.run(main)
```

```python
# AFTER — the factory is the whole poll → skills → dispatch → heartbeat
# → force-stop → loop. The environment key is the only credential.
import asyncio, os
from anthropic import AsyncAnthropic

async def main() -> None:
    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    async with AsyncAnthropic(auth_token=environment_key) as client:
        await client.beta.environments.work.worker(
            environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
            environment_key=environment_key,
            workdir="/workspace",
        ).run()

asyncio.run(main())
```

If you genuinely need the lower-level dispatch loop, `tool_dispatcher` →
`tool_runner`, but it is now dispatch-only — you must heartbeat `work.id` while
it runs and `client.beta.environments.work.stop(..., force=True)` after.

### 3f. Python webhook example — before / after

```python
# BEFORE
client = anthropic.AsyncAnthropic(auth_token=os.environ["ANTHROPIC_ENV_KEY"])
async for work, secret in client.beta.environments.work.poller(
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
    service_key=os.environ["ANTHROPIC_ENV_KEY"],
    block_ms=None, reclaim_older_than_ms=2000, drain=True, auto_stop=False,
):
    if work.data.type != "session":
        continue
    spawned.append(spawn_sandbox(
        session_id=work.data.id, work_id=work.id,
        environment_id=work.environment_id,
        sessions_token=secret.sessions_token,
    ))
```

```python
# AFTER — one credential, poller yields just `work`
environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
client = anthropic.AsyncAnthropic(auth_token=environment_key)
async for work in client.beta.environments.work.poller(
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
    environment_key=environment_key,
    block_ms=None, reclaim_older_than_ms=2000, drain=True, auto_stop=False,
):
    if work.data.type != "session":
        continue
    spawned.append(spawn_sandbox(
        session_id=work.data.id, work_id=work.id,
        environment_id=work.environment_id,
        environment_key=environment_key,          # was sessions_token=secret.sessions_token
    ))
```

### 3g. TypeScript example — before / after

```ts
// BEFORE
import { defaultTools } from '@anthropic-ai/sdk/helpers/beta/runner';
for await (const { work, secret } of client.beta.environments.work.poller({
  environmentId: process.env.ANTHROPIC_ENVIRONMENT_ID!,
  serviceKey: process.env.ANTHROPIC_ENV_KEY!,
  signal: ctrl.signal,
})) {
  if (work.data.type !== 'session') continue;
  for await (const call of client.beta.sessions.events.toolDispatcher({
    sessionId: work.data.id, workId: work.id,
    environmentId: work.environment_id,
    sessionToken: secret.sessions_token,
    tools: defaultTools({ workdir: '/workspace' }),
    signal: ctrl.signal,
  })) { /* ... */ }
}
```

```ts
// AFTER — the factory composes the whole loop
import Anthropic from '@anthropic-ai/sdk';

const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
const client = new Anthropic({ authToken: environmentKey });
const ctrl = new AbortController();
process.once('SIGTERM', () => ctrl.abort());

await client.beta.environments.work
  .worker({
    environmentId: process.env.ANTHROPIC_ENVIRONMENT_ID!,
    environmentKey,
    workdir: '/workspace',
    signal: ctrl.signal,
  })
  .run();
```

If you keep the lower-level `toolRunner`, note the **positional `sessionId`**:
`toolRunner(work.data.id, { tools, signal })`.

### 3h. TypeScript webhook example — before / after

The manual `poll` → `ack` drain loop loses `decodeWorkSecret`, the `!work.secret`
guard, the per-call `Authorization` header, and the bogus
`x-environment-runner-version` poll param:

```ts
// BEFORE
import { decodeWorkSecret } from '@anthropic-ai/sdk/helpers/beta/runner';
const anthropic = new Anthropic({ authToken: env.ENVIRONMENT_SERVICE_KEY, ... });
const work = await anthropic.beta.environments.work.poll(env.ENVIRONMENT_ID, {
  'x-environment-runner-version': '0.1.0', reclaim_older_than_ms: 2000,
});
if (!work) break;
if (work.data.type !== 'session' || !work.secret) continue;
const secret = decodeWorkSecret(work.secret);
await anthropic.beta.environments.work.ack(
  work.id, { environment_id: env.ENVIRONMENT_ID },
  { headers: { Authorization: `Bearer ${secret.sessions_token}` } },
);
spawned.push(await spawnSandbox({ ..., sessionsToken: secret.sessions_token }));
```

```ts
// AFTER
const anthropic = new Anthropic({ authToken: env.ANTHROPIC_ENVIRONMENT_KEY, ... });
const work = await anthropic.beta.environments.work.poll(env.ANTHROPIC_ENVIRONMENT_ID, {
  reclaim_older_than_ms: 2000,
});
if (!work) break;
if (work.data.type !== 'session') continue;       // data is now Session | HealthCheck
// client is authed with the environment key — ack needs no per-call header
await anthropic.beta.environments.work.ack(work.id, {
  environment_id: env.ANTHROPIC_ENVIRONMENT_ID,
});
spawned.push(await spawnSandbox({ ..., environmentKey: env.ANTHROPIC_ENVIRONMENT_KEY }));
```

### 3i. Skills & custom tools

`ToolEnv` → `AgentToolContext`; `default_tools` → `beta_agent_toolset_20260401`
(Python) / `betaAgentToolset20260401` (TS); per-tool factories gain the `beta_` /
`beta` prefix; imports move to `anthropic.lib.tools.agent_toolset` /
`@anthropic-ai/sdk/tools/agent-toolset/node`. `EnvironmentWorker` downloads the
session's skills automatically, so the manual `AgentToolContext(client=…,
session_id=…)` pattern is only needed when you compose the runner by hand. In the skills
section, "authenticates with … `sessions_token`" → "authenticates with the
environment key"; the endpoint
(`GET /v1/skills/{id}/versions/{version}/content`) is unchanged.

---

## Unchanged — leave these alone

- The `anthropic-version` / `anthropic-beta: managed-agents-2026-04-01`
  prerequisite, and "the SDK helpers add the header automatically."
- `client.beta.environments.create(...)` (§1) — same signature.
- The idle-policy description (`--max-idle`, 60s after `end_turn` idle).
- `reclaim_older_than_ms`, `block_ms`, `drain`, `auto_stop` poller semantics.
- `client.beta.webhooks.unwrap(...)`.
