# Deployments

## Create Deployment

`$ ant beta:deployments create`

**POST** `/v1/deployments`

Create Deployment

### Parameters

- `--agent: string or BetaManagedAgentsAgentParams`

  Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

- `--environment-id: string`

  Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

  minLength: 1, maxLength: 128

- `--initial-event: array of BetaManagedAgentsDeploymentInitialEventParams`

  Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

- `--name: string`

  Body param: Human-readable name for the deployment.

  minLength: 1, maxLength: 256

- `--budget: optional object`

  Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `--description: optional string`

  Body param: Description of what the deployment does.

  maxLength: 2048

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--resource: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

- `--schedule: optional object`

  Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `--vault-id: optional array of string`

  Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Example

```bash
ant beta:deployments create \
  --api-key my-anthropic-api-key \
  --agent string \
  --environment-id x \
  --initial-event '{content: [{text: '\''Where is my order #1234?'\'', type: text}], type: user.message}' \
  --name x
```

#### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## List Deployments

`$ ant beta:deployments list`

**GET** `/v1/deployments`

List Deployments

### Parameters

- `--agent-id: optional string`

  Query param: Filter by agent ID.

- `--created-at-gte: optional string`

  Query param: Return deployments created at or after this time (inclusive).

  format: date-time

- `--created-at-lte: optional string`

  Query param: Return deployments created at or before this time (inclusive).

  format: date-time

- `--include-archived: optional boolean`

  Query param: When true, includes archived deployments. Default: false (exclude archived).

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor.

