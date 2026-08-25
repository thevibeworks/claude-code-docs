# Count tokens in a Message

`messages.count_tokens(**kwargs) -> MessageTokensCount`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

## Parameters

- `messages: Array[MessageParam]`

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

  - `content: String | Array[ContentBlockParam]`

    - `String = String`

    - `UnionMember1 = Array[ContentBlockParam]`

      - `class TextBlockParam`

        - `text: String`

          minLength: 1

        - `type: :text`

        - `cache_control: CacheControlEphemeral`

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

        - `citations: Array[TextCitationParam]`

          - `class CitationCharLocationParam`

            - `cited_text: String`

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

              maxLength: 500, minLength: 1

            - `end_char_index: Integer`

            - `start_char_index: Integer`

              minimum: 0

            - `type: :char_location`

          - `class CitationPageLocationParam`

            - `cited_text: String`

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

              maxLength: 500, minLength: 1

            - `end_page_number: Integer`

            - `start_page_number: Integer`

              minimum: 1

            - `type: :page_location`

          - `class CitationContentBlockLocationParam`

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

          - `class CitationWebSearchResultLocationParam`

            - `cited_text: String`

            - `encrypted_index: String`

            - `title: String`

              maxLength: 512, minLength: 1

            - `type: :web_search_result_location`

            - `url: String`

              minLength: 1

          - `class CitationSearchResultLocationParam`

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

      - `class ImageBlockParam`

        - `source: Base64ImageSource | URLImageSource | FileImageSource`

          - `class Base64ImageSource`

            - `data: String`

              format: byte

            - `media_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"`

              - `:"image/jpeg"`

              - `:"image/png"`

              - `:"image/gif"`

              - `:"image/webp"`

            - `type: :base64`

          - `class URLImageSource`

            - `type: :url`

            - `url: String`

          - `class FileImageSource`

            - `file_id: String`

            - `type: :file`

        - `type: :image`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `transformations: ImageTransformationsParam`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `oversized_image: :downsize | :error`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `:downsize`

            - `:error`

      - `class DocumentBlockParam`

        - `source: Base64PDFSource | PlainTextSource | ContentBlockSource | 2 more`

          - `class Base64PDFSource`

            - `data: String`

              format: byte

            - `media_type: :"application/pdf"`

            - `type: :base64`

          - `class PlainTextSource`

            - `data: String`

            - `media_type: :"text/plain"`

            - `type: :text`

          - `class ContentBlockSource`

            - `content: String | Array[ContentBlockSourceContent]`

              - `String = String`

              - `ContentBlockSourceContent = Array[ContentBlockSourceContent]`

                - `class TextBlockParam`

                - `class ImageBlockParam`

            - `type: :content`

          - `class URLPDFSource`

            - `type: :url`

            - `url: String`

          - `class FileDocumentSource`

            - `file_id: String`

            - `type: :file`

        - `type: :document`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `citations: CitationsConfigParam`

          - `enabled: bool`

        - `context: String`

          minLength: 1

        - `title: String`

          maxLength: 500, minLength: 1

      - `class SearchResultBlockParam`

        - `content: Array[TextBlockParam]`

          - `text: String`

            minLength: 1

          - `type: :text`

          - `cache_control: CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `citations: Array[TextCitationParam]`

        - `source: String`

        - `title: String`

        - `type: :search_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `citations: CitationsConfigParam`

      - `class ThinkingBlockParam`

        - `signature: String`

          The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

          Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

        - `thinking: String`

          The `thinking` text of this block as returned by the API.

        - `type: :thinking`

      - `class RedactedThinkingBlockParam`

        - `data: String`

          The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

        - `type: :redacted_thinking`

      - `class ToolUseBlockParam`

        - `id: String`

          pattern: ^[a-zA-Z0-9_-]+$

        - `input: Hash[Symbol, untyped]`

        - `name: String`

          maxLength: 200, minLength: 1

        - `type: :tool_use`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

            - `type: :direct`

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

            - `tool_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :code_execution_20250825`

          - `class ServerToolCaller20260120`

            - `tool_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :code_execution_20260120`

        - `toolset_name: String`

          For a toolset member tool_use, the toolset family this member belongs to.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class ToolResultBlockParam`

        - `tool_use_id: String`

          pattern: ^[a-zA-Z0-9_-]+$

        - `type: :tool_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `content: String | Array[TextBlockParam | ImageBlockParam | SearchResultBlockParam | 3 more]`

          - `String = String`

          - `Content = Array[TextBlockParam | ImageBlockParam | SearchResultBlockParam | 3 more]`

            - `class TextBlockParam`

            - `class ImageBlockParam`

            - `class SearchResultBlockParam`

            - `class DocumentBlockParam`

            - `class ToolReferenceBlockParam`

              Tool reference block that can be included in tool_result content.

              - `tool_name: String`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `type: :tool_reference`

              - `cache_control: CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `class BrowserStateBlockParam`

              The caller's browser state after a browser toolset member call —
              the full inventory of open tabs, which tab is active, and any side
              effects (tabs opened, download state changes) the call produced.

              At most one per `tool_result`, only on a non-error result answering a
              browser toolset member `tool_use`. The server renders the
              model-visible text from it; the model never sees the raw fields.

              - `tabs: Array[BrowserStateTabEntry]`

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

              - `cache_control: CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `state_changes: Array[BrowserStateChange]`

                Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                maxItems: 200, minItems: 1

                - `class BrowserStateChangeTabOpened`

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

                - `class BrowserStateChangeDownloadStarted`

                  A file download that started during this call.

                  - `download_id: String`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `type: :download_started`

                  - `url: String`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `class BrowserStateChangeDownloadCompleted`

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

                - `class BrowserStateChangeDownloadFailed`

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

      - `class ServerToolUseBlockParam`

        - `id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `input: Hash[Symbol, untyped]`

        - `name: :web_search | :web_fetch | :code_execution | 4 more`

          - `:web_search`

          - `:web_fetch`

          - `:code_execution`

          - `:bash_code_execution`

          - `:text_editor_code_execution`

          - `:tool_search_tool_regex`

          - `:tool_search_tool_bm25`

        - `type: :server_tool_use`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120`

      - `class WebSearchToolResultBlockParam`

        - `content: WebSearchToolResultBlockParamContent`

          - `WebSearchToolResultBlockItem = Array[WebSearchResultBlockParam]`

            - `encrypted_content: String`

            - `title: String`

            - `type: :web_search_result`

            - `url: String`

            - `page_age: String`

          - `class WebSearchToolRequestError`

            - `error_code: WebSearchToolResultErrorCode`

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

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120`

      - `class WebFetchToolResultBlockParam`

        - `content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam`

          - `class WebFetchToolResultErrorBlockParam`

            - `error_code: WebFetchToolResultErrorCode`

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

          - `class WebFetchBlockParam`

            - `content: DocumentBlockParam`

            - `type: :web_fetch_result`

            - `url: String`

              Fetched content URL

            - `retrieved_at: String`

              ISO 8601 timestamp when the content was retrieved

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :web_fetch_tool_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120`

      - `class CodeExecutionToolResultBlockParam`

        - `content: CodeExecutionToolResultBlockParamContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultErrorParam`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

            - `type: :code_execution_tool_result_error`

          - `class CodeExecutionResultBlockParam`

            - `content: Array[CodeExecutionOutputBlockParam]`

              - `file_id: String`

              - `type: :code_execution_output`

            - `return_code: Integer`

            - `stderr: String`

            - `stdout: String`

            - `type: :code_execution_result`

          - `class EncryptedCodeExecutionResultBlockParam`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array[CodeExecutionOutputBlockParam]`

              - `file_id: String`

              - `type: :code_execution_output`

            - `encrypted_stdout: String`

            - `return_code: Integer`

            - `stderr: String`

            - `type: :encrypted_code_execution_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :code_execution_tool_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class BashCodeExecutionToolResultBlockParam`

        - `content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam`

          - `class BashCodeExecutionToolResultErrorParam`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

              - `:output_file_too_large`

            - `type: :bash_code_execution_tool_result_error`

          - `class BashCodeExecutionResultBlockParam`

            - `content: Array[BashCodeExecutionOutputBlockParam]`

              - `file_id: String`

              - `type: :bash_code_execution_output`

            - `return_code: Integer`

            - `stderr: String`

            - `stdout: String`

            - `type: :bash_code_execution_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :bash_code_execution_tool_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class TextEditorCodeExecutionToolResultBlockParam`

        - `content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam`

          - `class TextEditorCodeExecutionToolResultErrorParam`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

              - `:file_not_found`

            - `type: :text_editor_code_execution_tool_result_error`

            - `error_message: String`

          - `class TextEditorCodeExecutionViewResultBlockParam`

            - `content: String`

            - `file_type: :text | :image | :pdf`

              - `:text`

              - `:image`

              - `:pdf`

            - `type: :text_editor_code_execution_view_result`

            - `num_lines: Integer`

            - `start_line: Integer`

            - `total_lines: Integer`

          - `class TextEditorCodeExecutionCreateResultBlockParam`

            - `is_file_update: bool`

            - `type: :text_editor_code_execution_create_result`

          - `class TextEditorCodeExecutionStrReplaceResultBlockParam`

            - `type: :text_editor_code_execution_str_replace_result`

            - `lines: Array[String]`

            - `new_lines: Integer`

            - `new_start: Integer`

            - `old_lines: Integer`

            - `old_start: Integer`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :text_editor_code_execution_tool_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class ToolSearchToolResultBlockParam`

        - `content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam`

          - `class ToolSearchToolResultErrorParam`

            - `error_code: ToolSearchToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

            - `type: :tool_search_tool_result_error`

            - `error_message: String`

          - `class ToolSearchToolSearchResultBlockParam`

            - `tool_references: Array[ToolReferenceBlockParam]`

              - `tool_name: String`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `type: :tool_reference`

              - `cache_control: CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `type: :tool_search_tool_search_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :tool_search_tool_result`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

      - `class ContainerUploadBlockParam`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `file_id: String`

        - `type: :container_upload`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

  - `role: :user | :assistant | :system`

    - `:user`

    - `:assistant`

    - `:system`

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

