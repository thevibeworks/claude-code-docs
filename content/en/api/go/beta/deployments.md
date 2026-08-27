# Deployments

## Create Deployment

`client.Beta.Deployments.New(ctx, params) (*BetaManagedAgentsDeployment, error)`

**POST** `/v1/deployments`

Create Deployment

### Parameters

- `params BetaDeploymentNewParams`

  - `Agent param.Field[BetaDeploymentNewParamsAgentUnion]`

    Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsAgentParamsType`

      - `Version int64 Optional`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `EnvironmentID param.Field[string]`

    Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

    minLength: 1, maxLength: 128

  - `InitialEvents param.Field[[]BetaManagedAgentsDeploymentInitialEventParamsUnionResp]`

    Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

    - `type BetaManagedAgentsUserMessageEventParams struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsUserMessageEventParamsType`

    - `type BetaManagedAgentsUserDefineOutcomeEventParams struct{…}`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubricParams struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricParamsType`

        - `type BetaManagedAgentsTextRubricParams struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type BetaManagedAgentsTextRubricParamsType`

      - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsSystemMessageEventParamsResp struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsSystemMessageEventParamsType`

  - `Name param.Field[string]`

    Body param: Human-readable name for the deployment.

    minLength: 1, maxLength: 256

  - `Budget param.Field[BetaManagedAgentsBudgetLimit] Optional`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `Description param.Field[string] Optional`

    Body param: Description of what the deployment does.

    maxLength: 2048

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Resources param.Field[[]BetaDeploymentNewParamsResourceUnion] Optional`

    Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

      Mount a GitHub repository into the session's container.

      - `AuthorizationToken string`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

      - `URL string`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `type BetaManagedAgentsFileResourceParamsResp struct{…}`

      Mount a file uploaded via the Files API into the session.

      - `FileID string`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsFileResourceParamsType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}`

      Parameters for attaching a memory store to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceParamType`

      - `Access BetaManagedAgentsMemoryStoreResourceParamAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `Schedule param.Field[BetaManagedAgentsScheduleParamsResp] Optional`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `VaultIDs param.Field[[]string] Optional`

    Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeployment, err := client.Beta.Deployments.New(context.TODO(), anthropic.BetaDeploymentNewParams{
		Agent: anthropic.BetaDeploymentNewParamsAgentUnion{
			OfString: anthropic.String("string"),
		},
		EnvironmentID: "x",
		InitialEvents: []anthropic.BetaManagedAgentsDeploymentInitialEventParamsUnion{anthropic.BetaManagedAgentsDeploymentInitialEventParamsUnion{
			OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
				Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{
					OfText: &anthropic.BetaManagedAgentsTextBlockParam{
						Text: "Where is my order #1234?",
						Type: anthropic.BetaManagedAgentsTextBlockTypeText,
					},
				}},
				Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
			},
		}},
		Name: "x",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeployment.ID)
}
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

`client.Beta.Deployments.List(ctx, params) (*PageCursor[BetaManagedAgentsDeployment], error)`

**GET** `/v1/deployments`

List Deployments

### Parameters

- `params BetaDeploymentListParams`

  - `AgentID param.Field[string] Optional`

    Query param: Filter by agent ID.

  - `CreatedAtGte param.Field[Time] Optional`

    Query param: Return deployments created at or after this time (inclusive).

    format: date-time

  - `CreatedAtLte param.Field[Time] Optional`

    Query param: Return deployments created at or before this time (inclusive).

    format: date-time

  - `IncludeArchived param.Field[bool] Optional`

    Query param: When true, includes archived deployments. Default: false (exclude archived).

  - `Limit param.Field[int64] Optional`

    Query param: Maximum results per page. Default 20, maximum 100.

    format: int32

  - `Page param.Field[string] Optional`

    Query param: Opaque pagination cursor.

  - `Status param.Field[BetaManagedAgentsDeploymentStatus] Optional`

    Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Deployments.List(context.TODO(), anthropic.BetaDeploymentListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
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

`client.Beta.Deployments.Get(ctx, deploymentID, query) (*BetaManagedAgentsDeployment, error)`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `deploymentID string`

- `query BetaDeploymentGetParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeployment, err := client.Beta.Deployments.Get(
		context.TODO(),
		"depl_011CZkZcDH3vPqd7xnEfwTai",
		anthropic.BetaDeploymentGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeployment.ID)
}
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

