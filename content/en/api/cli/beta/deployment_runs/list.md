# List Deployment Runs

`$ ant beta:deployment-runs list`

**GET** `/v1/deployment_runs`

List Deployment Runs

## Parameters

- `--created-at-gt: optional string`

  Query param: Return runs created strictly after this time (exclusive).

  format: date-time

- `--created-at-gte: optional string`

  Query param: Return runs created at or after this time (inclusive).

  format: date-time

- `--created-at-lt: optional string`

  Query param: Return runs created strictly before this time (exclusive).

  format: date-time

- `--created-at-lte: optional string`

  Query param: Return runs created at or before this time (inclusive).

  format: date-time

- `--deployment-id: optional string`

  Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent `deployment_id` returns 200 with empty data.

- `--has-error: optional boolean`

  Query param: Filter: true for runs with non-null `error`, false for runs with non-null `session_id`. Omit for all.

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 1000.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor. Pass `next_page` from the previous response. Invalid or expired cursors return 400.

- `--trigger-type: optional "schedule" or "manual"`

  Query param: Filter runs by what triggered them. Omit to return all runs.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaManagedAgentsListDeploymentRunsData: object`

  Paginated list of deployment runs. Sorted by `created_at` descending (most recent first).

  - `data: array of BetaManagedAgentsDeploymentRun`

    List of deployment runs.

    - `id: string`

      Unique identifier for this run (`drun_...`).

    - `agent: object`

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

    - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

      Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

      - `beta_managed_agents_environment_archived_run_error: object`

        The deployment's environment was archived.

        - `message: string`

          Human-readable error description.

        - `type: "environment_archived_error"`

      - `beta_managed_agents_agent_archived_run_error: object`

        The deployment's agent was archived.

        - `message: string`

          Human-readable error description.

        - `type: "agent_archived_error"`

      - `beta_managed_agents_environment_not_found_run_error: object`

        The deployment's environment no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "environment_not_found_error"`

      - `beta_managed_agents_vault_not_found_run_error: object`

        A vault referenced by the deployment no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "vault_not_found_error"`

      - `beta_managed_agents_vault_archived_run_error: object`

        A vault referenced by the deployment is archived.

        - `message: string`

          Human-readable error description.

        - `type: "vault_archived_error"`

      - `beta_managed_agents_file_not_found_run_error: object`

        A file resource referenced by the deployment no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "file_not_found_error"`

      - `beta_managed_agents_memory_store_archived_run_error: object`

        A memory store referenced by the deployment is archived.

        - `message: string`

          Human-readable error description.

        - `type: "memory_store_archived_error"`

      - `beta_managed_agents_skill_not_found_run_error: object`

        A skill referenced by the deployment's agent no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "skill_not_found_error"`

      - `beta_managed_agents_session_resource_not_found_run_error: object`

        A referenced resource no longer exists and its kind was not reported.

        - `message: string`

          Human-readable error description.

        - `type: "session_resource_not_found_error"`

      - `beta_managed_agents_workspace_archived_run_error: object`

        The deployment's workspace was archived.

        - `message: string`

          Human-readable error description.

        - `type: "workspace_archived_error"`

      - `beta_managed_agents_organization_disabled_run_error: object`

        The deployment's organization is disabled.

        - `message: string`

          Human-readable error description.

        - `type: "organization_disabled_error"`

      - `beta_managed_agents_session_rate_limited_run_error: object`

        Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

        - `message: string`

          Human-readable error description.

        - `type: "session_rate_limited_error"`

      - `beta_managed_agents_session_creation_rejected_run_error: object`

        The session create request was rejected with a non-retryable validation error.

        - `message: string`

          Human-readable error description.

        - `type: "session_creation_rejected_error"`

      - `beta_managed_agents_unknown_run_error: object`

        An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

        - `message: string`

          Human-readable error description.

        - `type: "unknown_error"`

      - `beta_managed_agents_self_hosted_resources_unsupported_run_error: object`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `message: string`

          Human-readable error description.

        - `type: "self_hosted_resources_unsupported_error"`

      - `beta_managed_agents_mcp_egress_blocked_run_error: object`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `message: string`

          Human-readable error description.

        - `type: "mcp_egress_blocked_error"`

    - `session_id: string`

      Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null.

    - `trigger_context: BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

      Describes what triggered a deployment run, with trigger-specific metadata.

      - `beta_managed_agents_schedule_trigger_context: object`

        The run was fired by the deployment's cron schedule.

        - `scheduled_at: string`

          A timestamp in RFC 3339 format

          format: date-time

        - `type: "schedule"`

      - `beta_managed_agents_manual_trigger_context: object`

        The run was started manually by creating a session directly against the deployment.

        - `type: "manual"`

    - `type: "deployment_run"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

## Example

```bash
ant beta:deployment-runs list \
  --api-key my-anthropic-api-key
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
