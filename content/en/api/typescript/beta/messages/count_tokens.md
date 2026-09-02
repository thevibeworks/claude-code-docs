# Count tokens in a Message

`client.beta.messages.countTokens(params, options?): BetaMessageTokensCount`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

## Parameters

- `params: MessageCountTokensParams`

  - `messages: Array<BetaMessageParam>`

    Body param: Input messages.

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

    - `content: string | Array<BetaContentBlockParam>`

      - `string`

      - `Array<BetaContentBlockParam>`

        - `BetaTextBlockParam`

          - `text: string`

            minLength: 1

          - `type: "text"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl?: "5m" | "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `"5m"`

              - `"1h"`

          - `citations?: Array<BetaTextCitationParam> | null`

            - `BetaCitationCharLocationParam`

              - `cited_text: string`

              - `document_index: number`

                minimum: 0

              - `document_title: string | null`

                maxLength: 500, minLength: 1

              - `end_char_index: number`

              - `start_char_index: number`

                minimum: 0

              - `type: "char_location"`

            - `BetaCitationPageLocationParam`

              - `cited_text: string`

              - `document_index: number`

                minimum: 0

              - `document_title: string | null`

                maxLength: 500, minLength: 1

              - `end_page_number: number`

              - `start_page_number: number`

                minimum: 1

              - `type: "page_location"`

            - `BetaCitationContentBlockLocationParam`

              - `cited_text: string`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `document_index: number`

                minimum: 0

              - `document_title: string | null`

                maxLength: 500, minLength: 1

              - `end_block_index: number`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `start_block_index: number`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `type: "content_block_location"`

            - `BetaCitationWebSearchResultLocationParam`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string | null`

                maxLength: 512, minLength: 1

              - `type: "web_search_result_location"`

              - `url: string`

                minLength: 1

            - `BetaCitationSearchResultLocationParam`

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

              - `title: string | null`

              - `type: "search_result_location"`

        - `BetaImageBlockParam`

          - `source: BetaBase64ImageSource | BetaURLImageSource | BetaFileImageSource`

            - `BetaBase64ImageSource`

              - `data: string`

                format: byte

              - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                - `"image/jpeg"`

                - `"image/png"`

                - `"image/gif"`

                - `"image/webp"`

              - `type: "base64"`

            - `BetaURLImageSource`

              - `type: "url"`

              - `url: string`

            - `BetaFileImageSource`

              - `file_id: string`

              - `type: "file"`

          - `type: "image"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `transformations?: BetaImageTransformationsParam | null`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

            - `oversized_image?: "downsize" | "error"`

              What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

              - `"downsize"`

              - `"error"`

        - `BetaRequestDocumentBlock`

          - `source: BetaBase64PDFSource | BetaPlainTextSource | BetaContentBlockSource | 2 more`

            - `BetaBase64PDFSource`

              - `data: string`

                format: byte

              - `media_type: "application/pdf"`

              - `type: "base64"`

            - `BetaPlainTextSource`

              - `data: string`

              - `media_type: "text/plain"`

              - `type: "text"`

            - `BetaContentBlockSource`

              - `content: string | Array<BetaContentBlockSourceContent>`

                - `string`

                - `Array<BetaContentBlockSourceContent>`

                  - `BetaTextBlockParam`

                  - `BetaImageBlockParam`

              - `type: "content"`

            - `BetaURLPDFSource`

              - `type: "url"`

              - `url: string`

            - `BetaFileDocumentSource`

              - `file_id: string`

              - `type: "file"`

          - `type: "document"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `citations?: BetaCitationsConfigParam | null`

            - `enabled?: boolean`

          - `context?: string | null`

            minLength: 1

          - `title?: string | null`

            maxLength: 500, minLength: 1

        - `BetaSearchResultBlockParam`

          - `content: Array<BetaTextBlockParam>`

            - `text: string`

              minLength: 1

            - `type: "text"`

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `citations?: Array<BetaTextCitationParam> | null`

          - `source: string`

          - `title: string`

          - `type: "search_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `citations?: BetaCitationsConfigParam`

        - `BetaThinkingBlockParam`

          - `signature: string`

            The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

            Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

          - `thinking: string`

            The `thinking` text of this block as returned by the API.

          - `type: "thinking"`

        - `BetaRedactedThinkingBlockParam`

          - `data: string`

            The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `type: "redacted_thinking"`

        - `BetaToolUseBlockParam`

          - `id: string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `input: Record<string, unknown>`

          - `name: string`

            maxLength: 200, minLength: 1

          - `type: "tool_use"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `BetaDirectCaller`

              Tool invocation directly from the model.

              - `type: "direct"`

            - `BetaServerToolCaller`

              Tool invocation generated by a server-side tool.

              - `tool_id: string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `type: "code_execution_20250825"`

            - `BetaServerToolCaller20260120`

              - `tool_id: string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `type: "code_execution_20260120"`

          - `toolset_name?: string | null`

            For a toolset member tool_use, the toolset family this member belongs to.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `BetaToolResultBlockParam`

          - `tool_use_id: string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `type: "tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `content?: string | Array<BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | 3 more>`

            - `string`

            - `Array<BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | 3 more>`

              - `BetaTextBlockParam`

              - `BetaImageBlockParam`

              - `BetaSearchResultBlockParam`

              - `BetaRequestDocumentBlock`

              - `BetaToolReferenceBlockParam`

                Tool reference block that can be included in tool_result content.

                - `tool_name: string`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `type: "tool_reference"`

                - `cache_control?: BetaCacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

              - `BetaBrowserStateBlockParam`

                The caller's browser state after a browser toolset member call —
                the full inventory of open tabs, which tab is active, and any side
                effects (tabs opened, download state changes) the call produced.

                At most one per `tool_result`, only on a non-error result answering a
                browser toolset member `tool_use`. The server renders the
                model-visible text from it; the model never sees the raw fields.

                - `tabs: Array<BetaBrowserStateTabEntry>`

                  All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                  maxItems: 100

                  - `tab_id: string`

                    The caller-assigned identifier for this tab, unique within the inventory.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `title: string`

                    The title of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `url: string`

                    The URL of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `active?: boolean`

                    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                - `type: "browser_state"`

                - `cache_control?: BetaCacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                - `state_changes?: Array<BetaBrowserStateChange> | null`

                  Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                  maxItems: 200, minItems: 1

                  - `BetaBrowserStateChangeTabOpened`

                    A tab this call's execution opened that remains open at its end —
                    the creation delta of the `tabs` inventory, not an event log.

                    Carries only the `tab_id`; the tab's `title` and `url` live on its
                    `tabs` entry, which must include the same `tab_id`. A tab opened
                    during a failed call gets no deferred `tab_opened`; it simply appears
                    in the next result's `tabs` inventory.

                    - `tab_id: string`

                      The `tab_id` of the opened tab, present in `tabs`.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `type: "tab_opened"`

                  - `BetaBrowserStateChangeDownloadStarted`

                    A file download that started during this call.

                    - `download_id: string`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `type: "download_started"`

                    - `url: string`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `BetaBrowserStateChangeDownloadCompleted`

                    A file download that finished during this call, reported with the
                    same `download_id` as its `download_started` — or without a prior
                    `download_started`, when the download finished during the call that
                    started it (at most one state change per `download_id` per result).

                    - `download_id: string`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `type: "download_completed"`

                    - `url: string`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `path?: string | null`

                      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                    - `size_bytes?: number | null`

                      The completed download's size.

                      minimum: 0

                  - `BetaBrowserStateChangeDownloadFailed`

                    A file download that failed — or was cancelled — during this call.

                    - `download_id: string`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `type: "download_failed"`

                    - `url: string`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `error?: string | null`

                      The failure or cancellation detail, when known.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

          - `is_error?: boolean`

          - `toolset_name?: string | null`

            For a toolset member tool_result, the toolset family of the paired tool_use.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `BetaServerToolUseBlockParam`

          - `id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `input: Record<string, unknown>`

          - `name: "advisor" | "web_search" | "web_fetch" | 5 more`

            - `"advisor"`

            - `"web_search"`

            - `"web_fetch"`

            - `"code_execution"`

            - `"bash_code_execution"`

            - `"text_editor_code_execution"`

            - `"tool_search_tool_regex"`

            - `"tool_search_tool_bm25"`

          - `type: "server_tool_use"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `BetaDirectCaller`

              Tool invocation directly from the model.

            - `BetaServerToolCaller`

              Tool invocation generated by a server-side tool.

            - `BetaServerToolCaller20260120`

        - `BetaWebSearchToolResultBlockParam`

          - `content: BetaWebSearchToolResultBlockParamContent`

            - `Array<BetaWebSearchResultBlockParam>`

              - `encrypted_content: string`

              - `title: string`

              - `type: "web_search_result"`

              - `url: string`

              - `page_age?: string | null`

            - `BetaWebSearchToolRequestError`

              - `error_code: BetaWebSearchToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"max_uses_exceeded"`

                - `"too_many_requests"`

                - `"query_too_long"`

                - `"request_too_large"`

              - `type: "web_search_tool_result_error"`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "web_search_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `BetaDirectCaller`

              Tool invocation directly from the model.

            - `BetaServerToolCaller`

              Tool invocation generated by a server-side tool.

            - `BetaServerToolCaller20260120`

        - `BetaWebFetchToolResultBlockParam`

          - `content: BetaWebFetchToolResultErrorBlockParam | BetaWebFetchBlockParam`

            - `BetaWebFetchToolResultErrorBlockParam`

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

              - `type: "web_fetch_tool_result_error"`

            - `BetaWebFetchBlockParam`

              - `content: BetaRequestDocumentBlock`

              - `type: "web_fetch_result"`

              - `url: string`

                Fetched content URL

              - `retrieved_at?: string | null`

                ISO 8601 timestamp when the content was retrieved

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "web_fetch_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

            Tool invocation directly from the model.

            - `BetaDirectCaller`

              Tool invocation directly from the model.

            - `BetaServerToolCaller`

              Tool invocation generated by a server-side tool.

            - `BetaServerToolCaller20260120`

        - `BetaAdvisorToolResultBlockParam`

          - `content: BetaAdvisorToolResultErrorParam | BetaAdvisorResultBlockParam | BetaAdvisorRedactedResultBlockParam`

            - `BetaAdvisorToolResultErrorParam`

              - `error_code: "max_uses_exceeded" | "prompt_too_long" | "too_many_requests" | 4 more`

                - `"max_uses_exceeded"`

                - `"prompt_too_long"`

                - `"too_many_requests"`

                - `"overloaded"`

                - `"unavailable"`

                - `"execution_time_exceeded"`

                - `"model_not_found"`

              - `type: "advisor_tool_result_error"`

            - `BetaAdvisorResultBlockParam`

              - `text: string`

              - `type: "advisor_result"`

              - `stop_reason?: string | null`

            - `BetaAdvisorRedactedResultBlockParam`

              - `encrypted_content: string`

                Opaque blob produced by a prior response; must be round-tripped verbatim.

              - `type: "advisor_redacted_result"`

              - `stop_reason?: string | null`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "advisor_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaCodeExecutionToolResultBlockParam`

          - `content: BetaCodeExecutionToolResultBlockParamContent`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `BetaCodeExecutionToolResultErrorParam`

              - `error_code: BetaCodeExecutionToolResultErrorCode`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "code_execution_tool_result_error"`

            - `BetaCodeExecutionResultBlockParam`

              - `content: Array<BetaCodeExecutionOutputBlockParam>`

                - `file_id: string`

                - `type: "code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "code_execution_result"`

            - `BetaEncryptedCodeExecutionResultBlockParam`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `content: Array<BetaCodeExecutionOutputBlockParam>`

                - `file_id: string`

                - `type: "code_execution_output"`

              - `encrypted_stdout: string`

              - `return_code: number`

              - `stderr: string`

              - `type: "encrypted_code_execution_result"`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "code_execution_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaBashCodeExecutionToolResultBlockParam`

          - `content: BetaBashCodeExecutionToolResultErrorParam | BetaBashCodeExecutionResultBlockParam`

            - `BetaBashCodeExecutionToolResultErrorParam`

              - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"output_file_too_large"`

              - `type: "bash_code_execution_tool_result_error"`

            - `BetaBashCodeExecutionResultBlockParam`

              - `content: Array<BetaBashCodeExecutionOutputBlockParam>`

                - `file_id: string`

                - `type: "bash_code_execution_output"`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

              - `type: "bash_code_execution_result"`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "bash_code_execution_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaTextEditorCodeExecutionToolResultBlockParam`

          - `content: BetaTextEditorCodeExecutionToolResultErrorParam | BetaTextEditorCodeExecutionViewResultBlockParam | BetaTextEditorCodeExecutionCreateResultBlockParam | BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

            - `BetaTextEditorCodeExecutionToolResultErrorParam`

              - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"file_not_found"`

              - `type: "text_editor_code_execution_tool_result_error"`

              - `error_message?: string | null`

            - `BetaTextEditorCodeExecutionViewResultBlockParam`

              - `content: string`

              - `file_type: "text" | "image" | "pdf"`

                - `"text"`

                - `"image"`

                - `"pdf"`

              - `type: "text_editor_code_execution_view_result"`

              - `num_lines?: number | null`

              - `start_line?: number | null`

              - `total_lines?: number | null`

            - `BetaTextEditorCodeExecutionCreateResultBlockParam`

              - `is_file_update: boolean`

              - `type: "text_editor_code_execution_create_result"`

            - `BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

              - `type: "text_editor_code_execution_str_replace_result"`

              - `lines?: Array<string> | null`

              - `new_lines?: number | null`

              - `new_start?: number | null`

              - `old_lines?: number | null`

              - `old_start?: number | null`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "text_editor_code_execution_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaToolSearchToolResultBlockParam`

          - `content: BetaToolSearchToolResultErrorParam | BetaToolSearchToolSearchResultBlockParam`

            - `BetaToolSearchToolResultErrorParam`

              - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded"`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `type: "tool_search_tool_result_error"`

              - `error_message?: string | null`

            - `BetaToolSearchToolSearchResultBlockParam`

              - `tool_references: Array<BetaToolReferenceBlockParam>`

                - `tool_name: string`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `type: "tool_reference"`

                - `cache_control?: BetaCacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

              - `type: "tool_search_tool_search_result"`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "tool_search_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaMCPToolUseBlockParam`

          - `id: string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `input: Record<string, unknown>`

          - `name: string`

          - `server_name: string`

            The name of the MCP server

          - `type: "mcp_tool_use"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaRequestMCPToolResultBlockParam`

          - `tool_use_id: string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `type: "mcp_tool_result"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `content?: string | Array<BetaTextBlockParam>`

            - `string`

            - `Array<BetaTextBlockParam>`

              - `text: string`

                minLength: 1

              - `type: "text"`

              - `cache_control?: BetaCacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

              - `citations?: Array<BetaTextCitationParam> | null`

          - `is_error?: boolean`

        - `BetaContainerUploadBlockParam`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `file_id: string`

          - `type: "container_upload"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaCompactionBlockParam`

          A compaction block containing summary of previous context.

          Users should round-trip these blocks from responses to subsequent requests
          to maintain context across compaction boundaries.

          When content is None, the block represents a failed compaction. The server
          treats these as no-ops. Empty string content is not allowed.

          - `type: "compaction"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

          - `content?: string | null`

            Summary of previously compacted content, or null if compaction failed

          - `encrypted_content?: string | null`

            Opaque metadata from prior compaction, to be round-tripped verbatim

        - `BetaRequestToolAdditionBlock`

          Mid-conversation directive to surface a declared tool.

          `tool` references a tool (or MCP toolset) by name from the request's
          `tools`; it is offered to the model from this point in the
          conversation onward.

          - `tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `BetaToolChangeToolReference`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `name: string`

                pattern: ^[a-zA-Z0-9_-]{1,128}$

              - `type: "tool_reference"`

            - `BetaToolChangeMCPToolReference`

              Reference to a single MCP tool by its server and remote name — the
              same `server_name`/`name` pair `mcp_tool_use` carries.

              - `name: string`

              - `server_name: string`

              - `type: "mcp_tool_reference"`

            - `BetaToolChangeMCPToolsetReference`

              Reference to every tool in the named MCP server's toolset.

              - `server_name: string`

              - `type: "mcp_toolset_reference"`

          - `type: "tool_addition"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaRequestToolRemovalBlock`

          Mid-conversation directive to withdraw a tool.

          `tool` references a tool (or MCP toolset) by name from the request's
          `tools`; it is no longer offered to the model from this point in the
          conversation onward.

          - `tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `BetaToolChangeToolReference`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

            - `BetaToolChangeMCPToolReference`

              Reference to a single MCP tool by its server and remote name — the
              same `server_name`/`name` pair `mcp_tool_use` carries.

            - `BetaToolChangeMCPToolsetReference`

              Reference to every tool in the named MCP server's toolset.

          - `type: "tool_removal"`

          - `cache_control?: BetaCacheControlEphemeral | null`

            Create a cache control breakpoint at this content block.

        - `BetaFallbackBlockParam`

          A `fallback` block echoed back from a prior response.

          Accepted in `messages[].content` and not rendered into the prompt; not
          validated against the request's `fallbacks` chain or top-level `model`.

          Echo the assistant turn back verbatim, including this block in its
          original position. The block marks the boundary between content produced
          before and after a fallback hop, and the server relies on that boundary
          to validate the turn: when thinking runs flank the boundary, omitting
          the block merges them into one span the server cannot validate (the
          request is rejected), and moving it into the middle of a single run is
          likewise rejected; between non-thinking blocks the block's placement has
          no validation effect.

          - `from: BetaFallbackInfoParam`

            Identifies one hop of a fallback transition.

            - `model: Model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `"claude-fable-5-1" | "claude-mythos-5-1" | "claude-sonnet-5" | 14 more`

                - `"claude-fable-5-1"`

                  Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

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

              - `(string & {})`

          - `to: BetaFallbackInfoParam`

            Identifies one hop of a fallback transition.

          - `type: "fallback"`

          - `trigger?: unknown`

            The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

    - `role: "user" | "assistant" | "system"`

      - `"user"`

      - `"assistant"`

      - `"system"`

    - `clear_at?: "next_user_message" | "never" | null`

      How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages.

      - `"next_user_message"`

      - `"never"`

    - `output_config?: BetaSystemMessageOutputConfig | null`

      Per-message output configuration on a role:"system" input message.

      Fields here apply per-turn; `format` remains top-level only. An
      empty `{}` is accepted on a message that carries content; a message
      with neither content nor output_config fields is rejected.

      - `effort?: "low" | "medium" | "high" | 2 more | null`

        All possible effort levels.

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

  - `model: Model`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `cache_control?: BetaCacheControlEphemeral | null`

    Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `context_management?: BetaContextManagementConfig | null`

    Body param: Context management configuration.

    This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

    - `edits?: Array<BetaClearToolUses20250919Edit | BetaClearThinking20251015Edit | BetaCompact20260112Edit>`

      List of context management edits to apply

      minItems: 0

      - `BetaClearToolUses20250919Edit`

        - `type: "clear_tool_uses_20250919"`

        - `clear_at_least?: BetaInputTokensClearAtLeast | null`

          Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

          - `type: "input_tokens"`

          - `value: number`

            minimum: 0

        - `clear_tool_inputs?: boolean | Array<string> | null`

          Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

          - `boolean`

          - `Array<string>`

        - `exclude_tools?: Array<string> | null`

          Tool names whose uses are preserved from clearing

        - `keep?: BetaToolUsesKeep`

          Number of tool uses to retain in the conversation

          - `type: "tool_uses"`

          - `value: number`

            minimum: 0

        - `trigger?: BetaInputTokensTrigger | BetaToolUsesTrigger`

          Condition that triggers the context management strategy

          - `BetaInputTokensTrigger`

            - `type: "input_tokens"`

            - `value: number`

              minimum: 1

          - `BetaToolUsesTrigger`

            - `type: "tool_uses"`

            - `value: number`

              minimum: 1

      - `BetaClearThinking20251015Edit`

        - `type: "clear_thinking_20251015"`

        - `keep?: BetaThinkingTurns | BetaAllThinkingTurns | "all"`

          Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

          - `BetaThinkingTurns`

            - `type: "thinking_turns"`

            - `value: number`

              minimum: 1

          - `BetaAllThinkingTurns`

            - `type: "all"`

          - `"all"`

            - `"all"`

      - `BetaCompact20260112Edit`

        Automatically compact older context when reaching the configured trigger threshold.

        - `type: "compact_20260112"`

        - `instructions?: string | null`

          Additional instructions for summarization.

        - `pause_after_compaction?: boolean`

          Whether to pause after compaction and return the compaction block to the user.

        - `trigger?: BetaInputTokensTrigger | null`

          When to trigger compaction. Defaults to 150000 input tokens.

  - `mcp_servers?: Array<BetaRequestMCPServerURLDefinition>`

    Body param: MCP servers to be utilized in this request

    maxItems: 20

    - `name: string`

    - `type: "url"`

    - `url: string`

    - `authorization_token?: string | null`

    - `tool_configuration?: BetaRequestMCPServerToolConfiguration | null`

      - `allowed_tools?: Array<string> | null`

      - `enabled?: boolean | null`

  - `output_config?: BetaOutputConfig`

    Body param: Configuration options for the model's output, such as the output format.

    - `effort?: "low" | "medium" | "high" | 2 more | null`

      All possible effort levels.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `format?: BetaJSONOutputFormat | null`

      A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

      - `schema: Record<string, unknown>`

        The JSON schema of the format

      - `type: "json_schema"`

    - `task_budget?: BetaTokenTaskBudget | null`

      User-configurable total token budget across contexts.

      - `total: number`

        Total token budget across all contexts in the session.

        minimum: 1024

      - `type: "tokens"`

        The budget type. Currently only 'tokens' is supported.

      - `remaining?: number | null`

        Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

        minimum: 0

  - `speed?: "standard" | "fast" | null`

    Body param: Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

  - `system?: string | Array<BetaTextBlockParam>`

    Body param: System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `string`

    - `Array<BetaTextBlockParam>`

      - `text: string`

        minLength: 1

      - `type: "text"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `citations?: Array<BetaTextCitationParam> | null`

  - `thinking?: BetaThinkingConfigParam`

    Body param: Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `BetaThinkingConfigEnabled`

      - `budget_tokens: number`

        Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

        Must be ≥1024 and less than `max_tokens`.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        minimum: 1024

      - `type: "enabled"`

      - `block_binding?: BetaThinkingBlockBinding | null`

        Controls for block binding: what happens when a thinking block this
        request sends back fails the conversation check. Every field is optional;
        an empty object means every default.

        - `prefix_mismatch_behavior?: BetaThinkingPrefixMismatchBehavior | null`

          What happens when a thinking block in `messages` fails the conversation
          check: it was created in a different conversation, or the messages before
          it have changed since. `"error"` (the default) fails the request with a
          400 error. `"drop_block"` removes the failing blocks and the request
          proceeds; the model no longer sees the dropped reasoning.

          - `"error"`

          - `"drop_block"`

      - `display?: "summarized" | "omitted" | "updates" | null`

        Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

        - `"summarized"`

        - `"omitted"`

        - `"updates"`

    - `BetaThinkingConfigDisabled`

      - `type: "disabled"`

    - `BetaThinkingConfigAdaptive`

      - `type: "adaptive"`

      - `block_binding?: BetaThinkingBlockBinding | null`

        Controls for block binding: what happens when a thinking block this
        request sends back fails the conversation check. Every field is optional;
        an empty object means every default.

      - `display?: "summarized" | "omitted" | "updates" | null`

        Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

        - `"summarized"`

        - `"omitted"`

        - `"updates"`

  - `tool_choice?: BetaToolChoice`

    Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

    - `BetaToolChoiceAuto`

      The model will automatically decide whether to use tools.

      - `type: "auto"`

      - `disable_parallel_tool_use?: boolean`

        Whether to disable parallel tool use.

        Defaults to `false`. If set to `true`, the model will output at most one tool use.

    - `BetaToolChoiceAny`

      The model will use any available tools.

      - `type: "any"`

      - `disable_parallel_tool_use?: boolean`

        Whether to disable parallel tool use.

        Defaults to `false`. If set to `true`, the model will output exactly one tool use.

    - `BetaToolChoiceTool`

      The model will use the specified tool with `tool_choice.name`.

      - `name: string`

        The name of the tool to use.

      - `type: "tool"`

      - `disable_parallel_tool_use?: boolean`

        Whether to disable parallel tool use.

        Defaults to `false`. If set to `true`, the model will output exactly one tool use.

    - `BetaToolChoiceNone`

      The model will not be allowed to use tools.

      - `type: "none"`

  - `tools?: Array<BetaTool | BetaToolBash20241022 | BetaToolBash20250124 | 25 more>`

    Body param: Definitions of tools that the model may use.

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

    - `BetaTool`

      - `input_schema: InputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `type: "object"`

        - `properties?: Record<string, unknown> | null`

        - `required?: Array<string> | null`

      - `name: string`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `description?: string`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `eager_input_streaming?: boolean | null`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `type?: "custom" | null`

    - `BetaToolBash20241022`

      - `name: "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "bash_20241022"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolBash20250124`

      - `name: "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "bash_20250124"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaCodeExecutionTool20250522`

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "code_execution_20250522"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaCodeExecutionTool20250825`

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "code_execution_20250825"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaCodeExecutionTool20260120`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "code_execution_20260120"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaCodeExecutionTool20260521`

      Code execution tool with REPL state persistence.

      - `name: "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "code_execution_20260521"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaBrowserToolset20260801`

      The browser toolset: a single `tools[]` entry (carrying no
      `name`) that declares the browser tool family. The model is served
      the family's tool with any members disabled via `configs` removed
      from its schema.

      - `type: "browser_toolset_20260801"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `configs?: BetaBrowserToolsetConfigs | null`

        Per-member configuration for `browser_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `close_tab?: BetaBrowserCloseTabConfig | null`

          `close_tab`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `double_click?: BetaBrowserDoubleClickConfig | null`

          `double_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `file_upload?: BetaBrowserFileUploadConfig | null`

          `file_upload`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `find?: BetaBrowserFindConfig | null`

          `find`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `form_input?: BetaBrowserFormInputConfig | null`

          `form_input`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `get_page_text?: BetaBrowserGetPageTextConfig | null`

          `get_page_text`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `hold_key?: BetaBrowserHoldKeyConfig | null`

          `hold_key`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `hover?: BetaBrowserHoverConfig | null`

          `hover`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `javascript_exec?: BetaBrowserJavascriptExecConfig | null`

          `javascript_exec`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `key?: BetaBrowserKeyConfig | null`

          `key`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_click?: BetaBrowserLeftClickConfig | null`

          `left_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_click_drag?: BetaBrowserLeftClickDragConfig | null`

          `left_click_drag`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_mouse_down?: BetaBrowserLeftMouseDownConfig | null`

          `left_mouse_down`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_mouse_up?: BetaBrowserLeftMouseUpConfig | null`

          `left_mouse_up`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `list_tabs?: BetaBrowserListTabsConfig | null`

          `list_tabs`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `middle_click?: BetaBrowserMiddleClickConfig | null`

          `middle_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `mouse_move?: BetaBrowserMouseMoveConfig | null`

          `mouse_move`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `navigate?: BetaBrowserNavigateConfig | null`

          `navigate`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `new_tab?: BetaBrowserNewTabConfig | null`

          `new_tab`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `read_console?: BetaBrowserReadConsoleConfig | null`

          `read_console`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `read_network?: BetaBrowserReadNetworkConfig | null`

          `read_network`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `read_page?: BetaBrowserReadPageConfig | null`

          `read_page`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `right_click?: BetaBrowserRightClickConfig | null`

          `right_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `screenshot?: BetaBrowserScreenshotConfig | null`

          `screenshot`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `scroll?: BetaBrowserScrollConfig | null`

          `scroll`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `scroll_to?: BetaBrowserScrollToConfig | null`

          `scroll_to`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `switch_tab?: BetaBrowserSwitchTabConfig | null`

          `switch_tab`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `triple_click?: BetaBrowserTripleClickConfig | null`

          `triple_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type?: BetaBrowserTypeConfig | null`

          `type`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `wait?: BetaBrowserWaitConfig | null`

          `wait`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `zoom?: BetaBrowserZoomConfig | null`

          `zoom`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `BetaToolComputerUse20241022`

      - `display_height_px: number`

        The height of the display in pixels.

        minimum: 1

      - `display_width_px: number`

        The width of the display in pixels.

        minimum: 1

      - `name: "computer"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "computer_20241022"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `display_number?: number | null`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaMemoryTool20250818`

      - `name: "memory"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "memory_20250818"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolComputerUse20250124`

      - `display_height_px: number`

        The height of the display in pixels.

        minimum: 1

      - `display_width_px: number`

        The width of the display in pixels.

        minimum: 1

      - `name: "computer"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "computer_20250124"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `display_number?: number | null`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolTextEditor20241022`

      - `name: "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "text_editor_20241022"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolComputerUse20251124`

      - `display_height_px: number`

        The height of the display in pixels.

        minimum: 1

      - `display_width_px: number`

        The width of the display in pixels.

        minimum: 1

      - `name: "computer"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "computer_20251124"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `display_number?: number | null`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `enable_zoom?: boolean`

        Whether to enable an action to take a zoomed-in screenshot of the screen.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaComputerToolset20260801`

      The computer toolset: a single `tools[]` entry (carrying no
      `name`) that declares the computer tool family. The model is
      served the family's tool with any members disabled via `configs`
      removed from its schema. Every member is enabled by default, zoom
      included. The single-tool options `display_number` and
      `enable_zoom` are not fields of a toolset entry — it carries only
      `type`, `configs`, and `cache_control`; zoom is controlled
      via `configs.zoom.enabled`.

      - `type: "computer_toolset_20260801"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `configs?: BetaComputerToolsetConfigs | null`

        Per-member configuration for `computer_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `cursor_position?: BetaComputerCursorPositionConfig | null`

          `cursor_position`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `double_click?: BetaComputerDoubleClickConfig | null`

          `double_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `hold_key?: BetaComputerHoldKeyConfig | null`

          `hold_key`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `key?: BetaComputerKeyConfig | null`

          `key`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_click?: BetaComputerLeftClickConfig | null`

          `left_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_click_drag?: BetaComputerLeftClickDragConfig | null`

          `left_click_drag`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_mouse_down?: BetaComputerLeftMouseDownConfig | null`

          `left_mouse_down`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `left_mouse_up?: BetaComputerLeftMouseUpConfig | null`

          `left_mouse_up`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `middle_click?: BetaComputerMiddleClickConfig | null`

          `middle_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `mouse_move?: BetaComputerMouseMoveConfig | null`

          `mouse_move`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `right_click?: BetaComputerRightClickConfig | null`

          `right_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `screenshot?: BetaComputerScreenshotConfig | null`

          `screenshot`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `scroll?: BetaComputerScrollConfig | null`

          `scroll`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `triple_click?: BetaComputerTripleClickConfig | null`

          `triple_click`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type?: BetaComputerTypeConfig | null`

          `type`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `wait?: BetaComputerWaitConfig | null`

          `wait`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `zoom?: BetaComputerZoomConfig | null`

          `zoom`'s config overrides.

          - `defer_loading?: boolean | null`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `enabled?: boolean | null`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `BetaToolTextEditor20250124`

      - `name: "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "text_editor_20250124"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolTextEditor20250429`

      - `name: "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "text_editor_20250429"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolTextEditor20250728`

      - `name: "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "text_editor_20250728"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `input_examples?: Array<Record<string, unknown>>`

      - `max_characters?: number | null`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        minimum: 1

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaWebSearchTool20250305`

      - `name: "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_search_20250305"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `blocked_domains?: Array<string> | null`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `user_location?: BetaUserLocation | null`

        Parameters for the user's location. Used to provide more relevant search results.

        - `type: "approximate"`

        - `city?: string | null`

          The city of the user.

          maxLength: 255, minLength: 1

        - `country?: string | null`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          maxLength: 2, minLength: 2

        - `region?: string | null`

          The region of the user.

          maxLength: 255, minLength: 1

        - `timezone?: string | null`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

          maxLength: 255, minLength: 1

    - `BetaWebFetchTool20250910`

      - `name: "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_fetch_20250910"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        List of domains to allow fetching from

      - `blocked_domains?: Array<string> | null`

        List of domains to block fetching from

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `citations?: BetaCitationsConfigParam | null`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_content_tokens?: number | null`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaWebSearchTool20260209`

      - `name: "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_search_20260209"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `blocked_domains?: Array<string> | null`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `user_location?: BetaUserLocation | null`

        Parameters for the user's location. Used to provide more relevant search results.

    - `BetaWebFetchTool20260209`

      - `name: "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_fetch_20260209"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        List of domains to allow fetching from

      - `blocked_domains?: Array<string> | null`

        List of domains to block fetching from

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `citations?: BetaCitationsConfigParam | null`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_content_tokens?: number | null`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaWebFetchTool20260309`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `name: "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_fetch_20260309"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        List of domains to allow fetching from

      - `blocked_domains?: Array<string> | null`

        List of domains to block fetching from

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `citations?: BetaCitationsConfigParam | null`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_content_tokens?: number | null`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `use_cache?: boolean`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `BetaWebSearchTool20260318`

      - `name: "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_search_20260318"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `blocked_domains?: Array<string> | null`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `response_inclusion?: "full" | "excluded"`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `"full"`

        - `"excluded"`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `user_location?: BetaUserLocation | null`

        Parameters for the user's location. Used to provide more relevant search results.

    - `BetaWebFetchTool20260318`

      - `name: "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "web_fetch_20260318"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `allowed_domains?: Array<string> | null`

        List of domains to allow fetching from

      - `blocked_domains?: Array<string> | null`

        List of domains to block fetching from

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `citations?: BetaCitationsConfigParam | null`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_content_tokens?: number | null`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `response_inclusion?: "full" | "excluded"`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `"full"`

        - `"excluded"`

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

      - `use_cache?: boolean`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `BetaAdvisorTool20260301`

      - `model: Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `name: "advisor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "advisor_20260301"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `caching?: BetaCacheControlEphemeral | null`

        Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `max_tokens?: number | null`

        Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

        minimum: 1024

      - `max_uses?: number | null`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolSearchToolBm25_20251119`

      - `name: "tool_search_tool_bm25"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

        - `"tool_search_tool_bm25_20251119"`

        - `"tool_search_tool_bm25"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaToolSearchToolRegex20251119`

      - `name: "tool_search_tool_regex"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

        - `"tool_search_tool_regex_20251119"`

        - `"tool_search_tool_regex"`

      - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

        - `"direct"`

        - `"code_execution_20250825"`

        - `"code_execution_20260120"`

        - `"code_execution_20260521"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `defer_loading?: boolean`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `strict?: boolean`

        When true, guarantees schema validation on tool names and inputs

    - `BetaMCPToolset`

      Configuration for a group of tools from an MCP server.

      Allows configuring enabled status and defer_loading for all tools
      from an MCP server, with optional per-tool overrides.

      - `mcp_server_name: string`

        Name of the MCP server to configure tools for

        maxLength: 255, minLength: 1

      - `type: "mcp_toolset"`

      - `cache_control?: BetaCacheControlEphemeral | null`

        Create a cache control breakpoint at this content block.

      - `configs?: Record<string, BetaMCPToolConfig> | null`

        Configuration overrides for specific tools, keyed by tool name

        - `defer_loading?: boolean`

        - `enabled?: boolean`

      - `default_config?: BetaMCPToolDefaultConfig`

        Default configuration applied to all tools from this server

        - `defer_loading?: boolean`

        - `enabled?: boolean`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 41 more`

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

      - `"mid-conversation-output-config-2026-07-01"`

      - `"thinking-binding-controls-2026-08-01"`

      - `"mid-conversation-system-clear-at-2026-08-21"`

  - `user_profile_id?: string`

    Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

  - `output_format?: BetaJSONOutputFormat | null`

    **Deprecated**

    Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

## Returns

- `BetaMessageTokensCount`

  - `context_management: BetaCountTokensContextManagementResponse | null`

    Information about context management applied to the message.

    - `original_input_tokens: number`

      The original token count before context management was applied

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaMessageTokensCount = await client.beta.messages.countTokens({
  messages: [{ content: "Hello, world", role: "user" }],
  model: "claude-opus-5"
});

console.log(betaMessageTokensCount.context_management);
```

### Response (200)

```json
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```
