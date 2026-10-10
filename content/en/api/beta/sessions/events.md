---
title: Events
url: https://platform.claude.com/docs/en/api/beta/sessions/events
---

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

  format: int32

- `order: optional "asc" or "desc"`

  Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination cursor from a previous response's `next_page`.

- `types: optional array of BetaManagedAgentsSessionEventType`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

  - `"user.message"`

  - `"user.interrupt"`

  - `"user.tool_confirmation"`

  - `"user.custom_tool_result"`

  - `"agent.custom_tool_use"`

  - `"agent.message"`

  - `"agent.thinking"`

  - `"agent.mcp_tool_use"`

  - `"agent.mcp_tool_result"`

  - `"agent.tool_use"`

  - `"agent.tool_result"`

  - `"agent.thread_message_received"`

  - `"agent.thread_message_sent"`

  - `"agent.thread_context_compacted"`

  - `"session.error"`

  - `"session.status_rescheduled"`

  - `"session.status_running"`

  - `"session.status_idle"`

  - `"session.status_terminated"`

  - `"session.thread_created"`

  - `"span.outcome_evaluation_start"`

  - `"span.outcome_evaluation_end"`

  - `"span.model_request_start"`

  - `"span.model_request_end"`

  - `"span.outcome_evaluation_ongoing"`

  - `"user.define_outcome"`

  - `"session.thread_status_running"`

  - `"session.thread_status_idle"`

  - `"session.thread_status_terminated"`

  - `"user.tool_result"`

  - `"session.thread_status_rescheduled"`

  - `"session.updated"`

  - `"system.message"`

  - `"session.usage"`

  - `"workflow_run.created"`

  - `"workflow_run.status_running"`

  - `"workflow_run.status_idle"`

  - `"workflow_run.status_ended"`

  - `"workflow_run.error"`

  - `"workflow_run.phase_started"`

  - `"workflow_run.phase_ended"`

### Headers

- `"anthropic-version": optional string`

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `data: optional array of BetaManagedAgentsSessionEvent`

  Events for the session, ordered by `processed_at`.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at: optional string or null`

      Timestamp when the agent finished processing this message.

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: optional string or null`

      Timestamp when the interrupt was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      Timestamp when the confirmation was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for this search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

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

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result. The client can send it as soon as this event arrives, without waiting for `session.status_idle`.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      Timestamp when this tool use was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      Timestamp when this response was generated.

      format: date-time

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this thinking was produced.

      format: date-time

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `BetaManagedAgentsAgentToolEvaluationAuto object`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's judgement for this invocation.

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

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

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

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

    - `type: "agent.thread_message_received"`

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

      Timestamp when the message was received.

      format: date-time

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

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

      Timestamp when the message was sent.

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when compaction was processed.

      format: date-time

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 10 more`

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

      - `BetaManagedAgentsRepositoryAuthenticationError object`

        The repository host rejected the credentials, or required credentials and received none.

        - `type: "repository_authentication_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryForbiddenError object`

        The repository host refused access to the repository.

        - `type: "repository_forbidden_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryNotFoundError object`

        The repository host reported the repository as not found.

        - `type: "repository_not_found_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCheckoutError object`

        The requested branch or commit does not exist in the repository.

        - `type: "repository_checkout_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCloneError object`

        The repository could not be cloned.

        - `type: "repository_clone_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

    - `processed_at: string`

      Timestamp when the error occurred.

      format: date-time

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the session stopped. `null` when there is nothing more to report.

      - `type: "refusal"`

      - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

        The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

        - `"cyber"`

        - `"bio"`

        - `"frontier_llm"`

        - `"reasoning_extraction"`

        - `"general_harms"`

      - `explanation: string or null`

        Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

        - `type: "refusal"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a child thread is created. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      Timestamp when the thread was created.

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `workflow_run_id: string or null`

      Identifier of the workflow run that created the thread, or `null` for any other thread.

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

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

      Timestamp when outcome evaluation started.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

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

      Timestamp when outcome evaluation ended.

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

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

        Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the model request started.

      format: date-time

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for this model request.

    - `processed_at: string`

      Timestamp when the model request completed.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

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

      Timestamp when this heartbeat was emitted.

      format: date-time

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

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

      Timestamp when the outcome was accepted.

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the session was deleted.

      format: date-time

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the thread stopped. `null` when there is nothing more to report.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the update was applied.

      format: date-time

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

      - `type: "agent"`

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-haiku-5-5"`

            Fastest model for high-volume, real-time tasks

          - `"claude-sonnet-5-5"`

            Efficient model for coding and agents

          - `"claude-opus-5-5"`

            Powerful intelligence for coding, knowledge work, and long-running agents

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-sonnet-5"`

            Efficient model for coding and agents

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

          - `"claude-haiku-4-5-20251001"`

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagent or null`

        Resolved multiagent orchestration configuration. Null when the agent is single-threaded.

        - `BetaManagedAgentsSessionMultiagentCoordinator object`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `type: "coordinator"`

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `BetaManagedAgentsSessionThreadAgent object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `type: "agent"`

              - `id: string`

              - `description: string or null`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `type: "url"`

                - `name: string`

                - `url: string`

              - `model: BetaManagedAgentsModelConfig`

                Model identifier and configuration.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `BetaManagedAgentsAnthropicSkill object`

                  A resolved Anthropic-managed skill.

                  - `type: "anthropic"`

                  - `skill_id: string`

                  - `version: string`

                - `BetaManagedAgentsCustomSkill object`

                  A resolved user-created custom skill.

                  - `type: "custom"`

                  - `skill_id: string`

                  - `version: string`

              - `system: string or null`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `BetaManagedAgentsAgentToolset20260401 object`

                  - `type: "agent_toolset_20260401"`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `BetaManagedAgentsBashToolConfig object`

                      Configuration for the bash tool.

                      - `type: "bash"`

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                          - `type: "auto"`

                    - `BetaManagedAgentsEditToolConfig object`

                      Configuration for the edit tool.

                      - `type: "edit"`

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsReadToolConfig object`

                      Configuration for the read tool.

                      - `type: "read"`

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWriteToolConfig object`

                      Configuration for the write tool.

                      - `type: "write"`

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGlobToolConfig object`

                      Configuration for the glob tool.

                      - `type: "glob"`

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGrepToolConfig object`

                      Configuration for the grep tool.

                      - `type: "grep"`

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWebFetchToolConfig object`

                      Configuration for the web_fetch tool.

                      - `type: "web_fetch"`

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `url_sources: BetaManagedAgentsWebFetchURLSources or null`

                        Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source.

                        - `client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                            - `type: "all"`

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                            - `type: "none"`

                          - `BetaManagedAgentsWebFetchURLSourceOnly object`

                            Only the named tools' results contribute URLs that may be fetched.

                            - `type: "only"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                          - `BetaManagedAgentsWebFetchURLSourceExcept object`

                            Every tool's results contribute URLs that may be fetched, except the named tools' results.

                            - `type: "except"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                        - `server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both.

                        - `user_input: BetaManagedAgentsWebFetchURLSourceUserInput or null`

                          Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number or null`

                        format: int32

                    - `BetaManagedAgentsWebSearchToolConfig object`

                      Configuration for the web_search tool.

                      - `type: "web_search"`

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsMCPToolset object`

                  - `type: "mcp_toolset"`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `mcp_server_name: string`

                - `BetaManagedAgentsCustomTool object`

                  A custom tool as returned in API responses.

                  - `type: "custom"`

                  - `description: string`

                  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown] or null`

                    - `required: optional array of string or null`

                  - `name: string`

              - `version: number`

                format: int32

            - `BetaManagedAgentsAdvisor object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `type: "advisor"`

              - `model: string`

                The advisor model id.

        - `BetaManagedAgentsSessionMultiagent20261001 object`

          Resolved multiagent configuration with three members, as copied to the `session` at creation.

          - `type: "multiagent_20261001"`

          - `advisor: BetaManagedAgentsMultiagentAdvisor`

            Whether the session's primary thread can consult an advisor model.

            - `BetaManagedAgentsMultiagentAdvisorEnabled object`

              The session's primary thread can consult `model` mid-turn.

              - `type: "enabled"`

              - `model: string`

                The advisor model id.

            - `BetaManagedAgentsMultiagentAdvisorDisabled object`

              The agent has no advisor.

              - `type: "disabled"`

          - `subagents: BetaManagedAgentsSessionMultiagentSubagents`

            Whether the agent can spawn session threads.

            - `BetaManagedAgentsSessionMultiagentSubagentsEnabled object`

              The agent can spawn session threads.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether the agent can define inline agents, which are not saved, when it spawns session threads.

                - `BetaManagedAgentsMultiagentInlineAgentsEnabled object`

                  The agent can define inline agents.

                  - `type: "enabled"`

                - `BetaManagedAgentsMultiagentInlineAgentsDisabled object`

                  The agent cannot define inline agents.

                  - `type: "disabled"`

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that this agent can spawn as session threads.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentSubagentsDisabled object`

              The agent cannot spawn session threads.

              - `type: "disabled"`

          - `workflows: BetaManagedAgentsSessionMultiagentWorkflows`

            Whether the agent can start workflow runs.

            - `BetaManagedAgentsSessionMultiagentWorkflowsEnabled object`

              The agent can start workflow runs.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether a run's plan can define inline agents, which are not saved.

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that a run's plan can use.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentWorkflowsDisabled object`

              The agent cannot start workflow runs.

              - `type: "disabled"`

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

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

      - `type: "limit"`

      - `max_list_cost: BetaMonetaryAmount`

        Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at: optional string or null`

      Timestamp when this system message was processed.

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the snapshot was taken.

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      The session's cumulative usage at the snapshot time.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Tokens used to create prompt cache entries, broken down by cache TTL.

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

        Cumulative list cost of the session across all turns, priced at public list rates.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative server-executed tool usage across all turns.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's configured budget at the snapshot time, or null when the session has no budget.

  - `BetaManagedAgentsWorkflowRunCreatedEvent object`

    A workflow run was created. A workflow run is background work that the session's agent starts. Emitted once per run, before the run's other `workflow_run.*` events.

    - `type: "workflow_run.created"`

    - `id: string`

      Unique identifier for this event.

    - `description: string or null`

      Description that the agent gave the run, passed on as written, or `null` if it gave none.

    - `name: string`

      Name that the agent gave the run, passed on as written, or a name that the server assigned.

    - `phases: array of BetaManagedAgentsWorkflowRunPhase`

      The phases that the run's plan declares, in the plan's order. Can be empty.

      - `id: string`

        Unique identifier for the phase.

      - `description: string or null`

        Description that the agent gave the phase, passed on as written, or `null` if it gave none.

      - `name: string`

        Name that the agent gave the phase, passed on as written.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusEndedEvent object`

    A workflow run ended. Emitted once per run, as the last of the run's `workflow_run.*` events.

    - `type: "workflow_run.status_ended"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `result: BetaManagedAgentsWorkflowRunResult`

      How the run ended.

      - `BetaManagedAgentsWorkflowRunResultCompleted object`

        The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

        - `type: "completed"`

      - `BetaManagedAgentsWorkflowRunResultError object`

        The run failed or reached its time limit.

        - `type: "error"`

        - `error: BetaManagedAgentsWorkflowRunError`

          Why the run did not finish.

          - `BetaManagedAgentsTimeoutWorkflowRunError object`

            The run reached its time limit.

            - `type: "timeout_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsProgramWorkflowRunError object`

            The plan, a program that the agent wrote, failed, or the server refused it.

            - `type: "program_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsUnknownWorkflowRunError object`

            A failure that has no type of its own.

            - `type: "unknown_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsThreadLimitWorkflowRunError object`

            The run exceeded the limit on the number of threads that a run can create.

            - `type: "thread_limit_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

            No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

            - `type: "max_workflow_runs_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsWorkflowRunResultStopped object`

        The agent stopped the run.

        - `type: "stopped"`

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunPhaseStartedEvent object`

    A workflow run's plan entered a phase.

    - `type: "workflow_run.phase_started"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunPhaseEndedEvent object`

    A workflow run's plan left a phase, or the run's end closed it. Emitted once for every `workflow_run.phase_started` event, before the run's `workflow_run.status_ended` event. The event does not say whether the plan finished the phase's work, or why it left.

    - `type: "workflow_run.phase_ended"`

    - `id: string`

      Unique identifier for this event.

    - `phase_started_id: string`

      Identifier of the `workflow_run.phase_started` event that opened the phase.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunStatusRunningEvent object`

    A workflow run is running. Emitted when the run starts to execute, and each time it resumes after being idle. A run that starts idle emits `workflow_run.status_idle` first.

    - `type: "workflow_run.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusIdleEvent object`

    A workflow run is idle. Emitted each time the run goes idle, whatever the cause. If the run ends while idle, no `workflow_run.status_running` comes between this event and its `workflow_run.status_ended`.

    - `type: "workflow_run.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunErrorEvent object`

    A workflow run met an error, or an error kept a run from being created. A run that ends with a `result.type` of `error` emits this event before its `workflow_run.status_ended`, with the same `error`.

    - `type: "workflow_run.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsWorkflowRunError`

      Why the run did not finish, or was not created.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string or null`

      Identifier of the run that met the error, or `null` when the error kept a run from being created.

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
      "id": "sevt_011CZkZGPp1iBcp4kaQSihUm",
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
      "id": "sevt_011CZkZHPq1jCdq5mbRTjiVn",
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

- `"anthropic-version": optional string`

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Body parameters

- `events: array of BetaManagedAgentsEventParams`

  Events to send to the `session`.

  - `BetaManagedAgentsUserMessageEventParams object`

    Parameters for sending a user message to the session.

    - `type: "user.message"`

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

  - `BetaManagedAgentsUserInterruptEventParams object`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEventParams object`

    Parameters for confirming or denying a tool execution request.

    - `type: "user.tool_confirmation"`

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `BetaManagedAgentsUserCustomToolResultEventParams object`

    Parameters for providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

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

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for this search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

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

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsUserDefineOutcomeEventParams object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: "user.define_outcome"`

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      How to grade the outcome. Text or file reference.

      - `BetaManagedAgentsFileRubricParams object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubricParams object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: optional number or null`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `BetaManagedAgentsUserToolResultEventParams object`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

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

    - `type: "system.message"`

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

### Returns

- `BetaManagedAgentsSendSessionEvents object`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 4 more`

    Sent events

    - `BetaManagedAgentsUserMessageEvent object`

      A user message event in the session conversation.

      - `type: "user.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: "image"`

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            The source of the image data.

            - `BetaManagedAgentsBase64ImageSource object`

              Base64-encoded image data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `BetaManagedAgentsURLImageSource object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `BetaManagedAgentsFileImageSource object`

              Image referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: "document"`

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            The source of the document data.

            - `BetaManagedAgentsBase64DocumentSource object`

              Base64-encoded document data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `BetaManagedAgentsPlainTextDocumentSource object`

              Plain text document content.

              - `type: "text"`

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

            - `BetaManagedAgentsURLDocumentSource object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `BetaManagedAgentsFileDocumentSource object`

              Document referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

          - `context: optional string or null`

            Additional context about the document for the model.

          - `title: optional string or null`

            The title of the document.

        - `BetaManagedAgentsRedactedBlock object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `processed_at: optional string or null`

        Timestamp when the agent finished processing this message.

        format: date-time

    - `BetaManagedAgentsUserInterruptEvent object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `type: "user.interrupt"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: optional string or null`

        Timestamp when the interrupt was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `BetaManagedAgentsUserToolConfirmationEvent object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `type: "user.tool_confirmation"`

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        The confirmation result: 'allow' or 'deny'.

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `deny_message: optional string or null`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string or null`

        Timestamp when the confirmation was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

    - `BetaManagedAgentsUserCustomToolResultEvent object`

      Event sent by the client providing the result of a custom tool execution.

      - `type: "user.custom_tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

          - `type: "search_result"`

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for this search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

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

      - `is_error: optional boolean or null`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string or null`

        Timestamp when this result was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

    - `BetaManagedAgentsUserDefineOutcomeEvent object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `type: "user.define_outcome"`

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

        Timestamp when the outcome was accepted.

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

        - `BetaManagedAgentsFileRubric object`

          Rubric referenced by a file uploaded via the Files API.

          - `type: "file"`

          - `file_id: string`

            ID of the rubric file.

        - `BetaManagedAgentsTextRubric object`

          Rubric content provided inline as text.

          - `type: "text"`

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

    - `BetaManagedAgentsUserToolResultEvent object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `type: "user.tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        Timestamp when this result was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

    - `BetaManagedAgentsSystemMessageEvent object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `type: "system.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `processed_at: optional string or null`

        Timestamp when this system message was processed.

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
      "id": "sevt_011CZkZGPp1iBcp4kaQSihUm",
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

