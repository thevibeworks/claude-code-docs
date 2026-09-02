# Events

## List Events

**GET** `/v1/sessions/{session_id}/events`

List Events

### Path parameters

- `session_id: string`

### Query parameters

- `"created_at[gt]": optional string`

  Return events created after this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `"created_at[gte]": optional string`

  Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `"created_at[lt]": optional string`

  Return events created before this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `"created_at[lte]": optional string`

  Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `limit: optional number`

  Query parameter for limit

  format: int32

- `order: optional "asc" or "desc"`

  Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination cursor from a previous response's `next_page`.

- `types: optional array of string`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more`

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

### Returns

- `data: optional array of BetaManagedAgentsSessionEvent`

  Events for the session, ordered by `processed_at`.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast" or null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number or null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5-1"`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium object`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh object`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh object`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax object`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo: optional string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator or null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string or null`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `BetaManagedAgentsAnthropicSkill object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string or null`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `BetaManagedAgentsAgentToolset20260401 object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `BetaManagedAgentsBashToolConfig object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number or null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `user_location: optional BetaManagedAgentsUserLocation or null`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city: optional string or null`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: optional string or null`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: optional string or null`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: optional string or null`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown] or null`

                  - `required: optional array of string or null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object`

          A resolved user-created custom skill.

      - `system: string or null`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object`

        - `BetaManagedAgentsMCPToolset object`

        - `BetaManagedAgentsCustomTool object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `next_page: optional string or null`

  Opaque cursor for the next page. Null when no more results.

### Example

```bash
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

**POST** `/v1/sessions/{session_id}/events`

Send Events

### Path parameters

- `session_id: string`

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more`

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

### Body parameters

- `events: array of BetaManagedAgentsEventParams`

  Events to send to the `session`.

  - `BetaManagedAgentsUserMessageEventParams object`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

  - `BetaManagedAgentsUserInterruptEventParams object`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEventParams object`

    Parameters for confirming or denying a tool execution request.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `BetaManagedAgentsUserCustomToolResultEventParams object`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsUserDefineOutcomeEventParams object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubricParams object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `type: "text"`

    - `type: "user.define_outcome"`

    - `max_iterations: optional number or null`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `BetaManagedAgentsUserToolResultEventParams object`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsSystemMessageEventParams object`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

### Returns

- `BetaManagedAgentsSendSessionEvents object`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 4 more`

    Sent events

    - `BetaManagedAgentsUserMessageEvent object`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `BetaManagedAgentsURLImageSource object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `BetaManagedAgentsFileImageSource object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `BetaManagedAgentsURLDocumentSource object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `BetaManagedAgentsFileDocumentSource object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string or null`

            Additional context about the document for the model.

          - `title: optional string or null`

            The title of the document.

        - `BetaManagedAgentsRedactedBlock object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

    - `BetaManagedAgentsUserInterruptEvent object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `BetaManagedAgentsUserToolConfirmationEvent object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

      - `deny_message: optional string or null`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `BetaManagedAgentsUserCustomToolResultEvent object`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `BetaManagedAgentsSearchResultBlock object`

          A block containing a web search result.

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `text: string`

              The text content.

              minLength: 1

            - `type: "text"`

          - `source: string`

            The URL source of the search result.

            minLength: 1

          - `title: string`

            The title of the search result.

            minLength: 1

          - `type: "search_result"`

      - `is_error: optional boolean or null`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `BetaManagedAgentsUserDefineOutcomeEvent object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number or null`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `BetaManagedAgentsTextRubric object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

    - `BetaManagedAgentsUserToolResultEvent object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `BetaManagedAgentsSearchResultBlock object`

          A block containing a web search result.

      - `is_error: optional boolean or null`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `BetaManagedAgentsSystemMessageEvent object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "events": [
            {
              "content": [
                {
                  "text": "Where is my order #1234?",
                  "type": "text"
                }
              ],
              "type": "user.message"
            }
          ]
        }'
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

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Path parameters

- `session_id: string`

### Query parameters

- `event_deltas: optional array of BetaManagedAgentsDeltaType`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

### Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more`

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