- `--status: optional "active" or "paused"`

  Query param: Filter by status: `active` or `paused`. Omit for both. To include archived deployments, use `include_archived` instead; the two cannot be combined.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListDeploymentsData: object`

  Paginated list of deployments.

  - `data: array of BetaManagedAgentsDeployment`

    List of deployments.

    - `id: string`

      Unique identifier for this deployment.

    - `agent: object`

      A resolved agent reference with a concrete version.

      - `id: string`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      Description of what the deployment does.

    - `environment_id: string`

      ID of the `environment` where sessions run.

    - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

      Events sent to each session immediately after creation.

      - `beta_managed_agents_deployment_user_message_event: object`

        A user message sent to the session.

        - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

          Array of content blocks for the user message.

          - `beta_managed_agents_text_block: object`

            Regular text content.

            - `text: string`

              The text content.

              minLength: 1

            - `type: "text"`

          - `beta_managed_agents_image_block: object`

            Image content specified directly as base64 data or as a reference via a URL.

            - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

              Union type for image source variants.

              - `beta_managed_agents_base64_image_source: object`

                Base64-encoded image data.

                - `data: string`

                  Base64-encoded image data.

                  minLength: 1

                - `media_type: string`

                  MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                  minLength: 1

                - `type: "base64"`

              - `beta_managed_agents_url_image_source: object`

                Image referenced by URL.

                - `type: "url"`

                - `url: string`

                  URL of the image to fetch.

                  minLength: 1

              - `beta_managed_agents_file_image_source: object`

                Image referenced by file ID.

                - `file_id: string`

                  ID of a previously uploaded file.

                  minLength: 1

                - `type: "file"`

            - `type: "image"`

          - `beta_managed_agents_document_block: object`

            Document content, either specified directly as base64 data, as text, or as a reference via a URL.

            - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

              Union type for document source variants.

              - `beta_managed_agents_base64_document_source: object`

                Base64-encoded document data.

                - `data: string`

                  Base64-encoded document data.

                  minLength: 1

                - `media_type: string`

                  MIME type of the document (e.g., "application/pdf").

                  minLength: 1

                - `type: "base64"`

              - `beta_managed_agents_plain_text_document_source: object`

                Plain text document content.

                - `data: string`

                  The plain text content.

                  minLength: 1

                - `media_type: "text/plain"`

                  MIME type of the text content. Must be "text/plain".

                - `type: "text"`

              - `beta_managed_agents_url_document_source: object`

                Document referenced by URL.

                - `type: "url"`

                - `url: string`

                  URL of the document to fetch.

                  minLength: 1

              - `beta_managed_agents_file_document_source: object`

                Document referenced by file ID.

                - `file_id: string`

                  ID of a previously uploaded file.

                  minLength: 1

                - `type: "file"`

            - `type: "document"`

            - `context: optional string`

              Additional context about the document for the model.

            - `title: optional string`

              The title of the document.

          - `beta_managed_agents_redacted_block: object`

            Placeholder for content withheld by Anthropic model policy.

            - `type: "redacted"`

        - `type: "user.message"`

      - `beta_managed_agents_deployment_user_define_outcome_event: object`

        An outcome the agent should work toward. The agent begins work on receipt.

        - `description: string`

          What the agent should produce. This is the task specification.

        - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

          Rubric for grading the quality of an outcome.

          - `beta_managed_agents_file_rubric: object`

            Rubric referenced by a file uploaded via the Files API.

            - `file_id: string`

              ID of the rubric file.

            - `type: "file"`

          - `beta_managed_agents_text_rubric: object`

            Rubric content provided inline as text.

            - `content: string`

              Rubric content. Plain text or markdown — the grader treats it as freeform text.

            - `type: "text"`

        - `type: "user.define_outcome"`

        - `max_iterations: optional number`

          Eval→revision cycles before giving up. Default 3, max 20.

          format: int32

      - `beta_managed_agents_deployment_system_message_event: object`

        Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

        - `content: array of BetaManagedAgentsSystemContentBlock`

          System content blocks to append. Text-only.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `type: "system.message"`

    - `metadata: map[string]`

      Arbitrary key-value metadata. Maximum 16 pairs.

    - `name: string`

      Human-readable name.

    - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

      Why a deployment is paused. Non-null exactly when `status` is `paused`.

      - `beta_managed_agents_manual_deployment_paused_reason: object`

        The caller invoked the pause endpoint on the deployment.

        - `type: "manual"`

      - `beta_managed_agents_error_deployment_paused_reason: object`

        A scheduled fire recorded a failed run whose error auto-pauses the deployment.

        - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

          The error that triggered an auto-pause. Matches the failed run's `error.type`.

          - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

            The deployment's environment was archived.

            - `type: "environment_archived_error"`

          - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

            The deployment's agent was archived.

            - `type: "agent_archived_error"`

          - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

            The deployment's environment no longer exists.

            - `type: "environment_not_found_error"`

          - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

            A vault referenced by the deployment no longer exists.

            - `type: "vault_not_found_error"`

          - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

            A file resource referenced by the deployment no longer exists.

            - `type: "file_not_found_error"`

          - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

            A referenced resource no longer exists and its kind was not reported.

            - `type: "session_resource_not_found_error"`

          - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

            The deployment's workspace was archived.

            - `type: "workspace_archived_error"`

          - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

            The deployment's organization is disabled.

            - `type: "organization_disabled_error"`

          - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

            A memory store referenced by the deployment is archived.

            - `type: "memory_store_archived_error"`

          - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

            A skill referenced by the deployment's agent no longer exists.

            - `type: "skill_not_found_error"`

          - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

            A vault referenced by the deployment is archived.

            - `type: "vault_archived_error"`

          - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

            An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

            - `type: "unknown_error"`

          - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

            The deployment configures resources, but its environment is self-hosted and cannot mount them.

            - `type: "self_hosted_resources_unsupported_error"`

          - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

            An MCP server host used by the deployment's agent is blocked by the environment's network policy.

            - `type: "mcp_egress_blocked_error"`

        - `type: "error"`

    - `resources: array of BetaManagedAgentsSessionResourceConfig`

      Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

      - `beta_managed_agents_github_repository_resource_config: object`

        A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

        - `type: "github_repository"`

        - `url: string`

          Github URL of the repository

        - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

          Branch or commit to check out. Defaults to the repository's default branch.

          - `beta_managed_agents_branch_checkout: object`

            - `name: string`

              Branch name to check out.

              minLength: 1, maxLength: 255

            - `type: "branch"`

          - `beta_managed_agents_commit_checkout: object`

            - `sha: string`

              Full commit SHA to check out.

              minLength: 7, maxLength: 64

            - `type: "commit"`

        - `mount_path: optional string`

          Mount path in the container. Defaults to `/workspace/<repo-name>`.

      - `beta_managed_agents_file_resource_config: object`

        A file mounted into each session's container.

        - `file_id: string`

          ID of a previously uploaded file.

        - `type: "file"`

        - `mount_path: optional string`

          Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      - `beta_managed_agents_memory_store_resource_config: object`

        A memory store attached to each session created from this deployment.

        - `memory_store_id: string`

          The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

        - `type: "memory_store"`

        - `access: optional "read_write" or "read_only"`

          Access mode for an attached memory store.

          - `"read_write"`

          - `"read_only"`

        - `instructions: optional string`

          Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `schedule: object`

      5-field POSIX cron schedule with computed runtime timestamps.

      - `expression: string`

        5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

        minLength: 1, maxLength: 256

      - `timezone: string`

        IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

        minLength: 1

      - `type: "cron"`

      - `last_run_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `upcoming_runs_at: optional array of string`

        Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

    - `status: "active" or "paused"`

      Lifecycle status of a deployment.

      - `"active"`

      - `"paused"`

    - `type: "deployment"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `vault_ids: array of string`

      Vault IDs supplying stored credentials for sessions created from this deployment.

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```bash
ant beta:deployments list \
  --api-key my-anthropic-api-key
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`$ ant beta:deployments retrieve`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Example

