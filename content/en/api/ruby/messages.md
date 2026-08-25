# Messages

## Create a Message

`messages.create(**kwargs) -> Message`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

### Parameters

- `max_tokens: Integer`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

  minimum: 0

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

- `container: MessageCreateParamsContainer`

  Container identifier for reuse across requests.

  - `class ContainerParams`

    Container parameters with skills to be loaded.

    - `id: String`

      Container id

    - `skills: Array[SkillParams]`

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

- `inference_geo: String`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `metadata: Metadata`

  An object describing metadata about the request.

  - `user_id: String`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    maxLength: 512

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

- `service_tier: :auto | :standard_only`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

  - `:auto`

  - `:standard_only`

- `stop_sequences: Array[String]`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `stream: bool`

  Whether to incrementally stream the response using server-sent events.

  See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

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

- `tools: Array[ToolUnion]`

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

### Returns

- `class Message`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: Container`

    Information about the container used in the request (for the code execution tool)

    - `id: String`

      Identifier for the container used in this request

    - `expires_at: Time`

      The time at which the container will expire.

      format: date-time

    - `skills: Array[ContainerSkill]`

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

  - `content: Array[ContentBlock]`

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

    - `class TextBlock`

      - `citations: Array[TextCitation]`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_char_index: Integer`

          - `file_id: String`

          - `start_char_index: Integer`

            minimum: 0

          - `type: :char_location`

        - `class CitationPageLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_page_number: Integer`

          - `file_id: String`

          - `start_page_number: Integer`

            minimum: 1

          - `type: :page_location`

        - `class CitationContentBlockLocation`

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

        - `class CitationsWebSearchResultLocation`

          - `cited_text: String`

          - `encrypted_index: String`

          - `title: String`

            maxLength: 512

          - `type: :web_search_result_location`

          - `url: String`

        - `class CitationsSearchResultLocation`

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

    - `class ThinkingBlock`

      - `signature: String`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `thinking: String`

        The text of Claude's thinking process for this block.

      - `type: :thinking`

    - `class RedactedThinkingBlock`

      - `data: String`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `type: :redacted_thinking`

    - `class ToolUseBlock`

      - `id: String`

        pattern: ^[a-zA-Z0-9_-]+$

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

      - `input: Hash[Symbol, untyped]`

      - `name: String`

        minLength: 1

      - `type: :tool_use`

      - `toolset_name: String`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock`

      - `id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

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

    - `class WebSearchToolResultBlock`

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

      - `content: WebSearchToolResultBlockContent`

        - `class WebSearchToolResultError`

          - `error_code: WebSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:max_uses_exceeded`

            - `:too_many_requests`

            - `:query_too_long`

            - `:request_too_large`

          - `type: :web_search_tool_result_error`

        - `UnionMember1 = Array[WebSearchResultBlock]`

          - `encrypted_content: String`

          - `page_age: String`

          - `title: String`

          - `type: :web_search_result`

          - `url: String`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :web_search_tool_result`

    - `class WebFetchToolResultBlock`

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

      - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

        - `class WebFetchToolResultErrorBlock`

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

        - `class WebFetchBlock`

          - `content: DocumentBlock`

            - `citations: CitationsConfig`

              Citation configuration for the document

              - `enabled: bool`

            - `source: Base64PDFSource | PlainTextSource`

              - `class Base64PDFSource`

                - `data: String`

                  format: byte

                - `media_type: :"application/pdf"`

                - `type: :base64`

              - `class PlainTextSource`

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

    - `class CodeExecutionToolResultBlock`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `type: :code_execution_tool_result_error`

        - `class CodeExecutionResultBlock`

          - `content: Array[CodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :code_execution_result`

        - `class EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array[CodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `encrypted_stdout: String`

          - `return_code: Integer`

          - `stderr: String`

          - `type: :encrypted_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :code_execution_tool_result`

    - `class BashCodeExecutionToolResultBlock`

      - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

        - `class BashCodeExecutionToolResultError`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:output_file_too_large`

          - `type: :bash_code_execution_tool_result_error`

        - `class BashCodeExecutionResultBlock`

          - `content: Array[BashCodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :bash_code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :bash_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :bash_code_execution_tool_result`

    - `class TextEditorCodeExecutionToolResultBlock`

      - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

        - `class TextEditorCodeExecutionToolResultError`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:file_not_found`

          - `error_message: String`

          - `type: :text_editor_code_execution_tool_result_error`

        - `class TextEditorCodeExecutionViewResultBlock`

          - `content: String`

          - `file_type: :text | :image | :pdf`

            - `:text`

            - `:image`

            - `:pdf`

          - `num_lines: Integer`

          - `start_line: Integer`

          - `total_lines: Integer`

          - `type: :text_editor_code_execution_view_result`

        - `class TextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: bool`

          - `type: :text_editor_code_execution_create_result`

        - `class TextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array[String]`

          - `new_lines: Integer`

          - `new_start: Integer`

          - `old_lines: Integer`

          - `old_start: Integer`

          - `type: :text_editor_code_execution_str_replace_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :text_editor_code_execution_tool_result`

    - `class ToolSearchToolResultBlock`

      - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

        - `class ToolSearchToolResultError`

          - `error_code: ToolSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `error_message: String`

          - `type: :tool_search_tool_result_error`

        - `class ToolSearchToolSearchResultBlock`

          - `tool_references: Array[ToolReferenceBlock]`

            - `tool_name: String`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `type: :tool_reference`

          - `type: :tool_search_tool_search_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :tool_search_tool_result`

    - `class ContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: String`

      - `type: :container_upload`

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

  - `role: :assistant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `stop_details: RefusalStopDetails`

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

    - `type: :refusal`

  - `stop_reason: StopReason`

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

    - `:refusal`

    - `:model_context_window_exceeded`

  - `stop_sequence: String`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: :message`

    Object type.

    For Messages, this is always `"message"`.

  - `usage: Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: CacheCreation`

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

    - `inference_geo: String`

      The geographic region where inference was performed for this request.

    - `input_tokens: Integer`

      The number of input tokens which were used.

      minimum: 0

    - `output_tokens: Integer`

      The number of output tokens which were used.

      minimum: 0

    - `output_tokens_details: OutputTokensDetails`

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

    - `server_tool_use: ServerToolUsage`

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

- `RawMessageStreamEvent = RawMessageStartEvent | RawMessageDeltaEvent | RawMessageStopEvent | 3 more`

  - `class RawMessageStartEvent`

    - `message: Message`

    - `type: :message_start`

  - `class RawMessageDeltaEvent`

    - `delta: Delta`

      - `container: Container`

        Information about the container used in the request (for the code execution tool)

      - `stop_details: RefusalStopDetails`

        Structured information about a refusal.

      - `stop_reason: StopReason`

      - `stop_sequence: String`

    - `type: :message_delta`

    - `usage: MessageDeltaUsage`

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

      - `input_tokens: Integer`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `output_tokens: Integer`

        The cumulative number of output tokens which were used.

      - `output_tokens_details: OutputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `server_tool_use: ServerToolUsage`

        The number of server tool requests.

  - `class RawMessageStopEvent`

    - `type: :message_stop`

  - `class RawContentBlockStartEvent`

    - `content_block: TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

      Response model for a file uploaded to the container.

      - `class TextBlock`

      - `class ThinkingBlock`

      - `class RedactedThinkingBlock`

      - `class ToolUseBlock`

      - `class ServerToolUseBlock`

      - `class WebSearchToolResultBlock`

      - `class WebFetchToolResultBlock`

      - `class CodeExecutionToolResultBlock`

      - `class BashCodeExecutionToolResultBlock`

      - `class TextEditorCodeExecutionToolResultBlock`

      - `class ToolSearchToolResultBlock`

      - `class ContainerUploadBlock`

        Response model for a file uploaded to the container.

    - `index: Integer`

    - `type: :content_block_start`

  - `class RawContentBlockDeltaEvent`

    - `delta: RawContentBlockDelta`

      - `class TextDelta`

        - `text: String`

        - `type: :text_delta`

      - `class InputJSONDelta`

        - `partial_json: String`

        - `type: :input_json_delta`

      - `class CitationsDelta`

        - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

          - `class CitationCharLocation`

          - `class CitationPageLocation`

          - `class CitationContentBlockLocation`

          - `class CitationsWebSearchResultLocation`

          - `class CitationsSearchResultLocation`

        - `type: :citations_delta`

      - `class ThinkingDelta`

        - `thinking: String`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `type: :thinking_delta`

      - `class SignatureDelta`

        - `signature: String`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `type: :signature_delta`

    - `index: Integer`

    - `type: :content_block_delta`

  - `class RawContentBlockStopEvent`

    - `index: Integer`

    - `type: :content_block_stop`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message = anthropic.messages.create(
  max_tokens: 1024,
  messages: [{content: "Hello, world", role: :user}],
  model: Anthropic::Model::CLAUDE_OPUS_5
)

puts(message)
```

#### Response (200)

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
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
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
    "inference_geo": "global",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard"
  }
}
```

## Count tokens in a Message

`messages.count_tokens(**kwargs) -> MessageTokensCount`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Parameters

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

### Returns

- `class MessageTokensCount`

  - `input_tokens: Integer`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_tokens_count = anthropic.messages.count_tokens(
  messages: [{content: "Hello, world", role: :user}],
  model: Anthropic::Model::CLAUDE_OPUS_5
)

puts(message_tokens_count)
```

#### Response (200)

```json
{
  "input_tokens": 2095
}
```

## Domain types

### Base64 Image Source

- `class Base64ImageSource`

  - `data: String`

    format: byte

  - `media_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"`

    - `:"image/jpeg"`

    - `:"image/png"`

    - `:"image/gif"`

    - `:"image/webp"`

  - `type: :base64`

### Base64 PDF Source

- `class Base64PDFSource`

  - `data: String`

    format: byte

  - `media_type: :"application/pdf"`

  - `type: :base64`

### Bash Code Execution Output Block

- `class BashCodeExecutionOutputBlock`

  - `file_id: String`

  - `type: :bash_code_execution_output`

### Bash Code Execution Output Block Param

- `class BashCodeExecutionOutputBlockParam`

  - `file_id: String`

  - `type: :bash_code_execution_output`

### Bash Code Execution Result Block

- `class BashCodeExecutionResultBlock`

  - `content: Array[BashCodeExecutionOutputBlock]`

    - `file_id: String`

    - `type: :bash_code_execution_output`

  - `return_code: Integer`

  - `stderr: String`

  - `stdout: String`

  - `type: :bash_code_execution_result`

### Bash Code Execution Result Block Param

- `class BashCodeExecutionResultBlockParam`

  - `content: Array[BashCodeExecutionOutputBlockParam]`

    - `file_id: String`

    - `type: :bash_code_execution_output`

  - `return_code: Integer`

  - `stderr: String`

  - `stdout: String`

  - `type: :bash_code_execution_result`

### Bash Code Execution Tool Result Block

- `class BashCodeExecutionToolResultBlock`

  - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

    - `class BashCodeExecutionToolResultError`

      - `error_code: BashCodeExecutionToolResultErrorCode`

        - `:invalid_tool_input`

        - `:unavailable`

        - `:too_many_requests`

        - `:execution_time_exceeded`

        - `:output_file_too_large`

      - `type: :bash_code_execution_tool_result_error`

    - `class BashCodeExecutionResultBlock`

      - `content: Array[BashCodeExecutionOutputBlock]`

        - `file_id: String`

        - `type: :bash_code_execution_output`

      - `return_code: Integer`

      - `stderr: String`

      - `stdout: String`

      - `type: :bash_code_execution_result`

  - `tool_use_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :bash_code_execution_tool_result`

### Bash Code Execution Tool Result Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

### Bash Code Execution Tool Result Error

- `class BashCodeExecutionToolResultError`

  - `error_code: BashCodeExecutionToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

    - `:output_file_too_large`

  - `type: :bash_code_execution_tool_result_error`

### Bash Code Execution Tool Result Error Code

- `BashCodeExecutionToolResultErrorCode = :invalid_tool_input | :unavailable | :too_many_requests | 2 more`

  - `:invalid_tool_input`

  - `:unavailable`

  - `:too_many_requests`

  - `:execution_time_exceeded`

  - `:output_file_too_large`

### Bash Code Execution Tool Result Error Param

- `class BashCodeExecutionToolResultErrorParam`

  - `error_code: BashCodeExecutionToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

    - `:output_file_too_large`

  - `type: :bash_code_execution_tool_result_error`

### Browser Close Tab Config

- `class BrowserCloseTabConfig`

  `close_tab`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Double Click Config

- `class BrowserDoubleClickConfig`

  `double_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser File Upload Config

- `class BrowserFileUploadConfig`

  `file_upload`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Find Config

- `class BrowserFindConfig`

  `find`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Form Input Config

- `class BrowserFormInputConfig`

  `form_input`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Get Page Text Config

- `class BrowserGetPageTextConfig`

  `get_page_text`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hold Key Config

- `class BrowserHoldKeyConfig`

  `hold_key`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hover Config

- `class BrowserHoverConfig`

  `hover`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Javascript Exec Config

- `class BrowserJavascriptExecConfig`

  `javascript_exec`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Key Config

- `class BrowserKeyConfig`

  `key`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Config

- `class BrowserLeftClickConfig`

  `left_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Drag Config

- `class BrowserLeftClickDragConfig`

  `left_click_drag`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Down Config

- `class BrowserLeftMouseDownConfig`

  `left_mouse_down`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Up Config

- `class BrowserLeftMouseUpConfig`

  `left_mouse_up`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser List Tabs Config

- `class BrowserListTabsConfig`

  `list_tabs`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Middle Click Config

- `class BrowserMiddleClickConfig`

  `middle_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Mouse Move Config

- `class BrowserMouseMoveConfig`

  `mouse_move`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Navigate Config

- `class BrowserNavigateConfig`

  `navigate`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser New Tab Config

- `class BrowserNewTabConfig`

  `new_tab`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Console Config

- `class BrowserReadConsoleConfig`

  `read_console`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Network Config

- `class BrowserReadNetworkConfig`

  `read_network`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Page Config

- `class BrowserReadPageConfig`

  `read_page`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Right Click Config

- `class BrowserRightClickConfig`

  `right_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Screenshot Config

- `class BrowserScreenshotConfig`

  `screenshot`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll Config

- `class BrowserScrollConfig`

  `scroll`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll To Config

- `class BrowserScrollToConfig`

  `scroll_to`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser State Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Browser State Change

- `BrowserStateChange = BrowserStateChangeTabOpened | BrowserStateChangeDownloadStarted | BrowserStateChangeDownloadCompleted | BrowserStateChangeDownloadFailed`

  A tab this call's execution opened that remains open at its end —
  the creation delta of the `tabs` inventory, not an event log.

  Carries only the `tab_id`; the tab's `title` and `url` live on its
  `tabs` entry, which must include the same `tab_id`. A tab opened
  during a failed call gets no deferred `tab_opened`; it simply appears
  in the next result's `tabs` inventory.

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

### Browser State Change Download Completed

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

### Browser State Change Download Failed

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

### Browser State Change Download Started

- `class BrowserStateChangeDownloadStarted`

  A file download that started during this call.

  - `download_id: String`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `type: :download_started`

  - `url: String`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

### Browser State Change Tab Opened

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

### Browser State Tab Entry

- `class BrowserStateTabEntry`

  One open browser tab reported in a `browser_state` block's `tabs`
  inventory.

  `tab_id` is the caller-assigned identifier for the tab; `title` and
  `url` describe the page the tab is currently showing and may be empty
  strings (a blank tab legitimately has both empty). `active` marks the
  tab that is active after this call; whenever `tabs` is non-empty,
  exactly one entry is marked.

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

### Browser Switch Tab Config

- `class BrowserSwitchTabConfig`

  `switch_tab`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Toolset 20260801

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Browser Toolset Configs

- `class BrowserToolsetConfigs`

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

### Browser Triple Click Config

- `class BrowserTripleClickConfig`

  `triple_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Type Config

- `class BrowserTypeConfig`

  `type`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Wait Config

- `class BrowserWaitConfig`

  `wait`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Zoom Config

- `class BrowserZoomConfig`

  `zoom`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Cache Control Ephemeral

- `class CacheControlEphemeral`

  - `type: :ephemeral`

  - `ttl: :"5m" | :"1h"`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `:"5m"`

    - `:"1h"`

### Cache Creation

- `class CacheCreation`

  - `ephemeral_1h_input_tokens: Integer`

    The number of input tokens used to create the 1 hour cache entry.

    minimum: 0

  - `ephemeral_5m_input_tokens: Integer`

    The number of input tokens used to create the 5 minute cache entry.

    minimum: 0

### Citation Char Location

- `class CitationCharLocation`

  - `cited_text: String`

  - `document_index: Integer`

    minimum: 0

  - `document_title: String`

  - `end_char_index: Integer`

  - `file_id: String`

  - `start_char_index: Integer`

    minimum: 0

  - `type: :char_location`

### Citation Char Location Param

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

### Citation Content Block Location

- `class CitationContentBlockLocation`

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

### Citation Content Block Location Param

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

### Citation Page Location

- `class CitationPageLocation`

  - `cited_text: String`

  - `document_index: Integer`

    minimum: 0

  - `document_title: String`

  - `end_page_number: Integer`

  - `file_id: String`

  - `start_page_number: Integer`

    minimum: 1

  - `type: :page_location`

### Citation Page Location Param

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

### Citation Search Result Location Param

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

### Citation Web Search Result Location Param

- `class CitationWebSearchResultLocationParam`

  - `cited_text: String`

  - `encrypted_index: String`

  - `title: String`

    maxLength: 512, minLength: 1

  - `type: :web_search_result_location`

  - `url: String`

    minLength: 1

### Citations Config

- `class CitationsConfig`

  - `enabled: bool`

### Citations Config Param

- `class CitationsConfigParam`

  - `enabled: bool`

### Citations Delta

- `class CitationsDelta`

  - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

    - `class CitationCharLocation`

      - `cited_text: String`

      - `document_index: Integer`

        minimum: 0

      - `document_title: String`

      - `end_char_index: Integer`

      - `file_id: String`

      - `start_char_index: Integer`

        minimum: 0

      - `type: :char_location`

    - `class CitationPageLocation`

      - `cited_text: String`

      - `document_index: Integer`

        minimum: 0

      - `document_title: String`

      - `end_page_number: Integer`

      - `file_id: String`

      - `start_page_number: Integer`

        minimum: 1

      - `type: :page_location`

    - `class CitationContentBlockLocation`

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

    - `class CitationsWebSearchResultLocation`

      - `cited_text: String`

      - `encrypted_index: String`

      - `title: String`

        maxLength: 512

      - `type: :web_search_result_location`

      - `url: String`

    - `class CitationsSearchResultLocation`

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

  - `type: :citations_delta`

### Citations Search Result Location

- `class CitationsSearchResultLocation`

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

### Citations Web Search Result Location

- `class CitationsWebSearchResultLocation`

  - `cited_text: String`

  - `encrypted_index: String`

  - `title: String`

    maxLength: 512

  - `type: :web_search_result_location`

  - `url: String`

### Code Execution Output Block

- `class CodeExecutionOutputBlock`

  - `file_id: String`

  - `type: :code_execution_output`

### Code Execution Output Block Param

- `class CodeExecutionOutputBlockParam`

  - `file_id: String`

  - `type: :code_execution_output`

### Code Execution Result Block

- `class CodeExecutionResultBlock`

  - `content: Array[CodeExecutionOutputBlock]`

    - `file_id: String`

    - `type: :code_execution_output`

  - `return_code: Integer`

  - `stderr: String`

  - `stdout: String`

  - `type: :code_execution_result`

### Code Execution Result Block Param

- `class CodeExecutionResultBlockParam`

  - `content: Array[CodeExecutionOutputBlockParam]`

    - `file_id: String`

    - `type: :code_execution_output`

  - `return_code: Integer`

  - `stderr: String`

  - `stdout: String`

  - `type: :code_execution_result`

### Code Execution Tool 20250522

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260521

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

- `class CodeExecutionToolResultBlock`

  - `content: CodeExecutionToolResultBlockContent`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `class CodeExecutionToolResultError`

      - `error_code: CodeExecutionToolResultErrorCode`

        - `:invalid_tool_input`

        - `:unavailable`

        - `:too_many_requests`

        - `:execution_time_exceeded`

      - `type: :code_execution_tool_result_error`

    - `class CodeExecutionResultBlock`

      - `content: Array[CodeExecutionOutputBlock]`

        - `file_id: String`

        - `type: :code_execution_output`

      - `return_code: Integer`

      - `stderr: String`

      - `stdout: String`

      - `type: :code_execution_result`

    - `class EncryptedCodeExecutionResultBlock`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `content: Array[CodeExecutionOutputBlock]`

        - `file_id: String`

        - `type: :code_execution_output`

      - `encrypted_stdout: String`

      - `return_code: Integer`

      - `stderr: String`

      - `type: :encrypted_code_execution_result`

  - `tool_use_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :code_execution_tool_result`

### Code Execution Tool Result Block Content

- `CodeExecutionToolResultBlockContent = CodeExecutionToolResultError | CodeExecutionResultBlock | EncryptedCodeExecutionResultBlock`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `class CodeExecutionToolResultError`

    - `error_code: CodeExecutionToolResultErrorCode`

      - `:invalid_tool_input`

      - `:unavailable`

      - `:too_many_requests`

      - `:execution_time_exceeded`

    - `type: :code_execution_tool_result_error`

  - `class CodeExecutionResultBlock`

    - `content: Array[CodeExecutionOutputBlock]`

      - `file_id: String`

      - `type: :code_execution_output`

    - `return_code: Integer`

    - `stderr: String`

    - `stdout: String`

    - `type: :code_execution_result`

  - `class EncryptedCodeExecutionResultBlock`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `content: Array[CodeExecutionOutputBlock]`

      - `file_id: String`

      - `type: :code_execution_output`

    - `encrypted_stdout: String`

    - `return_code: Integer`

    - `stderr: String`

    - `type: :encrypted_code_execution_result`

### Code Execution Tool Result Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

### Code Execution Tool Result Block Param Content

- `CodeExecutionToolResultBlockParamContent = CodeExecutionToolResultErrorParam | CodeExecutionResultBlockParam | EncryptedCodeExecutionResultBlockParam`

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

### Code Execution Tool Result Error

- `class CodeExecutionToolResultError`

  - `error_code: CodeExecutionToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

  - `type: :code_execution_tool_result_error`

### Code Execution Tool Result Error Code

- `CodeExecutionToolResultErrorCode = :invalid_tool_input | :unavailable | :too_many_requests | :execution_time_exceeded`

  - `:invalid_tool_input`

  - `:unavailable`

  - `:too_many_requests`

  - `:execution_time_exceeded`

### Code Execution Tool Result Error Param

- `class CodeExecutionToolResultErrorParam`

  - `error_code: CodeExecutionToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

  - `type: :code_execution_tool_result_error`

### Computer Cursor Position Config

- `class ComputerCursorPositionConfig`

  `cursor_position`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Double Click Config

- `class ComputerDoubleClickConfig`

  `double_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Hold Key Config

- `class ComputerHoldKeyConfig`

  `hold_key`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Key Config

- `class ComputerKeyConfig`

  `key`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Config

- `class ComputerLeftClickConfig`

  `left_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Drag Config

- `class ComputerLeftClickDragConfig`

  `left_click_drag`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Down Config

- `class ComputerLeftMouseDownConfig`

  `left_mouse_down`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Up Config

- `class ComputerLeftMouseUpConfig`

  `left_mouse_up`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Middle Click Config

- `class ComputerMiddleClickConfig`

  `middle_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Mouse Move Config

- `class ComputerMouseMoveConfig`

  `mouse_move`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Right Click Config

- `class ComputerRightClickConfig`

  `right_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Screenshot Config

- `class ComputerScreenshotConfig`

  `screenshot`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Scroll Config

- `class ComputerScrollConfig`

  `scroll`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Toolset 20260801

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Computer Toolset Configs

- `class ComputerToolsetConfigs`

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

### Computer Triple Click Config

- `class ComputerTripleClickConfig`

  `triple_click`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Type Config

- `class ComputerTypeConfig`

  `type`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Wait Config

- `class ComputerWaitConfig`

  `wait`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Zoom Config

- `class ComputerZoomConfig`

  `zoom`'s config overrides.

  - `defer_loading: bool`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: bool`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Container

- `class Container`

  Information about the container used in the request (for the code execution tool)

  - `id: String`

    Identifier for the container used in this request

  - `expires_at: Time`

    The time at which the container will expire.

    format: date-time

  - `skills: Array[ContainerSkill]`

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

### Container Params

- `class ContainerParams`

  Container parameters with skills to be loaded.

  - `id: String`

    Container id

  - `skills: Array[SkillParams]`

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

### Container Skill

- `class ContainerSkill`

  A skill that was loaded in a container (response model).

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

### Container Upload Block

- `class ContainerUploadBlock`

  Response model for a file uploaded to the container.

  - `file_id: String`

  - `type: :container_upload`

### Container Upload Block Param

- `class ContainerUploadBlockParam`

  A content block that represents a file to be uploaded to the container
  Files uploaded via this block will be available in the container's input directory.

  - `file_id: String`

  - `type: :container_upload`

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

### Content Block

- `ContentBlock = TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

  Response model for a file uploaded to the container.

  - `class TextBlock`

    - `citations: Array[TextCitation]`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

      - `class CitationCharLocation`

        - `cited_text: String`

        - `document_index: Integer`

          minimum: 0

        - `document_title: String`

        - `end_char_index: Integer`

        - `file_id: String`

        - `start_char_index: Integer`

          minimum: 0

        - `type: :char_location`

      - `class CitationPageLocation`

        - `cited_text: String`

        - `document_index: Integer`

          minimum: 0

        - `document_title: String`

        - `end_page_number: Integer`

        - `file_id: String`

        - `start_page_number: Integer`

          minimum: 1

        - `type: :page_location`

      - `class CitationContentBlockLocation`

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

      - `class CitationsWebSearchResultLocation`

        - `cited_text: String`

        - `encrypted_index: String`

        - `title: String`

          maxLength: 512

        - `type: :web_search_result_location`

        - `url: String`

      - `class CitationsSearchResultLocation`

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

  - `class ThinkingBlock`

    - `signature: String`

      A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

      This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `thinking: String`

      The text of Claude's thinking process for this block.

    - `type: :thinking`

  - `class RedactedThinkingBlock`

    - `data: String`

      The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

      Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

    - `type: :redacted_thinking`

  - `class ToolUseBlock`

    - `id: String`

      pattern: ^[a-zA-Z0-9_-]+$

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

    - `input: Hash[Symbol, untyped]`

    - `name: String`

      minLength: 1

    - `type: :tool_use`

    - `toolset_name: String`

      For a toolset member tool_use, the toolset family.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

  - `class ServerToolUseBlock`

    - `id: String`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `class DirectCaller`

        Tool invocation directly from the model.

      - `class ServerToolCaller`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120`

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

  - `class WebSearchToolResultBlock`

    - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `class DirectCaller`

        Tool invocation directly from the model.

      - `class ServerToolCaller`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120`

    - `content: WebSearchToolResultBlockContent`

      - `class WebSearchToolResultError`

        - `error_code: WebSearchToolResultErrorCode`

          - `:invalid_tool_input`

          - `:unavailable`

          - `:max_uses_exceeded`

          - `:too_many_requests`

          - `:query_too_long`

          - `:request_too_large`

        - `type: :web_search_tool_result_error`

      - `UnionMember1 = Array[WebSearchResultBlock]`

        - `encrypted_content: String`

        - `page_age: String`

        - `title: String`

        - `type: :web_search_result`

        - `url: String`

    - `tool_use_id: String`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: :web_search_tool_result`

  - `class WebFetchToolResultBlock`

    - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `class DirectCaller`

        Tool invocation directly from the model.

      - `class ServerToolCaller`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120`

    - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

      - `class WebFetchToolResultErrorBlock`

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

      - `class WebFetchBlock`

        - `content: DocumentBlock`

          - `citations: CitationsConfig`

            Citation configuration for the document

            - `enabled: bool`

          - `source: Base64PDFSource | PlainTextSource`

            - `class Base64PDFSource`

              - `data: String`

                format: byte

              - `media_type: :"application/pdf"`

              - `type: :base64`

            - `class PlainTextSource`

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

  - `class CodeExecutionToolResultBlock`

    - `content: CodeExecutionToolResultBlockContent`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `class CodeExecutionToolResultError`

        - `error_code: CodeExecutionToolResultErrorCode`

          - `:invalid_tool_input`

          - `:unavailable`

          - `:too_many_requests`

          - `:execution_time_exceeded`

        - `type: :code_execution_tool_result_error`

      - `class CodeExecutionResultBlock`

        - `content: Array[CodeExecutionOutputBlock]`

          - `file_id: String`

          - `type: :code_execution_output`

        - `return_code: Integer`

        - `stderr: String`

        - `stdout: String`

        - `type: :code_execution_result`

      - `class EncryptedCodeExecutionResultBlock`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `content: Array[CodeExecutionOutputBlock]`

          - `file_id: String`

          - `type: :code_execution_output`

        - `encrypted_stdout: String`

        - `return_code: Integer`

        - `stderr: String`

        - `type: :encrypted_code_execution_result`

    - `tool_use_id: String`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: :code_execution_tool_result`

  - `class BashCodeExecutionToolResultBlock`

    - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

      - `class BashCodeExecutionToolResultError`

        - `error_code: BashCodeExecutionToolResultErrorCode`

          - `:invalid_tool_input`

          - `:unavailable`

          - `:too_many_requests`

          - `:execution_time_exceeded`

          - `:output_file_too_large`

        - `type: :bash_code_execution_tool_result_error`

      - `class BashCodeExecutionResultBlock`

        - `content: Array[BashCodeExecutionOutputBlock]`

          - `file_id: String`

          - `type: :bash_code_execution_output`

        - `return_code: Integer`

        - `stderr: String`

        - `stdout: String`

        - `type: :bash_code_execution_result`

    - `tool_use_id: String`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: :bash_code_execution_tool_result`

  - `class TextEditorCodeExecutionToolResultBlock`

    - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

      - `class TextEditorCodeExecutionToolResultError`

        - `error_code: TextEditorCodeExecutionToolResultErrorCode`

          - `:invalid_tool_input`

          - `:unavailable`

          - `:too_many_requests`

          - `:execution_time_exceeded`

          - `:file_not_found`

        - `error_message: String`

        - `type: :text_editor_code_execution_tool_result_error`

      - `class TextEditorCodeExecutionViewResultBlock`

        - `content: String`

        - `file_type: :text | :image | :pdf`

          - `:text`

          - `:image`

          - `:pdf`

        - `num_lines: Integer`

        - `start_line: Integer`

        - `total_lines: Integer`

        - `type: :text_editor_code_execution_view_result`

      - `class TextEditorCodeExecutionCreateResultBlock`

        - `is_file_update: bool`

        - `type: :text_editor_code_execution_create_result`

      - `class TextEditorCodeExecutionStrReplaceResultBlock`

        - `lines: Array[String]`

        - `new_lines: Integer`

        - `new_start: Integer`

        - `old_lines: Integer`

        - `old_start: Integer`

        - `type: :text_editor_code_execution_str_replace_result`

    - `tool_use_id: String`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: :text_editor_code_execution_tool_result`

  - `class ToolSearchToolResultBlock`

    - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

      - `class ToolSearchToolResultError`

        - `error_code: ToolSearchToolResultErrorCode`

          - `:invalid_tool_input`

          - `:unavailable`

          - `:too_many_requests`

          - `:execution_time_exceeded`

        - `error_message: String`

        - `type: :tool_search_tool_result_error`

      - `class ToolSearchToolSearchResultBlock`

        - `tool_references: Array[ToolReferenceBlock]`

          - `tool_name: String`

            maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `type: :tool_reference`

        - `type: :tool_search_tool_search_result`

    - `tool_use_id: String`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: :tool_search_tool_result`

  - `class ContainerUploadBlock`

    Response model for a file uploaded to the container.

    - `file_id: String`

    - `type: :container_upload`

### Content Block Param

- `ContentBlockParam = TextBlockParam | ImageBlockParam | DocumentBlockParam | 13 more`

  Regular text content.

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

### Content Block Source

- `class ContentBlockSource`

  - `content: String | Array[ContentBlockSourceContent]`

    - `String = String`

    - `ContentBlockSourceContent = Array[ContentBlockSourceContent]`

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

  - `type: :content`

### Content Block Source Content

- `ContentBlockSourceContent = TextBlockParam | ImageBlockParam`

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

### Direct Caller

- `class DirectCaller`

  Tool invocation directly from the model.

  - `type: :direct`

### Document Block

- `class DocumentBlock`

  - `citations: CitationsConfig`

    Citation configuration for the document

    - `enabled: bool`

  - `source: Base64PDFSource | PlainTextSource`

    - `class Base64PDFSource`

      - `data: String`

        format: byte

      - `media_type: :"application/pdf"`

      - `type: :base64`

    - `class PlainTextSource`

      - `data: String`

      - `media_type: :"text/plain"`

      - `type: :text`

  - `title: String`

    The title of the document

  - `type: :document`

### Document Block Param

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

### Encrypted Code Execution Result Block

- `class EncryptedCodeExecutionResultBlock`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: Array[CodeExecutionOutputBlock]`

    - `file_id: String`

    - `type: :code_execution_output`

  - `encrypted_stdout: String`

  - `return_code: Integer`

  - `stderr: String`

  - `type: :encrypted_code_execution_result`

### Encrypted Code Execution Result Block Param

- `class EncryptedCodeExecutionResultBlockParam`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: Array[CodeExecutionOutputBlockParam]`

    - `file_id: String`

    - `type: :code_execution_output`

  - `encrypted_stdout: String`

  - `return_code: Integer`

  - `stderr: String`

  - `type: :encrypted_code_execution_result`

### File Document Source

- `class FileDocumentSource`

  - `file_id: String`

  - `type: :file`

### File Image Source

- `class FileImageSource`

  - `file_id: String`

  - `type: :file`

### Image Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `transformations: ImageTransformationsParam`

    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

    - `oversized_image: :downsize | :error`

      What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

      - `:downsize`

      - `:error`

### Image Transformations Param

- `class ImageTransformationsParam`

  Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

  - `oversized_image: :downsize | :error`

    What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

    - `:downsize`

    - `:error`

### Input JSON Delta

- `class InputJSONDelta`

  - `partial_json: String`

  - `type: :input_json_delta`

### JSON Output Format

- `class JSONOutputFormat`

  - `schema: Hash[Symbol, untyped]`

    The JSON schema of the format

  - `type: :json_schema`

### Memory Tool 20250818

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: Array[Hash[Symbol, untyped]]`

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Message

- `class Message`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: Container`

    Information about the container used in the request (for the code execution tool)

    - `id: String`

      Identifier for the container used in this request

    - `expires_at: Time`

      The time at which the container will expire.

      format: date-time

    - `skills: Array[ContainerSkill]`

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

  - `content: Array[ContentBlock]`

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

    - `class TextBlock`

      - `citations: Array[TextCitation]`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_char_index: Integer`

          - `file_id: String`

          - `start_char_index: Integer`

            minimum: 0

          - `type: :char_location`

        - `class CitationPageLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_page_number: Integer`

          - `file_id: String`

          - `start_page_number: Integer`

            minimum: 1

          - `type: :page_location`

        - `class CitationContentBlockLocation`

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

        - `class CitationsWebSearchResultLocation`

          - `cited_text: String`

          - `encrypted_index: String`

          - `title: String`

            maxLength: 512

          - `type: :web_search_result_location`

          - `url: String`

        - `class CitationsSearchResultLocation`

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

    - `class ThinkingBlock`

      - `signature: String`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `thinking: String`

        The text of Claude's thinking process for this block.

      - `type: :thinking`

    - `class RedactedThinkingBlock`

      - `data: String`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `type: :redacted_thinking`

    - `class ToolUseBlock`

      - `id: String`

        pattern: ^[a-zA-Z0-9_-]+$

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

      - `input: Hash[Symbol, untyped]`

      - `name: String`

        minLength: 1

      - `type: :tool_use`

      - `toolset_name: String`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock`

      - `id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

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

    - `class WebSearchToolResultBlock`

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

      - `content: WebSearchToolResultBlockContent`

        - `class WebSearchToolResultError`

          - `error_code: WebSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:max_uses_exceeded`

            - `:too_many_requests`

            - `:query_too_long`

            - `:request_too_large`

          - `type: :web_search_tool_result_error`

        - `UnionMember1 = Array[WebSearchResultBlock]`

          - `encrypted_content: String`

          - `page_age: String`

          - `title: String`

          - `type: :web_search_result`

          - `url: String`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :web_search_tool_result`

    - `class WebFetchToolResultBlock`

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

      - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

        - `class WebFetchToolResultErrorBlock`

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

        - `class WebFetchBlock`

          - `content: DocumentBlock`

            - `citations: CitationsConfig`

              Citation configuration for the document

              - `enabled: bool`

            - `source: Base64PDFSource | PlainTextSource`

              - `class Base64PDFSource`

                - `data: String`

                  format: byte

                - `media_type: :"application/pdf"`

                - `type: :base64`

              - `class PlainTextSource`

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

    - `class CodeExecutionToolResultBlock`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `type: :code_execution_tool_result_error`

        - `class CodeExecutionResultBlock`

          - `content: Array[CodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :code_execution_result`

        - `class EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array[CodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `encrypted_stdout: String`

          - `return_code: Integer`

          - `stderr: String`

          - `type: :encrypted_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :code_execution_tool_result`

    - `class BashCodeExecutionToolResultBlock`

      - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

        - `class BashCodeExecutionToolResultError`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:output_file_too_large`

          - `type: :bash_code_execution_tool_result_error`

        - `class BashCodeExecutionResultBlock`

          - `content: Array[BashCodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :bash_code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :bash_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :bash_code_execution_tool_result`

    - `class TextEditorCodeExecutionToolResultBlock`

      - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

        - `class TextEditorCodeExecutionToolResultError`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:file_not_found`

          - `error_message: String`

          - `type: :text_editor_code_execution_tool_result_error`

        - `class TextEditorCodeExecutionViewResultBlock`

          - `content: String`

          - `file_type: :text | :image | :pdf`

            - `:text`

            - `:image`

            - `:pdf`

          - `num_lines: Integer`

          - `start_line: Integer`

          - `total_lines: Integer`

          - `type: :text_editor_code_execution_view_result`

        - `class TextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: bool`

          - `type: :text_editor_code_execution_create_result`

        - `class TextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array[String]`

          - `new_lines: Integer`

          - `new_start: Integer`

          - `old_lines: Integer`

          - `old_start: Integer`

          - `type: :text_editor_code_execution_str_replace_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :text_editor_code_execution_tool_result`

    - `class ToolSearchToolResultBlock`

      - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

        - `class ToolSearchToolResultError`

          - `error_code: ToolSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `error_message: String`

          - `type: :tool_search_tool_result_error`

        - `class ToolSearchToolSearchResultBlock`

          - `tool_references: Array[ToolReferenceBlock]`

            - `tool_name: String`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `type: :tool_reference`

          - `type: :tool_search_tool_search_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :tool_search_tool_result`

    - `class ContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: String`

      - `type: :container_upload`

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

  - `role: :assistant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `stop_details: RefusalStopDetails`

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

    - `type: :refusal`

  - `stop_reason: StopReason`

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

    - `:refusal`

    - `:model_context_window_exceeded`

  - `stop_sequence: String`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: :message`

    Object type.

    For Messages, this is always `"message"`.

  - `usage: Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: CacheCreation`

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

    - `inference_geo: String`

      The geographic region where inference was performed for this request.

    - `input_tokens: Integer`

      The number of input tokens which were used.

      minimum: 0

    - `output_tokens: Integer`

      The number of output tokens which were used.

      minimum: 0

    - `output_tokens_details: OutputTokensDetails`

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

    - `server_tool_use: ServerToolUsage`

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

### Message Count Tokens Tool

- `MessageCountTokensTool = Tool | ToolBash20250124 | CodeExecutionTool20250522 | 18 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

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

      - `type: :ephemeral`

      - `ttl: :"5m" | :"1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `:"5m"`

        - `:"1h"`

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

      - `enabled: bool`

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

### Message Create Params Container

- `MessageCreateParamsContainer = ContainerParams | String`

  Container identifier for reuse across requests.

  - `class ContainerParams`

    Container parameters with skills to be loaded.

    - `id: String`

      Container id

    - `skills: Array[SkillParams]`

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

### Message Delta Usage

- `class MessageDeltaUsage`

  - `cache_creation_input_tokens: Integer`

    The cumulative number of input tokens used to create the cache entry.

    minimum: 0

  - `cache_read_input_tokens: Integer`

    The cumulative number of input tokens read from the cache.

    minimum: 0

  - `input_tokens: Integer`

    The cumulative number of input tokens which were used.

    minimum: 0

  - `output_tokens: Integer`

    The cumulative number of output tokens which were used.

  - `output_tokens_details: OutputTokensDetails`

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

  - `server_tool_use: ServerToolUsage`

    The number of server tool requests.

    - `web_fetch_requests: Integer`

      The number of web fetch tool requests.

      minimum: 0

    - `web_search_requests: Integer`

      The number of web search tool requests.

      minimum: 0

### Message Param

- `class MessageParam`

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

### Message Tokens Count

- `class MessageTokensCount`

  - `input_tokens: Integer`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `class Metadata`

  - `user_id: String`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    maxLength: 512

### Model

- `Model = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-mythos-5" | 12 more | String`

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

### Output Config

- `class OutputConfig`

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

### Output Tokens Details

- `class OutputTokensDetails`

  - `thinking_tokens: Integer`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

    minimum: 0

### Plain Text Source

- `class PlainTextSource`

  - `data: String`

  - `media_type: :"text/plain"`

  - `type: :text`

### Raw Content Block Delta

- `RawContentBlockDelta = TextDelta | InputJSONDelta | CitationsDelta | 2 more`

  - `class TextDelta`

    - `text: String`

    - `type: :text_delta`

  - `class InputJSONDelta`

    - `partial_json: String`

    - `type: :input_json_delta`

  - `class CitationsDelta`

    - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

      - `class CitationCharLocation`

        - `cited_text: String`

        - `document_index: Integer`

          minimum: 0

        - `document_title: String`

        - `end_char_index: Integer`

        - `file_id: String`

        - `start_char_index: Integer`

          minimum: 0

        - `type: :char_location`

      - `class CitationPageLocation`

        - `cited_text: String`

        - `document_index: Integer`

          minimum: 0

        - `document_title: String`

        - `end_page_number: Integer`

        - `file_id: String`

        - `start_page_number: Integer`

          minimum: 1

        - `type: :page_location`

      - `class CitationContentBlockLocation`

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

      - `class CitationsWebSearchResultLocation`

        - `cited_text: String`

        - `encrypted_index: String`

        - `title: String`

          maxLength: 512

        - `type: :web_search_result_location`

        - `url: String`

      - `class CitationsSearchResultLocation`

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

    - `type: :citations_delta`

  - `class ThinkingDelta`

    - `thinking: String`

      The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

    - `type: :thinking_delta`

  - `class SignatureDelta`

    - `signature: String`

      The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

    - `type: :signature_delta`

### Raw Content Block Delta Event

- `class RawContentBlockDeltaEvent`

  - `delta: RawContentBlockDelta`

    - `class TextDelta`

      - `text: String`

      - `type: :text_delta`

    - `class InputJSONDelta`

      - `partial_json: String`

      - `type: :input_json_delta`

    - `class CitationsDelta`

      - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

        - `class CitationCharLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_char_index: Integer`

          - `file_id: String`

          - `start_char_index: Integer`

            minimum: 0

          - `type: :char_location`

        - `class CitationPageLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_page_number: Integer`

          - `file_id: String`

          - `start_page_number: Integer`

            minimum: 1

          - `type: :page_location`

        - `class CitationContentBlockLocation`

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

        - `class CitationsWebSearchResultLocation`

          - `cited_text: String`

          - `encrypted_index: String`

          - `title: String`

            maxLength: 512

          - `type: :web_search_result_location`

          - `url: String`

        - `class CitationsSearchResultLocation`

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

      - `type: :citations_delta`

    - `class ThinkingDelta`

      - `thinking: String`

        The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

      - `type: :thinking_delta`

    - `class SignatureDelta`

      - `signature: String`

        The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

      - `type: :signature_delta`

  - `index: Integer`

  - `type: :content_block_delta`

### Raw Content Block Start Event

- `class RawContentBlockStartEvent`

  - `content_block: TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

    Response model for a file uploaded to the container.

    - `class TextBlock`

      - `citations: Array[TextCitation]`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_char_index: Integer`

          - `file_id: String`

          - `start_char_index: Integer`

            minimum: 0

          - `type: :char_location`

        - `class CitationPageLocation`

          - `cited_text: String`

          - `document_index: Integer`

            minimum: 0

          - `document_title: String`

          - `end_page_number: Integer`

          - `file_id: String`

          - `start_page_number: Integer`

            minimum: 1

          - `type: :page_location`

        - `class CitationContentBlockLocation`

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

        - `class CitationsWebSearchResultLocation`

          - `cited_text: String`

          - `encrypted_index: String`

          - `title: String`

            maxLength: 512

          - `type: :web_search_result_location`

          - `url: String`

        - `class CitationsSearchResultLocation`

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

    - `class ThinkingBlock`

      - `signature: String`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `thinking: String`

        The text of Claude's thinking process for this block.

      - `type: :thinking`

    - `class RedactedThinkingBlock`

      - `data: String`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `type: :redacted_thinking`

    - `class ToolUseBlock`

      - `id: String`

        pattern: ^[a-zA-Z0-9_-]+$

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

      - `input: Hash[Symbol, untyped]`

      - `name: String`

        minLength: 1

      - `type: :tool_use`

      - `toolset_name: String`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock`

      - `id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

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

    - `class WebSearchToolResultBlock`

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

      - `content: WebSearchToolResultBlockContent`

        - `class WebSearchToolResultError`

          - `error_code: WebSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:max_uses_exceeded`

            - `:too_many_requests`

            - `:query_too_long`

            - `:request_too_large`

          - `type: :web_search_tool_result_error`

        - `UnionMember1 = Array[WebSearchResultBlock]`

          - `encrypted_content: String`

          - `page_age: String`

          - `title: String`

          - `type: :web_search_result`

          - `url: String`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :web_search_tool_result`

    - `class WebFetchToolResultBlock`

      - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `class DirectCaller`

          Tool invocation directly from the model.

        - `class ServerToolCaller`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120`

      - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

        - `class WebFetchToolResultErrorBlock`

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

        - `class WebFetchBlock`

          - `content: DocumentBlock`

            - `citations: CitationsConfig`

              Citation configuration for the document

              - `enabled: bool`

            - `source: Base64PDFSource | PlainTextSource`

              - `class Base64PDFSource`

                - `data: String`

                  format: byte

                - `media_type: :"application/pdf"`

                - `type: :base64`

              - `class PlainTextSource`

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

    - `class CodeExecutionToolResultBlock`

      - `content: CodeExecutionToolResultBlockContent`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError`

          - `error_code: CodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `type: :code_execution_tool_result_error`

        - `class CodeExecutionResultBlock`

          - `content: Array[CodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :code_execution_result`

        - `class EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: Array[CodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :code_execution_output`

          - `encrypted_stdout: String`

          - `return_code: Integer`

          - `stderr: String`

          - `type: :encrypted_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :code_execution_tool_result`

    - `class BashCodeExecutionToolResultBlock`

      - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

        - `class BashCodeExecutionToolResultError`

          - `error_code: BashCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:output_file_too_large`

          - `type: :bash_code_execution_tool_result_error`

        - `class BashCodeExecutionResultBlock`

          - `content: Array[BashCodeExecutionOutputBlock]`

            - `file_id: String`

            - `type: :bash_code_execution_output`

          - `return_code: Integer`

          - `stderr: String`

          - `stdout: String`

          - `type: :bash_code_execution_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :bash_code_execution_tool_result`

    - `class TextEditorCodeExecutionToolResultBlock`

      - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

        - `class TextEditorCodeExecutionToolResultError`

          - `error_code: TextEditorCodeExecutionToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

            - `:file_not_found`

          - `error_message: String`

          - `type: :text_editor_code_execution_tool_result_error`

        - `class TextEditorCodeExecutionViewResultBlock`

          - `content: String`

          - `file_type: :text | :image | :pdf`

            - `:text`

            - `:image`

            - `:pdf`

          - `num_lines: Integer`

          - `start_line: Integer`

          - `total_lines: Integer`

          - `type: :text_editor_code_execution_view_result`

        - `class TextEditorCodeExecutionCreateResultBlock`

          - `is_file_update: bool`

          - `type: :text_editor_code_execution_create_result`

        - `class TextEditorCodeExecutionStrReplaceResultBlock`

          - `lines: Array[String]`

          - `new_lines: Integer`

          - `new_start: Integer`

          - `old_lines: Integer`

          - `old_start: Integer`

          - `type: :text_editor_code_execution_str_replace_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :text_editor_code_execution_tool_result`

    - `class ToolSearchToolResultBlock`

      - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

        - `class ToolSearchToolResultError`

          - `error_code: ToolSearchToolResultErrorCode`

            - `:invalid_tool_input`

            - `:unavailable`

            - `:too_many_requests`

            - `:execution_time_exceeded`

          - `error_message: String`

          - `type: :tool_search_tool_result_error`

        - `class ToolSearchToolSearchResultBlock`

          - `tool_references: Array[ToolReferenceBlock]`

            - `tool_name: String`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `type: :tool_reference`

          - `type: :tool_search_tool_search_result`

      - `tool_use_id: String`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: :tool_search_tool_result`

    - `class ContainerUploadBlock`

      Response model for a file uploaded to the container.

      - `file_id: String`

      - `type: :container_upload`

  - `index: Integer`

  - `type: :content_block_start`

### Raw Content Block Stop Event

- `class RawContentBlockStopEvent`

  - `index: Integer`

  - `type: :content_block_stop`

### Raw Message Delta Event

- `class RawMessageDeltaEvent`

  - `delta: Delta`

    - `container: Container`

      Information about the container used in the request (for the code execution tool)

      - `id: String`

        Identifier for the container used in this request

      - `expires_at: Time`

        The time at which the container will expire.

        format: date-time

      - `skills: Array[ContainerSkill]`

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

    - `stop_details: RefusalStopDetails`

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

      - `type: :refusal`

    - `stop_reason: StopReason`

      - `:end_turn`

      - `:max_tokens`

      - `:stop_sequence`

      - `:tool_use`

      - `:pause_turn`

      - `:refusal`

      - `:model_context_window_exceeded`

    - `stop_sequence: String`

  - `type: :message_delta`

  - `usage: MessageDeltaUsage`

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

    - `input_tokens: Integer`

      The cumulative number of input tokens which were used.

      minimum: 0

    - `output_tokens: Integer`

      The cumulative number of output tokens which were used.

    - `output_tokens_details: OutputTokensDetails`

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

    - `server_tool_use: ServerToolUsage`

      The number of server tool requests.

      - `web_fetch_requests: Integer`

        The number of web fetch tool requests.

        minimum: 0

      - `web_search_requests: Integer`

        The number of web search tool requests.

        minimum: 0

### Raw Message Start Event

- `class RawMessageStartEvent`

  - `message: Message`

    - `id: String`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `container: Container`

      Information about the container used in the request (for the code execution tool)

      - `id: String`

        Identifier for the container used in this request

      - `expires_at: Time`

        The time at which the container will expire.

        format: date-time

      - `skills: Array[ContainerSkill]`

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

    - `content: Array[ContentBlock]`

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

      - `class TextBlock`

        - `citations: Array[TextCitation]`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class CitationCharLocation`

            - `cited_text: String`

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

            - `end_char_index: Integer`

            - `file_id: String`

            - `start_char_index: Integer`

              minimum: 0

            - `type: :char_location`

          - `class CitationPageLocation`

            - `cited_text: String`

            - `document_index: Integer`

              minimum: 0

            - `document_title: String`

            - `end_page_number: Integer`

            - `file_id: String`

            - `start_page_number: Integer`

              minimum: 1

            - `type: :page_location`

          - `class CitationContentBlockLocation`

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

          - `class CitationsWebSearchResultLocation`

            - `cited_text: String`

            - `encrypted_index: String`

            - `title: String`

              maxLength: 512

            - `type: :web_search_result_location`

            - `url: String`

          - `class CitationsSearchResultLocation`

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

      - `class ThinkingBlock`

        - `signature: String`

          A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

          This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `thinking: String`

          The text of Claude's thinking process for this block.

        - `type: :thinking`

      - `class RedactedThinkingBlock`

        - `data: String`

          The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

          Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

        - `type: :redacted_thinking`

      - `class ToolUseBlock`

        - `id: String`

          pattern: ^[a-zA-Z0-9_-]+$

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

        - `input: Hash[Symbol, untyped]`

        - `name: String`

          minLength: 1

        - `type: :tool_use`

        - `toolset_name: String`

          For a toolset member tool_use, the toolset family.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class ServerToolUseBlock`

        - `id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120`

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

      - `class WebSearchToolResultBlock`

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120`

        - `content: WebSearchToolResultBlockContent`

          - `class WebSearchToolResultError`

            - `error_code: WebSearchToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:max_uses_exceeded`

              - `:too_many_requests`

              - `:query_too_long`

              - `:request_too_large`

            - `type: :web_search_tool_result_error`

          - `UnionMember1 = Array[WebSearchResultBlock]`

            - `encrypted_content: String`

            - `page_age: String`

            - `title: String`

            - `type: :web_search_result`

            - `url: String`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :web_search_tool_result`

      - `class WebFetchToolResultBlock`

        - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `class DirectCaller`

            Tool invocation directly from the model.

          - `class ServerToolCaller`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120`

        - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

          - `class WebFetchToolResultErrorBlock`

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

          - `class WebFetchBlock`

            - `content: DocumentBlock`

              - `citations: CitationsConfig`

                Citation configuration for the document

                - `enabled: bool`

              - `source: Base64PDFSource | PlainTextSource`

                - `class Base64PDFSource`

                  - `data: String`

                    format: byte

                  - `media_type: :"application/pdf"`

                  - `type: :base64`

                - `class PlainTextSource`

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

      - `class CodeExecutionToolResultBlock`

        - `content: CodeExecutionToolResultBlockContent`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultError`

            - `error_code: CodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

            - `type: :code_execution_tool_result_error`

          - `class CodeExecutionResultBlock`

            - `content: Array[CodeExecutionOutputBlock]`

              - `file_id: String`

              - `type: :code_execution_output`

            - `return_code: Integer`

            - `stderr: String`

            - `stdout: String`

            - `type: :code_execution_result`

          - `class EncryptedCodeExecutionResultBlock`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `content: Array[CodeExecutionOutputBlock]`

              - `file_id: String`

              - `type: :code_execution_output`

            - `encrypted_stdout: String`

            - `return_code: Integer`

            - `stderr: String`

            - `type: :encrypted_code_execution_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :code_execution_tool_result`

      - `class BashCodeExecutionToolResultBlock`

        - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

          - `class BashCodeExecutionToolResultError`

            - `error_code: BashCodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

              - `:output_file_too_large`

            - `type: :bash_code_execution_tool_result_error`

          - `class BashCodeExecutionResultBlock`

            - `content: Array[BashCodeExecutionOutputBlock]`

              - `file_id: String`

              - `type: :bash_code_execution_output`

            - `return_code: Integer`

            - `stderr: String`

            - `stdout: String`

            - `type: :bash_code_execution_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :bash_code_execution_tool_result`

      - `class TextEditorCodeExecutionToolResultBlock`

        - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

          - `class TextEditorCodeExecutionToolResultError`

            - `error_code: TextEditorCodeExecutionToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

              - `:file_not_found`

            - `error_message: String`

            - `type: :text_editor_code_execution_tool_result_error`

          - `class TextEditorCodeExecutionViewResultBlock`

            - `content: String`

            - `file_type: :text | :image | :pdf`

              - `:text`

              - `:image`

              - `:pdf`

            - `num_lines: Integer`

            - `start_line: Integer`

            - `total_lines: Integer`

            - `type: :text_editor_code_execution_view_result`

          - `class TextEditorCodeExecutionCreateResultBlock`

            - `is_file_update: bool`

            - `type: :text_editor_code_execution_create_result`

          - `class TextEditorCodeExecutionStrReplaceResultBlock`

            - `lines: Array[String]`

            - `new_lines: Integer`

            - `new_start: Integer`

            - `old_lines: Integer`

            - `old_start: Integer`

            - `type: :text_editor_code_execution_str_replace_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :text_editor_code_execution_tool_result`

      - `class ToolSearchToolResultBlock`

        - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

          - `class ToolSearchToolResultError`

            - `error_code: ToolSearchToolResultErrorCode`

              - `:invalid_tool_input`

              - `:unavailable`

              - `:too_many_requests`

              - `:execution_time_exceeded`

            - `error_message: String`

            - `type: :tool_search_tool_result_error`

          - `class ToolSearchToolSearchResultBlock`

            - `tool_references: Array[ToolReferenceBlock]`

              - `tool_name: String`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `type: :tool_reference`

            - `type: :tool_search_tool_search_result`

        - `tool_use_id: String`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: :tool_search_tool_result`

      - `class ContainerUploadBlock`

        Response model for a file uploaded to the container.

        - `file_id: String`

        - `type: :container_upload`

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

    - `role: :assistant`

      Conversational role of the generated message.

      This will always be `"assistant"`.

    - `stop_details: RefusalStopDetails`

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

      - `type: :refusal`

    - `stop_reason: StopReason`

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

      - `:refusal`

      - `:model_context_window_exceeded`

    - `stop_sequence: String`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `type: :message`

      Object type.

      For Messages, this is always `"message"`.

    - `usage: Usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation: CacheCreation`

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

      - `inference_geo: String`

        The geographic region where inference was performed for this request.

      - `input_tokens: Integer`

        The number of input tokens which were used.

        minimum: 0

      - `output_tokens: Integer`

        The number of output tokens which were used.

        minimum: 0

      - `output_tokens_details: OutputTokensDetails`

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

      - `server_tool_use: ServerToolUsage`

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

  - `type: :message_start`

### Raw Message Stop Event

- `class RawMessageStopEvent`

  - `type: :message_stop`

### Raw Message Stream Event

- `RawMessageStreamEvent = RawMessageStartEvent | RawMessageDeltaEvent | RawMessageStopEvent | 3 more`

  - `class RawMessageStartEvent`

    - `message: Message`

      - `id: String`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `container: Container`

        Information about the container used in the request (for the code execution tool)

        - `id: String`

          Identifier for the container used in this request

        - `expires_at: Time`

          The time at which the container will expire.

          format: date-time

        - `skills: Array[ContainerSkill]`

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

      - `content: Array[ContentBlock]`

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

        - `class TextBlock`

          - `citations: Array[TextCitation]`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class CitationCharLocation`

              - `cited_text: String`

              - `document_index: Integer`

                minimum: 0

              - `document_title: String`

              - `end_char_index: Integer`

              - `file_id: String`

              - `start_char_index: Integer`

                minimum: 0

              - `type: :char_location`

            - `class CitationPageLocation`

              - `cited_text: String`

              - `document_index: Integer`

                minimum: 0

              - `document_title: String`

              - `end_page_number: Integer`

              - `file_id: String`

              - `start_page_number: Integer`

                minimum: 1

              - `type: :page_location`

            - `class CitationContentBlockLocation`

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

            - `class CitationsWebSearchResultLocation`

              - `cited_text: String`

              - `encrypted_index: String`

              - `title: String`

                maxLength: 512

              - `type: :web_search_result_location`

              - `url: String`

            - `class CitationsSearchResultLocation`

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

        - `class ThinkingBlock`

          - `signature: String`

            A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

            This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

          - `thinking: String`

            The text of Claude's thinking process for this block.

          - `type: :thinking`

        - `class RedactedThinkingBlock`

          - `data: String`

            The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

            Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `type: :redacted_thinking`

        - `class ToolUseBlock`

          - `id: String`

            pattern: ^[a-zA-Z0-9_-]+$

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

          - `input: Hash[Symbol, untyped]`

          - `name: String`

            minLength: 1

          - `type: :tool_use`

          - `toolset_name: String`

            For a toolset member tool_use, the toolset family.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ServerToolUseBlock`

          - `id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `class DirectCaller`

              Tool invocation directly from the model.

            - `class ServerToolCaller`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120`

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

        - `class WebSearchToolResultBlock`

          - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `class DirectCaller`

              Tool invocation directly from the model.

            - `class ServerToolCaller`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120`

          - `content: WebSearchToolResultBlockContent`

            - `class WebSearchToolResultError`

              - `error_code: WebSearchToolResultErrorCode`

                - `:invalid_tool_input`

                - `:unavailable`

                - `:max_uses_exceeded`

                - `:too_many_requests`

                - `:query_too_long`

                - `:request_too_large`

              - `type: :web_search_tool_result_error`

            - `UnionMember1 = Array[WebSearchResultBlock]`

              - `encrypted_content: String`

              - `page_age: String`

              - `title: String`

              - `type: :web_search_result`

              - `url: String`

          - `tool_use_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :web_search_tool_result`

        - `class WebFetchToolResultBlock`

          - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `class DirectCaller`

              Tool invocation directly from the model.

            - `class ServerToolCaller`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120`

          - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

            - `class WebFetchToolResultErrorBlock`

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

            - `class WebFetchBlock`

              - `content: DocumentBlock`

                - `citations: CitationsConfig`

                  Citation configuration for the document

                  - `enabled: bool`

                - `source: Base64PDFSource | PlainTextSource`

                  - `class Base64PDFSource`

                    - `data: String`

                      format: byte

                    - `media_type: :"application/pdf"`

                    - `type: :base64`

                  - `class PlainTextSource`

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

        - `class CodeExecutionToolResultBlock`

          - `content: CodeExecutionToolResultBlockContent`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultError`

              - `error_code: CodeExecutionToolResultErrorCode`

                - `:invalid_tool_input`

                - `:unavailable`

                - `:too_many_requests`

                - `:execution_time_exceeded`

              - `type: :code_execution_tool_result_error`

            - `class CodeExecutionResultBlock`

              - `content: Array[CodeExecutionOutputBlock]`

                - `file_id: String`

                - `type: :code_execution_output`

              - `return_code: Integer`

              - `stderr: String`

              - `stdout: String`

              - `type: :code_execution_result`

            - `class EncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `content: Array[CodeExecutionOutputBlock]`

                - `file_id: String`

                - `type: :code_execution_output`

              - `encrypted_stdout: String`

              - `return_code: Integer`

              - `stderr: String`

              - `type: :encrypted_code_execution_result`

          - `tool_use_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :code_execution_tool_result`

        - `class BashCodeExecutionToolResultBlock`

          - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

            - `class BashCodeExecutionToolResultError`

              - `error_code: BashCodeExecutionToolResultErrorCode`

                - `:invalid_tool_input`

                - `:unavailable`

                - `:too_many_requests`

                - `:execution_time_exceeded`

                - `:output_file_too_large`

              - `type: :bash_code_execution_tool_result_error`

            - `class BashCodeExecutionResultBlock`

              - `content: Array[BashCodeExecutionOutputBlock]`

                - `file_id: String`

                - `type: :bash_code_execution_output`

              - `return_code: Integer`

              - `stderr: String`

              - `stdout: String`

              - `type: :bash_code_execution_result`

          - `tool_use_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :bash_code_execution_tool_result`

        - `class TextEditorCodeExecutionToolResultBlock`

          - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

            - `class TextEditorCodeExecutionToolResultError`

              - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                - `:invalid_tool_input`

                - `:unavailable`

                - `:too_many_requests`

                - `:execution_time_exceeded`

                - `:file_not_found`

              - `error_message: String`

              - `type: :text_editor_code_execution_tool_result_error`

            - `class TextEditorCodeExecutionViewResultBlock`

              - `content: String`

              - `file_type: :text | :image | :pdf`

                - `:text`

                - `:image`

                - `:pdf`

              - `num_lines: Integer`

              - `start_line: Integer`

              - `total_lines: Integer`

              - `type: :text_editor_code_execution_view_result`

            - `class TextEditorCodeExecutionCreateResultBlock`

              - `is_file_update: bool`

              - `type: :text_editor_code_execution_create_result`

            - `class TextEditorCodeExecutionStrReplaceResultBlock`

              - `lines: Array[String]`

              - `new_lines: Integer`

              - `new_start: Integer`

              - `old_lines: Integer`

              - `old_start: Integer`

              - `type: :text_editor_code_execution_str_replace_result`

          - `tool_use_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :text_editor_code_execution_tool_result`

        - `class ToolSearchToolResultBlock`

          - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

            - `class ToolSearchToolResultError`

              - `error_code: ToolSearchToolResultErrorCode`

                - `:invalid_tool_input`

                - `:unavailable`

                - `:too_many_requests`

                - `:execution_time_exceeded`

              - `error_message: String`

              - `type: :tool_search_tool_result_error`

            - `class ToolSearchToolSearchResultBlock`

              - `tool_references: Array[ToolReferenceBlock]`

                - `tool_name: String`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `type: :tool_reference`

              - `type: :tool_search_tool_search_result`

          - `tool_use_id: String`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: :tool_search_tool_result`

        - `class ContainerUploadBlock`

          Response model for a file uploaded to the container.

          - `file_id: String`

          - `type: :container_upload`

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

      - `role: :assistant`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `stop_details: RefusalStopDetails`

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

        - `type: :refusal`

      - `stop_reason: StopReason`

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

        - `:refusal`

        - `:model_context_window_exceeded`

      - `stop_sequence: String`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `type: :message`

        Object type.

        For Messages, this is always `"message"`.

      - `usage: Usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `cache_creation: CacheCreation`

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

        - `inference_geo: String`

          The geographic region where inference was performed for this request.

        - `input_tokens: Integer`

          The number of input tokens which were used.

          minimum: 0

        - `output_tokens: Integer`

          The number of output tokens which were used.

          minimum: 0

        - `output_tokens_details: OutputTokensDetails`

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

        - `server_tool_use: ServerToolUsage`

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

    - `type: :message_start`

  - `class RawMessageDeltaEvent`

    - `delta: Delta`

      - `container: Container`

        Information about the container used in the request (for the code execution tool)

      - `stop_details: RefusalStopDetails`

        Structured information about a refusal.

      - `stop_reason: StopReason`

      - `stop_sequence: String`

    - `type: :message_delta`

    - `usage: MessageDeltaUsage`

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

      - `input_tokens: Integer`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `output_tokens: Integer`

        The cumulative number of output tokens which were used.

      - `output_tokens_details: OutputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `server_tool_use: ServerToolUsage`

        The number of server tool requests.

  - `class RawMessageStopEvent`

    - `type: :message_stop`

  - `class RawContentBlockStartEvent`

    - `content_block: TextBlock | ThinkingBlock | RedactedThinkingBlock | 9 more`

      Response model for a file uploaded to the container.

      - `class TextBlock`

      - `class ThinkingBlock`

      - `class RedactedThinkingBlock`

      - `class ToolUseBlock`

      - `class ServerToolUseBlock`

      - `class WebSearchToolResultBlock`

      - `class WebFetchToolResultBlock`

      - `class CodeExecutionToolResultBlock`

      - `class BashCodeExecutionToolResultBlock`

      - `class TextEditorCodeExecutionToolResultBlock`

      - `class ToolSearchToolResultBlock`

      - `class ContainerUploadBlock`

        Response model for a file uploaded to the container.

    - `index: Integer`

    - `type: :content_block_start`

  - `class RawContentBlockDeltaEvent`

    - `delta: RawContentBlockDelta`

      - `class TextDelta`

        - `text: String`

        - `type: :text_delta`

      - `class InputJSONDelta`

        - `partial_json: String`

        - `type: :input_json_delta`

      - `class CitationsDelta`

        - `citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

          - `class CitationCharLocation`

          - `class CitationPageLocation`

          - `class CitationContentBlockLocation`

          - `class CitationsWebSearchResultLocation`

          - `class CitationsSearchResultLocation`

        - `type: :citations_delta`

      - `class ThinkingDelta`

        - `thinking: String`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `type: :thinking_delta`

      - `class SignatureDelta`

        - `signature: String`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `type: :signature_delta`

    - `index: Integer`

    - `type: :content_block_delta`

  - `class RawContentBlockStopEvent`

    - `index: Integer`

    - `type: :content_block_stop`

### Redacted Thinking Block

- `class RedactedThinkingBlock`

  - `data: String`

    The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

    Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

  - `type: :redacted_thinking`

### Redacted Thinking Block Param

- `class RedactedThinkingBlockParam`

  - `data: String`

    The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

  - `type: :redacted_thinking`

### Refusal Stop Details

- `class RefusalStopDetails`

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

  - `type: :refusal`

### Search Result Block Param

- `class SearchResultBlockParam`

  - `content: Array[TextBlockParam]`

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

  - `source: String`

  - `title: String`

  - `type: :search_result`

  - `cache_control: CacheControlEphemeral`

    Create a cache control breakpoint at this content block.

  - `citations: CitationsConfigParam`

    - `enabled: bool`

### Server Tool Caller

- `class ServerToolCaller`

  Tool invocation generated by a server-side tool.

  - `tool_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :code_execution_20250825`

### Server Tool Caller 20260120

- `class ServerToolCaller20260120`

  - `tool_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :code_execution_20260120`

### Server Tool Usage

- `class ServerToolUsage`

  - `web_fetch_requests: Integer`

    The number of web fetch tool requests.

    minimum: 0

  - `web_search_requests: Integer`

    The number of web search tool requests.

    minimum: 0

### Server Tool Use Block

- `class ServerToolUseBlock`

  - `id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

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

### Server Tool Use Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Signature Delta

- `class SignatureDelta`

  - `signature: String`

    The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

  - `type: :signature_delta`

### Skill Params

- `class SkillParams`

  Specification for a skill to be loaded in a container (request model).

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

### Stop Reason

- `StopReason = :end_turn | :max_tokens | :stop_sequence | 4 more`

  - `:end_turn`

  - `:max_tokens`

  - `:stop_sequence`

  - `:tool_use`

  - `:pause_turn`

  - `:refusal`

  - `:model_context_window_exceeded`

### Text Block

- `class TextBlock`

  - `citations: Array[TextCitation]`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `class CitationCharLocation`

      - `cited_text: String`

      - `document_index: Integer`

        minimum: 0

      - `document_title: String`

      - `end_char_index: Integer`

      - `file_id: String`

      - `start_char_index: Integer`

        minimum: 0

      - `type: :char_location`

    - `class CitationPageLocation`

      - `cited_text: String`

      - `document_index: Integer`

        minimum: 0

      - `document_title: String`

      - `end_page_number: Integer`

      - `file_id: String`

      - `start_page_number: Integer`

        minimum: 1

      - `type: :page_location`

    - `class CitationContentBlockLocation`

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

    - `class CitationsWebSearchResultLocation`

      - `cited_text: String`

      - `encrypted_index: String`

      - `title: String`

        maxLength: 512

      - `type: :web_search_result_location`

      - `url: String`

    - `class CitationsSearchResultLocation`

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

### Text Block Param

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

### Text Citation

- `TextCitation = CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | 2 more`

  - `class CitationCharLocation`

    - `cited_text: String`

    - `document_index: Integer`

      minimum: 0

    - `document_title: String`

    - `end_char_index: Integer`

    - `file_id: String`

    - `start_char_index: Integer`

      minimum: 0

    - `type: :char_location`

  - `class CitationPageLocation`

    - `cited_text: String`

    - `document_index: Integer`

      minimum: 0

    - `document_title: String`

    - `end_page_number: Integer`

    - `file_id: String`

    - `start_page_number: Integer`

      minimum: 1

    - `type: :page_location`

  - `class CitationContentBlockLocation`

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

  - `class CitationsWebSearchResultLocation`

    - `cited_text: String`

    - `encrypted_index: String`

    - `title: String`

      maxLength: 512

    - `type: :web_search_result_location`

    - `url: String`

  - `class CitationsSearchResultLocation`

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

### Text Citation Param

- `TextCitationParam = CitationCharLocationParam | CitationPageLocationParam | CitationContentBlockLocationParam | 2 more`

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

### Text Delta

- `class TextDelta`

  - `text: String`

  - `type: :text_delta`

### Text Editor Code Execution Create Result Block

- `class TextEditorCodeExecutionCreateResultBlock`

  - `is_file_update: bool`

  - `type: :text_editor_code_execution_create_result`

### Text Editor Code Execution Create Result Block Param

- `class TextEditorCodeExecutionCreateResultBlockParam`

  - `is_file_update: bool`

  - `type: :text_editor_code_execution_create_result`

### Text Editor Code Execution Str Replace Result Block

- `class TextEditorCodeExecutionStrReplaceResultBlock`

  - `lines: Array[String]`

  - `new_lines: Integer`

  - `new_start: Integer`

  - `old_lines: Integer`

  - `old_start: Integer`

  - `type: :text_editor_code_execution_str_replace_result`

### Text Editor Code Execution Str Replace Result Block Param

- `class TextEditorCodeExecutionStrReplaceResultBlockParam`

  - `type: :text_editor_code_execution_str_replace_result`

  - `lines: Array[String]`

  - `new_lines: Integer`

  - `new_start: Integer`

  - `old_lines: Integer`

  - `old_start: Integer`

### Text Editor Code Execution Tool Result Block

- `class TextEditorCodeExecutionToolResultBlock`

  - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

    - `class TextEditorCodeExecutionToolResultError`

      - `error_code: TextEditorCodeExecutionToolResultErrorCode`

        - `:invalid_tool_input`

        - `:unavailable`

        - `:too_many_requests`

        - `:execution_time_exceeded`

        - `:file_not_found`

      - `error_message: String`

      - `type: :text_editor_code_execution_tool_result_error`

    - `class TextEditorCodeExecutionViewResultBlock`

      - `content: String`

      - `file_type: :text | :image | :pdf`

        - `:text`

        - `:image`

        - `:pdf`

      - `num_lines: Integer`

      - `start_line: Integer`

      - `total_lines: Integer`

      - `type: :text_editor_code_execution_view_result`

    - `class TextEditorCodeExecutionCreateResultBlock`

      - `is_file_update: bool`

      - `type: :text_editor_code_execution_create_result`

    - `class TextEditorCodeExecutionStrReplaceResultBlock`

      - `lines: Array[String]`

      - `new_lines: Integer`

      - `new_start: Integer`

      - `old_lines: Integer`

      - `old_start: Integer`

      - `type: :text_editor_code_execution_str_replace_result`

  - `tool_use_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :text_editor_code_execution_tool_result`

### Text Editor Code Execution Tool Result Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

### Text Editor Code Execution Tool Result Error

- `class TextEditorCodeExecutionToolResultError`

  - `error_code: TextEditorCodeExecutionToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

    - `:file_not_found`

  - `error_message: String`

  - `type: :text_editor_code_execution_tool_result_error`

### Text Editor Code Execution Tool Result Error Code

- `TextEditorCodeExecutionToolResultErrorCode = :invalid_tool_input | :unavailable | :too_many_requests | 2 more`

  - `:invalid_tool_input`

  - `:unavailable`

  - `:too_many_requests`

  - `:execution_time_exceeded`

  - `:file_not_found`

### Text Editor Code Execution Tool Result Error Param

- `class TextEditorCodeExecutionToolResultErrorParam`

  - `error_code: TextEditorCodeExecutionToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

    - `:file_not_found`

  - `type: :text_editor_code_execution_tool_result_error`

  - `error_message: String`

### Text Editor Code Execution View Result Block

- `class TextEditorCodeExecutionViewResultBlock`

  - `content: String`

  - `file_type: :text | :image | :pdf`

    - `:text`

    - `:image`

    - `:pdf`

  - `num_lines: Integer`

  - `start_line: Integer`

  - `total_lines: Integer`

  - `type: :text_editor_code_execution_view_result`

### Text Editor Code Execution View Result Block Param

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

### Thinking Block

- `class ThinkingBlock`

  - `signature: String`

    A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

    This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `thinking: String`

    The text of Claude's thinking process for this block.

  - `type: :thinking`

### Thinking Block Param

- `class ThinkingBlockParam`

  - `signature: String`

    The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

    Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

  - `thinking: String`

    The `thinking` text of this block as returned by the API.

  - `type: :thinking`

### Thinking Config Adaptive

- `class ThinkingConfigAdaptive`

  - `type: :adaptive`

  - `display_: :summarized | :omitted`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `:summarized`

    - `:omitted`

### Thinking Config Disabled

- `class ThinkingConfigDisabled`

  - `type: :disabled`

### Thinking Config Enabled

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

### Thinking Config Param

- `ThinkingConfigParam = ThinkingConfigEnabled | ThinkingConfigDisabled | ThinkingConfigAdaptive`

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

### Thinking Delta

- `class ThinkingDelta`

  - `thinking: String`

    The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

  - `type: :thinking_delta`

### Tool

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Tool Bash 20250124

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: Array[Hash[Symbol, untyped]]`

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `ToolChoice = ToolChoiceAuto | ToolChoiceAny | ToolChoiceTool | ToolChoiceNone`

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

### Tool Choice Any

- `class ToolChoiceAny`

  The model will use any available tools.

  - `type: :any`

  - `disable_parallel_tool_use: bool`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `class ToolChoiceAuto`

  The model will automatically decide whether to use tools.

  - `type: :auto`

  - `disable_parallel_tool_use: bool`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `class ToolChoiceNone`

  The model will not be allowed to use tools.

  - `type: :none`

### Tool Choice Tool

- `class ToolChoiceTool`

  The model will use the specified tool with `tool_choice.name`.

  - `name: String`

    The name of the tool to use.

  - `type: :tool`

  - `disable_parallel_tool_use: bool`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `class ToolReferenceBlock`

  - `tool_name: String`

    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

  - `type: :tool_reference`

### Tool Reference Block Param

- `class ToolReferenceBlockParam`

  Tool reference block that can be included in tool_result content.

  - `tool_name: String`

    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

  - `type: :tool_reference`

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

### Tool Result Block Param

- `class ToolResultBlockParam`

  - `tool_use_id: String`

    pattern: ^[a-zA-Z0-9_-]+$

  - `type: :tool_result`

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

  - `content: String | Array[TextBlockParam | ImageBlockParam | SearchResultBlockParam | 3 more]`

    - `String = String`

    - `Content = Array[TextBlockParam | ImageBlockParam | SearchResultBlockParam | 3 more]`

      - `class TextBlockParam`

        - `text: String`

          minLength: 1

        - `type: :text`

        - `cache_control: CacheControlEphemeral`

          Create a cache control breakpoint at this content block.

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

          - `enabled: bool`

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

        - `context: String`

          minLength: 1

        - `title: String`

          maxLength: 500, minLength: 1

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

### Tool Search Tool Bm25 20251119

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

- `class ToolSearchToolResultBlock`

  - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

    - `class ToolSearchToolResultError`

      - `error_code: ToolSearchToolResultErrorCode`

        - `:invalid_tool_input`

        - `:unavailable`

        - `:too_many_requests`

        - `:execution_time_exceeded`

      - `error_message: String`

      - `type: :tool_search_tool_result_error`

    - `class ToolSearchToolSearchResultBlock`

      - `tool_references: Array[ToolReferenceBlock]`

        - `tool_name: String`

          maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `type: :tool_reference`

      - `type: :tool_search_tool_search_result`

  - `tool_use_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :tool_search_tool_result`

### Tool Search Tool Result Block Param

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

          - `type: :ephemeral`

          - `ttl: :"5m" | :"1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `:"5m"`

            - `:"1h"`

      - `type: :tool_search_tool_search_result`

  - `tool_use_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :tool_search_tool_result`

  - `cache_control: CacheControlEphemeral`

    Create a cache control breakpoint at this content block.

### Tool Search Tool Result Error

- `class ToolSearchToolResultError`

  - `error_code: ToolSearchToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

  - `error_message: String`

  - `type: :tool_search_tool_result_error`

### Tool Search Tool Result Error Code

- `ToolSearchToolResultErrorCode = :invalid_tool_input | :unavailable | :too_many_requests | :execution_time_exceeded`

  - `:invalid_tool_input`

  - `:unavailable`

  - `:too_many_requests`

  - `:execution_time_exceeded`

### Tool Search Tool Result Error Param

- `class ToolSearchToolResultErrorParam`

  - `error_code: ToolSearchToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:too_many_requests`

    - `:execution_time_exceeded`

  - `type: :tool_search_tool_result_error`

  - `error_message: String`

### Tool Search Tool Search Result Block

- `class ToolSearchToolSearchResultBlock`

  - `tool_references: Array[ToolReferenceBlock]`

    - `tool_name: String`

      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

    - `type: :tool_reference`

  - `type: :tool_search_tool_search_result`

### Tool Search Tool Search Result Block Param

- `class ToolSearchToolSearchResultBlockParam`

  - `tool_references: Array[ToolReferenceBlockParam]`

    - `tool_name: String`

      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

    - `type: :tool_reference`

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

  - `type: :tool_search_tool_search_result`

### Tool Text Editor 20250124

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: Array[Hash[Symbol, untyped]]`

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: Array[Hash[Symbol, untyped]]`

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `defer_loading: bool`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: Array[Hash[Symbol, untyped]]`

  - `max_characters: Integer`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    minimum: 1

  - `strict: bool`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `ToolUnion = Tool | ToolBash20250124 | CodeExecutionTool20250522 | 18 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

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

      - `type: :ephemeral`

      - `ttl: :"5m" | :"1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `:"5m"`

        - `:"1h"`

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

      - `enabled: bool`

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

### Tool Use Block

- `class ToolUseBlock`

  - `id: String`

    pattern: ^[a-zA-Z0-9_-]+$

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

  - `input: Hash[Symbol, untyped]`

  - `name: String`

    minLength: 1

  - `type: :tool_use`

  - `toolset_name: String`

    For a toolset member tool_use, the toolset family.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

### Tool Use Block Param

- `class ToolUseBlockParam`

  - `id: String`

    pattern: ^[a-zA-Z0-9_-]+$

  - `input: Hash[Symbol, untyped]`

  - `name: String`

    maxLength: 200, minLength: 1

  - `type: :tool_use`

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

### URL Image Source

- `class URLImageSource`

  - `type: :url`

  - `url: String`

### URL PDF Source

- `class URLPDFSource`

  - `type: :url`

  - `url: String`

### Usage

- `class Usage`

  - `cache_creation: CacheCreation`

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

  - `inference_geo: String`

    The geographic region where inference was performed for this request.

  - `input_tokens: Integer`

    The number of input tokens which were used.

    minimum: 0

  - `output_tokens: Integer`

    The number of output tokens which were used.

    minimum: 0

  - `output_tokens_details: OutputTokensDetails`

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

  - `server_tool_use: ServerToolUsage`

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

### User Location

- `class UserLocation`

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

### Web Fetch Block

- `class WebFetchBlock`

  - `content: DocumentBlock`

    - `citations: CitationsConfig`

      Citation configuration for the document

      - `enabled: bool`

    - `source: Base64PDFSource | PlainTextSource`

      - `class Base64PDFSource`

        - `data: String`

          format: byte

        - `media_type: :"application/pdf"`

        - `type: :base64`

      - `class PlainTextSource`

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

### Web Fetch Block Param

- `class WebFetchBlockParam`

  - `content: DocumentBlockParam`

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

  - `type: :web_fetch_result`

  - `url: String`

    Fetched content URL

  - `retrieved_at: String`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `citations: CitationsConfigParam`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: bool`

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

### Web Fetch Tool 20260209

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `citations: CitationsConfigParam`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: bool`

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

### Web Fetch Tool 20260309

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `citations: CitationsConfigParam`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: bool`

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

### Web Fetch Tool 20260318

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

  - `citations: CitationsConfigParam`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: bool`

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

### Web Fetch Tool Result Block

- `class WebFetchToolResultBlock`

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

  - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

    - `class WebFetchToolResultErrorBlock`

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

    - `class WebFetchBlock`

      - `content: DocumentBlock`

        - `citations: CitationsConfig`

          Citation configuration for the document

          - `enabled: bool`

        - `source: Base64PDFSource | PlainTextSource`

          - `class Base64PDFSource`

            - `data: String`

              format: byte

            - `media_type: :"application/pdf"`

            - `type: :base64`

          - `class PlainTextSource`

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

### Web Fetch Tool Result Block Param

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

### Web Fetch Tool Result Error Block

- `class WebFetchToolResultErrorBlock`

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

### Web Fetch Tool Result Error Block Param

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

### Web Fetch Tool Result Error Code

- `WebFetchToolResultErrorCode = :invalid_tool_input | :url_too_long | :url_not_allowed | 6 more`

  - `:invalid_tool_input`

  - `:url_too_long`

  - `:url_not_allowed`

  - `:url_not_in_prior_context`

  - `:url_not_accessible`

  - `:unsupported_content_type`

  - `:too_many_requests`

  - `:max_uses_exceeded`

  - `:unavailable`

### Web Search Result Block

- `class WebSearchResultBlock`

  - `encrypted_content: String`

  - `page_age: String`

  - `title: String`

  - `type: :web_search_result`

  - `url: String`

### Web Search Result Block Param

- `class WebSearchResultBlockParam`

  - `encrypted_content: String`

  - `title: String`

  - `type: :web_search_result`

  - `url: String`

  - `page_age: String`

### Web Search Tool 20250305

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Web Search Tool 20260209

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Web Search Tool 20260318

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Web Search Tool Request Error

- `class WebSearchToolRequestError`

  - `error_code: WebSearchToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:max_uses_exceeded`

    - `:too_many_requests`

    - `:query_too_long`

    - `:request_too_large`

  - `type: :web_search_tool_result_error`

### Web Search Tool Result Block

- `class WebSearchToolResultBlock`

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

  - `content: WebSearchToolResultBlockContent`

    - `class WebSearchToolResultError`

      - `error_code: WebSearchToolResultErrorCode`

        - `:invalid_tool_input`

        - `:unavailable`

        - `:max_uses_exceeded`

        - `:too_many_requests`

        - `:query_too_long`

        - `:request_too_large`

      - `type: :web_search_tool_result_error`

    - `UnionMember1 = Array[WebSearchResultBlock]`

      - `encrypted_content: String`

      - `page_age: String`

      - `title: String`

      - `type: :web_search_result`

      - `url: String`

  - `tool_use_id: String`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: :web_search_tool_result`

### Web Search Tool Result Block Content

- `WebSearchToolResultBlockContent = WebSearchToolResultError | Array[WebSearchResultBlock]`

  - `class WebSearchToolResultError`

    - `error_code: WebSearchToolResultErrorCode`

      - `:invalid_tool_input`

      - `:unavailable`

      - `:max_uses_exceeded`

      - `:too_many_requests`

      - `:query_too_long`

      - `:request_too_large`

    - `type: :web_search_tool_result_error`

  - `UnionMember1 = Array[WebSearchResultBlock]`

    - `encrypted_content: String`

    - `page_age: String`

    - `title: String`

    - `type: :web_search_result`

    - `url: String`

### Web Search Tool Result Block Param

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

    - `type: :ephemeral`

    - `ttl: :"5m" | :"1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `:"5m"`

      - `:"1h"`

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

### Web Search Tool Result Block Param Content

- `WebSearchToolResultBlockParamContent = Array[WebSearchResultBlockParam] | WebSearchToolRequestError`

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

### Web Search Tool Result Error

- `class WebSearchToolResultError`

  - `error_code: WebSearchToolResultErrorCode`

    - `:invalid_tool_input`

    - `:unavailable`

    - `:max_uses_exceeded`

    - `:too_many_requests`

    - `:query_too_long`

    - `:request_too_large`

  - `type: :web_search_tool_result_error`

### Web Search Tool Result Error Code

- `WebSearchToolResultErrorCode = :invalid_tool_input | :unavailable | :max_uses_exceeded | 3 more`

  - `:invalid_tool_input`

  - `:unavailable`

  - `:max_uses_exceeded`

  - `:too_many_requests`

  - `:query_too_long`

  - `:request_too_large`

## Messages › Batches

### Create a Message Batch

`messages.batches.create(**kwargs) -> MessageBatch`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `requests: Array[Request]`

  List of requests for prompt completion. Each is an individual request to create a Message.

  maxItems: 100000, minItems: 1

  - `custom_id: String`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

  - `params: Params`

    Messages API creation parameters for the individual request.

    See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

    - `max_tokens: Integer`

      The maximum number of tokens to generate before stopping.

      Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

      Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

      Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

      minimum: 0

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

    - `container: MessageCreateParamsContainer`

      Container identifier for reuse across requests.

      - `class ContainerParams`

        Container parameters with skills to be loaded.

        - `id: String`

          Container id

        - `skills: Array[SkillParams]`

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

    - `inference_geo: String`

      Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

    - `metadata: Metadata`

      An object describing metadata about the request.

      - `user_id: String`

        An external identifier for the user who is associated with the request.

        This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

        maxLength: 512

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

    - `service_tier: :auto | :standard_only`

      Determines whether to use priority capacity (if available) or standard capacity for this request.

      Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

      - `:auto`

      - `:standard_only`

    - `stop_sequences: Array[String]`

      Custom text sequences that will cause the model to stop generating.

      Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

      If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

    - `stream: bool`

      Whether to incrementally stream the response using server-sent events.

      See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

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

    - `tools: Array[ToolUnion]`

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

- `user_profile_id: String`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

#### Returns

- `class MessageBatch`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: :in_progress | :canceling | :ended`

    Processing status of the Message Batch.

    - `:in_progress`

    - `:canceling`

    - `:ended`

  - `request_counts: MessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: Integer`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: Integer`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: Integer`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: Integer`

      Number of requests in the Message Batch that are processing.

    - `succeeded: Integer`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: String`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: :message_batch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_batch = anthropic.messages.batches.create(
  requests: [
    {
      custom_id: "my-custom-id-1",
      params: {max_tokens: 1024, messages: [{content: "Hello, world", role: :user}], model: Anthropic::Model::CLAUDE_OPUS_5}
    }
  ]
)

puts(message_batch)
```

##### Response (200)

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

### Retrieve a Message Batch

`messages.batches.retrieve(message_batch_id) -> MessageBatch`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `message_batch_id: String`

  ID of the Message Batch.

#### Returns

- `class MessageBatch`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: :in_progress | :canceling | :ended`

    Processing status of the Message Batch.

    - `:in_progress`

    - `:canceling`

    - `:ended`

  - `request_counts: MessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: Integer`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: Integer`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: Integer`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: Integer`

      Number of requests in the Message Batch that are processing.

    - `succeeded: Integer`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: String`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: :message_batch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_batch = anthropic.messages.batches.retrieve("message_batch_id")

puts(message_batch)
```

##### Response (200)

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

### List Message Batches

`messages.batches.list(**kwargs) -> Page<MessageBatch>`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

#### Returns

- `class MessageBatch`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: :in_progress | :canceling | :ended`

    Processing status of the Message Batch.

    - `:in_progress`

    - `:canceling`

    - `:ended`

  - `request_counts: MessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: Integer`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: Integer`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: Integer`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: Integer`

      Number of requests in the Message Batch that are processing.

    - `succeeded: Integer`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: String`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: :message_batch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.messages.batches.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Cancel a Message Batch

`messages.batches.cancel(message_batch_id) -> MessageBatch`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `message_batch_id: String`

  ID of the Message Batch.

#### Returns

- `class MessageBatch`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: :in_progress | :canceling | :ended`

    Processing status of the Message Batch.

    - `:in_progress`

    - `:canceling`

    - `:ended`

  - `request_counts: MessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: Integer`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: Integer`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: Integer`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: Integer`

      Number of requests in the Message Batch that are processing.

    - `succeeded: Integer`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: String`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: :message_batch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_batch = anthropic.messages.batches.cancel("message_batch_id")

puts(message_batch)
```

##### Response (200)

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

### Delete a Message Batch

`messages.batches.delete(message_batch_id) -> DeletedMessageBatch`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `message_batch_id: String`

  ID of the Message Batch.

#### Returns

- `class DeletedMessageBatch`

  - `id: String`

    ID of the Message Batch.

  - `type: :message_batch_deleted`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

deleted_message_batch = anthropic.messages.batches.delete("message_batch_id")

puts(deleted_message_batch)
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`messages.batches.results(message_batch_id) -> MessageBatchIndividualResponse`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `message_batch_id: String`

  ID of the Message Batch.

#### Returns

- `class MessageBatchIndividualResponse`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: String`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: MessageBatchResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult`

      - `message: Message`

        - `id: String`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: Container`

          Information about the container used in the request (for the code execution tool)

          - `id: String`

            Identifier for the container used in this request

          - `expires_at: Time`

            The time at which the container will expire.

            format: date-time

          - `skills: Array[ContainerSkill]`

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

        - `content: Array[ContentBlock]`

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

          - `class TextBlock`

            - `citations: Array[TextCitation]`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation`

                - `cited_text: String`

                - `document_index: Integer`

                  minimum: 0

                - `document_title: String`

                - `end_char_index: Integer`

                - `file_id: String`

                - `start_char_index: Integer`

                  minimum: 0

                - `type: :char_location`

              - `class CitationPageLocation`

                - `cited_text: String`

                - `document_index: Integer`

                  minimum: 0

                - `document_title: String`

                - `end_page_number: Integer`

                - `file_id: String`

                - `start_page_number: Integer`

                  minimum: 1

                - `type: :page_location`

              - `class CitationContentBlockLocation`

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

              - `class CitationsWebSearchResultLocation`

                - `cited_text: String`

                - `encrypted_index: String`

                - `title: String`

                  maxLength: 512

                - `type: :web_search_result_location`

                - `url: String`

              - `class CitationsSearchResultLocation`

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

          - `class ThinkingBlock`

            - `signature: String`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `thinking: String`

              The text of Claude's thinking process for this block.

            - `type: :thinking`

          - `class RedactedThinkingBlock`

            - `data: String`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `type: :redacted_thinking`

          - `class ToolUseBlock`

            - `id: String`

              pattern: ^[a-zA-Z0-9_-]+$

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

            - `input: Hash[Symbol, untyped]`

            - `name: String`

              minLength: 1

            - `type: :tool_use`

            - `toolset_name: String`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class ServerToolUseBlock`

            - `id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `class DirectCaller`

                Tool invocation directly from the model.

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120`

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

          - `class WebSearchToolResultBlock`

            - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `class DirectCaller`

                Tool invocation directly from the model.

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120`

            - `content: WebSearchToolResultBlockContent`

              - `class WebSearchToolResultError`

                - `error_code: WebSearchToolResultErrorCode`

                  - `:invalid_tool_input`

                  - `:unavailable`

                  - `:max_uses_exceeded`

                  - `:too_many_requests`

                  - `:query_too_long`

                  - `:request_too_large`

                - `type: :web_search_tool_result_error`

              - `UnionMember1 = Array[WebSearchResultBlock]`

                - `encrypted_content: String`

                - `page_age: String`

                - `title: String`

                - `type: :web_search_result`

                - `url: String`

            - `tool_use_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :web_search_tool_result`

          - `class WebFetchToolResultBlock`

            - `caller_: DirectCaller | ServerToolCaller | ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `class DirectCaller`

                Tool invocation directly from the model.

              - `class ServerToolCaller`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120`

            - `content: WebFetchToolResultErrorBlock | WebFetchBlock`

              - `class WebFetchToolResultErrorBlock`

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

              - `class WebFetchBlock`

                - `content: DocumentBlock`

                  - `citations: CitationsConfig`

                    Citation configuration for the document

                    - `enabled: bool`

                  - `source: Base64PDFSource | PlainTextSource`

                    - `class Base64PDFSource`

                      - `data: String`

                        format: byte

                      - `media_type: :"application/pdf"`

                      - `type: :base64`

                    - `class PlainTextSource`

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

          - `class CodeExecutionToolResultBlock`

            - `content: CodeExecutionToolResultBlockContent`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class CodeExecutionToolResultError`

                - `error_code: CodeExecutionToolResultErrorCode`

                  - `:invalid_tool_input`

                  - `:unavailable`

                  - `:too_many_requests`

                  - `:execution_time_exceeded`

                - `type: :code_execution_tool_result_error`

              - `class CodeExecutionResultBlock`

                - `content: Array[CodeExecutionOutputBlock]`

                  - `file_id: String`

                  - `type: :code_execution_output`

                - `return_code: Integer`

                - `stderr: String`

                - `stdout: String`

                - `type: :code_execution_result`

              - `class EncryptedCodeExecutionResultBlock`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `content: Array[CodeExecutionOutputBlock]`

                  - `file_id: String`

                  - `type: :code_execution_output`

                - `encrypted_stdout: String`

                - `return_code: Integer`

                - `stderr: String`

                - `type: :encrypted_code_execution_result`

            - `tool_use_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :code_execution_tool_result`

          - `class BashCodeExecutionToolResultBlock`

            - `content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock`

              - `class BashCodeExecutionToolResultError`

                - `error_code: BashCodeExecutionToolResultErrorCode`

                  - `:invalid_tool_input`

                  - `:unavailable`

                  - `:too_many_requests`

                  - `:execution_time_exceeded`

                  - `:output_file_too_large`

                - `type: :bash_code_execution_tool_result_error`

              - `class BashCodeExecutionResultBlock`

                - `content: Array[BashCodeExecutionOutputBlock]`

                  - `file_id: String`

                  - `type: :bash_code_execution_output`

                - `return_code: Integer`

                - `stderr: String`

                - `stdout: String`

                - `type: :bash_code_execution_result`

            - `tool_use_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :bash_code_execution_tool_result`

          - `class TextEditorCodeExecutionToolResultBlock`

            - `content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock`

              - `class TextEditorCodeExecutionToolResultError`

                - `error_code: TextEditorCodeExecutionToolResultErrorCode`

                  - `:invalid_tool_input`

                  - `:unavailable`

                  - `:too_many_requests`

                  - `:execution_time_exceeded`

                  - `:file_not_found`

                - `error_message: String`

                - `type: :text_editor_code_execution_tool_result_error`

              - `class TextEditorCodeExecutionViewResultBlock`

                - `content: String`

                - `file_type: :text | :image | :pdf`

                  - `:text`

                  - `:image`

                  - `:pdf`

                - `num_lines: Integer`

                - `start_line: Integer`

                - `total_lines: Integer`

                - `type: :text_editor_code_execution_view_result`

              - `class TextEditorCodeExecutionCreateResultBlock`

                - `is_file_update: bool`

                - `type: :text_editor_code_execution_create_result`

              - `class TextEditorCodeExecutionStrReplaceResultBlock`

                - `lines: Array[String]`

                - `new_lines: Integer`

                - `new_start: Integer`

                - `old_lines: Integer`

                - `old_start: Integer`

                - `type: :text_editor_code_execution_str_replace_result`

            - `tool_use_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :text_editor_code_execution_tool_result`

          - `class ToolSearchToolResultBlock`

            - `content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock`

              - `class ToolSearchToolResultError`

                - `error_code: ToolSearchToolResultErrorCode`

                  - `:invalid_tool_input`

                  - `:unavailable`

                  - `:too_many_requests`

                  - `:execution_time_exceeded`

                - `error_message: String`

                - `type: :tool_search_tool_result_error`

              - `class ToolSearchToolSearchResultBlock`

                - `tool_references: Array[ToolReferenceBlock]`

                  - `tool_name: String`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `type: :tool_reference`

                - `type: :tool_search_tool_search_result`

            - `tool_use_id: String`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `type: :tool_search_tool_result`

          - `class ContainerUploadBlock`

            Response model for a file uploaded to the container.

            - `file_id: String`

            - `type: :container_upload`

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

        - `role: :assistant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `stop_details: RefusalStopDetails`

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

          - `type: :refusal`

        - `stop_reason: StopReason`

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

          - `:refusal`

          - `:model_context_window_exceeded`

        - `stop_sequence: String`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `type: :message`

          Object type.

          For Messages, this is always `"message"`.

        - `usage: Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: CacheCreation`

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

          - `inference_geo: String`

            The geographic region where inference was performed for this request.

          - `input_tokens: Integer`

            The number of input tokens which were used.

            minimum: 0

          - `output_tokens: Integer`

            The number of output tokens which were used.

            minimum: 0

          - `output_tokens_details: OutputTokensDetails`

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

          - `server_tool_use: ServerToolUsage`

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

      - `type: :succeeded`

    - `class MessageBatchErroredResult`

      - `error: ErrorResponse`

        - `error: ErrorObject`

          - `class InvalidRequestError`

            - `message: String`

            - `type: :invalid_request_error`

          - `class AuthenticationError`

            - `message: String`

            - `type: :authentication_error`

          - `class BillingError`

            - `message: String`

            - `type: :billing_error`

          - `class PermissionError`

            - `message: String`

            - `type: :permission_error`

          - `class NotFoundError`

            - `message: String`

            - `type: :not_found_error`

          - `class RateLimitError`

            - `message: String`

            - `type: :rate_limit_error`

          - `class GatewayTimeoutError`

            - `message: String`

            - `type: :timeout_error`

          - `class APIErrorObject`

            - `message: String`

            - `type: :api_error`

          - `class OverloadedError`

            - `message: String`

            - `type: :overloaded_error`

        - `request_id: String`

        - `type: :error`

      - `type: :errored`

    - `class MessageBatchCanceledResult`

      - `type: :canceled`

    - `class MessageBatchExpiredResult`

      - `type: :expired`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

message_batch_individual_response = anthropic.messages.batches.results("message_batch_id")

puts(message_batch_individual_response)
```