### Returns

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in the session stream.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast" or null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number or null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5-1"`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium object`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh object`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh object`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax object`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo: optional string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator or null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string or null`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `BetaManagedAgentsAnthropicSkill object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string or null`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `BetaManagedAgentsAgentToolset20260401 object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `BetaManagedAgentsBashToolConfig object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number or null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `user_location: optional BetaManagedAgentsUserLocation or null`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city: optional string or null`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: optional string or null`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: optional string or null`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: optional string or null`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown] or null`

                  - `required: optional array of string or null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object`

          A resolved user-created custom skill.

      - `system: string or null`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object`

        - `BetaManagedAgentsMCPToolset object`

        - `BetaManagedAgentsCustomTool object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview object`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

      - `BetaManagedAgentsAgentThinkingPreview object`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

    - `type: "event_start"`

  - `BetaManagedAgentsDeltaEvent object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: "content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in the session stream.

### Example

```bash
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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

- `BetaManagedAgentsAgentCustomToolUseEvent object`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `name: string`

    Name of the custom tool being called.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.custom_tool_use"`

  - `session_thread_id: optional string or null`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

### Beta Managed Agents Agent MCP Tool Result Event

- `BetaManagedAgentsAgentMCPToolResultEvent object`

  Event representing the result of an MCP tool execution.

  - `id: string`

    Unique identifier for this event.

  - `mcp_tool_use_id: string`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.mcp_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `source: string`

        The URL source of the search result.

        minLength: 1

      - `title: string`

        The title of the search result.

        minLength: 1

      - `type: "search_result"`

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `BetaManagedAgentsAgentMCPToolUseEvent object`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `mcp_server_name: string`

    Name of the MCP server providing the tool.

  - `name: string`

    Name of the MCP tool being used.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.mcp_tool_use"`

  - `evaluated_permission: optional "allow" or "ask" or "deny"`

    AgentEvaluatedPermission enum

    - `"allow"`

    - `"ask"`

    - `"deny"`

  - `session_thread_id: optional string or null`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Agent Message Event

- `BetaManagedAgentsAgentMessageEvent object`

  An agent response event in the session conversation.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

    Array of text blocks comprising the agent response.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.message"`

### Beta Managed Agents Agent Thinking Event

- `BetaManagedAgentsAgentThinkingEvent object`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.thinking"`

### Beta Managed Agents Agent Thread Context Compacted Event

- `BetaManagedAgentsAgentThreadContextCompactedEvent object`

  Indicates that context compaction (summarization) occurred during the session.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.thread_context_compacted"`

### Beta Managed Agents Agent Thread Message Received Event

- `BetaManagedAgentsAgentThreadMessageReceivedEvent object`

  Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Message content blocks.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `from_session_thread_id: string`

    Public `sthr_` ID of the thread that sent the message.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.thread_message_received"`

  - `from_agent_name: optional string or null`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `BetaManagedAgentsAgentThreadMessageSentEvent object`

  Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Message content blocks.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `to_session_thread_id: string`

    Public `sthr_` ID of the thread the message was sent to.

  - `type: "agent.thread_message_sent"`

  - `to_agent_name: optional string or null`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Result Event

- `BetaManagedAgentsAgentToolResultEvent object`

  Event representing the result of an agent tool execution.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to.

  - `type: "agent.tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `source: string`

        The URL source of the search result.

        minLength: 1

      - `title: string`

        The title of the search result.

        minLength: 1

      - `type: "search_result"`

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `BetaManagedAgentsAgentToolUseEvent object`

  Event emitted when the agent invokes a built-in agent tool.

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `name: string`

    Name of the agent tool being used.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "agent.tool_use"`

  - `evaluated_permission: optional "allow" or "ask" or "deny"`

    AgentEvaluatedPermission enum

    - `"allow"`

    - `"ask"`

    - `"deny"`

  - `session_thread_id: optional string or null`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

### Beta Managed Agents Base64 Document Source

- `BetaManagedAgentsBase64DocumentSource object`

  Base64-encoded document data.

  - `data: string`

    Base64-encoded document data.

    minLength: 1

  - `media_type: string`

    MIME type of the document (e.g., "application/pdf").

    minLength: 1

  - `type: "base64"`

### Beta Managed Agents Base64 Image Source

