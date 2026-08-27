# Get Deployment Run

**GET** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

## Path parameters

- `deployment_run_id: string`

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

## Returns

- `BetaManagedAgentsDeploymentRun object`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more or null`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `BetaManagedAgentsEnvironmentArchivedRunError object`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

    - `BetaManagedAgentsAgentArchivedRunError object`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

    - `BetaManagedAgentsEnvironmentNotFoundRunError object`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

    - `BetaManagedAgentsVaultNotFoundRunError object`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

    - `BetaManagedAgentsVaultArchivedRunError object`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

    - `BetaManagedAgentsFileNotFoundRunError object`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

    - `BetaManagedAgentsMemoryStoreArchivedRunError object`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

    - `BetaManagedAgentsSkillNotFoundRunError object`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

    - `BetaManagedAgentsSessionResourceNotFoundRunError object`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

    - `BetaManagedAgentsWorkspaceArchivedRunError object`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

    - `BetaManagedAgentsOrganizationDisabledRunError object`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

    - `BetaManagedAgentsSessionRateLimitedRunError object`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

    - `BetaManagedAgentsSessionCreationRejectedRunError object`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

    - `BetaManagedAgentsUnknownRunError object`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

    - `BetaManagedAgentsSelfHostedResourcesUnsupportedRunError object`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

    - `BetaManagedAgentsMCPEgressBlockedRunError object`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

  - `session_id: string or null`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `BetaManagedAgentsScheduleTriggerContext object`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "schedule"`

    - `BetaManagedAgentsManualTriggerContext object`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

  - `type: "deployment_run"`

## Example

```bash
curl https://api.anthropic.com/v1/deployment_runs/$DEPLOYMENT_RUN_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

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
