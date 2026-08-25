# Events

## List Events

`EventListPage beta().sessions().events().list(params = EventListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/events`

List Events

### Parameters

- `EventListParams params`

  - `Optional<String> sessionId`

  - `Optional<LocalDateTime> createdAtGt`

    Return events created after this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `Optional<LocalDateTime> createdAtGte`

    Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `Optional<LocalDateTime> createdAtLt`

    Return events created before this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `Optional<LocalDateTime> createdAtLte`

    Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `Optional<Long> limit`

    Query parameter for limit

    format: int32

  - `Optional<Order> order`

    Sort direction for results, ordered by the event's `processed_at`. Defaults to asc (chronological).

    - `ASC("asc")`

    - `DESC("desc")`

  - `Optional<String> page`

    Opaque pagination cursor from a previous response's next_page.

  - `Optional<List<String>> types`

    Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsSessionEvent: union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.EventListPage;
import com.anthropic.models.beta.sessions.events.EventListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventListPage page = client.beta().sessions().events().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
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

## Send Events

`BetaManagedAgentsSendSessionEvents beta().sessions().events().send(params, requestOptions = RequestOptions.none())`

**POST** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `EventSendParams params`

  - `Optional<String> sessionId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

  - `List<BetaManagedAgentsEventParams> events`

    Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `Type type`

      - `Optional<String> sessionThreadId`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

      - `Result result`

        UserToolConfirmationResult enum

        - `ALLOW("allow")`

        - `DENY("deny")`

      - `String toolUseId`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<String> denyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

      - `String customToolUseId`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `BetaManagedAgentsSearchResultCitations citations`

            Citation settings for a search result.

            - `boolean enabled`

              Whether citations are enabled for this search result.

          - `List<BetaManagedAgentsSearchResultContent> content`

            Array of text content blocks from the search result.

            - `String text`

              The text content.

              minLength: 1

            - `Type type`

          - `String source`

            The URL source of the search result.

            minLength: 1

          - `String title`

            The title of the search result.

            minLength: 1

          - `Type type`

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsUserToolResultEventParams:`

      Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `String toolUseId`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

### Returns

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `Optional<List<Data>> data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `String id`

        Unique identifier for this event.

      - `List<Content> content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `String id`

        Unique identifier for this event.

      - `Type type`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `String id`

        Unique identifier for this event.

      - `Result result`

        UserToolConfirmationResult enum

        - `ALLOW("allow")`

        - `DENY("deny")`

      - `String toolUseId`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

      - `Optional<String> denyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `String id`

        Unique identifier for this event.

      - `String customToolUseId`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `BetaManagedAgentsSearchResultCitations citations`

            Citation settings for a search result.

            - `boolean enabled`

              Whether citations are enabled for this search result.

          - `List<BetaManagedAgentsSearchResultContent> content`

            Array of text content blocks from the search result.

            - `String text`

              The text content.

              minLength: 1

            - `Type type`

          - `String source`

            The URL source of the search result.

            minLength: 1

          - `String title`

            The title of the search result.

            minLength: 1

          - `Type type`

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsUserDefineOutcomeEvent:`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `String id`

        Unique identifier for this event.

      - `String description`

        What the agent should produce. Copied from the input event.

      - `Optional<Long> maxIterations`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `String outcomeId`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `LocalDateTime processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsUserToolResultEvent:`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `String id`

        Unique identifier for this event.

      - `String toolUseId`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSystemMessageEvent:`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `String id`

        Unique identifier for this event.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsSendSessionEvents;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsTextBlock;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsUserMessageEventParams;
import com.anthropic.models.beta.sessions.events.EventSendParams;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventSendParams params = EventSendParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .addUserMessageEvent(List.of(BetaManagedAgentsUserMessageEventParams.Content.ofText(BetaManagedAgentsTextBlock.builder()
                .text("Where is my order #1234?")
                .type(BetaManagedAgentsTextBlock.Type.TEXT)
                .build())))
            .build();
        BetaManagedAgentsSendSessionEvents betaManagedAgentsSendSessionEvents = client.beta().sessions().events().send(params);
    }
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
  ]
}
```

## Stream Events

