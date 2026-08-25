# Retrieve Message Batch results

`client.Beta.Messages.Batches.Results(ctx, messageBatchID, query) (*BetaMessageBatchIndividualResponse, error)`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `messageBatchID string`

  ID of the Message Batch.

- `query BetaMessageBatchResultsParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

## Returns

- `type BetaMessageBatchIndividualResponse struct{…}`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `CustomID string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `Result BetaMessageBatchResultUnion`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `type BetaMessageBatchSucceededResult struct{…}`

      - `Message BetaMessage`

        - `ID string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Container BetaContainer`

          Information about the container used in the request (for the code execution tool)

          - `ID string`

            Identifier for the container used in this request

          - `ExpiresAt Time`

            The time at which the container will expire.

            format: date-time

          - `Skills []BetaSkill`

            Skills loaded in the container

            - `SkillID string`

              Skill ID

              maxLength: 64, minLength: 1

            - `Type BetaSkillType`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `const BetaSkillTypeAnthropic BetaSkillType = "anthropic"`

              - `const BetaSkillTypeCustom BetaSkillType = "custom"`

            - `Version string`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

        - `Content []BetaContentBlockUnion`

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

          - `type BetaTextBlock struct{…}`

            - `Citations []BetaTextCitationUnion`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `type BetaCitationCharLocation struct{…}`

                - `CitedText string`

                - `DocumentIndex int64`

                  minimum: 0

                - `DocumentTitle string`

                - `EndCharIndex int64`

                - `FileID string`

                - `StartCharIndex int64`

                  minimum: 0

                - `Type CharLocation`

                  default: char_location

              - `type BetaCitationPageLocation struct{…}`

                - `CitedText string`

                - `DocumentIndex int64`

                  minimum: 0

                - `DocumentTitle string`

                - `EndPageNumber int64`

                - `FileID string`

                - `StartPageNumber int64`

                  minimum: 1

                - `Type PageLocation`

                  default: page_location

              - `type BetaCitationContentBlockLocation struct{…}`

                - `CitedText string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `DocumentIndex int64`

                  minimum: 0

                - `DocumentTitle string`

                - `EndBlockIndex int64`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `FileID string`

                - `StartBlockIndex int64`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `Type ContentBlockLocation`

                  default: content_block_location

              - `type BetaCitationsWebSearchResultLocation struct{…}`

                - `CitedText string`

                - `EncryptedIndex string`

                - `Title string`

                  maxLength: 512

                - `Type WebSearchResultLocation`

                  default: web_search_result_location

                - `URL string`

              - `type BetaCitationSearchResultLocation struct{…}`

                - `CitedText string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `EndBlockIndex int64`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `SearchResultIndex int64`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `Source string`

                - `StartBlockIndex int64`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `Title string`

                - `Type SearchResultLocation`

                  default: search_result_location

            - `Text string`

              maxLength: 5000000, minLength: 0

            - `Type Text`

              default: text

          - `type BetaThinkingBlock struct{…}`

            - `Signature string`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `Thinking string`

              The text of Claude's thinking process for this block.

            - `Type Thinking`

              default: thinking

          - `type BetaRedactedThinkingBlock struct{…}`

            - `Data string`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `Type RedactedThinking`

              default: redacted_thinking

          - `type BetaToolUseBlock struct{…}`

            - `ID string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input map[string, any]`

            - `Name string`

              minLength: 1

            - `Type ToolUse`

              default: tool_use

            - `Caller BetaToolUseBlockCallerUnion Optional`

              Tool invocation directly from the model.

              - `type BetaDirectCaller struct{…}`

                Tool invocation directly from the model.

                - `Type Direct`

              - `type BetaServerToolCaller struct{…}`

                Tool invocation generated by a server-side tool.

                - `ToolID string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `Type CodeExecution20250825`

              - `type BetaServerToolCaller20260120 struct{…}`

                - `ToolID string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `Type CodeExecution20260120`

            - `ToolsetName string Optional`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `type BetaServerToolUseBlock struct{…}`

            - `ID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Input map[string, any]`

            - `Name BetaServerToolUseBlockName`

              - `const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"`

              - `const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web_search"`

              - `const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web_fetch"`

              - `const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code_execution"`

              - `const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash_code_execution"`

              - `const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text_editor_code_execution"`

              - `const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool_search_tool_regex"`

              - `const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool_search_tool_bm25"`

            - `Type ServerToolUse`

              default: server_tool_use

            - `Caller BetaServerToolUseBlockCallerUnion Optional`

              Tool invocation directly from the model.

              - `type BetaDirectCaller struct{…}`

                Tool invocation directly from the model.

              - `type BetaServerToolCaller struct{…}`

                Tool invocation generated by a server-side tool.

              - `type BetaServerToolCaller20260120 struct{…}`

          - `type BetaWebSearchToolResultBlock struct{…}`

            - `Content BetaWebSearchToolResultBlockContentUnion`

              - `type BetaWebSearchToolResultError struct{…}`

                - `ErrorCode BetaWebSearchToolResultErrorCode`

                  - `const BetaWebSearchToolResultErrorCodeInvalidToolInput BetaWebSearchToolResultErrorCode = "invalid_tool_input"`

                  - `const BetaWebSearchToolResultErrorCodeUnavailable BetaWebSearchToolResultErrorCode = "unavailable"`

                  - `const BetaWebSearchToolResultErrorCodeMaxUsesExceeded BetaWebSearchToolResultErrorCode = "max_uses_exceeded"`

                  - `const BetaWebSearchToolResultErrorCodeTooManyRequests BetaWebSearchToolResultErrorCode = "too_many_requests"`

                  - `const BetaWebSearchToolResultErrorCodeQueryTooLong BetaWebSearchToolResultErrorCode = "query_too_long"`

                  - `const BetaWebSearchToolResultErrorCodeRequestTooLarge BetaWebSearchToolResultErrorCode = "request_too_large"`

                - `Type WebSearchToolResultError`

                  default: web_search_tool_result_error

              - `type BetaWebSearchToolResultBlockContentArray []BetaWebSearchResultBlock`

                - `EncryptedContent string`

                - `PageAge string`

                - `Title string`

                - `Type WebSearchResult`

                  default: web_search_result

                - `URL string`

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type WebSearchToolResult`

              default: web_search_tool_result

            - `Caller BetaWebSearchToolResultBlockCallerUnion Optional`

              Tool invocation directly from the model.

              - `type BetaDirectCaller struct{…}`

                Tool invocation directly from the model.

              - `type BetaServerToolCaller struct{…}`

                Tool invocation generated by a server-side tool.

              - `type BetaServerToolCaller20260120 struct{…}`

          - `type BetaWebFetchToolResultBlock struct{…}`

            - `Content BetaWebFetchToolResultBlockContentUnion`

              - `type BetaWebFetchToolResultErrorBlock struct{…}`

                - `ErrorCode BetaWebFetchToolResultErrorCode`

                  - `const BetaWebFetchToolResultErrorCodeInvalidToolInput BetaWebFetchToolResultErrorCode = "invalid_tool_input"`

                  - `const BetaWebFetchToolResultErrorCodeURLTooLong BetaWebFetchToolResultErrorCode = "url_too_long"`

                  - `const BetaWebFetchToolResultErrorCodeURLNotAllowed BetaWebFetchToolResultErrorCode = "url_not_allowed"`

                  - `const BetaWebFetchToolResultErrorCodeURLNotInPriorContext BetaWebFetchToolResultErrorCode = "url_not_in_prior_context"`

                  - `const BetaWebFetchToolResultErrorCodeURLNotAccessible BetaWebFetchToolResultErrorCode = "url_not_accessible"`

                  - `const BetaWebFetchToolResultErrorCodeUnsupportedContentType BetaWebFetchToolResultErrorCode = "unsupported_content_type"`

                  - `const BetaWebFetchToolResultErrorCodeTooManyRequests BetaWebFetchToolResultErrorCode = "too_many_requests"`

                  - `const BetaWebFetchToolResultErrorCodeMaxUsesExceeded BetaWebFetchToolResultErrorCode = "max_uses_exceeded"`

                  - `const BetaWebFetchToolResultErrorCodeUnavailable BetaWebFetchToolResultErrorCode = "unavailable"`

                - `Type WebFetchToolResultError`

                  default: web_fetch_tool_result_error

              - `type BetaWebFetchBlock struct{…}`

                - `Content BetaDocumentBlock`

                  - `Citations BetaCitationConfig`

                    Citation configuration for the document

                    - `Enabled bool`

                      default: false

                  - `Source BetaDocumentBlockSourceUnion`

                    - `type BetaBase64PDFSource struct{…}`

                      - `Data string`

                        format: byte

                      - `MediaType ApplicationPDF`

                      - `Type Base64`

                    - `type BetaPlainTextSource struct{…}`

                      - `Data string`

                      - `MediaType TextPlain`

                      - `Type Text`

                  - `Title string`

                    The title of the document

                  - `Type Document`

                    default: document

                - `RetrievedAt string`

                  ISO 8601 timestamp when the content was retrieved

                - `Type WebFetchResult`

                  default: web_fetch_result

                - `URL string`

                  Fetched content URL

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type WebFetchToolResult`

              default: web_fetch_tool_result

            - `Caller BetaWebFetchToolResultBlockCallerUnion Optional`

              Tool invocation directly from the model.

              - `type BetaDirectCaller struct{…}`

                Tool invocation directly from the model.

              - `type BetaServerToolCaller struct{…}`

                Tool invocation generated by a server-side tool.

              - `type BetaServerToolCaller20260120 struct{…}`

          - `type BetaAdvisorToolResultBlock struct{…}`

            - `Content BetaAdvisorToolResultBlockContentUnion`

              - `type BetaAdvisorToolResultError struct{…}`

                - `ErrorCode BetaAdvisorToolResultErrorErrorCode`

                  - `const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max_uses_exceeded"`

                  - `const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt_too_long"`

                  - `const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too_many_requests"`

                  - `const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"`

                  - `const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"`

                  - `const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution_time_exceeded"`

                  - `const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model_not_found"`

                - `Type AdvisorToolResultError`

                  default: advisor_tool_result_error

              - `type BetaAdvisorResultBlock struct{…}`

                - `StopReason string`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `Text string`

                - `Type AdvisorResult`

                  default: advisor_result

              - `type BetaAdvisorRedactedResultBlock struct{…}`

                - `EncryptedContent string`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `StopReason string`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `Type AdvisorRedactedResult`

                  default: advisor_redacted_result

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type AdvisorToolResult`

              default: advisor_tool_result

          - `type BetaCodeExecutionToolResultBlock struct{…}`

            - `Content BetaCodeExecutionToolResultBlockContentUnion`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `type BetaCodeExecutionToolResultError struct{…}`

                - `ErrorCode BetaCodeExecutionToolResultErrorCode`

                  - `const BetaCodeExecutionToolResultErrorCodeInvalidToolInput BetaCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                  - `const BetaCodeExecutionToolResultErrorCodeUnavailable BetaCodeExecutionToolResultErrorCode = "unavailable"`

                  - `const BetaCodeExecutionToolResultErrorCodeTooManyRequests BetaCodeExecutionToolResultErrorCode = "too_many_requests"`

                  - `const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded BetaCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                - `Type CodeExecutionToolResultError`

                  default: code_execution_tool_result_error

              - `type BetaCodeExecutionResultBlock struct{…}`

                - `Content []BetaCodeExecutionOutputBlock`

                  - `FileID string`

                  - `Type CodeExecutionOutput`

                    default: code_execution_output

                - `ReturnCode int64`

                - `Stderr string`

                - `Stdout string`

                - `Type CodeExecutionResult`

                  default: code_execution_result

              - `type BetaEncryptedCodeExecutionResultBlock struct{…}`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `Content []BetaCodeExecutionOutputBlock`

                  - `FileID string`

                  - `Type CodeExecutionOutput`

                    default: code_execution_output

                - `EncryptedStdout string`

                - `ReturnCode int64`

                - `Stderr string`

                - `Type EncryptedCodeExecutionResult`

                  default: encrypted_code_execution_result

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type CodeExecutionToolResult`

              default: code_execution_tool_result

          - `type BetaBashCodeExecutionToolResultBlock struct{…}`

            - `Content BetaBashCodeExecutionToolResultBlockContentUnion`

              - `type BetaBashCodeExecutionToolResultError struct{…}`

                - `ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode`

                  - `const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"`

                  - `const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"`

                  - `const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too_many_requests"`

                  - `const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"`

                  - `const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output_file_too_large"`

                - `Type BashCodeExecutionToolResultError`

                  default: bash_code_execution_tool_result_error

              - `type BetaBashCodeExecutionResultBlock struct{…}`

                - `Content []BetaBashCodeExecutionOutputBlock`

                  - `FileID string`

                  - `Type BashCodeExecutionOutput`

                    default: bash_code_execution_output

                - `ReturnCode int64`

                - `Stderr string`

                - `Stdout string`

                - `Type BashCodeExecutionResult`

                  default: bash_code_execution_result

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type BashCodeExecutionToolResult`

              default: bash_code_execution_tool_result

          - `type BetaTextEditorCodeExecutionToolResultBlock struct{…}`

            - `Content BetaTextEditorCodeExecutionToolResultBlockContentUnion`

              - `type BetaTextEditorCodeExecutionToolResultError struct{…}`

                - `ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode`

                  - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"`

                  - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"`

                  - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too_many_requests"`

                  - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"`

                  - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file_not_found"`

                - `ErrorMessage string`

                - `Type TextEditorCodeExecutionToolResultError`

                  default: text_editor_code_execution_tool_result_error

              - `type BetaTextEditorCodeExecutionViewResultBlock struct{…}`

                - `Content string`

                - `FileType BetaTextEditorCodeExecutionViewResultBlockFileType`

                  - `const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"`

                  - `const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"`

                  - `const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"`

                - `NumLines int64`

                - `StartLine int64`

                - `TotalLines int64`

                - `Type TextEditorCodeExecutionViewResult`

                  default: text_editor_code_execution_view_result

              - `type BetaTextEditorCodeExecutionCreateResultBlock struct{…}`

                - `IsFileUpdate bool`

                - `Type TextEditorCodeExecutionCreateResult`

                  default: text_editor_code_execution_create_result

              - `type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}`

                - `Lines []string`

                - `NewLines int64`

                - `NewStart int64`

                - `OldLines int64`

                - `OldStart int64`

                - `Type TextEditorCodeExecutionStrReplaceResult`

                  default: text_editor_code_execution_str_replace_result

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type TextEditorCodeExecutionToolResult`

              default: text_editor_code_execution_tool_result

          - `type BetaToolSearchToolResultBlock struct{…}`

            - `Content BetaToolSearchToolResultBlockContentUnion`

              - `type BetaToolSearchToolResultError struct{…}`

                - `ErrorCode BetaToolSearchToolResultErrorErrorCode`

                  - `const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid_tool_input"`

                  - `const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"`

                  - `const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too_many_requests"`

                  - `const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution_time_exceeded"`

                - `ErrorMessage string`

                - `Type ToolSearchToolResultError`

                  default: tool_search_tool_result_error

              - `type BetaToolSearchToolSearchResultBlock struct{…}`

                - `ToolReferences []BetaToolReferenceBlock`

                  - `ToolName string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `Type ToolReference`

                    default: tool_reference

                - `Type ToolSearchToolSearchResult`

                  default: tool_search_tool_search_result

            - `ToolUseID string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Type ToolSearchToolResult`

              default: tool_search_tool_result

          - `type BetaMCPToolUseBlock struct{…}`

            - `ID string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input map[string, any]`

            - `Name string`

              The name of the MCP tool

            - `ServerName string`

              The name of the MCP server

            - `Type MCPToolUse`

              default: mcp_tool_use

          - `type BetaMCPToolResultBlock struct{…}`

            - `Content BetaMCPToolResultBlockContentUnion`

              - `string`

              - `type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent []BetaTextBlock`

                - `Citations []BetaTextCitationUnion`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `Text string`

                  maxLength: 5000000, minLength: 0

                - `Type Text`

                  default: text

            - `IsError bool`

              default: false

            - `ToolUseID string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Type MCPToolResult`

              default: mcp_tool_result

          - `type BetaContainerUploadBlock struct{…}`

            Response model for a file uploaded to the container.

            - `FileID string`

            - `Type ContainerUpload`

              default: container_upload

          - `type BetaCompactionBlock struct{…}`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `Content string`

              Summary of compacted content, or null if compaction failed

            - `EncryptedContent string`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `Type Compaction`

              default: compaction

          - `type BetaFallbackBlock struct{…}`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `From BetaFallbackInfo`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `type Model string`

                  The model that will complete your prompt.

                  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                  - `const ModelClaudeSonnet5 Model = "claude-sonnet-5"`

                    High-performance model for coding and agents

                  - `const ModelClaudeFable5 Model = "claude-fable-5"`

                    Next generation of intelligence for the hardest knowledge work and coding problems

                  - `const ModelClaudeMythos5 Model = "claude-mythos-5"`

                    Most capable model for cybersecurity and biology research

                  - `const ModelClaudeOpus5 Model = "claude-opus-5"`

                    Powerful intelligence for long-running agents and coding

                  - `const ModelClaudeOpus4_8 Model = "claude-opus-4-8"`

                    Powerful intelligence for long-running agents and coding

                  - `const ModelClaudeOpus4_7 Model = "claude-opus-4-7"`

                    Powerful intelligence for long-running agents and coding

                  - `const ModelClaudeMythosPreview Model = "claude-mythos-preview"`

                    New class of intelligence, strongest in coding and cybersecurity

                  - `const ModelClaudeOpus4_6 Model = "claude-opus-4-6"`

                    Powerful intelligence for long-running agents and coding

                  - `const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"`

                    Best combination of speed and intelligence

                  - `const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"`

                    Fastest model with near-frontier intelligence

                  - `const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"`

                    Fastest model with near-frontier intelligence

                  - `const ModelClaudeOpus4_5 Model = "claude-opus-4-5"`

                    Powerful intelligence for long-running agents and coding

                  - `const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"`

                    Powerful intelligence for long-running agents and coding

                  - `const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"`

                    High-performance model for agents and coding

                  - `const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"`

                    High-performance model for agents and coding

                - `string`

            - `To BetaFallbackInfo`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `Trigger BetaFallbackRefusalTrigger`

              What caused the `from` model to hand over at this hop.

              - `Category BetaFallbackRefusalTriggerCategory`

                The policy category that triggered a refusal.

                - `const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"`

                  The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

                - `const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"`

                  The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

                - `const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier_llm"`

                  The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

                - `const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning_extraction"`

                  The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

                - `const BetaFallbackRefusalTriggerCategoryGeneralHarms BetaFallbackRefusalTriggerCategory = "general_harms"`

                  The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

              - `Type Refusal`

                default: refusal

            - `Type Fallback`

              default: fallback

        - `ContextManagement BetaContextManagementResponse`

          Context management response.

          Information about context management strategies applied during the request.

          - `AppliedEdits []BetaContextManagementResponseAppliedEditUnion`

            List of context management edits that were applied.

            - `type BetaClearToolUses20250919EditResponse struct{…}`

              - `ClearedInputTokens int64`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `ClearedToolUses int64`

                Number of tool uses that were cleared.

                minimum: 0

              - `Type ClearToolUses20250919`

                The type of context management edit applied.

                default: clear_tool_uses_20250919

            - `type BetaClearThinking20251015EditResponse struct{…}`

              - `ClearedInputTokens int64`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `ClearedThinkingTurns int64`

                Number of thinking turns that were cleared.

                minimum: 0

              - `Type ClearThinking20251015`

                The type of context management edit applied.

                default: clear_thinking_20251015

        - `Diagnostics BetaDiagnostics`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `CacheMissReason BetaDiagnosticsCacheMissReasonUnion`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `type BetaCacheMissModelChanged struct{…}`

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `Type ModelChanged`

                default: model_changed

            - `type BetaCacheMissSystemChanged struct{…}`

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `Type SystemChanged`

                default: system_changed

            - `type BetaCacheMissToolsChanged struct{…}`

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `Type ToolsChanged`

                default: tools_changed

            - `type BetaCacheMissMessagesChanged struct{…}`

              - `CacheMissedInputTokens int64`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `Type MessagesChanged`

                default: messages_changed

            - `type BetaCacheMissPreviousMessageNotFound struct{…}`

              - `Type PreviousMessageNotFound`

                default: previous_message_not_found

            - `type BetaCacheMissUnavailable struct{…}`

              - `Type Unavailable`

                default: unavailable

        - `Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Role Assistant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          default: assistant

        - `StopDetails BetaRefusalStopDetails`

          Structured information about a refusal.

          - `Category BetaRefusalStopDetailsCategory`

            The policy category that triggered a refusal.

            - `const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier_llm"`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning_extraction"`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `const BetaRefusalStopDetailsCategoryGeneralHarms BetaRefusalStopDetailsCategory = "general_harms"`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `Explanation string`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `FallbackCreditToken string`

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

          - `FallbackHasPrefillClaim bool`

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

          - `RecommendedModel string`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `Type Refusal`

            default: refusal

        - `StopReason BetaStopReason`

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

          - `const BetaStopReasonEndTurn BetaStopReason = "end_turn"`

          - `const BetaStopReasonMaxTokens BetaStopReason = "max_tokens"`

          - `const BetaStopReasonStopSequence BetaStopReason = "stop_sequence"`

          - `const BetaStopReasonToolUse BetaStopReason = "tool_use"`

          - `const BetaStopReasonPauseTurn BetaStopReason = "pause_turn"`

          - `const BetaStopReasonCompaction BetaStopReason = "compaction"`

          - `const BetaStopReasonRefusal BetaStopReason = "refusal"`

          - `const BetaStopReasonModelContextWindowExceeded BetaStopReason = "model_context_window_exceeded"`

        - `StopSequence string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `Type Message`

          Object type.

          For Messages, this is always `"message"`.

          default: message

        - `Usage BetaUsage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `CacheCreation BetaCacheCreation`

            Breakdown of cached tokens by TTL

            - `Ephemeral1hInputTokens int64`

              The number of input tokens used to create the 1 hour cache entry.

              default: 0, minimum: 0

            - `Ephemeral5mInputTokens int64`

              The number of input tokens used to create the 5 minute cache entry.

              default: 0, minimum: 0

          - `CacheCreationInputTokens int64`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `CacheReadInputTokens int64`

            The number of input tokens read from the cache.

            minimum: 0

          - `FallbackCredit BetaFallbackCreditUsage`

            Outcome of the `fallback_credit_token` presented on this request.

            - `Status BetaFallbackCreditUsageStatusUnion`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `type BetaFallbackCreditRedeemed struct{…}`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `Type Redeemed`

                  default: redeemed

              - `type BetaFallbackCreditNotApplied struct{…}`

                No reprice was applied; `reason` says why.

                - `Reason BetaFallbackCreditNotAppliedReason`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `const BetaFallbackCreditNotAppliedReasonBodyMismatch BetaFallbackCreditNotAppliedReason = "body_mismatch"`

                  - `const BetaFallbackCreditNotAppliedReasonContinuationExcluded BetaFallbackCreditNotAppliedReason = "continuation_excluded"`

                  - `const BetaFallbackCreditNotAppliedReasonContinuationOnly BetaFallbackCreditNotAppliedReason = "continuation_only"`

                  - `const BetaFallbackCreditNotAppliedReasonExpired BetaFallbackCreditNotAppliedReason = "expired"`

                  - `const BetaFallbackCreditNotAppliedReasonInvalidTargetModel BetaFallbackCreditNotAppliedReason = "invalid_target_model"`

                  - `const BetaFallbackCreditNotAppliedReasonNotEnabled BetaFallbackCreditNotAppliedReason = "not_enabled"`

                  - `const BetaFallbackCreditNotAppliedReasonRepriceUnavailable BetaFallbackCreditNotAppliedReason = "reprice_unavailable"`

                  - `const BetaFallbackCreditNotAppliedReasonTemporarilyUnavailable BetaFallbackCreditNotAppliedReason = "temporarily_unavailable"`

                  - `const BetaFallbackCreditNotAppliedReasonVariantFieldsPresent BetaFallbackCreditNotAppliedReason = "variant_fields_present"`

                  - `const BetaFallbackCreditNotAppliedReasonWrongOrganization BetaFallbackCreditNotAppliedReason = "wrong_organization"`

                  - `const BetaFallbackCreditNotAppliedReasonWrongPlatform BetaFallbackCreditNotAppliedReason = "wrong_platform"`

                  - `const BetaFallbackCreditNotAppliedReasonWrongWorkspace BetaFallbackCreditNotAppliedReason = "wrong_workspace"`

                - `Type NotApplied`

                  default: not_applied

                - `RemoveToRedeem []string Optional`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `InferenceGeo string`

            The geographic region where inference was performed for this request.

          - `InputTokens int64`

            The number of input tokens which were used.

            minimum: 0

          - `Iterations BetaIterationsUsage`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the true context window size from the last iteration
            - Understand token accumulation across server-side tool use loops

            - `type BetaMessageIterationUsage struct{…}`

              Token usage for a sampling iteration.

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

              - `Type Message`

                Usage for a sampling iteration

                default: message

            - `type BetaCompactionIterationUsage struct{…}`

              Token usage for a compaction iteration.

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

              - `Type Compaction`

                Usage for a compaction iteration

                default: compaction

            - `type BetaAdvisorMessageIterationUsage struct{…}`

              Token usage for an advisor sub-inference iteration.

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

              - `Type AdvisorMessage`

                Usage for an advisor sub-inference iteration

                default: advisor_message

            - `type BetaFallbackMessageIterationUsage struct{…}`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `CacheCreation BetaCacheCreation`

                Breakdown of cached tokens by TTL

              - `CacheCreationInputTokens int64`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `CacheReadInputTokens int64`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `InputTokens int64`

                The number of input tokens which were used.

                minimum: 0

              - `Model Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `OutputTokens int64`

                The number of output tokens which were used.

                minimum: 0

              - `Type FallbackMessage`

                Usage for the fallback-model attempt that served the response

                default: fallback_message

          - `OutputTokens int64`

            The number of output tokens which were used.

            minimum: 0

          - `OutputTokensDetails BetaOutputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `ThinkingTokens int64`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              default: 0, minimum: 0

          - `ServerToolUse BetaServerToolUsage`

            The number of server tool requests.

            - `WebFetchRequests int64`

              The number of web fetch tool requests.

              default: 0, minimum: 0

            - `WebSearchRequests int64`

              The number of web search tool requests.

              default: 0, minimum: 0

          - `ServiceTier BetaUsageServiceTier`

            If the request used the priority, standard, or batch tier.

            - `const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"`

            - `const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"`

            - `const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"`

          - `Speed BetaUsageSpeed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `const BetaUsageSpeedStandard BetaUsageSpeed = "standard"`

            - `const BetaUsageSpeedFast BetaUsageSpeed = "fast"`

      - `Type Succeeded`

        default: succeeded

    - `type BetaMessageBatchErroredResult struct{…}`

      - `Error BetaErrorResponse`

        - `Error BetaErrorUnion`

          - `type BetaInvalidRequestError struct{…}`

            - `Message string`

              default: Invalid request

            - `Type InvalidRequestError`

              default: invalid_request_error

          - `type BetaAuthenticationError struct{…}`

            - `Message string`

              default: Authentication error

            - `Type AuthenticationError`

              default: authentication_error

          - `type BetaBillingError struct{…}`

            - `Message string`

              default: Billing error

            - `Type BillingError`

              default: billing_error

          - `type BetaPermissionError struct{…}`

            - `Message string`

              default: Permission denied

            - `Type PermissionError`

              default: permission_error

          - `type BetaNotFoundError struct{…}`

            - `Message string`

              default: Not found

            - `Type NotFoundError`

              default: not_found_error

          - `type BetaRateLimitError struct{…}`

            - `Message string`

              default: Rate limited

            - `Type RateLimitError`

              default: rate_limit_error

          - `type BetaGatewayTimeoutError struct{…}`

            - `Message string`

              default: Request timeout

            - `Type TimeoutError`

              default: timeout_error

          - `type BetaAPIError struct{…}`

            - `Message string`

              default: Internal server error

            - `Type APIError`

              default: api_error

          - `type BetaOverloadedError struct{…}`

            - `Message string`

              default: Overloaded

            - `Type OverloadedError`

              default: overloaded_error

        - `RequestID string`

        - `Type Error`

          default: error

      - `Type Errored`

        default: errored

    - `type BetaMessageBatchCanceledResult struct{…}`

      - `Type Canceled`

        default: canceled

    - `type BetaMessageBatchExpiredResult struct{…}`

      - `Type Expired`

        default: expired

## Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	stream := client.Beta.Messages.Batches.ResultsStreaming(
		context.TODO(),
		"message_batch_id",
		anthropic.BetaMessageBatchResultsParams{},
	)
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
```