```bash
ant beta:deployments retrieve \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
```

#### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Update Deployment

`$ ant beta:deployments update`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `--deployment-id: string`

  Path param: Path parameter deployment_id

- `--agent: optional string or BetaManagedAgentsAgentParams`

  Body param: Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

- `--budget: optional object`

  Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `--description: optional string`

  Body param: Description. Omit to preserve; send empty string or null to clear.

  maxLength: 2048

- `--environment-id: optional string`

  Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  maxLength: 128

- `--initial-event: optional array of BetaManagedAgentsDeploymentInitialEventParams`

  Body param: Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--name: optional string`

  Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  maxLength: 256

- `--resource: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

- `--schedule: optional object`

  Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `--vault-id: optional array of string`

  Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Example

```bash
ant beta:deployments update \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
```

#### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Archive Deployment

`$ ant beta:deployments archive`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Example

```bash
ant beta:deployments archive \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
```

#### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Run Deployment Now

`$ ant beta:deployments run`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment_run: object`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

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

### Example

```bash
ant beta:deployments run \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
```

#### Response (200)

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

## Pause Deployment

`$ ant beta:deployments pause`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Example

```bash
ant beta:deployments pause \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
```

#### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Unpause Deployment

`$ ant beta:deployments unpause`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Example

```bash
ant beta:deployments unpause \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
```

#### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Domain types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

  The deployment's agent was archived.

  - `type: "agent_archived_error"`

### Beta Managed Agents Cron Schedule

- `beta_managed_agents_cron_schedule: object`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    minLength: 1

  - `type: "cron"`

  - `last_run_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `upcoming_runs_at: optional array of string`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `beta_managed_agents_cron_schedule_params: object`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

  - `type: "cron"`

### Beta Managed Agents Deployment