`BetaManagedAgentsStreamSessionEvents beta().sessions().events().streamStreaming(params = EventStreamParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `EventStreamParams params`

  - `Optional<String> sessionId`

  - `Optional<List<BetaManagedAgentsDeltaType>> eventDeltas`

    When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `AGENT_MESSAGE("agent.message")`

    - `AGENT_THINKING("agent.thinking")`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `String id`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type type`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `String id`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `BetaManagedAgentsTextBlock content`

        Regular text content.

      - `Type type`

      - `Optional<Long> index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `String eventId`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsStreamSessionEvents;
import com.anthropic.models.beta.sessions.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<BetaManagedAgentsStreamSessionEvents> betaManagedAgentsStreamSessionEvents = client.beta().sessions().events().streamStreaming("sesn_011CZkZAtmR3yMPDzynEDxu7");
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

## Domain types

### Beta Managed Agents Agent Custom Tool Use Event

- `class BetaManagedAgentsAgentCustomToolUseEvent:`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `String id`

    Unique identifier for this event.

  - `Input input`

    Input parameters for the tool call.

  - `String name`

    Name of the custom tool being called.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

  - `Optional<String> sessionThreadId`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

### Beta Managed Agents Agent MCP Tool Result Event

- `class BetaManagedAgentsAgentMcpToolResultEvent:`

  Event representing the result of an MCP tool execution.

  - `String id`

    Unique identifier for this event.

  - `String mcpToolUseId`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock:`

      A block containing a web search result.

      - `BetaManagedAgentsSearchResultCitations citations`

        Citation settings for a search result.

        - `boolean enabled`

          Whether citations are enabled for this search result.

      - `List<BetaManagedAgentsSearchResultContent> content`

        Array of text content blocks from the search result.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `String source`

        The URL source of the search result.

        minLength: 1

      - `String title`

        The title of the search result.

        minLength: 1

      - `Type type`

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `class BetaManagedAgentsAgentMcpToolUseEvent:`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `String id`

    Unique identifier for this event.

  - `Input input`

    Input parameters for the tool call.

  - `String mcpServerName`

    Name of the MCP server providing the tool.

  - `String name`

    Name of the MCP tool being used.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

  - `Optional<EvaluatedPermission> evaluatedPermission`

    AgentEvaluatedPermission enum

    - `ALLOW("allow")`

    - `ASK("ask")`

    - `DENY("deny")`

  - `Optional<String> sessionThreadId`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Agent Message Event

- `class BetaManagedAgentsAgentMessageEvent:`

  An agent response event in the session conversation.

  - `String id`

    Unique identifier for this event.

  - `List<Content> content`

    Array of text blocks comprising the agent response.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsRedactedBlock:`

      Placeholder for content withheld by Anthropic model policy.

      - `Type type`

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Agent Thinking Event

- `class BetaManagedAgentsAgentThinkingEvent:`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Agent Thread Context Compacted Event

- `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

  Indicates that context compaction (summarization) occurred during the session.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Agent Thread Message Received Event

- `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

  Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

  - `String id`

    Unique identifier for this event.

  - `List<Content> content`

    Message content blocks.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsRedactedBlock:`

      Placeholder for content withheld by Anthropic model policy.

      - `Type type`

  - `String fromSessionThreadId`

    Public `sthr_` ID of the thread that sent the message.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

  - `Optional<String> fromAgentName`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `class BetaManagedAgentsAgentThreadMessageSentEvent:`

  Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

  - `String id`

    Unique identifier for this event.

  - `List<Content> content`

    Message content blocks.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsRedactedBlock:`

      Placeholder for content withheld by Anthropic model policy.

      - `Type type`

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String toSessionThreadId`

    Public `sthr_` ID of the thread the message was sent to.

  - `Type type`

  - `Optional<String> toAgentName`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Result Event

