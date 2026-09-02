# Create a Message Batch

`beta.messages.batches.create(**kwargs)  -> BetaMessageBatch`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `requests: Iterable[Request]`

  List of requests for prompt completion. Each is an individual request to create a Message.

  maxItems: 100000, minItems: 1

  - `custom_id: str`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

  - `params: RequestParams`

    Messages API creation parameters for the individual request.

    See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

    - `max_tokens: int`

      The maximum number of tokens to generate before stopping.

      Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

      Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

      Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

      minimum: 0

    - `messages: Iterable[BetaMessageParam]`

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

      - `content: Union[str, List[BetaContentBlockParam]]`

        - `str`

        - `List[BetaContentBlockParam]`

          - `class BetaTextBlockParam: …`

            - `text: str`

              minLength: 1

            - `type: Literal["text"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

              - `type: Literal["ephemeral"]`

              - `ttl: Optional[Literal["5m", "1h"]]`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                - `"5m"`

                - `"1h"`

            - `citations: Optional[List[BetaTextCitationParam]]`

              - `class BetaCitationCharLocationParam: …`

                - `cited_text: str`

                - `document_index: int`

                  minimum: 0

                - `document_title: Optional[str]`

                  maxLength: 500, minLength: 1

                - `end_char_index: int`

                - `start_char_index: int`

                  minimum: 0

                - `type: Literal["char_location"]`

              - `class BetaCitationPageLocationParam: …`

                - `cited_text: str`

                - `document_index: int`

                  minimum: 0

                - `document_title: Optional[str]`

                  maxLength: 500, minLength: 1

                - `end_page_number: int`

                - `start_page_number: int`

                  minimum: 1

                - `type: Literal["page_location"]`

              - `class BetaCitationContentBlockLocationParam: …`

                - `cited_text: str`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: int`

                  minimum: 0

                - `document_title: Optional[str]`

                  maxLength: 500, minLength: 1

                - `end_block_index: int`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `start_block_index: int`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `type: Literal["content_block_location"]`

              - `class BetaCitationWebSearchResultLocationParam: …`

                - `cited_text: str`

                - `encrypted_index: str`

                - `title: Optional[str]`

                  maxLength: 512, minLength: 1

                - `type: Literal["web_search_result_location"]`

                - `url: str`

                  minLength: 1

              - `class BetaCitationSearchResultLocationParam: …`

                - `cited_text: str`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `end_block_index: int`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `search_result_index: int`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `source: str`

                - `start_block_index: int`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `title: Optional[str]`

                - `type: Literal["search_result_location"]`

          - `class BetaImageBlockParam: …`

            - `source: Source`

              - `class BetaBase64ImageSource: …`

                - `data: str`

                  format: byte

                - `media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

                - `type: Literal["base64"]`

              - `class BetaURLImageSource: …`

                - `type: Literal["url"]`

                - `url: str`

              - `class BetaFileImageSource: …`

                - `file_id: str`

                - `type: Literal["file"]`

            - `type: Literal["image"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `transformations: Optional[BetaImageTransformationsParam]`

              Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

              - `oversized_image: Optional[Literal["downsize", "error"]]`

                What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                - `"downsize"`

                - `"error"`

          - `class BetaRequestDocumentBlock: …`

            - `source: Source`

              - `class BetaBase64PDFSource: …`

                - `data: str`

                  format: byte

                - `media_type: Literal["application/pdf"]`

                - `type: Literal["base64"]`

              - `class BetaPlainTextSource: …`

                - `data: str`

                - `media_type: Literal["text/plain"]`

                - `type: Literal["text"]`

              - `class BetaContentBlockSource: …`

                - `content: Union[str, List[BetaContentBlockSourceContent]]`

                  - `str`

                  - `List[BetaContentBlockSourceContent]`

                    - `class BetaTextBlockParam: …`

                    - `class BetaImageBlockParam: …`

                - `type: Literal["content"]`

              - `class BetaURLPDFSource: …`

                - `type: Literal["url"]`

                - `url: str`

              - `class BetaFileDocumentSource: …`

                - `file_id: str`

                - `type: Literal["file"]`

            - `type: Literal["document"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `citations: Optional[BetaCitationsConfigParam]`

              - `enabled: Optional[bool]`

            - `context: Optional[str]`

              minLength: 1

            - `title: Optional[str]`

              maxLength: 500, minLength: 1

          - `class BetaSearchResultBlockParam: …`

            - `content: List[BetaTextBlockParam]`

              - `text: str`

                minLength: 1

              - `type: Literal["text"]`

              - `cache_control: Optional[BetaCacheControlEphemeral]`

                Create a cache control breakpoint at this content block.

              - `citations: Optional[List[BetaTextCitationParam]]`

            - `source: str`

            - `title: str`

            - `type: Literal["search_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `citations: Optional[BetaCitationsConfigParam]`

          - `class BetaThinkingBlockParam: …`

            - `signature: str`

              The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

              Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

            - `thinking: str`

              The `thinking` text of this block as returned by the API.

            - `type: Literal["thinking"]`

          - `class BetaRedactedThinkingBlockParam: …`

            - `data: str`

              The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

            - `type: Literal["redacted_thinking"]`

          - `class BetaToolUseBlockParam: …`

            - `id: str`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: Dict[str, object]`

            - `name: str`

              maxLength: 200, minLength: 1

            - `type: Literal["tool_use"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `caller: Optional[Caller]`

              Tool invocation directly from the model.

              - `class BetaDirectCaller: …`

                Tool invocation directly from the model.

                - `type: Literal["direct"]`

              - `class BetaServerToolCaller: …`

                Tool invocation generated by a server-side tool.

                - `tool_id: str`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `type: Literal["code_execution_20250825"]`

              - `class BetaServerToolCaller20260120: …`

                - `tool_id: str`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `type: Literal["code_execution_20260120"]`

            - `toolset_name: Optional[str]`

              For a toolset member tool_use, the toolset family this member belongs to.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaToolResultBlockParam: …`

            - `tool_use_id: str`

              pattern: ^[a-zA-Z0-9_-]+$

            - `type: Literal["tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `content: Optional[Union[str, List[Content], null]]`

              - `str`

              - `List[Content]`

                - `class BetaTextBlockParam: …`

                - `class BetaImageBlockParam: …`

                - `class BetaSearchResultBlockParam: …`

                - `class BetaRequestDocumentBlock: …`

                - `class BetaToolReferenceBlockParam: …`

                  Tool reference block that can be included in tool_result content.

                  - `tool_name: str`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `type: Literal["tool_reference"]`

                  - `cache_control: Optional[BetaCacheControlEphemeral]`

                    Create a cache control breakpoint at this content block.

                - `class BetaBrowserStateBlockParam: …`

                  The caller's browser state after a browser toolset member call —
                  the full inventory of open tabs, which tab is active, and any side
                  effects (tabs opened, download state changes) the call produced.

                  At most one per `tool_result`, only on a non-error result answering a
                  browser toolset member `tool_use`. The server renders the
                  model-visible text from it; the model never sees the raw fields.

                  - `tabs: List[BetaBrowserStateTabEntry]`

                    All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                    maxItems: 100

                    - `tab_id: str`

                      The caller-assigned identifier for this tab, unique within the inventory.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `title: str`

                      The title of the page the tab is showing. May be empty.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `url: str`

                      The URL of the page the tab is showing. May be empty.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `active: Optional[bool]`

                      Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                  - `type: Literal["browser_state"]`

                  - `cache_control: Optional[BetaCacheControlEphemeral]`

                    Create a cache control breakpoint at this content block.

                  - `state_changes: Optional[List[BetaBrowserStateChange]]`

                    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                    maxItems: 200, minItems: 1

                    - `class BetaBrowserStateChangeTabOpened: …`

                      A tab this call's execution opened that remains open at its end —
                      the creation delta of the `tabs` inventory, not an event log.

                      Carries only the `tab_id`; the tab's `title` and `url` live on its
                      `tabs` entry, which must include the same `tab_id`. A tab opened
                      during a failed call gets no deferred `tab_opened`; it simply appears
                      in the next result's `tabs` inventory.

                      - `tab_id: str`

                        The `tab_id` of the opened tab, present in `tabs`.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type: Literal["tab_opened"]`

                    - `class BetaBrowserStateChangeDownloadStarted: …`

                      A file download that started during this call.

                      - `download_id: str`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type: Literal["download_started"]`

                      - `url: str`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `class BetaBrowserStateChangeDownloadCompleted: …`

                      A file download that finished during this call, reported with the
                      same `download_id` as its `download_started` — or without a prior
                      `download_started`, when the download finished during the call that
                      started it (at most one state change per `download_id` per result).

                      - `download_id: str`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type: Literal["download_completed"]`

                      - `url: str`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `path: Optional[str]`

                        Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                      - `size_bytes: Optional[int]`

                        The completed download's size.

                        minimum: 0

                    - `class BetaBrowserStateChangeDownloadFailed: …`

                      A file download that failed — or was cancelled — during this call.

                      - `download_id: str`

                        The caller-assigned identifier for this download, stable across the state changes reporting it.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type: Literal["download_failed"]`

                      - `url: str`

                        The final post-redirect URL the download was served from.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `error: Optional[str]`

                        The failure or cancellation detail, when known.

                        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

            - `is_error: Optional[bool]`

            - `toolset_name: Optional[str]`

              For a toolset member tool_result, the toolset family of the paired tool_use.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaServerToolUseBlockParam: …`

            - `id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `input: Dict[str, object]`

            - `name: Literal["advisor", "web_search", "web_fetch", 5 more]`

              - `"advisor"`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

            - `type: Literal["server_tool_use"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `caller: Optional[Caller]`

              Tool invocation directly from the model.

              - `class BetaDirectCaller: …`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller: …`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120: …`

          - `class BetaWebSearchToolResultBlockParam: …`

            - `content: BetaWebSearchToolResultBlockParamContent`

              - `List[BetaWebSearchResultBlockParam]`

                - `encrypted_content: str`

                - `title: str`

                - `type: Literal["web_search_result"]`

                - `url: str`

                - `page_age: Optional[str]`

              - `class BetaWebSearchToolRequestError: …`

                - `error_code: BetaWebSearchToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

                - `type: Literal["web_search_tool_result_error"]`

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["web_search_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `caller: Optional[Caller]`

              Tool invocation directly from the model.

              - `class BetaDirectCaller: …`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller: …`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120: …`

          - `class BetaWebFetchToolResultBlockParam: …`

            - `content: Content`

              - `class BetaWebFetchToolResultErrorBlockParam: …`

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

                - `type: Literal["web_fetch_tool_result_error"]`

              - `class BetaWebFetchBlockParam: …`

                - `content: BetaRequestDocumentBlock`

                - `type: Literal["web_fetch_result"]`

                - `url: str`

                  Fetched content URL

                - `retrieved_at: Optional[str]`

                  ISO 8601 timestamp when the content was retrieved

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["web_fetch_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `caller: Optional[Caller]`

              Tool invocation directly from the model.

              - `class BetaDirectCaller: …`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller: …`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120: …`

          - `class BetaAdvisorToolResultBlockParam: …`

            - `content: Content`

              - `class BetaAdvisorToolResultErrorParam: …`

                - `error_code: Literal["max_uses_exceeded", "prompt_too_long", "too_many_requests", 4 more]`

                  - `"max_uses_exceeded"`

                  - `"prompt_too_long"`

                  - `"too_many_requests"`

                  - `"overloaded"`

                  - `"unavailable"`

                  - `"execution_time_exceeded"`

                  - `"model_not_found"`

                - `type: Literal["advisor_tool_result_error"]`

              - `class BetaAdvisorResultBlockParam: …`

                - `text: str`

                - `type: Literal["advisor_result"]`

                - `stop_reason: Optional[str]`

              - `class BetaAdvisorRedactedResultBlockParam: …`

                - `encrypted_content: str`

                  Opaque blob produced by a prior response; must be round-tripped verbatim.

                - `type: Literal["advisor_redacted_result"]`

                - `stop_reason: Optional[str]`

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["advisor_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaCodeExecutionToolResultBlockParam: …`

            - `content: BetaCodeExecutionToolResultBlockParamContent`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class BetaCodeExecutionToolResultErrorParam: …`

                - `error_code: BetaCodeExecutionToolResultErrorCode`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: Literal["code_execution_tool_result_error"]`

              - `class BetaCodeExecutionResultBlockParam: …`

                - `content: List[BetaCodeExecutionOutputBlockParam]`

                  - `file_id: str`

                  - `type: Literal["code_execution_output"]`

                - `return_code: int`

                - `stderr: str`

                - `stdout: str`

                - `type: Literal["code_execution_result"]`

              - `class BetaEncryptedCodeExecutionResultBlockParam: …`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: List[BetaCodeExecutionOutputBlockParam]`

                  - `file_id: str`

                  - `type: Literal["code_execution_output"]`

                - `encrypted_stdout: str`

                - `return_code: int`

                - `stderr: str`

                - `type: Literal["encrypted_code_execution_result"]`

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["code_execution_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaBashCodeExecutionToolResultBlockParam: …`

            - `content: Content`

              - `class BetaBashCodeExecutionToolResultErrorParam: …`

                - `error_code: Literal["invalid_tool_input", "unavailable", "too_many_requests", 2 more]`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

                - `type: Literal["bash_code_execution_tool_result_error"]`

              - `class BetaBashCodeExecutionResultBlockParam: …`

                - `content: List[BetaBashCodeExecutionOutputBlockParam]`

                  - `file_id: str`

                  - `type: Literal["bash_code_execution_output"]`

                - `return_code: int`

                - `stderr: str`

                - `stdout: str`

                - `type: Literal["bash_code_execution_result"]`

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["bash_code_execution_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaTextEditorCodeExecutionToolResultBlockParam: …`

            - `content: Content`

              - `class BetaTextEditorCodeExecutionToolResultErrorParam: …`

                - `error_code: Literal["invalid_tool_input", "unavailable", "too_many_requests", 2 more]`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `type: Literal["text_editor_code_execution_tool_result_error"]`

                - `error_message: Optional[str]`

              - `class BetaTextEditorCodeExecutionViewResultBlockParam: …`

                - `content: str`

                - `file_type: Literal["text", "image", "pdf"]`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `type: Literal["text_editor_code_execution_view_result"]`

                - `num_lines: Optional[int]`

                - `start_line: Optional[int]`

                - `total_lines: Optional[int]`

              - `class BetaTextEditorCodeExecutionCreateResultBlockParam: …`

                - `is_file_update: bool`

                - `type: Literal["text_editor_code_execution_create_result"]`

              - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …`

                - `type: Literal["text_editor_code_execution_str_replace_result"]`

                - `lines: Optional[List[str]]`

                - `new_lines: Optional[int]`

                - `new_start: Optional[int]`

                - `old_lines: Optional[int]`

                - `old_start: Optional[int]`

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["text_editor_code_execution_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaToolSearchToolResultBlockParam: …`

            - `content: Content`

              - `class BetaToolSearchToolResultErrorParam: …`

                - `error_code: Literal["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"]`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `type: Literal["tool_search_tool_result_error"]`

                - `error_message: Optional[str]`

              - `class BetaToolSearchToolSearchResultBlockParam: …`

                - `tool_references: List[BetaToolReferenceBlockParam]`

                  - `tool_name: str`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `type: Literal["tool_reference"]`

                  - `cache_control: Optional[BetaCacheControlEphemeral]`

                    Create a cache control breakpoint at this content block.

                - `type: Literal["tool_search_tool_search_result"]`

            - `tool_use_id: str`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: Literal["tool_search_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaMCPToolUseBlockParam: …`

            - `id: str`

              pattern: ^[a-zA-Z0-9_-]+$

            - `input: Dict[str, object]`

            - `name: str`

            - `server_name: str`

              The name of the MCP server

            - `type: Literal["mcp_tool_use"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaRequestMCPToolResultBlockParam: …`

            - `tool_use_id: str`

              pattern: ^[a-zA-Z0-9_-]+$

            - `type: Literal["mcp_tool_result"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `content: Optional[Union[str, List[BetaTextBlockParam], null]]`

              - `str`

              - `List[BetaTextBlockParam]`

                - `text: str`

                  minLength: 1

                - `type: Literal["text"]`

                - `cache_control: Optional[BetaCacheControlEphemeral]`

                  Create a cache control breakpoint at this content block.

                - `citations: Optional[List[BetaTextCitationParam]]`

            - `is_error: Optional[bool]`

          - `class BetaContainerUploadBlockParam: …`

            A content block that represents a file to be uploaded to the container
            Files uploaded via this block will be available in the container's input directory.

            - `file_id: str`

            - `type: Literal["container_upload"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaCompactionBlockParam: …`

            A compaction block containing summary of previous context.

            Users should round-trip these blocks from responses to subsequent requests
            to maintain context across compaction boundaries.

            When content is None, the block represents a failed compaction. The server
            treats these as no-ops. Empty string content is not allowed.

            - `type: Literal["compaction"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

            - `content: Optional[str]`

              Summary of previously compacted content, or null if compaction failed

            - `encrypted_content: Optional[str]`

              Opaque metadata from prior compaction, to be round-tripped verbatim

          - `class BetaRequestToolAdditionBlock: …`

            Mid-conversation directive to surface a declared tool.

            `tool` references a tool (or MCP toolset) by name from the request's
            `tools`; it is offered to the model from this point in the
            conversation onward.

            - `tool: Tool`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `class BetaToolChangeToolReference: …`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

                - `name: str`

                  pattern: ^[a-zA-Z0-9_-]{1,128}$

                - `type: Literal["tool_reference"]`

              - `class BetaToolChangeMCPToolReference: …`

                Reference to a single MCP tool by its server and remote name — the
                same `server_name`/`name` pair `mcp_tool_use` carries.

                - `name: str`

                - `server_name: str`

                - `type: Literal["mcp_tool_reference"]`

              - `class BetaToolChangeMCPToolsetReference: …`

                Reference to every tool in the named MCP server's toolset.

                - `server_name: str`

                - `type: Literal["mcp_toolset_reference"]`

            - `type: Literal["tool_addition"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaRequestToolRemovalBlock: …`

            Mid-conversation directive to withdraw a tool.

            `tool` references a tool (or MCP toolset) by name from the request's
            `tools`; it is no longer offered to the model from this point in the
            conversation onward.

            - `tool: Tool`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `class BetaToolChangeToolReference: …`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

              - `class BetaToolChangeMCPToolReference: …`

                Reference to a single MCP tool by its server and remote name — the
                same `server_name`/`name` pair `mcp_tool_use` carries.

              - `class BetaToolChangeMCPToolsetReference: …`

                Reference to every tool in the named MCP server's toolset.

            - `type: Literal["tool_removal"]`

            - `cache_control: Optional[BetaCacheControlEphemeral]`

              Create a cache control breakpoint at this content block.

          - `class BetaFallbackBlockParam: …`

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

            - `from_: BetaFallbackInfoParam`

              Identifies one hop of a fallback transition.

              - `model: Model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `Literal["claude-fable-5-1", "claude-mythos-5-1", "claude-sonnet-5", 14 more]`

                  The model that will complete your prompt.

                  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                  - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
                  - `claude-mythos-5-1` - Our most capable model for cybersecurity and biology research, available through trusted access programs
                  - `claude-sonnet-5` - High-performance model for coding and agents
                  - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
                  - `claude-mythos-5` - Most capable model for cybersecurity and biology research
                  - `claude-opus-5` - Powerful intelligence for long-running agents and coding
                  - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
                  - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
                  - `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
                  - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
                  - `claude-sonnet-4-6` - Best combination of speed and intelligence
                  - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
                  - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
                  - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
                  - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
                  - `claude-sonnet-4-5` - High-performance model for agents and coding
                  - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

                - `str`

            - `to: BetaFallbackInfoParam`

              Identifies one hop of a fallback transition.

            - `type: Literal["fallback"]`

            - `trigger: Optional[object]`

              The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

      - `role: Literal["user", "assistant", "system"]`

        - `"user"`

        - `"assistant"`

        - `"system"`

      - `clear_at: Optional[Literal["next_user_message", "never"]]`

        How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages.

        - `"next_user_message"`

        - `"never"`

      - `output_config: Optional[BetaSystemMessageOutputConfig]`

        Per-message output configuration on a role:"system" input message.

        Fields here apply per-turn; `format` remains top-level only. An
        empty `{}` is accepted on a message that carries content; a message
        with neither content nor output_config fields is rejected.

        - `effort: Optional[Literal["low", "medium", "high", 2 more]]`

          All possible effort levels.

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

    - `model: ModelParam`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `cache_control: Optional[BetaCacheControlEphemeralParam]`

      Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

    - `container: Optional[RequestParamsContainer]`

      Container identifier for reuse across requests.

      - `class BetaContainerParams: …`

        Container parameters with skills to be loaded.

        - `id: Optional[str]`

          Container id

        - `skills: Optional[List[BetaSkillParams]]`

          List of skills to load in the container

          maxItems: 20

          - `skill_id: str`

            Skill ID

            maxLength: 64, minLength: 1

          - `type: Literal["anthropic", "custom"]`

            Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

            - `"anthropic"`

            - `"custom"`

          - `version: Optional[str]`

            Skill version or 'latest' for most recent version

            maxLength: 64, minLength: 1

      - `str`

    - `context_management: Optional[BetaContextManagementConfigParam]`

      Context management configuration.

      This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

      - `edits: Optional[List[Edit]]`

        List of context management edits to apply

        minItems: 0

        - `class BetaClearToolUses20250919Edit: …`

          - `type: Literal["clear_tool_uses_20250919"]`

          - `clear_at_least: Optional[BetaInputTokensClearAtLeast]`

            Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

            - `type: Literal["input_tokens"]`

            - `value: int`

              minimum: 0

          - `clear_tool_inputs: Optional[Union[bool, List[str], null]]`

            Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

            - `bool`

            - `List[str]`

          - `exclude_tools: Optional[List[str]]`

            Tool names whose uses are preserved from clearing

          - `keep: Optional[BetaToolUsesKeep]`

            Number of tool uses to retain in the conversation

            - `type: Literal["tool_uses"]`

            - `value: int`

              minimum: 0

          - `trigger: Optional[Trigger]`

            Condition that triggers the context management strategy

            - `class BetaInputTokensTrigger: …`

              - `type: Literal["input_tokens"]`

              - `value: int`

                minimum: 1

            - `class BetaToolUsesTrigger: …`

              - `type: Literal["tool_uses"]`

              - `value: int`

                minimum: 1

        - `class BetaClearThinking20251015Edit: …`

          - `type: Literal["clear_thinking_20251015"]`

          - `keep: Optional[Keep]`

            Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

            - `class BetaThinkingTurns: …`

              - `type: Literal["thinking_turns"]`

              - `value: int`

                minimum: 1

            - `class BetaAllThinkingTurns: …`

              - `type: Literal["all"]`

            - `Literal["all"]`

        - `class BetaCompact20260112Edit: …`

          Automatically compact older context when reaching the configured trigger threshold.

          - `type: Literal["compact_20260112"]`

          - `instructions: Optional[str]`

            Additional instructions for summarization.

          - `pause_after_compaction: Optional[bool]`

            Whether to pause after compaction and return the compaction block to the user.

          - `trigger: Optional[BetaInputTokensTrigger]`

            When to trigger compaction. Defaults to 150000 input tokens.

    - `diagnostics: Optional[BetaDiagnosticsParam]`

      Request-level diagnostics. Currently carries the previous response
      id for prompt-cache divergence reporting.

      - `previous_message_id: Optional[str]`

        The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

        maxLength: 256

    - `fallback_credit_token: Optional[RequestParamsFallbackCreditToken]`

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

      - `str`

      - `class BetaFallbackCreditTokenParam: …`

        Object form of `fallback_credit_token`: the token plus a redemption
        mode.

        Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
        header the field accepts the bare string only. The bare string and the
        mode-less object are equivalent (both select `strict`), so wrapping
        an existing token changes nothing by itself.

        - `token: str`

          The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

          maxLength: 2048, minLength: 1

        - `mode: Optional[Literal["strict", "best_effort"]]`

          How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

          - `"strict"`

          - `"best_effort"`

    - `fallbacks: Optional[BetaFallbacksParam]`

      Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

      - `List[BetaFallbackParam]`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `max_tokens: Optional[int]`

        - `output_config: Optional[BetaOutputConfig]`

          - `effort: Optional[Literal["low", "medium", "high", 2 more]]`

            All possible effort levels.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `format: Optional[BetaJSONOutputFormat]`

            A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

            - `schema: Dict[str, object]`

              The JSON schema of the format

            - `type: Literal["json_schema"]`

          - `task_budget: Optional[BetaTokenTaskBudget]`

            User-configurable total token budget across contexts.

            - `total: int`

              Total token budget across all contexts in the session.

              minimum: 1024

            - `type: Literal["tokens"]`

              The budget type. Currently only 'tokens' is supported.

            - `remaining: Optional[int]`

              Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

              minimum: 0

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

        - `thinking: Optional[Thinking]`

          - `class BetaThinkingConfigEnabled: …`

            - `budget_tokens: int`

              Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

              Must be ≥1024 and less than `max_tokens`.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

              minimum: 1024

            - `type: Literal["enabled"]`

            - `block_binding: Optional[BetaThinkingBlockBinding]`

              Controls for block binding: what happens when a thinking block this
              request sends back fails the conversation check. Every field is optional;
              an empty object means every default.

              - `prefix_mismatch_behavior: Optional[BetaThinkingPrefixMismatchBehavior]`

                What happens when a thinking block in `messages` fails the conversation
                check: it was created in a different conversation, or the messages before
                it have changed since. `"error"` (the default) fails the request with a
                400 error. `"drop_block"` removes the failing blocks and the request
                proceeds; the model no longer sees the dropped reasoning.

                - `"error"`

                - `"drop_block"`

            - `display: Optional[Literal["summarized", "omitted", "updates"]]`

              Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

              - `"summarized"`

              - `"omitted"`

              - `"updates"`

          - `class BetaThinkingConfigDisabled: …`

            - `type: Literal["disabled"]`

          - `class BetaThinkingConfigAdaptive: …`

            - `type: Literal["adaptive"]`

            - `block_binding: Optional[BetaThinkingBlockBinding]`

              Controls for block binding: what happens when a thinking block this
              request sends back fails the conversation check. Every field is optional;
              an empty object means every default.

            - `display: Optional[Literal["summarized", "omitted", "updates"]]`

              Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

              - `"summarized"`

              - `"omitted"`

              - `"updates"`

      - `Literal["default"]`

    - `inference_geo: Optional[str]`

      Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

    - `mcp_servers: Optional[Iterable[BetaRequestMCPServerURLDefinitionParam]]`

      MCP servers to be utilized in this request

      maxItems: 20

      - `name: str`

      - `type: Literal["url"]`

      - `url: str`

      - `authorization_token: Optional[str]`

      - `tool_configuration: Optional[BetaRequestMCPServerToolConfiguration]`

        - `allowed_tools: Optional[List[str]]`

        - `enabled: Optional[bool]`

    - `metadata: Optional[BetaMetadataParam]`

      An object describing metadata about the request.

      - `user_id: Optional[str]`

        An external identifier for the user who is associated with the request.

        This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

        maxLength: 512

    - `output_config: Optional[BetaOutputConfigParam]`

      Configuration options for the model's output, such as the output format.

    - `service_tier: Optional[Literal["auto", "standard_only"]]`

      Determines whether to use priority capacity (if available) or standard capacity for this request.

      Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

      - `"auto"`

      - `"standard_only"`

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

    - `stop_sequences: Optional[Sequence[str]]`

      Custom text sequences that will cause the model to stop generating.

      Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

      If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

    - `stream: Optional[bool]`

      Whether to incrementally stream the response using server-sent events.

      See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

    - `system: Optional[Union[str, Iterable[BetaTextBlockParam]]]`

      System prompt.

      A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

      - `str`

      - `Iterable[BetaTextBlockParam]`

        - `text: str`

          minLength: 1

        - `type: Literal["text"]`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `citations: Optional[List[BetaTextCitationParam]]`

    - `thinking: Optional[BetaThinkingConfigParam]`

      Configuration for enabling Claude's extended thinking.

      When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `class BetaThinkingConfigEnabled: …`

      - `class BetaThinkingConfigDisabled: …`

      - `class BetaThinkingConfigAdaptive: …`

    - `tool_choice: Optional[BetaToolChoiceParam]`

      How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

      - `class BetaToolChoiceAuto: …`

        The model will automatically decide whether to use tools.

        - `type: Literal["auto"]`

        - `disable_parallel_tool_use: Optional[bool]`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output at most one tool use.

      - `class BetaToolChoiceAny: …`

        The model will use any available tools.

        - `type: Literal["any"]`

        - `disable_parallel_tool_use: Optional[bool]`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `class BetaToolChoiceTool: …`

        The model will use the specified tool with `tool_choice.name`.

        - `name: str`

          The name of the tool to use.

        - `type: Literal["tool"]`

        - `disable_parallel_tool_use: Optional[bool]`

          Whether to disable parallel tool use.

          Defaults to `false`. If set to `true`, the model will output exactly one tool use.

      - `class BetaToolChoiceNone: …`

        The model will not be allowed to use tools.

        - `type: Literal["none"]`

    - `tools: Optional[Iterable[BetaToolUnionParam]]`

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

      - `class BetaTool: …`

        - `input_schema: InputSchema`

          [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

          This defines the shape of the `input` that your tool accepts and that the model will produce.

          - `type: Literal["object"]`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

          maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `description: Optional[str]`

          Description of what this tool does.

          Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

        - `eager_input_streaming: Optional[bool]`

          Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

        - `type: Optional[Literal["custom"]]`

      - `class BetaToolBash20241022: …`

        - `name: Literal["bash"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["bash_20241022"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolBash20250124: …`

        - `name: Literal["bash"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["bash_20250124"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaCodeExecutionTool20250522: …`

        - `name: Literal["code_execution"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["code_execution_20250522"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaCodeExecutionTool20250825: …`

        - `name: Literal["code_execution"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["code_execution_20250825"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaCodeExecutionTool20260120: …`

        Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

        - `name: Literal["code_execution"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["code_execution_20260120"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaCodeExecutionTool20260521: …`

        Code execution tool with REPL state persistence.

        - `name: Literal["code_execution"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["code_execution_20260521"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaBrowserToolset20260801: …`

        The browser toolset: a single `tools[]` entry (carrying no
        `name`) that declares the browser tool family. The model is served
        the family's tool with any members disabled via `configs` removed
        from its schema.

        - `type: Literal["browser_toolset_20260801"]`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `configs: Optional[BetaBrowserToolsetConfigs]`

          Per-member configuration for `browser_toolset_20260801`: one
          optional field per member tool, keyed by the member name — the same
          name the member's `tool_use` blocks carry. Every member is an
          accepted key, and a member's defaults apply wherever its key is
          absent. Unknown keys are rejected: the field set is this toolset
          version's complete member set.

          - `close_tab: Optional[BetaBrowserCloseTabConfig]`

            `close_tab`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `double_click: Optional[BetaBrowserDoubleClickConfig]`

            `double_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `file_upload: Optional[BetaBrowserFileUploadConfig]`

            `file_upload`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `find: Optional[BetaBrowserFindConfig]`

            `find`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `form_input: Optional[BetaBrowserFormInputConfig]`

            `form_input`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `get_page_text: Optional[BetaBrowserGetPageTextConfig]`

            `get_page_text`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `hold_key: Optional[BetaBrowserHoldKeyConfig]`

            `hold_key`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `hover: Optional[BetaBrowserHoverConfig]`

            `hover`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `javascript_exec: Optional[BetaBrowserJavascriptExecConfig]`

            `javascript_exec`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `key: Optional[BetaBrowserKeyConfig]`

            `key`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_click: Optional[BetaBrowserLeftClickConfig]`

            `left_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_click_drag: Optional[BetaBrowserLeftClickDragConfig]`

            `left_click_drag`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_mouse_down: Optional[BetaBrowserLeftMouseDownConfig]`

            `left_mouse_down`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_mouse_up: Optional[BetaBrowserLeftMouseUpConfig]`

            `left_mouse_up`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `list_tabs: Optional[BetaBrowserListTabsConfig]`

            `list_tabs`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `middle_click: Optional[BetaBrowserMiddleClickConfig]`

            `middle_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `mouse_move: Optional[BetaBrowserMouseMoveConfig]`

            `mouse_move`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `navigate: Optional[BetaBrowserNavigateConfig]`

            `navigate`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `new_tab: Optional[BetaBrowserNewTabConfig]`

            `new_tab`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `read_console: Optional[BetaBrowserReadConsoleConfig]`

            `read_console`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `read_network: Optional[BetaBrowserReadNetworkConfig]`

            `read_network`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `read_page: Optional[BetaBrowserReadPageConfig]`

            `read_page`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `right_click: Optional[BetaBrowserRightClickConfig]`

            `right_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `screenshot: Optional[BetaBrowserScreenshotConfig]`

            `screenshot`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `scroll: Optional[BetaBrowserScrollConfig]`

            `scroll`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `scroll_to: Optional[BetaBrowserScrollToConfig]`

            `scroll_to`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `switch_tab: Optional[BetaBrowserSwitchTabConfig]`

            `switch_tab`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `triple_click: Optional[BetaBrowserTripleClickConfig]`

            `triple_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `type: Optional[BetaBrowserTypeConfig]`

            `type`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `wait: Optional[BetaBrowserWaitConfig]`

            `wait`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `zoom: Optional[BetaBrowserZoomConfig]`

            `zoom`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `class BetaToolComputerUse20241022: …`

        - `display_height_px: int`

          The height of the display in pixels.

          minimum: 1

        - `display_width_px: int`

          The width of the display in pixels.

          minimum: 1

        - `name: Literal["computer"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["computer_20241022"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `display_number: Optional[int]`

          The X11 display number (e.g. 0, 1) for the display.

          minimum: 0

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaMemoryTool20250818: …`

        - `name: Literal["memory"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["memory_20250818"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolComputerUse20250124: …`

        - `display_height_px: int`

          The height of the display in pixels.

          minimum: 1

        - `display_width_px: int`

          The width of the display in pixels.

          minimum: 1

        - `name: Literal["computer"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["computer_20250124"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `display_number: Optional[int]`

          The X11 display number (e.g. 0, 1) for the display.

          minimum: 0

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolTextEditor20241022: …`

        - `name: Literal["str_replace_editor"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["text_editor_20241022"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolComputerUse20251124: …`

        - `display_height_px: int`

          The height of the display in pixels.

          minimum: 1

        - `display_width_px: int`

          The width of the display in pixels.

          minimum: 1

        - `name: Literal["computer"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["computer_20251124"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `display_number: Optional[int]`

          The X11 display number (e.g. 0, 1) for the display.

          minimum: 0

        - `enable_zoom: Optional[bool]`

          Whether to enable an action to take a zoomed-in screenshot of the screen.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaComputerToolset20260801: …`

        The computer toolset: a single `tools[]` entry (carrying no
        `name`) that declares the computer tool family. The model is
        served the family's tool with any members disabled via `configs`
        removed from its schema. Every member is enabled by default, zoom
        included. The single-tool options `display_number` and
        `enable_zoom` are not fields of a toolset entry — it carries only
        `type`, `configs`, and `cache_control`; zoom is controlled
        via `configs.zoom.enabled`.

        - `type: Literal["computer_toolset_20260801"]`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `configs: Optional[BetaComputerToolsetConfigs]`

          Per-member configuration for `computer_toolset_20260801`: one
          optional field per member tool, keyed by the member name — the same
          name the member's `tool_use` blocks carry. Every member is an
          accepted key, and a member's defaults apply wherever its key is
          absent. Unknown keys are rejected: the field set is this toolset
          version's complete member set.

          - `cursor_position: Optional[BetaComputerCursorPositionConfig]`

            `cursor_position`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `double_click: Optional[BetaComputerDoubleClickConfig]`

            `double_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `hold_key: Optional[BetaComputerHoldKeyConfig]`

            `hold_key`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `key: Optional[BetaComputerKeyConfig]`

            `key`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_click: Optional[BetaComputerLeftClickConfig]`

            `left_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_click_drag: Optional[BetaComputerLeftClickDragConfig]`

            `left_click_drag`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_mouse_down: Optional[BetaComputerLeftMouseDownConfig]`

            `left_mouse_down`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `left_mouse_up: Optional[BetaComputerLeftMouseUpConfig]`

            `left_mouse_up`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `middle_click: Optional[BetaComputerMiddleClickConfig]`

            `middle_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `mouse_move: Optional[BetaComputerMouseMoveConfig]`

            `mouse_move`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `right_click: Optional[BetaComputerRightClickConfig]`

            `right_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `screenshot: Optional[BetaComputerScreenshotConfig]`

            `screenshot`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `scroll: Optional[BetaComputerScrollConfig]`

            `scroll`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `triple_click: Optional[BetaComputerTripleClickConfig]`

            `triple_click`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `type: Optional[BetaComputerTypeConfig]`

            `type`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `wait: Optional[BetaComputerWaitConfig]`

            `wait`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

          - `zoom: Optional[BetaComputerZoomConfig]`

            `zoom`'s config overrides.

            - `defer_loading: Optional[bool]`

              Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

            - `enabled: Optional[bool]`

              Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `class BetaToolTextEditor20250124: …`

        - `name: Literal["str_replace_editor"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["text_editor_20250124"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolTextEditor20250429: …`

        - `name: Literal["str_replace_based_edit_tool"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["text_editor_20250429"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolTextEditor20250728: …`

        - `name: Literal["str_replace_based_edit_tool"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["text_editor_20250728"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `input_examples: Optional[List[Dict[str, object]]]`

        - `max_characters: Optional[int]`

          Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

          minimum: 1

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaWebSearchTool20250305: …`

        - `name: Literal["web_search"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_search_20250305"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

        - `blocked_domains: Optional[List[str]]`

          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

        - `user_location: Optional[BetaUserLocation]`

          Parameters for the user's location. Used to provide more relevant search results.

          - `type: Literal["approximate"]`

          - `city: Optional[str]`

            The city of the user.

            maxLength: 255, minLength: 1

          - `country: Optional[str]`

            The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            maxLength: 2, minLength: 2

          - `region: Optional[str]`

            The region of the user.

            maxLength: 255, minLength: 1

          - `timezone: Optional[str]`

            The [IANA timezone](https://nodatime.org/TimeZones) of the user.

            maxLength: 255, minLength: 1

      - `class BetaWebFetchTool20250910: …`

        - `name: Literal["web_fetch"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_fetch_20250910"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          List of domains to allow fetching from

        - `blocked_domains: Optional[List[str]]`

          List of domains to block fetching from

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `citations: Optional[BetaCitationsConfigParam]`

          Citations configuration for fetched documents. Citations are disabled by default.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_content_tokens: Optional[int]`

          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          exclusiveMinimum: 0

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaWebSearchTool20260209: …`

        - `name: Literal["web_search"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_search_20260209"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

        - `blocked_domains: Optional[List[str]]`

          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

        - `user_location: Optional[BetaUserLocation]`

          Parameters for the user's location. Used to provide more relevant search results.

      - `class BetaWebFetchTool20260209: …`

        - `name: Literal["web_fetch"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_fetch_20260209"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          List of domains to allow fetching from

        - `blocked_domains: Optional[List[str]]`

          List of domains to block fetching from

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `citations: Optional[BetaCitationsConfigParam]`

          Citations configuration for fetched documents. Citations are disabled by default.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_content_tokens: Optional[int]`

          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          exclusiveMinimum: 0

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaWebFetchTool20260309: …`

        Web fetch tool with use_cache parameter for bypassing cached content.

        - `name: Literal["web_fetch"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_fetch_20260309"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          List of domains to allow fetching from

        - `blocked_domains: Optional[List[str]]`

          List of domains to block fetching from

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `citations: Optional[BetaCitationsConfigParam]`

          Citations configuration for fetched documents. Citations are disabled by default.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_content_tokens: Optional[int]`

          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          exclusiveMinimum: 0

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

        - `use_cache: Optional[bool]`

          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

      - `class BetaWebSearchTool20260318: …`

        - `name: Literal["web_search"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_search_20260318"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

        - `blocked_domains: Optional[List[str]]`

          If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `response_inclusion: Optional[Literal["full", "excluded"]]`

          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

          - `"full"`

          - `"excluded"`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

        - `user_location: Optional[BetaUserLocation]`

          Parameters for the user's location. Used to provide more relevant search results.

      - `class BetaWebFetchTool20260318: …`

        - `name: Literal["web_fetch"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["web_fetch_20260318"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `allowed_domains: Optional[List[str]]`

          List of domains to allow fetching from

        - `blocked_domains: Optional[List[str]]`

          List of domains to block fetching from

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `citations: Optional[BetaCitationsConfigParam]`

          Citations configuration for fetched documents. Citations are disabled by default.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_content_tokens: Optional[int]`

          Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          exclusiveMinimum: 0

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `response_inclusion: Optional[Literal["full", "excluded"]]`

          How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

          - `"full"`

          - `"excluded"`

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

        - `use_cache: Optional[bool]`

          Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

      - `class BetaAdvisorTool20260301: …`

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `name: Literal["advisor"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["advisor_20260301"]`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `caching: Optional[BetaCacheControlEphemeral]`

          Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `max_tokens: Optional[int]`

          Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

          minimum: 1024

        - `max_uses: Optional[int]`

          Maximum number of times the tool can be used in the API request.

          exclusiveMinimum: 0

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolSearchToolBm25_20251119: …`

        - `name: Literal["tool_search_tool_bm25"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["tool_search_tool_bm25_20251119", "tool_search_tool_bm25"]`

          - `"tool_search_tool_bm25_20251119"`

          - `"tool_search_tool_bm25"`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaToolSearchToolRegex20251119: …`

        - `name: Literal["tool_search_tool_regex"]`

          Name of the tool.

          This is how the tool will be called by the model and in `tool_use` blocks.

        - `type: Literal["tool_search_tool_regex_20251119", "tool_search_tool_regex"]`

          - `"tool_search_tool_regex_20251119"`

          - `"tool_search_tool_regex"`

        - `allowed_callers: Optional[List[Literal["direct", "code_execution_20250825", "code_execution_20260120", "code_execution_20260521"]]]`

          - `"direct"`

          - `"code_execution_20250825"`

          - `"code_execution_20260120"`

          - `"code_execution_20260521"`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `defer_loading: Optional[bool]`

          If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

        - `strict: Optional[bool]`

          When true, guarantees schema validation on tool names and inputs

      - `class BetaMCPToolset: …`

        Configuration for a group of tools from an MCP server.

        Allows configuring enabled status and defer_loading for all tools
        from an MCP server, with optional per-tool overrides.

        - `mcp_server_name: str`

          Name of the MCP server to configure tools for

          maxLength: 255, minLength: 1

        - `type: Literal["mcp_toolset"]`

        - `cache_control: Optional[BetaCacheControlEphemeral]`

          Create a cache control breakpoint at this content block.

        - `configs: Optional[Dict[str, BetaMCPToolConfig]]`

          Configuration overrides for specific tools, keyed by tool name

          - `defer_loading: Optional[bool]`

          - `enabled: Optional[bool]`

        - `default_config: Optional[BetaMCPToolDefaultConfig]`

          Default configuration applied to all tools from this server

          - `defer_loading: Optional[bool]`

          - `enabled: Optional[bool]`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 41 more]`

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

- `user_profile_id: Optional[str]`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

## Returns

- `class BetaMessageBatch: …`

  - `id: str`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: Optional[datetime]`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: Optional[datetime]`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: datetime`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: Optional[datetime]`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: datetime`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: Literal["in_progress", "canceling", "ended"]`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: BetaMessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: int`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `errored: int`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `expired: int`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `processing: int`

      Number of requests in the Message Batch that are processing.

      default: 0

    - `succeeded: int`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

  - `results_url: Optional[str]`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: Literal["message_batch"]`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    default: message_batch

## Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_message_batch = client.beta.messages.batches.create(
    requests=[
        {
            "custom_id": "my-custom-id-1",
            "params": {
                "max_tokens": 1024,
                "messages": [
                    {
                        "content": "Hello, world",
                        "role": "user",
                    }
                ],
                "model": "claude-opus-5",
            },
        }
    ],
)
print(beta_message_batch.id)
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