- `"anthropic-version": optional string`

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 41 more`

  Server-sent event in the session stream.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at: optional string or null`

      Timestamp when the agent finished processing this message.

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: optional string or null`

      Timestamp when the interrupt was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      Timestamp when the confirmation was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for this search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

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

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result. The client can send it as soon as this event arrives, without waiting for `session.status_idle`.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      Timestamp when this tool use was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      Timestamp when this response was generated.

      format: date-time

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this thinking was produced.

      format: date-time

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `BetaManagedAgentsAgentToolEvaluationAuto object`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's judgement for this invocation.

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

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

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

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

    - `type: "agent.thread_message_received"`

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

      Timestamp when the message was received.

      format: date-time

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

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

      Timestamp when the message was sent.

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when compaction was processed.

      format: date-time

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 10 more`

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

      - `BetaManagedAgentsRepositoryAuthenticationError object`

        The repository host rejected the credentials, or required credentials and received none.

        - `type: "repository_authentication_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryForbiddenError object`

        The repository host refused access to the repository.

        - `type: "repository_forbidden_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryNotFoundError object`

        The repository host reported the repository as not found.

        - `type: "repository_not_found_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCheckoutError object`

        The requested branch or commit does not exist in the repository.

        - `type: "repository_checkout_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCloneError object`

        The repository could not be cloned.

        - `type: "repository_clone_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

    - `processed_at: string`

      Timestamp when the error occurred.

      format: date-time

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the session stopped. `null` when there is nothing more to report.

      - `type: "refusal"`

      - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

        The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

        - `"cyber"`

        - `"bio"`

        - `"frontier_llm"`

        - `"reasoning_extraction"`

        - `"general_harms"`

      - `explanation: string or null`

        Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

        - `type: "refusal"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a child thread is created. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      Timestamp when the thread was created.

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `workflow_run_id: string or null`

      Identifier of the workflow run that created the thread, or `null` for any other thread.

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

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

      Timestamp when outcome evaluation started.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

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

      Timestamp when outcome evaluation ended.

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

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

        Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the model request started.

      format: date-time

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for this model request.

    - `processed_at: string`

      Timestamp when the model request completed.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

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

      Timestamp when this heartbeat was emitted.

      format: date-time

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

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

      Timestamp when the outcome was accepted.

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the session was deleted.

      format: date-time

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the thread stopped. `null` when there is nothing more to report.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the update was applied.

      format: date-time

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

      - `type: "agent"`

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-haiku-5-5"`

            Fastest model for high-volume, real-time tasks

          - `"claude-sonnet-5-5"`

            Efficient model for coding and agents

          - `"claude-opus-5-5"`

            Powerful intelligence for coding, knowledge work, and long-running agents

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-sonnet-5"`

            Efficient model for coding and agents

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

          - `"claude-haiku-4-5-20251001"`

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagent or null`

        Resolved multiagent orchestration configuration. Null when the agent is single-threaded.

        - `BetaManagedAgentsSessionMultiagentCoordinator object`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `type: "coordinator"`

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `BetaManagedAgentsSessionThreadAgent object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `type: "agent"`

              - `id: string`

              - `description: string or null`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `type: "url"`

                - `name: string`

                - `url: string`

              - `model: BetaManagedAgentsModelConfig`

                Model identifier and configuration.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `BetaManagedAgentsAnthropicSkill object`

                  A resolved Anthropic-managed skill.

                  - `type: "anthropic"`

                  - `skill_id: string`

                  - `version: string`

                - `BetaManagedAgentsCustomSkill object`

                  A resolved user-created custom skill.

                  - `type: "custom"`

                  - `skill_id: string`

                  - `version: string`

              - `system: string or null`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `BetaManagedAgentsAgentToolset20260401 object`

                  - `type: "agent_toolset_20260401"`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `BetaManagedAgentsBashToolConfig object`

                      Configuration for the bash tool.

                      - `type: "bash"`

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                          - `type: "auto"`

                    - `BetaManagedAgentsEditToolConfig object`

                      Configuration for the edit tool.

                      - `type: "edit"`

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsReadToolConfig object`

                      Configuration for the read tool.

                      - `type: "read"`

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWriteToolConfig object`

                      Configuration for the write tool.

                      - `type: "write"`

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGlobToolConfig object`

                      Configuration for the glob tool.

                      - `type: "glob"`

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGrepToolConfig object`

                      Configuration for the grep tool.

                      - `type: "grep"`

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWebFetchToolConfig object`

                      Configuration for the web_fetch tool.

                      - `type: "web_fetch"`

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `url_sources: BetaManagedAgentsWebFetchURLSources or null`

                        Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source.

                        - `client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                            - `type: "all"`

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                            - `type: "none"`

                          - `BetaManagedAgentsWebFetchURLSourceOnly object`

                            Only the named tools' results contribute URLs that may be fetched.

                            - `type: "only"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                          - `BetaManagedAgentsWebFetchURLSourceExcept object`

                            Every tool's results contribute URLs that may be fetched, except the named tools' results.

                            - `type: "except"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                        - `server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both.

                        - `user_input: BetaManagedAgentsWebFetchURLSourceUserInput or null`

                          Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number or null`

                        format: int32

                    - `BetaManagedAgentsWebSearchToolConfig object`

                      Configuration for the web_search tool.

                      - `type: "web_search"`

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsMCPToolset object`

                  - `type: "mcp_toolset"`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `mcp_server_name: string`

                - `BetaManagedAgentsCustomTool object`

                  A custom tool as returned in API responses.

                  - `type: "custom"`

                  - `description: string`

                  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown] or null`

                    - `required: optional array of string or null`

                  - `name: string`

              - `version: number`

                format: int32

            - `BetaManagedAgentsAdvisor object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `type: "advisor"`

              - `model: string`

                The advisor model id.

        - `BetaManagedAgentsSessionMultiagent20261001 object`

          Resolved multiagent configuration with three members, as copied to the `session` at creation.

          - `type: "multiagent_20261001"`

          - `advisor: BetaManagedAgentsMultiagentAdvisor`

            Whether the session's primary thread can consult an advisor model.

            - `BetaManagedAgentsMultiagentAdvisorEnabled object`

              The session's primary thread can consult `model` mid-turn.

              - `type: "enabled"`

              - `model: string`

                The advisor model id.

            - `BetaManagedAgentsMultiagentAdvisorDisabled object`

              The agent has no advisor.

              - `type: "disabled"`

          - `subagents: BetaManagedAgentsSessionMultiagentSubagents`

            Whether the agent can spawn session threads.

            - `BetaManagedAgentsSessionMultiagentSubagentsEnabled object`

              The agent can spawn session threads.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether the agent can define inline agents, which are not saved, when it spawns session threads.

                - `BetaManagedAgentsMultiagentInlineAgentsEnabled object`

                  The agent can define inline agents.

                  - `type: "enabled"`

                - `BetaManagedAgentsMultiagentInlineAgentsDisabled object`

                  The agent cannot define inline agents.

                  - `type: "disabled"`

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that this agent can spawn as session threads.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentSubagentsDisabled object`

              The agent cannot spawn session threads.

              - `type: "disabled"`

          - `workflows: BetaManagedAgentsSessionMultiagentWorkflows`

            Whether the agent can start workflow runs.

            - `BetaManagedAgentsSessionMultiagentWorkflowsEnabled object`

              The agent can start workflow runs.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether a run's plan can define inline agents, which are not saved.

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that a run's plan can use.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentWorkflowsDisabled object`

              The agent cannot start workflow runs.

              - `type: "disabled"`

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

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

      - `type: "limit"`

      - `max_list_cost: BetaMonetaryAmount`

        Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_start"`

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview object`

        - `type: "agent.message"`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `BetaManagedAgentsAgentThinkingPreview object`

        - `type: "agent.thinking"`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `BetaManagedAgentsDeltaEvent object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_delta"`

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: "content_delta"`

      - `content: BetaManagedAgentsTextBlock`

        A partial element of the content array at index, typed like the element itself — the same shape the buffered agent.message carries in content.

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at: optional string or null`

      Timestamp when this system message was processed.

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the snapshot was taken.

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      The session's cumulative usage at the snapshot time.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Tokens used to create prompt cache entries, broken down by cache TTL.

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

        Cumulative list cost of the session across all turns, priced at public list rates.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative server-executed tool usage across all turns.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's configured budget at the snapshot time, or null when the session has no budget.

  - `BetaManagedAgentsWorkflowRunCreatedEvent object`

    A workflow run was created. A workflow run is background work that the session's agent starts. Emitted once per run, before the run's other `workflow_run.*` events.

    - `type: "workflow_run.created"`

    - `id: string`

      Unique identifier for this event.

    - `description: string or null`

      Description that the agent gave the run, passed on as written, or `null` if it gave none.

    - `name: string`

      Name that the agent gave the run, passed on as written, or a name that the server assigned.

    - `phases: array of BetaManagedAgentsWorkflowRunPhase`

      The phases that the run's plan declares, in the plan's order. Can be empty.

      - `id: string`

        Unique identifier for the phase.

      - `description: string or null`

        Description that the agent gave the phase, passed on as written, or `null` if it gave none.

      - `name: string`

        Name that the agent gave the phase, passed on as written.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusEndedEvent object`

    A workflow run ended. Emitted once per run, as the last of the run's `workflow_run.*` events.

    - `type: "workflow_run.status_ended"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `result: BetaManagedAgentsWorkflowRunResult`

      How the run ended.

      - `BetaManagedAgentsWorkflowRunResultCompleted object`

        The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

        - `type: "completed"`

      - `BetaManagedAgentsWorkflowRunResultError object`

        The run failed or reached its time limit.

        - `type: "error"`

        - `error: BetaManagedAgentsWorkflowRunError`

          Why the run did not finish.

          - `BetaManagedAgentsTimeoutWorkflowRunError object`

            The run reached its time limit.

            - `type: "timeout_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsProgramWorkflowRunError object`

            The plan, a program that the agent wrote, failed, or the server refused it.

            - `type: "program_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsUnknownWorkflowRunError object`

            A failure that has no type of its own.

            - `type: "unknown_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsThreadLimitWorkflowRunError object`

            The run exceeded the limit on the number of threads that a run can create.

            - `type: "thread_limit_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

            No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

            - `type: "max_workflow_runs_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsWorkflowRunResultStopped object`

        The agent stopped the run.

        - `type: "stopped"`

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunPhaseStartedEvent object`

    A workflow run's plan entered a phase.

    - `type: "workflow_run.phase_started"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunPhaseEndedEvent object`

    A workflow run's plan left a phase, or the run's end closed it. Emitted once for every `workflow_run.phase_started` event, before the run's `workflow_run.status_ended` event. The event does not say whether the plan finished the phase's work, or why it left.

    - `type: "workflow_run.phase_ended"`

    - `id: string`

      Unique identifier for this event.

    - `phase_started_id: string`

      Identifier of the `workflow_run.phase_started` event that opened the phase.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunStatusRunningEvent object`

    A workflow run is running. Emitted when the run starts to execute, and each time it resumes after being idle. A run that starts idle emits `workflow_run.status_idle` first.

    - `type: "workflow_run.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusIdleEvent object`

    A workflow run is idle. Emitted each time the run goes idle, whatever the cause. If the run ends while idle, no `workflow_run.status_running` comes between this event and its `workflow_run.status_ended`.

    - `type: "workflow_run.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunErrorEvent object`

    A workflow run met an error, or an error kept a run from being created. A run that ends with a `result.type` of `error` emits this event before its `workflow_run.status_ended`, with the same `error`.

    - `type: "workflow_run.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsWorkflowRunError`

      Why the run did not finish, or was not created.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string or null`

      Identifier of the run that met the error, or `null` when the error kept a run from being created.

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
  "id": "sevt_011CZkZGPp1iBcp4kaQSihUm",
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

### Beta Managed Agents Agent Auto Evaluated Permission

- `BetaManagedAgentsAgentAutoEvaluatedPermission = BetaManagedAgentsAgentAutoEvaluatedPermissionAllow or BetaManagedAgentsAgentAutoEvaluatedPermissionAsk or BetaManagedAgentsAgentAutoEvaluatedPermissionDeny`

  The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

  - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

    The server judged the invocation safe to execute without client approval.

    - `type: "allow"`

  - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

    The server reached no judgement; the invocation is held for client approval.

    - `type: "ask"`

    - `reason_code: string`

      The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

      maxLength: 64

  - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

    The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

    - `type: "deny"`

    - `reason_code: string`

      The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

      maxLength: 64

### Beta Managed Agents Agent Auto Evaluated Permission Allow

- `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

  The server judged the invocation safe to execute without client approval.

  - `type: "allow"`

