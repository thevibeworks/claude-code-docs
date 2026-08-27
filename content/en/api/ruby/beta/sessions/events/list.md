# List Events

`beta.sessions.events.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/events`

List Events

## Parameters

- `session_id: String`

- `created_at_gt: Time`

  Return events created after this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `created_at_gte: Time`

  Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `created_at_lt: Time`

  Return events created before this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `created_at_lte: Time`

  Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `limit: Integer`

  Query parameter for limit

  format: int32

- `order: :asc | :desc`

  Sort direction for results, ordered by the event's `processed_at`. Defaults to asc (chronological).

  - `:asc`

  - `:desc`

- `page: String`

  Opaque pagination cursor from a previous response's next_page.

- `types: Array[String]`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

## Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 32 more`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

              minLength: 1

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

              minLength: 1

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

              minLength: 1

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: :text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: :redacted`

    - `type: :"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: Array[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `source: String`

          The URL source of the search result.

          minLength: 1

        - `title: String`

          The title of the search result.

          minLength: 1

        - `type: :search_result`

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.custom_tool_use"`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: String`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thread_message_received"`

    - `from_agent_name: String`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: String`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: :"agent.thread_message_sent"`

    - `to_agent_name: String`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

        - `type: :unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :billing_error`

      - `class BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: String`

          ID of the affected credential.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :credential_host_unreachable_error`

        - `vault_id: String`

          ID of the vault containing the affected credential.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: :retries_exhausted`

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: :budget_reached`

    - `type: :"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the callable agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public `sthr_` ID of the newly created thread.

    - `type: :"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

    - `id: String`

      Unique identifier for this event.

    - `iteration: Integer`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: String`

      Unique identifier for this event.

    - `explanation: String`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: Integer`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: String`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: String`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: :"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: Integer`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: Integer`

        Output tokens generated by this request.

        format: int32

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: String`

      Unique identifier for this event.

    - `iteration: Integer`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: String`

      Unique identifier for this event.

    - `description: String`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Integer`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: String`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

      - `class BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: :text`

    - `type: :"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that started running.

    - `type: :"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: :"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that terminated.

    - `type: :"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: String`

      Unique identifier for this event.

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that is retrying.

    - `type: :"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.updated"`

    - `agent: BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array[BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: String`

            - `description: String`

            - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

              - `name: String`

              - `type: :url`

              - `url: String`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: String`

            - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

              - `class BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: String`

                - `type: :anthropic`

                - `version: String`

              - `class BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: String`

                - `type: :custom`

                - `version: String`

            - `system_: String`

            - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

              - `class BetaManagedAgentsAgentToolset20260401`

                - `configs: Array[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: bool`

                    - `name: :bash`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: :always_allow`

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: :always_ask`

                    - `type: :bash`

                  - `class BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: bool`

                    - `name: :edit`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :edit`

                  - `class BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: bool`

                    - `name: :read`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :read`

                  - `class BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: bool`

                    - `name: :write`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :write`

                  - `class BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: bool`

                    - `name: :glob`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :glob`

                  - `class BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: bool`

                    - `name: :grep`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :grep`

                  - `class BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: bool`

                    - `name: :web_fetch`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_fetch`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `max_content_tokens: Integer`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: bool`

                    - `name: :web_search`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_search`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `user_location: BetaManagedAgentsUserLocation`

                      Approximate user location for search result localization.

                      - `type: :approximate`

                        Location precision. Only "approximate" is supported.

                      - `city: String`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: String`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: String`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: String`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: :agent_toolset_20260401`

              - `class BetaManagedAgentsMCPToolset`

                - `configs: Array[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: String`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: String`

                - `type: :mcp_toolset`

              - `class BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: String`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: :object`

                  - `properties: Hash[Symbol, untyped]`

                  - `required: Array[String]`

                - `name: String`

                - `type: :custom`

            - `type: :agent`

            - `version: Integer`

              format: int32

          - `class BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: String`

              The advisor model id.

            - `type: :advisor`

        - `type: :coordinator`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

        - `class BetaManagedAgentsMCPToolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: String`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: :limit`

    - `metadata: Hash[Symbol, String]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: String`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: String`

        The text content.

        minLength: 1

      - `type: :text`

    - `type: :"system.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Float`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Integer`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Integer`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Integer`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Integer`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: Integer`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Integer`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Integer`

          Number of server-executed web search requests.

          format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.events.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
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