- `class BetaManagedAgentsAgentToolResultEvent:`

  Event representing the result of an agent tool execution.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String toolUseId`

    The id of the `agent.tool_use` event this result corresponds to.

  - `Type type`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock:`

      A block containing a web search result.

      - `BetaManagedAgentsSearchResultCitations citations`

        Citation settings for a search result.

        - `boolean enabled`

          Whether citations are enabled for this search result.

      - `List<BetaManagedAgentsSearchResultContent> content`

        Array of text content blocks from the search result.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `String source`

        The URL source of the search result.

        minLength: 1

      - `String title`

        The title of the search result.

        minLength: 1

      - `Type type`

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class BetaManagedAgentsAgentToolUseEvent:`

  Event emitted when the agent invokes a built-in agent tool.

  - `String id`

    Unique identifier for this event.

  - `Input input`

    Input parameters for the tool call.

  - `String name`

    Name of the agent tool being used.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

  - `Optional<EvaluatedPermission> evaluatedPermission`

    AgentEvaluatedPermission enum

    - `ALLOW("allow")`

    - `ASK("ask")`

    - `DENY("deny")`

  - `Optional<String> sessionThreadId`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Base64 Document Source

- `class BetaManagedAgentsBase64DocumentSource:`

  Base64-encoded document data.

  - `String data`

    Base64-encoded document data.

    minLength: 1

  - `String mediaType`

    MIME type of the document (e.g., "application/pdf").

    minLength: 1

  - `Type type`

### Beta Managed Agents Base64 Image Source

- `class BetaManagedAgentsBase64ImageSource:`

  Base64-encoded image data.

  - `String data`

    Base64-encoded image data.

    minLength: 1

  - `String mediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

    minLength: 1

  - `Type type`

### Beta Managed Agents Billing Error

- `class BetaManagedAgentsBillingError:`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents Credential Host Unreachable Error

- `class BetaManagedAgentsCredentialHostUnreachableError:`

  An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

  - `String credentialId`

    ID of the affected credential.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

  - `String vaultId`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `class BetaManagedAgentsDocumentBlock:`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `Source source`

    Union type for document source variants.

    - `class BetaManagedAgentsBase64DocumentSource:`

      Base64-encoded document data.

      - `String data`

        Base64-encoded document data.

        minLength: 1

      - `String mediaType`

        MIME type of the document (e.g., "application/pdf").

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsPlainTextDocumentSource:`

      Plain text document content.

      - `String data`

        The plain text content.

        minLength: 1

      - `MediaType mediaType`

        MIME type of the text content. Must be "text/plain".

      - `Type type`

    - `class BetaManagedAgentsUrlDocumentSource:`

      Document referenced by URL.

      - `Type type`

      - `String url`

        URL of the document to fetch.

        minLength: 1

    - `class BetaManagedAgentsFileDocumentSource:`

      Document referenced by file ID.

      - `String fileId`

        ID of a previously uploaded file.

        minLength: 1

      - `Type type`

  - `Type type`

  - `Optional<String> context`

    Additional context about the document for the model.

  - `Optional<String> title`

    The title of the document.

### Beta Managed Agents Event Params

- `class BetaManagedAgentsEventParams: union`

  Union type for event parameters that can be sent to a session.

  - `class BetaManagedAgentsUserMessageEventParams:`

    Parameters for sending a user message to the session.

    - `List<Content> content`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsUserInterruptEventParams:`

    Parameters for sending an interrupt to pause the agent.

    - `Type type`

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEventParams:`

    Parameters for confirming or denying a tool execution request.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `class BetaManagedAgentsUserCustomToolResultEventParams:`

    Parameters for providing the result of a custom tool execution.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `String description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubricParams:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `Type type`

    - `Type type`

    - `Optional<Long> maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsUserToolResultEventParams:`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsSystemMessageEventParams:`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

### Beta Managed Agents File Document Source

- `class BetaManagedAgentsFileDocumentSource:`

  Document referenced by file ID.

  - `String fileId`

    ID of a previously uploaded file.

    minLength: 1

  - `Type type`

### Beta Managed Agents File Image Source

- `class BetaManagedAgentsFileImageSource:`

  Image referenced by file ID.

  - `String fileId`

    ID of a previously uploaded file.

    minLength: 1

  - `Type type`

### Beta Managed Agents File Rubric

- `class BetaManagedAgentsFileRubric:`

  Rubric referenced by a file uploaded via the Files API.

  - `String fileId`

    ID of the rubric file.

  - `Type type`

### Beta Managed Agents File Rubric Params

- `class BetaManagedAgentsFileRubricParams:`

  Rubric referenced by a file uploaded via the Files API.

  - `String fileId`

    ID of the rubric file.

  - `Type type`

### Beta Managed Agents Image Block

- `class BetaManagedAgentsImageBlock:`

  Image content specified directly as base64 data or as a reference via a URL.

  - `Source source`

    Union type for image source variants.

    - `class BetaManagedAgentsBase64ImageSource:`

      Base64-encoded image data.

      - `String data`

        Base64-encoded image data.

        minLength: 1

      - `String mediaType`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsUrlImageSource:`

      Image referenced by URL.

      - `Type type`

      - `String url`

        URL of the image to fetch.

        minLength: 1

    - `class BetaManagedAgentsFileImageSource:`

      Image referenced by file ID.

      - `String fileId`

        ID of a previously uploaded file.

        minLength: 1

      - `Type type`

  - `Type type`