### Beta Managed Agents Agent Auto Evaluated Permission Ask

- `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

  The server reached no judgement; the invocation is held for client approval.

  - `type: "ask"`

  - `reason_code: string`

    The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

    maxLength: 64

### Beta Managed Agents Agent Auto Evaluated Permission Deny

- `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

  The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

  - `type: "deny"`

  - `reason_code: string`

    The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

    maxLength: 64

### Beta Managed Agents Agent Custom Tool Use Event

- `BetaManagedAgentsAgentCustomToolUseEvent object`

  Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result. The client can send it as soon as this event arrives, without waiting for `session.status_idle`.

  - `type: "agent.custom_tool_use"`

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `name: string`

    Name of the custom tool being called.

  - `processed_at: string`

    Timestamp when this tool use was processed.

    format: date-time

  - `session_thread_id: optional string or null`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

### Beta Managed Agents Agent Evaluated Permission

- `BetaManagedAgentsAgentEvaluatedPermission = "allow" or "ask" or "deny"`

  - `"allow"`

  - `"ask"`

  - `"deny"`

### Beta Managed Agents Agent MCP Tool Result Event

- `BetaManagedAgentsAgentMCPToolResultEvent object`

  Event representing the result of an MCP tool execution.

  - `type: "agent.mcp_tool_result"`

  - `id: string`

    Unique identifier for this event.

  - `mcp_tool_use_id: string`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `type: "search_result"`

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for this search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

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

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

- `BetaManagedAgentsAgentMCPToolUseEvent object`

  Event emitted when the agent invokes a tool provided by an MCP server.

  - `type: "agent.mcp_tool_use"`

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `mcp_server_name: string`

    Name of the MCP server providing the tool.

  - `name: string`

    Name of the MCP tool being used.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

    The evaluated permission policy for this tool invocation.

    - `"allow"`

    - `"ask"`

    - `"deny"`

  - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

    Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

      The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

      - `type: "always_allow"`

    - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

      The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

      - `type: "always_ask"`

    - `BetaManagedAgentsAgentToolEvaluationAuto object`

      The resolved permission_policy was auto: the server judged this invocation individually.

      - `type: "auto"`

      - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

        The server's judgement for this invocation.

        - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

          The server judged the invocation safe to execute without client approval.

          - `type: "allow"`

        - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

          The server reached no judgement; the invocation is held for client approval.

          - `type: "ask"`

          - `reason_code: string`

            The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

            maxLength: 64

        - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

          The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

          - `type: "deny"`

          - `reason_code: string`

            The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

            maxLength: 64

  - `session_thread_id: optional string or null`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

### Beta Managed Agents Agent Message Event

- `BetaManagedAgentsAgentMessageEvent object`

  An agent response event in the session conversation.

  - `type: "agent.message"`

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

    Array of text blocks comprising the agent response.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `processed_at: string`

    Timestamp when this response was generated.

    format: date-time

### Beta Managed Agents Agent Thinking Event

- `BetaManagedAgentsAgentThinkingEvent object`

  Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `type: "agent.thinking"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when this thinking was produced.

    format: date-time

### Beta Managed Agents Agent Thread Context Compacted Event

- `BetaManagedAgentsAgentThreadContextCompactedEvent object`

  Indicates that context compaction (summarization) occurred during the session.

  - `type: "agent.thread_context_compacted"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when compaction was processed.

    format: date-time

### Beta Managed Agents Agent Thread Message Received Event

- `BetaManagedAgentsAgentThreadMessageReceivedEvent object`

  Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

  - `type: "agent.thread_message_received"`

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Message content blocks.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

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

    Timestamp when the message was received.

    format: date-time

  - `from_agent_name: optional string or null`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `BetaManagedAgentsAgentThreadMessageSentEvent object`

  Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

  - `type: "agent.thread_message_sent"`

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Message content blocks.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `processed_at: string`

    Timestamp when the message was sent.

    format: date-time

  - `to_session_thread_id: string`

    Public `sthr_` ID of the thread the message was sent to.

  - `to_agent_name: optional string or null`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Evaluation

- `BetaManagedAgentsAgentToolEvaluation = BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

  Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

  - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

    The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

    - `type: "always_allow"`

  - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

    The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

    - `type: "always_ask"`

  - `BetaManagedAgentsAgentToolEvaluationAuto object`

    The resolved permission_policy was auto: the server judged this invocation individually.

    - `type: "auto"`

    - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

      The server's judgement for this invocation.

      - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

        The server judged the invocation safe to execute without client approval.

        - `type: "allow"`

      - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

        The server reached no judgement; the invocation is held for client approval.

        - `type: "ask"`

        - `reason_code: string`

          The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

          maxLength: 64

      - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

        The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

        - `type: "deny"`

        - `reason_code: string`

          The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

          maxLength: 64

### Beta Managed Agents Agent Tool Evaluation Always Allow

- `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

  The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

  - `type: "always_allow"`

### Beta Managed Agents Agent Tool Evaluation Always Ask

- `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

  The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

  - `type: "always_ask"`

### Beta Managed Agents Agent Tool Evaluation Auto

- `BetaManagedAgentsAgentToolEvaluationAuto object`

  The resolved permission_policy was auto: the server judged this invocation individually.

  - `type: "auto"`

  - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

    The server's judgement for this invocation.

    - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

      The server judged the invocation safe to execute without client approval.

      - `type: "allow"`

    - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

      The server reached no judgement; the invocation is held for client approval.

      - `type: "ask"`

      - `reason_code: string`

        The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

        maxLength: 64

    - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

      The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

      - `type: "deny"`

      - `reason_code: string`

        The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

        maxLength: 64

### Beta Managed Agents Agent Tool Result Event

- `BetaManagedAgentsAgentToolResultEvent object`

  Event representing the result of an agent tool execution.

  - `type: "agent.tool_result"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to.

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `type: "search_result"`

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for this search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

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

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `BetaManagedAgentsAgentToolUseEvent object`

  Event emitted when the agent invokes a built-in agent tool.

  - `type: "agent.tool_use"`

  - `id: string`

    Unique identifier for this event.

  - `input: map[unknown]`

    Input parameters for the tool call.

  - `name: string`

    Name of the agent tool being used.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

    The evaluated permission policy for this tool invocation.

    - `"allow"`

    - `"ask"`

    - `"deny"`

  - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

    Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

      The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

      - `type: "always_allow"`

    - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

      The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

      - `type: "always_ask"`

    - `BetaManagedAgentsAgentToolEvaluationAuto object`

      The resolved permission_policy was auto: the server judged this invocation individually.

      - `type: "auto"`

      - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

        The server's judgement for this invocation.

        - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

          The server judged the invocation safe to execute without client approval.

          - `type: "allow"`

        - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

          The server reached no judgement; the invocation is held for client approval.

          - `type: "ask"`

          - `reason_code: string`

            The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

            maxLength: 64

        - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

          The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

          - `type: "deny"`

          - `reason_code: string`

            The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

            maxLength: 64

  - `session_thread_id: optional string or null`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

### Beta Managed Agents Base64 Document Source

- `BetaManagedAgentsBase64DocumentSource object`

  Base64-encoded document data.

  - `type: "base64"`

  - `data: string`

    Base64-encoded document data.

    minLength: 1

  - `media_type: string`

    MIME type of the document (e.g., "application/pdf").

    minLength: 1

### Beta Managed Agents Base64 Image Source

- `BetaManagedAgentsBase64ImageSource object`

  Base64-encoded image data.

  - `type: "base64"`

  - `data: string`

    Base64-encoded image data.

    minLength: 1

  - `media_type: string`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

    minLength: 1

### Beta Managed Agents Billing Error

- `BetaManagedAgentsBillingError object`

  The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

  - `type: "billing_error"`

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Credential Host Unreachable Error

- `BetaManagedAgentsCredentialHostUnreachableError object`

  An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

  - `type: "credential_host_unreachable_error"`

  - `credential_id: string`

    ID of the affected credential.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

  - `vault_id: string`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `BetaManagedAgentsDocumentBlock object`

  Document content, either specified directly as base64 data, as text, or as a reference via a URL.

  - `type: "document"`

  - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

    The source of the document data.

    - `BetaManagedAgentsBase64DocumentSource object`

      Base64-encoded document data.

      - `type: "base64"`

      - `data: string`

        Base64-encoded document data.

        minLength: 1

      - `media_type: string`

        MIME type of the document (e.g., "application/pdf").

        minLength: 1

    - `BetaManagedAgentsPlainTextDocumentSource object`

      Plain text document content.

      - `type: "text"`

      - `data: string`

        The plain text content.

        minLength: 1

      - `media_type: "text/plain"`

        MIME type of the text content. Must be "text/plain".

    - `BetaManagedAgentsURLDocumentSource object`

      Document referenced by URL.

      - `type: "url"`

      - `url: string`

        URL of the document to fetch.

        minLength: 1

    - `BetaManagedAgentsFileDocumentSource object`

      Document referenced by file ID.

      - `type: "file"`

      - `file_id: string`

        ID of a previously uploaded file.

        minLength: 1

  - `context: optional string or null`

    Additional context about the document for the model.

  - `title: optional string or null`

    The title of the document.

### Beta Managed Agents Event Params

- `BetaManagedAgentsEventParams = BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserInterruptEventParams or BetaManagedAgentsUserToolConfirmationEventParams or 4 more`

  Union type for event parameters that can be sent to a session.

  - `BetaManagedAgentsUserMessageEventParams object`

    Parameters for sending a user message to the session.

    - `type: "user.message"`

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

  - `BetaManagedAgentsUserInterruptEventParams object`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEventParams object`

    Parameters for confirming or denying a tool execution request.

    - `type: "user.tool_confirmation"`

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `BetaManagedAgentsUserCustomToolResultEventParams object`

    Parameters for providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

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

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for this search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

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

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsUserDefineOutcomeEventParams object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: "user.define_outcome"`

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      How to grade the outcome. Text or file reference.

      - `BetaManagedAgentsFileRubricParams object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubricParams object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: optional number or null`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `BetaManagedAgentsUserToolResultEventParams object`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

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

    - `type: "system.message"`

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

### Beta Managed Agents File Document Source

- `BetaManagedAgentsFileDocumentSource object`

  Document referenced by file ID.

  - `type: "file"`

  - `file_id: string`

    ID of a previously uploaded file.

    minLength: 1

### Beta Managed Agents File Image Source

- `BetaManagedAgentsFileImageSource object`

  Image referenced by file ID.

  - `type: "file"`

  - `file_id: string`

    ID of a previously uploaded file.

    minLength: 1

### Beta Managed Agents File Rubric

