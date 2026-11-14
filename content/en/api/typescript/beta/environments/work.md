---
title: Work
url: https://platform.claude.com/docs/en/api/typescript/beta/environments/work
---

# Work

## Get Work Item

- Signature: `client.beta.environments.work.retrieve(workID: string, params: WorkRetrieveParams, options?: RequestOptions): BetaSelfHostedWork`
- Endpoint: `GET /v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWork = await client.beta.environments.work.retrieve("work_id", {
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW"
});

console.log(betaSelfHostedWork.id);
```

### Example response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

workID: string; // path parameter

interface WorkRetrieveParams {
  environment_id: string; // path parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** Work resource representing a unit of work in a self-hosted environment. Work items are queued when sessions are created or when long-dormant sessions receive new messages. The environment worker polls for work to execute in a self-hosted sandbox. */
interface BetaSelfHostedWork {
  /** The type of object (always 'work') */
  type: "work";
  /** Work identifier (e.g., 'work_...') */
  id: string;
  /** RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox */
  acknowledged_at: string | null;
  /** RFC 3339 timestamp when work was created */
  created_at: string;
  /** The actual work to be performed */
  data: BetaSessionWorkData;
  /** Environment identifier this work belongs to (e.g., `env_...`) */
  environment_id: string;
  /** RFC 3339 timestamp of the most recent heartbeat */
  latest_heartbeat_at: string | null;
  /** User-provided metadata key-value pairs associated with this work item */
  metadata: Record<string, string>;
  /** Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths. */
  secret: string | null;
  /** RFC 3339 timestamp when work execution started */
  started_at: string | null;
  /** Current state of the work item */
  state: "queued" | "starting" | "active" | "stopping" | "stopped";
  /** RFC 3339 timestamp when stop was requested */
  stop_requested_at: string | null;
  /** RFC 3339 timestamp when work execution stopped */
  stopped_at: string | null;
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

### Types

```ts
type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";

/** Work data for session work items. This resource type is used when work represents a session that needs to be executed in a self-hosted environment. */
interface BetaSessionWorkData {
  /** Type of work data */
  type: "session";
  /** Session identifier (e.g., 'session_...') */
  id: string;
}
```

## Poll for Work

- Signature: `client.beta.environments.work.poll(environmentID: string, params?: WorkPollParams, options?: RequestOptions): BetaSelfHostedWork | null`
- Endpoint: `GET /v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWork = await client.beta.environments.work.poll(
  "env_011CZkZ9X2dpNyB7HsEFoRfW"
);

console.log(betaSelfHostedWork);
```

### Example response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Parameters

```ts
environmentID: string; // path parameter

interface WorkPollParams {
  /** How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available). */
  block_ms?: number | null; // query parameter, minimum: 1
  /** Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms). */
  reclaim_older_than_ms?: number | null; // query parameter, minimum: 1
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console */
  "Anthropic-Worker-ID"?: string; // header parameter
}
```

## Acknowledge Work

- Signature: `client.beta.environments.work.ack(workID: string, params: WorkAckParams, options?: RequestOptions): BetaSelfHostedWork`
- Endpoint: `POST /v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWork = await client.beta.environments.work.ack("work_id", {
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW"
});

console.log(betaSelfHostedWork.id);
```

### Example response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Parameters

```ts
workID: string; // path parameter

interface WorkAckParams {
  environment_id: string; // path parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
}
```

## Record Heartbeat

- Signature: `client.beta.environments.work.heartbeat(workID: string, params: WorkHeartbeatParams, options?: RequestOptions): BetaSelfHostedWorkHeartbeatResponse`
- Endpoint: `POST /v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWorkHeartbeatResponse = await client.beta.environments.work.heartbeat(
  "work_id",
  { environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW" }
);

console.log(betaSelfHostedWorkHeartbeatResponse.last_heartbeat);
```

### Example response (200)

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

### Parameters

```ts
workID: string; // path parameter

interface WorkHeartbeatParams {
  environment_id: string; // path parameter
  /** Desired TTL in seconds */
  desired_ttl_seconds?: number | null; // query parameter
  /** Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match. The server does not compare the value when the work item is 'stopping' or 'stopped'. */
  expected_last_heartbeat?: string | null; // query parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
}
```

### Returns

```ts
/** Response after recording a heartbeat for a work item. */
interface BetaSelfHostedWorkHeartbeatResponse {
  /** The type of response */
  type: "work_heartbeat";
  /** RFC 3339 timestamp of the most recent heartbeat recorded for this work item, or an empty string if none has been recorded */
  last_heartbeat: string;
  /** Whether the heartbeat succeeded in extending the lease */
  lease_extended: boolean;
  /** Current state of the work item (active/stopping/stopped) */
  state: "queued" | "starting" | "active" | "stopping" | "stopped";
  /** Effective TTL applied to the lease */
  ttl_seconds: number;
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `BetaHeartbeatPreconditionFailedError` (HTTP status 412, error code `heartbeat_precondition_failed`)

  `expected_last_heartbeat` does not match the stored heartbeat, so another worker may hold the lease.

## Stop Work

- Signature: `client.beta.environments.work.stop(workID: string, params: WorkStopParams, options?: RequestOptions): BetaSelfHostedWork`
- Endpoint: `POST /v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWork = await client.beta.environments.work.stop("work_id", {
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW"
});

console.log(betaSelfHostedWork.id);
```

### Example response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Parameters

```ts
workID: string; // path parameter

interface WorkStopParams {
  environment_id: string; // path parameter
  /** If true, immediately stop work without graceful shutdown */
  force?: boolean;
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## List Work Items

- Signature: `client.beta.environments.work.list(environmentID: string, params?: WorkListParams, options?: RequestOptions): PageCursor<BetaSelfHostedWork>`
- Endpoint: `GET /v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaSelfHostedWork of client.beta.environments.work.list(
  "env_011CZkZ9X2dpNyB7HsEFoRfW"
)) {
  console.log(betaSelfHostedWork.id);
}
```

### Example response (200)

```json
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "secret": "secret",
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

### Parameters

```ts
environmentID: string; // path parameter

interface WorkListParams {
  /** Maximum number of work items to return */
  limit?: number; // query parameter, minimum: 1, maximum: 1000
  /** Opaque cursor from previous response for pagination */
  page?: string | null; // query parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
}
```

## Update Work Item

- Signature: `client.beta.environments.work.update(workID: string, params: WorkUpdateParams, options?: RequestOptions): BetaSelfHostedWork`
- Endpoint: `POST /v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWork = await client.beta.environments.work.update("work_id", {
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW",
  metadata: { foo: "string" }
});

console.log(betaSelfHostedWork.id);
```

### Example response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Parameters

```ts
workID: string; // path parameter

interface WorkUpdateParams {
  environment_id: string; // path parameter
  /** Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata. */
  metadata: Record<string, string | null>;
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `BetaInvalidMetadataError` (HTTP status 400, error code `invalid_metadata`)