- `beta_managed_agents_deployment: object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `beta_managed_agents_deployment_system_message_event: object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

      - `type: "error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: "cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Beta Managed Agents Deployment Initial Event

- `beta_managed_agents_deployment_initial_event: BetaManagedAgentsDeploymentUserMessageEvent or BetaManagedAgentsDeploymentUserDefineOutcomeEvent or BetaManagedAgentsDeploymentSystemMessageEvent`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `beta_managed_agents_deployment_user_message_event: object`

    A user message sent to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

  - `beta_managed_agents_deployment_user_define_outcome_event: object`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric: object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `beta_managed_agents_text_rubric: object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `beta_managed_agents_deployment_system_message_event: object`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `beta_managed_agents_deployment_initial_event_params: BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserDefineOutcomeEventParams or BetaManagedAgentsSystemMessageEventParams`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `beta_managed_agents_user_message_event_params: object`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

  - `beta_managed_agents_user_define_outcome_event_params: object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric_params: object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `beta_managed_agents_text_rubric_params: object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `type: "text"`

    - `type: "user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `beta_managed_agents_system_message_event_params: object`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

### Beta Managed Agents Deployment Paused Reason

- `beta_managed_agents_deployment_paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `beta_managed_agents_manual_deployment_paused_reason: object`

    The caller invoked the pause endpoint on the deployment.

    - `type: "manual"`

  - `beta_managed_agents_error_deployment_paused_reason: object`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

        The deployment's environment was archived.

        - `type: "environment_archived_error"`

      - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

        The deployment's agent was archived.

        - `type: "agent_archived_error"`

      - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

        The deployment's environment no longer exists.

        - `type: "environment_not_found_error"`

      - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

        A vault referenced by the deployment no longer exists.

        - `type: "vault_not_found_error"`

      - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

        A file resource referenced by the deployment no longer exists.

        - `type: "file_not_found_error"`

      - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

        A referenced resource no longer exists and its kind was not reported.

        - `type: "session_resource_not_found_error"`

      - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

        The deployment's workspace was archived.

        - `type: "workspace_archived_error"`

      - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

        The deployment's organization is disabled.

        - `type: "organization_disabled_error"`

      - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

        A memory store referenced by the deployment is archived.

        - `type: "memory_store_archived_error"`

      - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

        A skill referenced by the deployment's agent no longer exists.

        - `type: "skill_not_found_error"`

      - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

        A vault referenced by the deployment is archived.

        - `type: "vault_archived_error"`

      - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: "unknown_error"`

      - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: "self_hosted_resources_unsupported_error"`

      - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: "mcp_egress_blocked_error"`

    - `type: "error"`

### Beta Managed Agents Deployment Paused Reason Error

- `beta_managed_agents_deployment_paused_reason_error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

    The deployment's environment was archived.

    - `type: "environment_archived_error"`

  - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

    The deployment's agent was archived.

    - `type: "agent_archived_error"`

  - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

    The deployment's environment no longer exists.

    - `type: "environment_not_found_error"`

  - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

    A vault referenced by the deployment no longer exists.

    - `type: "vault_not_found_error"`

  - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

    A file resource referenced by the deployment no longer exists.

    - `type: "file_not_found_error"`

  - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

    A referenced resource no longer exists and its kind was not reported.

    - `type: "session_resource_not_found_error"`

  - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

    The deployment's workspace was archived.

    - `type: "workspace_archived_error"`

  - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

    The deployment's organization is disabled.

    - `type: "organization_disabled_error"`

  - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

    A memory store referenced by the deployment is archived.

    - `type: "memory_store_archived_error"`

  - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

    A skill referenced by the deployment's agent no longer exists.

    - `type: "skill_not_found_error"`

  - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

    A vault referenced by the deployment is archived.

    - `type: "vault_archived_error"`

  - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: "unknown_error"`

  - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: "self_hosted_resources_unsupported_error"`

  - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: "mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `beta_managed_agents_deployment_status: "active" or "paused"`

  Lifecycle status of a deployment.

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `beta_managed_agents_deployment_system_message_event: object`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `content: array of BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `text: string`

      The text content.

      minLength: 1

    - `type: "text"`

  - `type: "system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `beta_managed_agents_deployment_user_define_outcome_event: object`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `description: string`

    What the agent should produce. This is the task specification.

  - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

    Rubric for grading the quality of an outcome.

    - `beta_managed_agents_file_rubric: object`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: string`

        ID of the rubric file.

      - `type: "file"`

    - `beta_managed_agents_text_rubric: object`

      Rubric content provided inline as text.

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: "text"`

  - `type: "user.define_outcome"`

  - `max_iterations: optional number`

    Eval→revision cycles before giving up. Default 3, max 20.

    format: int32

### Beta Managed Agents Deployment User Message Event

