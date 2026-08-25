# Stream Events

`beta.sessions.events.stream(session_id, **kwargs)  -> BetaManagedAgentsStreamSessionEvents`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

## Parameters

- `session_id: str`

- `event_deltas: Optional[List[BetaManagedAgentsDeltaType]]`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

## Returns

- `BetaManagedAgentsStreamSessionEvents`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `text: str`

          The text content.

          minLength: 1

        - `type: Literal["text"]`

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: Literal["base64"]`

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

            - `type: Literal["file"]`

        - `type: Literal["image"]`

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: Literal["base64"]`

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

            - `type: Literal["text"]`

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

            - `type: Literal["file"]`

        - `type: Literal["document"]`

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

    - `type: Literal["user.message"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: str`

      Unique identifier for this event.

    - `type: Literal["user.interrupt"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_confirmation"]`

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.custom_tool_result"]`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: str`

            The text content.

            minLength: 1

          - `type: Literal["text"]`

        - `source: str`

          The URL source of the search result.

          minLength: 1

        - `title: str`

          The title of the search result.

          minLength: 1

        - `type: Literal["search_result"]`

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.custom_tool_use"]`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.message"]`

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.thinking"]`

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.mcp_tool_use"]`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.mcp_tool_result"]`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.tool_use"]`

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: Literal["agent.tool_result"]`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.thread_message_received"]`

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: Literal["agent.thread_message_sent"]`

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["agent.thread_context_compacted"]`

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

        - `type: Literal["unknown_error"]`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_overloaded_error"]`

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_rate_limited_error"]`

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["model_request_failed_error"]`

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_connection_failed_error"]`

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["mcp_authentication_failed_error"]`

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["billing_error"]`

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: Literal["credential_host_unreachable_error"]`

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.error"]`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.status_rescheduled"]`

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.status_running"]`

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: Literal["requires_action"]`

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: Literal["budget_reached"]`

    - `type: Literal["session.status_idle"]`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.status_terminated"]`

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

    - `type: Literal["session.thread_created"]`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["span.outcome_evaluation_start"]`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: Literal["span.outcome_evaluation_end"]`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: int`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: int`

        Output tokens generated by this request.

        format: int32

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["span.model_request_start"]`

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["span.model_request_end"]`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["span.outcome_evaluation_ongoing"]`

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: str`

          ID of the rubric file.

        - `type: Literal["file"]`

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: Literal["text"]`

    - `type: Literal["user.define_outcome"]`

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.deleted"]`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

    - `type: Literal["session.thread_status_running"]`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: Literal["session.thread_status_idle"]`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

    - `type: Literal["session.thread_status_terminated"]`

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: Literal["user.tool_result"]`

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

    - `type: Literal["session.thread_status_rescheduled"]`

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.updated"]`

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: str`

        - `type: Literal["url"]`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-sonnet-5", "claude-fable-5", "claude-opus-5", 10 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: List[Agent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent: …`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: str`

            - `description: Optional[str]`

            - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

              - `name: str`

              - `type: Literal["url"]`

              - `url: str`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: str`

            - `skills: List[Skill]`

              - `class BetaManagedAgentsAnthropicSkill: …`

                A resolved Anthropic-managed skill.

                - `skill_id: str`

                - `type: Literal["anthropic"]`

                - `version: str`

              - `class BetaManagedAgentsCustomSkill: …`

                A resolved user-created custom skill.

                - `skill_id: str`

                - `type: Literal["custom"]`

                - `version: str`

            - `system: Optional[str]`

            - `tools: List[Tool]`

              - `class BetaManagedAgentsAgentToolset20260401: …`

                - `configs: List[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig: …`

                    Configuration for the bash tool.

                    - `enabled: bool`

                    - `name: Literal["bash"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                        - `type: Literal["always_allow"]`

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                        - `type: Literal["always_ask"]`

                    - `type: Literal["bash"]`

                  - `class BetaManagedAgentsEditToolConfig: …`

                    Configuration for the edit tool.

                    - `enabled: bool`

                    - `name: Literal["edit"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["edit"]`

                  - `class BetaManagedAgentsReadToolConfig: …`

                    Configuration for the read tool.

                    - `enabled: bool`

                    - `name: Literal["read"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["read"]`

                  - `class BetaManagedAgentsWriteToolConfig: …`

                    Configuration for the write tool.

                    - `enabled: bool`

                    - `name: Literal["write"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["write"]`

                  - `class BetaManagedAgentsGlobToolConfig: …`

                    Configuration for the glob tool.

                    - `enabled: bool`

                    - `name: Literal["glob"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["glob"]`

                  - `class BetaManagedAgentsGrepToolConfig: …`

                    Configuration for the grep tool.

                    - `enabled: bool`

                    - `name: Literal["grep"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["grep"]`

                  - `class BetaManagedAgentsWebFetchToolConfig: …`

                    Configuration for the web_fetch tool.

                    - `enabled: bool`

                    - `name: Literal["web_fetch"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["web_fetch"]`

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `max_content_tokens: Optional[int]`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig: …`

                    Configuration for the web_search tool.

                    - `enabled: bool`

                    - `name: Literal["web_search"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["web_search"]`

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `user_location: Optional[BetaManagedAgentsUserLocation]`

                      Approximate user location for search result localization.

                      - `type: Literal["approximate"]`

                        Location precision. Only "approximate" is supported.

                      - `city: Optional[str]`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: Optional[str]`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: Optional[str]`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: Optional[str]`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                - `type: Literal["agent_toolset_20260401"]`

              - `class BetaManagedAgentsMCPToolset: …`

                - `configs: List[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: str`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: str`

                - `type: Literal["mcp_toolset"]`

              - `class BetaManagedAgentsCustomTool: …`

                A custom tool as returned in API responses.

                - `description: str`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: Literal["object"]`

                  - `properties: Optional[Dict[str, object]]`

                  - `required: Optional[List[str]]`

                - `name: str`

                - `type: Literal["custom"]`

            - `type: Literal["agent"]`

            - `version: int`

              format: int32

          - `class BetaManagedAgentsAdvisor: …`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: str`

              The advisor model id.

            - `type: Literal["advisor"]`

        - `type: Literal["coordinator"]`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

      - `version: int`

        format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: str`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: Literal["limit"]`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

    - `type: Literal["event_start"]`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

        minLength: 1

      - `type: Literal["text"]`

    - `type: Literal["system.message"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent: …`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: Literal["session.usage"]`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Optional[float]`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Optional[int]`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Optional[int]`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Optional[int]`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Optional[int]`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: Optional[BetaMonetaryAmount]`

        A monetary amount in a specific currency.

      - `output_tokens: Optional[int]`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Optional[int]`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Optional[int]`

          Number of server-executed web search requests.

          format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `BetaManagedAgentsStreamSessionEvents`

  Server-sent event in the session stream.

## Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
for event in client.beta.sessions.events.stream(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
    print(event)
```

### Response (200)

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
