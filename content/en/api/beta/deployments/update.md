---
title: Update Deployment
url: https://platform.claude.com/docs/en/api/beta/deployments/update
---

# Update Deployment

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

## Path parameters

- `deployment_id: string`

  Unique identifier of the deployment to update.

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more`

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

    - `"compact-2026-09-04"`

    - `"inline-tools-2026-09-15"`

    - `"mcp-client-2026-09-15"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Body parameters

- `agent: optional string or BetaManagedAgentsAgentParams`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

  - `string`

  - `BetaManagedAgentsAgentParams object`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `type: "agent"`

    - `id: string`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

- `budget: optional BetaManagedAgentsBudgetLimit or null`

  Spend ceiling for future sessions. Full replacement. Omit to preserve; send null to clear (sessions created afterwards are uncapped). The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way.

  - `type: "limit"`

  - `max_list_cost: BetaMonetaryAmount`

    Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

- `description: optional string or null`

  Description. Omit to preserve; send empty string or null to clear.

  maxLength: 2048

- `environment_id: optional string`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  maxLength: 128

- `initial_events: optional array of BetaManagedAgentsDeploymentInitialEventParams`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

  - `BetaManagedAgentsUserMessageEventParams object`

    Parameters for sending a user message to the session.

    - `type: "user.message"`

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

  - `BetaManagedAgentsUserDefineOutcomeEventParams object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: "user.define_outcome"`

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      How to grade the outcome. Text or file reference.

      - `BetaManagedAgentsFileRubricParams object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubricParams object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: optional number or null`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `BetaManagedAgentsSystemMessageEventParams object`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `type: "system.message"`

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

- `metadata: optional map[string] or null`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: optional string`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  maxLength: 256

- `resources: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam or null`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

  - `BetaManagedAgentsGitHubRepositoryResourceParams object`

    Mount a GitHub repository into the session's container.

    - `type: "github_repository"`

    - `url: string`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `authorization_token: optional string`

      GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

      minLength: 1, maxLength: 4096

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout or null`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `BetaManagedAgentsBranchCheckout object`

        - `type: "branch"`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `BetaManagedAgentsCommitCheckout object`

        - `type: "commit"`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

    - `mount_path: optional string or null`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `BetaManagedAgentsFileResourceParams object`

    Mount a file uploaded via the Files API into the session.

    - `type: "file"`

    - `file_id: string`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `mount_path: optional string or null`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `BetaManagedAgentsMemoryStoreResourceParam object`

    Parameters for attaching a memory store to an agent session.

    - `type: "memory_store"`

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: optional "read_write" or "read_only" or null`

      Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string or null`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `schedule: optional BetaManagedAgentsScheduleParams or null`

  Cron schedule. Full replacement. Omit to preserve; send null to clear (revert to manual-only).

  - `type: "cron"`

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

- `vault_ids: optional array of string or null`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

## Returns

- `BetaManagedAgentsDeployment object`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: "deployment"`

  - `id: string`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: "agent"`

    - `id: string`

    - `version: number`

      format: int32

  - `archived_at: string or null`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    Time the deployment was created.

    format: date-time

  - `description: string or null`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `BetaManagedAgentsDeploymentUserMessageEvent object`

      A user message sent to the session.

      - `type: "user.message"`

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks for the user message.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: "image"`

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            The source of the image data.

            - `BetaManagedAgentsBase64ImageSource object`

              Base64-encoded image data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `BetaManagedAgentsURLImageSource object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `BetaManagedAgentsFileImageSource object`

              Image referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: "document"`

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            The source of the document data.

            - `BetaManagedAgentsBase64DocumentSource object`

              Base64-encoded document data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `BetaManagedAgentsPlainTextDocumentSource object`

              Plain text document content.

              - `type: "text"`

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

            - `BetaManagedAgentsURLDocumentSource object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `BetaManagedAgentsFileDocumentSource object`

              Document referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

          - `context: optional string or null`

            Additional context about the document for the model.

          - `title: optional string or null`

            The title of the document.

        - `BetaManagedAgentsRedactedBlock object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

    - `BetaManagedAgentsDeploymentUserDefineOutcomeEvent object`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: "user.define_outcome"`

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        How to grade the outcome. Text or file reference.

        - `BetaManagedAgentsFileRubric object`

          Rubric referenced by a file uploaded via the Files API.

          - `type: "file"`

          - `file_id: string`

            ID of the rubric file.

        - `BetaManagedAgentsTextRubric object`

          Rubric content provided inline as text.

          - `type: "text"`

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: optional number or null`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `BetaManagedAgentsDeploymentSystemMessageEvent object`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: "system.message"`

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason or null`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `BetaManagedAgentsManualDeploymentPausedReason object`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

    - `BetaManagedAgentsErrorDeploymentPausedReason object`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: "error"`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError object`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

        - `BetaManagedAgentsAgentArchivedDeploymentPausedReasonError object`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

        - `BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError object`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

        - `BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError object`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

        - `BetaManagedAgentsFileNotFoundDeploymentPausedReasonError object`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

        - `BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError object`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

        - `BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError object`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

        - `BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError object`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

        - `BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError object`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

        - `BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError object`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

        - `BetaManagedAgentsVaultArchivedDeploymentPausedReasonError object`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

        - `BetaManagedAgentsUnknownDeploymentPausedReasonError object`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

        - `BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError object`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

        - `BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError object`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `BetaManagedAgentsGitHubRepositoryResourceConfig object`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout or null`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `BetaManagedAgentsBranchCheckout object`

          - `type: "branch"`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `BetaManagedAgentsCommitCheckout object`

          - `type: "commit"`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: optional string or null`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `BetaManagedAgentsFileResourceConfig object`

      A file mounted into each session's container.

      - `type: "file"`

      - `file_id: string`

        ID of a previously uploaded file.

      - `mount_path: optional string or null`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `BetaManagedAgentsMemoryStoreResourceConfig object`

      A memory store attached to each session created from this deployment.

      - `type: "memory_store"`

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: optional "read_write" or "read_only" or null`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string or null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule or null`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: "cron"`

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: optional string or null`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: string`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: optional BetaManagedAgentsBudgetLimit or null`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: "limit"`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

## Example

```bash
curl https://api.anthropic.com/v1/deployments/$DEPLOYMENT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "schedule": {
            "expression": "0 9 * * 1-5",
            "timezone": "America/Los_Angeles",
            "type": "cron"
          }
        }'
```

### Response (200)

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