- `cache_control: CacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `output_config: OutputConfig`

  Configuration options for the model's output, such as the output format.

  - `effort: :low | :medium | :high | 2 more`

    All possible effort levels.

    - `:low`

    - `:medium`

    - `:high`

    - `:xhigh`

    - `:max`

  - `format_: JSONOutputFormat`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `schema: Hash[Symbol, untyped]`

      The JSON schema of the format

    - `type: :json_schema`

- `system_: String | Array[TextBlockParam]`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

  - `String = String`

  - `UnionMember1 = Array[TextBlockParam]`

    - `text: String`

      minLength: 1

    - `type: :text`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: Array[TextCitationParam]`

- `thinking: ThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `class ThinkingConfigEnabled`

    - `budget_tokens: Integer`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      minimum: 1024

    - `type: :enabled`

    - `display_: :summarized | :omitted`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `:summarized`

      - `:omitted`

  - `class ThinkingConfigDisabled`

    - `type: :disabled`

  - `class ThinkingConfigAdaptive`

    - `type: :adaptive`

    - `display_: :summarized | :omitted`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `:summarized`

      - `:omitted`

- `tool_choice: ToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `class ToolChoiceAuto`

    The model will automatically decide whether to use tools.

    - `type: :auto`

    - `disable_parallel_tool_use: bool`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `class ToolChoiceAny`

    The model will use any available tools.

    - `type: :any`

    - `disable_parallel_tool_use: bool`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceTool`

    The model will use the specified tool with `tool_choice.name`.

    - `name: String`

      The name of the tool to use.

    - `type: :tool`

    - `disable_parallel_tool_use: bool`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceNone`

    The model will not be allowed to use tools.

    - `type: :none`

