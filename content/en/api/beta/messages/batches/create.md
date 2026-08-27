# Create a Message Batch

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

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

- `"anthropic-user-profile-id": optional string`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

## Body parameters

- `requests: array of object`

  List of requests for prompt completion. Each is an individual request to create a Message.

  maxItems: 100000, minItems: 1

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

  - `params: object`

    Messages API creation parameters for the individual request.

    See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

    - `max_tokens: number`

      The maximum number of tokens to generate before stopping.

      Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

      Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

      Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

      minimum: 0

    - `messages: array of BetaMessageParam`

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

      - `content: string or array of BetaContentBlockParam`

        - `string`

        - `array of BetaContentBlockParam`

          - `BetaTextBlockParam object`

            - `text: string`

              minLength: 1

            - `type: "text"`

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

            - `citations: optional array of BetaTextCitationParam or null`

              - `BetaCitationCharLocationParam object`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string or null`

                  maxLength: 500, minLength: 1

                - `end_char_index: number`

                - `start_char_index: number`

                  minimum: 0

                - `type: "char_location"`

              - `BetaCitationPageLocationParam object`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string or null`

                  maxLength: 500, minLength: 1

                - `end_page_number: number`

                - `start_page_number: number`

                  minimum: 1

                - `type: "page_location"`

              - `BetaCitationContentBlockLocationParam object`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                  minimum: 0

                - `document_title: string or null`

                  maxLength: 500, minLength: 1

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `type: "content_block_location"`

              - `BetaCitationWebSearchResultLocationParam object`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string or null`

                  maxLength: 512, minLength: 1

                - `type: "web_search_result_location"`

                - `url: string`

                  minLength: 1

              - `BetaCitationSearchResultLocationParam object`

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

                - `type: "search_result_location"`

          - `BetaImageBlockParam object`

            - `source: BetaBase64ImageSource or BetaURLImageSource or BetaFileImageSource`

              - `BetaBase64ImageSource object`

                - `data: string`

                  format: byte

                - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

                - `type: "base64"`

              - `BetaURLImageSource object`

                - `type: "url"`

                - `url: string`

              - `BetaFileImageSource object`

                - `file_id: string`

                - `type: "file"`

            - `type: "image"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `transformations: optional BetaImageTransformationsParam or null`

              Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

              - `oversized_image: optional "downsize" or "error"`

                What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                - `"downsize"`

                - `"error"`

          - `BetaRequestDocumentBlock object`

            - `source: BetaBase64PDFSource or BetaPlainTextSource or BetaContentBlockSource or 2 more`

              - `BetaBase64PDFSource object`

                - `data: string`

                  format: byte

                - `media_type: "application/pdf"`

                - `type: "base64"`

              - `BetaPlainTextSource object`

                - `data: string`

                - `media_type: "text/plain"`

                - `type: "text"`

              - `BetaContentBlockSource object`

                - `content: string or array of BetaContentBlockSourceContent`

                  - `string`

                  - `BetaContentBlockSourceContent = array of BetaContentBlockSourceContent`

                    - `BetaTextBlockParam object`

                    - `BetaImageBlockParam object`

                - `type: "content"`

              - `BetaURLPDFSource object`

                - `type: "url"`

                - `url: string`

              - `BetaFileDocumentSource object`

                - `file_id: string`

                - `type: "file"`

            - `type: "document"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `citations: optional BetaCitationsConfigParam or null`

              - `enabled: optional boolean`

            - `context: optional string or null`

              minLength: 1

            - `title: optional string or null`

              maxLength: 500, minLength: 1

          - `BetaSearchResultBlockParam object`

            - `content: array of BetaTextBlockParam`

              - `text: string`

                minLength: 1

              - `type: "text"`

              - `cache_control: optional BetaCacheControlEphemeral or null`

                Create a cache control breakpoint at this content block.

              - `citations: optional array of BetaTextCitationParam or null`

            - `source: string`

            - `title: string`

            - `type: "search_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `citations: optional BetaCitationsConfigParam`

          - `BetaThinkingBlockParam object`

            - `signature: string`

              The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

              Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

            - `thinking: string`

              The `thinking` text of this block as returned by the API.

            - `type: "thinking"`

          - `BetaRedactedThinkingBlockParam object`

            - `data: string`

              The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

            - `type: "redacted_thinking"`

          - `BetaToolUseBlockParam object`

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: map[unknown]`

            - `name: string`

              maxLength: 200, minLength: 1

            - `type: "tool_use"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `type: "code_execution_20250825"`

              - `BetaServerToolCaller20260120 object`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `type: "code_execution_20260120"`

            - `toolset_name: optional string or null`

              For a toolset member tool_use, the toolset family this member belongs to.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `BetaToolResultBlockParam object`

            - `tool_use_id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `type: "tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `content: optional string or array of BetaTextBlockParam or BetaImageBlockParam or BetaSearchResultBlockParam or 3 more`

              - `string`

              - `array of BetaTextBlockParam or BetaImageBlockParam or BetaSearchResultBlockParam or 3 more`

                - `BetaTextBlockParam object`

                - `BetaImageBlockParam object`

                - `BetaSearchResultBlockParam object`

                - `BetaRequestDocumentBlock object`

                - `BetaToolReferenceBlockParam object`

                  Tool reference block that can be included in tool_result content.

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `type: "tool_reference"`

                  - `cache_control: optional BetaCacheControlEphemeral or null`

                    Create a cache control breakpoint at this content block.

                - `BetaBrowserStateBlockParam object`

                  The caller's browser state after a browser toolset member call —
                  the full inventory of open tabs, which tab is active, and any side
                  effects (tabs opened, download state changes) the call produced.

                  At most one per `tool_result`, only on a non-error result answering a
                  browser toolset member `tool_use`. The server renders the
                  model-visible text from it; the model never sees the raw fields.

                  - `tabs: array of BetaBrowserStateTabEntry`

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

                    - `active: optional boolean`

                      Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                  - `type: "browser_state"`

                  - `cache_control: optional BetaCacheControlEphemeral or null`

                    Create a cache control breakpoint at this content block.

                  - `state_changes: optional array of BetaBrowserStateChange or null`

                    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                    maxItems: 200, minItems: 1

                    - `BetaBrowserStateChangeTabOpened object`

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

                    - `BetaBrowserStateChangeDownloadStarted object`

                      A file download that started during this call.

                      - `download_id: string`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type: "download_started"`

                      - `url: string`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `BetaBrowserStateChangeDownloadCompleted object`

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

                      - `path: optional string or null`

                        Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                      - `size_bytes: optional number or null`

                        The completed download's size.

                        minimum: 0

                    - `BetaBrowserStateChangeDownloadFailed object`

                      A file download that failed — or was cancelled — during this call.

                      - `download_id: string`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type: "download_failed"`

                      - `url: string`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `error: optional string or null`

                        The failure or cancellation detail, when known.

                        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

            - `is_error: optional boolean`

            - `toolset_name: optional string or null`

              For a toolset member tool_result, the toolset family of the paired tool_use.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `BetaServerToolUseBlockParam object`

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

            - `type: "server_tool_use"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

              - `BetaServerToolCaller20260120 object`

          - `BetaWebSearchToolResultBlockParam object`

            - `content: BetaWebSearchToolResultBlockParamContent`

              - `ResultBlock = array of BetaWebSearchResultBlockParam`

                - `encrypted_content: string`

                - `title: string`

                - `type: "web_search_result"`

                - `url: string`

                - `page_age: optional string or null`

              - `BetaWebSearchToolRequestError object`

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

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

              - `BetaServerToolCaller20260120 object`

          - `BetaWebFetchToolResultBlockParam object`

            - `content: BetaWebFetchToolResultErrorBlockParam or BetaWebFetchBlockParam`

              - `BetaWebFetchToolResultErrorBlockParam object`

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

              - `BetaWebFetchBlockParam object`

                - `content: BetaRequestDocumentBlock`

                - `type: "web_fetch_result"`

                - `url: string`

                  Fetched content URL

                - `retrieved_at: optional string or null`

                  ISO 8601 timestamp when the content was retrieved

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: "web_fetch_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `caller: optional BetaDirectCaller or BetaServerToolCaller or BetaServerToolCaller20260120`

              Tool invocation directly from the model.

              - `BetaDirectCaller object`

                Tool invocation directly from the model.

              - `BetaServerToolCaller object`

                Tool invocation generated by a server-side tool.

              - `BetaServerToolCaller20260120 object`

          - `BetaAdvisorToolResultBlockParam object`

            - `content: BetaAdvisorToolResultErrorParam or BetaAdvisorResultBlockParam or BetaAdvisorRedactedResultBlockParam`

              - `BetaAdvisorToolResultErrorParam object`

                - `error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more`

                  - `"max_uses_exceeded"`

                  - `"prompt_too_long"`

                  - `"too_many_requests"`

                  - `"overloaded"`

                  - `"unavailable"`

                  - `"execution_time_exceeded"`

                  - `"model_not_found"`

                - `type: "advisor_tool_result_error"`

              - `BetaAdvisorResultBlockParam object`

                - `text: string`

                - `type: "advisor_result"`

                - `stop_reason: optional string or null`

              - `BetaAdvisorRedactedResultBlockParam object`

                - `encrypted_content: string`

                  Opaque blob produced by a prior response; must be round-tripped verbatim.

                - `type: "advisor_redacted_result"`

                - `stop_reason: optional string or null`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: "advisor_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaCodeExecutionToolResultBlockParam object`

            - `content: BetaCodeExecutionToolResultBlockParamContent`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `BetaCodeExecutionToolResultErrorParam object`

                - `error_code: BetaCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "code_execution_tool_result_error"`

              - `BetaCodeExecutionResultBlockParam object`

                - `content: array of BetaCodeExecutionOutputBlockParam`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "code_execution_result"`

              - `BetaEncryptedCodeExecutionResultBlockParam object`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: array of BetaCodeExecutionOutputBlockParam`

                  - `file_id: string`

                  - `type: "code_execution_output"`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

                - `type: "encrypted_code_execution_result"`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: "code_execution_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaBashCodeExecutionToolResultBlockParam object`

            - `content: BetaBashCodeExecutionToolResultErrorParam or BetaBashCodeExecutionResultBlockParam`

              - `BetaBashCodeExecutionToolResultErrorParam object`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: "bash_code_execution_tool_result_error"`

              - `BetaBashCodeExecutionResultBlockParam object`

                - `content: array of BetaBashCodeExecutionOutputBlockParam`

                  - `file_id: string`

                  - `type: "bash_code_execution_output"`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

                - `type: "bash_code_execution_result"`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: "bash_code_execution_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaTextEditorCodeExecutionToolResultBlockParam object`

            - `content: BetaTextEditorCodeExecutionToolResultErrorParam or BetaTextEditorCodeExecutionViewResultBlockParam or BetaTextEditorCodeExecutionCreateResultBlockParam or BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

              - `BetaTextEditorCodeExecutionToolResultErrorParam object`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `type: "text_editor_code_execution_tool_result_error"`

                - `error_message: optional string or null`

              - `BetaTextEditorCodeExecutionViewResultBlockParam object`

                - `content: string`

                - `file_type: "text" or "image" or "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `type: "text_editor_code_execution_view_result"`

                - `num_lines: optional number or null`

                - `start_line: optional number or null`

                - `total_lines: optional number or null`

              - `BetaTextEditorCodeExecutionCreateResultBlockParam object`

                - `is_file_update: boolean`

                - `type: "text_editor_code_execution_create_result"`

              - `BetaTextEditorCodeExecutionStrReplaceResultBlockParam object`

                - `type: "text_editor_code_execution_str_replace_result"`

                - `lines: optional array of string or null`

                - `new_lines: optional number or null`

                - `new_start: optional number or null`

                - `old_lines: optional number or null`

                - `old_start: optional number or null`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: "text_editor_code_execution_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaToolSearchToolResultBlockParam object`

            - `content: BetaToolSearchToolResultErrorParam or BetaToolSearchToolSearchResultBlockParam`

              - `BetaToolSearchToolResultErrorParam object`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: "tool_search_tool_result_error"`

                - `error_message: optional string or null`

              - `BetaToolSearchToolSearchResultBlockParam object`

                - `tool_references: array of BetaToolReferenceBlockParam`

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `type: "tool_reference"`

                  - `cache_control: optional BetaCacheControlEphemeral or null`

                    Create a cache control breakpoint at this content block.

                - `type: "tool_search_tool_search_result"`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: "tool_search_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaMCPToolUseBlockParam object`

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: map[unknown]`

            - `name: string`

            - `server_name: string`

              The name of the MCP server

            - `type: "mcp_tool_use"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaRequestMCPToolResultBlockParam object`

            - `tool_use_id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `type: "mcp_tool_result"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `content: optional string or array of BetaTextBlockParam`

              - `string`

              - `BetaMCPToolResultBlockParamContent = array of BetaTextBlockParam`

                - `text: string`

                  minLength: 1

                - `type: "text"`

                - `cache_control: optional BetaCacheControlEphemeral or null`

                  Create a cache control breakpoint at this content block.

                - `citations: optional array of BetaTextCitationParam or null`

            - `is_error: optional boolean`

          - `BetaContainerUploadBlockParam object`

            A content block that represents a file to be uploaded to the container
            Files uploaded via this block will be available in the container's input directory.

            - `file_id: string`

            - `type: "container_upload"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaCompactionBlockParam object`

            A compaction block containing summary of previous context.

            Users should round-trip these blocks from responses to subsequent requests
            to maintain context across compaction boundaries.

            When content is None, the block represents a failed compaction. The server
            treats these as no-ops. Empty string content is not allowed.

            - `type: "compaction"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

            - `content: optional string or null`

              Summary of previously compacted content, or null if compaction failed

            - `encrypted_content: optional string or null`

              Opaque metadata from prior compaction, to be round-tripped verbatim

          - `BetaRequestToolAdditionBlock object`

            Mid-conversation directive to surface a declared tool.

            `tool` references a tool (or MCP toolset) by name from the request's
            `tools`; it is offered to the model from this point in the
            conversation onward.

            - `tool: BetaToolChangeToolReference or BetaToolChangeMCPToolReference or BetaToolChangeMCPToolsetReference`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `BetaToolChangeToolReference object`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

                - `name: string`

                  pattern: ^[a-zA-Z0-9_-]{1,128}$

                - `type: "tool_reference"`

              - `BetaToolChangeMCPToolReference object`

                Reference to a single MCP tool by its server and remote name — the
                same `server_name`/`name` pair `mcp_tool_use` carries.

                - `name: string`

                - `server_name: string`

                - `type: "mcp_tool_reference"`

              - `BetaToolChangeMCPToolsetReference object`

                Reference to every tool in the named MCP server's toolset.

                - `server_name: string`

                - `type: "mcp_toolset_reference"`

            - `type: "tool_addition"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaRequestToolRemovalBlock object`

            Mid-conversation directive to withdraw a tool.

            `tool` references a tool (or MCP toolset) by name from the request's
            `tools`; it is no longer offered to the model from this point in the
            conversation onward.

            - `tool: BetaToolChangeToolReference or BetaToolChangeMCPToolReference or BetaToolChangeMCPToolsetReference`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `BetaToolChangeToolReference object`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

              - `BetaToolChangeMCPToolReference object`

                Reference to a single MCP tool by its server and remote name — the
                same `server_name`/`name` pair `mcp_tool_use` carries.

              - `BetaToolChangeMCPToolsetReference object`

                Reference to every tool in the named MCP server's toolset.

            - `type: "tool_removal"`

            - `cache_control: optional BetaCacheControlEphemeral or null`

              Create a cache control breakpoint at this content block.

          - `BetaFallbackBlockParam object`

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

            - `to: BetaFallbackInfoParam`

              Identifies one hop of a fallback transition.

            - `type: "fallback"`

            - `trigger: optional unknown`

              The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

      - `role: "user" or "assistant" or "system"`

        - `"user"`

        - `"assistant"`

        - `"system"`

    - `model: Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `cache_control: optional BetaCacheControlEphemeral or null`

      Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

    - `container: optional BetaContainerParams or string or null`

      Container identifier for reuse across requests.

      - `BetaContainerParams object`

        Container parameters with skills to be loaded.

        - `id: optional string or null`

          Container id

        - `skills: optional array of BetaSkillParams or null`

          List of skills to load in the container

          maxItems: 20

          - `skill_id: string`

            Skill ID

            maxLength: 64, minLength: 1

          - `type: "anthropic" or "custom"`

            Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

            - `"anthropic"`

            - `"custom"`

          - `version: optional string`

            Skill version or 'latest' for most recent version

            maxLength: 64, minLength: 1

      - `string`

    - `context_management: optional BetaContextManagementConfig or null`

      Context management configuration.

      This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

      - `edits: optional array of BetaClearToolUses20250919Edit or BetaClearThinking20251015Edit or BetaCompact20260112Edit`

        List of context management edits to apply

        minItems: 0

        - `BetaClearToolUses20250919Edit object`

          - `type: "clear_tool_uses_20250919"`

          - `clear_at_least: optional BetaInputTokensClearAtLeast or null`

            Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

            - `type: "input_tokens"`

            - `value: number`

              minimum: 0

          - `clear_tool_inputs: optional boolean or array of string or null`

            Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

            - `boolean`

            - `array of string`

          - `exclude_tools: optional array of string or null`

            Tool names whose uses are preserved from clearing

          - `keep: optional BetaToolUsesKeep`

            Number of tool uses to retain in the conversation

            - `type: "tool_uses"`

            - `value: number`

              minimum: 0

          - `trigger: optional BetaInputTokensTrigger or BetaToolUsesTrigger`

            Condition that triggers the context management strategy

            - `BetaInputTokensTrigger object`

              - `type: "input_tokens"`

              - `value: number`

                minimum: 1

            - `BetaToolUsesTrigger object`

              - `type: "tool_uses"`

              - `value: number`

                minimum: 1

        - `BetaClearThinking20251015Edit object`

          - `type: "clear_thinking_20251015"`

          - `keep: optional BetaThinkingTurns or BetaAllThinkingTurns or "all"`

            Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

            - `BetaThinkingTurns object`

              - `type: "thinking_turns"`

              - `value: number`

                minimum: 1

            - `BetaAllThinkingTurns object`

              - `type: "all"`

            - `"all"`

        - `BetaCompact20260112Edit object`

          Automatically compact older context when reaching the configured trigger threshold.

          - `type: "compact_20260112"`

          - `instructions: optional string or null`

            Additional instructions for summarization.

          - `pause_after_compaction: optional boolean`

            Whether to pause after compaction and return the compaction block to the user.

          - `trigger: optional BetaInputTokensTrigger or null`

            When to trigger compaction. Defaults to 150000 input tokens.

    - `diagnostics: optional BetaDiagnosticsParam or null`

      Request-level diagnostics. Currently carries the previous response
      id for prompt-cache divergence reporting.

      - `previous_message_id: optional string or null`

        The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

        maxLength: 256

    - `fallback_credit_token: optional string or BetaFallbackCreditTokenParam or null`

      The `fallback_credit_token` from a prior refusal's `stop_details`.

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

      - `BetaFallbackCreditTokenParam object`

        Object form of `fallback_credit_token`: the token plus a redemption
        mode.

        Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
        header the field accepts the bare string only. The bare string and the
        mode-less object are equivalent (both select `strict`), so wrapping
        an existing token changes nothing by itself.

        - `token: string`

          The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

          maxLength: 2048, minLength: 1

        - `mode: optional "strict" or "best_effort"`

          How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

          - `"strict"`

          - `"best_effort"`

    - `fallbacks: optional BetaFallbacksParam or null`

      Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

      - `array of BetaFallbackParam`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `max_tokens: optional number or null`

        - `output_config: optional BetaOutputConfig or null`

          - `effort: optional "low" or "medium" or "high" or 2 more or null`

            All possible effort levels.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `format: optional BetaJSONOutputFormat or null`

            A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

            - `schema: map[unknown]`

              The JSON schema of the format

            - `type: "json_schema"`

          - `task_budget: optional BetaTokenTaskBudget or null`

            User-configurable total token budget across contexts.

            - `total: number`

              Total token budget across all contexts in the session.

              minimum: 1024

            - `type: "tokens"`

              The budget type. Currently only 'tokens' is supported.

            - `remaining: optional number or null`

              Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

              minimum: 0

        - `speed: optional "standard" or "fast" or null`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

        - `thinking: optional BetaThinkingConfigEnabled or BetaThinkingConfigDisabled or BetaThinkingConfigAdaptive or null`

          - `BetaThinkingConfigEnabled object`

            - `budget_tokens: number`

              Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

              Must be ≥1024 and less than `max_tokens`.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

              minimum: 1024

            - `type: "enabled"`

            - `display: optional "summarized" or "omitted" or "updates" or null`

              Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

              - `"summarized"`

              - `"omitted"`

              - `"updates"`

          - `BetaThinkingConfigDisabled object`

            - `type: "disabled"`

          - `BetaThinkingConfigAdaptive object`

            - `type: "adaptive"`

            - `display: optional "summarized" or "omitted" or "updates" or null`

              Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

              - `"summarized"`

              - `"omitted"`

              - `"updates"`

      - `Default = "default"`

    - `inference_geo: optional string or null`

      Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

    - `mcp_servers: optional array of BetaRequestMCPServerURLDefinition`

      MCP servers to be utilized in this request

      maxItems: 20

      - `name: string`

      - `type: "url"`

      - `url: string`

      - `authorization_token: optional string or null`

      - `tool_configuration: optional BetaRequestMCPServerToolConfiguration or null`

        - `allowed_tools: optional array of string or null`

        - `enabled: optional boolean or null`

    - `metadata: optional BetaMetadata`

      An object describing metadata about the request.

      - `user_id: optional string or null`

        An external identifier for the user who is associated with the request.

        This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

        maxLength: 512

    - `output_config: optional BetaOutputConfig`

      Configuration options for the model's output, such as the output format.

    - `service_tier: optional "auto" or "standard_only"`

      Determines whether to use priority capacity (if available) or standard capacity for this request.

      Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

      - `"auto"`

      - `"standard_only"`

    - `speed: optional "standard" or "fast" or null`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

    - `stop_sequences: optional array of string`

      Custom text sequences that will cause the model to stop generating.

      Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

      If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

    - `stream: optional boolean`

      Whether to incrementally stream the response using server-sent events.

      See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

    - `system: optional string or array of BetaTextBlockParam`

      System prompt.

      A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

      - `string`

      - `array of BetaTextBlockParam`

        - `text: string`

          minLength: 1

        - `type: "text"`

        - `cache_control: optional BetaCacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `citations: optional array of BetaTextCitationParam or null`

    - `thinking: optional BetaThinkingConfigParam`

      Configuration for enabling Claude's extended thinking.

      When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `BetaThinkingConfigEnabled object`

      - `BetaThinkingConfigDisabled object`

      - `BetaThinkingConfigAdaptive object`

    - `tool_choice: optional BetaToolChoice`

      How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

      - `BetaToolChoiceAuto object`

        The model will automatically decide whether to use tools.

        - `type: "auto"`

        - `disable_parallel_tool_use: optional boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output at most one tool use.

      - `BetaToolChoiceAny object`

        The model will use any available tools.

        - `type: "any"`

        - `disable_parallel_tool_use: optional boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `BetaToolChoiceTool object`

        The model will use the specified tool with `tool_choice.name`.

        - `name: string`

          The name of the tool to use.

        - `type: "tool"`

        - `disable_parallel_tool_use: optional boolean`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `BetaToolChoiceNone object`

        The model will not be allowed to use tools.

        - `type: "none"`

    - `tools: optional array of BetaToolUnion`

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

      - `BetaTool object`

        - `input_schema: object`

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

        - `cache_control: optional BetaCacheControlEphemeral or null`

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

      - `BetaToolBash20241022 object`

        - `name: "bash"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "bash_20241022"`

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

      - `BetaToolBash20250124 object`

        - `name: "bash"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "bash_20250124"`

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

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "code_execution_20250522"`

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

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "code_execution_20250825"`

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

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "code_execution_20260120"`

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

        - `name: "code_execution"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "code_execution_20260521"`

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

        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: optional BetaCacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `configs: optional BetaBrowserToolsetConfigs or null`

          Per-member configuration for `browser_toolset_20260801`: one
          optional field per member tool, keyed by the member name — the same
          name the member's `tool_use` blocks carry. Every member is an
          accepted key, and a member's defaults apply wherever its key is
          absent. Unknown keys are rejected: the field set is this toolset
          version's complete member set.

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

          - `type: optional BetaBrowserTypeConfig or null`

            `type`'s config overrides.

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

        - `name: "memory"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "memory_20250818"`

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

        - `name: "str_replace_editor"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "text_editor_20241022"`

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

        - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: optional BetaCacheControlEphemeral or null`

          Create a cache control breakpoint at this content block.

        - `configs: optional BetaComputerToolsetConfigs or null`

          Per-member configuration for `computer_toolset_20260801`: one
          optional field per member tool, keyed by the member name — the same
          name the member's `tool_use` blocks carry. Every member is an
          accepted key, and a member's defaults apply wherever its key is
          absent. Unknown keys are rejected: the field set is this toolset
          version's complete member set.

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

          - `type: optional BetaComputerTypeConfig or null`

            `type`'s config overrides.

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

        - `name: "str_replace_editor"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "text_editor_20250124"`

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

        - `name: "str_replace_based_edit_tool"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "text_editor_20250429"`

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

        - `name: "str_replace_based_edit_tool"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "text_editor_20250728"`

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

        - `name: "web_search"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_search_20250305"`

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

        - `name: "web_fetch"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_fetch_20250910"`

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

      - `BetaWebSearchTool20260209 object`

        - `name: "web_search"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_search_20260209"`

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

        - `name: "web_fetch"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_fetch_20260209"`

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

      - `BetaWebFetchTool20260309 object`

        Web fetch tool with use_cache parameter for bypassing cached content.

        - `name: "web_fetch"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_fetch_20260309"`

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

        - `use_cache: optional boolean`

          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

      - `BetaWebSearchTool20260318 object`

        - `name: "web_search"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_search_20260318"`

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

        - `name: "web_fetch"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "web_fetch_20260318"`

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

        - `use_cache: optional boolean`

          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

      - `BetaAdvisorTool20260301 object`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `name: "advisor"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "advisor_20260301"`

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

        - `name: "tool_search_tool_bm25"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

          - `"tool_search_tool_bm25_20251119"`

          - `"tool_search_tool_bm25"`

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

        - `name: "tool_search_tool_regex"`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

          - `"tool_search_tool_regex_20251119"`

          - `"tool_search_tool_regex"`

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

        - `mcp_server_name: string`

          Name of the MCP server to configure tools for

          maxLength: 255, minLength: 1

        - `type: "mcp_toolset"`

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

    - `output_format: optional BetaJSONOutputFormat or null`

      **Deprecated**

      Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

      A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

    - `temperature: optional number`

      **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

      Amount of randomness injected into the response.

      Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

      Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

      maximum: 1, minimum: 0

    - `top_k: optional number`

      **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

      Only sample from the top K options for each subsequent token.

      Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

      Recommended for advanced use cases only.

      minimum: 0

    - `top_p: optional number`

      **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

      Use nucleus sampling.

      In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

      Recommended for advanced use cases only.

      maximum: 1, minimum: 0

## Returns

- `BetaMessageBatch object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string or null`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string or null`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string or null`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: BetaMessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `processing: number`

      Number of requests in the Message Batch that are processing.

      default: 0

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

  - `results_url: string or null`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    default: message_batch

## Example

```bash
curl https://api.anthropic.com/v1/messages/batches \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "requests": [
            {
              "custom_id": "my-custom-id-1",
              "params": {
                "max_tokens": 1024,
                "messages": [
                  {
                    "content": "Hello, world",
                    "role": "user"
                  }
                ],
                "model": "claude-opus-5"
              }
            }
          ]
        }'
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```