`client.Beta.Deployments.Update(ctx, deploymentID, params) (*BetaManagedAgentsDeployment, error)`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `deploymentID string`

- `params BetaDeploymentUpdateParams`

  - `Agent param.Field[BetaDeploymentUpdateParamsAgentUnion] Optional`

    Body param: Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsAgentParamsType`

      - `Version int64 Optional`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `Budget param.Field[BetaManagedAgentsBudgetLimit] Optional`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `Description param.Field[string] Optional`

    Body param: Description. Omit to preserve; send empty string or null to clear.

    maxLength: 2048

  - `EnvironmentID param.Field[string] Optional`

    Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

    maxLength: 128

  - `InitialEvents param.Field[[]BetaManagedAgentsDeploymentInitialEventParamsUnionResp] Optional`

    Body param: Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

    - `type BetaManagedAgentsUserMessageEventParams struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsUserMessageEventParamsType`

    - `type BetaManagedAgentsUserDefineOutcomeEventParams struct{…}`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubricParams struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricParamsType`

        - `type BetaManagedAgentsTextRubricParams struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type BetaManagedAgentsTextRubricParamsType`

      - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsSystemMessageEventParamsResp struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsSystemMessageEventParamsType`

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Name param.Field[string] Optional`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

    maxLength: 256

  - `Resources param.Field[[]BetaDeploymentUpdateParamsResourceUnion] Optional`

    Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

      Mount a GitHub repository into the session's container.

      - `AuthorizationToken string`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

      - `URL string`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `type BetaManagedAgentsFileResourceParamsResp struct{…}`

      Mount a file uploaded via the Files API into the session.

      - `FileID string`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsFileResourceParamsType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}`

      Parameters for attaching a memory store to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceParamType`

      - `Access BetaManagedAgentsMemoryStoreResourceParamAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `Schedule param.Field[BetaManagedAgentsScheduleParamsResp] Optional`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `VaultIDs param.Field[[]string] Optional`

    Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeployment, err := client.Beta.Deployments.Update(
		context.TODO(),
		"depl_011CZkZcDH3vPqd7xnEfwTai",
		anthropic.BetaDeploymentUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeployment.ID)
}
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

`client.Beta.Deployments.Archive(ctx, deploymentID, body) (*BetaManagedAgentsDeployment, error)`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `deploymentID string`

- `body BetaDeploymentArchiveParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeployment, err := client.Beta.Deployments.Archive(
		context.TODO(),
		"depl_011CZkZcDH3vPqd7xnEfwTai",
		anthropic.BetaDeploymentArchiveParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeployment.ID)
}
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

`client.Beta.Deployments.Run(ctx, deploymentID, body) (*BetaManagedAgentsDeploymentRun, error)`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `deploymentID string`

