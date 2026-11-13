---
title: List Work Items
url: https://platform.claude.com/docs/en/api/typescript/beta/environments/work/list
---

# List Work Items

- Signature: `client.beta.environments.work.list(environmentID: string, params?: WorkListParams, options?: RequestOptions): PageCursor<BetaSelfHostedWork>`
- Endpoint: `GET /v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

## Example request

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

## Example response (200)

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

## Parameters

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

## Returns

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

## Types

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

interface BetaSessionWorkData {
  /** Type of work data */
  type: "session";
  /** Session identifier (e.g., 'session_...') */
  id: string;
}
```
