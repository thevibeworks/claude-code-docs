# Send Events

`client.Beta.Sessions.Events.Send(ctx, sessionID, params) (*BetaManagedAgentsSendSessionEvents, error)`

**POST** `/v1/sessions/{session_id}/events`

Send Events

## Parameters

- `sessionID string`

- `params BetaSessionEventSendParams`

  - `Events param.Field[[]BetaManagedAgentsEventParamsUnionResp]`

    Body param: Events to send to the `session`.

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

    - `type BetaManagedAgentsUserInterruptEventParamsResp struct{…}`

      Parameters for sending an interrupt to pause the agent.

      - `Type BetaManagedAgentsUserInterruptEventParamsType`

      - `SessionThreadID string Optional`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}`

      Parameters for confirming or denying a tool execution request.

      - `Result BetaManagedAgentsUserToolConfirmationEventParamsResult`

        UserToolConfirmationResult enum

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"`

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"`

      - `ToolUseID string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsUserToolConfirmationEventParamsType`

      - `DenyMessage string Optional`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

    - `type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}`

      Parameters for providing the result of a custom tool execution.

      - `CustomToolUseID string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsUserCustomToolResultEventParamsType`

      - `Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionResp Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

          - `Citations BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `Enabled bool`

              Whether citations are enabled for this search result.

          - `Content []BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `Text string`

              The text content.

              minLength: 1

            - `Type BetaManagedAgentsSearchResultContentType`

          - `Source string`

            The URL source of the search result.

            minLength: 1

          - `Title string`

            The title of the search result.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultBlockType`

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

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

    - `type BetaManagedAgentsUserToolResultEventParamsResp struct{…}`

      Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `ToolUseID string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsUserToolResultEventParamsType`

      - `Content []BetaManagedAgentsUserToolResultEventParamsContentUnionResp Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

    - `type BetaManagedAgentsSystemMessageEventParamsResp struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsSystemMessageEventParamsType`

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

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

## Returns

- `type BetaManagedAgentsSendSessionEvents struct{…}`

  Events that were successfully sent to the session.

  - `Data []BetaManagedAgentsSendSessionEventsDataUnion Optional`

    Sent events

    - `type BetaManagedAgentsUserMessageEvent struct{…}`

      A user message event in the session conversation.

      - `ID string`

        Unique identifier for this event.

      - `Content []BetaManagedAgentsUserMessageEventContentUnion`

        Array of content blocks comprising the user message.

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

      - `Type BetaManagedAgentsUserMessageEventType`

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsUserInterruptEvent struct{…}`

      An interrupt event that pauses agent execution and returns control to the user.

      - `ID string`

        Unique identifier for this event.

      - `Type BetaManagedAgentsUserInterruptEventType`

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

      A tool confirmation event that approves or denies a pending tool execution.

      - `ID string`

        Unique identifier for this event.

      - `Result BetaManagedAgentsUserToolConfirmationEventResult`

        UserToolConfirmationResult enum

        - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

        - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

      - `ToolUseID string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserToolConfirmationEventType`

      - `DenyMessage string Optional`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

      Event sent by the client providing the result of a custom tool execution.

      - `ID string`

        Unique identifier for this event.

      - `CustomToolUseID string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserCustomToolResultEventType`

      - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

          - `Citations BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `Enabled bool`

              Whether citations are enabled for this search result.

          - `Content []BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `Text string`

              The text content.

              minLength: 1

            - `Type BetaManagedAgentsSearchResultContentType`

          - `Source string`

            The URL source of the search result.

            minLength: 1

          - `Title string`

            The title of the search result.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultBlockType`

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `ID string`

        Unique identifier for this event.

      - `Description string`

        What the agent should produce. Copied from the input event.

      - `MaxIterations int64`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `OutcomeID string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `ProcessedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

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

      - `Type BetaManagedAgentsUserDefineOutcomeEventType`

    - `type BetaManagedAgentsUserToolResultEvent struct{…}`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `ID string`

        Unique identifier for this event.

      - `ToolUseID string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserToolResultEventType`

      - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `type BetaManagedAgentsSystemMessageEvent struct{…}`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `ID string`

        Unique identifier for this event.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsSystemMessageEventType`

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

## Example

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
	betaManagedAgentsSendSessionEvents, err := client.Beta.Sessions.Events.Send(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionEventSendParams{
			Events: []anthropic.BetaManagedAgentsEventParamsUnion{anthropic.BetaManagedAgentsEventParamsUnion{
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
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSendSessionEvents.Data)
}
```

### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```