  `metadata` has too many keys, a key or value that is too long, or a reserved key. The message names each problem.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Get Queue Statistics

- Signature: `client.beta.environments.work.stats(environmentID: string, params?: WorkStatsParams, options?: RequestOptions): BetaSelfHostedWorkQueueStats`
- Endpoint: `GET /v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaSelfHostedWorkQueueStats = await client.beta.environments.work.stats(
  "env_011CZkZ9X2dpNyB7HsEFoRfW"
);

console.log(betaSelfHostedWorkQueueStats.depth);
```

### Example response (200)

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```

### Parameters

```ts
environmentID: string; // path parameter

interface WorkStatsParams {
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** Statistics about the work queue for an environment. */
interface BetaSelfHostedWorkQueueStats {
  /** The type of object */
  type: "work_queue_stats";
  /** Number of work items waiting to be picked up */
  depth: number;
  /** RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty */
  oldest_queued_at: string | null;
  /** Number of work items being processed (polled but not acknowledged) */
  pending: number; // default: 0
  /** Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests. */
  workers_polling: number | null;
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Errors

### BetaHeartbeatPreconditionFailedError

HTTP status 412, error code `heartbeat_precondition_failed`

- `class BetaHeartbeatPreconditionFailedError extends PreconditionFailedError`

  `expected_last_heartbeat` does not match the stored heartbeat, so another worker may hold the lease.

  - `errorCode: "heartbeat_precondition_failed"`

  - `details: BetaHeartbeatPreconditionFailedErrorDetails`

    - `current_state: BetaWorkLeaseState`

      The lease as the server holds it.

      - `last_heartbeat: string | null`

        RFC 3339 timestamp of the stored heartbeat, or null if there has been none

      - `lease_extended: boolean`

        Always false: a refused heartbeat does not extend the lease

      - `state: "queued" | "starting" | "active" | 2 more`

        Current state of the work item

        - `"queued"`

        - `"starting"`

        - `"active"`

        - `"stopping"`

        - `"stopped"`

      - `ttl_seconds: number`

        TTL of the lease

    - `error_code: "heartbeat_precondition_failed"`

## Types

```ts
/** `expected_last_heartbeat` does not match the stored heartbeat, so another worker may hold the lease. */
interface BetaHeartbeatPreconditionFailedErrorDetails {
  /** The lease as the server holds it. */
  current_state: BetaWorkLeaseState;
  error_code: "heartbeat_precondition_failed";
}

/** Response when listing work items with cursor-based pagination. */
interface BetaSelfHostedWorkListResponse {
  /** List of work items */
  data: Array<BetaSelfHostedWork>;
  /** Opaque cursor for fetching the next page of results */
  next_page: string | null;
}

/** Request to stop a work item. */
interface BetaSelfHostedWorkStopRequest {
  /** If true, immediately stop work without graceful shutdown */
  force?: boolean; // default: false
}

/** Request to update work item metadata. */
interface BetaSelfHostedWorkUpdateRequest {
  /** Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata. */
  metadata: Record<string, string | null>;
}

/** A work item's lease as the server holds it. */
interface BetaWorkLeaseState {
  /** RFC 3339 timestamp of the stored heartbeat, or null if there has been none */
  last_heartbeat: string | null;
  /** Always false: a refused heartbeat does not extend the lease */
  lease_extended: boolean;
  /** Current state of the work item */
  state: "queued" | "starting" | "active" | "stopping" | "stopped";
  /** TTL of the lease */
  ttl_seconds: number;
}
```
