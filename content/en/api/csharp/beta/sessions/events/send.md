# Send Events

`BetaManagedAgentsSendSessionEvents Beta.Sessions.Events.Send(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/events`

Send Events

## Parameters

- `EventSendParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required IReadOnlyList<BetaManagedAgentsEventParams> events`

    Body param: Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

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

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `required Type Type`

      - `string? SessionThreadID`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `Allow`

        - `Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

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

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsUserToolResultEventParams:`

      Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

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

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

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

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `IReadOnlyList<Data> Data`

    Sent events

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

## Example

```csharp
EventSendParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
};

var betaManagedAgentsSendSessionEvents = await client.Beta.Sessions.Events.Send(parameters);

Console.WriteLine(betaManagedAgentsSendSessionEvents);
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