- `beta_managed_agents_deployment_user_message_event: object`

  A user message sent to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Array of content blocks for the user message.

    - `beta_managed_agents_text_block: object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `beta_managed_agents_image_block: object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `beta_managed_agents_url_image_source: object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `beta_managed_agents_file_image_source: object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `beta_managed_agents_document_block: object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `beta_managed_agents_plain_text_document_source: object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `beta_managed_agents_url_document_source: object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `beta_managed_agents_file_document_source: object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

    - `beta_managed_agents_redacted_block: object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `type: "user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

  The deployment's environment was archived.

  - `type: "environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

  The deployment's environment no longer exists.

  - `type: "environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `beta_managed_agents_error_deployment_paused_reason: object`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object`

      The deployment's environment was archived.

      - `type: "environment_archived_error"`

    - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object`

      The deployment's agent was archived.

      - `type: "agent_archived_error"`

    - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object`

      The deployment's environment no longer exists.

      - `type: "environment_not_found_error"`

    - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

      A vault referenced by the deployment no longer exists.

      - `type: "vault_not_found_error"`

    - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

      A file resource referenced by the deployment no longer exists.

      - `type: "file_not_found_error"`

    - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

      A referenced resource no longer exists and its kind was not reported.

      - `type: "session_resource_not_found_error"`

    - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

      The deployment's workspace was archived.

      - `type: "workspace_archived_error"`

    - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

      The deployment's organization is disabled.

      - `type: "organization_disabled_error"`

    - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

      A memory store referenced by the deployment is archived.

      - `type: "memory_store_archived_error"`

    - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

      A skill referenced by the deployment's agent no longer exists.

      - `type: "skill_not_found_error"`

    - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

      A vault referenced by the deployment is archived.

      - `type: "vault_archived_error"`

    - `beta_managed_agents_unknown_deployment_paused_reason_error: object`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: "unknown_error"`

    - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: "self_hosted_resources_unsupported_error"`

    - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: "mcp_egress_blocked_error"`

  - `type: "error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `beta_managed_agents_file_not_found_deployment_paused_reason_error: object`

  A file resource referenced by the deployment no longer exists.

  - `type: "file_not_found_error"`

### Beta Managed Agents File Resource Config

- `beta_managed_agents_file_resource_config: object`

  A file mounted into each session's container.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `beta_managed_agents_github_repository_resource_config: object`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: "github_repository"`

  - `url: string`

    Github URL of the repository

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `beta_managed_agents_branch_checkout: object`

      - `name: string`

        Branch name to check out.

        minLength: 1, maxLength: 255

      - `type: "branch"`

    - `beta_managed_agents_commit_checkout: object`

      - `sha: string`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

      - `type: "commit"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `beta_managed_agents_manual_deployment_paused_reason: object`

  The caller invoked the pause endpoint on the deployment.

  - `type: "manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: "mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object`

  A memory store referenced by the deployment is archived.

  - `type: "memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `beta_managed_agents_memory_store_resource_config: object`

  A memory store attached to each session created from this deployment.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object`

  The deployment's organization is disabled.

  - `type: "organization_disabled_error"`

### Beta Managed Agents Schedule

- `beta_managed_agents_schedule: object`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    minLength: 1

  - `type: "cron"`

  - `last_run_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `upcoming_runs_at: optional array of string`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `beta_managed_agents_schedule_params: object`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

  - `type: "cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: "self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `beta_managed_agents_session_resource_config: BetaManagedAgentsGitHubRepositoryResourceConfig or BetaManagedAgentsFileResourceConfig or BetaManagedAgentsMemoryStoreResourceConfig`

  A configured session resource. Echoes the input minus write-only credentials.

  - `beta_managed_agents_github_repository_resource_config: object`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: "github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `beta_managed_agents_branch_checkout: object`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: "branch"`

      - `beta_managed_agents_commit_checkout: object`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: "commit"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `beta_managed_agents_file_resource_config: object`

    A file mounted into each session's container.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `beta_managed_agents_memory_store_resource_config: object`

    A memory store attached to each session created from this deployment.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object`

  A referenced resource no longer exists and its kind was not reported.

  - `type: "session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object`

  A skill referenced by the deployment's agent no longer exists.

  - `type: "skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `beta_managed_agents_unknown_deployment_paused_reason_error: object`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: "unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `beta_managed_agents_vault_archived_deployment_paused_reason_error: object`

  A vault referenced by the deployment is archived.

  - `type: "vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object`

  A vault referenced by the deployment no longer exists.

  - `type: "vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object`

  The deployment's workspace was archived.

  - `type: "workspace_archived_error"`