- `BetaManagedAgentsFileRubric object`

  Rubric referenced by a file uploaded via the Files API.

  - `type: "file"`

  - `file_id: string`

    ID of the rubric file.

### Beta Managed Agents File Rubric Params

- `BetaManagedAgentsFileRubricParams object`

  Rubric referenced by a file uploaded via the Files API.

  - `type: "file"`

  - `file_id: string`

    ID of the rubric file.

### Beta Managed Agents Image Block

- `BetaManagedAgentsImageBlock object`

  Image content specified directly as base64 data or as a reference via a URL.

  - `type: "image"`

  - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

    The source of the image data.

    - `BetaManagedAgentsBase64ImageSource object`

      Base64-encoded image data.

      - `type: "base64"`

      - `data: string`

        Base64-encoded image data.

        minLength: 1

      - `media_type: string`

        MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

        minLength: 1

    - `BetaManagedAgentsURLImageSource object`

      Image referenced by URL.

      - `type: "url"`

      - `url: string`

        URL of the image to fetch.

        minLength: 1

    - `BetaManagedAgentsFileImageSource object`

      Image referenced by file ID.

      - `type: "file"`

      - `file_id: string`

        ID of a previously uploaded file.

        minLength: 1

### Beta Managed Agents Max Workflow Runs Workflow Run Error

- `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

  No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

  - `type: "max_workflow_runs_error"`

  - `message: string`

    Short explanation written by the server. It never contains content from the run or its agents.

### Beta Managed Agents MCP Authentication Failed Error

- `BetaManagedAgentsMCPAuthenticationFailedError object`

  Authentication to an MCP server failed.

  - `type: "mcp_authentication_failed_error"`

  - `mcp_server_name: string`

    Name of the MCP server that failed authentication.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents MCP Connection Failed Error

- `BetaManagedAgentsMCPConnectionFailedError object`

  Failed to connect to an MCP server.

  - `type: "mcp_connection_failed_error"`

  - `mcp_server_name: string`

    Name of the MCP server that failed to connect.

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Model Overloaded Error

- `BetaManagedAgentsModelOverloadedError object`

  The model is currently overloaded. Emitted after automatic retries are exhausted.

  - `type: "model_overloaded_error"`

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Model Rate Limited Error

- `BetaManagedAgentsModelRateLimitedError object`

  The model request was rate-limited.

  - `type: "model_rate_limited_error"`

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Model Request Failed Error

- `BetaManagedAgentsModelRequestFailedError object`

  A model request failed for a reason other than overload or rate-limiting.

  - `type: "model_request_failed_error"`

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Plain Text Document Source

- `BetaManagedAgentsPlainTextDocumentSource object`

  Plain text document content.

  - `type: "text"`

  - `data: string`

    The plain text content.

    minLength: 1

  - `media_type: "text/plain"`

    MIME type of the text content. Must be "text/plain".

### Beta Managed Agents Program Workflow Run Error

- `BetaManagedAgentsProgramWorkflowRunError object`

  The plan, a program that the agent wrote, failed, or the server refused it.

  - `type: "program_error"`

  - `message: string`

    Short explanation written by the server. It never contains content from the run or its agents.

### Beta Managed Agents Redacted Block

- `BetaManagedAgentsRedactedBlock object`

  Placeholder for content withheld by Anthropic model policy.

  - `type: "redacted"`

### Beta Managed Agents Repository Authentication Error

- `BetaManagedAgentsRepositoryAuthenticationError object`

  The repository host rejected the credentials, or required credentials and received none.

  - `type: "repository_authentication_error"`

  - `message: string`

    Human-readable error description.

  - `repository_url: string or null`

    URL of the repository that could not be cloned. Null when it could not be identified.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next. Always `retrying`: the session keeps running without the repository.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Repository Checkout Error

- `BetaManagedAgentsRepositoryCheckoutError object`

  The requested branch or commit does not exist in the repository.

  - `type: "repository_checkout_error"`

  - `message: string`

    Human-readable error description.

  - `repository_url: string or null`

    URL of the repository that could not be cloned. Null when it could not be identified.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next. Always `retrying`: the session keeps running without the repository.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Repository Clone Error

- `BetaManagedAgentsRepositoryCloneError object`

  The repository could not be cloned.

  - `type: "repository_clone_error"`

  - `message: string`

    Human-readable error description.

  - `repository_url: string or null`

    URL of the repository that could not be cloned. Null when it could not be identified.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next. Always `retrying`: the session keeps running without the repository.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Repository Forbidden Error

- `BetaManagedAgentsRepositoryForbiddenError object`

  The repository host refused access to the repository.

  - `type: "repository_forbidden_error"`

  - `message: string`

    Human-readable error description.

  - `repository_url: string or null`

    URL of the repository that could not be cloned. Null when it could not be identified.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next. Always `retrying`: the session keeps running without the repository.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Repository Not Found Error

- `BetaManagedAgentsRepositoryNotFoundError object`

  The repository host reported the repository as not found.

  - `type: "repository_not_found_error"`

  - `message: string`

    Human-readable error description.

  - `repository_url: string or null`

    URL of the repository that could not be cloned. Null when it could not be identified.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next. Always `retrying`: the session keeps running without the repository.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

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

  - `type: "search_result"`

  - `citations: BetaManagedAgentsSearchResultCitations`

    Citation settings for this search result.

    - `enabled: boolean`

      Whether citations are enabled for this search result.

  - `content: array of BetaManagedAgentsSearchResultContent`

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

### Beta Managed Agents Search Result Citations

- `BetaManagedAgentsSearchResultCitations object`

  Citation settings for a search result.

  - `enabled: boolean`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `BetaManagedAgentsSearchResultContent object`

  Text content within a search result.

  - `type: "text"`

  - `text: string`

    The text content.

    minLength: 1

### Beta Managed Agents Send Session Events

- `BetaManagedAgentsSendSessionEvents object`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 4 more`

    Sent events

    - `BetaManagedAgentsUserMessageEvent object`

      A user message event in the session conversation.

      - `type: "user.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `BetaManagedAgentsTextBlock object`

          Regular text content.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `BetaManagedAgentsImageBlock object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: "image"`

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            The source of the image data.

            - `BetaManagedAgentsBase64ImageSource object`

              Base64-encoded image data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `BetaManagedAgentsURLImageSource object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `BetaManagedAgentsFileImageSource object`

              Image referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

        - `BetaManagedAgentsDocumentBlock object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: "document"`

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            The source of the document data.

            - `BetaManagedAgentsBase64DocumentSource object`

              Base64-encoded document data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `BetaManagedAgentsPlainTextDocumentSource object`

              Plain text document content.

              - `type: "text"`

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

            - `BetaManagedAgentsURLDocumentSource object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `BetaManagedAgentsFileDocumentSource object`

              Document referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

          - `context: optional string or null`

            Additional context about the document for the model.

          - `title: optional string or null`

            The title of the document.

        - `BetaManagedAgentsRedactedBlock object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `processed_at: optional string or null`

        Timestamp when the agent finished processing this message.

        format: date-time

    - `BetaManagedAgentsUserInterruptEvent object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `type: "user.interrupt"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: optional string or null`

        Timestamp when the interrupt was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `BetaManagedAgentsUserToolConfirmationEvent object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `type: "user.tool_confirmation"`

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        The confirmation result: 'allow' or 'deny'.

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `deny_message: optional string or null`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string or null`

        Timestamp when the confirmation was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

    - `BetaManagedAgentsUserCustomToolResultEvent object`

      Event sent by the client providing the result of a custom tool execution.

      - `type: "user.custom_tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

          - `type: "search_result"`

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for this search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

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

      - `is_error: optional boolean or null`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string or null`

        Timestamp when this result was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

    - `BetaManagedAgentsUserDefineOutcomeEvent object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `type: "user.define_outcome"`

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

        Timestamp when the outcome was accepted.

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

        - `BetaManagedAgentsFileRubric object`

          Rubric referenced by a file uploaded via the Files API.

          - `type: "file"`

          - `file_id: string`

            ID of the rubric file.

        - `BetaManagedAgentsTextRubric object`

          Rubric content provided inline as text.

          - `type: "text"`

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

    - `BetaManagedAgentsUserToolResultEvent object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `type: "user.tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        Timestamp when this result was processed.

        format: date-time

      - `session_thread_id: optional string or null`

        Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

    - `BetaManagedAgentsSystemMessageEvent object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `type: "system.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `processed_at: optional string or null`

        Timestamp when this system message was processed.

        format: date-time

### Beta Managed Agents Session Budget Reached

- `BetaManagedAgentsSessionBudgetReached object`

  The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `type: "budget_reached"`

### Beta Managed Agents Session Deleted Event

- `BetaManagedAgentsSessionDeletedEvent object`

  Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `type: "session.deleted"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when the session was deleted.

    format: date-time

### Beta Managed Agents Session End Turn

- `BetaManagedAgentsSessionEndTurn object`

  The agent completed its turn naturally and is ready for the next user message.

  - `type: "end_turn"`

### Beta Managed Agents Session Error Event

- `BetaManagedAgentsSessionErrorEvent object`

  An error event indicating a problem occurred during session execution.

  - `type: "session.error"`

  - `id: string`

    Unique identifier for this event.

  - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 10 more`

    - `BetaManagedAgentsUnknownError object`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type: "unknown_error"`

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type: "retrying"`

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type: "exhausted"`

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

          - `type: "terminal"`

    - `BetaManagedAgentsModelOverloadedError object`

      The model is currently overloaded. Emitted after automatic retries are exhausted.

      - `type: "model_overloaded_error"`

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsModelRateLimitedError object`

      The model request was rate-limited.

      - `type: "model_rate_limited_error"`

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsModelRequestFailedError object`

      A model request failed for a reason other than overload or rate-limiting.

      - `type: "model_request_failed_error"`

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsMCPConnectionFailedError object`

      Failed to connect to an MCP server.

      - `type: "mcp_connection_failed_error"`

      - `mcp_server_name: string`

        Name of the MCP server that failed to connect.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsMCPAuthenticationFailedError object`

      Authentication to an MCP server failed.

      - `type: "mcp_authentication_failed_error"`

      - `mcp_server_name: string`

        Name of the MCP server that failed authentication.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsBillingError object`

      The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

      - `type: "billing_error"`

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsCredentialHostUnreachableError object`

      An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

      - `type: "credential_host_unreachable_error"`

      - `credential_id: string`

        ID of the affected credential.

      - `message: string`

        Human-readable error description.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

      - `vault_id: string`

        ID of the vault containing the affected credential.

    - `BetaManagedAgentsRepositoryAuthenticationError object`

      The repository host rejected the credentials, or required credentials and received none.

      - `type: "repository_authentication_error"`

      - `message: string`

        Human-readable error description.

      - `repository_url: string or null`

        URL of the repository that could not be cloned. Null when it could not be identified.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next. Always `retrying`: the session keeps running without the repository.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsRepositoryForbiddenError object`

      The repository host refused access to the repository.

      - `type: "repository_forbidden_error"`

      - `message: string`

        Human-readable error description.

      - `repository_url: string or null`

        URL of the repository that could not be cloned. Null when it could not be identified.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next. Always `retrying`: the session keeps running without the repository.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsRepositoryNotFoundError object`

      The repository host reported the repository as not found.

      - `type: "repository_not_found_error"`

      - `message: string`

        Human-readable error description.

      - `repository_url: string or null`

        URL of the repository that could not be cloned. Null when it could not be identified.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next. Always `retrying`: the session keeps running without the repository.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsRepositoryCheckoutError object`

      The requested branch or commit does not exist in the repository.

      - `type: "repository_checkout_error"`

      - `message: string`

        Human-readable error description.

      - `repository_url: string or null`

        URL of the repository that could not be cloned. Null when it could not be identified.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next. Always `retrying`: the session keeps running without the repository.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

    - `BetaManagedAgentsRepositoryCloneError object`

      The repository could not be cloned.

      - `type: "repository_clone_error"`

      - `message: string`

        Human-readable error description.

      - `repository_url: string or null`

        URL of the repository that could not be cloned. Null when it could not be identified.

      - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

        What the client should do next. Always `retrying`: the session keeps running without the repository.

        - `BetaManagedAgentsRetryStatusRetrying object`

          The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

        - `BetaManagedAgentsRetryStatusExhausted object`

          This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

        - `BetaManagedAgentsRetryStatusTerminal object`

          The session encountered a terminal error and will transition to `terminated` state.

  - `processed_at: string`

    Timestamp when the error occurred.

    format: date-time