### Beta Managed Agents MCP Authentication Failed Error

- `class BetaManagedAgentsMcpAuthenticationFailedError:`

  Authentication to an MCP server failed.

  - `String mcpServerName`

    Name of the MCP server that failed authentication.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents MCP Connection Failed Error

- `class BetaManagedAgentsMcpConnectionFailedError:`

  Failed to connect to an MCP server.

  - `String mcpServerName`

    Name of the MCP server that failed to connect.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents Model Overloaded Error

- `class BetaManagedAgentsModelOverloadedError:`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents Model Rate Limited Error

- `class BetaManagedAgentsModelRateLimitedError:`

  The model request was rate-limited.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents Model Request Failed Error

- `class BetaManagedAgentsModelRequestFailedError:`

  A model request failed for a reason other than overload or rate-limiting.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents Plain Text Document Source

- `class BetaManagedAgentsPlainTextDocumentSource:`

  Plain text document content.

  - `String data`

    The plain text content.

    minLength: 1

  - `MediaType mediaType`

    MIME type of the text content. Must be "text/plain".

  - `Type type`

### Beta Managed Agents Redacted Block

- `class BetaManagedAgentsRedactedBlock:`

  Placeholder for content withheld by Anthropic model policy.

  - `Type type`

### Beta Managed Agents Retry Status Exhausted

- `class BetaManagedAgentsRetryStatusExhausted:`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `Type type`

### Beta Managed Agents Retry Status Retrying

- `class BetaManagedAgentsRetryStatusRetrying:`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `Type type`

### Beta Managed Agents Retry Status Terminal

- `class BetaManagedAgentsRetryStatusTerminal:`

  The session encountered a terminal error and will transition to `terminated` state.

  - `Type type`

### Beta Managed Agents Search Result Block

- `class BetaManagedAgentsSearchResultBlock:`

  A block containing a web search result.

  - `BetaManagedAgentsSearchResultCitations citations`

    Citation settings for a search result.

    - `boolean enabled`

      Whether citations are enabled for this search result.

  - `List<BetaManagedAgentsSearchResultContent> content`

    Array of text content blocks from the search result.

    - `String text`

      The text content.

      minLength: 1

    - `Type type`

  - `String source`

    The URL source of the search result.

    minLength: 1

  - `String title`

    The title of the search result.

    minLength: 1

  - `Type type`

### Beta Managed Agents Search Result Citations

- `class BetaManagedAgentsSearchResultCitations:`

  Citation settings for a search result.

  - `boolean enabled`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `class BetaManagedAgentsSearchResultContent:`

  Text content within a search result.

  - `String text`

    The text content.

    minLength: 1

  - `Type type`

### Beta Managed Agents Send Session Events

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `Optional<List<Data>> data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `String id`

        Unique identifier for this event.

      - `List<Content> content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `String id`

        Unique identifier for this event.

      - `Type type`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `String id`

        Unique identifier for this event.

      - `Result result`

        UserToolConfirmationResult enum

        - `ALLOW("allow")`

        - `DENY("deny")`

      - `String toolUseId`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

      - `Optional<String> denyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `String id`

        Unique identifier for this event.

      - `String customToolUseId`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `BetaManagedAgentsSearchResultCitations citations`

            Citation settings for a search result.

            - `boolean enabled`

              Whether citations are enabled for this search result.

          - `List<BetaManagedAgentsSearchResultContent> content`

            Array of text content blocks from the search result.

            - `String text`

              The text content.

              minLength: 1

            - `Type type`

          - `String source`

            The URL source of the search result.

            minLength: 1

          - `String title`

            The title of the search result.

            minLength: 1

          - `Type type`

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsUserDefineOutcomeEvent:`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `String id`

        Unique identifier for this event.

      - `String description`

        What the agent should produce. Copied from the input event.

      - `Optional<Long> maxIterations`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `String outcomeId`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `LocalDateTime processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsUserToolResultEvent:`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `String id`

        Unique identifier for this event.

      - `String toolUseId`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type type`

      - `Optional<List<Content>> content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `Optional<Boolean> isError`

        Whether the tool execution resulted in an error.

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<String> sessionThreadId`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSystemMessageEvent:`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `String id`

        Unique identifier for this event.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

      - `Optional<LocalDateTime> processedAt`

        A timestamp in RFC 3339 format

        format: date-time