- `body BetaDeploymentRunParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeploymentRun struct{…}`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `ID string`

    Unique identifier for this run (`drun_...`).

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `DeploymentID string`

    ID of the deployment that produced this run.

  - `Error BetaManagedAgentsDeploymentRunErrorUnion`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `type BetaManagedAgentsEnvironmentArchivedRunError struct{…}`

      The deployment's environment was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentArchivedRunErrorType`

    - `type BetaManagedAgentsAgentArchivedRunError struct{…}`

      The deployment's agent was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsAgentArchivedRunErrorType`

    - `type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}`

      The deployment's environment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentNotFoundRunErrorType`

    - `type BetaManagedAgentsVaultNotFoundRunError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultNotFoundRunErrorType`

    - `type BetaManagedAgentsVaultArchivedRunError struct{…}`

      A vault referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultArchivedRunErrorType`

    - `type BetaManagedAgentsFileNotFoundRunError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsFileNotFoundRunErrorType`

    - `type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMemoryStoreArchivedRunErrorType`

    - `type BetaManagedAgentsSkillNotFoundRunError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSkillNotFoundRunErrorType`

    - `type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionResourceNotFoundRunErrorType`

    - `type BetaManagedAgentsWorkspaceArchivedRunError struct{…}`

      The deployment's workspace was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsWorkspaceArchivedRunErrorType`

    - `type BetaManagedAgentsOrganizationDisabledRunError struct{…}`

      The deployment's organization is disabled.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsOrganizationDisabledRunErrorType`

    - `type BetaManagedAgentsSessionRateLimitedRunError struct{…}`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionRateLimitedRunErrorType`

    - `type BetaManagedAgentsSessionCreationRejectedRunError struct{…}`

      The session create request was rejected with a non-retryable validation error.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionCreationRejectedRunErrorType`

    - `type BetaManagedAgentsUnknownRunError struct{…}`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsUnknownRunErrorType`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType`

    - `type BetaManagedAgentsMCPEgressBlockedRunError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMCPEgressBlockedRunErrorType`

  - `SessionID string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `TriggerContext BetaManagedAgentsTriggerContextUnion`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `type BetaManagedAgentsScheduleTriggerContext struct{…}`

      The run was fired by the deployment's cron schedule.

      - `ScheduledAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `Type BetaManagedAgentsScheduleTriggerContextType`

    - `type BetaManagedAgentsManualTriggerContext struct{…}`

      The run was started manually by creating a session directly against the deployment.

      - `Type BetaManagedAgentsManualTriggerContextType`

  - `Type BetaManagedAgentsDeploymentRunType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeploymentRun, err := client.Beta.Deployments.Run(
		context.TODO(),
		"depl_011CZkZcDH3vPqd7xnEfwTai",
		anthropic.BetaDeploymentRunParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeploymentRun.ID)
}
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

`client.Beta.Deployments.Pause(ctx, deploymentID, body) (*BetaManagedAgentsDeployment, error)`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `deploymentID string`

- `body BetaDeploymentPauseParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeployment, err := client.Beta.Deployments.Pause(
		context.TODO(),
		"depl_011CZkZcDH3vPqd7xnEfwTai",
		anthropic.BetaDeploymentPauseParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeployment.ID)
}
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

`client.Beta.Deployments.Unpause(ctx, deploymentID, body) (*BetaManagedAgentsDeployment, error)`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `deploymentID string`

- `body BetaDeploymentUnpauseParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

### Returns

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaManagedAgentsDeployment, err := client.Beta.Deployments.Unpause(
		context.TODO(),
		"depl_011CZkZcDH3vPqd7xnEfwTai",
		anthropic.BetaDeploymentUnpauseParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeployment.ID)
}
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

- `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

  The deployment's agent was archived.

  - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

### Beta Managed Agents Cron Schedule

