---
title: Deployments
url: https://platform.claude.com/docs/en/api/python/beta/deployments
---

# Deployments

## Create Deployment

`beta.deployments.create(**kwargs)  -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments`

Create Deployment

### Parameters

- `agent: Agent`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

  - `str`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `type: Literal["agent"]`

    - `id: str`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

- `environment_id: str`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

  minLength: 1, maxLength: 128

- `initial_events: Iterable[BetaManagedAgentsDeploymentInitialEventParams]`

  Events to send to each session immediately after creation. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `type: Literal["user.message"]`

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          The source of the image data.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          The source of the document data.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: Literal["user.define_outcome"]`

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      How to grade the outcome. Text or file reference.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `type: Literal["system.message"]`

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

- `name: str`

  Human-readable name for the deployment.

  minLength: 1, maxLength: 256

- `budget: Optional[BetaManagedAgentsBudgetLimitParam]`

  Enforced spend ceiling stamped onto each session created from this deployment, copied at session-creation time. Omit to leave sessions uncapped. The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way.

  - `type: Literal["limit"]`

  - `max_list_cost: BetaMonetaryAmount`

    Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

    - `amount: str`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

- `description: Optional[str]`

  Description of what the deployment does.

  maxLength: 2048

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Optional[Iterable[Resource]]`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `type: Literal["github_repository"]`

    - `url: str`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `authorization_token: Optional[str]`

      GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

      minLength: 1, maxLength: 4096

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `type: Literal["file"]`

    - `file_id: str`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsMemoryStoreResourceParam`

    Parameters for attaching a memory store to an agent session.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `schedule: Optional[BetaManagedAgentsScheduleParams]`

  Optional recurring cron schedule. When present, the deployment fires automatically. Both expression and timezone are required when schedule is set.

  - `type: Literal["cron"]`

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.create(
    agent="string",
    environment_id="x",
    initial_events=[
        {
            "content": [
                {
                    "text": "Where is my order #1234?",
                    "type": "text",
                }
            ],
            "type": "user.message",
        }
    ],
    name="x",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.list(**kwargs)  -> SyncPageCursor[BetaManagedAgentsDeployment]`

**GET** `/v1/deployments`

List Deployments

### Parameters

- `agent_id: Optional[str]`

  Filter by agent ID.

- `created_at_gte: Optional[Union[str, datetime]]`

  Return deployments created at or after this time (inclusive).

  format: date-time

- `created_at_lte: Optional[Union[str, datetime]]`

  Return deployments created at or before this time (inclusive).

  format: date-time