### Beta Managed Agents Session Budget Reached

- `class BetaManagedAgentsSessionBudgetReached:`

  The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `Type type`

### Beta Managed Agents Session Deleted Event

- `class BetaManagedAgentsSessionDeletedEvent:`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Session End Turn

- `class BetaManagedAgentsSessionEndTurn:`

  The agent completed its turn naturally and is ready for the next user message.

  - `Type type`

### Beta Managed Agents Session Error Event

- `class BetaManagedAgentsSessionErrorEvent:`

  An error event indicating a problem occurred during session execution.

  - `String id`

    Unique identifier for this event.

  - `Error error`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `class BetaManagedAgentsUnknownError:`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `Type type`

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `Type type`

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsModelOverloadedError:`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

    - `class BetaManagedAgentsModelRateLimitedError:`

      The model request was rate-limited.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

    - `class BetaManagedAgentsModelRequestFailedError:`

      A model request failed for a reason other than overload or rate-limiting.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

    - `class BetaManagedAgentsMcpConnectionFailedError:`

      Failed to connect to an MCP server.

      - `String mcpServerName`

        Name of the MCP server that failed to connect.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

    - `class BetaManagedAgentsMcpAuthenticationFailedError:`

      Authentication to an MCP server failed.

      - `String mcpServerName`

        Name of the MCP server that failed authentication.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

    - `class BetaManagedAgentsBillingError:`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

    - `class BetaManagedAgentsCredentialHostUnreachableError:`

      An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

      - `String credentialId`

        ID of the affected credential.

      - `String message`

        Human-readable error description.

      - `RetryStatus retryStatus`

        What the client should do next in response to this error.

        - `class BetaManagedAgentsRetryStatusRetrying:`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `class BetaManagedAgentsRetryStatusExhausted:`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `class BetaManagedAgentsRetryStatusTerminal:`

          The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

      - `String vaultId`

        ID of the vault containing the affected credential.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Session Event

- `class BetaManagedAgentsSessionEvent: union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Beta Managed Agents Session Requires Action

- `class BetaManagedAgentsSessionRequiresAction:`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `List<String> eventIds`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `Type type`

### Beta Managed Agents Session Retries Exhausted

- `class BetaManagedAgentsSessionRetriesExhausted:`

  The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

  - `Type type`

### Beta Managed Agents Session Status Idle Event

- `class BetaManagedAgentsSessionStatusIdleEvent:`

  Indicates the agent has paused and is awaiting user input.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn:`

      The agent completed its turn naturally and is ready for the next user message.

      - `Type type`

    - `class BetaManagedAgentsSessionRequiresAction:`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `List<String> eventIds`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `Type type`

    - `class BetaManagedAgentsSessionRetriesExhausted:`

      The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `Type type`

    - `class BetaManagedAgentsSessionBudgetReached:`

      The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `Type type`

  - `Type type`

### Beta Managed Agents Session Status Rescheduled Event

- `class BetaManagedAgentsSessionStatusRescheduledEvent:`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Session Status Running Event

- `class BetaManagedAgentsSessionStatusRunningEvent:`

  Indicates the session is actively running and the agent is working.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Session Status Terminated Event

- `class BetaManagedAgentsSessionStatusTerminatedEvent:`

  Indicates the session has terminated, either due to an error or completion.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Session Thread Created Event

- `class BetaManagedAgentsSessionThreadCreatedEvent:`

  Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

  - `String id`

    Unique identifier for this event.

  - `String agentName`

    Name of the callable agent the thread runs.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String sessionThreadId`

    Public `sthr_` ID of the newly created thread.

  - `Type type`

### Beta Managed Agents Session Thread Status Idle Event