- `type BetaManagedAgentsCronSchedule struct{…}`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `Expression string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `Timezone string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    minLength: 1

  - `Type BetaManagedAgentsCronScheduleType`

  - `LastRunAt Time Optional`

    A timestamp in RFC 3339 format

    format: date-time

  - `UpcomingRunsAt []Time Optional`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `type BetaManagedAgentsCronScheduleParamsResp struct{…}`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Expression string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `Timezone string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

  - `Type BetaManagedAgentsCronScheduleParamsType`

### Beta Managed Agents Deployment

- `type BetaManagedAgentsDeployment struct{…}`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `ID string`

    Unique identifier for this deployment.

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    Description of what the deployment does.

  - `EnvironmentID string`

    ID of the `environment` where sessions run.

  - `InitialEvents []BetaManagedAgentsDeploymentInitialEventUnion`

    Events sent to each session immediately after creation.

    - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

      A user message sent to the session.

      - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `Name string`

    Human-readable name.

  - `PausedReason BetaManagedAgentsDeploymentPausedReasonUnion`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

      The caller invoked the pause endpoint on the deployment.

      - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's environment was archived.

          - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

          The deployment's agent was archived.

          - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

          The deployment's environment no longer exists.

          - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

          A file resource referenced by the deployment no longer exists.

          - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

          A referenced resource no longer exists and its kind was not reported.

          - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

          The deployment's workspace was archived.

          - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

          The deployment's organization is disabled.

          - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

          A memory store referenced by the deployment is archived.

          - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

          A skill referenced by the deployment's agent no longer exists.

          - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

          A vault referenced by the deployment is archived.

          - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

  - `Resources []BetaManagedAgentsSessionResourceConfigUnion`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceConfig struct{…}`

      A file mounted into each session's container.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceConfigType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

      A memory store attached to each session created from this deployment.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Schedule BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `Expression string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `Timezone string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type BetaManagedAgentsScheduleType`

    - `LastRunAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `UpcomingRunsAt []Time Optional`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

### Beta Managed Agents Deployment Initial Event

- `type BetaManagedAgentsDeploymentInitialEventUnion interface{…}`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

    A user message sent to the session.

    - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

      Array of content blocks for the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsTextBlockType`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type BetaManagedAgentsBase64ImageSourceType`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileImageSourceType`

        - `Type BetaManagedAgentsImageBlockType`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type BetaManagedAgentsBase64DocumentSourceType`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileDocumentSourceType`

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `Type BetaManagedAgentsDeploymentUserMessageEventType`

  - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `Description string`

      What the agent should produce. This is the task specification.

    - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

    - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

    - `MaxIterations int64 Optional`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsSystemContentBlockType`

    - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

### Beta Managed Agents Deployment Initial Event Params

- `type BetaManagedAgentsDeploymentInitialEventParamsUnionResp interface{…}`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `type BetaManagedAgentsUserMessageEventParams struct{…}`

    Parameters for sending a user message to the session.

    - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

      Array of content blocks for the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsTextBlockType`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type BetaManagedAgentsBase64ImageSourceType`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileImageSourceType`

        - `Type BetaManagedAgentsImageBlockType`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type BetaManagedAgentsBase64DocumentSourceType`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileDocumentSourceType`

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `Type BetaManagedAgentsUserMessageEventParamsType`

  - `type BetaManagedAgentsUserDefineOutcomeEventParams struct{…}`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `Description string`

      What the agent should produce. This is the task specification.

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubricParams struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricParamsType`

      - `type BetaManagedAgentsTextRubricParams struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `Type BetaManagedAgentsTextRubricParamsType`

    - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

    - `MaxIterations int64 Optional`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `type BetaManagedAgentsSystemMessageEventParamsResp struct{…}`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsSystemContentBlockType`

    - `Type BetaManagedAgentsSystemMessageEventParamsType`

### Beta Managed Agents Deployment Paused Reason

- `type BetaManagedAgentsDeploymentPausedReasonUnion interface{…}`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

    The caller invoked the pause endpoint on the deployment.

    - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

  - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

        The deployment's environment was archived.

        - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

        The deployment's agent was archived.

        - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

        The deployment's environment no longer exists.

        - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

        A vault referenced by the deployment no longer exists.

        - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

        A file resource referenced by the deployment no longer exists.

        - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

        A referenced resource no longer exists and its kind was not reported.

        - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

        The deployment's workspace was archived.

        - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

        The deployment's organization is disabled.

        - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

        A memory store referenced by the deployment is archived.

        - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

        A skill referenced by the deployment's agent no longer exists.

        - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

        A vault referenced by the deployment is archived.

        - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

      - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

    - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