- `BetaManagedAgentsBase64ImageSource object`

  Base64-encoded image data.

  - `data: string`

    Base64-encoded image data.

    minLength: 1

  - `media_type: string`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

    minLength: 1

  - `type: "base64"`

### Beta Managed Agents Billing Error

- `BetaManagedAgentsBillingError object`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "billing_error"`

### Beta Managed Agents Credential Host Unreachable Error

- `BetaManagedAgentsCredentialHostUnreachableError object`

  An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

  - `credential_id: string`

    ID of the affected credential.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "credential_host_unreachable_error"`

  - `vault_id: string`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `BetaManagedAgentsDocumentBlock object`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

    Union type for document source variants.

    - `BetaManagedAgentsBase64DocumentSource object`

      Base64-encoded document data.

      - `data: string`

        Base64-encoded document data.

        minLength: 1

      - `media_type: string`

        MIME type of the document (e.g., "application/pdf").

        minLength: 1

      - `type: "base64"`

    - `BetaManagedAgentsPlainTextDocumentSource object`

      Plain text document content.

      - `data: string`

        The plain text content.

        minLength: 1

      - `media_type: "text/plain"`

        MIME type of the text content. Must be "text/plain".

      - `type: "text"`

    - `BetaManagedAgentsURLDocumentSource object`

      Document referenced by URL.

      - `type: "url"`

      - `url: string`

        URL of the document to fetch.

        minLength: 1

    - `BetaManagedAgentsFileDocumentSource object`

      Document referenced by file ID.

      - `file_id: string`

        ID of a previously uploaded file.

        minLength: 1

      - `type: "file"`

  - `type: "document"`

  - `context: optional string or null`

    Additional context about the document for the model.

  - `title: optional string or null`

    The title of the document.

### Beta Managed Agents Event Params

- `BetaManagedAgentsEventParams = BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserInterruptEventParams or BetaManagedAgentsUserToolConfirmationEventParams or 4 more`

  Union type for event parameters that can be sent to a session.

  - `BetaManagedAgentsUserMessageEventParams object`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

  - `BetaManagedAgentsUserInterruptEventParams object`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEventParams object`

    Parameters for confirming or denying a tool execution request.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `BetaManagedAgentsUserCustomToolResultEventParams object`

    Parameters for providing the result of a custom tool execution.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsUserDefineOutcomeEventParams object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubricParams object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `type: "text"`

    - `type: "user.define_outcome"`

    - `max_iterations: optional number or null`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `BetaManagedAgentsUserToolResultEventParams object`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsSystemMessageEventParams object`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

### Beta Managed Agents File Document Source

- `BetaManagedAgentsFileDocumentSource object`

  Document referenced by file ID.

  - `file_id: string`

    ID of a previously uploaded file.

    minLength: 1

  - `type: "file"`

### Beta Managed Agents File Image Source

- `BetaManagedAgentsFileImageSource object`

  Image referenced by file ID.

  - `file_id: string`

    ID of a previously uploaded file.

    minLength: 1

  - `type: "file"`

### Beta Managed Agents File Rubric

- `BetaManagedAgentsFileRubric object`

  Rubric referenced by a file uploaded via the Files API.

  - `file_id: string`

    ID of the rubric file.

  - `type: "file"`

### Beta Managed Agents File Rubric Params

- `BetaManagedAgentsFileRubricParams object`

  Rubric referenced by a file uploaded via the Files API.

  - `file_id: string`

    ID of the rubric file.

  - `type: "file"`

### Beta Managed Agents Image Block

- `BetaManagedAgentsImageBlock object`

  Image content specified directly as base64 data or as a reference via a URL.

  - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

    Union type for image source variants.

    - `BetaManagedAgentsBase64ImageSource object`

      Base64-encoded image data.

      - `data: string`

        Base64-encoded image data.

        minLength: 1

      - `media_type: string`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

        minLength: 1

      - `type: "base64"`

    - `BetaManagedAgentsURLImageSource object`

      Image referenced by URL.

      - `type: "url"`

      - `url: string`

        URL of the image to fetch.

        minLength: 1

    - `BetaManagedAgentsFileImageSource object`

      Image referenced by file ID.

      - `file_id: string`

        ID of a previously uploaded file.

        minLength: 1

      - `type: "file"`

  - `type: "image"`

