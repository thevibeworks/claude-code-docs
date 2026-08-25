# List Session Thread Events

`EventListPageResponse Beta.Sessions.Threads.Events.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

## Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

## Returns

- `class EventListPageResponse:`

  Paginated list of events for a single thread within a `session`.

  - `IReadOnlyList<BetaManagedAgentsSessionEvent> Data`

    Events for the thread, ordered by `processed_at`.

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks comprising the user message.

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

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `required string ID`

        Unique identifier for this event.

      - `required Type Type`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `Allow`

        - `Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `required BetaManagedAgentsSearchResultCitations Citations`

            Citation settings for a search result.

            - `required bool Enabled`

              Whether citations are enabled for this search result.

          - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

            Array of text content blocks from the search result.

            - `required string Text`

              The text content.

              minLength: 1

            - `required Type Type`

          - `required string Source`

            The URL source of the search result.

            minLength: 1

          - `required string Title`

            The title of the search result.

            minLength: 1

          - `required Type Type`

      - `bool? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsAgentCustomToolUseEvent:`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string Name`

        Name of the custom tool being called.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

    - `class BetaManagedAgentsAgentMessageEvent:`

      An agent response event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of text blocks comprising the agent response.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsAgentThinkingEvent:`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsAgentMcpToolUseEvent:`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string McpServerName`

        Name of the MCP server providing the tool.

      - `required string Name`

        Name of the MCP tool being used.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `EvaluatedPermission EvaluatedPermission`

        AgentEvaluatedPermission enum

        - `Allow`

        - `Ask`

        - `Deny`

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `class BetaManagedAgentsAgentMcpToolResultEvent:`

      Event representing the result of an MCP tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string McpToolUseID`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `bool? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsAgentToolUseEvent:`

      Event emitted when the agent invokes a built-in agent tool.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyDictionary<string, JsonElement> Input`

        Input parameters for the tool call.

      - `required string Name`

        Name of the agent tool being used.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `EvaluatedPermission EvaluatedPermission`

        AgentEvaluatedPermission enum

        - `Allow`

        - `Ask`

        - `Deny`

      - `string? SessionThreadID`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `class BetaManagedAgentsAgentToolResultEvent:`

      Event representing the result of an agent tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to.

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `bool? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

      Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Message content blocks.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

      - `required string FromSessionThreadID`

        Public `sthr_` ID of the thread that sent the message.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `string? FromAgentName`

        Name of the callable agent this message came from. Absent when received from the primary agent.

    - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

      Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Message content blocks.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string ToSessionThreadID`

        Public `sthr_` ID of the thread the message was sent to.

      - `required Type Type`

      - `string? ToAgentName`

        Name of the callable agent this message was sent to. Absent when sent to the primary agent.

    - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

      Indicates that context compaction (summarization) occurred during the session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSessionErrorEvent:`

      An error event indicating a problem occurred during session execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Error Error`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `class BetaManagedAgentsUnknownError:`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `required Type Type`

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `required Type Type`

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsModelOverloadedError:`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

        - `class BetaManagedAgentsModelRateLimitedError:`

          The model request was rate-limited.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

        - `class BetaManagedAgentsModelRequestFailedError:`

          A model request failed for a reason other than overload or rate-limiting.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

        - `class BetaManagedAgentsMcpConnectionFailedError:`

          Failed to connect to an MCP server.

          - `required string McpServerName`

            Name of the MCP server that failed to connect.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

        - `class BetaManagedAgentsMcpAuthenticationFailedError:`

          Authentication to an MCP server failed.

          - `required string McpServerName`

            Name of the MCP server that failed authentication.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

        - `class BetaManagedAgentsBillingError:`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

        - `class BetaManagedAgentsCredentialHostUnreachableError:`

          An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

          - `required string CredentialID`

            ID of the affected credential.

          - `required string Message`

            Human-readable error description.

          - `required RetryStatus RetryStatus`

            What the client should do next in response to this error.

            - `class BetaManagedAgentsRetryStatusRetrying:`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `class BetaManagedAgentsRetryStatusExhausted:`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `class BetaManagedAgentsRetryStatusTerminal:`

              The session encountered a terminal error and will transition to `terminated` state.

          - `required Type Type`

          - `required string VaultID`

            ID of the vault containing the affected credential.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSessionStatusRunningEvent:`

      Indicates the session is actively running and the agent is working.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSessionStatusIdleEvent:`

      Indicates the agent has paused and is awaiting user input.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required StopReason StopReason`

        The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionEndTurn:`

          The agent completed its turn naturally and is ready for the next user message.

          - `required Type Type`

        - `class BetaManagedAgentsSessionRequiresAction:`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `required IReadOnlyList<string> EventIds`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `required Type Type`

        - `class BetaManagedAgentsSessionRetriesExhausted:`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

          - `required Type Type`

        - `class BetaManagedAgentsSessionBudgetReached:`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

      Indicates the session has terminated, either due to an error or completion.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSessionThreadCreatedEvent:`

      Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the callable agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string SessionThreadID`

        Public `sthr_` ID of the newly created thread.

      - `required Type Type`

    - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

      Emitted when an outcome evaluation cycle begins.

      - `required string ID`

        Unique identifier for this event.

      - `required int Iteration`

        0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

        format: int32

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

      Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

      - `required string ID`

        Unique identifier for this event.

      - `required string Explanation`

        Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

      - `required int Iteration`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `required string OutcomeEvaluationStartID`

        The id of the corresponding `span.outcome_evaluation_start` event.

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Result`

        Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

      - `required Type Type`

      - `required BetaManagedAgentsSpanModelUsage Usage`

        Token usage for a single model request.

        - `required int CacheCreationInputTokens`

          Tokens used to create prompt cache in this request.

          format: int32

        - `required int CacheReadInputTokens`

          Tokens read from prompt cache in this request.

          format: int32

        - `required int InputTokens`

          Input tokens consumed by this request.

          format: int32

        - `required int OutputTokens`

          Output tokens generated by this request.

          format: int32

        - `Speed? Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

    - `class BetaManagedAgentsSpanModelRequestStartEvent:`

      Emitted when a model request is initiated by the agent.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSpanModelRequestEndEvent:`

      Emitted when a model request completes.

      - `required string ID`

        Unique identifier for this event.

      - `required bool? IsError`

        Whether the model request resulted in an error.

      - `required string ModelRequestStartID`

        The id of the corresponding `span.model_request_start` event.

      - `required BetaManagedAgentsSpanModelUsage ModelUsage`

        Token usage for a single model request.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

      Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

      - `required string ID`

        Unique identifier for this event.

      - `required int Iteration`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `required string OutcomeID`

        The `outc_` ID of the outcome being evaluated.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsUserDefineOutcomeEvent:`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `required string ID`

        Unique identifier for this event.

      - `required string Description`

        What the agent should produce. Copied from the input event.

      - `required int? MaxIterations`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `required string OutcomeID`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

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

    - `class BetaManagedAgentsSessionDeletedEvent:`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

      A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that started running.

      - `required Type Type`

    - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

      A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that went idle.

      - `required StopReason StopReason`

        The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionEndTurn:`

          The agent completed its turn naturally and is ready for the next user message.

        - `class BetaManagedAgentsSessionRequiresAction:`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `class BetaManagedAgentsSessionRetriesExhausted:`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `class BetaManagedAgentsSessionBudgetReached:`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `required Type Type`

    - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

      A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that terminated.

      - `required Type Type`

    - `class BetaManagedAgentsUserToolResultEvent:`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `required string ID`

        Unique identifier for this event.

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `bool? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

      A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `required string ID`

        Unique identifier for this event.

      - `required string AgentName`

        Name of the agent the thread runs.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string SessionThreadID`

        Public sthr_ ID of the thread that is retrying.

      - `required Type Type`

    - `class BetaManagedAgentsSessionUpdatedEvent:`

      Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `BetaManagedAgentsSessionAgent? Agent`

        Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

        - `required string ID`

        - `required string? Description`

        - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

          - `required string Name`

          - `required Type Type`

          - `required string Url`

        - `required BetaManagedAgentsModelConfig Model`

          Model identifier and configuration.

          - `required BetaManagedAgentsModel ID`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `ClaudeSonnet5`

              High-performance model for coding and agents

            - `ClaudeFable5`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `ClaudeOpus5`

              Powerful intelligence for long-running agents and coding

            - `ClaudeOpus4_8`

              Powerful intelligence for long-running agents and coding

            - `ClaudeOpus4_7`

              Powerful intelligence for long-running agents and coding

            - `ClaudeOpus4_6`

              Powerful intelligence for long-running agents and coding

            - `ClaudeSonnet4_6`

              Best combination of speed and intelligence

            - `ClaudeHaiku4_5`

              Fastest model with near-frontier intelligence

            - `ClaudeHaiku4_5_20251001`

              Fastest model with near-frontier intelligence

            - `ClaudeOpus4_5`

              Powerful intelligence for long-running agents and coding

            - `ClaudeOpus4_5_20251101`

              Powerful intelligence for long-running agents and coding

            - `ClaudeSonnet4_5`

              High-performance model for agents and coding

            - `ClaudeSonnet4_5_20250929`

              High-performance model for agents and coding

          - `Effort Effort`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `class BetaManagedAgentsEffortLow:`

              Low effort. Favors latency over reasoning depth.

              - `required Type Type`

            - `class BetaManagedAgentsEffortMedium:`

              Medium effort. Balances latency and reasoning depth.

              - `required Type Type`

            - `class BetaManagedAgentsEffortHigh:`

              High effort. Favors reasoning depth.

              - `required Type Type`

            - `class BetaManagedAgentsEffortXhigh:`

              Extra-high effort. Not all models accept this level.

              - `required Type Type`

            - `class BetaManagedAgentsEffortMax:`

              Maximum effort. Favors reasoning depth over latency.

              - `required Type Type`

          - `string InferenceGeo`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

          - `Speed Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `Standard`

            - `Fast`

        - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `required IReadOnlyList<Agent> Agents`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `class BetaManagedAgentsSessionThreadAgent:`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `required string ID`

              - `required string? Description`

              - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

                - `required string Name`

                - `required Type Type`

                - `required string Url`

              - `required BetaManagedAgentsModelConfig Model`

                Model identifier and configuration.

              - `required string Name`

              - `required IReadOnlyList<Skill> Skills`

                - `class BetaManagedAgentsAnthropicSkill:`

                  A resolved Anthropic-managed skill.

                  - `required string SkillID`

                  - `required Type Type`

                  - `required string Version`

                - `class BetaManagedAgentsCustomSkill:`

                  A resolved user-created custom skill.

                  - `required string SkillID`

                  - `required Type Type`

                  - `required string Version`

              - `required string? System`

              - `required IReadOnlyList<Tool> Tools`

                - `class BetaManagedAgentsAgentToolset20260401:`

                  - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                    - `class BetaManagedAgentsBashToolConfig:`

                      Configuration for the bash tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                          - `required Type Type`

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                          - `required Type Type`

                      - `JsonElement Type constant`

                    - `class BetaManagedAgentsEditToolConfig:`

                      Configuration for the edit tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                    - `class BetaManagedAgentsReadToolConfig:`

                      Configuration for the read tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                    - `class BetaManagedAgentsWriteToolConfig:`

                      Configuration for the write tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                    - `class BetaManagedAgentsGlobToolConfig:`

                      Configuration for the glob tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                    - `class BetaManagedAgentsGrepToolConfig:`

                      Configuration for the grep tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                    - `class BetaManagedAgentsWebFetchToolConfig:`

                      Configuration for the web_fetch tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                      - `IReadOnlyList<string> AllowedDomains`

                      - `IReadOnlyList<string> BlockedDomains`

                      - `int? MaxContentTokens`

                        format: int32

                    - `class BetaManagedAgentsWebSearchToolConfig:`

                      Configuration for the web_search tool.

                      - `required bool Enabled`

                      - `JsonElement Name constant`

                      - `required PermissionPolicy PermissionPolicy`

                        Permission policy for tool execution.

                        - `class BetaManagedAgentsAlwaysAllowPolicy:`

                          Tool calls are automatically approved without user confirmation.

                        - `class BetaManagedAgentsAlwaysAskPolicy:`

                          Tool calls require user confirmation before execution.

                      - `JsonElement Type constant`

                      - `IReadOnlyList<string> AllowedDomains`

                      - `IReadOnlyList<string> BlockedDomains`

                      - `BetaManagedAgentsUserLocation? UserLocation`

                        Approximate user location for search result localization.

                        - `JsonElement Type constant`

                          Location precision. Only "approximate" is supported.

                        - `string? City`

                          City name.

                          minLength: 1, maxLength: 255

                        - `string? Country`

                          Two-letter ISO 3166-1 country code, uppercase.

                        - `string? Region`

                          Region or state name.

                          minLength: 1, maxLength: 255

                        - `string? Timezone`

                          IANA timezone identifier, e.g. "America/Los_Angeles".

                          minLength: 1, maxLength: 255

                  - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                    Resolved default configuration for agent tools.

                    - `required bool Enabled`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                  - `required Type Type`

                - `class BetaManagedAgentsMcpToolset:`

                  - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                    - `required bool Enabled`

                    - `required string Name`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                  - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                    Resolved default configuration for all tools from an MCP server.

                    - `required bool Enabled`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                  - `required string McpServerName`

                  - `required Type Type`

                - `class BetaManagedAgentsCustomTool:`

                  A custom tool as returned in API responses.

                  - `required string Description`

                  - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                    JSON Schema for custom tool input parameters.

                    - `JsonElement Type constant`

                    - `IReadOnlyDictionary<string, JsonElement>? Properties`

                    - `IReadOnlyList<string>? Required`

                  - `required string Name`

                  - `required Type Type`

              - `required Type Type`

              - `required int Version`

                format: int32

            - `class BetaManagedAgentsAdvisor:`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `required string Model`

                The advisor model id.

              - `required Type Type`

          - `required Type Type`

        - `required string Name`

        - `required IReadOnlyList<Skill> Skills`

          - `class BetaManagedAgentsAnthropicSkill:`

            A resolved Anthropic-managed skill.

          - `class BetaManagedAgentsCustomSkill:`

            A resolved user-created custom skill.

        - `required string? System`

        - `required IReadOnlyList<Tool> Tools`

          - `class BetaManagedAgentsAgentToolset20260401:`

          - `class BetaManagedAgentsMcpToolset:`

          - `class BetaManagedAgentsCustomTool:`

            A custom tool as returned in API responses.

        - `required Type Type`

        - `required int Version`

          format: int32

      - `BetaManagedAgentsBudgetLimit? Budget`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `required BetaMonetaryAmount MaxListCost`

          A monetary amount in a specific currency.

          - `required string Amount`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `required BetaCurrency Currency`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `required Type Type`

      - `IReadOnlyDictionary<string, string> Metadata`

        The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

      - `string? Title`

        The session's new title. Present only when the update changed it.

    - `class BetaManagedAgentsSystemMessageEvent:`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsSessionUsageEvent:`

      Periodic snapshot of the session's cumulative usage and tracked list cost.

      - `required string ID`

        Unique identifier for this event.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

      - `required BetaManagedAgentsSessionUsageSnapshot Usage`

        Point-in-time snapshot of a session's cumulative usage.

        - `double ActiveSeconds`

          Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

          format: double

        - `BetaManagedAgentsCacheCreationUsage CacheCreation`

          Prompt-cache creation token usage broken down by cache lifetime.

          - `int Ephemeral1hInputTokens`

            Tokens used to create 1-hour ephemeral cache entries.

            format: int32

          - `int Ephemeral5mInputTokens`

            Tokens used to create 5-minute ephemeral cache entries.

            format: int32

        - `int CacheReadInputTokens`

          Total tokens read from prompt cache.

          format: int32

        - `int InputTokens`

          Total input tokens consumed across all turns.

          format: int32

        - `BetaMonetaryAmount ListCost`

          A monetary amount in a specific currency.

        - `int OutputTokens`

          Total output tokens generated across all turns.

          format: int32

        - `BetaManagedAgentsServerToolUsage ServerToolUse`

          Cumulative count of server-executed tool invocations, broken down by tool.

          - `int WebFetchRequests`

            Number of server-executed web fetch requests.

            format: int32

          - `int WebSearchRequests`

            Number of server-executed web search requests.

            format: int32

      - `BetaManagedAgentsBudgetLimit? Budget`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? NextPage`

    Opaque cursor for the next page. Null when no more results.

## Example

```csharp
EventListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var page = await client.Beta.Sessions.Threads.Events.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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
  ],
  "next_page": "next_page"
}
```