### Beta Managed Agents Deployment Paused Reason Error

- `type BetaManagedAgentsDeploymentPausedReasonErrorUnion interface{…}`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

    The deployment's environment was archived.

    - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

    The deployment's agent was archived.

    - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

    The deployment's environment no longer exists.

    - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

    A vault referenced by the deployment no longer exists.

    - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

    A file resource referenced by the deployment no longer exists.

    - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

    A referenced resource no longer exists and its kind was not reported.

    - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

    The deployment's workspace was archived.

    - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

    The deployment's organization is disabled.

    - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

    A memory store referenced by the deployment is archived.

    - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

    A skill referenced by the deployment's agent no longer exists.

    - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

    A vault referenced by the deployment is archived.

    - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

  - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

### Beta Managed Agents Deployment Status

- `type BetaManagedAgentsDeploymentStatus string`

  Lifecycle status of a deployment.

  - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

  - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

### Beta Managed Agents Deployment System Message Event

- `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `Content []BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `Text string`

      The text content.

      minLength: 1

    - `Type BetaManagedAgentsSystemContentBlockType`

  - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

### Beta Managed Agents Deployment User Define Outcome Event

- `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `Description string`

    What the agent should produce. This is the task specification.

  - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

    Rubric for grading the quality of an outcome.

    - `type BetaManagedAgentsFileRubric struct{…}`

      Rubric referenced by a file uploaded via the Files API.

      - `FileID string`

        ID of the rubric file.

      - `Type BetaManagedAgentsFileRubricType`

    - `type BetaManagedAgentsTextRubric struct{…}`

      Rubric content provided inline as text.

      - `Content string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `Type BetaManagedAgentsTextRubricType`

  - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

  - `MaxIterations int64 Optional`

    Eval→revision cycles before giving up. Default 3, max 20.

    format: int32

### Beta Managed Agents Deployment User Message Event

- `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

  A user message sent to the session.

  - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

    Array of content blocks for the user message.

    - `type BetaManagedAgentsTextBlock struct{…}`

      Regular text content.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsTextBlockType`

    - `type BetaManagedAgentsImageBlock struct{…}`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source BetaManagedAgentsImageBlockSourceUnion`

        Union type for image source variants.

        - `type BetaManagedAgentsBase64ImageSource struct{…}`

          Base64-encoded image data.

          - `Data string`

            Base64-encoded image data.

            minLength: 1

          - `MediaType string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type BetaManagedAgentsBase64ImageSourceType`

        - `type BetaManagedAgentsURLImageSource struct{…}`

          Image referenced by URL.

          - `Type BetaManagedAgentsURLImageSourceType`

          - `URL string`

            URL of the image to fetch.

            minLength: 1

        - `type BetaManagedAgentsFileImageSource struct{…}`

          Image referenced by file ID.

          - `FileID string`

            ID of a previously uploaded file.

            minLength: 1

          - `Type BetaManagedAgentsFileImageSourceType`

      - `Type BetaManagedAgentsImageBlockType`

    - `type BetaManagedAgentsDocumentBlock struct{…}`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source BetaManagedAgentsDocumentBlockSourceUnion`

        Union type for document source variants.

        - `type BetaManagedAgentsBase64DocumentSource struct{…}`

          Base64-encoded document data.

          - `Data string`

            Base64-encoded document data.

            minLength: 1

          - `MediaType string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type BetaManagedAgentsBase64DocumentSourceType`

        - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

          Plain text document content.

          - `Data string`

            The plain text content.

            minLength: 1

          - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type BetaManagedAgentsPlainTextDocumentSourceType`

        - `type BetaManagedAgentsURLDocumentSource struct{…}`

          Document referenced by URL.

          - `Type BetaManagedAgentsURLDocumentSourceType`

          - `URL string`

            URL of the document to fetch.

            minLength: 1

        - `type BetaManagedAgentsFileDocumentSource struct{…}`

          Document referenced by file ID.

          - `FileID string`

            ID of a previously uploaded file.

            minLength: 1

          - `Type BetaManagedAgentsFileDocumentSourceType`

      - `Type BetaManagedAgentsDocumentBlockType`

      - `Context string Optional`

        Additional context about the document for the model.

      - `Title string Optional`

        The title of the document.

    - `type BetaManagedAgentsRedactedBlockParam struct{…}`

      Placeholder for content withheld by Anthropic model policy.

      - `Type BetaManagedAgentsRedactedBlockType`

  - `Type BetaManagedAgentsDeploymentUserMessageEventType`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

  The deployment's environment was archived.

  - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

  The deployment's environment no longer exists.

  - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

### Beta Managed Agents Error Deployment Paused Reason

- `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

      The deployment's environment was archived.

      - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

      The deployment's agent was archived.

      - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

      The deployment's environment no longer exists.

      - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

      The deployment's workspace was archived.

      - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

      The deployment's organization is disabled.

      - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

      A vault referenced by the deployment is archived.

      - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

    - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

  - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

  A file resource referenced by the deployment no longer exists.

  - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