### Beta Managed Agents MCP Authentication Failed Error

- `BetaManagedAgentsMCPAuthenticationFailedError object`

  Authentication to an MCP server failed.

  - `mcp_server_name: string`

    Name of the MCP server that failed authentication.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "mcp_authentication_failed_error"`

### Beta Managed Agents MCP Connection Failed Error

- `BetaManagedAgentsMCPConnectionFailedError object`

  Failed to connect to an MCP server.

  - `mcp_server_name: string`

    Name of the MCP server that failed to connect.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "mcp_connection_failed_error"`

### Beta Managed Agents Model Overloaded Error

- `BetaManagedAgentsModelOverloadedError object`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "model_overloaded_error"`

### Beta Managed Agents Model Rate Limited Error

- `BetaManagedAgentsModelRateLimitedError object`

  The model request was rate-limited.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "model_rate_limited_error"`

### Beta Managed Agents Model Request Failed Error

- `BetaManagedAgentsModelRequestFailedError object`

  A model request failed for a reason other than overload or rate-limiting.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "model_request_failed_error"`

### Beta Managed Agents Plain Text Document Source

- `BetaManagedAgentsPlainTextDocumentSource object`

  Plain text document content.

  - `data: string`

    The plain text content.

    minLength: 1

  - `media_type: "text/plain"`

    MIME type of the text content. Must be "text/plain".

  - `type: "text"`

### Beta Managed Agents Redacted Block

- `BetaManagedAgentsRedactedBlock object`

  Placeholder for content withheld by Anthropic model policy.

  - `type: "redacted"`

### Beta Managed Agents Retry Status Exhausted

- `BetaManagedAgentsRetryStatusExhausted object`

  This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

  - `type: "exhausted"`

### Beta Managed Agents Retry Status Retrying

- `BetaManagedAgentsRetryStatusRetrying object`

  The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

  - `type: "retrying"`

### Beta Managed Agents Retry Status Terminal

- `BetaManagedAgentsRetryStatusTerminal object`

  The session encountered a terminal error and will transition to `terminated` state.

  - `type: "terminal"`

### Beta Managed Agents Search Result Block

- `BetaManagedAgentsSearchResultBlock object`

  A block containing a web search result.

  - `citations: BetaManagedAgentsSearchResultCitations`

    Citation settings for a search result.

    - `enabled: boolean`

      Whether citations are enabled for this search result.

  - `content: array of BetaManagedAgentsSearchResultContent`

    Array of text content blocks from the search result.

    - `text: string`

      The text content.

      minLength: 1

    - `type: "text"`

  - `source: string`

    The URL source of the search result.

    minLength: 1

  - `title: string`

    The title of the search result.

    minLength: 1

  - `type: "search_result"`

### Beta Managed Agents Search Result Citations

- `BetaManagedAgentsSearchResultCitations object`

  Citation settings for a search result.

  - `enabled: boolean`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `BetaManagedAgentsSearchResultContent object`

  Text content within a search result.

  - `text: string`

    The text content.

    minLength: 1

  - `type: "text"`

### Beta Managed Agents Send Session Events

- `BetaManagedAgentsSendSessionEvents object`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 4 more`

    Sent events

    - `BetaManagedAgentsUserMessageEvent object`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `BetaManagedAgentsBase64ImageSource object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `BetaManagedAgentsURLImageSource object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `BetaManagedAgentsFileImageSource object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `BetaManagedAgentsBase64DocumentSource object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `BetaManagedAgentsPlainTextDocumentSource object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `BetaManagedAgentsURLDocumentSource object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `BetaManagedAgentsFileDocumentSource object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string or null`

            Additional context about the document for the model.

          - `title: optional string or null`

            The title of the document.

        - `BetaManagedAgentsRedactedBlock object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

    - `BetaManagedAgentsUserInterruptEvent object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `BetaManagedAgentsUserToolConfirmationEvent object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

      - `deny_message: optional string or null`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `BetaManagedAgentsUserCustomToolResultEvent object`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `BetaManagedAgentsSearchResultBlock object`

          A block containing a web search result.

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `text: string`

              The text content.

              minLength: 1

            - `type: "text"`

          - `source: string`

            The URL source of the search result.

            minLength: 1

          - `title: string`

            The title of the search result.

            minLength: 1

          - `type: "search_result"`

      - `is_error: optional boolean or null`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `BetaManagedAgentsUserDefineOutcomeEvent object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number or null`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `BetaManagedAgentsFileRubric object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `BetaManagedAgentsTextRubric object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

    - `BetaManagedAgentsUserToolResultEvent object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `BetaManagedAgentsSearchResultBlock object`

          A block containing a web search result.

      - `is_error: optional boolean or null`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string or null`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `BetaManagedAgentsSystemMessageEvent object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

      - `processed_at: optional string or null`

        A timestamp in RFC 3339 format

        format: date-time