- `include_archived: Optional[bool]`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit: Optional[int]`

  Maximum results per page. Default 20, maximum 100.

  format: int32

- `page: Optional[str]`

  Opaque pagination cursor.

- `status: Optional[BetaManagedAgentsDeploymentStatus]`

  Filter by status: `active` or `paused`. Omit for both. To include archived deployments, use `include_archived` instead; the two cannot be combined.

  - `"active"`

    The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

  - `"paused"`

    The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.deployments.list()
page = page.data[0]
print(page.id)
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

`beta.deployments.retrieve(deployment_id, **kwargs)  -> BetaManagedAgentsDeployment`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deployment_id: str`

  Unique identifier of the deployment.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.retrieve(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.update(deployment_id, **kwargs)  -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deployment_id: str`

  Unique identifier of the deployment to update.

- `agent: Optional[Agent]`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

  - `str`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `type: Literal["agent"]`

    - `id: str`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

- `budget: Optional[BetaManagedAgentsBudgetLimitParam]`

  Spend ceiling for future sessions. Full replacement. Omit to preserve; send null to clear (sessions created afterwards are uncapped). The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way.

  - `type: Literal["limit"]`

  - `max_list_cost: BetaMonetaryAmount`

    Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

    - `amount: str`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

- `description: Optional[str]`

  Description. Omit to preserve; send empty string or null to clear.

  maxLength: 2048

- `environment_id: Optional[str]`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  maxLength: 128

- `initial_events: Optional[Iterable[BetaManagedAgentsDeploymentInitialEventParams]]`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `type: Literal["user.message"]`

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          The source of the image data.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          The source of the document data.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: Literal["user.define_outcome"]`

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      How to grade the outcome. Text or file reference.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `type: Literal["system.message"]`

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: Optional[str]`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  maxLength: 256

- `resources: Optional[Iterable[Resource]]`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `type: Literal["github_repository"]`

    - `url: str`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `authorization_token: Optional[str]`

      GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

      minLength: 1, maxLength: 4096

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `type: Literal["file"]`

    - `file_id: str`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsMemoryStoreResourceParam`

    Parameters for attaching a memory store to an agent session.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `schedule: Optional[BetaManagedAgentsScheduleParams]`

  Cron schedule. Full replacement. Omit to preserve; send null to clear (revert to manual-only).

  - `type: Literal["cron"]`

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.update(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.archive(deployment_id, **kwargs)  -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deployment_id: str`

  Unique identifier of the deployment to archive.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.archive(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.run(deployment_id, **kwargs)  -> BetaManagedAgentsDeploymentRun`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deployment_id: str`

  Unique identifier of the deployment to run.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `type: Literal["deployment_run"]`

  - `id: str`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    Snapshot of the agent at fire time. Always fully resolved — deployments pin agent + version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `created_at: datetime`

    Time this run record was persisted.

    format: date-time

  - `deployment_id: str`

    ID of the deployment that produced this run.

  - `error: Optional[Error]`

    Populated on creation failure. Null on success. Exactly one of `session_id` or `error` is non-null.

    - `class BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `type: Literal["environment_archived_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `type: Literal["agent_archived_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `type: Literal["environment_not_found_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `type: Literal["vault_not_found_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `type: Literal["vault_archived_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `type: Literal["file_not_found_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `type: Literal["memory_store_archived_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `type: Literal["skill_not_found_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `type: Literal["session_resource_not_found_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `type: Literal["workspace_archived_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `type: Literal["organization_disabled_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `type: Literal["session_rate_limited_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `type: Literal["session_creation_rejected_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `type: Literal["unknown_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

      - `message: str`

        Human-readable error description.

    - `class BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: Literal["mcp_egress_blocked_error"]`

      - `message: str`

        Human-readable error description.

  - `session_id: Optional[str]`

    Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    What triggered this run and trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `type: Literal["schedule"]`

      - `scheduled_at: datetime`

        The UTC instant at which the cron expression matched in the configured timezone, before jitter is applied. At most one run is recorded per (`deployment_id`, `scheduled_at`) pair.

        format: date-time

    - `class BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: Literal["manual"]`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment_run = client.beta.deployments.run(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment_run.id)
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

`beta.deployments.pause(deployment_id, **kwargs)  -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deployment_id: str`

  Unique identifier of the deployment to pause.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.pause(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
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

`beta.deployments.unpause(deployment_id, **kwargs)  -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deployment_id: str`

  Unique identifier of the deployment to unpause.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 45 more]`

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

- `workspace_id: Optional[str]`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deployment = client.beta.deployments.unpause(
    deployment_id="depl_011CZkZcDH3vPqd7xnEfwTai",
)
print(beta_managed_agents_deployment.id)
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

- `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

  The deployment's agent was archived.

  - `type: Literal["agent_archived_error"]`

### Beta Managed Agents Cron Schedule

- `class BetaManagedAgentsCronSchedule`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `type: Literal["cron"]`

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: str`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    minLength: 1

  - `last_run_at: Optional[datetime]`

    Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

    format: date-time

  - `upcoming_runs_at: Optional[List[datetime]]`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `class BetaManagedAgentsCronScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `type: Literal["cron"]`

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

### Beta Managed Agents Deployment

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `type: Literal["deployment"]`

  - `id: str`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    Reference to the agent this deployment runs, resolved to a concrete version.

    - `type: Literal["agent"]`

    - `id: str`

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    Time the deployment was archived. Null if not archived.

    format: date-time

  - `created_at: datetime`

    Time the deployment was created.

    format: date-time

  - `description: Optional[str]`

    Description of what the deployment does.

  - `environment_id: str`

    ID of the `environment` where sessions run.

  - `initial_events: List[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `type: Literal["user.message"]`

      - `content: List[Content]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            The source of the image data.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            The source of the document data.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `type: Literal["user.define_outcome"]`

      - `description: str`

        What the agent should produce. This is the task specification.

      - `rubric: Rubric`

        How to grade the outcome. Text or file reference.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `max_iterations: Optional[int]`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `type: Literal["system.message"]`

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: str`

    Human-readable name.

  - `paused_reason: Optional[BetaManagedAgentsDeploymentPausedReason]`

    Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: Literal["manual"]`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `type: Literal["error"]`

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The failed run's error.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: Literal["environment_archived_error"]`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: Literal["agent_archived_error"]`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: Literal["environment_not_found_error"]`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: Literal["vault_not_found_error"]`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: Literal["file_not_found_error"]`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: Literal["session_resource_not_found_error"]`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: Literal["workspace_archived_error"]`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: Literal["organization_disabled_error"]`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: Literal["memory_store_archived_error"]`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: Literal["skill_not_found_error"]`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: Literal["vault_archived_error"]`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: Literal["unknown_error"]`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: Literal["self_hosted_resources_unsupported_error"]`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: Literal["mcp_egress_blocked_error"]`

  - `resources: List[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: Literal["github_repository"]`

      - `url: str`

        Github URL of the repository

      - `checkout: Optional[Checkout]`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of a previously uploaded file.

      - `mount_path: Optional[str]`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

        - `"read_write"`

        - `"read_only"`

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: Optional[BetaManagedAgentsSchedule]`

    Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant.

    - `type: Literal["cron"]`

    - `expression: str`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: str`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `last_run_at: Optional[datetime]`

      Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

      format: date-time

    - `upcoming_runs_at: Optional[List[datetime]]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set.

    - `"active"`

      The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

    - `"paused"`

      The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

  - `updated_at: datetime`

    Time the deployment was last updated.

    format: date-time

  - `vault_ids: List[str]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Beta Managed Agents Deployment Initial Event

- `type BetaManagedAgentsDeploymentInitialEvent = ...`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsDeploymentUserMessageEvent`

    A user message sent to the session.

    - `type: Literal["user.message"]`

    - `content: List[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          The source of the image data.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          The source of the document data.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

  - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `type: Literal["user.define_outcome"]`

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      How to grade the outcome. Text or file reference.

      - `class BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsDeploymentSystemMessageEvent`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `type: Literal["system.message"]`

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

### Beta Managed Agents Deployment Initial Event Params

- `type BetaManagedAgentsDeploymentInitialEventParams = ...`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `type: Literal["user.message"]`

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          The source of the image data.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          The source of the document data.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: Literal["user.define_outcome"]`

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      How to grade the outcome. Text or file reference.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `type: Literal["system.message"]`

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

### Beta Managed Agents Deployment Paused Reason

- `type BetaManagedAgentsDeploymentPausedReason = ...`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `class BetaManagedAgentsManualDeploymentPausedReason`

    The caller invoked the pause endpoint on the deployment.

    - `type: Literal["manual"]`

  - `class BetaManagedAgentsErrorDeploymentPausedReason`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `type: Literal["error"]`

    - `error: BetaManagedAgentsDeploymentPausedReasonError`

      The failed run's error.

      - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

        The deployment's environment was archived.

        - `type: Literal["environment_archived_error"]`

      - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

        The deployment's agent was archived.

        - `type: Literal["agent_archived_error"]`

      - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

        The deployment's environment no longer exists.

        - `type: Literal["environment_not_found_error"]`

      - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

        A vault referenced by the deployment no longer exists.

        - `type: Literal["vault_not_found_error"]`

      - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

        A file resource referenced by the deployment no longer exists.

        - `type: Literal["file_not_found_error"]`

      - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

        A referenced resource no longer exists and its kind was not reported.

        - `type: Literal["session_resource_not_found_error"]`

      - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

        The deployment's workspace was archived.

        - `type: Literal["workspace_archived_error"]`

      - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

        The deployment's organization is disabled.

        - `type: Literal["organization_disabled_error"]`

      - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

        A memory store referenced by the deployment is archived.

        - `type: Literal["memory_store_archived_error"]`

      - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

        A skill referenced by the deployment's agent no longer exists.

        - `type: Literal["skill_not_found_error"]`

      - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

        A vault referenced by the deployment is archived.

        - `type: Literal["vault_archived_error"]`

      - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: Literal["unknown_error"]`

      - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: Literal["self_hosted_resources_unsupported_error"]`

      - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: Literal["mcp_egress_blocked_error"]`

### Beta Managed Agents Deployment Paused Reason Error

- `type BetaManagedAgentsDeploymentPausedReasonError = ...`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

    The deployment's environment was archived.

    - `type: Literal["environment_archived_error"]`

  - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

    The deployment's agent was archived.

    - `type: Literal["agent_archived_error"]`

  - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

    The deployment's environment no longer exists.

    - `type: Literal["environment_not_found_error"]`

  - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

    A vault referenced by the deployment no longer exists.

    - `type: Literal["vault_not_found_error"]`

  - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

    A file resource referenced by the deployment no longer exists.

    - `type: Literal["file_not_found_error"]`

  - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

    A referenced resource no longer exists and its kind was not reported.

    - `type: Literal["session_resource_not_found_error"]`

  - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

    The deployment's workspace was archived.

    - `type: Literal["workspace_archived_error"]`

  - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

    The deployment's organization is disabled.

    - `type: Literal["organization_disabled_error"]`

  - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

    A memory store referenced by the deployment is archived.

    - `type: Literal["memory_store_archived_error"]`

  - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

    A skill referenced by the deployment's agent no longer exists.

    - `type: Literal["skill_not_found_error"]`

  - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

    A vault referenced by the deployment is archived.

    - `type: Literal["vault_archived_error"]`

  - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: Literal["unknown_error"]`

  - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: Literal["self_hosted_resources_unsupported_error"]`

  - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: Literal["mcp_egress_blocked_error"]`

### Beta Managed Agents Deployment Status

- `type BetaManagedAgentsDeploymentStatus = Literal["active", "paused"]`

  Lifecycle status of a deployment.

  - `"active"`

    The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them.

  - `"paused"`

    The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted.

### Beta Managed Agents Deployment System Message Event

- `class BetaManagedAgentsDeploymentSystemMessageEvent`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `type: Literal["system.message"]`

  - `content: List[BetaManagedAgentsSystemContentBlock]`

    System content blocks to append. Text-only.

    - `type: Literal["text"]`

    - `text: str`

      The text content.

      minLength: 1

### Beta Managed Agents Deployment User Define Outcome Event

- `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `type: Literal["user.define_outcome"]`

  - `description: str`

    What the agent should produce. This is the task specification.

  - `rubric: Rubric`

    How to grade the outcome. Text or file reference.

    - `class BetaManagedAgentsFileRubric`

      Rubric referenced by a file uploaded via the Files API.

      - `type: Literal["file"]`

      - `file_id: str`

        ID of the rubric file.

    - `class BetaManagedAgentsTextRubric`

      Rubric content provided inline as text.

      - `type: Literal["text"]`

      - `content: str`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `max_iterations: Optional[int]`

    Eval→revision cycles before giving up. Default 3, max 20.

    format: int32

### Beta Managed Agents Deployment User Message Event

- `class BetaManagedAgentsDeploymentUserMessageEvent`

  A user message sent to the session.

  - `type: Literal["user.message"]`

  - `content: List[Content]`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock`

      Regular text content.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `class BetaManagedAgentsImageBlock`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: Literal["image"]`

      - `source: Source`

        The source of the image data.

        - `class BetaManagedAgentsBase64ImageSource`

          Base64-encoded image data.

          - `type: Literal["base64"]`

          - `data: str`

            Base64-encoded image data.

            minLength: 1

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `class BetaManagedAgentsURLImageSource`

          Image referenced by URL.

          - `type: Literal["url"]`

          - `url: str`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource`

          Image referenced by file ID.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of a previously uploaded file.

            minLength: 1

    - `class BetaManagedAgentsDocumentBlock`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: Literal["document"]`

      - `source: Source`

        The source of the document data.

        - `class BetaManagedAgentsBase64DocumentSource`

          Base64-encoded document data.

          - `type: Literal["base64"]`

          - `data: str`

            Base64-encoded document data.

            minLength: 1

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `class BetaManagedAgentsPlainTextDocumentSource`

          Plain text document content.

          - `type: Literal["text"]`

          - `data: str`

            The plain text content.

            minLength: 1

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

        - `class BetaManagedAgentsURLDocumentSource`

          Document referenced by URL.

          - `type: Literal["url"]`

          - `url: str`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource`

          Document referenced by file ID.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of a previously uploaded file.

            minLength: 1

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsRedactedBlock`

      Placeholder for content withheld by Anthropic model policy.

      - `type: Literal["redacted"]`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

  The deployment's environment was archived.

  - `type: Literal["environment_archived_error"]`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

  The deployment's environment no longer exists.

  - `type: Literal["environment_not_found_error"]`

### Beta Managed Agents Error Deployment Paused Reason

- `class BetaManagedAgentsErrorDeploymentPausedReason`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `type: Literal["error"]`

  - `error: BetaManagedAgentsDeploymentPausedReasonError`

    The failed run's error.

    - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

      The deployment's environment was archived.

      - `type: Literal["environment_archived_error"]`

    - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

      The deployment's agent was archived.

      - `type: Literal["agent_archived_error"]`

    - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

      The deployment's environment no longer exists.

      - `type: Literal["environment_not_found_error"]`

    - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

      A vault referenced by the deployment no longer exists.

      - `type: Literal["vault_not_found_error"]`

    - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

      A file resource referenced by the deployment no longer exists.

      - `type: Literal["file_not_found_error"]`

    - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

      A referenced resource no longer exists and its kind was not reported.

      - `type: Literal["session_resource_not_found_error"]`

    - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

      The deployment's workspace was archived.

      - `type: Literal["workspace_archived_error"]`

    - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

      The deployment's organization is disabled.

      - `type: Literal["organization_disabled_error"]`

    - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

      A memory store referenced by the deployment is archived.

      - `type: Literal["memory_store_archived_error"]`

    - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

      A skill referenced by the deployment's agent no longer exists.

      - `type: Literal["skill_not_found_error"]`

    - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

      A vault referenced by the deployment is archived.

      - `type: Literal["vault_archived_error"]`

    - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: Literal["unknown_error"]`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: Literal["self_hosted_resources_unsupported_error"]`

    - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: Literal["mcp_egress_blocked_error"]`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

  A file resource referenced by the deployment no longer exists.

  - `type: Literal["file_not_found_error"]`

### Beta Managed Agents File Resource Config

- `class BetaManagedAgentsFileResourceConfig`

  A file mounted into each session's container.

  - `type: Literal["file"]`

  - `file_id: str`

    ID of a previously uploaded file.

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `class BetaManagedAgentsGitHubRepositoryResourceConfig`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: Literal["github_repository"]`

  - `url: str`

    Github URL of the repository

  - `checkout: Optional[Checkout]`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout`

      - `type: Literal["branch"]`

      - `name: str`

        Branch name to check out.

        minLength: 1, maxLength: 255

    - `class BetaManagedAgentsCommitCheckout`

      - `type: Literal["commit"]`

      - `sha: str`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `class BetaManagedAgentsManualDeploymentPausedReason`

  The caller invoked the pause endpoint on the deployment.

  - `type: Literal["manual"]`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: Literal["mcp_egress_blocked_error"]`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

  A memory store referenced by the deployment is archived.

  - `type: Literal["memory_store_archived_error"]`

### Beta Managed Agents Memory Store Resource Config

- `class BetaManagedAgentsMemoryStoreResourceConfig`

  A memory store attached to each session created from this deployment.

  - `type: Literal["memory_store"]`

  - `memory_store_id: str`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `access: Optional[Literal["read_write", "read_only"]]`

    Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

    - `"read_write"`

    - `"read_only"`

  - `instructions: Optional[str]`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

  The deployment's organization is disabled.

  - `type: Literal["organization_disabled_error"]`

### Beta Managed Agents Schedule

- `class BetaManagedAgentsSchedule`

  A recurring schedule with computed runtime timestamps. Discriminated union — only cron is supported currently.

  - `type: Literal["cron"]`

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: str`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    minLength: 1

  - `last_run_at: Optional[datetime]`

    Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this.

    format: date-time

  - `upcoming_runs_at: Optional[List[datetime]]`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `class BetaManagedAgentsScheduleParams`

  A recurring schedule. Discriminated union — only cron is supported currently.

  - `type: Literal["cron"]`

  - `expression: str`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: str`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: Literal["self_hosted_resources_unsupported_error"]`

### Beta Managed Agents Session Resource Config

- `type BetaManagedAgentsSessionResourceConfig = ...`

  A configured session resource. Echoes the input minus write-only credentials.

  - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: Literal["github_repository"]`

    - `url: str`

      Github URL of the repository

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceConfig`

    A file mounted into each session's container.

    - `type: Literal["file"]`

    - `file_id: str`

      ID of a previously uploaded file.

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceConfig`

    A memory store attached to each session created from this deployment.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

  A referenced resource no longer exists and its kind was not reported.

  - `type: Literal["session_resource_not_found_error"]`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

  A skill referenced by the deployment's agent no longer exists.

  - `type: Literal["skill_not_found_error"]`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: Literal["unknown_error"]`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

  A vault referenced by the deployment is archived.

  - `type: Literal["vault_archived_error"]`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

  A vault referenced by the deployment no longer exists.

  - `type: Literal["vault_not_found_error"]`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

  The deployment's workspace was archived.

  - `type: Literal["workspace_archived_error"]`
