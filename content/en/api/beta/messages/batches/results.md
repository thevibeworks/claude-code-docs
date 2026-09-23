---
title: Retrieve Message Batch results
url: https://platform.claude.com/docs/en/api/beta/messages/batches/results
---

# Retrieve Message Batch results

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Path parameters

- `message_batch_id: string`

  ID of the Message Batch.

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more`

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

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaMessageBatchIndividualResponse object`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: BetaMessageBatchResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `BetaMessageBatchSucceededResult object`

      - `type: "succeeded"`

        default: succeeded

      - `message: BetaMessage`

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

          default: message

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: BetaContainer or null`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

            format: date-time

          - `skills: array of BetaContainerSkill or null`

            Skills loaded in the container

            - `type: "anthropic" or "custom"`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `"anthropic"`

              - `"custom"`

            - `skill_id: string`

              Skill ID

              maxLength: 64, minLength: 1

            - `version: string`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

        - `content: array of BetaContentBlock`

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

          - `BetaTextBlock object`

            - `type: "text"`

              default: text

            - `citations: array of BetaTextCitation or null`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `BetaCitationCharLocation object`

                - `type: "char_location"`

                  default: char_location

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string or null`

                - `end_char_index: number`

                - `file_id: string or null`

                - `start_char_index: number`

                  minimum: 0

              - `BetaCitationPageLocation object`

                - `type: "page_location"`

                  default: page_location

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string or null`

                - `end_page_number: number`

                - `file_id: string or null`

                - `start_page_number: number`

                  minimum: 1

              - `BetaCitationContentBlockLocation object`

                - `type: "content_block_location"`

                  default: content_block_location

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                  minimum: 0

                - `document_title: string or null`

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `file_id: string or null`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

              - `BetaCitationsWebSearchResultLocation object`

                - `type: "web_search_result_location"`

                  default: web_search_result_location

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string or null`

                  maxLength: 512

                - `url: string`

              - `BetaCitationSearchResultLocation object`

                - `type: "search_result_location"`

                  default: search_result_location

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `search_result_index: number`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `source: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `title: string or null`

            - `text: string`

              minLength: 0

          - `BetaThinkingBlock object`

            - `type: "thinking"`

              default: thinking

            - `signature: string`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `thinking: string`

              The text of Claude's thinking process for this block.

          - `BetaRedactedThinkingBlock object`

            - `type: "redacted_thinking"`

              default: redacted_thinking

            - `data: string`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `BetaToolUseBlock object`

            - `type: "tool_use"`

              default: tool_use

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: map[unknown]`

            - `name: string`

              minLength: 1

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

                - `type: "code_execution_20250825"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `BetaServerToolCaller20260120 object`

                - `type: "code_execution_20260120"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `toolset_name: optional string or null`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `BetaServerToolUseBlock object`

            - `type: "server_tool_use"`

              default: server_tool_use

            - `id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `input: map[unknown]`

            - `name: "advisor" or "web_search" or "web_fetch" or 5 more`

              - `"advisor"`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

              - `BetaServerToolCaller20260120 object`

          - `BetaWebSearchToolResultBlock object`

            - `type: "web_search_tool_result"`

              default: web_search_tool_result

            - `content: BetaWebSearchToolResultBlockContent`

              - `BetaWebSearchToolResultError object`

                - `type: "web_search_tool_result_error"`

                  default: web_search_tool_result_error

                - `error_code: BetaWebSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

              - `array of BetaWebSearchResultBlock`

                - `type: "web_search_result"`

                  default: web_search_result

                - `encrypted_content: string`

                - `page_age: string or null`

                - `title: string`

                - `url: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

              - `BetaServerToolCaller20260120 object`

          - `BetaWebFetchToolResultBlock object`

            - `type: "web_fetch_tool_result"`

              default: web_fetch_tool_result

            - `content: BetaWebFetchToolResultErrorBlock or BetaWebFetchBlock`

              - `BetaWebFetchToolResultErrorBlock object`

                - `type: "web_fetch_tool_result_error"`

                  default: web_fetch_tool_result_error

                - `error_code: BetaWebFetchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_in_prior_context"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                  - `"content_too_large"`

              - `BetaWebFetchBlock object`

                - `type: "web_fetch_result"`

                  default: web_fetch_result

                - `content: BetaDocumentBlock`

                  - `type: "document"`

                    default: document

                  - `citations: BetaCitationConfig or null`

                    Citation configuration for the document

                    - `enabled: boolean`

                      default: false

                  - `source: BetaBase64PDFSource or BetaPlainTextSource`

                    - `BetaBase64PDFSource object`

                      - `type: "base64"`

                      - `data: string`

                        format: byte

                      - `media_type: "application/pdf"`

                    - `BetaPlainTextSource object`

                      - `type: "text"`

                      - `data: string`

                      - `media_type: "text/plain"`

                  - `title: string or null`

                    The title of the document

                - `retrieved_at: string or null`

                  ISO 8601 timestamp when the content was retrieved

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

              - `BetaServerToolCaller20260120 object`

          - `BetaAdvisorToolResultBlock object`

            - `type: "advisor_tool_result"`

              default: advisor_tool_result

            - `content: BetaAdvisorToolResultError or BetaAdvisorResultBlock or BetaAdvisorRedactedResultBlock`

              - `BetaAdvisorToolResultError object`

                - `type: "advisor_tool_result_error"`

                  default: advisor_tool_result_error

                - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more`

                  - `"max_uses_exceeded"`

                  - `"prompt_too_long"`

                  - `"too_many_requests"`

                  - `"overloaded"`

                  - `"unavailable"`

                  - `"execution_time_exceeded"`

                  - `"model_not_found"`

              - `BetaAdvisorResultBlock object`

                - `type: "advisor_result"`

                  default: advisor_result

                - `stop_reason: string or null`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `text: string`

              - `BetaAdvisorRedactedResultBlock object`

                - `type: "advisor_redacted_result"`

                  default: advisor_redacted_result

                - `encrypted_content: string`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `stop_reason: string or null`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `BetaCodeExecutionToolResultBlock object`

            - `type: "code_execution_tool_result"`

              default: code_execution_tool_result

            - `content: BetaCodeExecutionToolResultBlockContent`

              - `BetaCodeExecutionToolResultError object`

                - `type: "code_execution_tool_result_error"`

                  default: code_execution_tool_result_error

                - `error_code: BetaCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

              - `BetaCodeExecutionResultBlock object`

                - `type: "code_execution_result"`

                  default: code_execution_result

                - `content: array of BetaCodeExecutionOutputBlock`

                  - `type: "code_execution_output"`

                    default: code_execution_output

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

              - `BetaEncryptedCodeExecutionResultBlock object`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type: "encrypted_code_execution_result"`

                  default: encrypted_code_execution_result

                - `content: array of BetaCodeExecutionOutputBlock`

                  - `type: "code_execution_output"`

                    default: code_execution_output

                  - `file_id: string`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `BetaBashCodeExecutionToolResultBlock object`

            - `type: "bash_code_execution_tool_result"`

              default: bash_code_execution_tool_result

            - `content: BetaBashCodeExecutionToolResultError or BetaBashCodeExecutionResultBlock`

              - `BetaBashCodeExecutionToolResultError object`

                - `type: "bash_code_execution_tool_result_error"`

                  default: bash_code_execution_tool_result_error

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

              - `BetaBashCodeExecutionResultBlock object`

                - `type: "bash_code_execution_result"`

                  default: bash_code_execution_result

                - `content: array of BetaBashCodeExecutionOutputBlock`

                  - `type: "bash_code_execution_output"`

                    default: bash_code_execution_output

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `BetaTextEditorCodeExecutionToolResultBlock object`

            - `type: "text_editor_code_execution_tool_result"`

              default: text_editor_code_execution_tool_result

            - `content: BetaTextEditorCodeExecutionToolResultError or BetaTextEditorCodeExecutionViewResultBlock or BetaTextEditorCodeExecutionCreateResultBlock or BetaTextEditorCodeExecutionStrReplaceResultBlock`

              - `BetaTextEditorCodeExecutionToolResultError object`

                - `type: "text_editor_code_execution_tool_result_error"`

                  default: text_editor_code_execution_tool_result_error

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string or null`

              - `BetaTextEditorCodeExecutionViewResultBlock object`

                - `type: "text_editor_code_execution_view_result"`

                  default: text_editor_code_execution_view_result

                - `content: string`

                - `file_type: "text" or "image" or "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number or null`

                - `start_line: number or null`

                - `total_lines: number or null`

              - `BetaTextEditorCodeExecutionCreateResultBlock object`

                - `type: "text_editor_code_execution_create_result"`

                  default: text_editor_code_execution_create_result

                - `is_file_update: boolean`

              - `BetaTextEditorCodeExecutionStrReplaceResultBlock object`

                - `type: "text_editor_code_execution_str_replace_result"`

                  default: text_editor_code_execution_str_replace_result

                - `lines: array of string or null`

                - `new_lines: number or null`

                - `new_start: number or null`

                - `old_lines: number or null`

                - `old_start: number or null`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `BetaToolSearchToolResultBlock object`

            - `type: "tool_search_tool_result"`

              default: tool_search_tool_result

            - `content: BetaToolSearchToolResultError or BetaToolSearchToolSearchResultBlock`

              - `BetaToolSearchToolResultError object`

                - `type: "tool_search_tool_result_error"`

                  default: tool_search_tool_result_error

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string or null`

              - `BetaToolSearchToolSearchResultBlock object`

                - `type: "tool_search_tool_search_result"`

                  default: tool_search_tool_search_result

                - `tool_references: array of BetaToolReferenceBlock`

                  - `type: "tool_reference"`

                    default: tool_reference

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `BetaMCPToolUseBlock object`

            - `type: "mcp_tool_use"`

              default: mcp_tool_use

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: map[unknown]`

            - `name: string`

              The name of the MCP tool

            - `server_name: string`

              The name of the MCP server

          - `BetaMCPToolResultBlock object`

            - `type: "mcp_tool_result"`

              default: mcp_tool_result

            - `content: string or array of BetaTextBlock`

              - `string`

              - `BetaMCPToolResultBlockContent = array of BetaTextBlock`

                - `type: "text"`

                  default: text

                - `citations: array of BetaTextCitation or null`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `text: string`

                  minLength: 0

            - `is_error: boolean`

              default: false

            - `tool_use_id: string`

              pattern: ^[a-zA-Z0-9_-]+$

          - `BetaContainerUploadBlock object`

            Response model for a file uploaded to the container.

            - `type: "container_upload"`

              default: container_upload

            - `file_id: string`

          - `BetaCompactionBlock object`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `type: "compaction"`

              default: compaction

            - `content: string or null`

              Summary of compacted content, or null if compaction failed

            - `encrypted_content: string or null`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `signature: optional string or null`

              Signature over the summary, to be sent back with the block verbatim

            - `tool_changes: optional array of BetaResponseToolAdditionBlock or BetaResponseToolRemovalBlock or null`

              The tool changes of the compacted range: the `tool_addition` and `tool_removal` blocks that take the request's `tools` to the tool set in effect at the end of the range, or `[]` when the range changed no tool. Absent when the server did not compute them. Send the block back unchanged.

              - `BetaResponseToolAdditionBlock object`

                An entry of a `compaction` block's `tool_changes`: a tool the
                compacted range made available, as a reference to a `tools` entry or
                MCP toolset, or as the tool definition in effect at the end of the
                range, by value. Send it back unchanged.

                - `type: "tool_addition"`

                  default: tool_addition

                - `tool: BetaResponseToolChangeToolReference or BetaResponseToolChangeMCPToolReference or BetaResponseToolChangeMCPToolsetReference or BetaToolChangeToolDefinition`

                  The tool made available: a reference to a `tools` entry or MCP toolset, or a `tool_definition` carrying the definition by value.

                  - `BetaResponseToolChangeToolReference object`

                    Reference to a single tool, by the name the model uses to call it, as
                    a `compaction` block's `tool_changes` entry reports it: a tool
                    declared in `tools` or defined by an earlier `tool_addition` block.
                    Send it back unchanged with the block.

                    - `type: "tool_reference"`

                      default: tool_reference

                    - `name: string`

                  - `BetaResponseToolChangeMCPToolReference object`

                    Reference to a single MCP tool, by its server and its name on that
                    server, as a `compaction` block's `tool_changes` entry reports it.
                    Send it back unchanged with the block.

                    - `type: "mcp_tool_reference"`

                      default: mcp_tool_reference

                    - `name: string`

                    - `server_name: string`

                  - `BetaResponseToolChangeMCPToolsetReference object`

                    Reference to every tool in the named MCP server's toolset, as a
                    `compaction` block's `tool_changes` entry reports it. Send it back
                    unchanged with the block.

                    - `type: "mcp_toolset_reference"`

                      default: mcp_toolset_reference

                    - `server_name: string`

                  - `BetaToolChangeToolDefinition object`

                    A tool defined by value, as a `compaction` block's `tool_changes` entry
                    reports it: `definition` is the tool's definition as it was sent, in the
                    form of a `tools` entry, without `cache_control`. Send it back unchanged
                    with the block.

                    - `type: "tool_definition"`

                      default: tool_definition

                    - `definition: BetaResponseToolUnion`

                      - `BetaResponseTool object`

                        A custom tool definition, as sent.

                        - `type: optional "custom" or null`

                        - `input_schema: BetaResponseToolInputSchema`

                          [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

                          This defines the shape of the `input` that your tool accepts and that the model will produce.

                          - `type: "object"`

                          - `properties: optional map[unknown] or null`

                          - `required: optional array of string or null`

                        - `name: string`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                          maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `description: optional string`

                          Description of what this tool does.

                          Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

                        - `eager_input_streaming: optional boolean or null`

                          Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolBash20241022 object`

                        - `type: "bash_20241022"`

                        - `name: "bash"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                          - `type: "ephemeral"`

                          - `ttl: optional "5m" or "1h"`

                            The time-to-live for the cache control breakpoint.

                            This may be one the following values:

                            - `5m`: 5 minutes
                            - `1h`: 1 hour

                            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                            - `"5m"`

                            - `"1h"`

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolBash20250124 object`

                        - `type: "bash_20250124"`

                        - `name: "bash"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaCodeExecutionTool20250522 object`

                        - `type: "code_execution_20250522"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaCodeExecutionTool20250825 object`

                        - `type: "code_execution_20250825"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaCodeExecutionTool20260120 object`

                        Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

                        - `type: "code_execution_20260120"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaCodeExecutionTool20260521 object`

                        Code execution tool with REPL state persistence.

                        - `type: "code_execution_20260521"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaBrowserToolset20260801 object`

                        The browser toolset: a single `tools[]` entry (carrying no
                        `name`) that declares the browser tool family. The model is served
                        the family's tool with any members disabled via `configs` removed
                        from its schema.

                        - `type: "browser_toolset_20260801"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `configs: optional BetaBrowserToolsetConfigs or null`

                          Per-member configuration for `browser_toolset_20260801`: one
                          optional field per member tool, keyed by the member name — the same
                          name the member's `tool_use` blocks carry. Every member is an
                          accepted key, and a member's defaults apply wherever its key is
                          absent. Unknown keys are rejected: the field set is this toolset
                          version's complete member set.

                          - `type: optional BetaBrowserTypeConfig or null`

                            `type`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `close_tab: optional BetaBrowserCloseTabConfig or null`

                            `close_tab`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `double_click: optional BetaBrowserDoubleClickConfig or null`

                            `double_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `file_upload: optional BetaBrowserFileUploadConfig or null`

                            `file_upload`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `find: optional BetaBrowserFindConfig or null`

                            `find`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `form_input: optional BetaBrowserFormInputConfig or null`

                            `form_input`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `get_page_text: optional BetaBrowserGetPageTextConfig or null`

                            `get_page_text`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `hold_key: optional BetaBrowserHoldKeyConfig or null`

                            `hold_key`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `hover: optional BetaBrowserHoverConfig or null`

                            `hover`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `javascript_exec: optional BetaBrowserJavascriptExecConfig or null`

                            `javascript_exec`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `key: optional BetaBrowserKeyConfig or null`

                            `key`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_click: optional BetaBrowserLeftClickConfig or null`

                            `left_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_click_drag: optional BetaBrowserLeftClickDragConfig or null`

                            `left_click_drag`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_mouse_down: optional BetaBrowserLeftMouseDownConfig or null`

                            `left_mouse_down`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_mouse_up: optional BetaBrowserLeftMouseUpConfig or null`

                            `left_mouse_up`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `list_tabs: optional BetaBrowserListTabsConfig or null`

                            `list_tabs`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `middle_click: optional BetaBrowserMiddleClickConfig or null`

                            `middle_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `mouse_move: optional BetaBrowserMouseMoveConfig or null`

                            `mouse_move`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `navigate: optional BetaBrowserNavigateConfig or null`

                            `navigate`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `new_tab: optional BetaBrowserNewTabConfig or null`

                            `new_tab`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `read_console: optional BetaBrowserReadConsoleConfig or null`

                            `read_console`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `read_network: optional BetaBrowserReadNetworkConfig or null`

                            `read_network`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `read_page: optional BetaBrowserReadPageConfig or null`

                            `read_page`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `right_click: optional BetaBrowserRightClickConfig or null`

                            `right_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `screenshot: optional BetaBrowserScreenshotConfig or null`

                            `screenshot`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `scroll: optional BetaBrowserScrollConfig or null`

                            `scroll`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `scroll_to: optional BetaBrowserScrollToConfig or null`

                            `scroll_to`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `switch_tab: optional BetaBrowserSwitchTabConfig or null`

                            `switch_tab`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `triple_click: optional BetaBrowserTripleClickConfig or null`

                            `triple_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `wait: optional BetaBrowserWaitConfig or null`

                            `wait`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `zoom: optional BetaBrowserZoomConfig or null`

                            `zoom`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                      - `BetaToolComputerUse20241022 object`

                        - `type: "computer_20241022"`

                        - `display_height_px: number`

                          The height of the display in pixels.

                          minimum: 1

                        - `display_width_px: number`

                          The width of the display in pixels.

                          minimum: 1

                        - `name: "computer"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `display_number: optional number or null`

                          The X11 display number (e.g. 0, 1) for the display.

                          minimum: 0

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaMemoryTool20250818 object`

                        - `type: "memory_20250818"`

                        - `name: "memory"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolComputerUse20250124 object`

                        - `type: "computer_20250124"`

                        - `display_height_px: number`

                          The height of the display in pixels.

                          minimum: 1

                        - `display_width_px: number`

                          The width of the display in pixels.

                          minimum: 1

                        - `name: "computer"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `display_number: optional number or null`

                          The X11 display number (e.g. 0, 1) for the display.

                          minimum: 0

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolTextEditor20241022 object`

                        - `type: "text_editor_20241022"`

                        - `name: "str_replace_editor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolComputerUse20251124 object`

                        - `type: "computer_20251124"`

                        - `display_height_px: number`

                          The height of the display in pixels.

                          minimum: 1

                        - `display_width_px: number`

                          The width of the display in pixels.

                          minimum: 1

                        - `name: "computer"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `display_number: optional number or null`

                          The X11 display number (e.g. 0, 1) for the display.

                          minimum: 0

                        - `enable_zoom: optional boolean`

                          Whether to enable an action to take a zoomed-in screenshot of the screen.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaComputerToolset20260801 object`

                        The computer toolset: a single `tools[]` entry (carrying no
                        `name`) that declares the computer tool family. The model is
                        served the family's tool with any members disabled via `configs`
                        removed from its schema. Every member is enabled by default, zoom
                        included. The single-tool options `display_number` and
                        `enable_zoom` are not fields of a toolset entry — it carries only
                        `type`, `configs`, and `cache_control`; zoom is controlled
                        via `configs.zoom.enabled`.

                        - `type: "computer_toolset_20260801"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `configs: optional BetaComputerToolsetConfigs or null`

                          Per-member configuration for `computer_toolset_20260801`: one
                          optional field per member tool, keyed by the member name — the same
                          name the member's `tool_use` blocks carry. Every member is an
                          accepted key, and a member's defaults apply wherever its key is
                          absent. Unknown keys are rejected: the field set is this toolset
                          version's complete member set.

                          - `type: optional BetaComputerTypeConfig or null`

                            `type`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `cursor_position: optional BetaComputerCursorPositionConfig or null`

                            `cursor_position`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `double_click: optional BetaComputerDoubleClickConfig or null`

                            `double_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `hold_key: optional BetaComputerHoldKeyConfig or null`

                            `hold_key`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `key: optional BetaComputerKeyConfig or null`

                            `key`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_click: optional BetaComputerLeftClickConfig or null`

                            `left_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_click_drag: optional BetaComputerLeftClickDragConfig or null`

                            `left_click_drag`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_mouse_down: optional BetaComputerLeftMouseDownConfig or null`

                            `left_mouse_down`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `left_mouse_up: optional BetaComputerLeftMouseUpConfig or null`

                            `left_mouse_up`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `middle_click: optional BetaComputerMiddleClickConfig or null`

                            `middle_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `mouse_move: optional BetaComputerMouseMoveConfig or null`

                            `mouse_move`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `right_click: optional BetaComputerRightClickConfig or null`

                            `right_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `screenshot: optional BetaComputerScreenshotConfig or null`

                            `screenshot`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `scroll: optional BetaComputerScrollConfig or null`

                            `scroll`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `triple_click: optional BetaComputerTripleClickConfig or null`

                            `triple_click`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `wait: optional BetaComputerWaitConfig or null`

                            `wait`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                          - `zoom: optional BetaComputerZoomConfig or null`

                            `zoom`'s config overrides.

                            - `defer_loading: optional boolean or null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled: optional boolean or null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

                      - `BetaToolTextEditor20250124 object`

                        - `type: "text_editor_20250124"`

                        - `name: "str_replace_editor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolTextEditor20250429 object`

                        - `type: "text_editor_20250429"`

                        - `name: "str_replace_based_edit_tool"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolTextEditor20250728 object`

                        - `type: "text_editor_20250728"`

                        - `name: "str_replace_based_edit_tool"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `input_examples: optional array of map[unknown]`

                        - `max_characters: optional number or null`

                          Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

                          minimum: 1

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaWebSearchTool20250305 object`

                        - `type: "web_search_20250305"`

                        - `name: "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `blocked_domains: optional array of string or null`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `user_location: optional BetaUserLocation or null`

                          Parameters for the user's location. Used to provide more relevant search results.

                          - `type: "approximate"`

                          - `city: optional string or null`

                            The city of the user.

                            maxLength: 255, minLength: 1

                          - `country: optional string or null`

                            The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

                            maxLength: 2, minLength: 2

                          - `region: optional string or null`

                            The region of the user.

                            maxLength: 255, minLength: 1

                          - `timezone: optional string or null`

                            The [IANA timezone](https://nodatime.org/TimeZones) of the user.

                            maxLength: 255, minLength: 1

                      - `BetaWebFetchTool20250910 object`

                        - `type: "web_fetch_20250910"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          List of domains to allow fetching from

                        - `blocked_domains: optional array of string or null`

                          List of domains to block fetching from

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `citations: optional BetaCitationsConfigParam or null`

                          Citations configuration for fetched documents. Citations are disabled by default.

                          - `enabled: optional boolean`

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_content_tokens: optional number or null`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          exclusiveMinimum: 0

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `url_sources: optional BetaWebFetchURLSources or null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                          - `client_tool_results: optional BetaWebFetchURLSourceAll or BetaWebFetchURLSourceNone or BetaWebFetchURLSourceOnly or BetaWebFetchURLSourceExcept`

                            Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

                            - `BetaWebFetchURLSourceAll object`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                              - `type: "all"`

                            - `BetaWebFetchURLSourceNone object`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                              - `type: "none"`

                            - `BetaWebFetchURLSourceOnly object`

                              The tool filter variant under which only the named tools' results
                              contribute.

                              - `type: "only"`

                              - `tools: array of BetaWebFetchURLSourceToolReference`

                                - `type: "tool_reference"`

                                - `name: string`

                            - `BetaWebFetchURLSourceExcept object`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                              - `type: "except"`

                              - `tools: array of BetaWebFetchURLSourceToolReference`

                                - `type: "tool_reference"`

                                - `name: string`

                          - `server_tool_results: optional BetaWebFetchURLSourceAll or BetaWebFetchURLSourceNone or BetaWebFetchURLSourceOnly or BetaWebFetchURLSourceExcept`

                            Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

                            - `BetaWebFetchURLSourceAll object`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `BetaWebFetchURLSourceNone object`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                            - `BetaWebFetchURLSourceOnly object`

                              The tool filter variant under which only the named tools' results
                              contribute.

                            - `BetaWebFetchURLSourceExcept object`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                          - `user_input: optional BetaWebFetchURLSourceAll or BetaWebFetchURLSourceNone`

                            Whether URLs in user messages are fetchable: "all" or "none".

                            - `BetaWebFetchURLSourceAll object`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `BetaWebFetchURLSourceNone object`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                      - `BetaWebSearchTool20260209 object`

                        - `type: "web_search_20260209"`

                        - `name: "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `blocked_domains: optional array of string or null`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `user_location: optional BetaUserLocation or null`

                          Parameters for the user's location. Used to provide more relevant search results.

                      - `BetaWebFetchTool20260209 object`

                        - `type: "web_fetch_20260209"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          List of domains to allow fetching from

                        - `blocked_domains: optional array of string or null`

                          List of domains to block fetching from

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `citations: optional BetaCitationsConfigParam or null`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_content_tokens: optional number or null`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          exclusiveMinimum: 0

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `url_sources: optional BetaWebFetchURLSources or null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                      - `BetaWebFetchTool20260309 object`

                        Web fetch tool with use_cache parameter for bypassing cached content.

                        - `type: "web_fetch_20260309"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          List of domains to allow fetching from

                        - `blocked_domains: optional array of string or null`

                          List of domains to block fetching from

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `citations: optional BetaCitationsConfigParam or null`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_content_tokens: optional number or null`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          exclusiveMinimum: 0

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `url_sources: optional BetaWebFetchURLSources or null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                        - `use_cache: optional boolean`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `BetaWebSearchTool20260318 object`

                        - `type: "web_search_20260318"`

                        - `name: "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

                        - `blocked_domains: optional array of string or null`

                          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `response_inclusion: optional "full" or "excluded"`

                          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

                          - `"full"`

                          - `"excluded"`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `user_location: optional BetaUserLocation or null`

                          Parameters for the user's location. Used to provide more relevant search results.

                      - `BetaWebFetchTool20260318 object`

                        - `type: "web_fetch_20260318"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `allowed_domains: optional array of string or null`

                          List of domains to allow fetching from

                        - `blocked_domains: optional array of string or null`

                          List of domains to block fetching from

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `citations: optional BetaCitationsConfigParam or null`

                          Citations configuration for fetched documents. Citations are disabled by default.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_content_tokens: optional number or null`

                          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

                          exclusiveMinimum: 0

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `response_inclusion: optional "full" or "excluded"`

                          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

                          - `"full"`

                          - `"excluded"`

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                        - `url_sources: optional BetaWebFetchURLSources or null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                        - `use_cache: optional boolean`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `BetaAdvisorTool20260301 object`

                        - `type: "advisor_20260301"`

                        - `model: Model`

                          The model that will complete your prompt.

                          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                          - `"claude-fable-5-1" or "claude-opus-5-5" or "claude-mythos-5-1" or 15 more`

                            The model that will complete your prompt.

                            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                            - `"claude-fable-5-1"`

                              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                            - `"claude-opus-5-5"`

                              Powerful intelligence for coding, knowledge work, and long-running agents

                            - `"claude-mythos-5-1"`

                              Our most capable model for cybersecurity and biology research, available through trusted access programs

                            - `"claude-sonnet-5"`

                              High-performance model for coding and agents

                            - `"claude-fable-5"`

                              Next generation of intelligence for the hardest knowledge work and coding problems

                            - `"claude-mythos-5"`

                              Most capable model for cybersecurity and biology research

                            - `"claude-opus-5"`

                              Powerful intelligence for long-running agents and coding

                            - `"claude-opus-4-8"`

                              Powerful intelligence for long-running agents and coding

                            - `"claude-opus-4-7"`

                              Powerful intelligence for long-running agents and coding

                            - `"claude-mythos-preview"`

                              New class of intelligence, strongest in coding and cybersecurity

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

                        - `name: "advisor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `caching: optional BetaCacheControlEphemeral or null`

                          Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `max_tokens: optional number or null`

                          Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

                          minimum: 1024

                        - `max_uses: optional number or null`

                          Maximum number of times the tool can be used in the API request.

                          exclusiveMinimum: 0

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolSearchToolBm25_20251119 object`

                        - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

                          - `"tool_search_tool_bm25_20251119"`

                          - `"tool_search_tool_bm25"`

                        - `name: "tool_search_tool_bm25"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaToolSearchToolRegex20251119 object`

                        - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

                          - `"tool_search_tool_regex_20251119"`

                          - `"tool_search_tool_regex"`

                        - `name: "tool_search_tool_regex"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

                        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

                          - `"direct"`

                          - `"code_execution_20250825"`

                          - `"code_execution_20260120"`

                          - `"code_execution_20260521"`

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `defer_loading: optional boolean`

                          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                        - `strict: optional boolean`

                          When true, guarantees schema validation on tool names and inputs

                      - `BetaMCPToolset object`

                        Configuration for a group of tools from an MCP server.

                        Allows configuring enabled status and defer_loading for all tools
                        from an MCP server, with optional per-tool overrides.

                        - `type: "mcp_toolset"`

                        - `mcp_server_name: string`

                          Name of the MCP server to configure tools for

                          maxLength: 255, minLength: 1

                        - `cache_control: optional BetaCacheControlEphemeral or null`

                          Create a cache control breakpoint at this content block.

                        - `configs: optional map[BetaMCPToolConfig] or null`

                          Configuration overrides for specific tools, keyed by tool name

                          - `defer_loading: optional boolean`

                          - `enabled: optional boolean`

                        - `default_config: optional BetaMCPToolDefaultConfig`

                          Default configuration applied to all tools from this server

                          - `defer_loading: optional boolean`

                          - `enabled: optional boolean`

                        - `tools: optional array of BetaMCPToolParam or null`

                          The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

                          - `input_schema: map[unknown]`

                            The tool's input schema as the MCP server lists it, verbatim.

                          - `name: string`

                            The tool's name as the MCP server lists it (not prefixed with the server name).

                            minLength: 1

                          - `description: optional string or null`

                            The tool's description as the MCP server lists it.

              - `BetaResponseToolRemovalBlock object`

                An entry of a `compaction` block's `tool_changes`: a tool of the
                request's `tools` (or an MCP tool or toolset) that the compacted range
                withdrew. Send it back unchanged.

                - `type: "tool_removal"`

                  default: tool_removal

                - `tool: BetaResponseToolChangeToolReference or BetaResponseToolChangeMCPToolReference or BetaResponseToolChangeMCPToolsetReference`

                  A reference to the withdrawn `tools` entry, MCP tool or MCP toolset.

                  - `BetaResponseToolChangeToolReference object`

                    Reference to a single tool, by the name the model uses to call it, as
                    a `compaction` block's `tool_changes` entry reports it: a tool
                    declared in `tools` or defined by an earlier `tool_addition` block.
                    Send it back unchanged with the block.

                  - `BetaResponseToolChangeMCPToolReference object`

                    Reference to a single MCP tool, by its server and its name on that
                    server, as a `compaction` block's `tool_changes` entry reports it.
                    Send it back unchanged with the block.

                  - `BetaResponseToolChangeMCPToolsetReference object`

                    Reference to every tool in the named MCP server's toolset, as a
                    `compaction` block's `tool_changes` entry reports it. Send it back
                    unchanged with the block.

          - `BetaFallbackBlock object`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `type: "fallback"`

              default: fallback

            - `from: BetaFallbackInfo`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `model: Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `to: BetaFallbackInfo`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `trigger: BetaFallbackRefusalTrigger`

              What caused the `from` model to hand over at this hop.

              - `type: "refusal"`

                default: refusal

              - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

                The policy category that triggered a refusal.

                - `"cyber"`

                  The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

                - `"bio"`

                  The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

                - `"frontier_llm"`

                  The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

                - `"reasoning_extraction"`

                  The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

                - `"general_harms"`

                  The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `BetaMCPToolListingBlock object`

            The tool listing the server fetched from an MCP server while producing
            this response. Send the assistant message back unchanged, this block
            included, so later requests use this listing instead of asking the MCP
            server again.

            - `type: "mcp_tool_listing"`

              default: mcp_tool_listing

            - `mcp_server_name: string`

            - `tools: array of BetaMCPTool`

              - `input_schema: map[unknown]`

              - `name: string`

              - `description: optional string`

        - `context_management: BetaContextManagementResponse or null`

          Context management response.

          Information about context management strategies applied during the request.

          - `applied_edits: array of BetaClearToolUses20250919EditResponse or BetaClearThinking20251015EditResponse`

            List of context management edits that were applied.

            - `BetaClearToolUses20250919EditResponse object`

              - `type: "clear_tool_uses_20250919"`

                The type of context management edit applied.

                default: clear_tool_uses_20250919

              - `cleared_input_tokens: number`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `cleared_tool_uses: number`

                Number of tool uses that were cleared.

                minimum: 0

            - `BetaClearThinking20251015EditResponse object`

              - `type: "clear_thinking_20251015"`

                The type of context management edit applied.

                default: clear_thinking_20251015

              - `cleared_input_tokens: number`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `cleared_thinking_turns: number`

                Number of thinking turns that were cleared.

                minimum: 0

        - `diagnostics: BetaDiagnostics or null`

          Request-level diagnostics: why the prompt cache could not fully reuse
          the prefix of the request named by `diagnostics.previous_message_id`.

          - `cache_miss_reason: BetaCacheMissModelChanged or BetaCacheMissSystemChanged or BetaCacheMissToolsChanged or 3 more or null`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `BetaCacheMissModelChanged object`

              - `type: "model_changed"`

                default: model_changed

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `BetaCacheMissSystemChanged object`

              - `type: "system_changed"`

                default: system_changed

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `BetaCacheMissToolsChanged object`

              - `type: "tools_changed"`

                default: tools_changed

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `BetaCacheMissMessagesChanged object`

              - `type: "messages_changed"`

                default: messages_changed

              - `cache_missed_input_tokens: number`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `BetaCacheMissPreviousMessageNotFound object`

              - `type: "previous_message_not_found"`

                default: previous_message_not_found

            - `BetaCacheMissUnavailable object`

              - `type: "unavailable"`

                default: unavailable

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

          default: assistant

        - `stop_details: BetaRefusalStopDetails or null`

          Structured information about a refusal.

          - `type: "refusal"`

            default: refusal

          - `category: "cyber" or "bio" or "frontier_llm" or 2 more or null`

            The policy category that triggered a refusal.

            - `"cyber"`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `"bio"`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `"frontier_llm"`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `"reasoning_extraction"`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `"general_harms"`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `explanation: string or null`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `fallback_credit_token: string or null`

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

          - `fallback_has_prefill_claim: boolean or null`

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

          - `recommended_model: string or null`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

        - `stop_reason: BetaStopReason or null`

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

          - `"end_turn"`

          - `"max_tokens"`

          - `"stop_sequence"`

          - `"tool_use"`

          - `"pause_turn"`

          - `"compaction"`

          - `"refusal"`

          - `"model_context_window_exceeded"`

        - `stop_sequence: string or null`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `usage: BetaUsage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: BetaCacheCreation or null`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

              default: 0, minimum: 0

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

              default: 0, minimum: 0

          - `cache_creation_input_tokens: number or null`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `cache_read_input_tokens: number or null`

            The number of input tokens read from the cache.

            minimum: 0

          - `fallback_credit: BetaFallbackCreditUsage or null`

            Outcome of the `fallback_credit_token` presented on this request.

            - `status: BetaFallbackCreditRedeemed or BetaFallbackCreditNotApplied`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `BetaFallbackCreditRedeemed object`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `type: "redeemed"`

                  default: redeemed

              - `BetaFallbackCreditNotApplied object`

                No reprice was applied; `reason` says why.

                - `type: "not_applied"`

                  default: not_applied

                - `reason: "body_mismatch" or "continuation_excluded" or "continuation_only" or 9 more`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `"body_mismatch"`

                  - `"continuation_excluded"`

                  - `"continuation_only"`

                  - `"expired"`

                  - `"invalid_target_model"`

                  - `"not_enabled"`

                  - `"reprice_unavailable"`

                  - `"temporarily_unavailable"`

                  - `"variant_fields_present"`

                  - `"wrong_organization"`

                  - `"wrong_platform"`

                  - `"wrong_workspace"`

                - `remove_to_redeem: optional array of string or null`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `inference_geo: string or null`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

            minimum: 0

          - `iterations: BetaIterationsUsage or null`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `BetaMessageIterationUsage object`

              Token usage for a sampling iteration.

              - `type: "message"`

                Usage for a sampling iteration

                default: message

              - `cache_creation: BetaCacheCreation or null`

                Breakdown of cached tokens by TTL

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `model: Model or null`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

            - `BetaCompactionIterationUsage object`

              Token usage for a compaction iteration.

              - `type: "compaction"`

                Usage for a compaction iteration

                default: compaction

              - `cache_creation: BetaCacheCreation or null`

                Breakdown of cached tokens by TTL

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

            - `BetaAdvisorMessageIterationUsage object`

              Token usage for an advisor sub-inference iteration.

              - `type: "advisor_message"`

                Usage for an advisor sub-inference iteration

                default: advisor_message

              - `cache_creation: BetaCacheCreation or null`

                Breakdown of cached tokens by TTL

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `model: Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

            - `BetaFallbackMessageIterationUsage object`

              Token usage for the fallback-model attempt of a server-side fallback request.

              The terminal entry of a fallback-served turn: when a fallback hop's
              output is the returned message, the entry for the iteration that
              completed it carries this type in place of `message`. A declined hop
              and the serving hop's earlier tool-loop iterations produce `message`
              entries. Whether a fallback model served the response is signalled by
              the presence of this entry in `usage.iterations`.

              - `type: "fallback_message"`

                Usage for the fallback-model attempt that served the response

                default: fallback_message

              - `cache_creation: BetaCacheCreation or null`

                Breakdown of cached tokens by TTL

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                default: 0, minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                default: 0, minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `model: Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

          - `output_tokens: number`

            The number of output tokens which were used.

            minimum: 0

          - `output_tokens_details: BetaOutputTokensDetails or null`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `thinking_tokens: number`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              default: 0, minimum: 0

          - `server_tool_use: BetaServerToolUsage or null`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

              default: 0, minimum: 0

            - `web_search_requests: number`

              The number of web search tool requests.

              default: 0, minimum: 0

          - `service_tier: "standard" or "priority" or "batch" or null`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

          - `speed: "standard" or "fast" or null`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `input_transformations: optional array of BetaInputTransformation or null`

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

          - `BetaThinkingDroppedInputTransformation object`

            - `type: "thinking_dropped"`

              Always `thinking_dropped` for this entry type.

              default: thinking_dropped

            - `path: string`

              Where the removed block was in your request, as `messages.{i}.content.{j}`:
              `i` indexes the `messages` array you sent and `j` that message's `content`
              array — the same form error messages use.

            - `reason: "model_binding_mismatch" or "prefix_binding_mismatch" or "organization_binding_mismatch" or "end_user_binding_mismatch"`

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

              - `"model_binding_mismatch"`

              - `"prefix_binding_mismatch"`

              - `"organization_binding_mismatch"`

              - `"end_user_binding_mismatch"`

          - `BetaThinkingMismatchAllowedInputTransformation object`

            - `type: "thinking_mismatch_allowed"`

              Always `thinking_mismatch_allowed` for this entry type.

              default: thinking_mismatch_allowed

            - `path: string`

              Where the block is in your request, as `messages.{i}.content.{j}`:
              `i` indexes the `messages` array you sent and `j` that message's `content`
              array — the same form error messages use.

            - `reason: "model_binding_mismatch" or "prefix_binding_mismatch" or "organization_binding_mismatch" or "end_user_binding_mismatch"`

              Which binding check the block failed; the block was shown to the model all
              the same. Always `prefix_binding_mismatch` today — the conversation before
              the block differs from the conversation it was created in, or the block
              carries no record of one on a model that requires it. Were the check
              enforced for this request, the block would have been removed or the request
              rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also
              takes the rest of that turn's consecutive thinking blocks, whereas here each
              block is checked on its own, so `thinking_mismatch_allowed` entries are a
              lower bound on what enforcement would remove.

              - `"model_binding_mismatch"`

              - `"prefix_binding_mismatch"`

              - `"organization_binding_mismatch"`

              - `"end_user_binding_mismatch"`

    - `BetaMessageBatchErroredResult object`

      - `type: "errored"`

        default: errored

      - `error: BetaErrorResponse`

        - `type: "error"`

          default: error

        - `error: BetaError`

          - `BetaInvalidRequestError object`

            - `type: "invalid_request_error"`

              default: invalid_request_error

            - `message: string`

              default: Invalid request

          - `BetaAuthenticationError object`

            - `type: "authentication_error"`

              default: authentication_error

            - `message: string`

              default: Authentication error

          - `BetaBillingError object`

            - `type: "billing_error"`

              default: billing_error

            - `message: string`

              default: Billing error

          - `BetaPermissionError object`

            - `type: "permission_error"`

              default: permission_error

            - `message: string`

              default: Permission denied

          - `BetaNotFoundError object`

            - `type: "not_found_error"`

              default: not_found_error

            - `message: string`

              default: Not found

          - `BetaRateLimitError object`

            - `type: "rate_limit_error"`

              default: rate_limit_error

            - `message: string`

              default: Rate limited

          - `BetaGatewayTimeoutError object`

            - `type: "timeout_error"`

              default: timeout_error

            - `message: string`

              default: Request timeout

          - `BetaAPIError object`

            - `type: "api_error"`

              default: api_error

            - `message: string`

              default: Internal server error

          - `BetaOverloadedError object`

            - `type: "overloaded_error"`

              default: overloaded_error

            - `message: string`

              default: Overloaded

        - `request_id: string or null`

    - `BetaMessageBatchCanceledResult object`

      - `type: "canceled"`

        default: canceled

    - `BetaMessageBatchExpiredResult object`

      - `type: "expired"`

        default: expired

## Example

```bash
curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID/results \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```