### Beta Managed Agents Session Budget Reached

- `BetaManagedAgentsSessionBudgetReached object`

  The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `type: "budget_reached"`

### Beta Managed Agents Session Deleted Event

- `BetaManagedAgentsSessionDeletedEvent object`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.deleted"`

### Beta Managed Agents Session End Turn

- `BetaManagedAgentsSessionEndTurn object`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: "end_turn"`

### Beta Managed Agents Session Error Event

- `BetaManagedAgentsSessionErrorEvent object`

  An error event indicating a problem occurred during session execution.

  - `id: string`

    Unique identifier for this event.

  - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

    An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

    - `BetaManagedAgentsUnknownError object`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

      - `type: "unknown_error"`

    - `BetaManagedAgentsModelOverloadedError object`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "model_overloaded_error"`

    - `BetaManagedAgentsModelRateLimitedError object`

      The model request was rate-limited.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "model_rate_limited_error"`

    - `BetaManagedAgentsModelRequestFailedError object`

      A model request failed for a reason other than overload or rate-limiting.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "model_request_failed_error"`

    - `BetaManagedAgentsMCPConnectionFailedError object`

      Failed to connect to an MCP server.

      - `mcp_server_name: string`

        Name of the MCP server that failed to connect.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "mcp_connection_failed_error"`

    - `BetaManagedAgentsMCPAuthenticationFailedError object`

      Authentication to an MCP server failed.

      - `mcp_server_name: string`

        Name of the MCP server that failed authentication.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "mcp_authentication_failed_error"`

    - `BetaManagedAgentsBillingError object`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "billing_error"`

    - `BetaManagedAgentsCredentialHostUnreachableError object`

      An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

      - `credential_id: string`

        ID of the affected credential.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next in response to this error.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `type: "credential_host_unreachable_error"`

      - `vault_id: string`

        ID of the vault containing the affected credential.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.error"`

### Beta Managed Agents Session Event

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 32 more`

  Union type for all event types in a session.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast" or null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number or null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5-1"`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium object`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh object`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh object`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax object`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo: optional string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator or null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string or null`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `BetaManagedAgentsAnthropicSkill object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string or null`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `BetaManagedAgentsAgentToolset20260401 object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `BetaManagedAgentsBashToolConfig object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number or null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `user_location: optional BetaManagedAgentsUserLocation or null`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city: optional string or null`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: optional string or null`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: optional string or null`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: optional string or null`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown] or null`

                  - `required: optional array of string or null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object`

          A resolved user-created custom skill.

      - `system: string or null`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object`

        - `BetaManagedAgentsMCPToolset object`

        - `BetaManagedAgentsCustomTool object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Beta Managed Agents Session Requires Action

- `BetaManagedAgentsSessionRequiresAction object`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `event_ids: array of string`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

  - `type: "requires_action"`

### Beta Managed Agents Session Retries Exhausted

- `BetaManagedAgentsSessionRetriesExhausted object`

  The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

  - `type: "retries_exhausted"`

### Beta Managed Agents Session Status Idle Event

- `BetaManagedAgentsSessionStatusIdleEvent object`

  Indicates the agent has paused and is awaiting user input.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

    The agent completed its turn naturally and is ready for the next user message.

    - `BetaManagedAgentsSessionEndTurn object`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: "end_turn"`

    - `BetaManagedAgentsSessionRequiresAction object`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: array of string`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: "requires_action"`

    - `BetaManagedAgentsSessionRetriesExhausted object`

      The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type: "retries_exhausted"`

    - `BetaManagedAgentsSessionBudgetReached object`

      The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `type: "budget_reached"`

  - `type: "session.status_idle"`