- `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

  A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `String id`

    Unique identifier for this event.

  - `String agentName`

    Name of the agent the thread runs.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String sessionThreadId`

    Public sthr_ ID of the thread that went idle.

  - `StopReason stopReason`

    The agent completed its turn naturally and is ready for the next user message.

    - `class BetaManagedAgentsSessionEndTurn:`

      The agent completed its turn naturally and is ready for the next user message.

      - `Type type`

    - `class BetaManagedAgentsSessionRequiresAction:`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `List<String> eventIds`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `Type type`

    - `class BetaManagedAgentsSessionRetriesExhausted:`

      The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `Type type`

    - `class BetaManagedAgentsSessionBudgetReached:`

      The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `Type type`

  - `Type type`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

  A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `String id`

    Unique identifier for this event.

  - `String agentName`

    Name of the agent the thread runs.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String sessionThreadId`

    Public sthr_ ID of the thread that is retrying.

  - `Type type`

### Beta Managed Agents Session Thread Status Running Event

- `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

  A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `String id`

    Unique identifier for this event.

  - `String agentName`

    Name of the agent the thread runs.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String sessionThreadId`

    Public sthr_ ID of the thread that started running.

  - `Type type`

### Beta Managed Agents Session Thread Status Terminated Event

- `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

  A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `String id`

    Unique identifier for this event.

  - `String agentName`

    Name of the agent the thread runs.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String sessionThreadId`

    Public sthr_ ID of the thread that terminated.

  - `Type type`

### Beta Managed Agents Session Usage Snapshot

- `class BetaManagedAgentsSessionUsageSnapshot:`

  Point-in-time snapshot of a session's cumulative usage.

  - `Optional<Double> activeSeconds`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

    format: double

  - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `Optional<Long> ephemeral1hInputTokens`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `Optional<Long> ephemeral5mInputTokens`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `Optional<Long> cacheReadInputTokens`

    Total tokens read from prompt cache.

    format: int32

  - `Optional<Long> inputTokens`

    Total input tokens consumed across all turns.

    format: int32

  - `Optional<BetaMonetaryAmount> listCost`

    A monetary amount in a specific currency.

    - `String amount`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `BetaCurrency currency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `Optional<Long> outputTokens`

    Total output tokens generated across all turns.

    format: int32

  - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `Optional<Long> webFetchRequests`

      Number of server-executed web fetch requests.

      format: int32

    - `Optional<Long> webSearchRequests`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Span Model Request End Event

- `class BetaManagedAgentsSpanModelRequestEndEvent:`

  Emitted when a model request completes.

  - `String id`

    Unique identifier for this event.

  - `Optional<Boolean> isError`

    Whether the model request resulted in an error.

  - `String modelRequestStartId`

    The id of the corresponding `span.model_request_start` event.

  - `BetaManagedAgentsSpanModelUsage modelUsage`

    Token usage for a single model request.

    - `long cacheCreationInputTokens`

      Tokens used to create prompt cache in this request.

      format: int32

    - `long cacheReadInputTokens`

      Tokens read from prompt cache in this request.

      format: int32

    - `long inputTokens`

      Input tokens consumed by this request.

      format: int32

    - `long outputTokens`

      Output tokens generated by this request.

      format: int32

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Span Model Request Start Event

- `class BetaManagedAgentsSpanModelRequestStartEvent:`

  Emitted when a model request is initiated by the agent.

  - `String id`

    Unique identifier for this event.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Span Model Usage

- `class BetaManagedAgentsSpanModelUsage:`

  Token usage for a single model request.

  - `long cacheCreationInputTokens`

    Tokens used to create prompt cache in this request.

    format: int32

  - `long cacheReadInputTokens`

    Tokens read from prompt cache in this request.

    format: int32

  - `long inputTokens`

    Input tokens consumed by this request.

    format: int32

  - `long outputTokens`

    Output tokens generated by this request.

    format: int32

  - `Optional<Speed> speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `STANDARD("standard")`

    - `FAST("fast")`

### Beta Managed Agents Span Outcome Evaluation End Event

- `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

  Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

  - `String id`

    Unique identifier for this event.

  - `String explanation`

    Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

  - `long iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    format: int32

  - `String outcomeEvaluationStartId`

    The id of the corresponding `span.outcome_evaluation_start` event.

  - `String outcomeId`

    The `outc_` ID of the outcome being evaluated.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String result`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `Type type`

  - `BetaManagedAgentsSpanModelUsage usage`

    Token usage for a single model request.

    - `long cacheCreationInputTokens`

      Tokens used to create prompt cache in this request.

      format: int32

    - `long cacheReadInputTokens`

      Tokens read from prompt cache in this request.

      format: int32

    - `long inputTokens`

      Input tokens consumed by this request.

      format: int32

    - `long outputTokens`

      Output tokens generated by this request.

      format: int32

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

  Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

  - `String id`

    Unique identifier for this event.

  - `long iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    format: int32

  - `String outcomeId`

    The `outc_` ID of the outcome being evaluated.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Span Outcome Evaluation Start Event

- `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

  Emitted when an outcome evaluation cycle begins.

  - `String id`

    Unique identifier for this event.

  - `long iteration`

    0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    format: int32

  - `String outcomeId`

    The `outc_` ID of the outcome being evaluated.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

