# Create Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Create(parameters, cancellationToken = default)`

**POST** `/v1/deployments`

Create Deployment

## Parameters

- `DeploymentCreateParams parameters`

  - `required Agent agent`

    Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `required string environmentID`

    Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

    minLength: 1, maxLength: 128

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required string name`

    Body param: Human-readable name for the deployment.

    minLength: 1, maxLength: 256

  - `BetaManagedAgentsBudgetLimit? budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? description`

    Body param: Description of what the deployment does.

    maxLength: 2048

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<Resource> resources`

    Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite("read_write")`

        - `ReadOnly("read_only")`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

## Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? Description`

    Description of what the deployment does.

  - `required string EnvironmentID`

    ID of the `environment` where sessions run.

  - `required IReadOnlyList<BetaManagedAgentsDeploymentInitialEvent> InitialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite("read_write")`

        - `ReadOnly("read_only")`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active("active")`

    - `Paused("paused")`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

## Example

```csharp
DeploymentCreateParams parameters = new()
{
    Agent = "string",
    EnvironmentID = "x",
    InitialEvents =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
    Name = "x",
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Create(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
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
