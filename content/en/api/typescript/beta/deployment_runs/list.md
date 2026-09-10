---
title: List Deployment Runs
url: https://platform.claude.com/docs/en/api/typescript/beta/deployment_runs/list
---

# List Deployment Runs

`client.beta.deploymentRuns.list(params?, options?): PageCursor<BetaManagedAgentsDeploymentRun>`

**GET** `/v1/deployment_runs`

List Deployment Runs

## Parameters

- `params: DeploymentRunListParams`

  - `"created_at[gt]"?: string`

    Query param: Return runs created strictly after this time (exclusive).

    format: date-time

  - `"created_at[gte]"?: string`

    Query param: Return runs created at or after this time (inclusive).

    format: date-time

  - `"created_at[lt]"?: string`

    Query param: Return runs created strictly before this time (exclusive).

    format: date-time

  - `"created_at[lte]"?: string`

    Query param: Return runs created at or before this time (inclusive).

    format: date-time

  - `deployment_id?: string`

    Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent `deployment_id` returns 200 with empty data.

  - `has_error?: boolean`

    Query param: Filter: true for runs with non-null `error`, false for runs with non-null `session_id`. Omit for all.

  - `limit?: number`

    Query param: Maximum results per page. Default 20, maximum 1000.

    format: int32

  - `page?: string`

    Query param: Opaque pagination cursor. Pass `next_page` from the previous response. Invalid or expired cursors return 400.

  - `trigger_type?: BetaManagedAgentsTriggerType`

    Query param: Filter runs by what triggered them. Omit to return all runs.

    - `"schedule"`

    - `"manual"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 42 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"user-profiles-2026-09-04"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

      - `"compact-2026-01-12"`

      - `"computer-use-2025-11-24"`

      - `"mcp-tunnels-2026-06-22"`

      - `"structured-outputs-2025-11-13"`

      - `"task-budgets-2026-03-13"`

      - `"thinking-display-updates-2026-08-18"`

      - `"ce-user-management-2026-07-13"`

      - `"mid-conversation-output-config-2026-07-01"`

      - `"thinking-binding-controls-2026-08-01"`

      - `"mid-conversation-system-clear-at-2026-08-21"`

  - `workspace_id?: string`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `type: "deployment_run"`

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `type: "agent"`

    - `id: string`

    - `version: number`

      format: int32

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more | null`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `type: "environment_archived_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `type: "agent_archived_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `type: "environment_not_found_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `type: "vault_not_found_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `type: "vault_archived_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `type: "file_not_found_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `type: "memory_store_archived_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `type: "skill_not_found_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `type: "session_resource_not_found_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `type: "workspace_archived_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `type: "organization_disabled_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `type: "session_rate_limited_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `type: "session_creation_rejected_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `type: "unknown_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: "self_hosted_resources_unsupported_error"`

      - `message: string`

        Human-readable error description.

    - `BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: "mcp_egress_blocked_error"`

      - `message: string`

        Human-readable error description.

  - `session_id: string | null`

    Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `type: "schedule"`

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsDeploymentRun of client.beta.deploymentRuns.list()) {
  console.log(betaManagedAgentsDeploymentRun.id);
}
```

### Response (200)

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