- `tools: Array[MessageCountTokensTool]`

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

  - `class Tool`

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

    - `cache_control: CacheControlEphemeral`

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

  - `class ToolBash20250124`

    - `name: :bash`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :bash_20250124`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250522`

    - `name: :code_execution`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :code_execution_20250522`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250825`

    - `name: :code_execution`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :code_execution_20250825`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260120`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260521`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class BrowserToolset20260801`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `configs: BrowserToolsetConfigs`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `close_tab: BrowserCloseTabConfig`

        `close_tab`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: BrowserDoubleClickConfig`

        `double_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `file_upload: BrowserFileUploadConfig`

        `file_upload`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `find: BrowserFindConfig`

        `find`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `form_input: BrowserFormInputConfig`

        `form_input`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `get_page_text: BrowserGetPageTextConfig`

        `get_page_text`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: BrowserHoldKeyConfig`

        `hold_key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hover: BrowserHoverConfig`

        `hover`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `javascript_exec: BrowserJavascriptExecConfig`

        `javascript_exec`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: BrowserKeyConfig`

        `key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: BrowserLeftClickConfig`

        `left_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: BrowserLeftClickDragConfig`

        `left_click_drag`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: BrowserLeftMouseDownConfig`

        `left_mouse_down`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: BrowserLeftMouseUpConfig`

        `left_mouse_up`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `list_tabs: BrowserListTabsConfig`

        `list_tabs`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: BrowserMiddleClickConfig`

        `middle_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: BrowserMouseMoveConfig`

        `mouse_move`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `navigate: BrowserNavigateConfig`

        `navigate`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `new_tab: BrowserNewTabConfig`

        `new_tab`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_console: BrowserReadConsoleConfig`

        `read_console`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_network: BrowserReadNetworkConfig`

        `read_network`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_page: BrowserReadPageConfig`

        `read_page`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: BrowserRightClickConfig`

        `right_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: BrowserScreenshotConfig`

        `screenshot`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: BrowserScrollConfig`

        `scroll`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll_to: BrowserScrollToConfig`

        `scroll_to`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `switch_tab: BrowserSwitchTabConfig`

        `switch_tab`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: BrowserTripleClickConfig`

        `triple_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: BrowserTypeConfig`

        `type`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: BrowserWaitConfig`

        `wait`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: BrowserZoomConfig`

        `zoom`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class MemoryTool20250818`

    - `name: :memory`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :memory_20250818`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class ComputerToolset20260801`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `configs: ComputerToolsetConfigs`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `cursor_position: ComputerCursorPositionConfig`

        `cursor_position`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: ComputerDoubleClickConfig`

        `double_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: ComputerHoldKeyConfig`

        `hold_key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: ComputerKeyConfig`

        `key`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: ComputerLeftClickConfig`

        `left_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: ComputerLeftClickDragConfig`

        `left_click_drag`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: ComputerLeftMouseDownConfig`

        `left_mouse_down`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: ComputerLeftMouseUpConfig`

        `left_mouse_up`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: ComputerMiddleClickConfig`

        `middle_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: ComputerMouseMoveConfig`

        `mouse_move`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: ComputerRightClickConfig`

        `right_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: ComputerScreenshotConfig`

        `screenshot`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: ComputerScrollConfig`

        `scroll`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: ComputerTripleClickConfig`

        `triple_click`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: ComputerTypeConfig`

        `type`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: ComputerWaitConfig`

        `wait`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: ComputerZoomConfig`

        `zoom`'s config overrides.

        - `defer_loading: bool`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: bool`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class ToolTextEditor20250124`

    - `name: :str_replace_editor`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20250124`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250429`

    - `name: :str_replace_based_edit_tool`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20250429`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250728`

    - `name: :str_replace_based_edit_tool`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: :text_editor_20250728`

    - `allowed_callers: Array[:direct | :code_execution_20250825 | :code_execution_20260120 | :code_execution_20260521]`

      - `:direct`

      - `:code_execution_20250825`

      - `:code_execution_20260120`

      - `:code_execution_20260521`

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: Array[Hash[Symbol, untyped]]`

    - `max_characters: Integer`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      minimum: 1

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20250305`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: UserLocation`

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

  - `class WebFetchTool20250910`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: CitationsConfigParam`

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

  - `class WebSearchTool20260209`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: Integer`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: UserLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class WebFetchTool20260209`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: CitationsConfigParam`

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

  - `class WebFetchTool20260309`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: CitationsConfigParam`

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

  - `class WebSearchTool20260318`

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

    - `cache_control: CacheControlEphemeral`

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

    - `user_location: UserLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class WebFetchTool20260318`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `citations: CitationsConfigParam`

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

  - `class ToolSearchToolBm25_20251119`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolRegex20251119`

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

    - `cache_control: CacheControlEphemeral`

      Create a cache control breakpoint at this content block.

    - `defer_loading: bool`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: bool`

      When true, guarantees schema validation on tool names and inputs

- `user_profile_id: String`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

## Returns

- `class MessageTokensCount`

  - `input_tokens: Integer`

    The total number of tokens across the provided list of messages, system prompt, and tools.

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_tokens_count = anthropic.messages.count_tokens(
  messages: [{content: "Hello, world", role: :user}],
  model: Anthropic::Model::CLAUDE_OPUS_5
)

puts(message_tokens_count)
```

### Response (200)

```json
{
  "input_tokens": 2095
}
```