### Beta Managed Agents Session Event

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 39 more`

  Union type for all event types in a session.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at: optional string or null`

      Timestamp when the agent finished processing this message.

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: optional string or null`

      Timestamp when the interrupt was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      Timestamp when the confirmation was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for this search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

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

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result. The client can send it as soon as this event arrives, without waiting for `session.status_idle`.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      Timestamp when this tool use was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      Timestamp when this response was generated.

      format: date-time

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this thinking was produced.

      format: date-time

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `BetaManagedAgentsAgentToolEvaluationAuto object`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's judgement for this invocation.

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

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

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

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

    - `type: "agent.thread_message_received"`

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

      Timestamp when the message was received.

      format: date-time

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

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

      Timestamp when the message was sent.

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when compaction was processed.

      format: date-time

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 10 more`

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

      - `BetaManagedAgentsRepositoryAuthenticationError object`

        The repository host rejected the credentials, or required credentials and received none.

        - `type: "repository_authentication_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryForbiddenError object`

        The repository host refused access to the repository.

        - `type: "repository_forbidden_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryNotFoundError object`

        The repository host reported the repository as not found.

        - `type: "repository_not_found_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCheckoutError object`

        The requested branch or commit does not exist in the repository.

        - `type: "repository_checkout_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCloneError object`

        The repository could not be cloned.

        - `type: "repository_clone_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

    - `processed_at: string`

      Timestamp when the error occurred.

      format: date-time

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the session stopped. `null` when there is nothing more to report.

      - `type: "refusal"`

      - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

        The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

        - `"cyber"`

        - `"bio"`

        - `"frontier_llm"`

        - `"reasoning_extraction"`

        - `"general_harms"`

      - `explanation: string or null`

        Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

        - `type: "refusal"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a child thread is created. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      Timestamp when the thread was created.

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `workflow_run_id: string or null`

      Identifier of the workflow run that created the thread, or `null` for any other thread.

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

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

      Timestamp when outcome evaluation started.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

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

      Timestamp when outcome evaluation ended.

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

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

        Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the model request started.

      format: date-time

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for this model request.

    - `processed_at: string`

      Timestamp when the model request completed.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

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

      Timestamp when this heartbeat was emitted.

      format: date-time

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

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

      Timestamp when the outcome was accepted.

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the session was deleted.

      format: date-time

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the thread stopped. `null` when there is nothing more to report.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the update was applied.

      format: date-time

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

      - `type: "agent"`

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-haiku-5-5"`

            Fastest model for high-volume, real-time tasks

          - `"claude-sonnet-5-5"`

            Efficient model for coding and agents

          - `"claude-opus-5-5"`

            Powerful intelligence for coding, knowledge work, and long-running agents

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-sonnet-5"`

            Efficient model for coding and agents

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

          - `"claude-haiku-4-5-20251001"`

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagent or null`

        Resolved multiagent orchestration configuration. Null when the agent is single-threaded.

        - `BetaManagedAgentsSessionMultiagentCoordinator object`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `type: "coordinator"`

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `BetaManagedAgentsSessionThreadAgent object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `type: "agent"`

              - `id: string`

              - `description: string or null`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `type: "url"`

                - `name: string`

                - `url: string`

              - `model: BetaManagedAgentsModelConfig`

                Model identifier and configuration.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `BetaManagedAgentsAnthropicSkill object`

                  A resolved Anthropic-managed skill.

                  - `type: "anthropic"`

                  - `skill_id: string`

                  - `version: string`

                - `BetaManagedAgentsCustomSkill object`

                  A resolved user-created custom skill.

                  - `type: "custom"`

                  - `skill_id: string`

                  - `version: string`

              - `system: string or null`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `BetaManagedAgentsAgentToolset20260401 object`

                  - `type: "agent_toolset_20260401"`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `BetaManagedAgentsBashToolConfig object`

                      Configuration for the bash tool.

                      - `type: "bash"`

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                          - `type: "auto"`

                    - `BetaManagedAgentsEditToolConfig object`

                      Configuration for the edit tool.

                      - `type: "edit"`

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsReadToolConfig object`

                      Configuration for the read tool.

                      - `type: "read"`

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWriteToolConfig object`

                      Configuration for the write tool.

                      - `type: "write"`

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGlobToolConfig object`

                      Configuration for the glob tool.

                      - `type: "glob"`

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGrepToolConfig object`

                      Configuration for the grep tool.

                      - `type: "grep"`

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWebFetchToolConfig object`

                      Configuration for the web_fetch tool.

                      - `type: "web_fetch"`

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `url_sources: BetaManagedAgentsWebFetchURLSources or null`

                        Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source.

                        - `client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                            - `type: "all"`

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                            - `type: "none"`

                          - `BetaManagedAgentsWebFetchURLSourceOnly object`

                            Only the named tools' results contribute URLs that may be fetched.

                            - `type: "only"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                          - `BetaManagedAgentsWebFetchURLSourceExcept object`

                            Every tool's results contribute URLs that may be fetched, except the named tools' results.

                            - `type: "except"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                        - `server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both.

                        - `user_input: BetaManagedAgentsWebFetchURLSourceUserInput or null`

                          Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number or null`

                        format: int32

                    - `BetaManagedAgentsWebSearchToolConfig object`

                      Configuration for the web_search tool.

                      - `type: "web_search"`

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsMCPToolset object`

                  - `type: "mcp_toolset"`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `mcp_server_name: string`

                - `BetaManagedAgentsCustomTool object`

                  A custom tool as returned in API responses.

                  - `type: "custom"`

                  - `description: string`

                  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown] or null`

                    - `required: optional array of string or null`

                  - `name: string`

              - `version: number`

                format: int32

            - `BetaManagedAgentsAdvisor object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `type: "advisor"`

              - `model: string`

                The advisor model id.

        - `BetaManagedAgentsSessionMultiagent20261001 object`

          Resolved multiagent configuration with three members, as copied to the `session` at creation.

          - `type: "multiagent_20261001"`

          - `advisor: BetaManagedAgentsMultiagentAdvisor`

            Whether the session's primary thread can consult an advisor model.

            - `BetaManagedAgentsMultiagentAdvisorEnabled object`

              The session's primary thread can consult `model` mid-turn.

              - `type: "enabled"`

              - `model: string`

                The advisor model id.

            - `BetaManagedAgentsMultiagentAdvisorDisabled object`

              The agent has no advisor.

              - `type: "disabled"`

          - `subagents: BetaManagedAgentsSessionMultiagentSubagents`

            Whether the agent can spawn session threads.

            - `BetaManagedAgentsSessionMultiagentSubagentsEnabled object`

              The agent can spawn session threads.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether the agent can define inline agents, which are not saved, when it spawns session threads.

                - `BetaManagedAgentsMultiagentInlineAgentsEnabled object`

                  The agent can define inline agents.

                  - `type: "enabled"`

                - `BetaManagedAgentsMultiagentInlineAgentsDisabled object`

                  The agent cannot define inline agents.

                  - `type: "disabled"`

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that this agent can spawn as session threads.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentSubagentsDisabled object`

              The agent cannot spawn session threads.

              - `type: "disabled"`

          - `workflows: BetaManagedAgentsSessionMultiagentWorkflows`

            Whether the agent can start workflow runs.

            - `BetaManagedAgentsSessionMultiagentWorkflowsEnabled object`

              The agent can start workflow runs.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether a run's plan can define inline agents, which are not saved.

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that a run's plan can use.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentWorkflowsDisabled object`

              The agent cannot start workflow runs.

              - `type: "disabled"`

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

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

      - `type: "limit"`

      - `max_list_cost: BetaMonetaryAmount`

        Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at: optional string or null`

      Timestamp when this system message was processed.

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the snapshot was taken.

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      The session's cumulative usage at the snapshot time.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Tokens used to create prompt cache entries, broken down by cache TTL.

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

        Cumulative list cost of the session across all turns, priced at public list rates.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative server-executed tool usage across all turns.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's configured budget at the snapshot time, or null when the session has no budget.

  - `BetaManagedAgentsWorkflowRunCreatedEvent object`

    A workflow run was created. A workflow run is background work that the session's agent starts. Emitted once per run, before the run's other `workflow_run.*` events.

    - `type: "workflow_run.created"`

    - `id: string`

      Unique identifier for this event.

    - `description: string or null`

      Description that the agent gave the run, passed on as written, or `null` if it gave none.

    - `name: string`

      Name that the agent gave the run, passed on as written, or a name that the server assigned.

    - `phases: array of BetaManagedAgentsWorkflowRunPhase`

      The phases that the run's plan declares, in the plan's order. Can be empty.

      - `id: string`

        Unique identifier for the phase.

      - `description: string or null`

        Description that the agent gave the phase, passed on as written, or `null` if it gave none.

      - `name: string`

        Name that the agent gave the phase, passed on as written.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusEndedEvent object`

    A workflow run ended. Emitted once per run, as the last of the run's `workflow_run.*` events.

    - `type: "workflow_run.status_ended"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `result: BetaManagedAgentsWorkflowRunResult`

      How the run ended.

      - `BetaManagedAgentsWorkflowRunResultCompleted object`

        The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

        - `type: "completed"`

      - `BetaManagedAgentsWorkflowRunResultError object`

        The run failed or reached its time limit.

        - `type: "error"`

        - `error: BetaManagedAgentsWorkflowRunError`

          Why the run did not finish.

          - `BetaManagedAgentsTimeoutWorkflowRunError object`

            The run reached its time limit.

            - `type: "timeout_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsProgramWorkflowRunError object`

            The plan, a program that the agent wrote, failed, or the server refused it.

            - `type: "program_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsUnknownWorkflowRunError object`

            A failure that has no type of its own.

            - `type: "unknown_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsThreadLimitWorkflowRunError object`

            The run exceeded the limit on the number of threads that a run can create.

            - `type: "thread_limit_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

            No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

            - `type: "max_workflow_runs_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsWorkflowRunResultStopped object`

        The agent stopped the run.

        - `type: "stopped"`

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunPhaseStartedEvent object`

    A workflow run's plan entered a phase.

    - `type: "workflow_run.phase_started"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunPhaseEndedEvent object`

    A workflow run's plan left a phase, or the run's end closed it. Emitted once for every `workflow_run.phase_started` event, before the run's `workflow_run.status_ended` event. The event does not say whether the plan finished the phase's work, or why it left.

    - `type: "workflow_run.phase_ended"`

    - `id: string`

      Unique identifier for this event.

    - `phase_started_id: string`

      Identifier of the `workflow_run.phase_started` event that opened the phase.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunStatusRunningEvent object`

    A workflow run is running. Emitted when the run starts to execute, and each time it resumes after being idle. A run that starts idle emits `workflow_run.status_idle` first.

    - `type: "workflow_run.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusIdleEvent object`

    A workflow run is idle. Emitted each time the run goes idle, whatever the cause. If the run ends while idle, no `workflow_run.status_running` comes between this event and its `workflow_run.status_ended`.

    - `type: "workflow_run.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunErrorEvent object`

    A workflow run met an error, or an error kept a run from being created. A run that ends with a `result.type` of `error` emits this event before its `workflow_run.status_ended`, with the same `error`.

    - `type: "workflow_run.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsWorkflowRunError`

      Why the run did not finish, or was not created.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string or null`

      Identifier of the run that met the error, or `null` when the error kept a run from being created.

### Beta Managed Agents Session Event Type

- `BetaManagedAgentsSessionEventType = "user.message" or "user.interrupt" or "user.tool_confirmation" or 38 more`

  The `type` of a session event.

  - `"user.message"`

  - `"user.interrupt"`

  - `"user.tool_confirmation"`

  - `"user.custom_tool_result"`

  - `"agent.custom_tool_use"`

  - `"agent.message"`

  - `"agent.thinking"`

  - `"agent.mcp_tool_use"`

  - `"agent.mcp_tool_result"`

  - `"agent.tool_use"`

  - `"agent.tool_result"`

  - `"agent.thread_message_received"`

  - `"agent.thread_message_sent"`

  - `"agent.thread_context_compacted"`

  - `"session.error"`

  - `"session.status_rescheduled"`

  - `"session.status_running"`

  - `"session.status_idle"`

  - `"session.status_terminated"`

  - `"session.thread_created"`

  - `"span.outcome_evaluation_start"`

  - `"span.outcome_evaluation_end"`

  - `"span.model_request_start"`

  - `"span.model_request_end"`

  - `"span.outcome_evaluation_ongoing"`

  - `"user.define_outcome"`

  - `"session.thread_status_running"`

  - `"session.thread_status_idle"`

  - `"session.thread_status_terminated"`

  - `"user.tool_result"`

  - `"session.thread_status_rescheduled"`

  - `"session.updated"`

  - `"system.message"`

  - `"session.usage"`

  - `"workflow_run.created"`

  - `"workflow_run.status_running"`

  - `"workflow_run.status_idle"`

  - `"workflow_run.status_ended"`

  - `"workflow_run.error"`

  - `"workflow_run.phase_started"`

  - `"workflow_run.phase_ended"`

### Beta Managed Agents Session Refusal

- `BetaManagedAgentsSessionRefusal object`

  The turn ended because the model's response was refused, for example by a safety classifier.

  - `type: "refusal"`

### Beta Managed Agents Session Refusal Stop Details

- `BetaManagedAgentsSessionRefusalStopDetails object`

  Structured information about a refusal.

  - `type: "refusal"`

  - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

    The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

    - `"cyber"`

    - `"bio"`

    - `"frontier_llm"`

    - `"reasoning_extraction"`

    - `"general_harms"`

  - `explanation: string or null`

    Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

### Beta Managed Agents Session Requires Action

- `BetaManagedAgentsSessionRequiresAction object`

  The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

  - `type: "requires_action"`

  - `event_ids: array of string`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

### Beta Managed Agents Session Retries Exhausted

- `BetaManagedAgentsSessionRetriesExhausted object`

  The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

  - `type: "retries_exhausted"`

### Beta Managed Agents Session Status Idle Event

- `BetaManagedAgentsSessionStatusIdleEvent object`

  Indicates the agent has paused and is awaiting user input.

  - `type: "session.status_idle"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp of status change.

    format: date-time

  - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

    Structured information about why the session stopped. `null` when there is nothing more to report.

    - `type: "refusal"`

    - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

      The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

      - `"cyber"`

      - `"bio"`

      - `"frontier_llm"`

      - `"reasoning_extraction"`

      - `"general_harms"`

    - `explanation: string or null`

      Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

  - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

    - `BetaManagedAgentsSessionEndTurn object`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: "end_turn"`

    - `BetaManagedAgentsSessionRequiresAction object`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type: "requires_action"`

      - `event_ids: array of string`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

    - `BetaManagedAgentsSessionRetriesExhausted object`

      The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type: "retries_exhausted"`

    - `BetaManagedAgentsSessionBudgetReached object`

      The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `type: "budget_reached"`

    - `BetaManagedAgentsSessionRefusal object`

      The turn ended because the model's response was refused, for example by a safety classifier.

      - `type: "refusal"`

### Beta Managed Agents Session Status Rescheduled Event

- `BetaManagedAgentsSessionStatusRescheduledEvent object`

  Indicates the session is recovering from an error state and is rescheduled for execution.

  - `type: "session.status_rescheduled"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp of status change.

    format: date-time