### Beta Managed Agents File Resource Config

- `type BetaManagedAgentsFileResourceConfig struct{…}`

  A file mounted into each session's container.

  - `FileID string`

    ID of a previously uploaded file.

  - `Type BetaManagedAgentsFileResourceConfigType`

  - `MountPath string Optional`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

  - `URL string`

    Github URL of the repository

  - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `type BetaManagedAgentsBranchCheckout struct{…}`

      - `Name string`

        Branch name to check out.

        minLength: 1, maxLength: 255

      - `Type BetaManagedAgentsBranchCheckoutType`

    - `type BetaManagedAgentsCommitCheckout struct{…}`

      - `Sha string`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

      - `Type BetaManagedAgentsCommitCheckoutType`

  - `MountPath string Optional`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

  The caller invoked the pause endpoint on the deployment.

  - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

  A memory store referenced by the deployment is archived.

  - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

### Beta Managed Agents Memory Store Resource Config

- `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

  A memory store attached to each session created from this deployment.

  - `MemoryStoreID string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

  - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

    Access mode for an attached memory store.

    - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

    - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

  - `Instructions string Optional`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

  The deployment's organization is disabled.

  - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

### Beta Managed Agents Schedule

- `type BetaManagedAgentsSchedule struct{…}`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `Expression string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `Timezone string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    minLength: 1

  - `Type BetaManagedAgentsScheduleType`

  - `LastRunAt Time Optional`

    A timestamp in RFC 3339 format

    format: date-time

  - `UpcomingRunsAt []Time Optional`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `type BetaManagedAgentsScheduleParamsResp struct{…}`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Expression string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `Timezone string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

  - `Type BetaManagedAgentsScheduleParamsType`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

### Beta Managed Agents Session Resource Config

- `type BetaManagedAgentsSessionResourceConfigUnion interface{…}`

  A configured session resource. Echoes the input minus write-only credentials.

  - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

    - `URL string`

      Github URL of the repository

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion Optional`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type BetaManagedAgentsBranchCheckoutType`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type BetaManagedAgentsCommitCheckoutType`

    - `MountPath string Optional`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `type BetaManagedAgentsFileResourceConfig struct{…}`

    A file mounted into each session's container.

    - `FileID string`

      ID of a previously uploaded file.

    - `Type BetaManagedAgentsFileResourceConfigType`

    - `MountPath string Optional`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

    A memory store attached to each session created from this deployment.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

    - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess Optional`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

    - `Instructions string Optional`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

  A referenced resource no longer exists and its kind was not reported.

  - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

  A skill referenced by the deployment's agent no longer exists.

  - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

  A vault referenced by the deployment is archived.

  - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

  A vault referenced by the deployment no longer exists.

  - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

  The deployment's workspace was archived.

  - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`