### Beta Managed Agents Stream Session Events

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `String id`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type type`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `String id`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `BetaManagedAgentsTextBlock content`

        Regular text content.

      - `Type type`

      - `Optional<Long> index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `String eventId`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Beta Managed Agents System Message Event Params

- `class BetaManagedAgentsSystemMessageEventParams:`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

  - `List<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

    - `String text`

      The text content.

      minLength: 1

    - `Type type`

  - `Type type`

### Beta Managed Agents Text Block

- `class BetaManagedAgentsTextBlock:`

  Regular text content.

  - `String text`

    The text content.

    minLength: 1

  - `Type type`

### Beta Managed Agents Text Rubric

- `class BetaManagedAgentsTextRubric:`

  Rubric content provided inline as text.

  - `String content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `Type type`

### Beta Managed Agents Text Rubric Params

- `class BetaManagedAgentsTextRubricParams:`

  Rubric content provided inline as text.

  - `String content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

    maxLength: 262144

  - `Type type`

### Beta Managed Agents Unknown Error

- `class BetaManagedAgentsUnknownError:`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `String message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

    - `class BetaManagedAgentsRetryStatusRetrying:`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusExhausted:`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `Type type`

    - `class BetaManagedAgentsRetryStatusTerminal:`

      The session encountered a terminal error and will transition to `terminated` state.

      - `Type type`

  - `Type type`

### Beta Managed Agents URL Document Source

- `class BetaManagedAgentsUrlDocumentSource:`

  Document referenced by URL.

  - `Type type`

  - `String url`

    URL of the document to fetch.

    minLength: 1

### Beta Managed Agents URL Image Source

- `class BetaManagedAgentsUrlImageSource:`

  Image referenced by URL.

  - `Type type`

  - `String url`

    URL of the image to fetch.

    minLength: 1

### Beta Managed Agents User Custom Tool Result Event

- `class BetaManagedAgentsUserCustomToolResultEvent:`

  Event sent by the client providing the result of a custom tool execution.

  - `String id`

    Unique identifier for this event.

  - `String customToolUseId`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock:`

      A block containing a web search result.

      - `BetaManagedAgentsSearchResultCitations citations`

        Citation settings for a search result.

        - `boolean enabled`

          Whether citations are enabled for this search result.

      - `List<BetaManagedAgentsSearchResultContent> content`

        Array of text content blocks from the search result.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `String source`

        The URL source of the search result.

        minLength: 1

      - `String title`

        The title of the search result.

        minLength: 1

      - `Type type`

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> sessionThreadId`

    Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

### Beta Managed Agents User Custom Tool Result Event Params

- `class BetaManagedAgentsUserCustomToolResultEventParams:`

  Parameters for providing the result of a custom tool execution.

  - `String customToolUseId`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `Type type`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock:`

      A block containing a web search result.

      - `BetaManagedAgentsSearchResultCitations citations`

        Citation settings for a search result.

        - `boolean enabled`

          Whether citations are enabled for this search result.

      - `List<BetaManagedAgentsSearchResultContent> content`

        Array of text content blocks from the search result.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `String source`

        The URL source of the search result.

        minLength: 1

      - `String title`

        The title of the search result.

        minLength: 1

      - `Type type`

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

