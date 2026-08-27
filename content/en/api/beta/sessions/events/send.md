# Send Events

**POST** `/v1/sessions/{session_id}/events`

Send Events

## Path parameters

- `session_id: string`

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more`

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

## Body parameters

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

## Returns

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

## Example

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
  ]
}
```
