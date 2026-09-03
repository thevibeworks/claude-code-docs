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

## Returns

- `class BetaMessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `BetaMessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class BetaMessageBatchSucceededResult:`

      - `BetaMessage message`

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<BetaContainer> container`

          Information about the container used in the request (for the code execution tool)

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

            format: date-time

          - `Optional<List<BetaContainerSkill>> skills`

            Skills loaded in the container

            - `String skillId`

              Skill ID

              maxLength: 64, minLength: 1

            - `Type type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `ANTHROPIC("anthropic")`

              - `CUSTOM("custom")`

            - `String version`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

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

          - `class BetaTextBlock:`

            - `Optional<List<BetaTextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class BetaCitationCharLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                  minimum: 0

                - `JsonValue type = "char_location"`

              - `class BetaCitationPageLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                  minimum: 1

                - `JsonValue type = "page_location"`

              - `class BetaCitationContentBlockLocation:`

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

                - `JsonValue type = "content_block_location"`

              - `class BetaCitationsWebSearchResultLocation:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512

                - `JsonValue type = "web_search_result_location"`

                - `String url`

              - `class BetaCitationSearchResultLocation:`

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

                - `JsonValue type = "search_result_location"`

            - `String text`

              maxLength: 5000000, minLength: 0

            - `JsonValue type = "text"`

          - `class BetaThinkingBlock:`

            - `String signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `String thinking`

              The text of Claude's thinking process for this block.

            - `JsonValue type = "thinking"`

          - `class BetaRedactedThinkingBlock:`

            - `String data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `JsonValue type = "redacted_thinking"`

          - `class BetaToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              minLength: 1

            - `JsonValue type = "tool_use"`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue type = "direct"`

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type = "code_execution_20250825"`

              - `class BetaServerToolCaller20260120:`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type = "code_execution_20260120"`

            - `Optional<String> toolsetName`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaServerToolUseBlock:`

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

            - `JsonValue type = "server_tool_use"`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebSearchToolResultBlock:`

            - `BetaWebSearchToolResultBlockContent content`

              - `class BetaWebSearchToolResultError:`

                - `BetaWebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

                - `JsonValue type = "web_search_tool_result_error"`

              - `List<BetaWebSearchResultBlock>`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `JsonValue type = "web_search_result"`

                - `String url`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "web_search_tool_result"`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebFetchToolResultBlock:`

            - `Content content`

              - `class BetaWebFetchToolResultErrorBlock:`

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

                - `JsonValue type = "web_fetch_tool_result_error"`

              - `class BetaWebFetchBlock:`

                - `BetaDocumentBlock content`

                  - `Optional<BetaCitationConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class BetaBase64PdfSource:`

                      - `String data`

                        format: byte

                      - `JsonValue mediaType = "application/pdf"`

                      - `JsonValue type = "base64"`

                    - `class BetaPlainTextSource:`

                      - `String data`

                      - `JsonValue mediaType = "text/plain"`

                      - `JsonValue type = "text"`

                  - `Optional<String> title`

                    The title of the document

                  - `JsonValue type = "document"`

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonValue type = "web_fetch_result"`

                - `String url`

                  Fetched content URL

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "web_fetch_tool_result"`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaAdvisorToolResultBlock:`

            - `Content content`

              - `class BetaAdvisorToolResultError:`

                - `ErrorCode errorCode`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `PROMPT_TOO_LONG("prompt_too_long")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `OVERLOADED("overloaded")`

                  - `UNAVAILABLE("unavailable")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `MODEL_NOT_FOUND("model_not_found")`

                - `JsonValue type = "advisor_tool_result_error"`

              - `class BetaAdvisorResultBlock:`

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `String text`

                - `JsonValue type = "advisor_result"`

              - `class BetaAdvisorRedactedResultBlock:`

                - `String encryptedContent`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `JsonValue type = "advisor_redacted_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "advisor_tool_result"`

          - `class BetaCodeExecutionToolResultBlock:`

            - `BetaCodeExecutionToolResultBlockContent content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class BetaCodeExecutionToolResultError:`

                - `BetaCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `JsonValue type = "code_execution_tool_result_error"`

              - `class BetaCodeExecutionResultBlock:`

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type = "code_execution_output"`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type = "code_execution_result"`

              - `class BetaEncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type = "code_execution_output"`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

                - `JsonValue type = "encrypted_code_execution_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "code_execution_tool_result"`

          - `class BetaBashCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BetaBashCodeExecutionToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                - `JsonValue type = "bash_code_execution_tool_result_error"`

              - `class BetaBashCodeExecutionResultBlock:`

                - `List<BetaBashCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type = "bash_code_execution_output"`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type = "bash_code_execution_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "bash_code_execution_tool_result"`

          - `class BetaTextEditorCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BetaTextEditorCodeExecutionToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

                - `JsonValue type = "text_editor_code_execution_tool_result_error"`

              - `class BetaTextEditorCodeExecutionViewResultBlock:`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

                - `JsonValue type = "text_editor_code_execution_view_result"`

              - `class BetaTextEditorCodeExecutionCreateResultBlock:`

                - `boolean isFileUpdate`

                - `JsonValue type = "text_editor_code_execution_create_result"`

              - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

                - `JsonValue type = "text_editor_code_execution_str_replace_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "text_editor_code_execution_tool_result"`

          - `class BetaToolSearchToolResultBlock:`

            - `Content content`

              - `class BetaToolSearchToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

                - `JsonValue type = "tool_search_tool_result_error"`

              - `class BetaToolSearchToolSearchResultBlock:`

                - `List<BetaToolReferenceBlock> toolReferences`

                  - `String toolName`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `JsonValue type = "tool_reference"`

                - `JsonValue type = "tool_search_tool_search_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "tool_search_tool_result"`

          - `class BetaMcpToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              The name of the MCP tool

            - `String serverName`

              The name of the MCP server

            - `JsonValue type = "mcp_tool_use"`

          - `class BetaMcpToolResultBlock:`

            - `Content content`

              - `String`

              - `List<BetaTextBlock>`

                - `Optional<List<BetaTextCitation>> citations`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `String text`

                  maxLength: 5000000, minLength: 0

                - `JsonValue type = "text"`

            - `boolean isError`

            - `String toolUseId`

              pattern: ^[a-zA-Z0-9_-]+$

            - `JsonValue type = "mcp_tool_result"`

          - `class BetaContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `String fileId`

            - `JsonValue type = "container_upload"`

          - `class BetaCompactionBlock:`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `Optional<String> content`

              Summary of compacted content, or null if compaction failed

            - `Optional<String> encryptedContent`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `JsonValue type = "compaction"`

          - `class BetaFallbackBlock:`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `BetaFallbackInfo from`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

                  Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

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

                - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

                  New class of intelligence, strongest in coding and cybersecurity

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

            - `BetaFallbackInfo to`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `BetaFallbackRefusalTrigger trigger`

              What caused the `from` model to hand over at this hop.

              - `Optional<Category> category`

                The policy category that triggered a refusal.

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

              - `JsonValue type = "refusal"`

            - `JsonValue type = "fallback"`

        - `Optional<BetaContextManagementResponse> contextManagement`

          Context management response.

          Information about context management strategies applied during the request.

          - `List<AppliedEdit> appliedEdits`

            List of context management edits that were applied.

            - `class BetaClearToolUses20250919EditResponse:`

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedToolUses`

                Number of tool uses that were cleared.

                minimum: 0

              - `JsonValue type = "clear_tool_uses_20250919"`

                The type of context management edit applied.

            - `class BetaClearThinking20251015EditResponse:`

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedThinkingTurns`

                Number of thinking turns that were cleared.

                minimum: 0

              - `JsonValue type = "clear_thinking_20251015"`

                The type of context management edit applied.

        - `Optional<BetaDiagnostics> diagnostics`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `Optional<CacheMissReason> cacheMissReason`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `class BetaCacheMissModelChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type = "model_changed"`

            - `class BetaCacheMissSystemChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type = "system_changed"`

            - `class BetaCacheMissToolsChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type = "tools_changed"`

            - `class BetaCacheMissMessagesChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type = "messages_changed"`

            - `class BetaCacheMissPreviousMessageNotFound:`

              - `JsonValue type = "previous_message_not_found"`

            - `class BetaCacheMissUnavailable:`

              - `JsonValue type = "unavailable"`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `JsonValue role = "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `Optional<BetaRefusalStopDetails> stopDetails`

          Structured information about a refusal.

          - `Optional<Category> category`

            The policy category that triggered a refusal.

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

          - `JsonValue type = "refusal"`

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

        - `JsonValue type = "message"`

          Object type.

          For Messages, this is always `"message"`.

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

            - `Status status`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `class BetaFallbackCreditRedeemed:`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `JsonValue type = "redeemed"`

              - `class BetaFallbackCreditNotApplied:`

                No reprice was applied; `reason` says why.

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

                - `JsonValue type = "not_applied"`

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

            - `class BetaMessageIterationUsage:`

              Token usage for a sampling iteration.

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

              - `JsonValue type = "message"`

                Usage for a sampling iteration

            - `class BetaCompactionIterationUsage:`

              Token usage for a compaction iteration.

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

              - `JsonValue type = "compaction"`

                Usage for a compaction iteration

            - `class BetaAdvisorMessageIterationUsage:`

              Token usage for an advisor sub-inference iteration.

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

              - `JsonValue type = "advisor_message"`

                Usage for an advisor sub-inference iteration

            - `class BetaFallbackMessageIterationUsage:`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

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

              - `JsonValue type = "fallback_message"`

                Usage for the fallback-model attempt that served the response

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

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `STANDARD("standard")`

            - `FAST("fast")`

        - `Optional<List<BetaThinkingDroppedInputTransformation>> inputTransformations`

          Changes the API made to the request's input before showing it to the model:
          one entry per change, in request order. Today the only entry type is
          `thinking_dropped` — a `thinking`, `redacted_thinking` or `connector_text`
          block from the request's `messages` that was removed from the prompt instead
          of being shown to the model because it failed a binding check. More entry
          types may be added over time; ignore types you do not recognize.

          Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
          every such response from a model that supports extended thinking, as `[]`
          when nothing was changed; without the beta, blocks are removed all the same
          but nothing is reported. Removed blocks contribute nothing to
          `usage.input_tokens`. When streaming, the array is final in `message_start`;
          the final `message_delta` event carries it only when a server-side model
          fallback happened mid-stream, in which case it holds the serving model's
          entries and replaces the one in `message_start`.

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

          - `JsonValue type = "thinking_dropped"`

            Always `thinking_dropped` for this entry type.

      - `JsonValue type = "succeeded"`

    - `class BetaMessageBatchErroredResult:`

      - `BetaErrorResponse error`

        - `BetaError error`

          - `class BetaInvalidRequestError:`

            - `String message`

            - `JsonValue type = "invalid_request_error"`

          - `class BetaAuthenticationError:`

            - `String message`

            - `JsonValue type = "authentication_error"`

          - `class BetaBillingError:`

            - `String message`

            - `JsonValue type = "billing_error"`

          - `class BetaPermissionError:`

            - `String message`

            - `JsonValue type = "permission_error"`

          - `class BetaNotFoundError:`

            - `String message`

            - `JsonValue type = "not_found_error"`

          - `class BetaRateLimitError:`

            - `String message`

            - `JsonValue type = "rate_limit_error"`

          - `class BetaGatewayTimeoutError:`

            - `String message`

            - `JsonValue type = "timeout_error"`

          - `class BetaApiError:`

            - `String message`

            - `JsonValue type = "api_error"`

          - `class BetaOverloadedError:`

            - `String message`

            - `JsonValue type = "overloaded_error"`

        - `Optional<String> requestId`

        - `JsonValue type = "error"`

      - `JsonValue type = "errored"`

    - `class BetaMessageBatchCanceledResult:`

      - `JsonValue type = "canceled"`

    - `class BetaMessageBatchExpiredResult:`

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
