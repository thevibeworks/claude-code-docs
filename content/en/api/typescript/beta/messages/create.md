---
title: Create a Message
url: https://platform.claude.com/docs/en/api/typescript/beta/messages/create
---

# Create a Message

`client.beta.messages.create(params, options?): BetaMessage | Stream<BetaRawMessageStreamEvent>`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

## Parameters

- `type MessageCreateParams = MessageCreateParamsNonStreaming | MessageCreateParamsStreaming`

  - `interface MessageCreateParamsBase`

    - `max_tokens: number`

      Body param: The maximum number of tokens to generate before stopping.

      Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

      Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

      Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

      minimum: 0

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

          - `interface BetaTextBlockParam`

            - `type: "text"`

            - `text: string`

              minLength: 1

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

              - `interface BetaCitationCharLocationParam`

                - `type: "char_location"`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string | null`

                  maxLength: 500, minLength: 1

                - `end_char_index: number`

                - `start_char_index: number`

                  minimum: 0

              - `interface BetaCitationPageLocationParam`

                - `type: "page_location"`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string | null`

                  maxLength: 500, minLength: 1

                - `end_page_number: number`

                - `start_page_number: number`

                  minimum: 1

              - `interface BetaCitationContentBlockLocationParam`

                - `type: "content_block_location"`

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

              - `interface BetaCitationWebSearchResultLocationParam`

                - `type: "web_search_result_location"`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string | null`

                  maxLength: 512, minLength: 1

                - `url: string`

                  minLength: 1

              - `interface BetaCitationSearchResultLocationParam`

                - `type: "search_result_location"`

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

          - `interface BetaImageBlockParam`

            - `type: "image"`

            - `source: BetaBase64ImageSource | BetaURLImageSource | BetaFileImageSource`

              - `interface BetaBase64ImageSource`

                - `type: "base64"`

                - `data: string`

                  format: byte

                - `media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp"`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

              - `interface BetaURLImageSource`

                - `type: "url"`

                - `url: string`

              - `interface BetaFileImageSource`

                - `type: "file"`

                - `file_id: string`

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `transformations?: BetaImageTransformationsParam | null`

              Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

              - `oversized_image?: "downsize" | "error"`

                What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                - `"downsize"`

                - `"error"`

          - `interface BetaRequestDocumentBlock`

            - `type: "document"`

            - `source: BetaBase64PDFSource | BetaPlainTextSource | BetaContentBlockSource | 2 more`

              - `interface BetaBase64PDFSource`

                - `type: "base64"`

                - `data: string`

                  format: byte

                - `media_type: "application/pdf"`

              - `interface BetaPlainTextSource`

                - `type: "text"`

                - `data: string`

                - `media_type: "text/plain"`

              - `interface BetaContentBlockSource`

                - `type: "content"`

                - `content: string | Array<BetaContentBlockSourceContent>`

                  - `string`

                  - `Array<BetaContentBlockSourceContent>`

                    - `interface BetaTextBlockParam`

                    - `interface BetaImageBlockParam`

              - `interface BetaURLPDFSource`

                - `type: "url"`

                - `url: string`

              - `interface BetaFileDocumentSource`

                - `type: "file"`

                - `file_id: string`

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `citations?: BetaCitationsConfigParam | null`

              - `enabled?: boolean`

            - `context?: string | null`

              minLength: 1

            - `title?: string | null`

              maxLength: 500, minLength: 1

          - `interface BetaSearchResultBlockParam`

            - `type: "search_result"`

            - `content: Array<BetaTextBlockParam>`

              - `type: "text"`

              - `text: string`

                minLength: 1

              - `cache_control?: BetaCacheControlEphemeral | null`

                Create a cache control breakpoint at this content block.

              - `citations?: Array<BetaTextCitationParam> | null`

            - `source: string`

            - `title: string`

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `citations?: BetaCitationsConfigParam`

          - `interface BetaThinkingBlockParam`

            - `type: "thinking"`

            - `signature: string`

              The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

              Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

            - `thinking: string`

              The `thinking` text of this block as returned by the API.

          - `interface BetaRedactedThinkingBlockParam`

            - `type: "redacted_thinking"`

            - `data: string`

              The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `interface BetaToolUseBlockParam`

            - `type: "tool_use"`

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: Record<string, unknown>`

            - `name: string`

              maxLength: 200, minLength: 1

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

              - `interface BetaDirectCaller`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `interface BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

                - `type: "code_execution_20250825"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `interface BetaServerToolCaller20260120`

                - `type: "code_execution_20260120"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `toolset_name?: string | null`

              For a toolset member tool_use, the toolset family this member belongs to.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `interface BetaToolResultBlockParam`

            - `type: "tool_result"`

            - `tool_use_id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `content?: string | Array<BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | 3 more>`

              - `string`

              - `Array<BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | 3 more>`

                - `interface BetaTextBlockParam`

                - `interface BetaImageBlockParam`

                - `interface BetaSearchResultBlockParam`

                - `interface BetaRequestDocumentBlock`

                - `interface BetaToolReferenceBlockParam`

                  Tool reference block that can be included in tool_result content.

                  - `type: "tool_reference"`

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `cache_control?: BetaCacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                - `interface BetaBrowserStateBlockParam`

                  The caller's browser state after a browser toolset member call —
                  the full inventory of open tabs, which tab is active, and any side
                  effects (tabs opened, download state changes) the call produced.

                  At most one per `tool_result`, only on a non-error result answering a
                  browser toolset member `tool_use`. The server renders the
                  model-visible text from it; the model never sees the raw fields.

                  - `type: "browser_state"`

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

                  - `cache_control?: BetaCacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

                  - `state_changes?: Array<BetaBrowserStateChange> | null`

                    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                    maxItems: 200, minItems: 1

                    - `interface BetaBrowserStateChangeTabOpened`

                      A tab this call's execution opened that remains open at its end —
                      the creation delta of the `tabs` inventory, not an event log.

                      Carries only the `tab_id`; the tab's `title` and `url` live on its
                      `tabs` entry, which must include the same `tab_id`. A tab opened
                      during a failed call gets no deferred `tab_opened`; it simply appears
                      in the next result's `tabs` inventory.

                      - `type: "tab_opened"`

                      - `tab_id: string`

                        The `tab_id` of the opened tab, present in `tabs`.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `interface BetaBrowserStateChangeDownloadStarted`

                      A file download that started during this call.

                      - `type: "download_started"`

                      - `download_id: string`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `url: string`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `interface BetaBrowserStateChangeDownloadCompleted`

                      A file download that finished during this call, reported with the
                      same `download_id` as its `download_started` — or without a prior
                      `download_started`, when the download finished during the call that
                      started it (at most one state change per `download_id` per result).

                      - `type: "download_completed"`

                      - `download_id: string`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `url: string`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `path?: string | null`

                        Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                      - `size_bytes?: number | null`

                        The completed download's size.

                        minimum: 0

                    - `interface BetaBrowserStateChangeDownloadFailed`

                      A file download that failed — or was cancelled — during this call.

                      - `type: "download_failed"`

                      - `download_id: string`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

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

          - `interface BetaServerToolUseBlockParam`

            - `type: "server_tool_use"`

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

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

              - `interface BetaDirectCaller`

                Tool invocation directly from the model.

              - `interface BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `interface BetaServerToolCaller20260120`

          - `interface BetaWebSearchToolResultBlockParam`

            - `type: "web_search_tool_result"`

            - `content: BetaWebSearchToolResultBlockParamContent`

              - `Array<BetaWebSearchResultBlockParam>`

                - `type: "web_search_result"`

                - `encrypted_content: string`

                - `title: string`

                - `url: string`

                - `page_age?: string | null`

              - `interface BetaWebSearchToolRequestError`

                - `type: "web_search_tool_result_error"`

                - `error_code: BetaWebSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

              - `interface BetaDirectCaller`

                Tool invocation directly from the model.

              - `interface BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `interface BetaServerToolCaller20260120`

          - `interface BetaWebFetchToolResultBlockParam`

            - `type: "web_fetch_tool_result"`

            - `content: BetaWebFetchToolResultErrorBlockParam | BetaWebFetchBlockParam`

              - `interface BetaWebFetchToolResultErrorBlockParam`

                - `type: "web_fetch_tool_result_error"`

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

              - `interface BetaWebFetchBlockParam`

                - `type: "web_fetch_result"`

                - `content: BetaRequestDocumentBlock`

                - `url: string`

                  Fetched content URL

                - `retrieved_at?: string | null`

                  ISO 8601 timestamp when the content was retrieved

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

              - `interface BetaDirectCaller`

                Tool invocation directly from the model.

              - `interface BetaServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `interface BetaServerToolCaller20260120`

          - `interface BetaAdvisorToolResultBlockParam`

            - `type: "advisor_tool_result"`

            - `content: BetaAdvisorToolResultErrorParam | BetaAdvisorResultBlockParam | BetaAdvisorRedactedResultBlockParam`

              - `interface BetaAdvisorToolResultErrorParam`

                - `type: "advisor_tool_result_error"`

                - `error_code: "max_uses_exceeded" | "prompt_too_long" | "too_many_requests" | 4 more`

                  - `"max_uses_exceeded"`

                  - `"prompt_too_long"`

                  - `"too_many_requests"`

                  - `"overloaded"`

                  - `"unavailable"`

                  - `"execution_time_exceeded"`

                  - `"model_not_found"`

              - `interface BetaAdvisorResultBlockParam`

                - `type: "advisor_result"`

                - `text: string`

                - `stop_reason?: string | null`

              - `interface BetaAdvisorRedactedResultBlockParam`

                - `type: "advisor_redacted_result"`

                - `encrypted_content: string`

                  Opaque blob produced by a prior response; must be round-tripped verbatim.

                - `stop_reason?: string | null`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaCodeExecutionToolResultBlockParam`

            - `type: "code_execution_tool_result"`

            - `content: BetaCodeExecutionToolResultBlockParamContent`

              - `interface BetaCodeExecutionToolResultErrorParam`

                - `type: "code_execution_tool_result_error"`

                - `error_code: BetaCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

              - `interface BetaCodeExecutionResultBlockParam`

                - `type: "code_execution_result"`

                - `content: Array<BetaCodeExecutionOutputBlockParam>`

                  - `type: "code_execution_output"`

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

              - `interface BetaEncryptedCodeExecutionResultBlockParam`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type: "encrypted_code_execution_result"`

                - `content: Array<BetaCodeExecutionOutputBlockParam>`

                  - `type: "code_execution_output"`

                  - `file_id: string`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaBashCodeExecutionToolResultBlockParam`

            - `type: "bash_code_execution_tool_result"`

            - `content: BetaBashCodeExecutionToolResultErrorParam | BetaBashCodeExecutionResultBlockParam`

              - `interface BetaBashCodeExecutionToolResultErrorParam`

                - `type: "bash_code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

              - `interface BetaBashCodeExecutionResultBlockParam`

                - `type: "bash_code_execution_result"`

                - `content: Array<BetaBashCodeExecutionOutputBlockParam>`

                  - `type: "bash_code_execution_output"`

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaTextEditorCodeExecutionToolResultBlockParam`

            - `type: "text_editor_code_execution_tool_result"`

            - `content: BetaTextEditorCodeExecutionToolResultErrorParam | BetaTextEditorCodeExecutionViewResultBlockParam | BetaTextEditorCodeExecutionCreateResultBlockParam | BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

              - `interface BetaTextEditorCodeExecutionToolResultErrorParam`

                - `type: "text_editor_code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message?: string | null`

              - `interface BetaTextEditorCodeExecutionViewResultBlockParam`

                - `type: "text_editor_code_execution_view_result"`

                - `content: string`

                - `file_type: "text" | "image" | "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines?: number | null`

                - `start_line?: number | null`

                - `total_lines?: number | null`

              - `interface BetaTextEditorCodeExecutionCreateResultBlockParam`

                - `type: "text_editor_code_execution_create_result"`

                - `is_file_update: boolean`

              - `interface BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

                - `type: "text_editor_code_execution_str_replace_result"`

                - `lines?: Array<string> | null`

                - `new_lines?: number | null`

                - `new_start?: number | null`

                - `old_lines?: number | null`

                - `old_start?: number | null`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaToolSearchToolResultBlockParam`

            - `type: "tool_search_tool_result"`

            - `content: BetaToolSearchToolResultErrorParam | BetaToolSearchToolSearchResultBlockParam`

              - `interface BetaToolSearchToolResultErrorParam`

                - `type: "tool_search_tool_result_error"`

                - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message?: string | null`

              - `interface BetaToolSearchToolSearchResultBlockParam`

                - `type: "tool_search_tool_search_result"`

                - `tool_references: Array<BetaToolReferenceBlockParam>`

                  - `type: "tool_reference"`

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `cache_control?: BetaCacheControlEphemeral | null`

                    Create a cache control breakpoint at this content block.

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaMCPToolUseBlockParam`

            - `type: "mcp_tool_use"`

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: Record<string, unknown>`

            - `name: string`

            - `server_name: string`

              The name of the MCP server

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaRequestMCPToolResultBlockParam`

            - `type: "mcp_tool_result"`

            - `tool_use_id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

            - `content?: string | Array<BetaTextBlockParam>`

              - `string`

              - `Array<BetaTextBlockParam>`

                - `type: "text"`

                - `text: string`

                  minLength: 1

                - `cache_control?: BetaCacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

                - `citations?: Array<BetaTextCitationParam> | null`

            - `is_error?: boolean`

          - `interface BetaContainerUploadBlockParam`

            A content block that represents a file to be uploaded to the container
            Files uploaded via this block will be available in the container's input directory.

            - `type: "container_upload"`

            - `file_id: string`

            - `cache_control?: BetaCacheControlEphemeral | null`

              Create a cache control breakpoint at this content block.

          - `interface BetaCompactionBlockParam`

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

            - `signature?: string | null`

              The block's signature as returned, to be sent back verbatim

            - `tool_changes?: Array<BetaRequestToolAdditionBlock | BetaRequestToolRemovalBlock> | null`

              The tool changes of the compacted range, as the server returned them on this block: the `tool_addition` and `tool_removal` entries that take the request's `tools` to the tool set in effect at the end of the range. Send them back unchanged with the block.

              - `interface BetaRequestToolAdditionBlock`

                Mid-conversation directive to make a tool available.

                `tool` is a reference to a tool (or MCP toolset) declared in the
                request's `tools`. Under the `inline-tools-2026-09-15` beta it may
                instead be a reference to a tool defined earlier in `messages`, or a
                `tool_definition` object that carries an inline tool definition in
                `definition` (the same object a `tools` entry holds). An `mcp_toolset`
                definition also requires the `mcp-client-2026-09-15` beta. The tool is
                offered to the model from this point in the conversation onward.

                - `type: "tool_addition"`

                - `tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference | BetaToolChangeToolDefinitionParam`

                  - `interface BetaToolChangeToolReference`

                    Reference to a single tool, by the name the model uses to call it: a
                    tool declared in `tools` or defined by an earlier `tool_addition`
                    block. Does not accept the composed `{server}_{name}` form the server
                    assigns to MCP-resolved tools; use `mcp_tool_reference` or
                    `mcp_toolset_reference` for those.

                    - `type: "tool_reference"`

                    - `name: string`

                      pattern: ^[a-zA-Z0-9_-]{1,128}$

                  - `interface BetaToolChangeMCPToolReference`

                    Reference to a single MCP tool by its server and remote name; the
                    same `server_name`/`name` pair `mcp_tool_use` carries.

                    - `type: "mcp_tool_reference"`

                    - `name: string`

                    - `server_name: string`

                  - `interface BetaToolChangeMCPToolsetReference`

                    Reference to every tool in the named MCP server's toolset.

                    - `type: "mcp_toolset_reference"`

                    - `server_name: string`

                  - `interface BetaToolChangeToolDefinitionParam`

                    A tool defined by value: `definition` is a `tools` entry (any kind
                    `tools` accepts, an MCP toolset included). An `mcp_toolset` given here
                    also requires the `mcp-client-2026-09-15` beta.

                    - `type: "tool_definition"`

                    - `definition: BetaToolUnion`

                      - `interface BetaTool`

                        - `type?: "custom" | null`

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

                      - `interface BetaToolBash20241022`

                        - `type: "bash_20241022"`

                        - `name: "bash"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolBash20250124`

                        - `type: "bash_20250124"`

                        - `name: "bash"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaCodeExecutionTool20250522`

                        - `type: "code_execution_20250522"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaCodeExecutionTool20250825`

                        - `type: "code_execution_20250825"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaCodeExecutionTool20260120`

                        Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

                        - `type: "code_execution_20260120"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaCodeExecutionTool20260521`

                        Code execution tool with REPL state persistence.

                        - `type: "code_execution_20260521"`

                        - `name: "code_execution"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaBrowserToolset20260801`

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

                          - `type?: BetaBrowserTypeConfig | null`

                            `type`'s config overrides.

                            - `defer_loading?: boolean | null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled?: boolean | null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

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

                      - `interface BetaToolComputerUse20241022`

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

                      - `interface BetaMemoryTool20250818`

                        - `type: "memory_20250818"`

                        - `name: "memory"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolComputerUse20250124`

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

                      - `interface BetaToolTextEditor20241022`

                        - `type: "text_editor_20241022"`

                        - `name: "str_replace_editor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolComputerUse20251124`

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

                      - `interface BetaComputerToolset20260801`

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

                          - `type?: BetaComputerTypeConfig | null`

                            `type`'s config overrides.

                            - `defer_loading?: boolean | null`

                              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                            - `enabled?: boolean | null`

                              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

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

                      - `interface BetaToolTextEditor20250124`

                        - `type: "text_editor_20250124"`

                        - `name: "str_replace_editor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolTextEditor20250429`

                        - `type: "text_editor_20250429"`

                        - `name: "str_replace_based_edit_tool"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolTextEditor20250728`

                        - `type: "text_editor_20250728"`

                        - `name: "str_replace_based_edit_tool"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaWebSearchTool20250305`

                        - `type: "web_search_20250305"`

                        - `name: "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaWebFetchTool20250910`

                        - `type: "web_fetch_20250910"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                        - `url_sources?: BetaWebFetchURLSources | null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                          - `client_tool_results?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone | BetaWebFetchURLSourceOnly | BetaWebFetchURLSourceExcept`

                            Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

                            - `interface BetaWebFetchURLSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                              - `type: "all"`

                            - `interface BetaWebFetchURLSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                              - `type: "none"`

                            - `interface BetaWebFetchURLSourceOnly`

                              The tool filter variant under which only the named tools' results
                              contribute.

                              - `type: "only"`

                              - `tools: Array<BetaWebFetchURLSourceToolReference>`

                                - `type: "tool_reference"`

                                - `name: string`

                            - `interface BetaWebFetchURLSourceExcept`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                              - `type: "except"`

                              - `tools: Array<BetaWebFetchURLSourceToolReference>`

                                - `type: "tool_reference"`

                                - `name: string`

                          - `server_tool_results?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone | BetaWebFetchURLSourceOnly | BetaWebFetchURLSourceExcept`

                            Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

                            - `interface BetaWebFetchURLSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `interface BetaWebFetchURLSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                            - `interface BetaWebFetchURLSourceOnly`

                              The tool filter variant under which only the named tools' results
                              contribute.

                            - `interface BetaWebFetchURLSourceExcept`

                              The tool filter variant under which every result but the named
                              tools' contributes.

                          - `user_input?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone`

                            Whether URLs in user messages are fetchable: "all" or "none".

                            - `interface BetaWebFetchURLSourceAll`

                              The `url_sources` variant under which a source contributes in
                              full: every result of the tool filter's source, or all user input.

                            - `interface BetaWebFetchURLSourceNone`

                              The `url_sources` variant under which a source contributes nothing:
                              no result of the tool filter's source, or no user input.

                      - `interface BetaWebSearchTool20260209`

                        - `type: "web_search_20260209"`

                        - `name: "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaWebFetchTool20260209`

                        - `type: "web_fetch_20260209"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                        - `url_sources?: BetaWebFetchURLSources | null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                      - `interface BetaWebFetchTool20260309`

                        Web fetch tool with use_cache parameter for bypassing cached content.

                        - `type: "web_fetch_20260309"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                        - `url_sources?: BetaWebFetchURLSources | null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                        - `use_cache?: boolean`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `interface BetaWebSearchTool20260318`

                        - `type: "web_search_20260318"`

                        - `name: "web_search"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaWebFetchTool20260318`

                        - `type: "web_fetch_20260318"`

                        - `name: "web_fetch"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                        - `url_sources?: BetaWebFetchURLSources | null`

                          Which sources contribute to the set of URLs web fetch may fetch.

                          Each key is a tagged variant: `user_input` is `all` or `none`; the
                          two tool filters are `all`, `none`, `only` (only the named tools'
                          results) or `except` (every result but the named tools'). A named tool
                          must be declared in this request's `tools[]`.

                        - `use_cache?: boolean`

                          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                      - `interface BetaAdvisorTool20260301`

                        - `type: "advisor_20260301"`

                        - `model: Model`

                          The model that will complete your prompt.

                          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                          - `"claude-fable-5-1" | "claude-opus-5-5" | "claude-mythos-5-1" | 15 more`

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

                          - `(string & {})`

                        - `name: "advisor"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolSearchToolBm25_20251119`

                        - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

                          - `"tool_search_tool_bm25_20251119"`

                          - `"tool_search_tool_bm25"`

                        - `name: "tool_search_tool_bm25"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaToolSearchToolRegex20251119`

                        - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

                          - `"tool_search_tool_regex_20251119"`

                          - `"tool_search_tool_regex"`

                        - `name: "tool_search_tool_regex"`

                          Name of the tool.

                          This is how the tool will be called by the model and in `tool_use` blocks.

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

                      - `interface BetaMCPToolset`

                        Configuration for a group of tools from an MCP server.

                        Allows configuring enabled status and defer_loading for all tools
                        from an MCP server, with optional per-tool overrides.

                        - `type: "mcp_toolset"`

                        - `mcp_server_name: string`

                          Name of the MCP server to configure tools for

                          maxLength: 255, minLength: 1

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

                        - `tools?: Array<BetaMCPToolParam> | null`

                          The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

                          - `input_schema: Record<string, unknown>`

                            The tool's input schema as the MCP server lists it, verbatim.

                          - `name: string`

                            The tool's name as the MCP server lists it (not prefixed with the server name).

                            minLength: 1

                          - `description?: string | null`

                            The tool's description as the MCP server lists it.

                - `cache_control?: BetaCacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

              - `interface BetaRequestToolRemovalBlock`

                Mid-conversation directive to withdraw a tool.

                `tool` references a tool (or MCP toolset) by name: one declared in the
                request's `tools` or defined earlier in `messages`. It is no longer
                offered to the model from this point in the conversation onward.

                - `type: "tool_removal"`

                - `tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference`

                  - `interface BetaToolChangeToolReference`

                    Reference to a single tool, by the name the model uses to call it: a
                    tool declared in `tools` or defined by an earlier `tool_addition`
                    block. Does not accept the composed `{server}_{name}` form the server
                    assigns to MCP-resolved tools; use `mcp_tool_reference` or
                    `mcp_toolset_reference` for those.

                  - `interface BetaToolChangeMCPToolReference`

                    Reference to a single MCP tool by its server and remote name; the
                    same `server_name`/`name` pair `mcp_tool_use` carries.

                  - `interface BetaToolChangeMCPToolsetReference`

                    Reference to every tool in the named MCP server's toolset.

                - `cache_control?: BetaCacheControlEphemeral | null`

                  Create a cache control breakpoint at this content block.

          - `interface BetaRequestToolAdditionBlock`

            Mid-conversation directive to make a tool available.

            `tool` is a reference to a tool (or MCP toolset) declared in the
            request's `tools`. Under the `inline-tools-2026-09-15` beta it may
            instead be a reference to a tool defined earlier in `messages`, or a
            `tool_definition` object that carries an inline tool definition in
            `definition` (the same object a `tools` entry holds). An `mcp_toolset`
            definition also requires the `mcp-client-2026-09-15` beta. The tool is
            offered to the model from this point in the conversation onward.

          - `interface BetaRequestToolRemovalBlock`

            Mid-conversation directive to withdraw a tool.

            `tool` references a tool (or MCP toolset) by name: one declared in the
            request's `tools` or defined earlier in `messages`. It is no longer
            offered to the model from this point in the conversation onward.

          - `interface BetaMCPToolListingBlockParam`

            The tool listing an MCP server returned while an earlier response was
            produced, as that response carried it. Send the assistant message back
            unchanged, this block included, and the server uses this listing for the
            matching `mcp_toolset` instead of asking the MCP server again.

            - `type: "mcp_tool_listing"`

            - `mcp_server_name: string`

              The name of the MCP server this listing came from, as `mcp_servers` declares it.

              maxLength: 255, minLength: 1

            - `tools: Array<BetaMCPToolParam>`

              The server's tools, exactly as the response listed them.

              - `input_schema: Record<string, unknown>`

                The tool's input schema as the MCP server lists it, verbatim.

              - `name: string`

                The tool's name as the MCP server lists it (not prefixed with the server name).

                minLength: 1

              - `description?: string | null`

                The tool's description as the MCP server lists it.

          - `interface BetaFallbackBlockParam`

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

            - `type: "fallback"`

            - `from: BetaFallbackInfoParam`

              Identifies one hop of a fallback transition.

              - `model: Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `to: BetaFallbackInfoParam`

              Identifies one hop of a fallback transition.

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

    - `compaction?: BetaCompactionConfig | null`

      Body param: Compact the whole conversation and return a signed `compaction` block,
      alone, that a later request sends back first in `messages`, in place of
      the messages it summarizes. There is no trigger and no pause flag: sending
      the parameter compacts, and nothing is sampled after the block.

      The summarization prompt is the server's own unless `instructions` are
      given, which then replace it for this request; a value that is empty or
      only whitespace counts as absent.

      - `type: "summarize"`

      - `instructions?: string | null`

        Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

        maxLength: 16384

    - `container?: BetaContainerParams | string | null`

      Body param: Container identifier for reuse across requests.

      - `interface BetaContainerParams`

        Container parameters with skills to be loaded.

        - `id?: string | null`

          Container id

        - `skills?: Array<BetaSkillParams> | null`

          List of skills to load in the container

          maxItems: 20

          - `type: "anthropic" | "custom"`

            Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

            - `"anthropic"`

            - `"custom"`

          - `skill_id: string`

            Skill ID

            maxLength: 64, minLength: 1

          - `version?: string`

            Skill version or 'latest' for most recent version

            maxLength: 64, minLength: 1

      - `string`

    - `context_management?: BetaContextManagementConfig | null`

      Body param: Context management configuration.

      This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

      - `edits?: Array<BetaClearToolUses20250919Edit | BetaClearThinking20251015Edit | BetaCompact20260112Edit>`

        List of context management edits to apply

        minItems: 0

        - `interface BetaClearToolUses20250919Edit`

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

            - `interface BetaInputTokensTrigger`

              - `type: "input_tokens"`

              - `value: number`

                minimum: 1

            - `interface BetaToolUsesTrigger`

              - `type: "tool_uses"`

              - `value: number`

                minimum: 1

        - `interface BetaClearThinking20251015Edit`

          - `type: "clear_thinking_20251015"`

          - `keep?: BetaThinkingTurns | BetaAllThinkingTurns | "all"`

            Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

            - `interface BetaThinkingTurns`

              - `type: "thinking_turns"`

              - `value: number`

                minimum: 1

            - `interface BetaAllThinkingTurns`

              - `type: "all"`

            - `"all"`

              - `"all"`

        - `interface BetaCompact20260112Edit`

          Automatically compact older context when reaching the configured trigger threshold.

          - `type: "compact_20260112"`

          - `instructions?: string | null`

            Additional instructions for summarization.

          - `pause_after_compaction?: boolean`

            Whether to pause after compaction and return the compaction block to the user.

          - `trigger?: BetaInputTokensTrigger | null`

            When to trigger compaction. Defaults to 150000 input tokens.

    - `diagnostics?: BetaDiagnosticsParam | null`

      Body param: Request-level diagnostics. Currently carries the previous response
      id for prompt-cache divergence reporting.

      - `previous_message_id?: string | null`

        The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

        maxLength: 256

    - `fallback_credit_token?: string | BetaFallbackCreditTokenParam | null`

      Body param: The `fallback_credit_token` from a prior refusal's `stop_details`.

      When a preceding request was refused and returned a `fallback_credit_token`,
      pass that code here on the retry to have the retry's cache-creation tokens
      for the prefix that was warm on the refused model billed at the cache-read
      rate. Must be redeemed by the same organization and workspace, with the same
      request body (optionally extended by one appended `assistant` message whose
      content is the partial text — with any trailing whitespace stripped from
      the final text block — and paired server-tool blocks streamed before the
      refusal; the appended-assistant form is not available for requests with
      `output_format` set or forced `tool_choice`), on an eligible fallback
      model, on the same platform,
      and within 5 minutes of the refusal; a mismatch is a 400. A token minted
      mid-server-tool-loop whose partial content was continuable may only be
      redeemed with the appended-assistant form — if an exact-body retry is
      rejected with a 400 saying the token must be redeemed by continuing the
      partial response, retry with the appended-assistant form instead.

      When the appended-assistant form is used on a model that otherwise disallows
      assistant-turn prefill, this token also authorizes that one prefill.

      - `string`

      - `interface BetaFallbackCreditTokenParam`

        Object form of `fallback_credit_token`: the token plus a redemption
        mode.

        Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
        header the field accepts the bare string only. The bare string and the
        mode-less object are equivalent (both select `strict`), so wrapping
        an existing token changes nothing by itself.

        - `token: string`

          The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

          maxLength: 2048, minLength: 1

        - `mode?: "strict" | "best_effort"`

          How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

          - `"strict"`

          - `"best_effort"`

    - `fallbacks?: BetaFallbacksParam | null`

      Body param: Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

      - `Array<BetaFallbackParam>`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `max_tokens?: number | null`

        - `output_config?: BetaOutputConfig | null`

          - `effort?: "low" | "medium" | "high" | 2 more | null`

            All possible effort levels.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `format?: BetaJSONOutputFormat | null`

            A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

            - `type: "json_schema"`

            - `schema: Record<string, unknown>`

              The JSON schema of the format

          - `task_budget?: BetaTokenTaskBudget | null`

            User-configurable total token budget across contexts.

            - `type: "tokens"`

              The budget type. Currently only 'tokens' is supported.

            - `total: number`

              Total token budget across all contexts in the session.

              minimum: 1024

            - `remaining?: number | null`

              Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

              minimum: 0

        - `speed?: "standard" | "fast" | null`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

        - `thinking?: BetaThinkingConfigEnabled | BetaThinkingConfigDisabled | BetaThinkingConfigAdaptive | null`

          - `interface BetaThinkingConfigEnabled`

            - `type: "enabled"`

            - `budget_tokens: number`

              Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

              Must be ≥1024 and less than `max_tokens`.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

              minimum: 1024

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

          - `interface BetaThinkingConfigDisabled`

            - `type: "disabled"`

          - `interface BetaThinkingConfigAdaptive`

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

      - `"default"`

        - `"default"`

    - `inference_geo?: string | null`

      Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

    - `mcp_servers?: Array<BetaRequestMCPServerURLDefinition>`

      Body param: MCP servers to be utilized in this request

      maxItems: 20

      - `type: "url"`

      - `name: string`

      - `url: string`

      - `authorization_token?: string | null`

      - `tool_configuration?: BetaRequestMCPServerToolConfiguration | null`

        - `allowed_tools?: Array<string> | null`

        - `enabled?: boolean | null`

    - `metadata?: BetaMetadata`

      Body param: An object describing metadata about the request.

      - `user_id?: string | null`

        An external identifier for the user who is associated with the request.

        This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

        maxLength: 512

    - `output_config?: BetaOutputConfig`

      Body param: Configuration options for the model's output, such as the output format.

    - `service_tier?: "auto" | "standard_only"`

      Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

      Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

      - `"auto"`

      - `"standard_only"`

    - `speed?: "standard" | "fast" | null`

      Body param: Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

    - `stop_sequences?: Array<string>`

      Body param: Custom text sequences that will cause the model to stop generating.

      Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

      If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

    - `stream?: false`

      Body param: Whether to incrementally stream the response using server-sent events.

      See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

    - `system?: string | Array<BetaTextBlockParam>`

      Body param: System prompt.

      A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

      - `string`

      - `Array<BetaTextBlockParam>`

        - `type: "text"`

        - `text: string`

          minLength: 1

        - `cache_control?: BetaCacheControlEphemeral | null`

          Create a cache control breakpoint at this content block.

        - `citations?: Array<BetaTextCitationParam> | null`

    - `thinking?: BetaThinkingConfigParam`

      Body param: Configuration for enabling Claude's extended thinking.

      When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `interface BetaThinkingConfigEnabled`

      - `interface BetaThinkingConfigDisabled`

      - `interface BetaThinkingConfigAdaptive`

    - `tool_choice?: BetaToolChoice`

      Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

      - `interface BetaToolChoiceAuto`

        The model will automatically decide whether to use tools.

        - `type: "auto"`

        - `disable_parallel_tool_use?: boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output at most one tool use.

      - `interface BetaToolChoiceAny`

        The model will use any available tools.

        - `type: "any"`

        - `disable_parallel_tool_use?: boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `interface BetaToolChoiceTool`

        The model will use the specified tool with `tool_choice.name`.

        - `type: "tool"`

        - `name: string`

          The name of the tool to use.

        - `disable_parallel_tool_use?: boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `interface BetaToolChoiceNone`

        The model will not be allowed to use tools.

        - `type: "none"`

    - `tools?: Array<BetaToolUnion>`

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

      - `interface BetaTool`

      - `interface BetaToolBash20241022`

      - `interface BetaToolBash20250124`

      - `interface BetaCodeExecutionTool20250522`

      - `interface BetaCodeExecutionTool20250825`

      - `interface BetaCodeExecutionTool20260120`

        Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `interface BetaCodeExecutionTool20260521`

        Code execution tool with REPL state persistence.

      - `interface BetaBrowserToolset20260801`

        The browser toolset: a single `tools[]` entry (carrying no
        `name`) that declares the browser tool family. The model is served
        the family's tool with any members disabled via `configs` removed
        from its schema.

      - `interface BetaToolComputerUse20241022`

      - `interface BetaMemoryTool20250818`

      - `interface BetaToolComputerUse20250124`

      - `interface BetaToolTextEditor20241022`

      - `interface BetaToolComputerUse20251124`

      - `interface BetaComputerToolset20260801`

        The computer toolset: a single `tools[]` entry (carrying no
        `name`) that declares the computer tool family. The model is
        served the family's tool with any members disabled via `configs`
        removed from its schema. Every member is enabled by default, zoom
        included. The single-tool options `display_number` and
        `enable_zoom` are not fields of a toolset entry — it carries only
        `type`, `configs`, and `cache_control`; zoom is controlled
        via `configs.zoom.enabled`.

      - `interface BetaToolTextEditor20250124`

      - `interface BetaToolTextEditor20250429`

      - `interface BetaToolTextEditor20250728`

      - `interface BetaWebSearchTool20250305`

      - `interface BetaWebFetchTool20250910`

      - `interface BetaWebSearchTool20260209`

      - `interface BetaWebFetchTool20260209`

      - `interface BetaWebFetchTool20260309`

        Web fetch tool with use_cache parameter for bypassing cached content.

      - `interface BetaWebSearchTool20260318`

      - `interface BetaWebFetchTool20260318`

      - `interface BetaAdvisorTool20260301`

      - `interface BetaToolSearchToolBm25_20251119`

      - `interface BetaToolSearchToolRegex20251119`

      - `interface BetaMCPToolset`

        Configuration for a group of tools from an MCP server.

        Allows configuring enabled status and defer_loading for all tools
        from an MCP server, with optional per-tool overrides.

    - `betas?: Array<AnthropicBeta>`

      Header param: Optional header to specify the beta version(s) you want to use.

      - `(string & {})`

      - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 45 more`

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

    - `user_profile_id?: string`

      Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

    - `workspace_id?: string`

      Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

      Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

    - `output_format?: BetaJSONOutputFormat | null`

      **Deprecated**

      Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

      A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

    - `temperature?: number`

      **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

      Body param: Amount of randomness injected into the response.

      Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

      Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

      maximum: 1, minimum: 0

    - `top_k?: number`

      **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

      Body param: Only sample from the top K options for each subsequent token.

      Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

      Recommended for advanced use cases only.

      minimum: 0

    - `top_p?: number`

      **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

      Body param: Use nucleus sampling.

      In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

      Recommended for advanced use cases only.

      maximum: 1, minimum: 0

  - `interface MessageCreateParamsNonStreaming extends  MessageCreateParamsBase`

    - `stream?: false`

      Body param: Whether to incrementally stream the response using server-sent events.

      See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

  - `interface MessageCreateParamsStreaming extends  MessageCreateParamsBase`

    - `stream: true`

      Body param: Whether to incrementally stream the response using server-sent events.

      See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

## Returns

- `interface BetaMessage`

  - `type: "message"`

    Object type.

    For Messages, this is always `"message"`.

    default: message

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: BetaContainer | null`

    Information about the container used in the request (for the code execution tool)

    - `id: string`

      Identifier for the container used in this request

    - `expires_at: string`

      The time at which the container will expire.

      format: date-time

    - `skills: Array<BetaContainerSkill> | null`

      Skills loaded in the container

      - `type: "anthropic" | "custom"`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `"anthropic"`

        - `"custom"`

      - `skill_id: string`

        Skill ID

        maxLength: 64, minLength: 1

      - `version: string`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `content: Array<BetaContentBlock>`

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

    - `interface BetaTextBlock`

      - `type: "text"`

        default: text

      - `citations: Array<BetaTextCitation> | null`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `interface BetaCitationCharLocation`

          - `type: "char_location"`

            default: char_location

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string | null`

          - `end_char_index: number`

          - `file_id: string | null`

          - `start_char_index: number`

            minimum: 0

        - `interface BetaCitationPageLocation`

          - `type: "page_location"`

            default: page_location

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string | null`

          - `end_page_number: number`

          - `file_id: string | null`

          - `start_page_number: number`

            minimum: 1

        - `interface BetaCitationContentBlockLocation`

          - `type: "content_block_location"`

            default: content_block_location

          - `cited_text: string`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `document_index: number`

            minimum: 0

          - `document_title: string | null`

          - `end_block_index: number`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `file_id: string | null`

          - `start_block_index: number`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

        - `interface BetaCitationsWebSearchResultLocation`

          - `type: "web_search_result_location"`

            default: web_search_result_location

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string | null`

            maxLength: 512

          - `url: string`

        - `interface BetaCitationSearchResultLocation`

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

          - `title: string | null`

      - `text: string`

        minLength: 0

    - `interface BetaThinkingBlock`

      - `type: "thinking"`

        default: thinking

      - `signature: string`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `thinking: string`

        The text of Claude's thinking process for this block.

    - `interface BetaRedactedThinkingBlock`

      - `type: "redacted_thinking"`

        default: redacted_thinking

      - `data: string`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

    - `interface BetaToolUseBlock`

      - `type: "tool_use"`

        default: tool_use

      - `id: string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `input: Record<string, unknown>`

      - `name: string`

        minLength: 1

      - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        - `interface BetaDirectCaller`

          Tool invocation directly from the model.

          - `type: "direct"`

        - `interface BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `type: "code_execution_20250825"`

          - `tool_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `interface BetaServerToolCaller20260120`

          - `type: "code_execution_20260120"`

          - `tool_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `toolset_name?: string | null`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `interface BetaServerToolUseBlock`

      - `type: "server_tool_use"`

        default: server_tool_use

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

      - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        - `interface BetaDirectCaller`

          Tool invocation directly from the model.

        - `interface BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `interface BetaServerToolCaller20260120`

    - `interface BetaWebSearchToolResultBlock`

      - `type: "web_search_tool_result"`

        default: web_search_tool_result

      - `content: BetaWebSearchToolResultBlockContent`

        - `interface BetaWebSearchToolResultError`

          - `type: "web_search_tool_result_error"`

            default: web_search_tool_result_error

          - `error_code: BetaWebSearchToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

        - `Array<BetaWebSearchResultBlock>`

          - `type: "web_search_result"`

            default: web_search_result

          - `encrypted_content: string`

          - `page_age: string | null`

          - `title: string`

          - `url: string`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        - `interface BetaDirectCaller`

          Tool invocation directly from the model.

        - `interface BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `interface BetaServerToolCaller20260120`

    - `interface BetaWebFetchToolResultBlock`

      - `type: "web_fetch_tool_result"`

        default: web_fetch_tool_result

      - `content: BetaWebFetchToolResultErrorBlock | BetaWebFetchBlock`

        - `interface BetaWebFetchToolResultErrorBlock`

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

        - `interface BetaWebFetchBlock`

          - `type: "web_fetch_result"`

            default: web_fetch_result

          - `content: BetaDocumentBlock`

            - `type: "document"`

              default: document

            - `citations: BetaCitationConfig | null`

              Citation configuration for the document

              - `enabled: boolean`

                default: false

            - `source: BetaBase64PDFSource | BetaPlainTextSource`

              - `interface BetaBase64PDFSource`

                - `type: "base64"`

                - `data: string`

                  format: byte

                - `media_type: "application/pdf"`

              - `interface BetaPlainTextSource`

                - `type: "text"`

                - `data: string`

                - `media_type: "text/plain"`

            - `title: string | null`

              The title of the document

          - `retrieved_at: string | null`

            ISO 8601 timestamp when the content was retrieved

          - `url: string`

            Fetched content URL

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        - `interface BetaDirectCaller`

          Tool invocation directly from the model.

        - `interface BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `interface BetaServerToolCaller20260120`

    - `interface BetaAdvisorToolResultBlock`

      - `type: "advisor_tool_result"`

        default: advisor_tool_result

      - `content: BetaAdvisorToolResultError | BetaAdvisorResultBlock | BetaAdvisorRedactedResultBlock`

        - `interface BetaAdvisorToolResultError`

          - `type: "advisor_tool_result_error"`

            default: advisor_tool_result_error

          - `error_code: "max_uses_exceeded" | "prompt_too_long" | "too_many_requests" | 4 more`

            - `"max_uses_exceeded"`

            - `"prompt_too_long"`

            - `"too_many_requests"`

            - `"overloaded"`

            - `"unavailable"`

            - `"execution_time_exceeded"`

            - `"model_not_found"`

        - `interface BetaAdvisorResultBlock`

          - `type: "advisor_result"`

            default: advisor_result

          - `stop_reason: string | null`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

          - `text: string`

        - `interface BetaAdvisorRedactedResultBlock`

          - `type: "advisor_redacted_result"`

            default: advisor_redacted_result

          - `encrypted_content: string`

            Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

          - `stop_reason: string | null`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `interface BetaCodeExecutionToolResultBlock`

      - `type: "code_execution_tool_result"`

        default: code_execution_tool_result

      - `content: BetaCodeExecutionToolResultBlockContent`

        - `interface BetaCodeExecutionToolResultError`

          - `type: "code_execution_tool_result_error"`

            default: code_execution_tool_result_error

          - `error_code: BetaCodeExecutionToolResultErrorCode`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

        - `interface BetaCodeExecutionResultBlock`

          - `type: "code_execution_result"`

            default: code_execution_result

          - `content: Array<BetaCodeExecutionOutputBlock>`

            - `type: "code_execution_output"`

              default: code_execution_output

            - `file_id: string`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

        - `interface BetaEncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `type: "encrypted_code_execution_result"`

            default: encrypted_code_execution_result

          - `content: Array<BetaCodeExecutionOutputBlock>`

            - `type: "code_execution_output"`

              default: code_execution_output

            - `file_id: string`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `interface BetaBashCodeExecutionToolResultBlock`

      - `type: "bash_code_execution_tool_result"`

        default: bash_code_execution_tool_result

      - `content: BetaBashCodeExecutionToolResultError | BetaBashCodeExecutionResultBlock`

        - `interface BetaBashCodeExecutionToolResultError`

          - `type: "bash_code_execution_tool_result_error"`

            default: bash_code_execution_tool_result_error

          - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

        - `interface BetaBashCodeExecutionResultBlock`

          - `type: "bash_code_execution_result"`

            default: bash_code_execution_result

          - `content: Array<BetaBashCodeExecutionOutputBlock>`

            - `type: "bash_code_execution_output"`

              default: bash_code_execution_output

            - `file_id: string`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `interface BetaTextEditorCodeExecutionToolResultBlock`

      - `type: "text_editor_code_execution_tool_result"`

        default: text_editor_code_execution_tool_result

      - `content: BetaTextEditorCodeExecutionToolResultError | BetaTextEditorCodeExecutionViewResultBlock | BetaTextEditorCodeExecutionCreateResultBlock | BetaTextEditorCodeExecutionStrReplaceResultBlock`

        - `interface BetaTextEditorCodeExecutionToolResultError`

          - `type: "text_editor_code_execution_tool_result_error"`

            default: text_editor_code_execution_tool_result_error

          - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: string | null`

        - `interface BetaTextEditorCodeExecutionViewResultBlock`

          - `type: "text_editor_code_execution_view_result"`

            default: text_editor_code_execution_view_result

          - `content: string`

          - `file_type: "text" | "image" | "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: number | null`

          - `start_line: number | null`

          - `total_lines: number | null`

        - `interface BetaTextEditorCodeExecutionCreateResultBlock`

          - `type: "text_editor_code_execution_create_result"`

            default: text_editor_code_execution_create_result

          - `is_file_update: boolean`

        - `interface BetaTextEditorCodeExecutionStrReplaceResultBlock`

          - `type: "text_editor_code_execution_str_replace_result"`

            default: text_editor_code_execution_str_replace_result

          - `lines: Array<string> | null`

          - `new_lines: number | null`

          - `new_start: number | null`

          - `old_lines: number | null`

          - `old_start: number | null`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `interface BetaToolSearchToolResultBlock`

      - `type: "tool_search_tool_result"`

        default: tool_search_tool_result

      - `content: BetaToolSearchToolResultError | BetaToolSearchToolSearchResultBlock`

        - `interface BetaToolSearchToolResultError`

          - `type: "tool_search_tool_result_error"`

            default: tool_search_tool_result_error

          - `error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: string | null`

        - `interface BetaToolSearchToolSearchResultBlock`

          - `type: "tool_search_tool_search_result"`

            default: tool_search_tool_search_result

          - `tool_references: Array<BetaToolReferenceBlock>`

            - `type: "tool_reference"`

              default: tool_reference

            - `tool_name: string`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `interface BetaMCPToolUseBlock`

      - `type: "mcp_tool_use"`

        default: mcp_tool_use

      - `id: string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `input: Record<string, unknown>`

      - `name: string`

        The name of the MCP tool

      - `server_name: string`

        The name of the MCP server

    - `interface BetaMCPToolResultBlock`

      - `type: "mcp_tool_result"`

        default: mcp_tool_result

      - `content: string | Array<BetaTextBlock>`

        - `string`

        - `Array<BetaTextBlock>`

          - `type: "text"`

            default: text

          - `citations: Array<BetaTextCitation> | null`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `text: string`

            minLength: 0

      - `is_error: boolean`

        default: false

      - `tool_use_id: string`

        pattern: ^[a-zA-Z0-9_-]+$

    - `interface BetaContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `type: "container_upload"`

        default: container_upload

      - `file_id: string`

    - `interface BetaCompactionBlock`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `type: "compaction"`

        default: compaction

      - `content: string | null`

        Summary of compacted content, or null if compaction failed

      - `encrypted_content: string | null`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `signature?: string | null`

        Signature over the summary, to be sent back with the block verbatim

      - `tool_changes?: Array<BetaResponseToolAdditionBlock | BetaResponseToolRemovalBlock> | null`

        The tool changes of the compacted range: the `tool_addition` and `tool_removal` blocks that take the request's `tools` to the tool set in effect at the end of the range, or `[]` when the range changed no tool. Absent when the server did not compute them. Send the block back unchanged.

        - `interface BetaResponseToolAdditionBlock`

          An entry of a `compaction` block's `tool_changes`: a tool the
          compacted range made available, as a reference to a `tools` entry or
          MCP toolset, or as the tool definition in effect at the end of the
          range, by value. Send it back unchanged.

          - `type: "tool_addition"`

            default: tool_addition

          - `tool: BetaResponseToolChangeToolReference | BetaResponseToolChangeMCPToolReference | BetaResponseToolChangeMCPToolsetReference | BetaToolChangeToolDefinition`

            The tool made available: a reference to a `tools` entry or MCP toolset, or a `tool_definition` carrying the definition by value.

            - `interface BetaResponseToolChangeToolReference`

              Reference to a single tool, by the name the model uses to call it, as
              a `compaction` block's `tool_changes` entry reports it: a tool
              declared in `tools` or defined by an earlier `tool_addition` block.
              Send it back unchanged with the block.

              - `type: "tool_reference"`

                default: tool_reference

              - `name: string`

            - `interface BetaResponseToolChangeMCPToolReference`

              Reference to a single MCP tool, by its server and its name on that
              server, as a `compaction` block's `tool_changes` entry reports it.
              Send it back unchanged with the block.

              - `type: "mcp_tool_reference"`

                default: mcp_tool_reference

              - `name: string`

              - `server_name: string`

            - `interface BetaResponseToolChangeMCPToolsetReference`

              Reference to every tool in the named MCP server's toolset, as a
              `compaction` block's `tool_changes` entry reports it. Send it back
              unchanged with the block.

              - `type: "mcp_toolset_reference"`

                default: mcp_toolset_reference

              - `server_name: string`

            - `interface BetaToolChangeToolDefinition`

              A tool defined by value, as a `compaction` block's `tool_changes` entry
              reports it: `definition` is the tool's definition as it was sent, in the
              form of a `tools` entry, without `cache_control`. Send it back unchanged
              with the block.

              - `type: "tool_definition"`

                default: tool_definition

              - `definition: BetaResponseToolUnion`

                - `interface BetaResponseTool`

                  A custom tool definition, as sent.

                  - `type?: "custom" | null`

                  - `input_schema: BetaResponseToolInputSchema`

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

                - `interface BetaToolBash20241022`

                  - `type: "bash_20241022"`

                  - `name: "bash"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

                  - `allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">`

                    - `"direct"`

                    - `"code_execution_20250825"`

                    - `"code_execution_20260120"`

                    - `"code_execution_20260521"`

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

                  - `defer_loading?: boolean`

                    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

                  - `input_examples?: Array<Record<string, unknown>>`

                  - `strict?: boolean`

                    When true, guarantees schema validation on tool names and inputs

                - `interface BetaToolBash20250124`

                  - `type: "bash_20250124"`

                  - `name: "bash"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaCodeExecutionTool20250522`

                  - `type: "code_execution_20250522"`

                  - `name: "code_execution"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaCodeExecutionTool20250825`

                  - `type: "code_execution_20250825"`

                  - `name: "code_execution"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaCodeExecutionTool20260120`

                  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

                  - `type: "code_execution_20260120"`

                  - `name: "code_execution"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaCodeExecutionTool20260521`

                  Code execution tool with REPL state persistence.

                  - `type: "code_execution_20260521"`

                  - `name: "code_execution"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaBrowserToolset20260801`

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

                    - `type?: BetaBrowserTypeConfig | null`

                      `type`'s config overrides.

                      - `defer_loading?: boolean | null`

                        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                      - `enabled?: boolean | null`

                        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

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

                - `interface BetaToolComputerUse20241022`

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

                - `interface BetaMemoryTool20250818`

                  - `type: "memory_20250818"`

                  - `name: "memory"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaToolComputerUse20250124`

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

                - `interface BetaToolTextEditor20241022`

                  - `type: "text_editor_20241022"`

                  - `name: "str_replace_editor"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaToolComputerUse20251124`

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

                - `interface BetaComputerToolset20260801`

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

                    - `type?: BetaComputerTypeConfig | null`

                      `type`'s config overrides.

                      - `defer_loading?: boolean | null`

                        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

                      - `enabled?: boolean | null`

                        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

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

                - `interface BetaToolTextEditor20250124`

                  - `type: "text_editor_20250124"`

                  - `name: "str_replace_editor"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaToolTextEditor20250429`

                  - `type: "text_editor_20250429"`

                  - `name: "str_replace_based_edit_tool"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaToolTextEditor20250728`

                  - `type: "text_editor_20250728"`

                  - `name: "str_replace_based_edit_tool"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaWebSearchTool20250305`

                  - `type: "web_search_20250305"`

                  - `name: "web_search"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaWebFetchTool20250910`

                  - `type: "web_fetch_20250910"`

                  - `name: "web_fetch"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                    - `enabled?: boolean`

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

                  - `url_sources?: BetaWebFetchURLSources | null`

                    Which sources contribute to the set of URLs web fetch may fetch.

                    Each key is a tagged variant: `user_input` is `all` or `none`; the
                    two tool filters are `all`, `none`, `only` (only the named tools'
                    results) or `except` (every result but the named tools'). A named tool
                    must be declared in this request's `tools[]`.

                    - `client_tool_results?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone | BetaWebFetchURLSourceOnly | BetaWebFetchURLSourceExcept`

                      Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

                      - `interface BetaWebFetchURLSourceAll`

                        The `url_sources` variant under which a source contributes in
                        full: every result of the tool filter's source, or all user input.

                        - `type: "all"`

                      - `interface BetaWebFetchURLSourceNone`

                        The `url_sources` variant under which a source contributes nothing:
                        no result of the tool filter's source, or no user input.

                        - `type: "none"`

                      - `interface BetaWebFetchURLSourceOnly`

                        The tool filter variant under which only the named tools' results
                        contribute.

                        - `type: "only"`

                        - `tools: Array<BetaWebFetchURLSourceToolReference>`

                          - `type: "tool_reference"`

                          - `name: string`

                      - `interface BetaWebFetchURLSourceExcept`

                        The tool filter variant under which every result but the named
                        tools' contributes.

                        - `type: "except"`

                        - `tools: Array<BetaWebFetchURLSourceToolReference>`

                          - `type: "tool_reference"`

                          - `name: string`

                    - `server_tool_results?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone | BetaWebFetchURLSourceOnly | BetaWebFetchURLSourceExcept`

                      Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

                      - `interface BetaWebFetchURLSourceAll`

                        The `url_sources` variant under which a source contributes in
                        full: every result of the tool filter's source, or all user input.

                      - `interface BetaWebFetchURLSourceNone`

                        The `url_sources` variant under which a source contributes nothing:
                        no result of the tool filter's source, or no user input.

                      - `interface BetaWebFetchURLSourceOnly`

                        The tool filter variant under which only the named tools' results
                        contribute.

                      - `interface BetaWebFetchURLSourceExcept`

                        The tool filter variant under which every result but the named
                        tools' contributes.

                    - `user_input?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone`

                      Whether URLs in user messages are fetchable: "all" or "none".

                      - `interface BetaWebFetchURLSourceAll`

                        The `url_sources` variant under which a source contributes in
                        full: every result of the tool filter's source, or all user input.

                      - `interface BetaWebFetchURLSourceNone`

                        The `url_sources` variant under which a source contributes nothing:
                        no result of the tool filter's source, or no user input.

                - `interface BetaWebSearchTool20260209`

                  - `type: "web_search_20260209"`

                  - `name: "web_search"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaWebFetchTool20260209`

                  - `type: "web_fetch_20260209"`

                  - `name: "web_fetch"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                  - `url_sources?: BetaWebFetchURLSources | null`

                    Which sources contribute to the set of URLs web fetch may fetch.

                    Each key is a tagged variant: `user_input` is `all` or `none`; the
                    two tool filters are `all`, `none`, `only` (only the named tools'
                    results) or `except` (every result but the named tools'). A named tool
                    must be declared in this request's `tools[]`.

                - `interface BetaWebFetchTool20260309`

                  Web fetch tool with use_cache parameter for bypassing cached content.

                  - `type: "web_fetch_20260309"`

                  - `name: "web_fetch"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                  - `url_sources?: BetaWebFetchURLSources | null`

                    Which sources contribute to the set of URLs web fetch may fetch.

                    Each key is a tagged variant: `user_input` is `all` or `none`; the
                    two tool filters are `all`, `none`, `only` (only the named tools'
                    results) or `except` (every result but the named tools'). A named tool
                    must be declared in this request's `tools[]`.

                  - `use_cache?: boolean`

                    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                - `interface BetaWebSearchTool20260318`

                  - `type: "web_search_20260318"`

                  - `name: "web_search"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaWebFetchTool20260318`

                  - `type: "web_fetch_20260318"`

                  - `name: "web_fetch"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                  - `url_sources?: BetaWebFetchURLSources | null`

                    Which sources contribute to the set of URLs web fetch may fetch.

                    Each key is a tagged variant: `user_input` is `all` or `none`; the
                    two tool filters are `all`, `none`, `only` (only the named tools'
                    results) or `except` (every result but the named tools'). A named tool
                    must be declared in this request's `tools[]`.

                  - `use_cache?: boolean`

                    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

                - `interface BetaAdvisorTool20260301`

                  - `type: "advisor_20260301"`

                  - `model: Model`

                    The model that will complete your prompt.

                    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                    - `"claude-fable-5-1" | "claude-opus-5-5" | "claude-mythos-5-1" | 15 more`

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

                    - `(string & {})`

                  - `name: "advisor"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaToolSearchToolBm25_20251119`

                  - `type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25"`

                    - `"tool_search_tool_bm25_20251119"`

                    - `"tool_search_tool_bm25"`

                  - `name: "tool_search_tool_bm25"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaToolSearchToolRegex20251119`

                  - `type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex"`

                    - `"tool_search_tool_regex_20251119"`

                    - `"tool_search_tool_regex"`

                  - `name: "tool_search_tool_regex"`

                    Name of the tool.

                    This is how the tool will be called by the model and in `tool_use` blocks.

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

                - `interface BetaMCPToolset`

                  Configuration for a group of tools from an MCP server.

                  Allows configuring enabled status and defer_loading for all tools
                  from an MCP server, with optional per-tool overrides.

                  - `type: "mcp_toolset"`

                  - `mcp_server_name: string`

                    Name of the MCP server to configure tools for

                    maxLength: 255, minLength: 1

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

                  - `tools?: Array<BetaMCPToolParam> | null`

                    The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

                    - `input_schema: Record<string, unknown>`

                      The tool's input schema as the MCP server lists it, verbatim.

                    - `name: string`

                      The tool's name as the MCP server lists it (not prefixed with the server name).

                      minLength: 1

                    - `description?: string | null`

                      The tool's description as the MCP server lists it.

        - `interface BetaResponseToolRemovalBlock`

          An entry of a `compaction` block's `tool_changes`: a tool of the
          request's `tools` (or an MCP tool or toolset) that the compacted range
          withdrew. Send it back unchanged.

          - `type: "tool_removal"`

            default: tool_removal

          - `tool: BetaResponseToolChangeToolReference | BetaResponseToolChangeMCPToolReference | BetaResponseToolChangeMCPToolsetReference`

            A reference to the withdrawn `tools` entry, MCP tool or MCP toolset.

            - `interface BetaResponseToolChangeToolReference`

              Reference to a single tool, by the name the model uses to call it, as
              a `compaction` block's `tool_changes` entry reports it: a tool
              declared in `tools` or defined by an earlier `tool_addition` block.
              Send it back unchanged with the block.

            - `interface BetaResponseToolChangeMCPToolReference`

              Reference to a single MCP tool, by its server and its name on that
              server, as a `compaction` block's `tool_changes` entry reports it.
              Send it back unchanged with the block.

            - `interface BetaResponseToolChangeMCPToolsetReference`

              Reference to every tool in the named MCP server's toolset, as a
              `compaction` block's `tool_changes` entry reports it. Send it back
              unchanged with the block.

    - `interface BetaFallbackBlock`

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

        - `category: "cyber" | "bio" | "frontier_llm" | 2 more | null`

          The policy category that triggered a refusal.

          - `cyber` - The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.
          - `bio` - The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.
          - `frontier_llm` - The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.
          - `reasoning_extraction` - The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).
          - `general_harms` - The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

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

    - `interface BetaMCPToolListingBlock`

      The tool listing the server fetched from an MCP server while producing
      this response. Send the assistant message back unchanged, this block
      included, so later requests use this listing instead of asking the MCP
      server again.

      - `type: "mcp_tool_listing"`

        default: mcp_tool_listing

      - `mcp_server_name: string`

      - `tools: Array<BetaMCPTool>`

        - `input_schema: Record<string, unknown>`

        - `name: string`

        - `description?: string`

  - `context_management: BetaContextManagementResponse | null`

    Context management response.

    Information about context management strategies applied during the request.

    - `applied_edits: Array<BetaClearToolUses20250919EditResponse | BetaClearThinking20251015EditResponse>`

      List of context management edits that were applied.

      - `interface BetaClearToolUses20250919EditResponse`

        - `type: "clear_tool_uses_20250919"`

          The type of context management edit applied.

          default: clear_tool_uses_20250919

        - `cleared_input_tokens: number`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `cleared_tool_uses: number`

          Number of tool uses that were cleared.

          minimum: 0

      - `interface BetaClearThinking20251015EditResponse`

        - `type: "clear_thinking_20251015"`

          The type of context management edit applied.

          default: clear_thinking_20251015

        - `cleared_input_tokens: number`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `cleared_thinking_turns: number`

          Number of thinking turns that were cleared.

          minimum: 0

  - `diagnostics: BetaDiagnostics | null`

    Request-level diagnostics: why the prompt cache could not fully reuse
    the prefix of the request named by `diagnostics.previous_message_id`.

    - `cache_miss_reason: BetaCacheMissModelChanged | BetaCacheMissSystemChanged | BetaCacheMissToolsChanged | 3 more | null`

      Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

      - `interface BetaCacheMissModelChanged`

        - `type: "model_changed"`

          default: model_changed

        - `cache_missed_input_tokens: number`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

      - `interface BetaCacheMissSystemChanged`

        - `type: "system_changed"`

          default: system_changed

        - `cache_missed_input_tokens: number`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

      - `interface BetaCacheMissToolsChanged`

        - `type: "tools_changed"`

          default: tools_changed

        - `cache_missed_input_tokens: number`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

      - `interface BetaCacheMissMessagesChanged`

        - `type: "messages_changed"`

          default: messages_changed

        - `cache_missed_input_tokens: number`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

      - `interface BetaCacheMissPreviousMessageNotFound`

        - `type: "previous_message_not_found"`

          default: previous_message_not_found

      - `interface BetaCacheMissUnavailable`

        - `type: "unavailable"`

          default: unavailable

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `role: "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    default: assistant

  - `stop_details: BetaRefusalStopDetails | null`

    Structured information about a refusal.

    - `type: "refusal"`

      default: refusal

    - `category: "cyber" | "bio" | "frontier_llm" | 2 more | null`

      The policy category that triggered a refusal.

      - `cyber` - The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.
      - `bio` - The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.
      - `frontier_llm` - The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.
      - `reasoning_extraction` - The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).
      - `general_harms` - The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

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

    - `explanation: string | null`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `fallback_credit_token: string | null`

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

    - `fallback_has_prefill_claim: boolean | null`

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

    - `recommended_model: string | null`

      The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

  - `stop_reason: BetaStopReason | null`

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

  - `stop_sequence: string | null`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `usage: BetaUsage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: BetaCacheCreation | null`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

        default: 0, minimum: 0

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

        default: 0, minimum: 0

    - `cache_creation_input_tokens: number | null`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `cache_read_input_tokens: number | null`

      The number of input tokens read from the cache.

      minimum: 0

    - `fallback_credit: BetaFallbackCreditUsage | null`

      Outcome of the `fallback_credit_token` presented on this request.

      - `status: BetaFallbackCreditRedeemed | BetaFallbackCreditNotApplied`

        Whether the fallback-credit reprice was applied to this response's billing.

        A union discriminated on `type`. `redeemed`: the retry is billed as if
        the conversation had been on the retry model all along — including when the
        resulting shift is zero because there was nothing to move. `not_applied`:
        no reprice was applied; the arm's `reason` says why.

        - `interface BetaFallbackCreditRedeemed`

          The reprice was applied: the retry is billed as if the conversation
          had been on the retry model all along.

          - `type: "redeemed"`

            default: redeemed

        - `interface BetaFallbackCreditNotApplied`

          No reprice was applied; `reason` says why.

          - `type: "not_applied"`

            default: not_applied

          - `reason: "body_mismatch" | "continuation_excluded" | "continuation_only" | 9 more`

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

          - `remove_to_redeem?: Array<string> | null`

            Request fields to remove before retrying, so the retry can redeem this
            token.

            Present exactly when `reason` is `variant_fields_present` — never null,
            never an empty array; absent otherwise. Fields are named only from your own request, and only after
            the sealed variant hash matched. A served best-effort retry has already
            been billed at normal price; nothing redeems retroactively, but a corrected
            re-send inside the token's five-minute window can still redeem.

    - `inference_geo: string | null`

      The geographic region where inference was performed for this request.

    - `input_tokens: number`

      The number of input tokens which were used.

      minimum: 0

    - `iterations: BetaIterationsUsage | null`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the context window size from the last `message` entry
      - Understand token accumulation across server-side tool use loops

      A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `interface BetaMessageIterationUsage`

        Token usage for a sampling iteration.

        - `type: "message"`

          Usage for a sampling iteration

          default: message

        - `cache_creation: BetaCacheCreation | null`

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

        - `model: Model | null`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `output_tokens: number`

          The number of output tokens which were used.

          minimum: 0

      - `interface BetaCompactionIterationUsage`

        Token usage for a compaction iteration.

        - `type: "compaction"`

          Usage for a compaction iteration

          default: compaction

        - `cache_creation: BetaCacheCreation | null`

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

      - `interface BetaAdvisorMessageIterationUsage`

        Token usage for an advisor sub-inference iteration.

        - `type: "advisor_message"`

          Usage for an advisor sub-inference iteration

          default: advisor_message

        - `cache_creation: BetaCacheCreation | null`

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

      - `interface BetaFallbackMessageIterationUsage`

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

        - `cache_creation: BetaCacheCreation | null`

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

    - `output_tokens_details: BetaOutputTokensDetails | null`

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

    - `server_tool_use: BetaServerToolUsage | null`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

        default: 0, minimum: 0

      - `web_search_requests: number`

        The number of web search tool requests.

        default: 0, minimum: 0

    - `service_tier: "standard" | "priority" | "batch" | null`

      If the request used the priority, standard, or batch tier.

      - `"standard"`

      - `"priority"`

      - `"batch"`

    - `speed: "standard" | "fast" | null`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `input_transformations?: Array<BetaInputTransformation> | null`

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

    - `interface BetaThinkingDroppedInputTransformation`

      - `type: "thinking_dropped"`

        Always `thinking_dropped` for this entry type.

        default: thinking_dropped

      - `path: string`

        Where the removed block was in your request, as `messages.{i}.content.{j}`:
        `i` indexes the `messages` array you sent and `j` that message's `content`
        array — the same form error messages use.

      - `reason: "model_binding_mismatch" | "prefix_binding_mismatch" | "organization_binding_mismatch" | "end_user_binding_mismatch"`

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

    - `interface BetaThinkingMismatchAllowedInputTransformation`

      - `type: "thinking_mismatch_allowed"`

        Always `thinking_mismatch_allowed` for this entry type.

        default: thinking_mismatch_allowed

      - `path: string`

        Where the block is in your request, as `messages.{i}.content.{j}`:
        `i` indexes the `messages` array you sent and `j` that message's `content`
        array — the same form error messages use.

      - `reason: "model_binding_mismatch" | "prefix_binding_mismatch" | "organization_binding_mismatch" | "end_user_binding_mismatch"`

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

- `type BetaRawMessageStreamEvent = BetaRawMessageStartEvent | BetaRawMessageDeltaEvent | BetaRawMessageStopEvent | 3 more`

  - `interface BetaRawMessageStartEvent`

    - `type: "message_start"`

      default: message_start

    - `message: BetaMessage`

  - `interface BetaRawMessageDeltaEvent`

    - `type: "message_delta"`

      default: message_delta

    - `context_management: BetaContextManagementResponse | null`

      Information about context management strategies applied during the request

    - `delta: Delta`

      - `container: BetaContainer | null`

        Information about the container used in the request (for the code execution tool)

      - `stop_details: BetaRefusalStopDetails | null`

        Structured information about a refusal.

      - `stop_reason: BetaStopReason | null`

      - `stop_sequence: string | null`

    - `usage: BetaMessageDeltaUsage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation_input_tokens: number | null`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `cache_read_input_tokens: number | null`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `fallback_credit: BetaFallbackCreditUsage | null`

        Outcome of the `fallback_credit_token` presented on this request.

      - `input_tokens: number | null`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `iterations: BetaIterationsUsage | null`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the context window size from the last `message` entry
        - Understand token accumulation across server-side tool use loops

        A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `output_tokens: number`

        The cumulative number of output tokens which were used.

      - `output_tokens_details: BetaOutputTokensDetails | null`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `server_tool_use: BetaServerToolUsage | null`

        The number of server tool requests.

    - `input_transformations?: Array<BetaInputTransformation> | null`

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

      - `interface BetaThinkingDroppedInputTransformation`

      - `interface BetaThinkingMismatchAllowedInputTransformation`

  - `interface BetaRawMessageStopEvent`

    - `type: "message_stop"`

      default: message_stop

  - `interface BetaRawContentBlockStartEvent`

    - `type: "content_block_start"`

      default: content_block_start

    - `content_block: BetaTextBlock | BetaThinkingBlock | BetaRedactedThinkingBlock | 15 more`

      - `interface BetaTextBlock`

      - `interface BetaThinkingBlock`

      - `interface BetaRedactedThinkingBlock`

      - `interface BetaToolUseBlock`

      - `interface BetaServerToolUseBlock`

      - `interface BetaWebSearchToolResultBlock`

      - `interface BetaWebFetchToolResultBlock`

      - `interface BetaAdvisorToolResultBlock`

      - `interface BetaCodeExecutionToolResultBlock`

      - `interface BetaBashCodeExecutionToolResultBlock`

      - `interface BetaTextEditorCodeExecutionToolResultBlock`

      - `interface BetaToolSearchToolResultBlock`

      - `interface BetaMCPToolUseBlock`

      - `interface BetaMCPToolResultBlock`

      - `interface BetaContainerUploadBlock`

        Response model for a file uploaded to the container.

      - `interface BetaCompactionBlock`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

      - `interface BetaFallbackBlock`

        Marks the point in `content` where one model's output gives way to the next.

        One block appears per hop where a preceding model actually ran this turn and
        declined. A turn where no preceding model ran and declined has no such
        boundary and carries no block — the signal for whether a fallback model
        served the response is the presence of a `fallback_message` entry in
        `usage.iterations`, not this block.

        The block is treated like a server-tool content block for streaming: it
        arrives via the standard `content_block_start` / `content_block_stop`
        pair and carries no deltas.

      - `interface BetaMCPToolListingBlock`

        The tool listing the server fetched from an MCP server while producing
        this response. Send the assistant message back unchanged, this block
        included, so later requests use this listing instead of asking the MCP
        server again.

    - `index: number`

  - `interface BetaRawContentBlockDeltaEvent`

    - `type: "content_block_delta"`

      default: content_block_delta

    - `delta: BetaRawContentBlockDelta`

      - `interface BetaTextDelta`

        - `type: "text_delta"`

          default: text_delta

        - `text: string`

      - `interface BetaInputJSONDelta`

        - `type: "input_json_delta"`

          default: input_json_delta

        - `partial_json: string`

      - `interface BetaCitationsDelta`

        - `type: "citations_delta"`

          default: citations_delta

        - `citation: BetaCitationCharLocation | BetaCitationPageLocation | BetaCitationContentBlockLocation | 2 more`

          - `interface BetaCitationCharLocation`

          - `interface BetaCitationPageLocation`

          - `interface BetaCitationContentBlockLocation`

          - `interface BetaCitationsWebSearchResultLocation`

          - `interface BetaCitationSearchResultLocation`

      - `interface BetaThinkingDelta`

        - `type: "thinking_delta"`

          default: thinking_delta

        - `estimated_tokens: number | null`

          Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

        - `thinking: string`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

      - `interface BetaSignatureDelta`

        - `type: "signature_delta"`

          default: signature_delta

        - `signature: string`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

      - `interface BetaCompactionContentBlockDelta`

        - `type: "compaction_delta"`

          default: compaction_delta

        - `content: string | null`

        - `encrypted_content: string | null`

          Opaque metadata from prior compaction, to be round-tripped verbatim

    - `index: number`

  - `interface BetaRawContentBlockStopEvent`

    - `type: "content_block_stop"`

      default: content_block_stop

    - `index: number`

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaMessage = await client.beta.messages.create({
  max_tokens: 1024,
  messages: [{ content: "Hello, world", role: "user" }],
  model: "claude-opus-5"
});

console.log(betaMessage.id);
```

### Response (200)

```json
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": [
        {
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "fallback_credit_token": "QW50aHJvcGljL0NsYXVkZQ==",
    "fallback_has_prefill_claim": true,
    "recommended_model": "claude-opus-4-8",
    "type": "refusal"
  },
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "fallback_credit": {
      "status": {
        "type": "redeemed"
      }
    },
    "inference_geo": "global",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "model": "claude-fable-5-1",
        "output_tokens": 0,
        "type": "message"
      }
    ],
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  },
  "input_transformations": [
    {
      "path": "path",
      "reason": "model_binding_mismatch",
      "type": "thinking_dropped"
    }
  ]
}
```
