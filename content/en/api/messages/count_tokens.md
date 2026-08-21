---
title: Count tokens in a Message
url: https://platform.claude.com/docs/en/api/messages/count_tokens
---

## Count tokens in a Message

**post** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Header Parameters

- `"anthropic-user-profile-id": optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

### Body Parameters

- `messages: array of MessageParam`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

  Example with a single `user` message:

  ```json
  [{"role": "user", "content": "Hello, Claude"}]
  ```

  Example with multiple conversational turns:

  ```json
  [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
  ]
  ```

  Example with a partially-filled response from Claude:

  ```json
  [
    {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
    {"role": "assistant", "content": "The best answer is ("},
  ]
  ```

  Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

  ```json
  {"role": "user", "content": "Hello, Claude"}
  ```

  ```json
  {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
  ```

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

  - `content: string or array of ContentBlockParam`

    - `string`

    - `array of ContentBlockParam`

      - `TextBlockParam object { text, type, cache_control, citations }`

        - `text: string`

        - `type: "text"`

          - `"text"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

            - `"ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of TextCitationParam or null`

          - `CitationCharLocationParam object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string or null`

            - `end_char_index: number`

            - `start_char_index: number`

            - `type: "char_location"`

              - `"char_location"`

          - `CitationPageLocationParam object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

            - `document_index: number`

            - `document_title: string or null`

            - `end_page_number: number`

            - `start_page_number: number`

            - `type: "page_location"`

              - `"page_location"`

          - `CitationContentBlockLocationParam object { cited_text, document_index, document_title, 3 more }`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `document_index: number`

            - `document_title: string or null`

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

            - `type: "content_block_location"`

              - `"content_block_location"`

          - `CitationWebSearchResultLocationParam object { cited_text, encrypted_index, title, 2 more }`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string or null`

            - `type: "web_search_result_location"`

              - `"web_search_result_location"`

            - `url: string`

          - `CitationSearchResultLocationParam object { cited_text, end_block_index, search_result_index, 4 more }`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `search_result_index: number`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

            - `source: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

            - `title: string or null`

            - `type: "search_result_location"`

              - `"search_result_location"`

      - `ImageBlockParam object { source, type, cache_control, transformations }`

        - `source: Base64ImageSource or URLImageSource or FileImageSource`

          - `Base64ImageSource object { data, media_type, type }`

            - `data: string`

            - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

              - `"base64"`

          - `URLImageSource object { type, url }`

            - `type: "url"`

              - `"url"`

            - `url: string`

          - `FileImageSource object { file_id, type }`

            - `file_id: string`

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `transformations: optional ImageTransformationsParam or null`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `oversized_image: optional "downsize" or "error"`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `"downsize"`

            - `"error"`

      - `DocumentBlockParam object { source, type, cache_control, 3 more }`

        - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

          - `Base64PDFSource object { data, media_type, type }`

            - `data: string`

            - `media_type: "application/pdf"`

              - `"application/pdf"`

            - `type: "base64"`

              - `"base64"`

          - `PlainTextSource object { data, media_type, type }`

            - `data: string`

            - `media_type: "text/plain"`

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `ContentBlockSource object { content, type }`

            - `content: string or array of ContentBlockSourceContent`

              - `string`

              - `ContentBlockSourceContent = array of ContentBlockSourceContent`

                - `TextBlockParam object { text, type, cache_control, citations }`

                - `ImageBlockParam object { source, type, cache_control, transformations }`

            - `type: "content"`

              - `"content"`

          - `URLPDFSource object { type, url }`

            - `type: "url"`

              - `"url"`

            - `url: string`

          - `FileDocumentSource object { file_id, type }`

            - `file_id: string`

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `citations: optional CitationsConfigParam or null`

          - `enabled: optional boolean`

        - `context: optional string or null`

        - `title: optional string or null`

      - `SearchResultBlockParam object { content, source, title, 3 more }`

        - `content: array of TextBlockParam`

          - `text: string`

          - `type: "text"`

          - `cache_control: optional CacheControlEphemeral or null`

            Create a cache control breakpoint at this content block.

          - `citations: optional array of TextCitationParam or null`

        - `source: string`

        - `title: string`

        - `type: "search_result"`

          - `"search_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `citations: optional CitationsConfigParam`

      - `ThinkingBlockParam object { signature, thinking, type }`

        - `signature: string`

          The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

          Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

        - `thinking: string`

          The `thinking` text of this block as returned by the API.

        - `type: "thinking"`

          - `"thinking"`

      - `RedactedThinkingBlockParam object { data, type }`

        - `data: string`

          The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

        - `type: "redacted_thinking"`

          - `"redacted_thinking"`

      - `ToolUseBlockParam object { id, input, name, 4 more }`

        - `id: string`

        - `input: map[unknown]`

        - `name: string`

        - `type: "tool_use"`

          - `"tool_use"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller object { type }`

            Tool invocation directly from the model.

            - `type: "direct"`

              - `"direct"`

          - `ServerToolCaller object { tool_id, type }`

            Tool invocation generated by a server-side tool.

            - `tool_id: string`

            - `type: "code_execution_20250825"`

              - `"code_execution_20250825"`

          - `ServerToolCaller20260120 object { tool_id, type }`

            - `tool_id: string`

            - `type: "code_execution_20260120"`

              - `"code_execution_20260120"`

        - `toolset_name: optional string or null`

          For a toolset member tool_use, the toolset family this member belongs to.

      - `ToolResultBlockParam object { tool_use_id, type, cache_control, 3 more }`

        - `tool_use_id: string`

        - `type: "tool_result"`

          - `"tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `content: optional string or array of TextBlockParam or ImageBlockParam or SearchResultBlockParam or 3 more`

          - `string`

          - `array of TextBlockParam or ImageBlockParam or SearchResultBlockParam or 3 more`

            - `TextBlockParam object { text, type, cache_control, citations }`

            - `ImageBlockParam object { source, type, cache_control, transformations }`

            - `SearchResultBlockParam object { content, source, title, 3 more }`

            - `DocumentBlockParam object { source, type, cache_control, 3 more }`

            - `ToolReferenceBlockParam object { tool_name, type, cache_control }`

              Tool reference block that can be included in tool_result content.

              - `tool_name: string`

              - `type: "tool_reference"`

                - `"tool_reference"`

              - `cache_control: optional CacheControlEphemeral or null`

                Create a cache control breakpoint at this content block.

            - `BrowserStateBlockParam object { tabs, type, cache_control, state_changes }`

              The caller's browser state after a browser toolset member call —
              the full inventory of open tabs, which tab is active, and any side
              effects (tabs opened, download state changes) the call produced.

              At most one per `tool_result`, only on a non-error result answering a
              browser toolset member `tool_use`. The server renders the
              model-visible text from it; the model never sees the raw fields.

              - `tabs: array of BrowserStateTabEntry`

                All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                - `tab_id: string`

                  The caller-assigned identifier for this tab, unique within the inventory.

                - `title: string`

                  The title of the page the tab is showing. May be empty.

                - `url: string`

                  The URL of the page the tab is showing. May be empty.

                - `active: optional boolean`

                  Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

              - `type: "browser_state"`

                - `"browser_state"`

              - `cache_control: optional CacheControlEphemeral or null`

                Create a cache control breakpoint at this content block.

              - `state_changes: optional array of BrowserStateChange or null`

                Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                - `BrowserStateChangeTabOpened object { tab_id, type }`

                  A tab this call's execution opened that remains open at its end —
                  the creation delta of the `tabs` inventory, not an event log.

                  Carries only the `tab_id`; the tab's `title` and `url` live on its
                  `tabs` entry, which must include the same `tab_id`. A tab opened
                  during a failed call gets no deferred `tab_opened`; it simply appears
                  in the next result's `tabs` inventory.

                  - `tab_id: string`

                    The `tab_id` of the opened tab, present in `tabs`.

                  - `type: "tab_opened"`

                    - `"tab_opened"`

                - `BrowserStateChangeDownloadStarted object { download_id, type, url }`

                  A file download that started during this call.

                  - `download_id: string`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                  - `type: "download_started"`

                    - `"download_started"`

                  - `url: string`

                    The final post-redirect URL the download was served from.

                - `BrowserStateChangeDownloadCompleted object { download_id, type, url, 2 more }`

                  A file download that finished during this call, reported with the
                  same `download_id` as its `download_started` — or without a prior
                  `download_started`, when the download finished during the call that
                  started it (at most one state change per `download_id` per result).

                  - `download_id: string`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                  - `type: "download_completed"`

                    - `"download_completed"`

                  - `url: string`

                    The final post-redirect URL the download was served from.

                  - `path: optional string or null`

                    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                  - `size_bytes: optional number or null`

                    The completed download's size.

                - `BrowserStateChangeDownloadFailed object { download_id, type, url, error }`

                  A file download that failed — or was cancelled — during this call.

                  - `download_id: string`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                  - `type: "download_failed"`

                    - `"download_failed"`

                  - `url: string`

                    The final post-redirect URL the download was served from.

                  - `error: optional string or null`

                    The failure or cancellation detail, when known.

        - `is_error: optional boolean`

        - `toolset_name: optional string or null`

          For a toolset member tool_result, the toolset family of the paired tool_use.

      - `ServerToolUseBlockParam object { id, input, name, 3 more }`

        - `id: string`

        - `input: map[unknown]`

        - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

        - `type: "server_tool_use"`

          - `"server_tool_use"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller object { type }`

            Tool invocation directly from the model.

          - `ServerToolCaller object { tool_id, type }`

            Tool invocation generated by a server-side tool.

          - `ServerToolCaller20260120 object { tool_id, type }`

      - `WebSearchToolResultBlockParam object { content, tool_use_id, type, 2 more }`

        - `content: WebSearchToolResultBlockParamContent`

          - `WebSearchToolResultBlockItem = array of WebSearchResultBlockParam`

            - `encrypted_content: string`

            - `title: string`

            - `type: "web_search_result"`

              - `"web_search_result"`

            - `url: string`

            - `page_age: optional string or null`

          - `WebSearchToolRequestError object { error_code, type }`

            - `error_code: WebSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

            - `type: "web_search_tool_result_error"`

              - `"web_search_tool_result_error"`

        - `tool_use_id: string`

        - `type: "web_search_tool_result"`

          - `"web_search_tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller object { type }`

            Tool invocation directly from the model.

          - `ServerToolCaller object { tool_id, type }`

            Tool invocation generated by a server-side tool.

          - `ServerToolCaller20260120 object { tool_id, type }`

      - `WebFetchToolResultBlockParam object { content, tool_use_id, type, 2 more }`

        - `content: WebFetchToolResultErrorBlockParam or WebFetchBlockParam`

          - `WebFetchToolResultErrorBlockParam object { error_code, type }`

            - `error_code: WebFetchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_in_prior_context"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

            - `type: "web_fetch_tool_result_error"`

              - `"web_fetch_tool_result_error"`

          - `WebFetchBlockParam object { content, type, url, retrieved_at }`

            - `content: DocumentBlockParam`

            - `type: "web_fetch_result"`

              - `"web_fetch_result"`

            - `url: string`

              Fetched content URL

            - `retrieved_at: optional string or null`

              ISO 8601 timestamp when the content was retrieved

        - `tool_use_id: string`

        - `type: "web_fetch_tool_result"`

          - `"web_fetch_tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `DirectCaller object { type }`

            Tool invocation directly from the model.

          - `ServerToolCaller object { tool_id, type }`

            Tool invocation generated by a server-side tool.

          - `ServerToolCaller20260120 object { tool_id, type }`

      - `CodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }`

        - `content: CodeExecutionToolResultBlockParamContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `CodeExecutionToolResultErrorParam object { error_code, type }`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "code_execution_tool_result_error"`

              - `"code_execution_tool_result_error"`

          - `CodeExecutionResultBlockParam object { content, return_code, stderr, 2 more }`

            - `content: array of CodeExecutionOutputBlockParam`

              - `file_id: string`

              - `type: "code_execution_output"`

                - `"code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "code_execution_result"`

              - `"code_execution_result"`

          - `EncryptedCodeExecutionResultBlockParam object { content, encrypted_stdout, return_code, 2 more }`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: array of CodeExecutionOutputBlockParam`

              - `file_id: string`

              - `type: "code_execution_output"`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

            - `type: "encrypted_code_execution_result"`

              - `"encrypted_code_execution_result"`

        - `tool_use_id: string`

        - `type: "code_execution_tool_result"`

          - `"code_execution_tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

      - `BashCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }`

        - `content: BashCodeExecutionToolResultErrorParam or BashCodeExecutionResultBlockParam`

          - `BashCodeExecutionToolResultErrorParam object { error_code, type }`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

            - `type: "bash_code_execution_tool_result_error"`

              - `"bash_code_execution_tool_result_error"`

          - `BashCodeExecutionResultBlockParam object { content, return_code, stderr, 2 more }`

            - `content: array of BashCodeExecutionOutputBlockParam`

              - `file_id: string`

              - `type: "bash_code_execution_output"`

                - `"bash_code_execution_output"`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

            - `type: "bash_code_execution_result"`

              - `"bash_code_execution_result"`

        - `tool_use_id: string`

        - `type: "bash_code_execution_tool_result"`

          - `"bash_code_execution_tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

      - `TextEditorCodeExecutionToolResultBlockParam object { content, tool_use_id, type, cache_control }`

        - `content: TextEditorCodeExecutionToolResultErrorParam or TextEditorCodeExecutionViewResultBlockParam or TextEditorCodeExecutionCreateResultBlockParam or TextEditorCodeExecutionStrReplaceResultBlockParam`

          - `TextEditorCodeExecutionToolResultErrorParam object { error_code, type, error_message }`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `type: "text_editor_code_execution_tool_result_error"`

              - `"text_editor_code_execution_tool_result_error"`

            - `error_message: optional string or null`

          - `TextEditorCodeExecutionViewResultBlockParam object { content, file_type, type, 3 more }`

            - `content: string`

            - `file_type: "text" or "image" or "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `type: "text_editor_code_execution_view_result"`

              - `"text_editor_code_execution_view_result"`

            - `num_lines: optional number or null`

            - `start_line: optional number or null`

            - `total_lines: optional number or null`

          - `TextEditorCodeExecutionCreateResultBlockParam object { is_file_update, type }`

            - `is_file_update: boolean`

            - `type: "text_editor_code_execution_create_result"`

              - `"text_editor_code_execution_create_result"`

          - `TextEditorCodeExecutionStrReplaceResultBlockParam object { type, lines, new_lines, 3 more }`

            - `type: "text_editor_code_execution_str_replace_result"`

              - `"text_editor_code_execution_str_replace_result"`

            - `lines: optional array of string or null`

            - `new_lines: optional number or null`

            - `new_start: optional number or null`

            - `old_lines: optional number or null`

            - `old_start: optional number or null`

        - `tool_use_id: string`

        - `type: "text_editor_code_execution_tool_result"`

          - `"text_editor_code_execution_tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

      - `ToolSearchToolResultBlockParam object { content, tool_use_id, type, cache_control }`

        - `content: ToolSearchToolResultErrorParam or ToolSearchToolSearchResultBlockParam`

          - `ToolSearchToolResultErrorParam object { error_code, type, error_message }`

            - `error_code: ToolSearchToolResultErrorCode`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `type: "tool_search_tool_result_error"`

              - `"tool_search_tool_result_error"`

            - `error_message: optional string or null`

          - `ToolSearchToolSearchResultBlockParam object { tool_references, type }`

            - `tool_references: array of ToolReferenceBlockParam`

              - `tool_name: string`

              - `type: "tool_reference"`

              - `cache_control: optional CacheControlEphemeral or null`

                Create a cache control breakpoint at this content block.

            - `type: "tool_search_tool_search_result"`

              - `"tool_search_tool_search_result"`

        - `tool_use_id: string`

        - `type: "tool_search_tool_result"`

          - `"tool_search_tool_result"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

      - `ContainerUploadBlockParam object { file_id, type, cache_control }`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `file_id: string`

        - `type: "container_upload"`

          - `"container_upload"`

        - `cache_control: optional CacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

  - `role: "user" or "assistant" or "system"`

    - `"user"`

    - `"assistant"`

    - `"system"`

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

- `cache_control: optional CacheControlEphemeral or null`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `output_config: optional OutputConfig`

  Configuration options for the model's output, such as the output format.

  - `effort: optional "low" or "medium" or "high" or 2 more or null`

    All possible effort levels.

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

    - `"max"`

  - `format: optional JSONOutputFormat or null`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `schema: map[unknown]`

      The JSON schema of the format

    - `type: "json_schema"`

      - `"json_schema"`

- `system: optional string or array of TextBlockParam`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

  - `string`

  - `array of TextBlockParam`

    - `text: string`

    - `type: "text"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `citations: optional array of TextCitationParam or null`

- `thinking: optional ThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `ThinkingConfigEnabled object { budget_tokens, type, display }`

    - `budget_tokens: number`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `type: "enabled"`

      - `"enabled"`

    - `display: optional "summarized" or "omitted" or null`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `"summarized"`

      - `"omitted"`

  - `ThinkingConfigDisabled object { type }`

    - `type: "disabled"`

      - `"disabled"`

  - `ThinkingConfigAdaptive object { type, display }`

    - `type: "adaptive"`

      - `"adaptive"`

    - `display: optional "summarized" or "omitted" or null`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `"summarized"`

      - `"omitted"`

- `tool_choice: optional ToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `ToolChoiceAuto object { type, disable_parallel_tool_use }`

    The model will automatically decide whether to use tools.

    - `type: "auto"`

      - `"auto"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `ToolChoiceAny object { type, disable_parallel_tool_use }`

    The model will use any available tools.

    - `type: "any"`

      - `"any"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceTool object { name, type, disable_parallel_tool_use }`

    The model will use the specified tool with `tool_choice.name`.

    - `name: string`

      The name of the tool to use.

    - `type: "tool"`

      - `"tool"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceNone object { type }`

    The model will not be allowed to use tools.

    - `type: "none"`

      - `"none"`

- `tools: optional array of MessageCountTokensTool`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

  Each tool definition includes:

  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

  For example, if you defined `tools` as:

  ```json
  [
    {
      "name": "get_stock_price",
      "description": "Get the current stock price for a given ticker symbol.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
  ]
  ```

  And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

  ```json
  [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "get_stock_price",
      "input": { "ticker": "^GSPC" }
    }
  ]
  ```

  You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

  ```json
  [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "content": "259.75 USD"
    }
  ]
  ```

  Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

  See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

  - `Tool object { input_schema, name, allowed_callers, 7 more }`

    - `input_schema: object { type, properties, required }`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: "object"`

        - `"object"`

      - `properties: optional map[unknown] or null`

      - `required: optional array of string or null`

    - `name: string`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

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

    - `type: optional "custom" or null`

      - `"custom"`

  - `ToolBash20250124 object { name, type, allowed_callers, 4 more }`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"bash"`

    - `type: "bash_20250124"`

      - `"bash_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522 object { name, type, allowed_callers, 3 more }`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20250522"`

      - `"code_execution_20250522"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825 object { name, type, allowed_callers, 3 more }`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20250825"`

      - `"code_execution_20250825"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120 object { name, type, allowed_callers, 3 more }`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20260120"`

      - `"code_execution_20260120"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260521 object { name, type, allowed_callers, 3 more }`

    Code execution tool with REPL state persistence.

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"code_execution"`

    - `type: "code_execution_20260521"`

      - `"code_execution_20260521"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `BrowserToolset20260801 object { type, allowed_callers, cache_control, configs }`

    The browser toolset: a single `tools[]` entry (carrying no
    `name`) that declares the browser tool family. The model is served
    the family's tool with any members disabled via `configs` removed
    from its schema.

    - `type: "browser_toolset_20260801"`

      - `"browser_toolset_20260801"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `configs: optional BrowserToolsetConfigs or null`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `close_tab: optional BrowserCloseTabConfig or null`

        `close_tab`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: optional BrowserDoubleClickConfig or null`

        `double_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `file_upload: optional BrowserFileUploadConfig or null`

        `file_upload`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `find: optional BrowserFindConfig or null`

        `find`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `form_input: optional BrowserFormInputConfig or null`

        `form_input`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `get_page_text: optional BrowserGetPageTextConfig or null`

        `get_page_text`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: optional BrowserHoldKeyConfig or null`

        `hold_key`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hover: optional BrowserHoverConfig or null`

        `hover`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `javascript_exec: optional BrowserJavascriptExecConfig or null`

        `javascript_exec`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: optional BrowserKeyConfig or null`

        `key`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: optional BrowserLeftClickConfig or null`

        `left_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: optional BrowserLeftClickDragConfig or null`

        `left_click_drag`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: optional BrowserLeftMouseDownConfig or null`

        `left_mouse_down`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: optional BrowserLeftMouseUpConfig or null`

        `left_mouse_up`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `list_tabs: optional BrowserListTabsConfig or null`

        `list_tabs`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: optional BrowserMiddleClickConfig or null`

        `middle_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: optional BrowserMouseMoveConfig or null`

        `mouse_move`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `navigate: optional BrowserNavigateConfig or null`

        `navigate`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `new_tab: optional BrowserNewTabConfig or null`

        `new_tab`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_console: optional BrowserReadConsoleConfig or null`

        `read_console`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_network: optional BrowserReadNetworkConfig or null`

        `read_network`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_page: optional BrowserReadPageConfig or null`

        `read_page`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: optional BrowserRightClickConfig or null`

        `right_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: optional BrowserScreenshotConfig or null`

        `screenshot`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: optional BrowserScrollConfig or null`

        `scroll`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll_to: optional BrowserScrollToConfig or null`

        `scroll_to`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `switch_tab: optional BrowserSwitchTabConfig or null`

        `switch_tab`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: optional BrowserTripleClickConfig or null`

        `triple_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: optional BrowserTypeConfig or null`

        `type`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: optional BrowserWaitConfig or null`

        `wait`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: optional BrowserZoomConfig or null`

        `zoom`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `MemoryTool20250818 object { name, type, allowed_callers, 4 more }`

    - `name: "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"memory"`

    - `type: "memory_20250818"`

      - `"memory_20250818"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ComputerToolset20260801 object { type, allowed_callers, cache_control, configs }`

    The computer toolset: a single `tools[]` entry (carrying no
    `name`) that declares the computer tool family. The model is
    served the family's tool with any members disabled via `configs`
    removed from its schema. Every member is enabled by default, zoom
    included. The single-tool options `display_number` and
    `enable_zoom` are not fields of a toolset entry — it carries only
    `type`, `configs`, and `cache_control`; zoom is controlled
    via `configs.zoom.enabled`.

    - `type: "computer_toolset_20260801"`

      - `"computer_toolset_20260801"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `configs: optional ComputerToolsetConfigs or null`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `cursor_position: optional ComputerCursorPositionConfig or null`

        `cursor_position`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: optional ComputerDoubleClickConfig or null`

        `double_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: optional ComputerHoldKeyConfig or null`

        `hold_key`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: optional ComputerKeyConfig or null`

        `key`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: optional ComputerLeftClickConfig or null`

        `left_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: optional ComputerLeftClickDragConfig or null`

        `left_click_drag`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: optional ComputerLeftMouseDownConfig or null`

        `left_mouse_down`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: optional ComputerLeftMouseUpConfig or null`

        `left_mouse_up`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: optional ComputerMiddleClickConfig or null`

        `middle_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: optional ComputerMouseMoveConfig or null`

        `mouse_move`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: optional ComputerRightClickConfig or null`

        `right_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: optional ComputerScreenshotConfig or null`

        `screenshot`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: optional ComputerScrollConfig or null`

        `scroll`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: optional ComputerTripleClickConfig or null`

        `triple_click`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: optional ComputerTypeConfig or null`

        `type`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: optional ComputerWaitConfig or null`

        `wait`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: optional ComputerZoomConfig or null`

        `zoom`'s config overrides.

        - `defer_loading: optional boolean or null`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean or null`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `ToolTextEditor20250124 object { name, type, allowed_callers, 4 more }`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_editor"`

    - `type: "text_editor_20250124"`

      - `"text_editor_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429 object { name, type, allowed_callers, 4 more }`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: "text_editor_20250429"`

      - `"text_editor_20250429"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728 object { name, type, allowed_callers, 5 more }`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"str_replace_based_edit_tool"`

    - `type: "text_editor_20250728"`

      - `"text_editor_20250728"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `max_characters: optional number or null`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305 object { name, type, allowed_callers, 7 more }`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20250305"`

      - `"web_search_20250305"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string or null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional UserLocation or null`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

        - `"approximate"`

      - `city: optional string or null`

        The city of the user.

      - `country: optional string or null`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      - `region: optional string or null`

        The region of the user.

      - `timezone: optional string or null`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

  - `WebFetchTool20250910 object { name, type, allowed_callers, 8 more }`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20250910"`

      - `"web_fetch_20250910"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string or null`

      List of domains to block fetching from

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `citations: optional CitationsConfigParam or null`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number or null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209 object { name, type, allowed_callers, 7 more }`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20260209"`

      - `"web_search_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string or null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional UserLocation or null`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260209 object { name, type, allowed_callers, 8 more }`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20260209"`

      - `"web_fetch_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string or null`

      List of domains to block fetching from

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `citations: optional CitationsConfigParam or null`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number or null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `WebFetchTool20260309 object { name, type, allowed_callers, 9 more }`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20260309"`

      - `"web_fetch_20260309"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string or null`

      List of domains to block fetching from

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `citations: optional CitationsConfigParam or null`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number or null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `WebSearchTool20260318 object { name, type, allowed_callers, 8 more }`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_search"`

    - `type: "web_search_20260318"`

      - `"web_search_20260318"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string or null`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `response_inclusion: optional "full" or "excluded"`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `"full"`

      - `"excluded"`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional UserLocation or null`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260318 object { name, type, allowed_callers, 10 more }`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"web_fetch"`

    - `type: "web_fetch_20260318"`

      - `"web_fetch_20260318"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string or null`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string or null`

      List of domains to block fetching from

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `citations: optional CitationsConfigParam or null`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number or null`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `max_uses: optional number or null`

      Maximum number of times the tool can be used in the API request.

    - `response_inclusion: optional "full" or "excluded"`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `"full"`

      - `"excluded"`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `ToolSearchToolBm25_20251119 object { name, type, allowed_callers, 3 more }`

    - `name: "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_bm25"`

    - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119 object { name, type, allowed_callers, 3 more }`

    - `name: "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      - `"tool_search_tool_regex"`

    - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional CacheControlEphemeral or null`

      Create a cache control breakpoint at this content block.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

### Returns

- `MessageTokensCount object { input_tokens }`

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```http
curl https://api.anthropic.com/v1/messages/count_tokens \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "messages": [
            {
              "content": "Hello, world",
              "role": "user"
            }
          ],
          "model": "claude-opus-5",
          "system": [
            {
              "text": "Today'\''s date is 2024-06-01.",
              "type": "text"
            }
          ],
          "thinking": {
            "type": "adaptive"
          },
          "tools": [
            {
              "input_schema": {
                "type": "object",
                "properties": {
                  "location": "bar",
                  "unit": "bar"
                },
                "required": [
                  "location"
                ]
              },
              "name": "name"
            }
          ]
        }'
```

#### Response

```json
{
  "input_tokens": 2095
}
```
