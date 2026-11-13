---
title: Deployment Runs
url: https://platform.claude.com/docs/en/api/typescript/beta/deployment_runs
---

# Deployment Runs

## List Deployment Runs

- Signature: `client.beta.deploymentRuns.list(params?: DeploymentRunListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsDeploymentRun>`
- Endpoint: `GET /v1/deployment_runs`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsDeploymentRun of client.beta.deploymentRuns.list()) {
  console.log(betaManagedAgentsDeploymentRun.id);
}
```

### Example response (200)

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

interface DeploymentRunListParams {
  /** Return runs created strictly after this time (exclusive). */
  "created_at[gt]"?: string; // query parameter, format: date-time
  /** Return runs created at or after this time (inclusive). */
  "created_at[gte]"?: string; // query parameter, format: date-time
  /** Return runs created strictly before this time (exclusive). */
  "created_at[lt]"?: string; // query parameter, format: date-time
  /** Return runs created at or before this time (inclusive). */
  "created_at[lte]"?: string; // query parameter, format: date-time
  /** Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent `deployment_id` returns 200 with empty data. */
  deployment_id?: string; // query parameter
  /** Filter: true for runs with non-null `error`, false for runs with non-null `session_id`. Omit for all. */
  has_error?: boolean; // query parameter
  /** Maximum results per page. Default 20, maximum 1000. */
  limit?: number; // query parameter, format: int32
  /** Opaque pagination cursor. Pass `next_page` from the previous response. Invalid or expired cursors return 400. */
  page?: string; // query parameter
  /** Filter runs by what triggered them. Omit to return all runs. */
  trigger_type?: BetaManagedAgentsTriggerType; // query parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking. */
interface BetaManagedAgentsDeploymentRun {
  type: "deployment_run";
  /** Unique identifier for this run (`drun_...`). */
  id: string;
  /** Snapshot of the agent at fire time. Always fully resolved — deployments pin agent + version. */
  agent: BetaManagedAgentsAgentReference;
  /** Time this run record was persisted. */
  created_at: string; // format: date-time
  /** ID of the deployment that produced this run. */
  deployment_id: string;
  /** Populated on creation failure. Null on success. Exactly one of `session_id` or `error` is non-null. */
  error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | BetaManagedAgentsVaultNotFoundRunError | BetaManagedAgentsVaultArchivedRunError | BetaManagedAgentsFileNotFoundRunError | BetaManagedAgentsMemoryStoreArchivedRunError | BetaManagedAgentsSkillNotFoundRunError | BetaManagedAgentsSessionResourceNotFoundRunError | BetaManagedAgentsWorkspaceArchivedRunError | BetaManagedAgentsOrganizationDisabledRunError | BetaManagedAgentsSessionRateLimitedRunError | BetaManagedAgentsSessionCreationRejectedRunError | BetaManagedAgentsUnknownRunError | BetaManagedAgentsSelfHostedResourcesUnsupportedRunError | BetaManagedAgentsMCPEgressBlockedRunError | null;
  /** Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null. */
  session_id: string | null;
  /** What triggered this run and trigger-specific metadata. */
  trigger_context: BetaManagedAgentsTriggerContext;
}
```

### Types