### Beta Managed Agents Session Status Running Event

- `BetaManagedAgentsSessionStatusRunningEvent object`

  Indicates the session is actively running and the agent is working.

  - `type: "session.status_running"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp of status change.

    format: date-time

### Beta Managed Agents Session Status Terminated Event

- `BetaManagedAgentsSessionStatusTerminatedEvent object`

  Indicates the session has terminated, either due to an error or completion.

  - `type: "session.status_terminated"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp of status change.

    format: date-time

### Beta Managed Agents Session Thread Created Event

- `BetaManagedAgentsSessionThreadCreatedEvent object`

  Emitted when a child thread is created. Written to the parent thread's output stream so clients observing the session see child creation.

  - `type: "session.thread_created"`

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the callable agent the thread runs.

  - `processed_at: string`

    Timestamp when the thread was created.

    format: date-time

  - `session_thread_id: string`

    Public `sthr_` ID of the newly created thread.

  - `workflow_run_id: string or null`

    Identifier of the workflow run that created the thread, or `null` for any other thread.

### Beta Managed Agents Session Thread Status Idle Event

- `BetaManagedAgentsSessionThreadStatusIdleEvent object`

  A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `type: "session.thread_status_idle"`

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    Timestamp of the status transition.

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that went idle.

  - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

    Structured information about why the thread stopped. `null` when there is nothing more to report.

    - `type: "refusal"`

    - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

      The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

      - `"cyber"`

      - `"bio"`

      - `"frontier_llm"`

      - `"reasoning_extraction"`

      - `"general_harms"`

    - `explanation: string or null`

      Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

  - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

    - `BetaManagedAgentsSessionEndTurn object`

      The agent completed its turn naturally and is ready for the next user message.

      - `type: "end_turn"`

    - `BetaManagedAgentsSessionRequiresAction object`

      The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type: "requires_action"`

      - `event_ids: array of string`

        The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

    - `BetaManagedAgentsSessionRetriesExhausted object`

      The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type: "retries_exhausted"`

    - `BetaManagedAgentsSessionBudgetReached object`

      The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `type: "budget_reached"`

    - `BetaManagedAgentsSessionRefusal object`

      The turn ended because the model's response was refused, for example by a safety classifier.

      - `type: "refusal"`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

  A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `type: "session.thread_status_rescheduled"`

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    Timestamp of the status transition.

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that is retrying.

### Beta Managed Agents Session Thread Status Running Event

- `BetaManagedAgentsSessionThreadStatusRunningEvent object`

  A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `type: "session.thread_status_running"`

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    Timestamp of the status transition.

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that started running.

### Beta Managed Agents Session Thread Status Terminated Event

- `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

  A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `type: "session.thread_status_terminated"`

  - `id: string`

    Unique identifier for this event.

  - `agent_name: string`

    Name of the agent the thread runs.

  - `processed_at: string`

    Timestamp of the status transition.

    format: date-time

  - `session_thread_id: string`

    Public sthr_ ID of the thread that terminated.

### Beta Managed Agents Session Usage Snapshot

- `BetaManagedAgentsSessionUsageSnapshot object`

  Point-in-time snapshot of a session's cumulative usage.

  - `active_seconds: optional number`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

    format: double

  - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

    Tokens used to create prompt cache entries, broken down by cache TTL.

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

    Cumulative list cost of the session across all turns, priced at public list rates.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `output_tokens: optional number`

    Total output tokens generated across all turns.

    format: int32

  - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

    Cumulative server-executed tool usage across all turns.

    - `web_fetch_requests: optional number`

      Number of server-executed web fetch requests.

      format: int32

    - `web_search_requests: optional number`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Span Model Request End Event

- `BetaManagedAgentsSpanModelRequestEndEvent object`

  Emitted when a model request completes.

  - `type: "span.model_request_end"`

  - `id: string`

    Unique identifier for this event.

  - `is_error: boolean or null`

    Whether the model request resulted in an error.

  - `model_request_start_id: string`

    The id of the corresponding `span.model_request_start` event.

  - `model_usage: BetaManagedAgentsSpanModelUsage`

    Token usage for this model request.

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

      Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

      - `"standard"`

      - `"fast"`

  - `processed_at: string`

    Timestamp when the model request completed.

    format: date-time

### Beta Managed Agents Span Model Request Start Event

- `BetaManagedAgentsSpanModelRequestStartEvent object`

  Emitted when a model request is initiated by the agent.

  - `type: "span.model_request_start"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when the model request started.

    format: date-time

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

    Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Span Outcome Evaluation End Event

- `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

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

    Timestamp when outcome evaluation ended.

    format: date-time

  - `result: string`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `usage: BetaManagedAgentsSpanModelUsage`

    Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

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

      Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

      - `"standard"`

      - `"fast"`

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

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

    Timestamp when this heartbeat was emitted.

    format: date-time

### Beta Managed Agents Span Outcome Evaluation Start Event

- `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

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

    Timestamp when outcome evaluation started.

    format: date-time