- `class BetaManagedAgentsUserDefineOutcomeEvent:`

  Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

  - `String id`

    Unique identifier for this event.

  - `String description`

    What the agent should produce. Copied from the input event.

  - `Optional<Long> maxIterations`

    Evaluate-then-revise cycles before giving up. Default 3, max 20.

    format: int32

  - `String outcomeId`

    Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

  - `LocalDateTime processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubric:`

      Rubric referenced by a file uploaded via the Files API.

      - `String fileId`

        ID of the rubric file.

      - `Type type`

    - `class BetaManagedAgentsTextRubric:`

      Rubric content provided inline as text.

      - `String content`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `Type type`

  - `Type type`

### Beta Managed Agents User Define Outcome Event Params

- `class BetaManagedAgentsUserDefineOutcomeEventParams:`

  Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

  - `String description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

    - `class BetaManagedAgentsFileRubricParams:`

      Rubric referenced by a file uploaded via the Files API.

      - `String fileId`

        ID of the rubric file.

      - `Type type`

    - `class BetaManagedAgentsTextRubricParams:`

      Rubric content provided inline as text.

      - `String content`

        Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        maxLength: 262144

      - `Type type`

  - `Type type`

  - `Optional<Long> maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

    format: int32

### Beta Managed Agents User Interrupt Event

- `class BetaManagedAgentsUserInterruptEvent:`

  An interrupt event that pauses agent execution and returns control to the user.

  - `String id`

    Unique identifier for this event.

  - `Type type`

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> sessionThreadId`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Interrupt Event Params

- `class BetaManagedAgentsUserInterruptEventParams:`

  Parameters for sending an interrupt to pause the agent.

  - `Type type`

  - `Optional<String> sessionThreadId`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Message Event

- `class BetaManagedAgentsUserMessageEvent:`

  A user message event in the session conversation.

  - `String id`

    Unique identifier for this event.

  - `List<Content> content`

    Array of content blocks comprising the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsRedactedBlock:`

      Placeholder for content withheld by Anthropic model policy.

      - `Type type`

  - `Type type`

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents User Message Event Params

- `class BetaManagedAgentsUserMessageEventParams:`

  Parameters for sending a user message to the session.

  - `List<Content> content`

    Array of content blocks for the user message.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsRedactedBlock:`

      Placeholder for content withheld by Anthropic model policy.

      - `Type type`

  - `Type type`

### Beta Managed Agents User Tool Confirmation Event

- `class BetaManagedAgentsUserToolConfirmationEvent:`

  A tool confirmation event that approves or denies a pending tool execution.

  - `String id`

    Unique identifier for this event.

  - `Result result`

    UserToolConfirmationResult enum

    - `ALLOW("allow")`

    - `DENY("deny")`

  - `String toolUseId`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type type`

  - `Optional<String> denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    maxLength: 10000

  - `Optional<LocalDateTime> processedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> sessionThreadId`

    When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

### Beta Managed Agents User Tool Confirmation Event Params

- `class BetaManagedAgentsUserToolConfirmationEventParams:`

  Parameters for confirming or denying a tool execution request.

  - `Result result`

    UserToolConfirmationResult enum

    - `ALLOW("allow")`

    - `DENY("deny")`

  - `String toolUseId`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `Type type`

  - `Optional<String> denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    maxLength: 10000

### Beta Managed Agents User Tool Result Event Params

- `class BetaManagedAgentsUserToolResultEventParams:`

  Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `String toolUseId`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `Type type`

  - `Optional<List<Content>> content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `String data`

            Base64-encoded image data.

            minLength: 1

          - `String mediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `Type type`

          - `String url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `String data`

            Base64-encoded document data.

            minLength: 1

          - `String mediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `String data`

            The plain text content.

            minLength: 1

          - `MediaType mediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `Type type`

          - `String url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `String fileId`

            ID of a previously uploaded file.

            minLength: 1

          - `Type type`

      - `Type type`

      - `Optional<String> context`

        Additional context about the document for the model.

      - `Optional<String> title`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock:`

      A block containing a web search result.

      - `BetaManagedAgentsSearchResultCitations citations`

        Citation settings for a search result.

        - `boolean enabled`

          Whether citations are enabled for this search result.

      - `List<BetaManagedAgentsSearchResultContent> content`

        Array of text content blocks from the search result.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `String source`

        The URL source of the search result.

        minLength: 1

      - `String title`

        The title of the search result.

        minLength: 1

      - `Type type`

  - `Optional<Boolean> isError`

    Whether the tool execution resulted in an error.