```ts
/** What triggered a deployment run. */
type BetaManagedAgentsTriggerType =
  /** The run was fired by the deployment's cron schedule. */
  | "schedule"
  /** The run was started manually by creating a session directly against the deployment. */
  | "manual";

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

interface BetaManagedAgentsAgentReference {
  type: "agent";
  id: string;
  version: number; // format: int32
}

/** The deployment's environment was archived. */
interface BetaManagedAgentsEnvironmentArchivedRunError {
  type: "environment_archived_error";
  /** Human-readable error description. */
  message: string;
}

/** The deployment's agent was archived. */
interface BetaManagedAgentsAgentArchivedRunError {
  type: "agent_archived_error";
  /** Human-readable error description. */
  message: string;
}

/** The deployment's environment no longer exists. */
interface BetaManagedAgentsEnvironmentNotFoundRunError {
  type: "environment_not_found_error";
  /** Human-readable error description. */
  message: string;
}

/** A vault referenced by the deployment no longer exists. */
interface BetaManagedAgentsVaultNotFoundRunError {
  type: "vault_not_found_error";
  /** Human-readable error description. */
  message: string;
}

/** A vault referenced by the deployment is archived. */
interface BetaManagedAgentsVaultArchivedRunError {
  type: "vault_archived_error";
  /** Human-readable error description. */
  message: string;
}

/** A file resource referenced by the deployment no longer exists. */
interface BetaManagedAgentsFileNotFoundRunError {
  type: "file_not_found_error";
  /** Human-readable error description. */
  message: string;
}

/** A memory store referenced by the deployment is archived. */
interface BetaManagedAgentsMemoryStoreArchivedRunError {
  type: "memory_store_archived_error";
  /** Human-readable error description. */
  message: string;
}

/** A skill referenced by the deployment's agent no longer exists. */
interface BetaManagedAgentsSkillNotFoundRunError {
  type: "skill_not_found_error";
  /** Human-readable error description. */
  message: string;
}

/** A referenced resource no longer exists and its kind was not reported. */
interface BetaManagedAgentsSessionResourceNotFoundRunError {
  type: "session_resource_not_found_error";
  /** Human-readable error description. */
  message: string;
}

/** The deployment's workspace was archived. */
interface BetaManagedAgentsWorkspaceArchivedRunError {
  type: "workspace_archived_error";
  /** Human-readable error description. */
  message: string;
}

/** The deployment's organization is disabled. */
interface BetaManagedAgentsOrganizationDisabledRunError {
  type: "organization_disabled_error";
  /** Human-readable error description. */
  message: string;
}

/** Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed. */
interface BetaManagedAgentsSessionRateLimitedRunError {
  type: "session_rate_limited_error";
  /** Human-readable error description. */
  message: string;
}

/** The session create request was rejected with a non-retryable validation error. */
interface BetaManagedAgentsSessionCreationRejectedRunError {
  type: "session_creation_rejected_error";
  /** Human-readable error description. */
  message: string;
}

/** An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone. */
interface BetaManagedAgentsUnknownRunError {
  type: "unknown_error";
  /** Human-readable error description. */
  message: string;
}

/** The deployment configures resources, but its environment is self-hosted and cannot mount them. */
interface BetaManagedAgentsSelfHostedResourcesUnsupportedRunError {
  type: "self_hosted_resources_unsupported_error";
  /** Human-readable error description. */
  message: string;
}

/** An MCP server host used by the deployment's agent is blocked by the environment's network policy. */
interface BetaManagedAgentsMCPEgressBlockedRunError {
  type: "mcp_egress_blocked_error";
  /** Human-readable error description. */
  message: string;
}

/** Describes what triggered a deployment run, with trigger-specific metadata. */
type BetaManagedAgentsTriggerContext = BetaManagedAgentsScheduleTriggerContext | BetaManagedAgentsManualTriggerContext;

/** The run was fired by the deployment's cron schedule. */
interface BetaManagedAgentsScheduleTriggerContext {
  type: "schedule";
  /** The UTC instant at which the cron expression matched in the configured timezone, before jitter is applied. At most one run is recorded per (`deployment_id`, `scheduled_at`) pair. */
  scheduled_at: string; // format: date-time
}

/** The run was started manually by creating a session directly against the deployment. */
interface BetaManagedAgentsManualTriggerContext {
  type: "manual";
}
```

## Get Deployment Run

- Signature: `client.beta.deploymentRuns.retrieve(deploymentRunID: string, params?: DeploymentRunRetrieveParams, options?: RequestOptions): BetaManagedAgentsDeploymentRun`
- Endpoint: `GET /v1/deployment_runs/{deployment_run_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeploymentRun = await client.beta.deploymentRuns.retrieve(
  "deployment_run_id"
);

console.log(betaManagedAgentsDeploymentRun.id);
```

### Example response (200)

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

### Parameters

```ts
/** Unique identifier of the deployment run. */
deploymentRunID: string; // path parameter

interface DeploymentRunRetrieveParams {
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```
