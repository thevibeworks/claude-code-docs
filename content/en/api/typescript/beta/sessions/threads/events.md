---
title: Events
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/threads/events
---

# Events

## List Session Thread Events

`client.beta.sessions.threads.events.list(threadID, params, options?): PageCursor<BetaManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

### Parameters

- `threadID: string`

- `params: EventListParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `limit?: number`

    Query param: Query parameter for limit

    format: int32

  - `page?: string`

    Query param: Query parameter for page

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 42 more`

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

      - `"user-profiles-2026-09-04"`

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

  - `workspace_id?: string`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 32 more`

  Union type for all event types in a session.

  - `BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" | "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message?: string | null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: Array<BetaManagedAgentsSearchResultContent>`

          Array of text content blocks from the search result.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock>`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation?: BetaManagedAgentsAgentToolEvaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `BetaManagedAgentsAgentToolEvaluationAuto`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation?: BetaManagedAgentsAgentToolEvaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: "agent.thread_message_received"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name?: string | null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name?: string | null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: Array<string>`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

    - `type: "span.outcome_evaluation_start"`

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

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: "span.outcome_evaluation_end"`

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

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean | null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: "span.outcome_evaluation_ongoing"`

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

  - `BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number | null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent?: BetaManagedAgentsSessionAgent | null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: "agent"`

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1" | "claude-sonnet-5" | "claude-fable-5" | 11 more`

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

          - `(string & {})`

        - `effort?: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo?: string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed?: "standard" | "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: "coordinator"`

        - `agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: "agent"`

            - `id: string`

            - `description: string | null`

            - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

              - `type: "url"`

              - `name: string`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

              - `BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `type: "anthropic"`

                - `skill_id: string`

                - `version: string`

              - `BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `type: "custom"`

                - `skill_id: string`

                - `version: string`

            - `system: string | null`

            - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

              - `BetaManagedAgentsAgentToolset20260401`

                - `type: "agent_toolset_20260401"`

                - `configs: Array<BetaManagedAgentsAgentToolConfig>`

                  - `BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `type: "bash"`

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: "auto"`

                  - `BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `type: "edit"`

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `type: "read"`

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `type: "write"`

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `type: "glob"`

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `type: "grep"`

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `type: "web_fetch"`

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `max_content_tokens?: number | null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `type: "web_search"`

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `user_location?: BetaManagedAgentsUserLocation | null`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city?: string | null`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country?: string | null`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region?: string | null`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone?: string | null`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `BetaManagedAgentsMCPToolset`

                - `type: "mcp_toolset"`

                - `configs: Array<BetaManagedAgentsMCPToolConfig>`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: string`

              - `BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `type: "custom"`

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties?: Record<string, unknown> | null`

                  - `required?: Array<string> | null`

                - `name: string`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: "advisor"`

            - `model: string`

              The advisor model id.

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

        - `BetaManagedAgentsMCPToolset`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `version: number`

        format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: "limit"`

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata?: Record<string, string>`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title?: string | null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds?: number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens?: number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens?: number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens?: number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens?: number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost?: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens?: number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use?: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests?: number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests?: number`

          Number of server-executed web search requests.

          format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSessionEvent of client.beta.sessions.threads.events.list(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  { session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7" }
)) {
  console.log(betaManagedAgentsSessionEvent);
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

`client.beta.sessions.threads.events.stream(threadID, params, options?): BetaManagedAgentsStreamSessionThreadEvents | Stream<BetaManagedAgentsStreamSessionThreadEvents>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

### Parameters

- `threadID: string`

- `params: EventStreamParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `event_deltas?: Array<BetaManagedAgentsDeltaType>`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `"agent.message"`

    - `"agent.thinking"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 42 more`

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

      - `"user-profiles-2026-09-04"`

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

  - `workspace_id?: string`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in a single thread's stream.

  - `BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" | "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message?: string | null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: Array<BetaManagedAgentsSearchResultContent>`

          Array of text content blocks from the search result.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock>`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation?: BetaManagedAgentsAgentToolEvaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `BetaManagedAgentsAgentToolEvaluationAuto`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation?: BetaManagedAgentsAgentToolEvaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: "agent.thread_message_received"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name?: string | null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name?: string | null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: Array<string>`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

    - `type: "span.outcome_evaluation_start"`

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

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: "span.outcome_evaluation_end"`

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

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean | null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: "span.outcome_evaluation_ongoing"`

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

  - `BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number | null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent?: BetaManagedAgentsSessionAgent | null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: "agent"`

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1" | "claude-sonnet-5" | "claude-fable-5" | 11 more`

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

          - `(string & {})`

        - `effort?: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo?: string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed?: "standard" | "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: "coordinator"`

        - `agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: "agent"`

            - `id: string`

            - `description: string | null`

            - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

              - `type: "url"`

              - `name: string`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

              - `BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `type: "anthropic"`

                - `skill_id: string`

                - `version: string`

              - `BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `type: "custom"`

                - `skill_id: string`

                - `version: string`

            - `system: string | null`

            - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

              - `BetaManagedAgentsAgentToolset20260401`

                - `type: "agent_toolset_20260401"`

                - `configs: Array<BetaManagedAgentsAgentToolConfig>`

                  - `BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `type: "bash"`

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: "auto"`

                  - `BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `type: "edit"`

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `type: "read"`

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `type: "write"`

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `type: "glob"`

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `type: "grep"`

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `type: "web_fetch"`

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `max_content_tokens?: number | null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `type: "web_search"`

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `user_location?: BetaManagedAgentsUserLocation | null`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city?: string | null`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country?: string | null`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region?: string | null`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone?: string | null`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `BetaManagedAgentsMCPToolset`

                - `type: "mcp_toolset"`

                - `configs: Array<BetaManagedAgentsMCPToolConfig>`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: string`

              - `BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `type: "custom"`

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties?: Record<string, unknown> | null`

                  - `required?: Array<string> | null`

                - `name: string`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: "advisor"`

            - `model: string`

              The advisor model id.

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

        - `BetaManagedAgentsMCPToolset`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `version: number`

        format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: "limit"`

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata?: Record<string, string>`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title?: string | null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_start"`

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview`

        - `type: "agent.message"`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `BetaManagedAgentsAgentThinkingPreview`

        - `type: "agent.thinking"`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `BetaManagedAgentsDeltaEvent`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_delta"`

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: "content_delta"`

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `index?: number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds?: number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens?: number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens?: number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens?: number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens?: number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost?: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens?: number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use?: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests?: number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests?: number`

          Number of server-executed web search requests.

          format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsStreamSessionThreadEvents =
  await client.beta.sessions.threads.events.stream("sthr_011CZkZVWa6oIjw0rgXZpnBt", {
    session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
  });

console.log(betaManagedAgentsStreamSessionThreadEvents);
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
