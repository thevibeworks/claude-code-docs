---
title: Retrieve Message Batch results
url: https://platform.claude.com/docs/en/api/java/beta/messages/batches/results
---

# Retrieve Message Batch results

`BetaMessageBatchIndividualResponse beta().messages().batches().resultsStreaming(params = BatchResultsParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `BatchResultsParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

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

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

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

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

  - `Optional<String> workspaceId`

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaMessageBatchIndividualResponse`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `BetaMessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class BetaMessageBatchSucceededResult`

      - `JsonValue type = "succeeded"`

      - `BetaMessage message`

        - `JsonValue type = "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<BetaContainer> container`

          Information about the container used in this request.

          This will be non-null if a container tool (e.g. code execution) was used.

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

            format: date-time

          - `Optional<List<BetaContainerSkill>> skills`

            Skills loaded in the container

            - `Type type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `ANTHROPIC("anthropic")`

              - `CUSTOM("custom")`

            - `String skillId`

              Skill ID

              minLength: 1, maxLength: 64

            - `String version`

              The resolved version: a skill version ID for custom skills.

              minLength: 1, maxLength: 64

        - `List<BetaContentBlock> content`

          Content generated by the model.

          This is an array of content blocks, each of which has a `type` that determines its shape.

          Example:

          ```json
          [{"type": "text", "text": "Hi, I'm Claude."}]
          ```

          If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

          For example, if the input `messages` were:

          ```json
          [
            {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
            {"role": "assistant", "content": "The best answer is ("}
          ]
          ```

          Then the response `content` might be:

          ```json
          [{"type": "text", "text": "B)"}]
          ```

          - `class BetaTextBlock`

            - `JsonValue type = "text"`

            - `Optional<List<BetaTextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class BetaCitationCharLocation`

                - `JsonValue type = "char_location"`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                  minimum: 0

              - `class BetaCitationPageLocation`

                - `JsonValue type = "page_location"`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                  minimum: 1

              - `class BetaCitationContentBlockLocation`

                - `JsonValue type = "content_block_location"`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `Optional<String> fileId`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

              - `class BetaCitationsWebSearchResultLocation`

                - `JsonValue type = "web_search_result_location"`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512

                - `String url`

              - `class BetaCitationSearchResultLocation`

                - `JsonValue type = "search_result_location"`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `long searchResultIndex`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `String source`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `Optional<String> title`

            - `String text`

          - `class BetaThinkingBlock`

            - `JsonValue type = "thinking"`

            - `String signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `String thinking`

              The text of Claude's thinking process for this block.

          - `class BetaRedactedThinkingBlock`

            - `JsonValue type = "redacted_thinking"`

            - `String data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `class BetaToolUseBlock`

            - `JsonValue type = "tool_use"`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              minLength: 1

            - `Optional<Caller> caller`

              - `class BetaDirectCaller`

                Tool invocation directly from the model.

                - `JsonValue type = "direct"`

              - `class BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `JsonValue type = "code_execution_20250825"`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `class BetaServerToolCaller20260120`

                - `JsonValue type = "code_execution_20260120"`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Optional<String> toolsetName`

              For a toolset member tool_use, the toolset family.

              minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaServerToolUseBlock`

            - `JsonValue type = "server_tool_use"`

            - `String id`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Input input`

            - `Name name`

              - `ADVISOR("advisor")`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

            - `Optional<Caller> caller`

              - `class BetaDirectCaller`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120`

          - `class BetaWebSearchToolResultBlock`

            - `JsonValue type = "web_search_tool_result"`

            - `BetaWebSearchToolResultBlockContent content`

              - `class BetaWebSearchToolResultError`

                - `JsonValue type = "web_search_tool_result_error"`

                - `BetaWebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

              - `List<BetaWebSearchResultBlock>`

                - `JsonValue type = "web_search_result"`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `String url`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Optional<Caller> caller`

              - `class BetaDirectCaller`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120`

          - `class BetaWebFetchToolResultBlock`

            - `JsonValue type = "web_fetch_tool_result"`

            - `Content content`

              - `class BetaWebFetchToolResultErrorBlock`

                - `JsonValue type = "web_fetch_tool_result_error"`

                - `BetaWebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                  - `CONTENT_TOO_LARGE("content_too_large")`

              - `class BetaWebFetchBlock`

                - `JsonValue type = "web_fetch_result"`

                - `BetaDocumentBlock content`

                  - `JsonValue type = "document"`

                  - `Optional<BetaCitationConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class BetaBase64PdfSource`

                      - `JsonValue type = "base64"`

                      - `String data`

                        format: byte

                      - `JsonValue mediaType = "application/pdf"`

                    - `class BetaPlainTextSource`

                      - `JsonValue type = "text"`

                      - `String data`

                      - `JsonValue mediaType = "text/plain"`

                  - `Optional<String> title`

                    The title of the document

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `String url`

                  Fetched content URL

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Optional<Caller> caller`

              - `class BetaDirectCaller`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120`

          - `class BetaAdvisorToolResultBlock`

            - `JsonValue type = "advisor_tool_result"`

            - `Content content`

              - `class BetaAdvisorToolResultError`

                - `JsonValue type = "advisor_tool_result_error"`

                - `ErrorCode errorCode`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `PROMPT_TOO_LONG("prompt_too_long")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `OVERLOADED("overloaded")`

                  - `UNAVAILABLE("unavailable")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `MODEL_NOT_FOUND("model_not_found")`

              - `class BetaAdvisorResultBlock`

                - `JsonValue type = "advisor_result"`

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `String text`

              - `class BetaAdvisorRedactedResultBlock`

                - `JsonValue type = "advisor_redacted_result"`

                - `String encryptedContent`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class BetaCodeExecutionToolResultBlock`

            - `JsonValue type = "code_execution_tool_result"`

            - `BetaCodeExecutionToolResultBlockContent content`

              - `class BetaCodeExecutionToolResultError`

                - `JsonValue type = "code_execution_tool_result_error"`

                - `BetaCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `class BetaCodeExecutionResultBlock`

                - `JsonValue type = "code_execution_result"`

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `JsonValue type = "code_execution_output"`

                  - `String fileId`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

              - `class BetaEncryptedCodeExecutionResultBlock`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `JsonValue type = "encrypted_code_execution_result"`

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `JsonValue type = "code_execution_output"`

                  - `String fileId`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class BetaBashCodeExecutionToolResultBlock`

            - `JsonValue type = "bash_code_execution_tool_result"`

            - `Content content`

              - `class BetaBashCodeExecutionToolResultError`

                - `JsonValue type = "bash_code_execution_tool_result_error"`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `class BetaBashCodeExecutionResultBlock`

                - `JsonValue type = "bash_code_execution_result"`

                - `List<BetaBashCodeExecutionOutputBlock> content`

                  - `JsonValue type = "bash_code_execution_output"`

                  - `String fileId`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class BetaTextEditorCodeExecutionToolResultBlock`

            - `JsonValue type = "text_editor_code_execution_tool_result"`

            - `Content content`

              - `class BetaTextEditorCodeExecutionToolResultError`

                - `JsonValue type = "text_editor_code_execution_tool_result_error"`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

              - `class BetaTextEditorCodeExecutionViewResultBlock`

                - `JsonValue type = "text_editor_code_execution_view_result"`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

              - `class BetaTextEditorCodeExecutionCreateResultBlock`

                - `JsonValue type = "text_editor_code_execution_create_result"`

                - `boolean isFileUpdate`

              - `class BetaTextEditorCodeExecutionStrReplaceResultBlock`

                - `JsonValue type = "text_editor_code_execution_str_replace_result"`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class BetaToolSearchToolResultBlock`

            - `JsonValue type = "tool_search_tool_result"`

            - `Content content`

              - `class BetaToolSearchToolResultError`

                - `JsonValue type = "tool_search_tool_result_error"`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

              - `class BetaToolSearchToolSearchResultBlock`

                - `JsonValue type = "tool_search_tool_search_result"`

                - `List<BetaToolReferenceBlock> toolReferences`

                  - `JsonValue type = "tool_reference"`

                  - `String toolName`

                    minLength: 1, maxLength: 256, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `class BetaMcpToolUseBlock`

            - `JsonValue type = "mcp_tool_use"`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              The name of the MCP tool

            - `String serverName`

              The name of the MCP server

          - `class BetaMcpToolResultBlock`

            - `JsonValue type = "mcp_tool_result"`

            - `Content content`

              - `String`

              - `List<BetaTextBlock>`

                - `JsonValue type = "text"`

                - `Optional<List<BetaTextCitation>> citations`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `String text`

            - `boolean isError`

            - `String toolUseId`

              pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaContainerUploadBlock`

            Response model for a file uploaded to the container.

            - `JsonValue type = "container_upload"`

            - `String fileId`

          - `class BetaCompactionBlock`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `JsonValue type = "compaction"`

            - `Optional<String> content`

              Summary of compacted content, or null if compaction failed

            - `Optional<String> encryptedContent`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `Optional<String> signature`

              Signature over the summary, to be sent back with the block verbatim

            - `Optional<List<ToolChange>> toolChanges`

              The tool changes of the compacted range: the `tool_addition` and `tool_removal` blocks that take the request's `tools` to the tool set in effect at the end of the range, or `[]` when the range changed no tool. Absent when the server did not compute them. Send the block back unchanged.

              - `class BetaResponseToolAdditionBlock`

                An entry of a `compaction` block's `tool_changes`: a tool the
                compacted range made available, as a reference to a `tools` entry or
                MCP toolset, or as the tool definition in effect at the end of the
                range, by value. Send it back unchanged.

                - `JsonValue type = "tool_addition"`

                - `Tool tool`

                  The tool made available: a reference to a `tools` entry or MCP toolset, or a `tool_definition` carrying the definition by value.

                  - `class BetaResponseToolChangeToolReference`

                    Reference to a single tool, by the name the model uses to call it, as
                    a `compaction` block's `tool_changes` entry reports it: a tool
                    declared in `tools` or defined by an earlier `tool_addition` block.
                    Send it back unchanged with the block.

                    - `JsonValue type = "tool_reference"`

                    - `String name`

                  - `class BetaResponseToolChangeMcpToolReference`

                    Reference to a single MCP tool, by its server and its name on that
                    server, as a `compaction` block's `tool_changes` entry reports it.
                    Send it back unchanged with the block.

                    - `JsonValue type = "mcp_tool_reference"`

                    - `String name`

                    - `String serverName`

                  - `class BetaResponseToolChangeMcpToolsetReference`

                    Reference to every tool in the named MCP server's toolset, as a
                    `compaction` block's `tool_changes` entry reports it. Send it back
                    unchanged with the block.

                    - `JsonValue type = "mcp_toolset_reference"`

                    - `String serverName`

                  - `class BetaToolChangeToolDefinition`

                    A tool defined by value, as a `compaction` block's `tool_changes` entry
                    reports it: `definition` is the tool's definition as it was sent, in the
                    form of a `tools` entry, without `cache_control`. Send it back unchanged
                    with the block.

                    - `JsonValue type = "tool_definition"`

                    - `BetaResponseToolUnion definition`

                      - `class BetaResponseTool`

                        A custom tool definition, as sent.

                        - `Optional<Type> type`

                        - `BetaResponseToolInputSchema inputSchema`

                          [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

                          This defines the shape of the `input` that your tool accepts and that the model will produce.

                          - `JsonValue type = "object"`

                          - `Optional<Properties> properties`

                          - `Optional<List<String>> required`

                        - `String name`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                          minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<String> description`

                          Description of what this tool does.

                          Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

                        - `Optional<Boolean> eagerInputStreaming`

                          Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolBash20241022`

                        - `JsonValue type = "bash_20241022"`

                        - `JsonValue name = "bash"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                          - `JsonValue type = "ephemeral"`

                          - `Optional<Ttl> ttl`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                            - `TTL_5M("5m")`

                            - `TTL_1H("1h")`

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolBash20250124`

                        - `JsonValue type = "bash_20250124"`

                        - `JsonValue name = "bash"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaCodeExecutionTool20250522`

                        - `JsonValue type = "code_execution_20250522"`

                        - `JsonValue name = "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaCodeExecutionTool20250825`

                        - `JsonValue type = "code_execution_20250825"`

                        - `JsonValue name = "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaCodeExecutionTool20260120`

                        Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

                        - `JsonValue type = "code_execution_20260120"`

                        - `JsonValue name = "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaCodeExecutionTool20260521`

                        Code execution tool with REPL state persistence.

                        - `JsonValue type = "code_execution_20260521"`

                        - `JsonValue name = "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaBrowserToolset20260801`

                        The browser toolset: a single `tools[]` entry (carrying no
                        `name`) that declares the browser tool family. The model is served
                        the family's tool with any members disabled via `configs` removed
                        from its schema.

                        - `JsonValue type = "browser_toolset_20260801"`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaBrowserToolsetConfigs> configs`

                          Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

                          - `Optional<BetaBrowserTypeConfig> type`

                            `type`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserCloseTabConfig> closeTab`

                            `close_tab`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserDoubleClickConfig> doubleClick`

                            `double_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserFileUploadConfig> fileUpload`

                            `file_upload`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserFindConfig> find`

                            `find`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserFormInputConfig> formInput`

                            `form_input`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserGetPageTextConfig> getPageText`

                            `get_page_text`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserHoldKeyConfig> holdKey`

                            `hold_key`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserHoverConfig> hover`

                            `hover`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserJavascriptExecConfig> javascriptExec`

                            `javascript_exec`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserKeyConfig> key`

                            `key`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserLeftClickConfig> leftClick`

                            `left_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserLeftClickDragConfig> leftClickDrag`

                            `left_click_drag`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserLeftMouseDownConfig> leftMouseDown`

                            `left_mouse_down`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserLeftMouseUpConfig> leftMouseUp`

                            `left_mouse_up`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserListTabsConfig> listTabs`

                            `list_tabs`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserMiddleClickConfig> middleClick`

                            `middle_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserMouseMoveConfig> mouseMove`

                            `mouse_move`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserNavigateConfig> navigate`

                            `navigate`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserNewTabConfig> newTab`

                            `new_tab`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserReadConsoleConfig> readConsole`

                            `read_console`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserReadNetworkConfig> readNetwork`

                            `read_network`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserReadPageConfig> readPage`

                            `read_page`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserRightClickConfig> rightClick`

                            `right_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserScreenshotConfig> screenshot`

                            `screenshot`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserScrollConfig> scroll`

                            `scroll`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserScrollToConfig> scrollTo`

                            `scroll_to`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserSwitchTabConfig> switchTab`

                            `switch_tab`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserTripleClickConfig> tripleClick`

                            `triple_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserWaitConfig> wait`

                            `wait`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaBrowserZoomConfig> zoom`

                            `zoom`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                      - `class BetaToolComputerUse20241022`

                        - `JsonValue type = "computer_20241022"`

                        - `long displayHeightPx`

                          The height of the display in pixels.

                          minimum: 1

                        - `long displayWidthPx`

                          The width of the display in pixels.

                          minimum: 1

                        - `JsonValue name = "computer"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> displayNumber`

                          The X11 display number (e.g. 0, 1) for the display.

                          minimum: 0

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaMemoryTool20250818`

                        - `JsonValue type = "memory_20250818"`

                        - `JsonValue name = "memory"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolComputerUse20250124`

                        - `JsonValue type = "computer_20250124"`

                        - `long displayHeightPx`

                          The height of the display in pixels.

                          minimum: 1

                        - `long displayWidthPx`

                          The width of the display in pixels.

                          minimum: 1

                        - `JsonValue name = "computer"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> displayNumber`

                          The X11 display number (e.g. 0, 1) for the display.

                          minimum: 0

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolTextEditor20241022`

                        - `JsonValue type = "text_editor_20241022"`

                        - `JsonValue name = "str_replace_editor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolComputerUse20251124`

                        - `JsonValue type = "computer_20251124"`

                        - `long displayHeightPx`

                          The height of the display in pixels.

                          minimum: 1

                        - `long displayWidthPx`

                          The width of the display in pixels.

                          minimum: 1

                        - `JsonValue name = "computer"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> displayNumber`

                          The X11 display number (e.g. 0, 1) for the display.

                          minimum: 0

                        - `Optional<Boolean> enableZoom`

                          Whether to enable an action to take a zoomed-in screenshot of the screen.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaComputerToolset20260801`

                        The computer toolset: a single `tools[]` entry (carrying no
                        `name`) that declares the computer tool family. The model is
                        served the family's tool with any members disabled via `configs`
                        removed from its schema. Every member is enabled by default, zoom
                        included. The single-tool options `display_number` and
                        `enable_zoom` are not fields of a toolset entry — it carries only
                        `type`, `configs`, and `cache_control`; zoom is controlled
                        via `configs.zoom.enabled`.

                        - `JsonValue type = "computer_toolset_20260801"`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaComputerToolsetConfigs> configs`

                          Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

                          - `Optional<BetaComputerTypeConfig> type`

                            `type`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerCursorPositionConfig> cursorPosition`

                            `cursor_position`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerDoubleClickConfig> doubleClick`

                            `double_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerHoldKeyConfig> holdKey`

                            `hold_key`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerKeyConfig> key`

                            `key`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerLeftClickConfig> leftClick`

                            `left_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerLeftClickDragConfig> leftClickDrag`

                            `left_click_drag`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerLeftMouseDownConfig> leftMouseDown`

                            `left_mouse_down`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerLeftMouseUpConfig> leftMouseUp`

                            `left_mouse_up`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerMiddleClickConfig> middleClick`

                            `middle_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerMouseMoveConfig> mouseMove`

                            `mouse_move`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerRightClickConfig> rightClick`

                            `right_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerScreenshotConfig> screenshot`

                            `screenshot`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerScrollConfig> scroll`

                            `scroll`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerTripleClickConfig> tripleClick`

                            `triple_click`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerWaitConfig> wait`

                            `wait`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `Optional<BetaComputerZoomConfig> zoom`

                            `zoom`'s config overrides.

                            - `Optional<Boolean> deferLoading`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `Optional<Boolean> enabled`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                      - `class BetaToolTextEditor20250124`

                        - `JsonValue type = "text_editor_20250124"`

                        - `JsonValue name = "str_replace_editor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolTextEditor20250429`

                        - `JsonValue type = "text_editor_20250429"`

                        - `JsonValue name = "str_replace_based_edit_tool"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolTextEditor20250728`

                        - `JsonValue type = "text_editor_20250728"`

                        - `JsonValue name = "str_replace_based_edit_tool"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<List<InputExample>> inputExamples`

                        - `Optional<Long> maxCharacters`

                          Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaWebSearchTool20250305`

                        - `JsonValue type = "web_search_20250305"`

                        - `JsonValue name = "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `Optional<List<String>> blockedDomains`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaUserLocation> userLocation`

                          Parameters for the user's location. Used to provide more relevant search results.

                          - `JsonValue type = "approximate"`

                          - `Optional<String> city`

                            The city of the user.

                            minLength: 1, maxLength: 255

                          - `Optional<String> country`

                            The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

                            minLength: 2, maxLength: 2

                          - `Optional<String> region`

                            The region of the user.

                            minLength: 1, maxLength: 255

                          - `Optional<String> timezone`

                            The [IANA timezone](https://nodatime.org/TimeZones) of the user.

                            minLength: 1, maxLength: 255

                      - `class BetaWebFetchTool20250910`

                        - `JsonValue type = "web_fetch_20250910"`

                        - `JsonValue name = "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          List of domains to allow fetching from

                        - `Optional<List<String>> blockedDomains`

                          List of domains to block fetching from

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaCitationsConfigParam> citations`

                          Citations configuration for fetched documents. Citations are disabled by default.

                          - `Optional<Boolean> enabled`

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxContentTokens`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaWebFetchUrlSources> urlSources`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                          - `Optional<ClientToolResults> clientToolResults`

                            Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

                            - `class BetaWebFetchUrlSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                              - `JsonValue type = "all"`

                            - `class BetaWebFetchUrlSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                              - `JsonValue type = "none"`

                            - `class BetaWebFetchUrlSourceOnly`

                              The tool filter variant under which only the named tools' results
                              contribute.

                              - `JsonValue type = "only"`

                              - `List<BetaWebFetchUrlSourceToolReference> tools`

                                - `JsonValue type = "tool_reference"`

                                - `String name`

                            - `class BetaWebFetchUrlSourceExcept`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                              - `JsonValue type = "except"`

                              - `List<BetaWebFetchUrlSourceToolReference> tools`

                                - `JsonValue type = "tool_reference"`

                                - `String name`

                          - `Optional<ServerToolResults> serverToolResults`

                            Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

                            - `class BetaWebFetchUrlSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `class BetaWebFetchUrlSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                            - `class BetaWebFetchUrlSourceOnly`

                              The tool filter variant under which only the named tools' results
                              contribute.

                            - `class BetaWebFetchUrlSourceExcept`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                          - `Optional<UserInput> userInput`

                            Whether URLs in user messages are fetchable: "all" or "none".

                            - `class BetaWebFetchUrlSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `class BetaWebFetchUrlSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                      - `class BetaWebSearchTool20260209`

                        - `JsonValue type = "web_search_20260209"`

                        - `JsonValue name = "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `Optional<List<String>> blockedDomains`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaUserLocation> userLocation`

                          Parameters for the user's location. Used to provide more relevant search results.

                      - `class BetaWebFetchTool20260209`

                        - `JsonValue type = "web_fetch_20260209"`

                        - `JsonValue name = "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          List of domains to allow fetching from

                        - `Optional<List<String>> blockedDomains`

                          List of domains to block fetching from

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaCitationsConfigParam> citations`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxContentTokens`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaWebFetchUrlSources> urlSources`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                      - `class BetaWebFetchTool20260309`

                        Web fetch tool with use_cache parameter for bypassing cached content.

                        - `JsonValue type = "web_fetch_20260309"`

                        - `JsonValue name = "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          List of domains to allow fetching from

                        - `Optional<List<String>> blockedDomains`

                          List of domains to block fetching from

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaCitationsConfigParam> citations`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxContentTokens`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaWebFetchUrlSources> urlSources`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                        - `Optional<Boolean> useCache`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `class BetaWebSearchTool20260318`

                        - `JsonValue type = "web_search_20260318"`

                        - `JsonValue name = "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `Optional<List<String>> blockedDomains`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<ResponseInclusion> responseInclusion`

                          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

                          - `FULL("full")`

                          - `EXCLUDED("excluded")`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaUserLocation> userLocation`

                          Parameters for the user's location. Used to provide more relevant search results.

                      - `class BetaWebFetchTool20260318`

                        - `JsonValue type = "web_fetch_20260318"`

                        - `JsonValue name = "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<List<String>> allowedDomains`

                          List of domains to allow fetching from

                        - `Optional<List<String>> blockedDomains`

                          List of domains to block fetching from

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaCitationsConfigParam> citations`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxContentTokens`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          minimum: 1

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<ResponseInclusion> responseInclusion`

                          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

                          - `FULL("full")`

                          - `EXCLUDED("excluded")`

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                        - `Optional<BetaWebFetchUrlSources> urlSources`

                          Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

                        - `Optional<Boolean> useCache`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `class BetaAdvisorTool20260301`

                        - `JsonValue type = "advisor_20260301"`

                        - `Model model`

                          The model that will complete your prompt.

                          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                          - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

                            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                          - `CLAUDE_OPUS_5_5("claude-opus-5-5")`

                            Powerful intelligence for coding, knowledge work, and long-running agents

                          - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

                            Our most capable model for cybersecurity and biology research, available through trusted access programs

                          - `CLAUDE_SONNET_5("claude-sonnet-5")`

                            High-performance model for coding and agents

                          - `CLAUDE_FABLE_5("claude-fable-5")`

                            Next generation of intelligence for the hardest knowledge work and coding problems

                          - `CLAUDE_MYTHOS_5("claude-mythos-5")`

                            Most capable model for cybersecurity and biology research

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

                          - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

                            **Deprecated**: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

                            New class of intelligence, strongest in coding and cybersecurity

                        - `JsonValue name = "advisor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<BetaCacheControlEphemeral> caching`

                          Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Long> maxTokens`

                          Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

                          minimum: 1024

                        - `Optional<Long> maxUses`

                          Maximum number of times the tool can be used in the API request.

                          minimum: 1

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolSearchToolBm25_20251119`

                        - `Type type`

                          - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

                          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

                        - `JsonValue name = "tool_search_tool_bm25"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaToolSearchToolRegex20251119`

                        - `Type type`

                          - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

                          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

                        - `JsonValue name = "tool_search_tool_regex"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `Optional<List<AllowedCaller>> allowedCallers`

                          - `DIRECT("direct")`

                          - `CODE_EXECUTION_20250825("code_execution_20250825")`

                          - `CODE_EXECUTION_20260120("code_execution_20260120")`

                          - `CODE_EXECUTION_20260521("code_execution_20260521")`

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Boolean> deferLoading`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `Optional<Boolean> strict`

                          When true, guarantees schema validation on tool names and inputs

                      - `class BetaMcpToolset`

                        Configuration for a group of tools from an MCP server.

                        Allows configuring enabled status and defer_loading for all tools
                        from an MCP server, with optional per-tool overrides.

                        - `JsonValue type = "mcp_toolset"`

                        - `String mcpServerName`

                          Name of the MCP server to configure tools for

                          minLength: 1, maxLength: 255

                        - `Optional<BetaCacheControlEphemeral> cacheControl`

                          Create a cache control breakpoint at this content block.

                        - `Optional<Configs> configs`

                          Configuration overrides for specific tools, keyed by tool name

                          - `Optional<Boolean> deferLoading`

                          - `Optional<Boolean> enabled`

                        - `Optional<BetaMcpToolDefaultConfig> defaultConfig`

                          Default configuration applied to all tools from this server

                          - `Optional<Boolean> deferLoading`

                          - `Optional<Boolean> enabled`

                        - `Optional<List<BetaMcpToolParam>> tools`

                          The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

                          - `InputSchema inputSchema`

                            The tool's input schema as the MCP server lists it, verbatim.

                          - `String name`

                            The tool's name as the MCP server lists it (not prefixed with the server name).

                            minLength: 1

                          - `Optional<String> description`

                            The tool's description as the MCP server lists it.

              - `class BetaResponseToolRemovalBlock`

                An entry of a `compaction` block's `tool_changes`: a tool of the
                request's `tools` (or an MCP tool or toolset) that the compacted range
                withdrew. Send it back unchanged.

                - `JsonValue type = "tool_removal"`

                - `Tool tool`

                  A reference to the withdrawn `tools` entry, MCP tool or MCP toolset.

                  - `class BetaResponseToolChangeToolReference`

                    Reference to a single tool, by the name the model uses to call it, as
                    a `compaction` block's `tool_changes` entry reports it: a tool
                    declared in `tools` or defined by an earlier `tool_addition` block.
                    Send it back unchanged with the block.

                  - `class BetaResponseToolChangeMcpToolReference`

                    Reference to a single MCP tool, by its server and its name on that
                    server, as a `compaction` block's `tool_changes` entry reports it.
                    Send it back unchanged with the block.

                  - `class BetaResponseToolChangeMcpToolsetReference`

                    Reference to every tool in the named MCP server's toolset, as a
                    `compaction` block's `tool_changes` entry reports it. Send it back
                    unchanged with the block.

          - `class BetaFallbackBlock`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `JsonValue type = "fallback"`

            - `BetaFallbackInfo from`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `BetaFallbackInfo to`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `BetaFallbackRefusalTrigger trigger`

              What caused the `from` model to hand over at this hop.

              - `JsonValue type = "refusal"`

              - `Optional<Category> category`

                The policy category that triggered the `from` model's refusal at this hop. `null` when the refusal doesn't map to a named category. Same vocabulary as `stop_details.category`.

                - `CYBER("cyber")`

                  The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

                - `BIO("bio")`

                  The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

                - `FRONTIER_LLM("frontier_llm")`

                  The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

                - `REASONING_EXTRACTION("reasoning_extraction")`

                  The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

                - `GENERAL_HARMS("general_harms")`

                  The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `class BetaMcpToolListingBlock`

            The tool listing the server fetched from an MCP server while producing
            this response. Send the assistant message back unchanged, this block
            included, so later requests use this listing instead of asking the MCP
            server again.

            - `JsonValue type = "mcp_tool_listing"`

            - `String mcpServerName`

            - `List<BetaMcpTool> tools`

              - `InputSchema inputSchema`

              - `String name`

              - `Optional<String> description`

        - `Optional<BetaContextManagementResponse> contextManagement`

          Context management response.

          Information about context management strategies applied during the request.

          - `List<AppliedEdit> appliedEdits`

            List of context management edits that were applied.

            - `class BetaClearToolUses20250919EditResponse`

              - `JsonValue type = "clear_tool_uses_20250919"`

                The type of context management edit applied.

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedToolUses`

                Number of tool uses that were cleared.

                minimum: 0

            - `class BetaClearThinking20251015EditResponse`

              - `JsonValue type = "clear_thinking_20251015"`

                The type of context management edit applied.

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedThinkingTurns`

                Number of thinking turns that were cleared.

                minimum: 0

        - `Optional<BetaDiagnostics> diagnostics`

          Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected.

          - `Optional<BetaCacheMissReason> cacheMissReason`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `class BetaCacheMissModelChanged`

              - `JsonValue type = "model_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class BetaCacheMissSystemChanged`

              - `JsonValue type = "system_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class BetaCacheMissToolsChanged`

              - `JsonValue type = "tools_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class BetaCacheMissMessagesChanged`

              - `JsonValue type = "messages_changed"`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `class BetaCacheMissPreviousMessageNotFound`

              - `JsonValue type = "previous_message_not_found"`

            - `class BetaCacheMissUnavailable`

              - `JsonValue type = "unavailable"`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `JsonValue role = "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `Optional<BetaRefusalStopDetails> stopDetails`

          Structured information about why model output stopped.

          This is `null` when the `stop_reason` has no additional detail to report.

          - `JsonValue type = "refusal"`

          - `Optional<Category> category`

            The policy category that triggered the refusal.

            `null` when the refusal doesn't map to a named category.

            - `CYBER("cyber")`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `BIO("bio")`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `FRONTIER_LLM("frontier_llm")`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `REASONING_EXTRACTION("reasoning_extraction")`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `GENERAL_HARMS("general_harms")`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `Optional<String> explanation`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `Optional<String> fallbackCreditToken`

            Opaque code that refunds the cache-miss cost when retrying this refused
            request on the fallback model. Pass it as `fallback_credit_token` on the
            retry request. Expires 5 minutes after the refusal.

            The retry is sent either with the same request body (`system`, `messages`,
            `tools`, and other render-shaping fields), or with the same body plus one
            appended `assistant` message whose content is the partial text (with any
            trailing whitespace stripped from the final text block) and paired
            server-tool blocks from this refusal — which also authorizes that
            appended turn as an assistant-prefill continuation on models that otherwise
            disallow prefill. A token minted mid-server-tool-loop whose partial content
            was continuable may only be redeemed the second way — if a same-body retry
            is rejected with a 400 saying the token must be redeemed by continuing the
            partial response, retry the second way instead. Either way: same workspace,
            same platform; a mismatch is a 400. Resending a token for an already-warm
            prefix is permitted but yields no additional credit.

            `null` when the refused model isn't eligible for a fallback credit.

          - `Optional<Boolean> fallbackHasPrefillClaim`

            Whether the accompanying `fallback_credit_token` may be redeemed with the
            appended-assistant retry form. Only set when `fallback_credit_token` is
            present.

            `true`: retry by resending the same request body plus one appended
            `assistant` message whose content is this response's `content` with any
            trailing whitespace stripped from the final text block and unpaired
            `tool_use` blocks omitted (the same appended-turn shape described on
            `fallback_credit_token`), with the token attached. `false`: retry by
            resending the original request body unchanged, with the token attached —
            the appended-assistant form is not available for this refusal (no
            continuable partial content, or the request uses `output_format` or a
            `tool_choice` that forces tool use). One exception: when the request used
            `output_format` or a forced `tool_choice` and the refusal arrived after
            server tools (including MCP connector tools) had already executed, the
            token may not be redeemable by either retry form; if the exact-body retry
            is then rejected with a 400 saying the token must be redeemed by
            continuing the partial response, discard the token and retry without it.

            Advisory: if an appended-assistant retry is rejected with a 400 despite
            `true`, fall back to resending the original request body with the token.

          - `Optional<String> recommendedModel`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

        - `Optional<BetaStopReason> stopReason`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
          * `"model_context_window_exceeded"`: we exceeded the model's context window

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `END_TURN("end_turn")`

          - `MAX_TOKENS("max_tokens")`

          - `STOP_SEQUENCE("stop_sequence")`

          - `TOOL_USE("tool_use")`

          - `PAUSE_TURN("pause_turn")`

          - `COMPACTION("compaction")`

          - `REFUSAL("refusal")`

          - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `BetaUsage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<BetaCacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

            - `long ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `long ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `Optional<Long> cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `Optional<Long> cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `Optional<BetaFallbackCreditUsage> fallbackCredit`

            Outcome of the `fallback_credit_token` presented on this request.

            Present on every response to a non-batch request that carried a
            `fallback_credit_token`, in either redemption mode; absent otherwise (batch
            items accept and ignore the token and carry no outcome object).

            - `Status status`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `class BetaFallbackCreditRedeemed`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `JsonValue type = "redeemed"`

              - `class BetaFallbackCreditNotApplied`

                No reprice was applied; `reason` says why.

                - `JsonValue type = "not_applied"`

                - `Reason reason`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `BODY_MISMATCH("body_mismatch")`

                  - `CONTINUATION_EXCLUDED("continuation_excluded")`

                  - `CONTINUATION_ONLY("continuation_only")`

                  - `EXPIRED("expired")`

                  - `INVALID_TARGET_MODEL("invalid_target_model")`

                  - `NOT_ENABLED("not_enabled")`

                  - `REPRICE_UNAVAILABLE("reprice_unavailable")`

                  - `TEMPORARILY_UNAVAILABLE("temporarily_unavailable")`

                  - `VARIANT_FIELDS_PRESENT("variant_fields_present")`

                  - `WRONG_ORGANIZATION("wrong_organization")`

                  - `WRONG_PLATFORM("wrong_platform")`

                  - `WRONG_WORKSPACE("wrong_workspace")`

                - `Optional<List<String>> removeToRedeem`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `Optional<List<Iteration>> iterations`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `class BetaMessageIterationUsage`

              Token usage for a sampling iteration.

              - `JsonValue type = "message"`

                Usage for a sampling iteration

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Optional<Model> model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

            - `class BetaCompactionIterationUsage`

              Token usage for a compaction iteration.

              - `JsonValue type = "compaction"`

                Usage for a compaction iteration

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

            - `class BetaAdvisorMessageIterationUsage`

              Token usage for an advisor sub-inference iteration.

              - `JsonValue type = "advisor_message"`

                Usage for an advisor sub-inference iteration

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

            - `class BetaFallbackMessageIterationUsage`

              Token usage for the fallback-model attempt of a server-side fallback request.

              The terminal entry of a fallback-served turn: when a fallback hop's
              output is the returned message, the entry for the iteration that
              completed it carries this type in place of `message`. A declined hop
              and the serving hop's earlier tool-loop iterations produce `message`
              entries. Whether a fallback model served the response is signalled by
              the presence of this entry in `usage.iterations`.

              - `JsonValue type = "fallback_message"`

                Usage for the fallback-model attempt that served the response

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `Optional<BetaOutputTokensDetails> outputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `long thinkingTokens`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `Optional<BetaServerToolUsage> serverToolUse`

            The number of server tool requests.

            - `long webFetchRequests`

              The number of web fetch tool requests.

              minimum: 0

            - `long webSearchRequests`

              The number of web search tool requests.

              minimum: 0

          - `Optional<ServiceTier> serviceTier`

            If the request used the priority, standard, or batch tier.

            - `STANDARD("standard")`

            - `PRIORITY("priority")`

            - `BATCH("batch")`

          - `Optional<Speed> speed`

            The inference speed mode used for this request.

            - `STANDARD("standard")`

            - `FAST("fast")`

        - `Optional<List<BetaInputTransformation>> inputTransformations`

          Changes the API made to the request's input before showing it to the model,
          and blocks that failed a binding check but were left unchanged: one entry per
          block, in request order. Two entry types today. `thinking_dropped` — a
          `thinking`, `redacted_thinking` or `connector_text` block from the request's
          `messages` that was removed from the prompt instead of being shown to the
          model because it failed a binding check. `thinking_mismatch_allowed` — a
          `thinking` or `redacted_thinking` block that failed the conversation check
          (the conversation before it differs from the one it was created in, or it
          carries no record of one on a model that requires it) and was shown to the
          model all the same, because that check is not enforced for this request.
          More entry types may be added over time; ignore types you do not recognize.

          Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
          every such response from a model that supports extended thinking, as `[]`
          when there is no entry to report; without the beta, blocks are removed or
          left in place all the same but nothing is reported. Removed blocks contribute
          nothing to `usage.input_tokens`; blocks left in place count as sent. When
          streaming, the array is final in `message_start`; the final `message_delta`
          event carries it only when a server-side model fallback happened mid-stream,
          in which case it holds the serving model's entries and replaces the one in
          `message_start`.

          - `class BetaThinkingDroppedInputTransformation`

            - `JsonValue type = "thinking_dropped"`

              Always `thinking_dropped` for this entry type.

            - `String path`

              Where the removed block was in your request, as `messages.{i}.content.{j}`:
              `i` indexes the `messages` array you sent and `j` that message's `content`
              array — the same form error messages use.

            - `Reason reason`

              Which binding check removed the block: `model_binding_mismatch` — it was
              created by a model whose reasoning the requested model may not read;
              `prefix_binding_mismatch` — the conversation before it differs from the
              conversation it was created in (the rest of that turn's consecutive thinking
              blocks are removed with it, each with this reason);
              `organization_binding_mismatch` — it was created under a different
              organization (an Anthropic organization, AWS account or Google Cloud project)
              and this organization is not one of its additional organizations;
              `end_user_binding_mismatch` — it was created for a different end user, or
              was removed by the consumer-organization binding. A block that would fail
              several checks reports one reason, in this order of precedence:
              `organization_binding_mismatch`, `end_user_binding_mismatch`,
              `model_binding_mismatch`, `prefix_binding_mismatch`.

              - `MODEL_BINDING_MISMATCH("model_binding_mismatch")`

              - `PREFIX_BINDING_MISMATCH("prefix_binding_mismatch")`

              - `ORGANIZATION_BINDING_MISMATCH("organization_binding_mismatch")`

              - `END_USER_BINDING_MISMATCH("end_user_binding_mismatch")`

          - `class BetaThinkingMismatchAllowedInputTransformation`

            - `JsonValue type = "thinking_mismatch_allowed"`

              Always `thinking_mismatch_allowed` for this entry type.

            - `String path`

              Where the block is in your request, as `messages.{i}.content.{j}`:
              `i` indexes the `messages` array you sent and `j` that message's `content`
              array — the same form error messages use.

            - `Reason reason`

              Which binding check the block failed; the block was shown to the model all
              the same. Always `prefix_binding_mismatch` today — the conversation before
              the block differs from the conversation it was created in, or the block
              carries no record of one on a model that requires it. Were the check
              enforced for this request, the block would have been removed or the request
              rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also
              takes the rest of that turn's consecutive thinking blocks, whereas here each
              block is checked on its own, so `thinking_mismatch_allowed` entries are a
              lower bound on what enforcement would remove.

              - `MODEL_BINDING_MISMATCH("model_binding_mismatch")`

              - `PREFIX_BINDING_MISMATCH("prefix_binding_mismatch")`

              - `ORGANIZATION_BINDING_MISMATCH("organization_binding_mismatch")`

              - `END_USER_BINDING_MISMATCH("end_user_binding_mismatch")`

    - `class BetaMessageBatchErroredResult`

      - `JsonValue type = "errored"`

      - `BetaErrorResponse error`

        - `JsonValue type = "error"`

        - `BetaError error`

          - `class BetaInvalidRequestError`

            - `JsonValue type = "invalid_request_error"`

            - `String message`

          - `class BetaAuthenticationError`

            - `JsonValue type = "authentication_error"`

            - `String message`

          - `class BetaBillingError`

            - `JsonValue type = "billing_error"`

            - `String message`

          - `class BetaPermissionError`

            - `JsonValue type = "permission_error"`

            - `String message`

          - `class BetaNotFoundError`

            - `JsonValue type = "not_found_error"`

            - `String message`

          - `class BetaRateLimitError`

            - `JsonValue type = "rate_limit_error"`

            - `String message`

          - `class BetaGatewayTimeoutError`

            - `JsonValue type = "timeout_error"`

            - `String message`

          - `class BetaApiError`

            - `JsonValue type = "api_error"`

            - `String message`

          - `class BetaOverloadedError`

            - `JsonValue type = "overloaded_error"`

            - `String message`

        - `Optional<String> requestId`

    - `class BetaMessageBatchCanceledResult`

      - `JsonValue type = "canceled"`

    - `class BetaMessageBatchExpiredResult`

      - `JsonValue type = "expired"`

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.messages.batches.BatchResultsParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatchIndividualResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<BetaMessageBatchIndividualResponse> betaMessageBatchIndividualResponse = client.beta().messages().batches().resultsStreaming("message_batch_id");
    }
}
```