### Beta Managed Agents Session Status Rescheduled Event

- `BetaManagedAgentsSessionStatusRescheduledEvent object`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.status_rescheduled"`

### Beta Managed Agents Session Status Running Event

- `BetaManagedAgentsSessionStatusRunningEvent object`

  Indicates the session is actively running and the agent is working.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.status_running"`

### Beta Managed Agents Session Status Terminated Event

- `BetaManagedAgentsSessionStatusTerminatedEvent object`

  Indicates the session has terminated, either due to an error or completion.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.status_terminated"`

### Beta Managed Agents Session Thread Created Event

- `BetaManagedAgentsSessionThreadCreatedEvent object`

  Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the callable agent the thread runs.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: string`

    Public `sthr_` ID of the newly created thread.

  - `type: "session.thread_created"`

### Beta Managed Agents Session Thread Status Idle Event

- `BetaManagedAgentsSessionThreadStatusIdleEvent object`

  A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that went idle.

  - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

    The agent completed its turn naturally and is ready for the next user message.

    - `BetaManagedAgentsSessionEndTurn object`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: "end_turn"`

    - `BetaManagedAgentsSessionRequiresAction object`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `event_ids: array of string`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `type: "requires_action"`

    - `BetaManagedAgentsSessionRetriesExhausted object`

      The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type: "retries_exhausted"`

    - `BetaManagedAgentsSessionBudgetReached object`

      The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `type: "budget_reached"`

  - `type: "session.thread_status_idle"`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

  A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that is retrying.

  - `type: "session.thread_status_rescheduled"`

### Beta Managed Agents Session Thread Status Running Event

- `BetaManagedAgentsSessionThreadStatusRunningEvent object`

  A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that started running.

  - `type: "session.thread_status_running"`

### Beta Managed Agents Session Thread Status Terminated Event

- `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

  A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that terminated.

  - `type: "session.thread_status_terminated"`

### Beta Managed Agents Session Usage Snapshot

- `BetaManagedAgentsSessionUsageSnapshot object`

  Point-in-time snapshot of a session's cumulative usage.

  - `active_seconds: optional number`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

    format: double

  - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens: optional number`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `ephemeral_5m_input_tokens: optional number`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `cache_read_input_tokens: optional number`

    Total tokens read from prompt cache.

    format: int32

  - `input_tokens: optional number`

    Total input tokens consumed across all turns.

    format: int32

  - `list_cost: optional BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `output_tokens: optional number`

    Total output tokens generated across all turns.

    format: int32

  - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `web_fetch_requests: optional number`

      Number of server-executed web fetch requests.

      format: int32

    - `web_search_requests: optional number`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Span Model Request End Event

- `BetaManagedAgentsSpanModelRequestEndEvent object`

  Emitted when a model request completes.

  - `id: string`

    Unique identifier for this event.

  - `is_error: boolean or null`

    Whether the model request resulted in an error.

  - `model_request_start_id: string`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: BetaManagedAgentsSpanModelUsage`

    Token usage for a single model request.

    - `cache_creation_input_tokens: number`

      Tokens used to create prompt cache in this request.

      format: int32

    - `cache_read_input_tokens: number`

      Tokens read from prompt cache in this request.

      format: int32

    - `input_tokens: number`

      Input tokens consumed by this request.

      format: int32

    - `output_tokens: number`

      Output tokens generated by this request.

      format: int32

    - `speed: optional "standard" or "fast" or null`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "span.model_request_end"`

### Beta Managed Agents Span Model Request Start Event

