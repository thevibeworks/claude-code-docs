# Create a Message

`beta.messages.create(**kwargs) -> BetaMessage`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

## Parameters

- `max_tokens: Integer`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

  minimum: 0

- `messages: Array[BetaMessageParam]`

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

  - `content: String | Array[BetaContentBlockParam]`

    - `String = String`

    - `UnionMember1 = Array[BetaContentBlockParam]`

      - `class BetaTextBlockParam`

        - `text: String`

          minLength: 1

        - `type: :text`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

          - `type: :ephemeral`

          - `ttl: :"5m" | :"1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `:"5m"`

            - `:"1h"`

        - `citations: Array[BetaTextCitationParam]`

          - `class BetaCitationCharLocationParam`

            - `cited_text: String`

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

              maxLength: 500, minLength: 1

            - `end_char_index: Integer`

            - `start_char_index: Integer`

              minimum: 0

            - `type: :char_location`

          - `class BetaCitationPageLocationParam`

            - `cited_text: String`

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

              maxLength: 500, minLength: 1

            - `end_page_number: Integer`

            - `start_page_number: Integer`

              minimum: 1

            - `type: :page_location`

          - `class BetaCitationContentBlockLocationParam`

            - `cited_text: String`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

              maxLength: 500, minLength: 1

            - `end_block_index: Integer`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `start_block_index: Integer`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `type: :content_block_location`

          - `class BetaCitationWebSearchResultLocationParam`

            - `cited_text: String`

            - `encrypted_index: String`

            - `title: String`

              maxLength: 512, minLength: 1

            - `type: :web_search_result_location`

            - `url: String`

              minLength: 1

          - `class BetaCitationSearchResultLocationParam`

            - `cited_text: String`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `end_block_index: Integer`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `search_result_index: Integer`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `source: String`

            - `start_block_index: Integer`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `title: String`

            - `type: :search_result_location`

      - `class BetaImageBlockParam`

        - `source: BetaBase64ImageSource | BetaURLImageSource | BetaFileImageSource`

          - `class BetaBase64ImageSource`

            - `data: String`

              format: byte

            - `media_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"`

              - `:"image/jpeg"`

              - `:"image/png"`

              - `:"image/gif"`

              - `:"image/webp"`

            - `type: :base64`

          - `class BetaURLImageSource`

            - `type: :url`

            - `url: String`

          - `class BetaFileImageSource`

            - `file_id: String`

            - `type: :file`

        - `type: :image`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `transformations: BetaImageTransformationsParam`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `oversized_image: :downsize | :error`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `:downsize`

            - `:error`

      - `class BetaRequestDocumentBlock`

        - `source: BetaBase64PDFSource | BetaPlainTextSource | BetaContentBlockSource | 2 more`

          - `class BetaBase64PDFSource`

            - `data: String`

              format: byte

            - `media_type: :"application/pdf"`

            - `type: :base64`

          - `class BetaPlainTextSource`

            - `data: String`

            - `media_type: :"text/plain"`

            - `type: :text`

          - `class BetaContentBlockSource`

            - `content: String | Array[BetaContentBlockSourceContent]`

              - `String = String`

              - `BetaContentBlockSourceContent = Array[BetaContentBlockSourceContent]`

                - `class BetaTextBlockParam`

                - `class BetaImageBlockParam`

            - `type: :content`

          - `class BetaURLPDFSource`

            - `type: :url`

            - `url: String`

          - `class BetaFileDocumentSource`

            - `file_id: String`

            - `type: :file`

        - `type: :document`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `citations: BetaCitationsConfigParam`

          - `enabled: bool`

        - `context: String`

          minLength: 1

        - `title: String`

          maxLength: 500, minLength: 1

      - `class BetaSearchResultBlockParam`

        - `content: Array[BetaTextBlockParam]`

          - `text: String`

            minLength: 1

          - `type: :text`

          - `cache_control: BetaCacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `citations: Array[BetaTextCitationParam]`

        - `source: String`

        - `title: String`

        - `type: :search_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `citations: BetaCitationsConfigParam`

      - `class BetaThinkingBlockParam`

        - `signature: String`

          The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

          Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

        - `thinking: String`

          The `thinking` text of this block as returned by the API.

        - `type: :thinking`

      - `class BetaRedactedThinkingBlockParam`

        - `data: String`

          The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

        - `type: :redacted_thinking`

      - `class BetaToolUseBlockParam`

        - `id: String`

          pattern: ^[a-zA-Z0-9_-]+$

        - `input: Hash[Symbol, untyped]`

        - `name: String`

          maxLength: 200, minLength: 1

        - `type: :tool_use`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class BetaDirectCaller`

            Tool invocation directly from the model.

            - `type: :direct`

          - `class BetaServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :code_execution_20250825`

          - `class BetaServerToolCaller20260120`

            - `tool_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :code_execution_20260120`

        - `toolset_name: String`

          For a toolset member tool_use, the toolset family this member belongs to.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class BetaToolResultBlockParam`

        - `tool_use_id: String`

          pattern: ^[a-zA-Z0-9_-]+$

        - `type: :tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `content: String | Array[BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | 3 more]`

          - `String = String`

          - `Content = Array[BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | 3 more]`

            - `class BetaTextBlockParam`

            - `class BetaImageBlockParam`

            - `class BetaSearchResultBlockParam`

            - `class BetaRequestDocumentBlock`

            - `class BetaToolReferenceBlockParam`

              Tool reference block that can be included in tool_result content.

              - `tool_name: String`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `type: :tool_reference`

              - `cache_control: BetaCacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `class BetaBrowserStateBlockParam`

              The caller's browser state after a browser toolset member call —
              the full inventory of open tabs, which tab is active, and any side
              effects (tabs opened, download state changes) the call produced.

              At most one per `tool_result`, only on a non-error result answering a
              browser toolset member `tool_use`. The server renders the
              model-visible text from it; the model never sees the raw fields.

              - `tabs: Array[BetaBrowserStateTabEntry]`

                All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                maxItems: 100

                - `tab_id: String`

                  The caller-assigned identifier for this tab, unique within the inventory.

                  maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `title: String`

                  The title of the page the tab is showing. May be empty.

                  maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `url: String`

                  The URL of the page the tab is showing. May be empty.

                  maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `active: bool`

                  Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

              - `type: :browser_state`

              - `cache_control: BetaCacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `state_changes: Array[BetaBrowserStateChange]`

                Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                maxItems: 200, minItems: 1

                - `class BetaBrowserStateChangeTabOpened`

                  A tab this call's execution opened that remains open at its end —
                  the creation delta of the `tabs` inventory, not an event log.

                  Carries only the `tab_id`; the tab's `title` and `url` live on its
                  `tabs` entry, which must include the same `tab_id`. A tab opened
                  during a failed call gets no deferred `tab_opened`; it simply appears
                  in the next result's `tabs` inventory.

                  - `tab_id: String`

                    The `tab_id` of the opened tab, present in `tabs`.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `type: :tab_opened`

                - `class BetaBrowserStateChangeDownloadStarted`

                  A file download that started during this call.

                  - `download_id: String`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `type: :download_started`

                  - `url: String`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `class BetaBrowserStateChangeDownloadCompleted`

                  A file download that finished during this call, reported with the
                  same `download_id` as its `download_started` — or without a prior
                  `download_started`, when the download finished during the call that
                  started it (at most one state change per `download_id` per result).

                  - `download_id: String`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `type: :download_completed`

                  - `url: String`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `path: String`

                    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                  - `size_bytes: Integer`

                    The completed download's size.

                    minimum: 0

                - `class BetaBrowserStateChangeDownloadFailed`

                  A file download that failed — or was cancelled — during this call.

                  - `download_id: String`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `type: :download_failed`

                  - `url: String`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `error: String`

                    The failure or cancellation detail, when known.

                    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

        - `is_error: bool`

        - `toolset_name: String`

          For a toolset member tool_result, the toolset family of the paired tool_use.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class BetaServerToolUseBlockParam`

        - `id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `input: Hash[Symbol, untyped]`

        - `name: :advisor | :web_search | :web_fetch | 5 more`

          - `:advisor`

          - `:web_search`

          - `:web_fetch`

          - `:code_execution`

          - `:bash_code_execution`

          - `:text_editor_code_execution`

          - `:tool_search_tool_regex`

          - `:tool_search_tool_bm25`

        - `type: :server_tool_use`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class BetaDirectCaller`

            Tool invocation directly from the model.

          - `class BetaServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class BetaServerToolCaller20260120`

      - `class BetaWebSearchToolResultBlockParam`

        - `content: BetaWebSearchToolResultBlockParamContent`

          - `ResultBlock = Array[BetaWebSearchResultBlockParam]`

            - `encrypted_content: String`

            - `title: String`

            - `type: :web_search_result`

            - `url: String`

            - `page_age: String`

          - `class BetaWebSearchToolRequestError`

            - `error_code: BetaWebSearchToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:max_uses_exceeded`

              - `:too_many_requests`

              - `:query_too_long`

              - `:request_too_large`

            - `type: :web_search_tool_result_error`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :web_search_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class BetaDirectCaller`

            Tool invocation directly from the model.

          - `class BetaServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class BetaServerToolCaller20260120`

      - `class BetaWebFetchToolResultBlockParam`

        - `content: BetaWebFetchToolResultErrorBlockParam | BetaWebFetchBlockParam`

          - `class BetaWebFetchToolResultErrorBlockParam`

            - `error_code: BetaWebFetchToolResultErrorCode`

              - `:invalid_tool_input`

              - `:url_too_long`

              - `:url_not_allowed`

              - `:url_not_in_prior_context`

              - `:url_not_accessible`

              - `:unsupported_content_type`

              - `:too_many_requests`

              - `:max_uses_exceeded`

              - `:unavailable`

            - `type: :web_fetch_tool_result_error`

          - `class BetaWebFetchBlockParam`

            - `content: BetaRequestDocumentBlock`

            - `type: :web_fetch_result`

            - `url: String`

              Fetched content URL

            - `retrieved_at: String`

              ISO 8601 timestamp when the content was retrieved

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :web_fetch_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class BetaDirectCaller`

            Tool invocation directly from the model.

          - `class BetaServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class BetaServerToolCaller20260120`

      - `class BetaAdvisorToolResultBlockParam`

        - `content: BetaAdvisorToolResultErrorParam | BetaAdvisorResultBlockParam | BetaAdvisorRedactedResultBlockParam`

          - `class BetaAdvisorToolResultErrorParam`

            - `error_code: :max_uses_exceeded | :prompt_too_long | :too_many_requests | 4 more`

              - `:max_uses_exceeded`

              - `:prompt_too_long`

              - `:too_many_requests`

              - `:overloaded`

              - `:unavailable`

              - `:execution_time_exceeded`

              - `:model_not_found`

            - `type: :advisor_tool_result_error`

          - `class BetaAdvisorResultBlockParam`

            - `text: String`

            - `type: :advisor_result`

            - `stop_reason: String`

          - `class BetaAdvisorRedactedResultBlockParam`

            - `encrypted_content: String`

              Opaque blob produced by a prior response; must be round-tripped verbatim.

            - `type: :advisor_redacted_result`

            - `stop_reason: String`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :advisor_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaCodeExecutionToolResultBlockParam`

        - `content: BetaCodeExecutionToolResultBlockParamContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class BetaCodeExecutionToolResultErrorParam`

            - `error_code: BetaCodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

            - `type: :code_execution_tool_result_error`

          - `class BetaCodeExecutionResultBlockParam`

            - `content: Array[BetaCodeExecutionOutputBlockParam]`

              - `file_id: String`

              - `type: :code_execution_output`

            - `return_code: Integer`

            - `stderr: String`

            - `stdout: String`

            - `type: :code_execution_result`

          - `class BetaEncryptedCodeExecutionResultBlockParam`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array[BetaCodeExecutionOutputBlockParam]`

              - `file_id: String`

              - `type: :code_execution_output`

            - `encrypted_stdout: String`

            - `return_code: Integer`

            - `stderr: String`

            - `type: :encrypted_code_execution_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :code_execution_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaBashCodeExecutionToolResultBlockParam`

        - `content: BetaBashCodeExecutionToolResultErrorParam | BetaBashCodeExecutionResultBlockParam`

          - `class BetaBashCodeExecutionToolResultErrorParam`

            - `error_code: :invalid_tool_input | :unavailable | :too_many_requests | 2 more`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

              - `:output_file_too_large`

            - `type: :bash_code_execution_tool_result_error`

          - `class BetaBashCodeExecutionResultBlockParam`

            - `content: Array[BetaBashCodeExecutionOutputBlockParam]`

              - `file_id: String`

              - `type: :bash_code_execution_output`

            - `return_code: Integer`

            - `stderr: String`

            - `stdout: String`

            - `type: :bash_code_execution_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :bash_code_execution_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaTextEditorCodeExecutionToolResultBlockParam`

        - `content: BetaTextEditorCodeExecutionToolResultErrorParam | BetaTextEditorCodeExecutionViewResultBlockParam | BetaTextEditorCodeExecutionCreateResultBlockParam | BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

          - `class BetaTextEditorCodeExecutionToolResultErrorParam`

            - `error_code: :invalid_tool_input | :unavailable | :too_many_requests | 2 more`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

              - `:file_not_found`

            - `type: :text_editor_code_execution_tool_result_error`

            - `error_message: String`

          - `class BetaTextEditorCodeExecutionViewResultBlockParam`

            - `content: String`

            - `file_type: :text | :image | :pdf`

              - `:text`

              - `:image`

              - `:pdf`

            - `type: :text_editor_code_execution_view_result`

            - `num_lines: Integer`

            - `start_line: Integer`

            - `total_lines: Integer`

          - `class BetaTextEditorCodeExecutionCreateResultBlockParam`

            - `is_file_update: bool`

            - `type: :text_editor_code_execution_create_result`

          - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

            - `type: :text_editor_code_execution_str_replace_result`

            - `lines: Array[String]`

            - `new_lines: Integer`

            - `new_start: Integer`

            - `old_lines: Integer`

            - `old_start: Integer`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :text_editor_code_execution_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaToolSearchToolResultBlockParam`

        - `content: BetaToolSearchToolResultErrorParam | BetaToolSearchToolSearchResultBlockParam`

          - `class BetaToolSearchToolResultErrorParam`

            - `error_code: :invalid_tool_input | :unavailable | :too_many_requests | :execution_time_exceeded`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

            - `type: :tool_search_tool_result_error`

            - `error_message: String`

          - `class BetaToolSearchToolSearchResultBlockParam`

            - `tool_references: Array[BetaToolReferenceBlockParam]`

              - `tool_name: String`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `type: :tool_reference`

              - `cache_control: BetaCacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `type: :tool_search_tool_search_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :tool_search_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaMCPToolUseBlockParam`

        - `id: String`

          pattern: ^[a-zA-Z0-9_-]+$

        - `input: Hash[Symbol, untyped]`

        - `name: String`

        - `server_name: String`

          The name of the MCP server

        - `type: :mcp_tool_use`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaRequestMCPToolResultBlockParam`

        - `tool_use_id: String`

          pattern: ^[a-zA-Z0-9_-]+$

        - `type: :mcp_tool_result`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `content: String | Array[BetaTextBlockParam]`

          - `String = String`

          - `BetaMCPToolResultBlockParamContent = Array[BetaTextBlockParam]`

            - `text: String`

              minLength: 1

            - `type: :text`

            - `cache_control: BetaCacheControlEphemeral`

              Create a cache control breakpoint at this content block.

            - `citations: Array[BetaTextCitationParam]`

        - `is_error: bool`

      - `class BetaContainerUploadBlockParam`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `file_id: String`

        - `type: :container_upload`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaCompactionBlockParam`

        A compaction block containing summary of previous context.

        Users should round-trip these blocks from responses to subsequent requests
        to maintain context across compaction boundaries.

        When content is None, the block represents a failed compaction. The server
        treats these as no-ops. Empty string content is not allowed.

        - `type: :compaction`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `content: String`

          Summary of previously compacted content, or null if compaction failed

        - `encrypted_content: String`

          Opaque metadata from prior compaction, to be round-tripped verbatim

      - `class BetaRequestToolAdditionBlock`

        Mid-conversation directive to surface a declared tool.

        `tool` references a tool (or MCP toolset) by name from the request's
        `tools`; it is offered to the model from this point in the
        conversation onward.

        - `tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference`

          Reference to a single tool the caller declared directly in
          `tools[]`. Does not accept the composed `{server}_{name}` form the
          server assigns to MCP-resolved tools — use `mcp_tool_reference` or
          `mcp_toolset_reference` for those.

          - `class BetaToolChangeToolReference`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `name: String`

              pattern: ^[a-zA-Z0-9_-]{1,128}$

            - `type: :tool_reference`

          - `class BetaToolChangeMCPToolReference`

            Reference to a single MCP tool by its server and remote name — the
            same `server_name`/`name` pair `mcp_tool_use` carries.

            - `name: String`

            - `server_name: String`

            - `type: :mcp_tool_reference`

          - `class BetaToolChangeMCPToolsetReference`

            Reference to every tool in the named MCP server's toolset.

            - `server_name: String`

            - `type: :mcp_toolset_reference`

        - `type: :tool_addition`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaRequestToolRemovalBlock`

        Mid-conversation directive to withdraw a tool.

        `tool` references a tool (or MCP toolset) by name from the request's
        `tools`; it is no longer offered to the model from this point in the
        conversation onward.

        - `tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference`

          Reference to a single tool the caller declared directly in
          `tools[]`. Does not accept the composed `{server}_{name}` form the
          server assigns to MCP-resolved tools — use `mcp_tool_reference` or
          `mcp_toolset_reference` for those.

          - `class BetaToolChangeToolReference`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

          - `class BetaToolChangeMCPToolReference`

            Reference to a single MCP tool by its server and remote name — the
            same `server_name`/`name` pair `mcp_tool_use` carries.

          - `class BetaToolChangeMCPToolsetReference`

            Reference to every tool in the named MCP server's toolset.

        - `type: :tool_removal`

        - `cache_control: BetaCacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BetaFallbackBlockParam`

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

            - `Model = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-mythos-5" | 12 more`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `:"claude-sonnet-5"`

                High-performance model for coding and agents

              - `:"claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `:"claude-mythos-5"`

                Most capable model for cybersecurity and biology research

              - `:"claude-opus-5"`

                Powerful intelligence for long-running agents and coding

              - `:"claude-opus-4-8"`

                Powerful intelligence for long-running agents and coding

              - `:"claude-opus-4-7"`

                Powerful intelligence for long-running agents and coding

              - `:"claude-mythos-preview"`

                New class of intelligence, strongest in coding and cybersecurity

              - `:"claude-opus-4-6"`

                Powerful intelligence for long-running agents and coding

              - `:"claude-sonnet-4-6"`

                Best combination of speed and intelligence

              - `:"claude-haiku-4-5"`

                Fastest model with near-frontier intelligence

              - `:"claude-haiku-4-5-20251001"`

                Fastest model with near-frontier intelligence

              - `:"claude-opus-4-5"`

                Powerful intelligence for long-running agents and coding

              - `:"claude-opus-4-5-20251101"`

                Powerful intelligence for long-running agents and coding

              - `:"claude-sonnet-4-5"`

                High-performance model for agents and coding

              - `:"claude-sonnet-4-5-20250929"`

                High-performance model for agents and coding

            - `String = String`

        - `to: BetaFallbackInfoParam`

          Identifies one hop of a fallback transition.

        - `type: :fallback`

        - `trigger: untyped`

          The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

  - `role: :user | :assistant | :system`

    - `:user`

    - `:assistant`

    - `:system`

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cache_control: BetaCacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `container: BetaContainerParams | String`

  Container identifier for reuse across requests.

  - `class BetaContainerParams`

    Container parameters with skills to be loaded.

    - `id: String`

      Container id

    - `skills: Array[BetaSkillParams]`

      List of skills to load in the container

      maxItems: 20

      - `skill_id: String`

        Skill ID

        maxLength: 64, minLength: 1

      - `type: :anthropic | :custom`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `:anthropic`

        - `:custom`

      - `version: String`

        Skill version or 'latest' for most recent version

        maxLength: 64, minLength: 1

  - `String = String`

- `context_management: BetaContextManagementConfig`

  Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

  - `edits: Array[BetaClearToolUses20250919Edit | BetaClearThinking20251015Edit | BetaCompact20260112Edit]`

    List of context management edits to apply

    minItems: 0

    - `class BetaClearToolUses20250919Edit`

      - `type: :clear_tool_uses_20250919`

      - `clear_at_least: BetaInputTokensClearAtLeast`

        Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

        - `type: :input_tokens`

        - `value: Integer`

          minimum: 0

      - `clear_tool_inputs: bool | Array[String]`

        Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

        - `UnionMember0 = bool`

        - `UnionMember1 = Array[String]`

      - `exclude_tools: Array[String]`

        Tool names whose uses are preserved from clearing

      - `keep: BetaToolUsesKeep`

        Number of tool uses to retain in the conversation

        - `type: :tool_uses`

        - `value: Integer`

          minimum: 0

      - `trigger: BetaInputTokensTrigger | BetaToolUsesTrigger`

        Condition that triggers the context management strategy

        - `class BetaInputTokensTrigger`

          - `type: :input_tokens`

          - `value: Integer`

            minimum: 1

        - `class BetaToolUsesTrigger`

          - `type: :tool_uses`

          - `value: Integer`

            minimum: 1

    - `class BetaClearThinking20251015Edit`

      - `type: :clear_thinking_20251015`

      - `keep: BetaThinkingTurns | BetaAllThinkingTurns | :all`

        Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

        - `class BetaThinkingTurns`

          - `type: :thinking_turns`

          - `value: Integer`

            minimum: 1

        - `class BetaAllThinkingTurns`

          - `type: :all`

        - `Keep = :all`

    - `class BetaCompact20260112Edit`

      Automatically compact older context when reaching the configured trigger threshold.

      - `type: :compact_20260112`

      - `instructions: String`

        Additional instructions for summarization.

      - `pause_after_compaction: bool`

        Whether to pause after compaction and return the compaction block to the user.

      - `trigger: BetaInputTokensTrigger`

        When to trigger compaction. Defaults to 150000 input tokens.

- `diagnostics: BetaDiagnosticsParam`

  Request-level diagnostics. Currently carries the previous response
  id for prompt-cache divergence reporting.

  - `previous_message_id: String`

    The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

    maxLength: 256

- `fallback_credit_token: String | BetaFallbackCreditTokenParam`

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

  - `String = String`

  - `class BetaFallbackCreditTokenParam`

    Object form of `fallback_credit_token`: the token plus a redemption
    mode.

    Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
    header the field accepts the bare string only. The bare string and the
    mode-less object are equivalent (both select `strict`), so wrapping
    an existing token changes nothing by itself.

    - `token: String`

      The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

      maxLength: 2048, minLength: 1

    - `mode: :strict | :best_effort`

      How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

      - `:strict`

      - `:best_effort`

- `fallbacks: BetaFallbacksParam`

  Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

  - `UnionMember0 = Array[BetaFallbackParam]`

    - `model: Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `max_tokens: Integer`

    - `output_config: BetaOutputConfig`

      - `effort: :low | :medium | :high | 2 more`

        All possible effort levels.

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `format_: BetaJSONOutputFormat`

        A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        - `schema: Hash[Symbol, untyped]`

          The JSON schema of the format

        - `type: :json_schema`

      - `task_budget: BetaTokenTaskBudget`

        User-configurable total token budget across contexts.

        - `total: Integer`

          Total token budget across all contexts in the session.

          minimum: 1024

        - `type: :tokens`

          The budget type. Currently only 'tokens' is supported.

        - `remaining: Integer`

          Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

          minimum: 0

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

    - `thinking: BetaThinkingConfigEnabled | BetaThinkingConfigDisabled | BetaThinkingConfigAdaptive`

      - `class BetaThinkingConfigEnabled`

        - `budget_tokens: Integer`

          Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

          Must be ≥1024 and less than `max_tokens`.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

          minimum: 1024

        - `type: :enabled`

        - `display_: :summarized | :omitted | :updates`

          Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

          - `:summarized`

          - `:omitted`

          - `:updates`

      - `class BetaThinkingConfigDisabled`

        - `type: :disabled`

      - `class BetaThinkingConfigAdaptive`

        - `type: :adaptive`

        - `display_: :summarized | :omitted | :updates`

          Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

          - `:summarized`

          - `:omitted`

          - `:updates`

  - `BetaFallbacksParam = :default`