### Beta Managed Agents Stream Session Events

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 41 more`

  Server-sent event in the session stream.

  - `BetaManagedAgentsUserMessageEvent object`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at: optional string or null`

      Timestamp when the agent finished processing this message.

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: optional string or null`

      Timestamp when the interrupt was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: optional string or null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string or null`

      Timestamp when the confirmation was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsUserCustomToolResultEvent object`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

        - `type: "search_result"`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for this search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

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

    - `is_error: optional boolean or null`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string or null`

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsAgentCustomToolUseEvent object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result. The client can send it as soon as this event arrives, without waiting for `session.status_idle`.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      Timestamp when this tool use was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMessageEvent object`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      Timestamp when this response was generated.

      format: date-time

  - `BetaManagedAgentsAgentThinkingEvent object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this thinking was produced.

      format: date-time

  - `BetaManagedAgentsAgentMCPToolUseEvent object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAllow object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `BetaManagedAgentsAgentToolEvaluationAlwaysAsk object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `BetaManagedAgentsAgentToolEvaluationAuto object`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's judgement for this invocation.

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAllow object`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionAsk object`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `BetaManagedAgentsAgentAutoEvaluatedPermissionDeny object`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentMCPToolResultEvent object`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

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

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `evaluated_permission: optional BetaManagedAgentsAgentEvaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `session_thread_id: optional string or null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `BetaManagedAgentsAgentToolResultEvent object`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

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

    - `type: "agent.thread_message_received"`

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

      Timestamp when the message was received.

      format: date-time

    - `from_agent_name: optional string or null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

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

      Timestamp when the message was sent.

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: optional string or null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent object`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when compaction was processed.

      format: date-time

  - `BetaManagedAgentsSessionErrorEvent object`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 10 more`

      - `BetaManagedAgentsUnknownError object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `BetaManagedAgentsModelOverloadedError object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRateLimitedError object`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsModelRequestFailedError object`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPConnectionFailedError object`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsMCPAuthenticationFailedError object`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsBillingError object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsCredentialHostUnreachableError object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

      - `BetaManagedAgentsRepositoryAuthenticationError object`

        The repository host rejected the credentials, or required credentials and received none.

        - `type: "repository_authentication_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryForbiddenError object`

        The repository host refused access to the repository.

        - `type: "repository_forbidden_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryNotFoundError object`

        The repository host reported the repository as not found.

        - `type: "repository_not_found_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCheckoutError object`

        The requested branch or commit does not exist in the repository.

        - `type: "repository_checkout_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `BetaManagedAgentsRepositoryCloneError object`

        The repository could not be cloned.

        - `type: "repository_clone_error"`

        - `message: string`

          Human-readable error description.

        - `repository_url: string or null`

          URL of the repository that could not be cloned. Null when it could not be identified.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next. Always `retrying`: the session keeps running without the repository.

          - `BetaManagedAgentsRetryStatusRetrying object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal object`

            The session encountered a terminal error and will transition to `terminated` state.

    - `processed_at: string`

      Timestamp when the error occurred.

      format: date-time

  - `BetaManagedAgentsSessionStatusRescheduledEvent object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusRunningEvent object`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionStatusIdleEvent object`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the session stopped. `null` when there is nothing more to report.

      - `type: "refusal"`

      - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

        The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time.

        - `"cyber"`

        - `"bio"`

        - `"frontier_llm"`

        - `"reasoning_extraction"`

        - `"general_harms"`

      - `explanation: string or null`

        Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

        - `type: "refusal"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent object`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp of status change.

      format: date-time

  - `BetaManagedAgentsSessionThreadCreatedEvent object`

    Emitted when a child thread is created. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      Timestamp when the thread was created.

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `workflow_run_id: string or null`

      Identifier of the workflow run that created the thread, or `null` for any other thread.

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent object`

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

      Timestamp when outcome evaluation started.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent object`

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

      Timestamp when outcome evaluation ended.

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

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

        Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent object`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the model request started.

      format: date-time

  - `BetaManagedAgentsSpanModelRequestEndEvent object`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean or null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for this model request.

    - `processed_at: string`

      Timestamp when the model request completed.

      format: date-time

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent object`

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

      Timestamp when this heartbeat was emitted.

      format: date-time

  - `BetaManagedAgentsUserDefineOutcomeEvent object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

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

      Timestamp when the outcome was accepted.

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

      - `BetaManagedAgentsFileRubric object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubric object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `BetaManagedAgentsSessionDeletedEvent object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the session was deleted.

      format: date-time

  - `BetaManagedAgentsSessionThreadStatusRunningEvent object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `BetaManagedAgentsSessionThreadStatusIdleEvent object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_details: BetaManagedAgentsSessionRefusalStopDetails or null`

      Structured information about why the thread stopped. `null` when there is nothing more to report.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or 2 more`

      - `BetaManagedAgentsSessionEndTurn object`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `BetaManagedAgentsSessionRefusal object`

        The turn ended because the model's response was refused, for example by a safety classifier.

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

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

      Timestamp when this result was processed.

      format: date-time

    - `session_thread_id: optional string or null`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      Timestamp of the status transition.

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the update was applied.

      format: date-time

    - `agent: optional BetaManagedAgentsSessionAgent or null`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

      - `type: "agent"`

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-haiku-5-5"`

            Fastest model for high-volume, real-time tasks

          - `"claude-sonnet-5-5"`

            Efficient model for coding and agents

          - `"claude-opus-5-5"`

            Powerful intelligence for coding, knowledge work, and long-running agents

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-sonnet-5"`

            Efficient model for coding and agents

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

          - `"claude-haiku-4-5-20251001"`

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

            High-performance model for agents and coding

          - `string`

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: BetaManagedAgentsSessionMultiagent or null`

        Resolved multiagent orchestration configuration. Null when the agent is single-threaded.

        - `BetaManagedAgentsSessionMultiagentCoordinator object`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `type: "coordinator"`

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `BetaManagedAgentsSessionThreadAgent object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `type: "agent"`

              - `id: string`

              - `description: string or null`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `type: "url"`

                - `name: string`

                - `url: string`

              - `model: BetaManagedAgentsModelConfig`

                Model identifier and configuration.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `BetaManagedAgentsAnthropicSkill object`

                  A resolved Anthropic-managed skill.

                  - `type: "anthropic"`

                  - `skill_id: string`

                  - `version: string`

                - `BetaManagedAgentsCustomSkill object`

                  A resolved user-created custom skill.

                  - `type: "custom"`

                  - `skill_id: string`

                  - `version: string`

              - `system: string or null`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `BetaManagedAgentsAgentToolset20260401 object`

                  - `type: "agent_toolset_20260401"`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `BetaManagedAgentsBashToolConfig object`

                      Configuration for the bash tool.

                      - `type: "bash"`

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                          - `type: "auto"`

                    - `BetaManagedAgentsEditToolConfig object`

                      Configuration for the edit tool.

                      - `type: "edit"`

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsReadToolConfig object`

                      Configuration for the read tool.

                      - `type: "read"`

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWriteToolConfig object`

                      Configuration for the write tool.

                      - `type: "write"`

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGlobToolConfig object`

                      Configuration for the glob tool.

                      - `type: "glob"`

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsGrepToolConfig object`

                      Configuration for the grep tool.

                      - `type: "grep"`

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `BetaManagedAgentsWebFetchToolConfig object`

                      Configuration for the web_fetch tool.

                      - `type: "web_fetch"`

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `url_sources: BetaManagedAgentsWebFetchURLSources or null`

                        Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source.

                        - `client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                            - `type: "all"`

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                            - `type: "none"`

                          - `BetaManagedAgentsWebFetchURLSourceOnly object`

                            Only the named tools' results contribute URLs that may be fetched.

                            - `type: "only"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                          - `BetaManagedAgentsWebFetchURLSourceExcept object`

                            Every tool's results contribute URLs that may be fetched, except the named tools' results.

                            - `type: "except"`

                            - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                              The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                              - `type: "tool_reference"`

                                Must be "tool_reference".

                              - `name: string`

                                Name of the tool. Compared exactly, so upper and lower case letters are different.

                                minLength: 1, maxLength: 128

                        - `server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter or null`

                          Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both.

                        - `user_input: BetaManagedAgentsWebFetchURLSourceUserInput or null`

                          Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

                          - `BetaManagedAgentsWebFetchURLSourceAll object`

                            Every URL from this source may be fetched. This is the default.

                          - `BetaManagedAgentsWebFetchURLSourceNone object`

                            This source contributes no URLs that may be fetched.

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number or null`

                        format: int32

                    - `BetaManagedAgentsWebSearchToolConfig object`

                      Configuration for the web_search tool.

                      - `type: "web_search"`

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `BetaManagedAgentsAlwaysAllowPolicy object`

                          Tool calls are automatically approved without user confirmation.

                        - `BetaManagedAgentsAlwaysAskPolicy object`

                          Tool calls require user confirmation before execution.

                        - `BetaManagedAgentsAutoPolicy object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsMCPToolset object`

                  - `type: "mcp_toolset"`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy object`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy object`

                        Tool calls require user confirmation before execution.

                      - `BetaManagedAgentsAutoPolicy object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `mcp_server_name: string`

                - `BetaManagedAgentsCustomTool object`

                  A custom tool as returned in API responses.

                  - `type: "custom"`

                  - `description: string`

                  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown] or null`

                    - `required: optional array of string or null`

                  - `name: string`

              - `version: number`

                format: int32

            - `BetaManagedAgentsAdvisor object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `type: "advisor"`

              - `model: string`

                The advisor model id.

        - `BetaManagedAgentsSessionMultiagent20261001 object`

          Resolved multiagent configuration with three members, as copied to the `session` at creation.

          - `type: "multiagent_20261001"`

          - `advisor: BetaManagedAgentsMultiagentAdvisor`

            Whether the session's primary thread can consult an advisor model.

            - `BetaManagedAgentsMultiagentAdvisorEnabled object`

              The session's primary thread can consult `model` mid-turn.

              - `type: "enabled"`

              - `model: string`

                The advisor model id.

            - `BetaManagedAgentsMultiagentAdvisorDisabled object`

              The agent has no advisor.

              - `type: "disabled"`

          - `subagents: BetaManagedAgentsSessionMultiagentSubagents`

            Whether the agent can spawn session threads.

            - `BetaManagedAgentsSessionMultiagentSubagentsEnabled object`

              The agent can spawn session threads.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether the agent can define inline agents, which are not saved, when it spawns session threads.

                - `BetaManagedAgentsMultiagentInlineAgentsEnabled object`

                  The agent can define inline agents.

                  - `type: "enabled"`

                - `BetaManagedAgentsMultiagentInlineAgentsDisabled object`

                  The agent cannot define inline agents.

                  - `type: "disabled"`

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that this agent can spawn as session threads.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentSubagentsDisabled object`

              The agent cannot spawn session threads.

              - `type: "disabled"`

          - `workflows: BetaManagedAgentsSessionMultiagentWorkflows`

            Whether the agent can start workflow runs.

            - `BetaManagedAgentsSessionMultiagentWorkflowsEnabled object`

              The agent can start workflow runs.

              - `type: "enabled"`

              - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

                Whether a run's plan can define inline agents, which are not saved.

              - `predefined_agents: array of BetaManagedAgentsSessionThreadAgent`

                Full `agent` definitions of the predefined agents, which are saved agents that a run's plan can use.

                - `type: "agent"`

                - `id: string`

                - `description: string or null`

                - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `model: BetaManagedAgentsModelConfig`

                  Model identifier and configuration.

                - `name: string`

                - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `system: string or null`

                - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `version: number`

                  format: int32

            - `BetaManagedAgentsMultiagentWorkflowsDisabled object`

              The agent cannot start workflow runs.

              - `type: "disabled"`

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

      - `version: number`

        format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

      - `type: "limit"`

      - `max_list_cost: BetaMonetaryAmount`

        Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string or null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_start"`

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview object`

        - `type: "agent.message"`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `BetaManagedAgentsAgentThinkingPreview object`

        - `type: "agent.thinking"`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `BetaManagedAgentsDeltaEvent object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_delta"`

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: "content_delta"`

      - `content: BetaManagedAgentsTextBlock`

        A partial element of the content array at index, typed like the element itself — the same shape the buffered agent.message carries in content.

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `BetaManagedAgentsSystemMessageEvent object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at: optional string or null`

      Timestamp when this system message was processed.

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when the snapshot was taken.

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      The session's cumulative usage at the snapshot time.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

        Tokens used to create prompt cache entries, broken down by cache TTL.

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

        Cumulative list cost of the session across all turns, priced at public list rates.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional BetaManagedAgentsServerToolUsage`

        Cumulative server-executed tool usage across all turns.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional BetaManagedAgentsBudgetLimit or null`

      The session's configured budget at the snapshot time, or null when the session has no budget.

  - `BetaManagedAgentsWorkflowRunCreatedEvent object`

    A workflow run was created. A workflow run is background work that the session's agent starts. Emitted once per run, before the run's other `workflow_run.*` events.

    - `type: "workflow_run.created"`

    - `id: string`

      Unique identifier for this event.

    - `description: string or null`

      Description that the agent gave the run, passed on as written, or `null` if it gave none.

    - `name: string`

      Name that the agent gave the run, passed on as written, or a name that the server assigned.

    - `phases: array of BetaManagedAgentsWorkflowRunPhase`

      The phases that the run's plan declares, in the plan's order. Can be empty.

      - `id: string`

        Unique identifier for the phase.

      - `description: string or null`

        Description that the agent gave the phase, passed on as written, or `null` if it gave none.

      - `name: string`

        Name that the agent gave the phase, passed on as written.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusEndedEvent object`

    A workflow run ended. Emitted once per run, as the last of the run's `workflow_run.*` events.

    - `type: "workflow_run.status_ended"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `result: BetaManagedAgentsWorkflowRunResult`

      How the run ended.

      - `BetaManagedAgentsWorkflowRunResultCompleted object`

        The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

        - `type: "completed"`

      - `BetaManagedAgentsWorkflowRunResultError object`

        The run failed or reached its time limit.

        - `type: "error"`

        - `error: BetaManagedAgentsWorkflowRunError`

          Why the run did not finish.

          - `BetaManagedAgentsTimeoutWorkflowRunError object`

            The run reached its time limit.

            - `type: "timeout_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsProgramWorkflowRunError object`

            The plan, a program that the agent wrote, failed, or the server refused it.

            - `type: "program_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsUnknownWorkflowRunError object`

            A failure that has no type of its own.

            - `type: "unknown_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsThreadLimitWorkflowRunError object`

            The run exceeded the limit on the number of threads that a run can create.

            - `type: "thread_limit_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

          - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

            No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

            - `type: "max_workflow_runs_error"`

            - `message: string`

              Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsWorkflowRunResultStopped object`

        The agent stopped the run.

        - `type: "stopped"`

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunPhaseStartedEvent object`

    A workflow run's plan entered a phase.

    - `type: "workflow_run.phase_started"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunPhaseEndedEvent object`

    A workflow run's plan left a phase, or the run's end closed it. Emitted once for every `workflow_run.phase_started` event, before the run's `workflow_run.status_ended` event. The event does not say whether the plan finished the phase's work, or why it left.

    - `type: "workflow_run.phase_ended"`

    - `id: string`

      Unique identifier for this event.

    - `phase_started_id: string`

      Identifier of the `workflow_run.phase_started` event that opened the phase.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

    - `workflow_run_phase_id: string`

      Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

  - `BetaManagedAgentsWorkflowRunStatusRunningEvent object`

    A workflow run is running. Emitted when the run starts to execute, and each time it resumes after being idle. A run that starts idle emits `workflow_run.status_idle` first.

    - `type: "workflow_run.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunStatusIdleEvent object`

    A workflow run is idle. Emitted each time the run goes idle, whatever the cause. If the run ends while idle, no `workflow_run.status_running` comes between this event and its `workflow_run.status_ended`.

    - `type: "workflow_run.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string`

      Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `BetaManagedAgentsWorkflowRunErrorEvent object`

    A workflow run met an error, or an error kept a run from being created. A run that ends with a `result.type` of `error` emits this event before its `workflow_run.status_ended`, with the same `error`.

    - `type: "workflow_run.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsWorkflowRunError`

      Why the run did not finish, or was not created.

    - `processed_at: string`

      Timestamp when this event was processed.

      format: date-time

    - `workflow_run_id: string or null`

      Identifier of the run that met the error, or `null` when the error kept a run from being created.

### Beta Managed Agents System Message Event Params

- `BetaManagedAgentsSystemMessageEventParams object`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

  - `type: "system.message"`

  - `content: array of BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `type: "text"`

    - `text: string`

      The text content.

      minLength: 1

### Beta Managed Agents Text Block

- `BetaManagedAgentsTextBlock object`

  Regular text content.

  - `type: "text"`

  - `text: string`

    The text content.

    minLength: 1

### Beta Managed Agents Text Rubric

- `BetaManagedAgentsTextRubric object`

  Rubric content provided inline as text.

  - `type: "text"`

  - `content: string`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

### Beta Managed Agents Text Rubric Params

- `BetaManagedAgentsTextRubricParams object`

  Rubric content provided inline as text.

  - `type: "text"`

  - `content: string`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

    maxLength: 262144

### Beta Managed Agents Thread Limit Workflow Run Error

- `BetaManagedAgentsThreadLimitWorkflowRunError object`

  The run exceeded the limit on the number of threads that a run can create.

  - `type: "thread_limit_error"`

  - `message: string`

    Short explanation written by the server. It never contains content from the run or its agents.

### Beta Managed Agents Timeout Workflow Run Error

- `BetaManagedAgentsTimeoutWorkflowRunError object`

  The run reached its time limit.

  - `type: "timeout_error"`

  - `message: string`

    Short explanation written by the server. It never contains content from the run or its agents.

### Beta Managed Agents Unknown Error

- `BetaManagedAgentsUnknownError object`

  An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

  - `type: "unknown_error"`

  - `message: string`

    Human-readable error description.

  - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

    What the client should do next.

    - `BetaManagedAgentsRetryStatusRetrying object`

      The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

      - `type: "retrying"`

    - `BetaManagedAgentsRetryStatusExhausted object`

      This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

      - `type: "exhausted"`

    - `BetaManagedAgentsRetryStatusTerminal object`

      The session encountered a terminal error and will transition to `terminated` state.

      - `type: "terminal"`

### Beta Managed Agents Unknown Workflow Run Error

- `BetaManagedAgentsUnknownWorkflowRunError object`

  A failure that has no type of its own.

  - `type: "unknown_error"`

  - `message: string`

    Short explanation written by the server. It never contains content from the run or its agents.

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

  - `type: "user.custom_tool_result"`

  - `id: string`

    Unique identifier for this event.

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `type: "search_result"`

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for this search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

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

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

  - `processed_at: optional string or null`

    Timestamp when this result was processed.

    format: date-time

  - `session_thread_id: optional string or null`

    Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

### Beta Managed Agents User Custom Tool Result Event Params

- `BetaManagedAgentsUserCustomToolResultEventParams object`

  Parameters for providing the result of a custom tool execution.

  - `type: "user.custom_tool_result"`

  - `custom_tool_use_id: string`

    The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `type: "search_result"`

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for this search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

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

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

- `BetaManagedAgentsUserDefineOutcomeEvent object`

  Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

  - `type: "user.define_outcome"`

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

    Timestamp when the outcome was accepted.

    format: date-time

  - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

    How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

    - `BetaManagedAgentsFileRubric object`

      Rubric referenced by a file uploaded via the Files API.

      - `type: "file"`

      - `file_id: string`

        ID of the rubric file.

    - `BetaManagedAgentsTextRubric object`

      Rubric content provided inline as text.

      - `type: "text"`

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

### Beta Managed Agents User Define Outcome Event Params

- `BetaManagedAgentsUserDefineOutcomeEventParams object`

  Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

  - `type: "user.define_outcome"`

  - `description: string`

    What the agent should produce. This is the task specification.

  - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

    How to grade the outcome. Text or file reference.

    - `BetaManagedAgentsFileRubricParams object`

      Rubric referenced by a file uploaded via the Files API.

      - `type: "file"`

      - `file_id: string`

        ID of the rubric file.

    - `BetaManagedAgentsTextRubricParams object`

      Rubric content provided inline as text.

      - `type: "text"`

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        maxLength: 262144

  - `max_iterations: optional number or null`

    Eval→revision cycles before giving up. Default 3, max 20.

    format: int32

### Beta Managed Agents User Interrupt Event

- `BetaManagedAgentsUserInterruptEvent object`

  An interrupt event that pauses agent execution and returns control to the user.

  - `type: "user.interrupt"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: optional string or null`

    Timestamp when the interrupt was processed.

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

  - `type: "user.message"`

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Array of content blocks comprising the user message.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

  - `processed_at: optional string or null`

    Timestamp when the agent finished processing this message.

    format: date-time

### Beta Managed Agents User Message Event Params

- `BetaManagedAgentsUserMessageEventParams object`

  Parameters for sending a user message to the session.

  - `type: "user.message"`

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

    Array of content blocks for the user message.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsRedactedBlock object`

      Placeholder for content withheld by Anthropic model policy.

      - `type: "redacted"`

