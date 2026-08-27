# List Events

`client.Beta.Sessions.Events.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionEventUnion], error)`

**GET** `/v1/sessions/{session_id}/events`

List Events

## Parameters

- `sessionID string`

- `params BetaSessionEventListParams`

  - `CreatedAtGt param.Field[Time] Optional`

    Query param: Return events created after this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `CreatedAtGte param.Field[Time] Optional`

    Query param: Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `CreatedAtLt param.Field[Time] Optional`

    Query param: Return events created before this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `CreatedAtLte param.Field[Time] Optional`

    Query param: Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `Limit param.Field[int64] Optional`

    Query param: Query parameter for limit

    format: int32

  - `Order param.Field[BetaSessionEventListParamsOrder] Optional`

    Query param: Sort direction for results, ordered by the event's `processed_at`. Defaults to asc (chronological).

    - `const BetaSessionEventListParamsOrderAsc BetaSessionEventListParamsOrder = "asc"`

    - `const BetaSessionEventListParamsOrderDesc BetaSessionEventListParamsOrder = "desc"`

  - `Page param.Field[string] Optional`

    Query param: Opaque pagination cursor from a previous response's next_page.

  - `Types param.Field[[]string] Optional`

    Query param: Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

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

## Returns

- `type BetaManagedAgentsSessionEventUnion interface{…}`

  Union type for all event types in a session.

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

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentMessageEventContentUnion`

      Array of text blocks comprising the agent response.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMessageEventType`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThinkingEventType`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion Optional`

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

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion Optional`

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

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

        - `Type BetaManagedAgentsUnknownErrorType`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsBillingErrorType`

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `CredentialID string`

          ID of the affected credential.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsCredentialHostUnreachableErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionErrorEventType`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

        format: int32

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

        format: int32

      - `InputTokens int64`

        Input tokens consumed by this request.

        format: int32

      - `OutputTokens int64`

        Output tokens generated by this request.

        format: int32

      - `Speed BetaManagedAgentsSpanModelUsageSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

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

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionDeletedEventType`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

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

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Name string`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `SkillID string`

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `SkillID string`

                - `Type BetaManagedAgentsCustomSkillType`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Enabled bool`

                    - `Name Bash`

                    - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                        - `Type BetaManagedAgentsAlwaysAskPolicyType`

                    - `Type Bash`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Edit`

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Read`

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Write`

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Glob`

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Grep`

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebFetch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebSearch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `UserLocation BetaManagedAgentsUserLocation Optional`

                      Approximate user location for search result localization.

                      - `Type Approximate`

                        Location precision. Only "approximate" is supported.

                      - `City string Optional`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Country string Optional`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Region string Optional`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Timezone string Optional`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `Type BetaManagedAgentsAgentToolset20260401Type`

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `MCPServerName string`

                - `Type BetaManagedAgentsMCPToolsetType`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

                - `Type BetaManagedAgentsCustomToolType`

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Model string`

              The advisor model id.

            - `Type BetaManagedAgentsAdvisorType`

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

      - `System string`

      - `Tools []BetaManagedAgentsSessionAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

        - `type BetaManagedAgentsMCPToolset struct{…}`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

      - `Type BetaManagedAgentsSessionAgentType`

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type BetaManagedAgentsBudgetLimitType`

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

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

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `Usage BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `ActiveSeconds float64 Optional`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Ephemeral1hInputTokens int64 Optional`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Ephemeral5mInputTokens int64 Optional`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `CacheReadInputTokens int64 Optional`

        Total tokens read from prompt cache.

        format: int32

      - `InputTokens int64 Optional`

        Total input tokens consumed across all turns.

        format: int32

      - `ListCost BetaMonetaryAmount Optional`

        A monetary amount in a specific currency.

      - `OutputTokens int64 Optional`

        Total output tokens generated across all turns.

        format: int32

      - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `WebFetchRequests int64 Optional`

          Number of server-executed web fetch requests.

          format: int32

        - `WebSearchRequests int64 Optional`

          Number of server-executed web search requests.

          format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

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
	page, err := client.Beta.Sessions.Events.List(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionEventListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