- `BetaManagedAgentsSpanModelRequestStartEvent object`

  Emitted when a model request is initiated by the agent.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "span.model_request_start"`

### Beta Managed Agents Span Model Usage

- `BetaManagedAgentsSpanModelUsage object`

  Token usage for a single model request.

  - `cache_creation_input_tokens: number`

    Tokens used to create prompt cache in this request.

    format: int32

  - `cache_read_input_tokens: number`

    Tokens read from prompt cache in this request.

    format: int32

  - `input_tokens: number`

    Input tokens consumed by this request.

    format: int32

  - `output_tokens: number`

    Output tokens generated by this request.

    format: int32

  - `speed: optional "standard" or "fast" or null`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Span Outcome Evaluation End Event

- `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

  Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

  - `id: string`

    Unique identifier for this event.

  - `explanation: string`

    Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

  - `iteration: number`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    format: int32

  - `outcome_evaluation_start_id: string`

    The id of the corresponding `span.outcome_evaluation_start` event.

  - `outcome_id: string`

    The `outc_` ID of the outcome being evaluated.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `result: string`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `type: "span.outcome_evaluation_end"`

  - `usage: BetaManagedAgentsSpanModelUsage`

    Token usage for a single model request.

    - `cache_creation_input_tokens: number`

      Tokens used to create prompt cache in this request.

      format: int32

    - `cache_read_input_tokens: number`

      Tokens read from prompt cache in this request.

      format: int32

    - `input_tokens: number`

      Input tokens consumed by this request.

      format: int32

    - `output_tokens: number`

      Output tokens generated by this request.

      format: int32

    - `speed: optional "standard" or "fast" or null`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

  Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

  - `id: string`

    Unique identifier for this event.

  - `iteration: number`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    format: int32

  - `outcome_id: string`

    The `outc_` ID of the outcome being evaluated.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "span.outcome_evaluation_ongoing"`

### Beta Managed Agents Span Outcome Evaluation Start Event

- `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

  Emitted when an outcome evaluation cycle begins.

  - `id: string`

    Unique identifier for this event.

  - `iteration: number`

    0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    format: int32

  - `outcome_id: string`

    The `outc_` ID of the outcome being evaluated.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "span.outcome_evaluation_start"`

### Beta Managed Agents Stream Session Events

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in the session stream.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent object`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast" or null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number or null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock object`

        A block containing a web search result.

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string or null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-fable-5-1"`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

            - `"claude-sonnet-5"`

              High-performance model for coding and agents

            - `"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow object`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium object`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh object`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh object`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax object`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo: optional string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator or null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string or null`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `BetaManagedAgentsAnthropicSkill object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string or null`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `BetaManagedAgentsAgentToolset20260401 object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `BetaManagedAgentsBashToolConfig object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number or null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `user_location: optional BetaManagedAgentsUserLocation or null`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city: optional string or null`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: optional string or null`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: optional string or null`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: optional string or null`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown] or null`

                  - `required: optional array of string or null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill object`

          A resolved user-created custom skill.

      - `system: string or null`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object`

        - `BetaManagedAgentsMCPToolset object`

        - `BetaManagedAgentsCustomTool object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview object`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

      - `BetaManagedAgentsAgentThinkingPreview object`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

    - `type: "event_start"`

  - `BetaManagedAgentsDeltaEvent object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: "content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at: optional string or null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Beta Managed Agents System Message Event Params

- `BetaManagedAgentsSystemMessageEventParams object`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

  - `content: array of BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `text: string`

      The text content.

      minLength: 1

    - `type: "text"`

  - `type: "system.message"`

### Beta Managed Agents Text Block

- `BetaManagedAgentsTextBlock object`

  Regular text content.

  - `text: string`

    The text content.

    minLength: 1

  - `type: "text"`

### Beta Managed Agents Text Rubric

- `BetaManagedAgentsTextRubric object`

  Rubric content provided inline as text.

  - `content: string`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `type: "text"`

### Beta Managed Agents Text Rubric Params

- `BetaManagedAgentsTextRubricParams object`

  Rubric content provided inline as text.

  - `content: string`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

    maxLength: 262144

  - `type: "text"`

### Beta Managed Agents Unknown Error

- `BetaManagedAgentsUnknownError object`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next in response to this error.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `type: "unknown_error"`

### Beta Managed Agents URL Document Source

- `BetaManagedAgentsURLDocumentSource object`

  Document referenced by URL.

  - `type: "url"`

  - `url: string`

    URL of the document to fetch.

    minLength: 1

### Beta Managed Agents URL Image Source

- `BetaManagedAgentsURLImageSource object`

  Image referenced by URL.

  - `type: "url"`

  - `url: string`

    URL of the image to fetch.

    minLength: 1

### Beta Managed Agents User Custom Tool Result Event

- `BetaManagedAgentsUserCustomToolResultEvent object`

  Event sent by the client providing the result of a custom tool execution.

  - `id: string`

    Unique identifier for this event.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.custom_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `source: string`

        The URL source of the search result.

        minLength: 1

      - `title: string`

        The title of the search result.

        minLength: 1

      - `type: "search_result"`

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

  - `processed_at: optional string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: optional string or null`

    Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

### Beta Managed Agents User Custom Tool Result Event Params

- `BetaManagedAgentsUserCustomToolResultEventParams object`

  Parameters for providing the result of a custom tool execution.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `type: "user.custom_tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `source: string`

        The URL source of the search result.

        minLength: 1

      - `title: string`

        The title of the search result.

        minLength: 1

      - `type: "search_result"`

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