### Beta Managed Agents User Tool Confirmation Event

- `BetaManagedAgentsUserToolConfirmationEvent object`

  A tool confirmation event that approves or denies a pending tool execution.

  - `type: "user.tool_confirmation"`

  - `id: string`

    Unique identifier for this event.

  - `result: "allow" or "deny"`

    The confirmation result: 'allow' or 'deny'.

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `deny_message: optional string or null`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    maxLength: 10000

  - `processed_at: optional string or null`

    Timestamp when the confirmation was processed.

    format: date-time

  - `session_thread_id: optional string or null`

    Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

### Beta Managed Agents User Tool Confirmation Event Params

- `BetaManagedAgentsUserToolConfirmationEventParams object`

  Parameters for confirming or denying a tool execution request.

  - `type: "user.tool_confirmation"`

  - `result: "allow" or "deny"`

    The confirmation result: 'allow' or 'deny'.

    - `"allow"`

    - `"deny"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `deny_message: optional string or null`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    maxLength: 10000

### Beta Managed Agents User Tool Result Event Params

- `BetaManagedAgentsUserToolResultEventParams object`

  Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `type: "user.tool_result"`

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    minLength: 1, maxLength: 128

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `BetaManagedAgentsTextBlock object`

      Regular text content.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `BetaManagedAgentsImageBlock object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: "image"`

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        The source of the image data.

        - `BetaManagedAgentsBase64ImageSource object`

          Base64-encoded image data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `BetaManagedAgentsURLImageSource object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `BetaManagedAgentsFileImageSource object`

          Image referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

    - `BetaManagedAgentsDocumentBlock object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: "document"`

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        The source of the document data.

        - `BetaManagedAgentsBase64DocumentSource object`

          Base64-encoded document data.

          - `type: "base64"`

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `BetaManagedAgentsPlainTextDocumentSource object`

          Plain text document content.

          - `type: "text"`

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

        - `BetaManagedAgentsURLDocumentSource object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `BetaManagedAgentsFileDocumentSource object`

          Document referenced by file ID.

          - `type: "file"`

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

      - `context: optional string or null`

        Additional context about the document for the model.

      - `title: optional string or null`

        The title of the document.

    - `BetaManagedAgentsSearchResultBlock object`

      A block containing a web search result.

      - `type: "search_result"`

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for this search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

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

  - `is_error: optional boolean or null`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Workflow Run Created Event

- `BetaManagedAgentsWorkflowRunCreatedEvent object`

  A workflow run was created. A workflow run is background work that the session's agent starts. Emitted once per run, before the run's other `workflow_run.*` events.

  - `type: "workflow_run.created"`

  - `id: string`

    Unique identifier for this event.

  - `description: string or null`

    Description that the agent gave the run, passed on as written, or `null` if it gave none.

  - `name: string`

    Name that the agent gave the run, passed on as written, or a name that the server assigned.

  - `phases: array of BetaManagedAgentsWorkflowRunPhase`

    The phases that the run's plan declares, in the plan's order. Can be empty.

    - `id: string`

      Unique identifier for the phase.

    - `description: string or null`

      Description that the agent gave the phase, passed on as written, or `null` if it gave none.

    - `name: string`

      Name that the agent gave the phase, passed on as written.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `workflow_run_id: string`

    Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

### Beta Managed Agents Workflow Run Error

- `BetaManagedAgentsWorkflowRunError = BetaManagedAgentsTimeoutWorkflowRunError or BetaManagedAgentsProgramWorkflowRunError or BetaManagedAgentsUnknownWorkflowRunError or 2 more`

  Why a workflow run did not finish, or was not created. More types may be added. On `workflow_run.status_ended`, for a `type` you do not recognize, rely on the event's `result.type`.

  - `BetaManagedAgentsTimeoutWorkflowRunError object`

    The run reached its time limit.

    - `type: "timeout_error"`

    - `message: string`

      Short explanation written by the server. It never contains content from the run or its agents.

  - `BetaManagedAgentsProgramWorkflowRunError object`

    The plan, a program that the agent wrote, failed, or the server refused it.

    - `type: "program_error"`

    - `message: string`

      Short explanation written by the server. It never contains content from the run or its agents.

  - `BetaManagedAgentsUnknownWorkflowRunError object`

    A failure that has no type of its own.

    - `type: "unknown_error"`

    - `message: string`

      Short explanation written by the server. It never contains content from the run or its agents.

  - `BetaManagedAgentsThreadLimitWorkflowRunError object`

    The run exceeded the limit on the number of threads that a run can create.

    - `type: "thread_limit_error"`

    - `message: string`

      Short explanation written by the server. It never contains content from the run or its agents.

  - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

    No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

    - `type: "max_workflow_runs_error"`

    - `message: string`

      Short explanation written by the server. It never contains content from the run or its agents.

### Beta Managed Agents Workflow Run Error Event

- `BetaManagedAgentsWorkflowRunErrorEvent object`

  A workflow run met an error, or an error kept a run from being created. A run that ends with a `result.type` of `error` emits this event before its `workflow_run.status_ended`, with the same `error`.

  - `type: "workflow_run.error"`

  - `id: string`

    Unique identifier for this event.

  - `error: BetaManagedAgentsWorkflowRunError`

    Why the run did not finish, or was not created.

    - `BetaManagedAgentsTimeoutWorkflowRunError object`

      The run reached its time limit.

      - `type: "timeout_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsProgramWorkflowRunError object`

      The plan, a program that the agent wrote, failed, or the server refused it.

      - `type: "program_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsUnknownWorkflowRunError object`

      A failure that has no type of its own.

      - `type: "unknown_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsThreadLimitWorkflowRunError object`

      The run exceeded the limit on the number of threads that a run can create.

      - `type: "thread_limit_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

      No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

      - `type: "max_workflow_runs_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `workflow_run_id: string or null`

    Identifier of the run that met the error, or `null` when the error kept a run from being created.

### Beta Managed Agents Workflow Run Phase

- `BetaManagedAgentsWorkflowRunPhase object`

  A phase that a workflow run's plan declares.

  - `id: string`

    Unique identifier for the phase.

  - `description: string or null`

    Description that the agent gave the phase, passed on as written, or `null` if it gave none.

  - `name: string`

    Name that the agent gave the phase, passed on as written.

### Beta Managed Agents Workflow Run Phase Ended Event

- `BetaManagedAgentsWorkflowRunPhaseEndedEvent object`

  A workflow run's plan left a phase, or the run's end closed it. Emitted once for every `workflow_run.phase_started` event, before the run's `workflow_run.status_ended` event. The event does not say whether the plan finished the phase's work, or why it left.

  - `type: "workflow_run.phase_ended"`

  - `id: string`

    Unique identifier for this event.

  - `phase_started_id: string`

    Identifier of the `workflow_run.phase_started` event that opened the phase.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `workflow_run_id: string`

    Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `workflow_run_phase_id: string`

    Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

### Beta Managed Agents Workflow Run Phase Started Event

- `BetaManagedAgentsWorkflowRunPhaseStartedEvent object`

  A workflow run's plan entered a phase.

  - `type: "workflow_run.phase_started"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `workflow_run_id: string`

    Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

  - `workflow_run_phase_id: string`

    Identifier of the phase, as in `phases` on the run's `workflow_run.created` event.

### Beta Managed Agents Workflow Run Result

- `BetaManagedAgentsWorkflowRunResult = BetaManagedAgentsWorkflowRunResultCompleted or BetaManagedAgentsWorkflowRunResultError or BetaManagedAgentsWorkflowRunResultStopped`

  How a workflow run ended.

  - `BetaManagedAgentsWorkflowRunResultCompleted object`

    The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

    - `type: "completed"`

  - `BetaManagedAgentsWorkflowRunResultError object`

    The run failed or reached its time limit.

    - `type: "error"`

    - `error: BetaManagedAgentsWorkflowRunError`

      Why the run did not finish.

      - `BetaManagedAgentsTimeoutWorkflowRunError object`

        The run reached its time limit.

        - `type: "timeout_error"`

        - `message: string`

          Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsProgramWorkflowRunError object`

        The plan, a program that the agent wrote, failed, or the server refused it.

        - `type: "program_error"`

        - `message: string`

          Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsUnknownWorkflowRunError object`

        A failure that has no type of its own.

        - `type: "unknown_error"`

        - `message: string`

          Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsThreadLimitWorkflowRunError object`

        The run exceeded the limit on the number of threads that a run can create.

        - `type: "thread_limit_error"`

        - `message: string`

          Short explanation written by the server. It never contains content from the run or its agents.

      - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

        No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

        - `type: "max_workflow_runs_error"`

        - `message: string`

          Short explanation written by the server. It never contains content from the run or its agents.

  - `BetaManagedAgentsWorkflowRunResultStopped object`

    The agent stopped the run.

    - `type: "stopped"`

### Beta Managed Agents Workflow Run Result Completed

- `BetaManagedAgentsWorkflowRunResultCompleted object`

  The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

  - `type: "completed"`

### Beta Managed Agents Workflow Run Result Error

- `BetaManagedAgentsWorkflowRunResultError object`

  The run failed or reached its time limit.

  - `type: "error"`

  - `error: BetaManagedAgentsWorkflowRunError`

    Why the run did not finish.

    - `BetaManagedAgentsTimeoutWorkflowRunError object`

      The run reached its time limit.

      - `type: "timeout_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsProgramWorkflowRunError object`

      The plan, a program that the agent wrote, failed, or the server refused it.

      - `type: "program_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsUnknownWorkflowRunError object`

      A failure that has no type of its own.

      - `type: "unknown_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsThreadLimitWorkflowRunError object`

      The run exceeded the limit on the number of threads that a run can create.

      - `type: "thread_limit_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

      No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

      - `type: "max_workflow_runs_error"`

      - `message: string`

        Short explanation written by the server. It never contains content from the run or its agents.

### Beta Managed Agents Workflow Run Result Stopped

- `BetaManagedAgentsWorkflowRunResultStopped object`

  The agent stopped the run.

  - `type: "stopped"`

### Beta Managed Agents Workflow Run Status Ended Event

- `BetaManagedAgentsWorkflowRunStatusEndedEvent object`

  A workflow run ended. Emitted once per run, as the last of the run's `workflow_run.*` events.

  - `type: "workflow_run.status_ended"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `result: BetaManagedAgentsWorkflowRunResult`

    How the run ended.

    - `BetaManagedAgentsWorkflowRunResultCompleted object`

      The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded.

      - `type: "completed"`

    - `BetaManagedAgentsWorkflowRunResultError object`

      The run failed or reached its time limit.

      - `type: "error"`

      - `error: BetaManagedAgentsWorkflowRunError`

        Why the run did not finish.

        - `BetaManagedAgentsTimeoutWorkflowRunError object`

          The run reached its time limit.

          - `type: "timeout_error"`

          - `message: string`

            Short explanation written by the server. It never contains content from the run or its agents.

        - `BetaManagedAgentsProgramWorkflowRunError object`

          The plan, a program that the agent wrote, failed, or the server refused it.

          - `type: "program_error"`

          - `message: string`

            Short explanation written by the server. It never contains content from the run or its agents.

        - `BetaManagedAgentsUnknownWorkflowRunError object`

          A failure that has no type of its own.

          - `type: "unknown_error"`

          - `message: string`

            Short explanation written by the server. It never contains content from the run or its agents.

        - `BetaManagedAgentsThreadLimitWorkflowRunError object`

          The run exceeded the limit on the number of threads that a run can create.

          - `type: "thread_limit_error"`

          - `message: string`

            Short explanation written by the server. It never contains content from the run or its agents.

        - `BetaManagedAgentsMaxWorkflowRunsWorkflowRunError object`

          No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type.

          - `type: "max_workflow_runs_error"`

          - `message: string`

            Short explanation written by the server. It never contains content from the run or its agents.

    - `BetaManagedAgentsWorkflowRunResultStopped object`

      The agent stopped the run.

      - `type: "stopped"`

  - `workflow_run_id: string`

    Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

### Beta Managed Agents Workflow Run Status Idle Event

- `BetaManagedAgentsWorkflowRunStatusIdleEvent object`

  A workflow run is idle. Emitted each time the run goes idle, whatever the cause. If the run ends while idle, no `workflow_run.status_running` comes between this event and its `workflow_run.status_ended`.

  - `type: "workflow_run.status_idle"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `workflow_run_id: string`

    Identifier of the run. The same value is on all of the run's `workflow_run.*` events.

### Beta Managed Agents Workflow Run Status Running Event

- `BetaManagedAgentsWorkflowRunStatusRunningEvent object`

  A workflow run is running. Emitted when the run starts to execute, and each time it resumes after being idle. A run that starts idle emits `workflow_run.status_idle` first.

  - `type: "workflow_run.status_running"`

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    Timestamp when this event was processed.

    format: date-time

  - `workflow_run_id: string`

    Identifier of the run. The same value is on all of the run's `workflow_run.*` events.