- `inference_geo: String`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `mcp_servers: Array[BetaRequestMCPServerURLDefinition]`

  MCP servers to be utilized in this request

  maxItems: 20

  - `name: String`

  - `type: :url`

  - `url: String`

  - `authorization_token: String`

  - `tool_configuration: BetaRequestMCPServerToolConfiguration`

    - `allowed_tools: Array[String]`

    - `enabled: bool`

- `metadata: BetaMetadata`

  An object describing metadata about the request.

  - `user_id: String`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    maxLength: 512

- `output_config: BetaOutputConfig`

  Configuration options for the model's output, such as the output format.

- `service_tier: :auto | :standard_only`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

  - `:auto`

  - `:standard_only`

- `speed: :standard | :fast`

  Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

  - `:standard`

  - `:fast`

- `stop_sequences: Array[String]`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `stream: bool`

  Whether to incrementally stream the response using server-sent events.

  See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

- `system_: String | Array[BetaTextBlockParam]`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

  - `String = String`

  - `UnionMember1 = Array[BetaTextBlockParam]`

    - `text: String`

      minLength: 1

    - `type: :text`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: Array[BetaTextCitationParam]`

- `thinking: BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `class BetaThinkingConfigEnabled`

  - `class BetaThinkingConfigDisabled`

  - `class BetaThinkingConfigAdaptive`

