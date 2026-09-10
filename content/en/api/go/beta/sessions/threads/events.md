---
title: Events
url: https://platform.claude.com/docs/en/api/go/beta/sessions/threads/events
---

# Events

## List Session Thread Events

`client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (*PageCursor[BetaManagedAgentsSessionEventUnion], error)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `threadID string`

- `params BetaSessionThreadEventListParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `Limit param.Field[int64] Optional`

    Query param: Query parameter for limit

    format: int32

  - `Page param.Field[string] Optional`

    Query param: Query parameter for page

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

      - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

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

  - `WorkspaceID param.Field[string] Optional`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `type BetaManagedAgentsSessionEventUnion interface{…}`

  Union type for all event types in a session.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `Type BetaManagedAgentsUserMessageEventType`

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Type BetaManagedAgentsTextBlockType`

        - `Text string`

          The text content.

          minLength: 1

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Type BetaManagedAgentsImageBlockType`

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Type BetaManagedAgentsBase64ImageSourceType`

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `Type BetaManagedAgentsFileImageSourceType`

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `Type BetaManagedAgentsFileDocumentSourceType`

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `Type BetaManagedAgentsUserInterruptEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        - `Type BetaManagedAgentsSearchResultBlockType`

        - `Citations BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `Enabled bool`

            Whether citations are enabled for this search result.

        - `Content []BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `Type BetaManagedAgentsSearchResultContentType`

          - `Text string`

            The text content.

            minLength: 1

        - `Source string`

          The URL source of the search result.

          minLength: 1

        - `Title string`

          The title of the search result.

          minLength: 1

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `Type BetaManagedAgentsAgentMessageEventType`

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

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `Type BetaManagedAgentsAgentThinkingEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

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

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `Evaluation BetaManagedAgentsAgentToolEvaluationUnion Optional`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `type BetaManagedAgentsAgentToolEvaluationAlwaysAllow struct{…}`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `Type AlwaysAllow`

      - `type BetaManagedAgentsAgentToolEvaluationAlwaysAsk struct{…}`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `Type AlwaysAsk`

      - `type BetaManagedAgentsAgentToolEvaluationAuto struct{…}`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `Type Auto`

        - `EvaluatedPermission BetaManagedAgentsAgentAutoEvaluatedPermissionUnion`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `type BetaManagedAgentsAgentAutoEvaluatedPermissionAllow struct{…}`

            The server judged the invocation safe to execute without client approval.

            - `Type Allow`

          - `type BetaManagedAgentsAgentAutoEvaluatedPermissionAsk struct{…}`

            The server reached no judgement; the invocation is held for client approval.

            - `Type Ask`

            - `ReasonCode string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `type BetaManagedAgentsAgentAutoEvaluatedPermissionDeny struct{…}`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `Type Deny`

            - `ReasonCode string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

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

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `Evaluation BetaManagedAgentsAgentToolEvaluationUnion Optional`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

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

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

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

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

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

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `Type BetaManagedAgentsSessionErrorEventType`

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Type BetaManagedAgentsUnknownErrorType`

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

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

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

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

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

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

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

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

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

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

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

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Type BetaManagedAgentsBillingErrorType`

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

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

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

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

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

        - `Type BetaManagedAgentsSessionRequiresActionType`

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

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

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

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

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

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

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

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

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

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

        - `Type BetaManagedAgentsFileRubricType`

        - `FileID string`

          ID of the rubric file.

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Type BetaManagedAgentsTextRubricType`

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `Type BetaManagedAgentsSessionDeletedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

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

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

  - `type BetaManagedAgentsUserToolResultEvent struct{…}`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `Type BetaManagedAgentsUserToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `Type BetaManagedAgentsSessionAgentType`

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `Name string`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeFable5_1 BetaManagedAgentsModel = "claude-fable-5-1"`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

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

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `Name string`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `SkillID string`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `Type BetaManagedAgentsCustomSkillType`

                - `SkillID string`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Type BetaManagedAgentsAgentToolset20260401Type`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Type Bash`

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

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `Type Auto`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Type Edit`

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Type Read`

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Type Write`

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Type Glob`

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Type Grep`

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Type WebFetch`

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Type WebSearch`

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `type BetaManagedAgentsAutoPolicy struct{…}`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Type BetaManagedAgentsMCPToolsetType`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                    - `type BetaManagedAgentsAutoPolicy struct{…}`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                    - `type BetaManagedAgentsAutoPolicy struct{…}`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `MCPServerName string`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Type BetaManagedAgentsCustomToolType`

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Type BetaManagedAgentsAdvisorType`

            - `Model string`

              The advisor model id.

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

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `Type BetaManagedAgentsBudgetLimitType`

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `Type BetaManagedAgentsSystemMessageEventType`

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Type BetaManagedAgentsSystemContentBlockType`

      - `Text string`

        The text content.

        minLength: 1

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

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
	page, err := client.Beta.Sessions.Threads.Events.List(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadEventListParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
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
  ],
  "next_page": "next_page"
}
```

## Stream Session Thread Events

`client.Beta.Sessions.Threads.Events.Stream(ctx, threadID, params) (*BetaManagedAgentsStreamSessionThreadEventsUnion, error)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `threadID string`

- `params BetaSessionThreadEventStreamParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `EventDeltas param.Field[[]BetaManagedAgentsDeltaType] Optional`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `const BetaManagedAgentsDeltaTypeAgentMessage BetaManagedAgentsDeltaType = "agent.message"`

    - `const BetaManagedAgentsDeltaTypeAgentThinking BetaManagedAgentsDeltaType = "agent.thinking"`

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

      - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

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

  - `WorkspaceID param.Field[string] Optional`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `type BetaManagedAgentsStreamSessionThreadEventsUnion interface{…}`

  Server-sent event in a single thread's stream.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `Type BetaManagedAgentsUserMessageEventType`

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Type BetaManagedAgentsTextBlockType`

        - `Text string`

          The text content.

          minLength: 1

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Type BetaManagedAgentsImageBlockType`

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Type BetaManagedAgentsBase64ImageSourceType`

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `Type BetaManagedAgentsFileImageSourceType`

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `Type BetaManagedAgentsFileDocumentSourceType`

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `Type BetaManagedAgentsUserInterruptEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        - `Type BetaManagedAgentsSearchResultBlockType`

        - `Citations BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `Enabled bool`

            Whether citations are enabled for this search result.

        - `Content []BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `Type BetaManagedAgentsSearchResultContentType`

          - `Text string`

            The text content.

            minLength: 1

        - `Source string`

          The URL source of the search result.

          minLength: 1

        - `Title string`

          The title of the search result.

          minLength: 1

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `Type BetaManagedAgentsAgentMessageEventType`

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

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `Type BetaManagedAgentsAgentThinkingEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

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

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `Evaluation BetaManagedAgentsAgentToolEvaluationUnion Optional`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `type BetaManagedAgentsAgentToolEvaluationAlwaysAllow struct{…}`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `Type AlwaysAllow`

      - `type BetaManagedAgentsAgentToolEvaluationAlwaysAsk struct{…}`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `Type AlwaysAsk`

      - `type BetaManagedAgentsAgentToolEvaluationAuto struct{…}`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `Type Auto`

        - `EvaluatedPermission BetaManagedAgentsAgentAutoEvaluatedPermissionUnion`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `type BetaManagedAgentsAgentAutoEvaluatedPermissionAllow struct{…}`

            The server judged the invocation safe to execute without client approval.

            - `Type Allow`

          - `type BetaManagedAgentsAgentAutoEvaluatedPermissionAsk struct{…}`

            The server reached no judgement; the invocation is held for client approval.

            - `Type Ask`

            - `ReasonCode string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `type BetaManagedAgentsAgentAutoEvaluatedPermissionDeny struct{…}`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `Type Deny`

            - `ReasonCode string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

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

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `Evaluation BetaManagedAgentsAgentToolEvaluationUnion Optional`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

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

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

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

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

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

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `Type BetaManagedAgentsSessionErrorEventType`

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Type BetaManagedAgentsUnknownErrorType`

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

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

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

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

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

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

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

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

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

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

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

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Type BetaManagedAgentsBillingErrorType`

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

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

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

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

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

        - `Type BetaManagedAgentsSessionRequiresActionType`

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

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

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

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

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

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

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

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

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

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

        - `Type BetaManagedAgentsFileRubricType`

        - `FileID string`

          ID of the rubric file.

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Type BetaManagedAgentsTextRubricType`

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `Type BetaManagedAgentsSessionDeletedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

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

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

  - `type BetaManagedAgentsUserToolResultEvent struct{…}`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `Type BetaManagedAgentsUserToolResultEventType`

    - `ID string`

      Unique identifier for this event.

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `Type BetaManagedAgentsSessionAgentType`

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `Name string`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeFable5_1 BetaManagedAgentsModel = "claude-fable-5-1"`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

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

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `Name string`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `SkillID string`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `Type BetaManagedAgentsCustomSkillType`

                - `SkillID string`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Type BetaManagedAgentsAgentToolset20260401Type`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Type Bash`

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

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `Type Auto`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Type Edit`

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Type Read`

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Type Write`

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Type Glob`

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Type Grep`

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Type WebFetch`

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Type WebSearch`

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                      - `type BetaManagedAgentsAutoPolicy struct{…}`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `type BetaManagedAgentsAutoPolicy struct{…}`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Type BetaManagedAgentsMCPToolsetType`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                    - `type BetaManagedAgentsAutoPolicy struct{…}`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                    - `type BetaManagedAgentsAutoPolicy struct{…}`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `MCPServerName string`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Type BetaManagedAgentsCustomToolType`

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Type BetaManagedAgentsAdvisorType`

            - `Model string`

              The advisor model id.

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

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `Type BetaManagedAgentsBudgetLimitType`

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsStartEvent struct{…}`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Type BetaManagedAgentsStartEventType`

    - `Event BetaManagedAgentsStartEventPreviewUnion`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `type BetaManagedAgentsAgentMessagePreview struct{…}`

        - `Type BetaManagedAgentsAgentMessagePreviewType`

        - `ID string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `type BetaManagedAgentsAgentThinkingPreview struct{…}`

        - `Type BetaManagedAgentsAgentThinkingPreviewType`

        - `ID string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `type BetaManagedAgentsDeltaEvent struct{…}`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Type BetaManagedAgentsDeltaEventType`

    - `Delta BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `Type BetaManagedAgentsDeltaContentType`

      - `Content BetaManagedAgentsTextBlock`

        Regular text content.

      - `Index int64 Optional`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `EventID string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `Type BetaManagedAgentsSystemMessageEventType`

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Type BetaManagedAgentsSystemContentBlockType`

      - `Text string`

        The text content.

        minLength: 1

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

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
	stream := client.Beta.Sessions.Threads.Events.StreamEvents(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadEventStreamParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
```

#### Response (200)

```json
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
```