- `BetaManagedAgentsUserDefineOutcomeEvent object`

  Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

  - `id: string`

    Unique identifier for this event.

  - `description: string`

    What the agent should produce. Copied from the input event.

  - `max_iterations: number or null`

    Evaluate-then-revise cycles before giving up. Default 3, max 20.

    format: int32

  - `outcome_id: string`

    Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

    Rubric for grading the quality of an outcome.

    - `BetaManagedAgentsFileRubric object`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: string`

        ID of the rubric file.

      - `type: "file"`

    - `BetaManagedAgentsTextRubric object`

      Rubric content provided inline as text.

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: "text"`

  - `type: "user.define_outcome"`

### Beta Managed Agents User Define Outcome Event Params

- `BetaManagedAgentsUserDefineOutcomeEventParams object`

  Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

  - `description: string`

    What the agent should produce. This is the task specification.

  - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

    Rubric for grading the quality of an outcome.

    - `BetaManagedAgentsFileRubricParams object`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: string`

        ID of the rubric file.

      - `type: "file"`

    - `BetaManagedAgentsTextRubricParams object`

      Rubric content provided inline as text.

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        maxLength: 262144

      - `type: "text"`

  - `type: "user.define_outcome"`

  - `max_iterations: optional number or null`

    Eval→revision cycles before giving up. Default 3, max 20.

    format: int32

### Beta Managed Agents User Interrupt Event

- `BetaManagedAgentsUserInterruptEvent object`

  An interrupt event that pauses agent execution and returns control to the user.

  - `id: string`

    Unique identifier for this event.

  - `type: "user.interrupt"`

  - `processed_at: optional string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: optional string or null`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Interrupt Event Params

- `BetaManagedAgentsUserInterruptEventParams object`

  Parameters for sending an interrupt to pause the agent.

  - `type: "user.interrupt"`

  - `session_thread_id: optional string or null`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Message Event

- `BetaManagedAgentsUserMessageEvent object`

  A user message event in the session conversation.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Array of content blocks comprising the user message.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `type: "user.message"`

  - `processed_at: optional string or null`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents User Message Event Params

- `BetaManagedAgentsUserMessageEventParams object`

  Parameters for sending a user message to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Array of content blocks for the user message.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `type: "user.message"`

### Beta Managed Agents User Tool Confirmation Event

- `BetaManagedAgentsUserToolConfirmationEvent object`

  A tool confirmation event that approves or denies a pending tool execution.

  - `id: string`

    Unique identifier for this event.

  - `result: "allow" or "deny"`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_confirmation"`

  - `deny_message: optional string or null`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    maxLength: 10000

  - `processed_at: optional string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: optional string or null`

    When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

### Beta Managed Agents User Tool Confirmation Event Params

- `BetaManagedAgentsUserToolConfirmationEventParams object`

  Parameters for confirming or denying a tool execution request.

  - `result: "allow" or "deny"`

    UserToolConfirmationResult enum

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `type: "user.tool_confirmation"`

  - `deny_message: optional string or null`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    maxLength: 10000

### Beta Managed Agents User Tool Result Event Params

- `BetaManagedAgentsUserToolResultEventParams object`

  Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `type: "user.tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `source: string`

        The URL source of the search result.

        minLength: 1

      - `title: string`

        The title of the search result.

        minLength: 1

      - `type: "search_result"`

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.