- `tool_choice: BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `class BetaToolChoiceAuto`

    The model will automatically decide whether to use tools.

    - `type: :auto`

    - `disable_parallel_tool_use: bool`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `class BetaToolChoiceAny`

    The model will use any available tools.

    - `type: :any`

    - `disable_parallel_tool_use: bool`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class BetaToolChoiceTool`

    The model will use the specified tool with `tool_choice.name`.

    - `name: String`

      The name of the tool to use.

    - `type: :tool`

    - `disable_parallel_tool_use: bool`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class BetaToolChoiceNone`

    The model will not be allowed to use tools.

    - `type: :none`

- `tools: Array[BetaToolUnion]`

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

  - `class BetaTool`

    - `input_schema: InputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: :object`

      - `properties: Hash[Symbol, untyped]`

      - `required: Array[String]`

    - `name: String`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description: String`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming: bool`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `type: :custom`

  - `class BetaToolBash20241022`

    - `name: :bash`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :bash_20241022`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolBash20250124`

    - `name: :bash`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :bash_20250124`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20250522`

    - `name: :code_execution`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :code_execution_20250522`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20250825`

    - `name: :code_execution`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :code_execution_20250825`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20260120`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: :code_execution`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :code_execution_20260120`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20260521`

    Code execution tool with REPL state persistence.

    - `name: :code_execution`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :code_execution_20260521`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaBrowserToolset20260801`

    The browser toolset: a single `tools[]` entry (carrying no
    `name`) that declares the browser tool family. The model is served
    the family's tool with any members disabled via `configs` removed
    from its schema.

    - `type: :browser_toolset_20260801`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `configs: BetaBrowserToolsetConfigs`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `close_tab: BetaBrowserCloseTabConfig`

        `close_tab`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: BetaBrowserDoubleClickConfig`

        `double_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `file_upload: BetaBrowserFileUploadConfig`

        `file_upload`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `find: BetaBrowserFindConfig`

        `find`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `form_input: BetaBrowserFormInputConfig`

        `form_input`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `get_page_text: BetaBrowserGetPageTextConfig`

        `get_page_text`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: BetaBrowserHoldKeyConfig`

        `hold_key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hover: BetaBrowserHoverConfig`

        `hover`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `javascript_exec: BetaBrowserJavascriptExecConfig`

        `javascript_exec`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: BetaBrowserKeyConfig`

        `key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: BetaBrowserLeftClickConfig`

        `left_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: BetaBrowserLeftClickDragConfig`

        `left_click_drag`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: BetaBrowserLeftMouseDownConfig`

        `left_mouse_down`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: BetaBrowserLeftMouseUpConfig`

        `left_mouse_up`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `list_tabs: BetaBrowserListTabsConfig`

        `list_tabs`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: BetaBrowserMiddleClickConfig`

        `middle_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: BetaBrowserMouseMoveConfig`

        `mouse_move`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `navigate: BetaBrowserNavigateConfig`

        `navigate`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `new_tab: BetaBrowserNewTabConfig`

        `new_tab`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_console: BetaBrowserReadConsoleConfig`

        `read_console`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_network: BetaBrowserReadNetworkConfig`

        `read_network`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_page: BetaBrowserReadPageConfig`

        `read_page`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: BetaBrowserRightClickConfig`

        `right_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: BetaBrowserScreenshotConfig`

        `screenshot`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: BetaBrowserScrollConfig`

        `scroll`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll_to: BetaBrowserScrollToConfig`

        `scroll_to`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `switch_tab: BetaBrowserSwitchTabConfig`

        `switch_tab`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: BetaBrowserTripleClickConfig`

        `triple_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: BetaBrowserTypeConfig`

        `type`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: BetaBrowserWaitConfig`

        `wait`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: BetaBrowserZoomConfig`

        `zoom`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class BetaToolComputerUse20241022`

    - `display_height_px: Integer`

      The height of the display in pixels.

      minimum: 1

    - `display_width_px: Integer`

      The width of the display in pixels.

      minimum: 1

    - `name: :computer`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :computer_20241022`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `display_number: Integer`

      The X11 display number (e.g. 0, 1) for the display.

      minimum: 0

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaMemoryTool20250818`

    - `name: :memory`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :memory_20250818`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolComputerUse20250124`

    - `display_height_px: Integer`

      The height of the display in pixels.

      minimum: 1

    - `display_width_px: Integer`

      The width of the display in pixels.

      minimum: 1

    - `name: :computer`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :computer_20250124`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `display_number: Integer`

      The X11 display number (e.g. 0, 1) for the display.

      minimum: 0

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20241022`

    - `name: :str_replace_editor`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20241022`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolComputerUse20251124`

    - `display_height_px: Integer`

      The height of the display in pixels.

      minimum: 1

    - `display_width_px: Integer`

      The width of the display in pixels.

      minimum: 1

    - `name: :computer`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :computer_20251124`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `display_number: Integer`

      The X11 display number (e.g. 0, 1) for the display.

      minimum: 0

    - `enable_zoom: bool`

      Whether to enable an action to take a zoomed-in screenshot of the screen.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

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

    - `type: :computer_toolset_20260801`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `configs: BetaComputerToolsetConfigs`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `cursor_position: BetaComputerCursorPositionConfig`

        `cursor_position`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: BetaComputerDoubleClickConfig`

        `double_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: BetaComputerHoldKeyConfig`

        `hold_key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: BetaComputerKeyConfig`

        `key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: BetaComputerLeftClickConfig`

        `left_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: BetaComputerLeftClickDragConfig`

        `left_click_drag`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: BetaComputerLeftMouseDownConfig`

        `left_mouse_down`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: BetaComputerLeftMouseUpConfig`

        `left_mouse_up`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: BetaComputerMiddleClickConfig`

        `middle_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: BetaComputerMouseMoveConfig`

        `mouse_move`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: BetaComputerRightClickConfig`

        `right_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: BetaComputerScreenshotConfig`

        `screenshot`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: BetaComputerScrollConfig`

        `scroll`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: BetaComputerTripleClickConfig`

        `triple_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: BetaComputerTypeConfig`

        `type`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: BetaComputerWaitConfig`

        `wait`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: BetaComputerZoomConfig`

        `zoom`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class BetaToolTextEditor20250124`

    - `name: :str_replace_editor`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20250124`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20250429`

    - `name: :str_replace_based_edit_tool`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20250429`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20250728`

    - `name: :str_replace_based_edit_tool`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20250728`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `max_characters: Integer`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      minimum: 1

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaWebSearchTool20250305`

    - `name: :web_search`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_search_20250305`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: Array[String]`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: BetaUserLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: :approximate`

      - `city: String`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: String`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: String`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: String`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `class BetaWebFetchTool20250910`

    - `name: :web_fetch`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_fetch_20250910`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      List of domains to allow fetching from

    - `blocked_domains: Array[String]`

      List of domains to block fetching from

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: BetaCitationsConfigParam`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: Integer`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaWebSearchTool20260209`

    - `name: :web_search`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_search_20260209`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: Array[String]`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: BetaUserLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20260209`

    - `name: :web_fetch`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_fetch_20260209`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      List of domains to allow fetching from

    - `blocked_domains: Array[String]`

      List of domains to block fetching from

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: BetaCitationsConfigParam`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: Integer`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaWebFetchTool20260309`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `name: :web_fetch`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_fetch_20260309`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      List of domains to allow fetching from

    - `blocked_domains: Array[String]`

      List of domains to block fetching from

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: BetaCitationsConfigParam`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: Integer`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: bool`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class BetaWebSearchTool20260318`

    - `name: :web_search`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_search_20260318`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: Array[String]`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `response_inclusion: :full | :excluded`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `:full`

      - `:excluded`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: BetaUserLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20260318`

    - `name: :web_fetch`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :web_fetch_20260318`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `allowed_domains: Array[String]`

      List of domains to allow fetching from

    - `blocked_domains: Array[String]`

      List of domains to block fetching from

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: BetaCitationsConfigParam`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: Integer`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `response_inclusion: :full | :excluded`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `:full`

      - `:excluded`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: bool`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class BetaAdvisorTool20260301`

    - `model: Model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `name: :advisor`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :advisor_20260301`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `caching: BetaCacheControlEphemeral`

      Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_tokens: Integer`

      Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

      minimum: 1024

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolSearchToolBm25_20251119`

    - `name: :tool_search_tool_bm25`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :tool_search_tool_bm25_20251119 | :tool_search_tool_bm25`

      - `:tool_search_tool_bm25_20251119`

      - `:tool_search_tool_bm25`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolSearchToolRegex20251119`

    - `name: :tool_search_tool_regex`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :tool_search_tool_regex_20251119 | :tool_search_tool_regex`

      - `:tool_search_tool_regex_20251119`

      - `:tool_search_tool_regex`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaMCPToolset`

    Configuration for a group of tools from an MCP server.

    Allows configuring enabled status and defer_loading for all tools
    from an MCP server, with optional per-tool overrides.

    - `mcp_server_name: String`

      Name of the MCP server to configure tools for

      maxLength: 255, minLength: 1

    - `type: :mcp_toolset`

    - `cache_control: BetaCacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `configs: Hash[Symbol, BetaMCPToolConfig]`

      Configuration overrides for specific tools, keyed by tool name

      - `defer_loading: bool`

      - `enabled: bool`

    - `default_config: BetaMCPToolDefaultConfig`

      Default configuration applied to all tools from this server

      - `defer_loading: bool`

      - `enabled: bool`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

- `user_profile_id: String`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

- `output_format: BetaJSONOutputFormat`

  **Deprecated**

  Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

- `temperature: Float`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

  maximum: 1, minimum: 0

- `top_k: Integer`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

  Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

  minimum: 0

- `top_p: Float`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

  maximum: 1, minimum: 0

## Returns

- `class BetaMessage`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: BetaContainer`

    Information about the container used in the request (for the code execution tool)

    - `id: String`

      Identifier for the container used in this request

    - `expires_at: Time`

      The time at which the container will expire.

      format: date-time

    - `skills: Array[BetaSkill]`

      Skills loaded in the container

      - `skill_id: String`

        Skill ID

        maxLength: 64, minLength: 1

      - `type: :anthropic | :custom`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `:anthropic`

        - `:custom`

      - `version: String`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `content: Array[BetaContentBlock]`

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

      - `citations: Array[BetaTextCitation]`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class BetaCitationCharLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_char_index: Integer`

          - `file_id: String`

          - `start_char_index: Integer`

            minimum: 0

          - `type: :char_location`

        - `class BetaCitationPageLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_page_number: Integer`

          - `file_id: String`

          - `start_page_number: Integer`

            minimum: 1

          - `type: :page_location`

        - `class BetaCitationContentBlockLocation`

          - `cited_text: String`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_block_index: Integer`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `file_id: String`

          - `start_block_index: Integer`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `type: :content_block_location`

        - `class BetaCitationsWebSearchResultLocation`

          - `cited_text: String`

          - `encrypted_index: String`

          - `title: String`

            maxLength: 512

          - `type: :web_search_result_location`

          - `url: String`

        - `class BetaCitationSearchResultLocation`

          - `cited_text: String`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `end_block_index: Integer`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `search_result_index: Integer`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `source: String`

          - `start_block_index: Integer`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `title: String`

          - `type: :search_result_location`

      - `text: String`

        maxLength: 5000000, minLength: 0

      - `type: :text`

    - `class BetaThinkingBlock`

      - `signature: String`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `thinking: String`

        The text of Claude's thinking process for this block.

      - `type: :thinking`

    - `class BetaRedactedThinkingBlock`

      - `data: String`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `type: :redacted_thinking`

    - `class BetaToolUseBlock`

      - `id: String`

        pattern: ^[a-zA-Z0-9_-]+$

      - `input: Hash[Symbol, untyped]`

      - `name: String`

        minLength: 1

      - `type: :tool_use`

      - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class BetaDirectCaller`

          Tool invocation directly from the model.

          - `type: :direct`

        - `class BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

          - `tool_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :code_execution_20250825`

        - `class BetaServerToolCaller20260120`

          - `tool_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :code_execution_20260120`

      - `toolset_name: String`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class BetaServerToolUseBlock`

      - `id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `input: Hash[Symbol, untyped]`

      - `name: :advisor | :web_search | :web_fetch | 5 more`

        - `:advisor`

        - `:web_search`

        - `:web_fetch`

        - `:code_execution`

        - `:bash_code_execution`

        - `:text_editor_code_execution`

        - `:tool_search_tool_regex`

        - `:tool_search_tool_bm25`

      - `type: :server_tool_use`

      - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class BetaDirectCaller`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120`

    - `class BetaWebSearchToolResultBlock`

      - `content: BetaWebSearchToolResultBlockContent`

        - `class BetaWebSearchToolResultError`

          - `error_code: BetaWebSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:max_uses_exceeded`

            - `:too_many_requests`

            - `:query_too_long`

            - `:request_too_large`

          - `type: :web_search_tool_result_error`

        - `UnionMember1 = Array[BetaWebSearchResultBlock]`

          - `encrypted_content: String`

          - `page_age: String`

          - `title: String`

          - `type: :web_search_result`

          - `url: String`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :web_search_tool_result`

      - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class BetaDirectCaller`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120`

    - `class BetaWebFetchToolResultBlock`

      - `content: BetaWebFetchToolResultErrorBlock | BetaWebFetchBlock`

        - `class BetaWebFetchToolResultErrorBlock`

          - `error_code: BetaWebFetchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:url_too_long`

            - `:url_not_allowed`

            - `:url_not_in_prior_context`

            - `:url_not_accessible`

            - `:unsupported_content_type`

            - `:too_many_requests`

            - `:max_uses_exceeded`

            - `:unavailable`

          - `type: :web_fetch_tool_result_error`

        - `class BetaWebFetchBlock`

          - `content: BetaDocumentBlock`

            - `citations: BetaCitationConfig`

              Citation configuration for the document

              - `enabled: bool`

            - `source: BetaBase64PDFSource | BetaPlainTextSource`

              - `class BetaBase64PDFSource`

                - `data: String`

                  format: byte

                - `media_type: :"application/pdf"`

                - `type: :base64`

              - `class BetaPlainTextSource`

                - `data: String`

                - `media_type: :"text/plain"`

                - `type: :text`

            - `title: String`

              The title of the document

            - `type: :document`

          - `retrieved_at: String`

            ISO 8601 timestamp when the content was retrieved

          - `type: :web_fetch_result`

          - `url: String`

            Fetched content URL

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :web_fetch_tool_result`

      - `caller_: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class BetaDirectCaller`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120`

    - `class BetaAdvisorToolResultBlock`

      - `content: BetaAdvisorToolResultError | BetaAdvisorResultBlock | BetaAdvisorRedactedResultBlock`

        - `class BetaAdvisorToolResultError`

          - `error_code: :max_uses_exceeded | :prompt_too_long | :too_many_requests | 4 more`

            - `:max_uses_exceeded`

            - `:prompt_too_long`

            - `:too_many_requests`

            - `:overloaded`

            - `:unavailable`

            - `:execution_time_exceeded`

            - `:model_not_found`

          - `type: :advisor_tool_result_error`

        - `class BetaAdvisorResultBlock`

          - `stop_reason: String`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

          - `text: String`

          - `type: :advisor_result`

        - `class BetaAdvisorRedactedResultBlock`

          - `encrypted_content: String`

            Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

          - `stop_reason: String`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

          - `type: :advisor_redacted_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :advisor_tool_result`

    - `class BetaCodeExecutionToolResultBlock`

      - `content: BetaCodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class BetaCodeExecutionToolResultError`

          - `error_code: BetaCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `type: :code_execution_tool_result_error`

        - `class BetaCodeExecutionResultBlock`

          - `content: Array[BetaCodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :code_execution_result`

        - `class BetaEncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array[BetaCodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `encrypted_stdout: String`

          - `return_code: Integer`

          - `stderr: String`

          - `type: :encrypted_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :code_execution_tool_result`

    - `class BetaBashCodeExecutionToolResultBlock`

      - `content: BetaBashCodeExecutionToolResultError | BetaBashCodeExecutionResultBlock`

        - `class BetaBashCodeExecutionToolResultError`

          - `error_code: :invalid_tool_input | :unavailable | :too_many_requests | 2 more`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:output_file_too_large`

          - `type: :bash_code_execution_tool_result_error`

        - `class BetaBashCodeExecutionResultBlock`

          - `content: Array[BetaBashCodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :bash_code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :bash_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :bash_code_execution_tool_result`

    - `class BetaTextEditorCodeExecutionToolResultBlock`

      - `content: BetaTextEditorCodeExecutionToolResultError | BetaTextEditorCodeExecutionViewResultBlock | BetaTextEditorCodeExecutionCreateResultBlock | BetaTextEditorCodeExecutionStrReplaceResultBlock`

        - `class BetaTextEditorCodeExecutionToolResultError`

          - `error_code: :invalid_tool_input | :unavailable | :too_many_requests | 2 more`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:file_not_found`

          - `error_message: String`

          - `type: :text_editor_code_execution_tool_result_error`

        - `class BetaTextEditorCodeExecutionViewResultBlock`

          - `content: String`

          - `file_type: :text | :image | :pdf`

            - `:text`

            - `:image`

            - `:pdf`

          - `num_lines: Integer`

          - `start_line: Integer`

          - `total_lines: Integer`

          - `type: :text_editor_code_execution_view_result`

        - `class BetaTextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: bool`

          - `type: :text_editor_code_execution_create_result`

        - `class BetaTextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array[String]`

          - `new_lines: Integer`

          - `new_start: Integer`

          - `old_lines: Integer`

          - `old_start: Integer`

          - `type: :text_editor_code_execution_str_replace_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :text_editor_code_execution_tool_result`

    - `class BetaToolSearchToolResultBlock`

      - `content: BetaToolSearchToolResultError | BetaToolSearchToolSearchResultBlock`

        - `class BetaToolSearchToolResultError`

          - `error_code: :invalid_tool_input | :unavailable | :too_many_requests | :execution_time_exceeded`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `error_message: String`

          - `type: :tool_search_tool_result_error`

        - `class BetaToolSearchToolSearchResultBlock`

          - `tool_references: Array[BetaToolReferenceBlock]`

            - `tool_name: String`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `type: :tool_reference`

          - `type: :tool_search_tool_search_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :tool_search_tool_result`

    - `class BetaMCPToolUseBlock`

      - `id: String`

        pattern: ^[a-zA-Z0-9_-]+$

      - `input: Hash[Symbol, untyped]`

      - `name: String`

        The name of the MCP tool

      - `server_name: String`

        The name of the MCP server

      - `type: :mcp_tool_use`

    - `class BetaMCPToolResultBlock`

      - `content: String | Array[BetaTextBlock]`

        - `String = String`

        - `BetaMCPToolResultBlockContent = Array[BetaTextBlock]`

          - `citations: Array[BetaTextCitation]`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `text: String`

            maxLength: 5000000, minLength: 0

          - `type: :text`

      - `is_error: bool`

      - `tool_use_id: String`

        pattern: ^[a-zA-Z0-9_-]+$

      - `type: :mcp_tool_result`

    - `class BetaContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: String`

      - `type: :container_upload`

    - `class BetaCompactionBlock`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `content: String`

        Summary of compacted content, or null if compaction failed

      - `encrypted_content: String`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `type: :compaction`

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

      - `from: BetaFallbackInfo`

        The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Model = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-mythos-5" | 12 more`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-mythos-5"`

              Most capable model for cybersecurity and biology research

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-mythos-preview"`

              New class of intelligence, strongest in coding and cybersecurity

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

      - `to: BetaFallbackInfo`

        The fallback model producing the content that follows this block. Its `model` is always the canonical id.

      - `trigger: BetaFallbackRefusalTrigger`

        What caused the `from` model to hand over at this hop.

        - `category: :cyber | :bio | :frontier_llm | 2 more`

          The policy category that triggered a refusal.

          - `:cyber`

            The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

          - `:bio`

            The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

          - `:frontier_llm`

            The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

          - `:reasoning_extraction`

            The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

          - `:general_harms`

            The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

        - `type: :refusal`

      - `type: :fallback`

  - `context_management: BetaContextManagementResponse`

    Context management response.

    Information about context management strategies applied during the request.

    - `applied_edits: Array[BetaClearToolUses20250919EditResponse | BetaClearThinking20251015EditResponse]`

      List of context management edits that were applied.

      - `class BetaClearToolUses20250919EditResponse`

        - `cleared_input_tokens: Integer`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `cleared_tool_uses: Integer`

          Number of tool uses that were cleared.

          minimum: 0

        - `type: :clear_tool_uses_20250919`

          The type of context management edit applied.

      - `class BetaClearThinking20251015EditResponse`

        - `cleared_input_tokens: Integer`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `cleared_thinking_turns: Integer`

          Number of thinking turns that were cleared.

          minimum: 0

        - `type: :clear_thinking_20251015`

          The type of context management edit applied.

  - `diagnostics: BetaDiagnostics`

    Response envelope for request-level diagnostics. Present (possibly
    null) whenever the caller supplied `diagnostics` on the request.

    - `cache_miss_reason: BetaCacheMissModelChanged | BetaCacheMissSystemChanged | BetaCacheMissToolsChanged | 3 more`

      Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

      - `class BetaCacheMissModelChanged`

        - `cache_missed_input_tokens: Integer`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `type: :model_changed`

      - `class BetaCacheMissSystemChanged`

        - `cache_missed_input_tokens: Integer`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `type: :system_changed`

      - `class BetaCacheMissToolsChanged`

        - `cache_missed_input_tokens: Integer`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `type: :tools_changed`

      - `class BetaCacheMissMessagesChanged`

        - `cache_missed_input_tokens: Integer`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `type: :messages_changed`

      - `class BetaCacheMissPreviousMessageNotFound`

        - `type: :previous_message_not_found`

      - `class BetaCacheMissUnavailable`

        - `type: :unavailable`

  - `model: Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `role: :assistant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `stop_details: BetaRefusalStopDetails`

    Structured information about a refusal.

    - `category: :cyber | :bio | :frontier_llm | 2 more`

      The policy category that triggered a refusal.

      - `:cyber`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `:bio`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `:frontier_llm`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `:reasoning_extraction`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `:general_harms`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `explanation: String`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `fallback_credit_token: String`

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

    - `fallback_has_prefill_claim: bool`

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

    - `recommended_model: String`

      The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

    - `type: :refusal`

  - `stop_reason: BetaStopReason`

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

    - `:end_turn`

    - `:max_tokens`

    - `:stop_sequence`

    - `:tool_use`

    - `:pause_turn`

    - `:compaction`

    - `:refusal`

    - `:model_context_window_exceeded`

  - `stop_sequence: String`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: :message`

    Object type.

    For Messages, this is always `"message"`.

  - `usage: BetaUsage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: BetaCacheCreation`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: Integer`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `ephemeral_5m_input_tokens: Integer`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `cache_creation_input_tokens: Integer`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `cache_read_input_tokens: Integer`

      The number of input tokens read from the cache.

      minimum: 0

    - `fallback_credit: BetaFallbackCreditUsage`

      Outcome of the `fallback_credit_token` presented on this request.

      - `status: BetaFallbackCreditRedeemed | BetaFallbackCreditNotApplied`

        Whether the fallback-credit reprice was applied to this response's billing.

        A union discriminated on `type`. `redeemed`: the retry is billed as if
        the conversation had been on the retry model all along — including when the
        resulting shift is zero because there was nothing to move. `not_applied`:
        no reprice was applied; the arm's `reason` says why.

        - `class BetaFallbackCreditRedeemed`

          The reprice was applied: the retry is billed as if the conversation
          had been on the retry model all along.

          - `type: :redeemed`

        - `class BetaFallbackCreditNotApplied`

          No reprice was applied; `reason` says why.

          - `reason: :body_mismatch | :continuation_excluded | :continuation_only | 9 more`

            Why the reprice was not applied.

            A closed enum; additions to the redemption-check vocabulary arrive as
            deliberate schema updates.

            - `:body_mismatch`

            - `:continuation_excluded`

            - `:continuation_only`

            - `:expired`

            - `:invalid_target_model`

            - `:not_enabled`

            - `:reprice_unavailable`

            - `:temporarily_unavailable`

            - `:variant_fields_present`

            - `:wrong_organization`

            - `:wrong_platform`

            - `:wrong_workspace`

          - `type: :not_applied`

          - `remove_to_redeem: Array[String]`

            Request fields to remove before retrying, so the retry can redeem this
            token.

            Present exactly when `reason` is `variant_fields_present` — never null,
            never an empty array; absent otherwise. Fields are named only from your own request, and only after
            the sealed variant hash matched. A served best-effort retry has already
            been billed at normal price; nothing redeems retroactively, but a corrected
            re-send inside the token's five-minute window can still redeem.

    - `inference_geo: String`

      The geographic region where inference was performed for this request.

    - `input_tokens: Integer`

      The number of input tokens which were used.

      minimum: 0

    - `iterations: BetaIterationsUsage`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the context window size from the last `message` entry
      - Understand token accumulation across server-side tool use loops

      A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `class BetaMessageIterationUsage`

        Token usage for a sampling iteration.

        - `cache_creation: BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `cache_creation_input_tokens: Integer`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `cache_read_input_tokens: Integer`

          The number of input tokens read from the cache.

          minimum: 0

        - `input_tokens: Integer`

          The number of input tokens which were used.

          minimum: 0

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `output_tokens: Integer`

          The number of output tokens which were used.

          minimum: 0

        - `type: :message`

          Usage for a sampling iteration

      - `class BetaCompactionIterationUsage`

        Token usage for a compaction iteration.

        - `cache_creation: BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `cache_creation_input_tokens: Integer`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `cache_read_input_tokens: Integer`

          The number of input tokens read from the cache.

          minimum: 0

        - `input_tokens: Integer`

          The number of input tokens which were used.

          minimum: 0

        - `output_tokens: Integer`

          The number of output tokens which were used.

          minimum: 0

        - `type: :compaction`

          Usage for a compaction iteration

      - `class BetaAdvisorMessageIterationUsage`

        Token usage for an advisor sub-inference iteration.

        - `cache_creation: BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `cache_creation_input_tokens: Integer`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `cache_read_input_tokens: Integer`

          The number of input tokens read from the cache.

          minimum: 0

        - `input_tokens: Integer`

          The number of input tokens which were used.

          minimum: 0

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `output_tokens: Integer`

          The number of output tokens which were used.

          minimum: 0

        - `type: :advisor_message`

          Usage for an advisor sub-inference iteration

      - `class BetaFallbackMessageIterationUsage`

        Token usage for the fallback-model attempt of a server-side fallback request.

        Produced in place of a `message` entry for whichever hop served the
        response. A declined hop produces the existing `message` entry. Whether
        a fallback model served the response is signalled by the presence of this
        entry in `usage.iterations`.

        - `cache_creation: BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `cache_creation_input_tokens: Integer`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `cache_read_input_tokens: Integer`

          The number of input tokens read from the cache.

          minimum: 0

        - `input_tokens: Integer`

          The number of input tokens which were used.

          minimum: 0

        - `model: Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `output_tokens: Integer`

          The number of output tokens which were used.

          minimum: 0

        - `type: :fallback_message`

          Usage for the fallback-model attempt that served the response

    - `output_tokens: Integer`

      The number of output tokens which were used.

      minimum: 0

    - `output_tokens_details: BetaOutputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `thinking_tokens: Integer`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `server_tool_use: BetaServerToolUsage`

      The number of server tool requests.

      - `web_fetch_requests: Integer`

        The number of web fetch tool requests.

        minimum: 0

      - `web_search_requests: Integer`

        The number of web search tool requests.

        minimum: 0

    - `service_tier: :standard | :priority | :batch`

      If the request used the priority, standard, or batch tier.

      - `:standard`

      - `:priority`

      - `:batch`

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `BetaRawMessageStreamEvent = BetaRawMessageStartEvent | BetaRawMessageDeltaEvent | BetaRawMessageStopEvent | 3 more`

  - `class BetaRawMessageStartEvent`

    - `message: BetaMessage`

    - `type: :message_start`

  - `class BetaRawMessageDeltaEvent`

    - `context_management: BetaContextManagementResponse`

      Information about context management strategies applied during the request

    - `delta: Delta`

      - `container: BetaContainer`

        Information about the container used in the request (for the code execution tool)

      - `stop_details: BetaRefusalStopDetails`

        Structured information about a refusal.

      - `stop_reason: BetaStopReason`

      - `stop_sequence: String`

    - `type: :message_delta`

    - `usage: BetaMessageDeltaUsage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation_input_tokens: Integer`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `cache_read_input_tokens: Integer`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `fallback_credit: BetaFallbackCreditUsage`

        Outcome of the `fallback_credit_token` presented on this request.

      - `input_tokens: Integer`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `iterations: BetaIterationsUsage`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the context window size from the last `message` entry
        - Understand token accumulation across server-side tool use loops

        A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `output_tokens: Integer`

        The cumulative number of output tokens which were used.

      - `output_tokens_details: BetaOutputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `server_tool_use: BetaServerToolUsage`

        The number of server tool requests.

  - `class BetaRawMessageStopEvent`

    - `type: :message_stop`

  - `class BetaRawContentBlockStartEvent`

    - `content_block: BetaTextBlock | BetaThinkingBlock | BetaRedactedThinkingBlock | 14 more`

      Response model for a file uploaded to the container.

      - `class BetaTextBlock`

      - `class BetaThinkingBlock`

      - `class BetaRedactedThinkingBlock`

      - `class BetaToolUseBlock`

      - `class BetaServerToolUseBlock`

      - `class BetaWebSearchToolResultBlock`

      - `class BetaWebFetchToolResultBlock`

      - `class BetaAdvisorToolResultBlock`

      - `class BetaCodeExecutionToolResultBlock`

      - `class BetaBashCodeExecutionToolResultBlock`

      - `class BetaTextEditorCodeExecutionToolResultBlock`

      - `class BetaToolSearchToolResultBlock`

      - `class BetaMCPToolUseBlock`

      - `class BetaMCPToolResultBlock`

      - `class BetaContainerUploadBlock`

        Response model for a file uploaded to the container.

      - `class BetaCompactionBlock`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

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

    - `index: Integer`

    - `type: :content_block_start`

  - `class BetaRawContentBlockDeltaEvent`

    - `delta: BetaRawContentBlockDelta`

      - `class BetaTextDelta`

        - `text: String`

        - `type: :text_delta`

      - `class BetaInputJSONDelta`

        - `partial_json: String`

        - `type: :input_json_delta`

      - `class BetaCitationsDelta`

        - `citation: BetaCitationCharLocation | BetaCitationPageLocation | BetaCitationContentBlockLocation | 2 more`

          - `class BetaCitationCharLocation`

          - `class BetaCitationPageLocation`

          - `class BetaCitationContentBlockLocation`

          - `class BetaCitationsWebSearchResultLocation`

          - `class BetaCitationSearchResultLocation`

        - `type: :citations_delta`

      - `class BetaThinkingDelta`

        - `estimated_tokens: Integer`

          Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

        - `thinking: String`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `type: :thinking_delta`

      - `class BetaSignatureDelta`

        - `signature: String`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `type: :signature_delta`

      - `class BetaCompactionContentBlockDelta`

        - `content: String`

        - `encrypted_content: String`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `type: :compaction_delta`

    - `index: Integer`

    - `type: :content_block_delta`

  - `class BetaRawContentBlockStopEvent`

    - `index: Integer`

    - `type: :content_block_stop`

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_message = anthropic.beta.messages.create(
  max_tokens: 1024,
  messages: [{content: "Hello, world", role: :user}],
  model: Anthropic::Model::CLAUDE_OPUS_5
)

puts(beta_message)
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
        "model": "claude-sonnet-5",
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
  }
}
```
