---
title: Send Events
url: https://platform.claude.com/docs/en/api/cli/beta/sessions/events/send
---

# Send Events

`$ ant beta:sessions:events send`

**POST** `/v1/sessions/{session_id}/events`

Send Events

## Parameters

- `--session-id: string` (path parameter)

- `--event: array of BetaManagedAgentsEventParams`

  Events to send to the `session`.

  - `beta_managed_agents_user_message_event_params: object`

    Parameters for sending a user message to the session.

    - `type: "user.message"`

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          The source of the image data.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          The source of the document data.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

  - `beta_managed_agents_user_interrupt_event_params: object`

    Parameters for sending an interrupt to pause the agent.

    - `type: "user.interrupt"`

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `beta_managed_agents_user_tool_confirmation_event_params: object`

    Parameters for confirming or denying a tool execution request.

    - `type: "user.tool_confirmation"`

    - `result: "allow" or "deny"`

      The confirmation result: 'allow' or 'deny'.

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=cli#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `beta_managed_agents_user_custom_tool_result_event_params: object`

    Parameters for providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=cli#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

        - `type: "search_result"`

        - `citations: object`

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

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_user_define_outcome_event_params: object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: "user.define_outcome"`

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      How to grade the outcome. Text or file reference.

      - `beta_managed_agents_file_rubric_params: object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `beta_managed_agents_text_rubric_params: object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `beta_managed_agents_user_tool_result_event_params: object`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=cli#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_system_message_event_params: object`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `type: "system.message"`

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

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

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_send_session_events: object`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 4 more`

    Sent events

    - `beta_managed_agents_user_message_event: object`

      A user message event in the session conversation.

      - `type: "user.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: "image"`

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            The source of the image data.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: "document"`

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            The source of the document data.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `type: "text"`

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `processed_at: optional string`

        Timestamp when the agent finished processing this message.

        format: date-time

    - `beta_managed_agents_user_interrupt_event: object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `type: "user.interrupt"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: optional string`

        Timestamp when the interrupt was processed.

        format: date-time

      - `session_thread_id: optional string`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `beta_managed_agents_user_tool_confirmation_event: object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `type: "user.tool_confirmation"`

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        The confirmation result: 'allow' or 'deny'.

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=cli#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string`

        Timestamp when the confirmation was processed.

        format: date-time

      - `session_thread_id: optional string`

        Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

    - `beta_managed_agents_user_custom_tool_result_event: object`

      Event sent by the client providing the result of a custom tool execution.

      - `type: "user.custom_tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=cli#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

          - `type: "search_result"`

          - `citations: object`

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

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        Timestamp when this result was processed.

        format: date-time

      - `session_thread_id: optional string`

        Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

    - `beta_managed_agents_user_define_outcome_event: object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `type: "user.define_outcome"`

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        Timestamp when the outcome was accepted.

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `type: "file"`

          - `file_id: string`

            ID of the rubric file.

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `type: "text"`

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

    - `beta_managed_agents_user_tool_result_event: object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `type: "user.tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=cli#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        Timestamp when this result was processed.

        format: date-time

      - `session_thread_id: optional string`

        Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

    - `beta_managed_agents_system_message_event: object`

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

      - `processed_at: optional string`

        Timestamp when this system message was processed.

        format: date-time

## Example

```bash
ant beta:sessions:events send \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --event '{content: [{text: "Where is my order #1234?", type: text}], type: user.message}'
```

### Response (200)

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
