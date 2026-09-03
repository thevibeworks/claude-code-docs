# Messages

## Create a Message

`Message messages().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

### Parameters

- `MessageCreateParams params`

  - `Optional<String> userProfileId`

    The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

  - `long maxTokens`

    The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

    Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

    minimum: 0

  - `List<MessageParam> messages`

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

    - `Content content`

      - `String`

      - `List<ContentBlockParam>`

        - `class TextBlockParam:`

          - `String text`

            minLength: 1

          - `JsonValue type = "text"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue type = "ephemeral"`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

                maxLength: 500, minLength: 1

              - `long endCharIndex`

              - `long startCharIndex`

                minimum: 0

              - `JsonValue type = "char_location"`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

                maxLength: 500, minLength: 1

              - `long endPageNumber`

              - `long startPageNumber`

                minimum: 1

              - `JsonValue type = "page_location"`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

                maxLength: 500, minLength: 1

              - `long endBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `long startBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `JsonValue type = "content_block_location"`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

                maxLength: 512, minLength: 1

              - `JsonValue type = "web_search_result_location"`

              - `String url`

                minLength: 1

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `long endBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `long searchResultIndex`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

                minimum: 0

              - `String source`

              - `long startBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `Optional<String> title`

              - `JsonValue type = "search_result_location"`

        - `class ImageBlockParam:`

          - `Source source`

            - `class Base64ImageSource:`

              - `String data`

                format: byte

              - `MediaType mediaType`

                - `IMAGE_JPEG("image/jpeg")`

                - `IMAGE_PNG("image/png")`

                - `IMAGE_GIF("image/gif")`

                - `IMAGE_WEBP("image/webp")`

              - `JsonValue type = "base64"`

            - `class UrlImageSource:`

              - `JsonValue type = "url"`

              - `String url`

            - `class FileImageSource:`

              - `String fileId`

              - `JsonValue type = "file"`

          - `JsonValue type = "image"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<ImageTransformationsParam> transformations`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

            - `Optional<OversizedImage> oversizedImage`

              What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

              - `DOWNSIZE("downsize")`

              - `ERROR("error")`

        - `class DocumentBlockParam:`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

                format: byte

              - `JsonValue mediaType = "application/pdf"`

              - `JsonValue type = "base64"`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue mediaType = "text/plain"`

              - `JsonValue type = "text"`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                  - `class ImageBlockParam:`

              - `JsonValue type = "content"`

            - `class UrlPdfSource:`

              - `JsonValue type = "url"`

              - `String url`

            - `class FileDocumentSource:`

              - `String fileId`

              - `JsonValue type = "file"`

          - `JsonValue type = "document"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

            minLength: 1

          - `Optional<String> title`

            maxLength: 500, minLength: 1

        - `class SearchResultBlockParam:`

          - `List<TextBlockParam> content`

            - `String text`

              minLength: 1

            - `JsonValue type = "text"`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

            - `Optional<List<TextCitationParam>> citations`

          - `String source`

          - `String title`

          - `JsonValue type = "search_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

        - `class ThinkingBlockParam:`

          - `String signature`

            The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

            Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

          - `String thinking`

            The `thinking` text of this block as returned by the API.

          - `JsonValue type = "thinking"`

        - `class RedactedThinkingBlockParam:`

          - `String data`

            The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `JsonValue type = "redacted_thinking"`

        - `class ToolUseBlockParam:`

          - `String id`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Input input`

          - `String name`

            maxLength: 200, minLength: 1

          - `JsonValue type = "tool_use"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue type = "direct"`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_20250825"`

            - `class ServerToolCaller20260120:`

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_20260120"`

          - `Optional<String> toolsetName`

            For a toolset member tool_use, the toolset family this member belongs to.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ToolResultBlockParam:`

          - `String toolUseId`

            pattern: ^[a-zA-Z0-9_-]+$

          - `JsonValue type = "tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Content> content`

            - `String`

            - `List<Block>`

              - `class TextBlockParam:`

              - `class ImageBlockParam:`

              - `class SearchResultBlockParam:`

              - `class DocumentBlockParam:`

              - `class ToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `String toolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonValue type = "tool_reference"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

              - `class BrowserStateBlockParam:`

                The caller's browser state after a browser toolset member call —
                the full inventory of open tabs, which tab is active, and any side
                effects (tabs opened, download state changes) the call produced.

                At most one per `tool_result`, only on a non-error result answering a
                browser toolset member `tool_use`. The server renders the
                model-visible text from it; the model never sees the raw fields.

                - `List<BrowserStateTabEntry> tabs`

                  All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                  maxItems: 100

                  - `String tabId`

                    The caller-assigned identifier for this tab, unique within the inventory.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `String title`

                    The title of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `String url`

                    The URL of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `Optional<Boolean> active`

                    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                - `JsonValue type = "browser_state"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                - `Optional<List<BrowserStateChange>> stateChanges`

                  Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                  maxItems: 200, minItems: 1

                  - `class BrowserStateChangeTabOpened:`

                    A tab this call's execution opened that remains open at its end —
                    the creation delta of the `tabs` inventory, not an event log.

                    Carries only the `tab_id`; the tab's `title` and `url` live on its
                    `tabs` entry, which must include the same `tab_id`. A tab opened
                    during a failed call gets no deferred `tab_opened`; it simply appears
                    in the next result's `tabs` inventory.

                    - `String tabId`

                      The `tab_id` of the opened tab, present in `tabs`.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "tab_opened"`

                  - `class BrowserStateChangeDownloadStarted:`

                    A file download that started during this call.

                    - `String downloadId`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "download_started"`

                    - `String url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `class BrowserStateChangeDownloadCompleted:`

                    A file download that finished during this call, reported with the
                    same `download_id` as its `download_started` — or without a prior
                    `download_started`, when the download finished during the call that
                    started it (at most one state change per `download_id` per result).

                    - `String downloadId`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "download_completed"`

                    - `String url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `Optional<String> path`

                      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                    - `Optional<Long> sizeBytes`

                      The completed download's size.

                      minimum: 0

                  - `class BrowserStateChangeDownloadFailed:`

                    A file download that failed — or was cancelled — during this call.

                    - `String downloadId`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "download_failed"`

                    - `String url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `Optional<String> error`

                      The failure or cancellation detail, when known.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

          - `Optional<Boolean> isError`

          - `Optional<String> toolsetName`

            For a toolset member tool_result, the toolset family of the paired tool_use.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ServerToolUseBlockParam:`

          - `String id`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue type = "server_tool_use"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class WebSearchToolResultBlockParam:`

          - `WebSearchToolResultBlockParamContent content`

            - `List<WebSearchResultBlockParam>`

              - `String encryptedContent`

              - `String title`

              - `JsonValue type = "web_search_result"`

              - `String url`

              - `Optional<String> pageAge`

            - `class WebSearchToolRequestError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue type = "web_search_tool_result_error"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "web_search_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class WebFetchToolResultBlockParam:`

          - `Content content`

            - `class WebFetchToolResultErrorBlockParam:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue type = "web_fetch_tool_result_error"`

            - `class WebFetchBlockParam:`

              - `DocumentBlockParam content`

              - `JsonValue type = "web_fetch_result"`

              - `String url`

                Fetched content URL

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "web_fetch_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class CodeExecutionToolResultBlockParam:`

          - `CodeExecutionToolResultBlockParamContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultErrorParam:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue type = "code_execution_tool_result_error"`

            - `class CodeExecutionResultBlockParam:`

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue type = "code_execution_output"`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type = "code_execution_result"`

            - `class EncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue type = "code_execution_output"`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue type = "encrypted_code_execution_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class BashCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class BashCodeExecutionToolResultErrorParam:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue type = "bash_code_execution_tool_result_error"`

            - `class BashCodeExecutionResultBlockParam:`

              - `List<BashCodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue type = "bash_code_execution_output"`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type = "bash_code_execution_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "bash_code_execution_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class TextEditorCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultErrorParam:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `JsonValue type = "text_editor_code_execution_tool_result_error"`

              - `Optional<String> errorMessage`

            - `class TextEditorCodeExecutionViewResultBlockParam:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `JsonValue type = "text_editor_code_execution_view_result"`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

            - `class TextEditorCodeExecutionCreateResultBlockParam:`

              - `boolean isFileUpdate`

              - `JsonValue type = "text_editor_code_execution_create_result"`

            - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonValue type = "text_editor_code_execution_str_replace_result"`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "text_editor_code_execution_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class ToolSearchToolResultBlockParam:`

          - `Content content`

            - `class ToolSearchToolResultErrorParam:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue type = "tool_search_tool_result_error"`

              - `Optional<String> errorMessage`

            - `class ToolSearchToolSearchResultBlockParam:`

              - `List<ToolReferenceBlockParam> toolReferences`

                - `String toolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonValue type = "tool_reference"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

              - `JsonValue type = "tool_search_tool_search_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "tool_search_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class ContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `String fileId`

          - `JsonValue type = "container_upload"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

    - `Role role`

      - `USER("user")`

      - `ASSISTANT("assistant")`

      - `SYSTEM("system")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Optional<CacheControlEphemeral> cacheControl`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Optional<MessageCreateParamsContainer> container`

    Container identifier for reuse across requests.

  - `Optional<String> inferenceGeo`

    Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `Optional<Metadata> metadata`

    An object describing metadata about the request.

  - `Optional<OutputConfig> outputConfig`

    Configuration options for the model's output, such as the output format.

  - `Optional<ServiceTier> serviceTier`

    Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

    - `AUTO("auto")`

    - `STANDARD_ONLY("standard_only")`

  - `Optional<List<String>> stopSequences`

    Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `Optional<System> system`

    System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `String`

    - `List<TextBlockParam>`

      - `String text`

        minLength: 1

      - `JsonValue type = "text"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<List<TextCitationParam>> citations`

  - `Optional<ThinkingConfigParam> thinking`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `Optional<ToolChoice> toolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `Optional<List<ToolUnion>> tools`

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

    - `class Tool:`

      - `InputSchema inputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonValue type = "object"`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<String> description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `Optional<Boolean> eagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Type> type`

    - `class ToolBash20250124:`

      - `JsonValue name = "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "bash_20250124"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250522:`

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20250522"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250825:`

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20250825"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20260120"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260521:`

      Code execution tool with REPL state persistence.

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20260521"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BrowserToolset20260801:`

      The browser toolset: a single `tools[]` entry (carrying no
      `name`) that declares the browser tool family. The model is served
      the family's tool with any members disabled via `configs` removed
      from its schema.

      - `JsonValue type = "browser_toolset_20260801"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<BrowserToolsetConfigs> configs`

        Per-member configuration for `browser_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `Optional<BrowserCloseTabConfig> closeTab`

          `close_tab`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserDoubleClickConfig> doubleClick`

          `double_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserFileUploadConfig> fileUpload`

          `file_upload`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserFindConfig> find`

          `find`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserFormInputConfig> formInput`

          `form_input`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserGetPageTextConfig> getPageText`

          `get_page_text`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserHoldKeyConfig> holdKey`

          `hold_key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserHoverConfig> hover`

          `hover`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserJavascriptExecConfig> javascriptExec`

          `javascript_exec`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserKeyConfig> key`

          `key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftClickConfig> leftClick`

          `left_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

          `left_click_drag`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

          `left_mouse_down`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

          `left_mouse_up`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserListTabsConfig> listTabs`

          `list_tabs`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserMiddleClickConfig> middleClick`

          `middle_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserMouseMoveConfig> mouseMove`

          `mouse_move`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserNavigateConfig> navigate`

          `navigate`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserNewTabConfig> newTab`

          `new_tab`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserReadConsoleConfig> readConsole`

          `read_console`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserReadNetworkConfig> readNetwork`

          `read_network`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserReadPageConfig> readPage`

          `read_page`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserRightClickConfig> rightClick`

          `right_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserScreenshotConfig> screenshot`

          `screenshot`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserScrollConfig> scroll`

          `scroll`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserScrollToConfig> scrollTo`

          `scroll_to`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserSwitchTabConfig> switchTab`

          `switch_tab`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserTripleClickConfig> tripleClick`

          `triple_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserTypeConfig> type`

          `type`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserWaitConfig> wait`

          `wait`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserZoomConfig> zoom`

          `zoom`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class MemoryTool20250818:`

      - `JsonValue name = "memory"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "memory_20250818"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ComputerToolset20260801:`

      The computer toolset: a single `tools[]` entry (carrying no
      `name`) that declares the computer tool family. The model is
      served the family's tool with any members disabled via `configs`
      removed from its schema. Every member is enabled by default, zoom
      included. The single-tool options `display_number` and
      `enable_zoom` are not fields of a toolset entry — it carries only
      `type`, `configs`, and `cache_control`; zoom is controlled
      via `configs.zoom.enabled`.

      - `JsonValue type = "computer_toolset_20260801"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<ComputerToolsetConfigs> configs`

        Per-member configuration for `computer_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `Optional<ComputerCursorPositionConfig> cursorPosition`

          `cursor_position`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerDoubleClickConfig> doubleClick`

          `double_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerHoldKeyConfig> holdKey`

          `hold_key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerKeyConfig> key`

          `key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftClickConfig> leftClick`

          `left_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

          `left_click_drag`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

          `left_mouse_down`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

          `left_mouse_up`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerMiddleClickConfig> middleClick`

          `middle_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerMouseMoveConfig> mouseMove`

          `mouse_move`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerRightClickConfig> rightClick`

          `right_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerScreenshotConfig> screenshot`

          `screenshot`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerScrollConfig> scroll`

          `scroll`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerTripleClickConfig> tripleClick`

          `triple_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerTypeConfig> type`

          `type`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerWaitConfig> wait`

          `wait`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerZoomConfig> zoom`

          `zoom`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class ToolTextEditor20250124:`

      - `JsonValue name = "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "text_editor_20250124"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250429:`

      - `JsonValue name = "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "text_editor_20250429"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250728:`

      - `JsonValue name = "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "text_editor_20250728"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Long> maxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        minimum: 1

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20250305:`

      - `JsonValue name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_search_20250305"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue type = "approximate"`

        - `Optional<String> city`

          The city of the user.

          maxLength: 255, minLength: 1

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          maxLength: 2, minLength: 2

        - `Optional<String> region`

          The region of the user.

          maxLength: 255, minLength: 1

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

          maxLength: 255, minLength: 1

    - `class WebFetchTool20250910:`

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20250910"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20260209:`

      - `JsonValue name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_search_20260209"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class WebFetchTool20260209:`

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20260209"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebFetchTool20260309:`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20260309"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Boolean> useCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class WebSearchTool20260318:`

      - `JsonValue name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_search_20260318"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<ResponseInclusion> responseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `FULL("full")`

        - `EXCLUDED("excluded")`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class WebFetchTool20260318:`

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20260318"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<ResponseInclusion> responseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `FULL("full")`

        - `EXCLUDED("excluded")`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Boolean> useCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class ToolSearchToolBm25_20251119:`

      - `JsonValue name = "tool_search_tool_bm25"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type type`

        - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolRegex20251119:`

      - `JsonValue name = "tool_search_tool_regex"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type type`

        - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

  - `Optional<Double> temperature`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    maximum: 1, minimum: 0

  - `Optional<Long> topK`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

    Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

    minimum: 0

  - `Optional<Double> topP`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

    maximum: 1, minimum: 0

### Returns

- `class Message:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<Container> container`

    Information about the container used in the request (for the code execution tool)

    - `String id`

      Identifier for the container used in this request

    - `LocalDateTime expiresAt`

      The time at which the container will expire.

      format: date-time

    - `Optional<List<ContainerSkill>> skills`

      Skills loaded in the container

      - `String skillId`

        Skill ID

        maxLength: 64, minLength: 1

      - `Type type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `ANTHROPIC("anthropic")`

        - `CUSTOM("custom")`

      - `String version`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `List<ContentBlock> content`

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

    - `class TextBlock:`

      - `Optional<List<TextCitation>> citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

            minimum: 0

          - `JsonValue type = "char_location"`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

            minimum: 1

          - `JsonValue type = "page_location"`

        - `class CitationContentBlockLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `Optional<String> fileId`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `JsonValue type = "content_block_location"`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

            maxLength: 512

          - `JsonValue type = "web_search_result_location"`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `long searchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `String source`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `Optional<String> title`

          - `JsonValue type = "search_result_location"`

      - `String text`

        maxLength: 5000000, minLength: 0

      - `JsonValue type = "text"`

    - `class ThinkingBlock:`

      - `String signature`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `String thinking`

        The text of Claude's thinking process for this block.

      - `JsonValue type = "thinking"`

    - `class RedactedThinkingBlock:`

      - `String data`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `JsonValue type = "redacted_thinking"`

    - `class ToolUseBlock:`

      - `String id`

        pattern: ^[a-zA-Z0-9_-]+$

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue type = "direct"`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_20250825"`

        - `class ServerToolCaller20260120:`

          - `String toolId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_20260120"`

      - `Input input`

      - `String name`

        minLength: 1

      - `JsonValue type = "tool_use"`

      - `Optional<String> toolsetName`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock:`

      - `String id`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `Input input`

      - `Name name`

        - `WEB_SEARCH("web_search")`

        - `WEB_FETCH("web_fetch")`

        - `CODE_EXECUTION("code_execution")`

        - `BASH_CODE_EXECUTION("bash_code_execution")`

        - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `JsonValue type = "server_tool_use"`

    - `class WebSearchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `WebSearchToolResultBlockContent content`

        - `class WebSearchToolResultError:`

          - `WebSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `QUERY_TOO_LONG("query_too_long")`

            - `REQUEST_TOO_LARGE("request_too_large")`

          - `JsonValue type = "web_search_tool_result_error"`

        - `List<WebSearchResultBlock>`

          - `String encryptedContent`

          - `Optional<String> pageAge`

          - `String title`

          - `JsonValue type = "web_search_result"`

          - `String url`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "web_search_tool_result"`

    - `class WebFetchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `Content content`

        - `class WebFetchToolResultErrorBlock:`

          - `WebFetchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `URL_TOO_LONG("url_too_long")`

            - `URL_NOT_ALLOWED("url_not_allowed")`

            - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

            - `URL_NOT_ACCESSIBLE("url_not_accessible")`

            - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `UNAVAILABLE("unavailable")`

          - `JsonValue type = "web_fetch_tool_result_error"`

        - `class WebFetchBlock:`

          - `DocumentBlock content`

            - `Optional<CitationsConfig> citations`

              Citation configuration for the document

              - `boolean enabled`

            - `Source source`

              - `class Base64PdfSource:`

                - `String data`

                  format: byte

                - `JsonValue mediaType = "application/pdf"`

                - `JsonValue type = "base64"`

              - `class PlainTextSource:`

                - `String data`

                - `JsonValue mediaType = "text/plain"`

                - `JsonValue type = "text"`

            - `Optional<String> title`

              The title of the document

            - `JsonValue type = "document"`

          - `Optional<String> retrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonValue type = "web_fetch_result"`

          - `String url`

            Fetched content URL

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "web_fetch_tool_result"`

    - `class CodeExecutionToolResultBlock:`

      - `CodeExecutionToolResultBlockContent content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `CodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `JsonValue type = "code_execution_tool_result_error"`

        - `class CodeExecutionResultBlock:`

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "code_execution_output"`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue type = "code_execution_result"`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "code_execution_output"`

          - `String encryptedStdout`

          - `long returnCode`

          - `String stderr`

          - `JsonValue type = "encrypted_code_execution_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_tool_result"`

    - `class BashCodeExecutionToolResultBlock:`

      - `Content content`

        - `class BashCodeExecutionToolResultError:`

          - `BashCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

          - `JsonValue type = "bash_code_execution_tool_result_error"`

        - `class BashCodeExecutionResultBlock:`

          - `List<BashCodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "bash_code_execution_output"`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue type = "bash_code_execution_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "bash_code_execution_tool_result"`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `Content content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `TextEditorCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `FILE_NOT_FOUND("file_not_found")`

          - `Optional<String> errorMessage`

          - `JsonValue type = "text_editor_code_execution_tool_result_error"`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `String content`

          - `FileType fileType`

            - `TEXT("text")`

            - `IMAGE("image")`

            - `PDF("pdf")`

          - `Optional<Long> numLines`

          - `Optional<Long> startLine`

          - `Optional<Long> totalLines`

          - `JsonValue type = "text_editor_code_execution_view_result"`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `boolean isFileUpdate`

          - `JsonValue type = "text_editor_code_execution_create_result"`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `Optional<List<String>> lines`

          - `Optional<Long> newLines`

          - `Optional<Long> newStart`

          - `Optional<Long> oldLines`

          - `Optional<Long> oldStart`

          - `JsonValue type = "text_editor_code_execution_str_replace_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "text_editor_code_execution_tool_result"`

    - `class ToolSearchToolResultBlock:`

      - `Content content`

        - `class ToolSearchToolResultError:`

          - `ToolSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `Optional<String> errorMessage`

          - `JsonValue type = "tool_search_tool_result_error"`

        - `class ToolSearchToolSearchResultBlock:`

          - `List<ToolReferenceBlock> toolReferences`

            - `String toolName`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `JsonValue type = "tool_reference"`

          - `JsonValue type = "tool_search_tool_search_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "tool_search_tool_result"`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `String fileId`

      - `JsonValue type = "container_upload"`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

      Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

    - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

      Our most capable model for cybersecurity and biology research, available through trusted access programs

    - `CLAUDE_SONNET_5("claude-sonnet-5")`

      High-performance model for coding and agents

    - `CLAUDE_FABLE_5("claude-fable-5")`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `CLAUDE_MYTHOS_5("claude-mythos-5")`

      Most capable model for cybersecurity and biology research

    - `CLAUDE_OPUS_5("claude-opus-5")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

      New class of intelligence, strongest in coding and cybersecurity

    - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

      Best combination of speed and intelligence

    - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

      Fastest model with near-frontier intelligence

    - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

      Fastest model with near-frontier intelligence

    - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

      High-performance model for agents and coding

    - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

      High-performance model for agents and coding

  - `JsonValue role = "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `Optional<RefusalStopDetails> stopDetails`

    Structured information about a refusal.

    - `Optional<Category> category`

      The policy category that triggered a refusal.

      - `CYBER("cyber")`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `BIO("bio")`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `FRONTIER_LLM("frontier_llm")`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `REASONING_EXTRACTION("reasoning_extraction")`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `GENERAL_HARMS("general_harms")`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `Optional<String> explanation`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `JsonValue type = "refusal"`

  - `Optional<StopReason> stopReason`

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

    - `END_TURN("end_turn")`

    - `MAX_TOKENS("max_tokens")`

    - `STOP_SEQUENCE("stop_sequence")`

    - `TOOL_USE("tool_use")`

    - `PAUSE_TURN("pause_turn")`

    - `REFUSAL("refusal")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

  - `Optional<String> stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonValue type = "message"`

    Object type.

    For Messages, this is always `"message"`.

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `Optional<CacheCreation> cacheCreation`

      Breakdown of cached tokens by TTL

      - `long ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `long ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `Optional<Long> cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `Optional<Long> cacheReadInputTokens`

      The number of input tokens read from the cache.

      minimum: 0

    - `Optional<String> inferenceGeo`

      The geographic region where inference was performed for this request.

    - `long inputTokens`

      The number of input tokens which were used.

      minimum: 0

    - `long outputTokens`

      The number of output tokens which were used.

      minimum: 0

    - `Optional<OutputTokensDetails> outputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `long thinkingTokens`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `Optional<ServerToolUsage> serverToolUse`

      The number of server tool requests.

      - `long webFetchRequests`

        The number of web fetch tool requests.

        minimum: 0

      - `long webSearchRequests`

        The number of web search tool requests.

        minimum: 0

    - `Optional<ServiceTier> serviceTier`

      If the request used the priority, standard, or batch tier.

      - `STANDARD("standard")`

      - `PRIORITY("priority")`

      - `BATCH("batch")`

- `class RawMessageStreamEvent: union`

  - `class RawMessageStartEvent:`

    - `Message message`

    - `JsonValue type = "message_start"`

  - `class RawMessageDeltaEvent:`

    - `Delta delta`

      - `Optional<Container> container`

        Information about the container used in the request (for the code execution tool)

      - `Optional<RefusalStopDetails> stopDetails`

        Structured information about a refusal.

      - `Optional<StopReason> stopReason`

      - `Optional<String> stopSequence`

    - `JsonValue type = "message_delta"`

    - `MessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<Long> cacheCreationInputTokens`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `Optional<Long> cacheReadInputTokens`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `Optional<Long> inputTokens`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `long outputTokens`

        The cumulative number of output tokens which were used.

      - `Optional<OutputTokensDetails> outputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `Optional<ServerToolUsage> serverToolUse`

        The number of server tool requests.

  - `class RawMessageStopEvent:`

    - `JsonValue type = "message_stop"`

  - `class RawContentBlockStartEvent:`

    - `ContentBlock contentBlock`

      Response model for a file uploaded to the container.

      - `class TextBlock:`

      - `class ThinkingBlock:`

      - `class RedactedThinkingBlock:`

      - `class ToolUseBlock:`

      - `class ServerToolUseBlock:`

      - `class WebSearchToolResultBlock:`

      - `class WebFetchToolResultBlock:`

      - `class CodeExecutionToolResultBlock:`

      - `class BashCodeExecutionToolResultBlock:`

      - `class TextEditorCodeExecutionToolResultBlock:`

      - `class ToolSearchToolResultBlock:`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

    - `long index`

    - `JsonValue type = "content_block_start"`

  - `class RawContentBlockDeltaEvent:`

    - `RawContentBlockDelta delta`

      - `class TextDelta:`

        - `String text`

        - `JsonValue type = "text_delta"`

      - `class InputJsonDelta:`

        - `String partialJson`

        - `JsonValue type = "input_json_delta"`

      - `class CitationsDelta:`

        - `Citation citation`

          - `class CitationCharLocation:`

          - `class CitationPageLocation:`

          - `class CitationContentBlockLocation:`

          - `class CitationsWebSearchResultLocation:`

          - `class CitationsSearchResultLocation:`

        - `JsonValue type = "citations_delta"`

      - `class ThinkingDelta:`

        - `String thinking`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `JsonValue type = "thinking_delta"`

      - `class SignatureDelta:`

        - `String signature`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `JsonValue type = "signature_delta"`

    - `long index`

    - `JsonValue type = "content_block_delta"`

  - `class RawContentBlockStopEvent:`

    - `long index`

    - `JsonValue type = "content_block_stop"`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Message;
import com.anthropic.models.messages.MessageCreateParams;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCreateParams params = MessageCreateParams.builder()
            .maxTokens(1024L)
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_5)
            .build();
        Message message = client.messages().create(params);
    }
}
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

`MessageTokensCount messages().countTokens(params, requestOptions = RequestOptions.none())`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Parameters

- `MessageCountTokensParams params`

  - `Optional<String> userProfileId`

    The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

  - `List<MessageParam> messages`

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

    - `Content content`

      - `String`

      - `List<ContentBlockParam>`

        - `class TextBlockParam:`

          - `String text`

            minLength: 1

          - `JsonValue type = "text"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonValue type = "ephemeral"`

            - `Optional<Ttl> ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `TTL_5M("5m")`

              - `TTL_1H("1h")`

          - `Optional<List<TextCitationParam>> citations`

            - `class CitationCharLocationParam:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

                maxLength: 500, minLength: 1

              - `long endCharIndex`

              - `long startCharIndex`

                minimum: 0

              - `JsonValue type = "char_location"`

            - `class CitationPageLocationParam:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

                maxLength: 500, minLength: 1

              - `long endPageNumber`

              - `long startPageNumber`

                minimum: 1

              - `JsonValue type = "page_location"`

            - `class CitationContentBlockLocationParam:`

              - `String citedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

                maxLength: 500, minLength: 1

              - `long endBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `long startBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `JsonValue type = "content_block_location"`

            - `class CitationWebSearchResultLocationParam:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

                maxLength: 512, minLength: 1

              - `JsonValue type = "web_search_result_location"`

              - `String url`

                minLength: 1

            - `class CitationSearchResultLocationParam:`

              - `String citedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `long endBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `long searchResultIndex`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

                minimum: 0

              - `String source`

              - `long startBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `Optional<String> title`

              - `JsonValue type = "search_result_location"`

        - `class ImageBlockParam:`

          - `Source source`

            - `class Base64ImageSource:`

              - `String data`

                format: byte

              - `MediaType mediaType`

                - `IMAGE_JPEG("image/jpeg")`

                - `IMAGE_PNG("image/png")`

                - `IMAGE_GIF("image/gif")`

                - `IMAGE_WEBP("image/webp")`

              - `JsonValue type = "base64"`

            - `class UrlImageSource:`

              - `JsonValue type = "url"`

              - `String url`

            - `class FileImageSource:`

              - `String fileId`

              - `JsonValue type = "file"`

          - `JsonValue type = "image"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<ImageTransformationsParam> transformations`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

            - `Optional<OversizedImage> oversizedImage`

              What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

              - `DOWNSIZE("downsize")`

              - `ERROR("error")`

        - `class DocumentBlockParam:`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

                format: byte

              - `JsonValue mediaType = "application/pdf"`

              - `JsonValue type = "base64"`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue mediaType = "text/plain"`

              - `JsonValue type = "text"`

            - `class ContentBlockSource:`

              - `Content content`

                - `String`

                - `List<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                  - `class ImageBlockParam:`

              - `JsonValue type = "content"`

            - `class UrlPdfSource:`

              - `JsonValue type = "url"`

              - `String url`

            - `class FileDocumentSource:`

              - `String fileId`

              - `JsonValue type = "file"`

          - `JsonValue type = "document"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            - `Optional<Boolean> enabled`

          - `Optional<String> context`

            minLength: 1

          - `Optional<String> title`

            maxLength: 500, minLength: 1

        - `class SearchResultBlockParam:`

          - `List<TextBlockParam> content`

            - `String text`

              minLength: 1

            - `JsonValue type = "text"`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

            - `Optional<List<TextCitationParam>> citations`

          - `String source`

          - `String title`

          - `JsonValue type = "search_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

        - `class ThinkingBlockParam:`

          - `String signature`

            The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

            Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

          - `String thinking`

            The `thinking` text of this block as returned by the API.

          - `JsonValue type = "thinking"`

        - `class RedactedThinkingBlockParam:`

          - `String data`

            The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `JsonValue type = "redacted_thinking"`

        - `class ToolUseBlockParam:`

          - `String id`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Input input`

          - `String name`

            maxLength: 200, minLength: 1

          - `JsonValue type = "tool_use"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue type = "direct"`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_20250825"`

            - `class ServerToolCaller20260120:`

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_20260120"`

          - `Optional<String> toolsetName`

            For a toolset member tool_use, the toolset family this member belongs to.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ToolResultBlockParam:`

          - `String toolUseId`

            pattern: ^[a-zA-Z0-9_-]+$

          - `JsonValue type = "tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Content> content`

            - `String`

            - `List<Block>`

              - `class TextBlockParam:`

              - `class ImageBlockParam:`

              - `class SearchResultBlockParam:`

              - `class DocumentBlockParam:`

              - `class ToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `String toolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonValue type = "tool_reference"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

              - `class BrowserStateBlockParam:`

                The caller's browser state after a browser toolset member call —
                the full inventory of open tabs, which tab is active, and any side
                effects (tabs opened, download state changes) the call produced.

                At most one per `tool_result`, only on a non-error result answering a
                browser toolset member `tool_use`. The server renders the
                model-visible text from it; the model never sees the raw fields.

                - `List<BrowserStateTabEntry> tabs`

                  All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                  maxItems: 100

                  - `String tabId`

                    The caller-assigned identifier for this tab, unique within the inventory.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `String title`

                    The title of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `String url`

                    The URL of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `Optional<Boolean> active`

                    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                - `JsonValue type = "browser_state"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                - `Optional<List<BrowserStateChange>> stateChanges`

                  Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                  maxItems: 200, minItems: 1

                  - `class BrowserStateChangeTabOpened:`

                    A tab this call's execution opened that remains open at its end —
                    the creation delta of the `tabs` inventory, not an event log.

                    Carries only the `tab_id`; the tab's `title` and `url` live on its
                    `tabs` entry, which must include the same `tab_id`. A tab opened
                    during a failed call gets no deferred `tab_opened`; it simply appears
                    in the next result's `tabs` inventory.

                    - `String tabId`

                      The `tab_id` of the opened tab, present in `tabs`.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "tab_opened"`

                  - `class BrowserStateChangeDownloadStarted:`

                    A file download that started during this call.

                    - `String downloadId`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "download_started"`

                    - `String url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `class BrowserStateChangeDownloadCompleted:`

                    A file download that finished during this call, reported with the
                    same `download_id` as its `download_started` — or without a prior
                    `download_started`, when the download finished during the call that
                    started it (at most one state change per `download_id` per result).

                    - `String downloadId`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "download_completed"`

                    - `String url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `Optional<String> path`

                      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                    - `Optional<Long> sizeBytes`

                      The completed download's size.

                      minimum: 0

                  - `class BrowserStateChangeDownloadFailed:`

                    A file download that failed — or was cancelled — during this call.

                    - `String downloadId`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonValue type = "download_failed"`

                    - `String url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `Optional<String> error`

                      The failure or cancellation detail, when known.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

          - `Optional<Boolean> isError`

          - `Optional<String> toolsetName`

            For a toolset member tool_result, the toolset family of the paired tool_use.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ServerToolUseBlockParam:`

          - `String id`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue type = "server_tool_use"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class WebSearchToolResultBlockParam:`

          - `WebSearchToolResultBlockParamContent content`

            - `List<WebSearchResultBlockParam>`

              - `String encryptedContent`

              - `String title`

              - `JsonValue type = "web_search_result"`

              - `String url`

              - `Optional<String> pageAge`

            - `class WebSearchToolRequestError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue type = "web_search_tool_result_error"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "web_search_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class WebFetchToolResultBlockParam:`

          - `Content content`

            - `class WebFetchToolResultErrorBlockParam:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue type = "web_fetch_tool_result_error"`

            - `class WebFetchBlockParam:`

              - `DocumentBlockParam content`

              - `JsonValue type = "web_fetch_result"`

              - `String url`

                Fetched content URL

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "web_fetch_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class CodeExecutionToolResultBlockParam:`

          - `CodeExecutionToolResultBlockParamContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultErrorParam:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue type = "code_execution_tool_result_error"`

            - `class CodeExecutionResultBlockParam:`

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue type = "code_execution_output"`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type = "code_execution_result"`

            - `class EncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue type = "code_execution_output"`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue type = "encrypted_code_execution_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class BashCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class BashCodeExecutionToolResultErrorParam:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue type = "bash_code_execution_tool_result_error"`

            - `class BashCodeExecutionResultBlockParam:`

              - `List<BashCodeExecutionOutputBlockParam> content`

                - `String fileId`

                - `JsonValue type = "bash_code_execution_output"`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type = "bash_code_execution_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "bash_code_execution_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class TextEditorCodeExecutionToolResultBlockParam:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultErrorParam:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `JsonValue type = "text_editor_code_execution_tool_result_error"`

              - `Optional<String> errorMessage`

            - `class TextEditorCodeExecutionViewResultBlockParam:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `JsonValue type = "text_editor_code_execution_view_result"`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

            - `class TextEditorCodeExecutionCreateResultBlockParam:`

              - `boolean isFileUpdate`

              - `JsonValue type = "text_editor_code_execution_create_result"`

            - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonValue type = "text_editor_code_execution_str_replace_result"`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "text_editor_code_execution_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class ToolSearchToolResultBlockParam:`

          - `Content content`

            - `class ToolSearchToolResultErrorParam:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue type = "tool_search_tool_result_error"`

              - `Optional<String> errorMessage`

            - `class ToolSearchToolSearchResultBlockParam:`

              - `List<ToolReferenceBlockParam> toolReferences`

                - `String toolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonValue type = "tool_reference"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

              - `JsonValue type = "tool_search_tool_search_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "tool_search_tool_result"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class ContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `String fileId`

          - `JsonValue type = "container_upload"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

    - `Role role`

      - `USER("user")`

      - `ASSISTANT("assistant")`

      - `SYSTEM("system")`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Optional<CacheControlEphemeral> cacheControl`

    Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Optional<OutputConfig> outputConfig`

    Configuration options for the model's output, such as the output format.

  - `Optional<System> system`

    System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `String`

    - `List<TextBlockParam>`

      - `String text`

        minLength: 1

      - `JsonValue type = "text"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<List<TextCitationParam>> citations`

  - `Optional<ThinkingConfigParam> thinking`

    Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `Optional<ToolChoice> toolChoice`

    How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `Optional<List<MessageCountTokensTool>> tools`

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

    - `class Tool:`

      - `InputSchema inputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonValue type = "object"`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<String> description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `Optional<Boolean> eagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Type> type`

    - `class ToolBash20250124:`

      - `JsonValue name = "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "bash_20250124"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250522:`

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20250522"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250825:`

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20250825"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20260120"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260521:`

      Code execution tool with REPL state persistence.

      - `JsonValue name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "code_execution_20260521"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BrowserToolset20260801:`

      The browser toolset: a single `tools[]` entry (carrying no
      `name`) that declares the browser tool family. The model is served
      the family's tool with any members disabled via `configs` removed
      from its schema.

      - `JsonValue type = "browser_toolset_20260801"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<BrowserToolsetConfigs> configs`

        Per-member configuration for `browser_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `Optional<BrowserCloseTabConfig> closeTab`

          `close_tab`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserDoubleClickConfig> doubleClick`

          `double_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserFileUploadConfig> fileUpload`

          `file_upload`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserFindConfig> find`

          `find`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserFormInputConfig> formInput`

          `form_input`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserGetPageTextConfig> getPageText`

          `get_page_text`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserHoldKeyConfig> holdKey`

          `hold_key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserHoverConfig> hover`

          `hover`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserJavascriptExecConfig> javascriptExec`

          `javascript_exec`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserKeyConfig> key`

          `key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftClickConfig> leftClick`

          `left_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

          `left_click_drag`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

          `left_mouse_down`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

          `left_mouse_up`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserListTabsConfig> listTabs`

          `list_tabs`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserMiddleClickConfig> middleClick`

          `middle_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserMouseMoveConfig> mouseMove`

          `mouse_move`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserNavigateConfig> navigate`

          `navigate`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserNewTabConfig> newTab`

          `new_tab`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserReadConsoleConfig> readConsole`

          `read_console`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserReadNetworkConfig> readNetwork`

          `read_network`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserReadPageConfig> readPage`

          `read_page`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserRightClickConfig> rightClick`

          `right_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserScreenshotConfig> screenshot`

          `screenshot`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserScrollConfig> scroll`

          `scroll`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserScrollToConfig> scrollTo`

          `scroll_to`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserSwitchTabConfig> switchTab`

          `switch_tab`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserTripleClickConfig> tripleClick`

          `triple_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserTypeConfig> type`

          `type`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserWaitConfig> wait`

          `wait`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<BrowserZoomConfig> zoom`

          `zoom`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class MemoryTool20250818:`

      - `JsonValue name = "memory"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "memory_20250818"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ComputerToolset20260801:`

      The computer toolset: a single `tools[]` entry (carrying no
      `name`) that declares the computer tool family. The model is
      served the family's tool with any members disabled via `configs`
      removed from its schema. Every member is enabled by default, zoom
      included. The single-tool options `display_number` and
      `enable_zoom` are not fields of a toolset entry — it carries only
      `type`, `configs`, and `cache_control`; zoom is controlled
      via `configs.zoom.enabled`.

      - `JsonValue type = "computer_toolset_20260801"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<ComputerToolsetConfigs> configs`

        Per-member configuration for `computer_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `Optional<ComputerCursorPositionConfig> cursorPosition`

          `cursor_position`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerDoubleClickConfig> doubleClick`

          `double_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerHoldKeyConfig> holdKey`

          `hold_key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerKeyConfig> key`

          `key`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftClickConfig> leftClick`

          `left_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

          `left_click_drag`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

          `left_mouse_down`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

          `left_mouse_up`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerMiddleClickConfig> middleClick`

          `middle_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerMouseMoveConfig> mouseMove`

          `mouse_move`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerRightClickConfig> rightClick`

          `right_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerScreenshotConfig> screenshot`

          `screenshot`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerScrollConfig> scroll`

          `scroll`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerTripleClickConfig> tripleClick`

          `triple_click`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerTypeConfig> type`

          `type`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerWaitConfig> wait`

          `wait`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Optional<ComputerZoomConfig> zoom`

          `zoom`'s config overrides.

          - `Optional<Boolean> deferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Optional<Boolean> enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class ToolTextEditor20250124:`

      - `JsonValue name = "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "text_editor_20250124"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250429:`

      - `JsonValue name = "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "text_editor_20250429"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250728:`

      - `JsonValue name = "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "text_editor_20250728"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<List<InputExample>> inputExamples`

      - `Optional<Long> maxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        minimum: 1

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20250305:`

      - `JsonValue name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_search_20250305"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonValue type = "approximate"`

        - `Optional<String> city`

          The city of the user.

          maxLength: 255, minLength: 1

        - `Optional<String> country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          maxLength: 2, minLength: 2

        - `Optional<String> region`

          The region of the user.

          maxLength: 255, minLength: 1

        - `Optional<String> timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

          maxLength: 255, minLength: 1

    - `class WebFetchTool20250910:`

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20250910"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20260209:`

      - `JsonValue name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_search_20260209"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class WebFetchTool20260209:`

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20260209"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebFetchTool20260309:`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20260309"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Boolean> useCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class WebSearchTool20260318:`

      - `JsonValue name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_search_20260318"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `Optional<List<String>> blockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<ResponseInclusion> responseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `FULL("full")`

        - `EXCLUDED("excluded")`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<UserLocation> userLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class WebFetchTool20260318:`

      - `JsonValue name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonValue type = "web_fetch_20260318"`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<List<String>> allowedDomains`

        List of domains to allow fetching from

      - `Optional<List<String>> blockedDomains`

        List of domains to block fetching from

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<CitationsConfigParam> citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Long> maxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `Optional<Long> maxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Optional<ResponseInclusion> responseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `FULL("full")`

        - `EXCLUDED("excluded")`

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

      - `Optional<Boolean> useCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class ToolSearchToolBm25_20251119:`

      - `JsonValue name = "tool_search_tool_bm25"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type type`

        - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolRegex20251119:`

      - `JsonValue name = "tool_search_tool_regex"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type type`

        - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `Optional<List<AllowedCaller>> allowedCallers`

        - `DIRECT("direct")`

        - `CODE_EXECUTION_20250825("code_execution_20250825")`

        - `CODE_EXECUTION_20260120("code_execution_20260120")`

        - `CODE_EXECUTION_20260521("code_execution_20260521")`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<Boolean> deferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Optional<Boolean> strict`

        When true, guarantees schema validation on tool names and inputs

### Returns

- `class MessageTokensCount:`

  - `long inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.MessageCountTokensParams;
import com.anthropic.models.messages.MessageTokensCount;
import com.anthropic.models.messages.Model;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageCountTokensParams params = MessageCountTokensParams.builder()
            .addUserMessage("Hello, world")
            .model(Model.CLAUDE_OPUS_5)
            .build();
        MessageTokensCount messageTokensCount = client.messages().countTokens(params);
    }
}
```

#### Response (200)

```json
{
  "input_tokens": 2095
}
```

## Domain types

### Base64 Image Source

- `class Base64ImageSource:`

  - `String data`

    format: byte

  - `MediaType mediaType`

    - `IMAGE_JPEG("image/jpeg")`

    - `IMAGE_PNG("image/png")`

    - `IMAGE_GIF("image/gif")`

    - `IMAGE_WEBP("image/webp")`

  - `JsonValue type = "base64"`

### Base64 PDF Source

- `class Base64PdfSource:`

  - `String data`

    format: byte

  - `JsonValue mediaType = "application/pdf"`

  - `JsonValue type = "base64"`

### Bash Code Execution Output Block

- `class BashCodeExecutionOutputBlock:`

  - `String fileId`

  - `JsonValue type = "bash_code_execution_output"`

### Bash Code Execution Output Block Param

- `class BashCodeExecutionOutputBlockParam:`

  - `String fileId`

  - `JsonValue type = "bash_code_execution_output"`

### Bash Code Execution Result Block

- `class BashCodeExecutionResultBlock:`

  - `List<BashCodeExecutionOutputBlock> content`

    - `String fileId`

    - `JsonValue type = "bash_code_execution_output"`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue type = "bash_code_execution_result"`

### Bash Code Execution Result Block Param

- `class BashCodeExecutionResultBlockParam:`

  - `List<BashCodeExecutionOutputBlockParam> content`

    - `String fileId`

    - `JsonValue type = "bash_code_execution_output"`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue type = "bash_code_execution_result"`

### Bash Code Execution Tool Result Block

- `class BashCodeExecutionToolResultBlock:`

  - `Content content`

    - `class BashCodeExecutionToolResultError:`

      - `BashCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

      - `JsonValue type = "bash_code_execution_tool_result_error"`

    - `class BashCodeExecutionResultBlock:`

      - `List<BashCodeExecutionOutputBlock> content`

        - `String fileId`

        - `JsonValue type = "bash_code_execution_output"`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue type = "bash_code_execution_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "bash_code_execution_tool_result"`

### Bash Code Execution Tool Result Block Param

- `class BashCodeExecutionToolResultBlockParam:`

  - `Content content`

    - `class BashCodeExecutionToolResultErrorParam:`

      - `BashCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

      - `JsonValue type = "bash_code_execution_tool_result_error"`

    - `class BashCodeExecutionResultBlockParam:`

      - `List<BashCodeExecutionOutputBlockParam> content`

        - `String fileId`

        - `JsonValue type = "bash_code_execution_output"`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue type = "bash_code_execution_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "bash_code_execution_tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Bash Code Execution Tool Result Error

- `class BashCodeExecutionToolResultError:`

  - `BashCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

  - `JsonValue type = "bash_code_execution_tool_result_error"`

### Bash Code Execution Tool Result Error Code

- `enum BashCodeExecutionToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

### Bash Code Execution Tool Result Error Param

- `class BashCodeExecutionToolResultErrorParam:`

  - `BashCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

  - `JsonValue type = "bash_code_execution_tool_result_error"`

### Browser Close Tab Config

- `class BrowserCloseTabConfig:`

  `close_tab`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Double Click Config

- `class BrowserDoubleClickConfig:`

  `double_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser File Upload Config

- `class BrowserFileUploadConfig:`

  `file_upload`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Find Config

- `class BrowserFindConfig:`

  `find`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Form Input Config

- `class BrowserFormInputConfig:`

  `form_input`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Get Page Text Config

- `class BrowserGetPageTextConfig:`

  `get_page_text`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hold Key Config

- `class BrowserHoldKeyConfig:`

  `hold_key`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hover Config

- `class BrowserHoverConfig:`

  `hover`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Javascript Exec Config

- `class BrowserJavascriptExecConfig:`

  `javascript_exec`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Key Config

- `class BrowserKeyConfig:`

  `key`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Config

- `class BrowserLeftClickConfig:`

  `left_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Drag Config

- `class BrowserLeftClickDragConfig:`

  `left_click_drag`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Down Config

- `class BrowserLeftMouseDownConfig:`

  `left_mouse_down`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Up Config

- `class BrowserLeftMouseUpConfig:`

  `left_mouse_up`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser List Tabs Config

- `class BrowserListTabsConfig:`

  `list_tabs`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Middle Click Config

- `class BrowserMiddleClickConfig:`

  `middle_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Mouse Move Config

- `class BrowserMouseMoveConfig:`

  `mouse_move`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Navigate Config

- `class BrowserNavigateConfig:`

  `navigate`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser New Tab Config

- `class BrowserNewTabConfig:`

  `new_tab`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Console Config

- `class BrowserReadConsoleConfig:`

  `read_console`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Network Config

- `class BrowserReadNetworkConfig:`

  `read_network`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Page Config

- `class BrowserReadPageConfig:`

  `read_page`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Right Click Config

- `class BrowserRightClickConfig:`

  `right_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Screenshot Config

- `class BrowserScreenshotConfig:`

  `screenshot`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll Config

- `class BrowserScrollConfig:`

  `scroll`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll To Config

- `class BrowserScrollToConfig:`

  `scroll_to`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser State Block Param

- `class BrowserStateBlockParam:`

  The caller's browser state after a browser toolset member call —
  the full inventory of open tabs, which tab is active, and any side
  effects (tabs opened, download state changes) the call produced.

  At most one per `tool_result`, only on a non-error result answering a
  browser toolset member `tool_use`. The server renders the
  model-visible text from it; the model never sees the raw fields.

  - `List<BrowserStateTabEntry> tabs`

    All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

    maxItems: 100

    - `String tabId`

      The caller-assigned identifier for this tab, unique within the inventory.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `String title`

      The title of the page the tab is showing. May be empty.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `String url`

      The URL of the page the tab is showing. May be empty.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `Optional<Boolean> active`

      Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

  - `JsonValue type = "browser_state"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<List<BrowserStateChange>> stateChanges`

    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

    maxItems: 200, minItems: 1

    - `class BrowserStateChangeTabOpened:`

      A tab this call's execution opened that remains open at its end —
      the creation delta of the `tabs` inventory, not an event log.

      Carries only the `tab_id`; the tab's `title` and `url` live on its
      `tabs` entry, which must include the same `tab_id`. A tab opened
      during a failed call gets no deferred `tab_opened`; it simply appears
      in the next result's `tabs` inventory.

      - `String tabId`

        The `tab_id` of the opened tab, present in `tabs`.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `JsonValue type = "tab_opened"`

    - `class BrowserStateChangeDownloadStarted:`

      A file download that started during this call.

      - `String downloadId`

        The caller-assigned identifier for this download, stable across the state changes reporting it.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `JsonValue type = "download_started"`

      - `String url`

        The final post-redirect URL the download was served from.

        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `class BrowserStateChangeDownloadCompleted:`

      A file download that finished during this call, reported with the
      same `download_id` as its `download_started` — or without a prior
      `download_started`, when the download finished during the call that
      started it (at most one state change per `download_id` per result).

      - `String downloadId`

        The caller-assigned identifier for this download, stable across the state changes reporting it.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `JsonValue type = "download_completed"`

      - `String url`

        The final post-redirect URL the download was served from.

        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `Optional<String> path`

        Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

      - `Optional<Long> sizeBytes`

        The completed download's size.

        minimum: 0

    - `class BrowserStateChangeDownloadFailed:`

      A file download that failed — or was cancelled — during this call.

      - `String downloadId`

        The caller-assigned identifier for this download, stable across the state changes reporting it.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `JsonValue type = "download_failed"`

      - `String url`

        The final post-redirect URL the download was served from.

        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `Optional<String> error`

        The failure or cancellation detail, when known.

        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

### Browser State Change

- `class BrowserStateChange: union`

  A tab this call's execution opened that remains open at its end —
  the creation delta of the `tabs` inventory, not an event log.

  Carries only the `tab_id`; the tab's `title` and `url` live on its
  `tabs` entry, which must include the same `tab_id`. A tab opened
  during a failed call gets no deferred `tab_opened`; it simply appears
  in the next result's `tabs` inventory.

  - `class BrowserStateChangeTabOpened:`

    A tab this call's execution opened that remains open at its end —
    the creation delta of the `tabs` inventory, not an event log.

    Carries only the `tab_id`; the tab's `title` and `url` live on its
    `tabs` entry, which must include the same `tab_id`. A tab opened
    during a failed call gets no deferred `tab_opened`; it simply appears
    in the next result's `tabs` inventory.

    - `String tabId`

      The `tab_id` of the opened tab, present in `tabs`.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `JsonValue type = "tab_opened"`

  - `class BrowserStateChangeDownloadStarted:`

    A file download that started during this call.

    - `String downloadId`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `JsonValue type = "download_started"`

    - `String url`

      The final post-redirect URL the download was served from.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `class BrowserStateChangeDownloadCompleted:`

    A file download that finished during this call, reported with the
    same `download_id` as its `download_started` — or without a prior
    `download_started`, when the download finished during the call that
    started it (at most one state change per `download_id` per result).

    - `String downloadId`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `JsonValue type = "download_completed"`

    - `String url`

      The final post-redirect URL the download was served from.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `Optional<String> path`

      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

    - `Optional<Long> sizeBytes`

      The completed download's size.

      minimum: 0

  - `class BrowserStateChangeDownloadFailed:`

    A file download that failed — or was cancelled — during this call.

    - `String downloadId`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `JsonValue type = "download_failed"`

    - `String url`

      The final post-redirect URL the download was served from.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `Optional<String> error`

      The failure or cancellation detail, when known.

      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

### Browser State Change Download Completed

- `class BrowserStateChangeDownloadCompleted:`

  A file download that finished during this call, reported with the
  same `download_id` as its `download_started` — or without a prior
  `download_started`, when the download finished during the call that
  started it (at most one state change per `download_id` per result).

  - `String downloadId`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `JsonValue type = "download_completed"`

  - `String url`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `Optional<String> path`

    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

  - `Optional<Long> sizeBytes`

    The completed download's size.

    minimum: 0

### Browser State Change Download Failed

- `class BrowserStateChangeDownloadFailed:`

  A file download that failed — or was cancelled — during this call.

  - `String downloadId`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `JsonValue type = "download_failed"`

  - `String url`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `Optional<String> error`

    The failure or cancellation detail, when known.

    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

### Browser State Change Download Started

- `class BrowserStateChangeDownloadStarted:`

  A file download that started during this call.

  - `String downloadId`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `JsonValue type = "download_started"`

  - `String url`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

### Browser State Change Tab Opened

- `class BrowserStateChangeTabOpened:`

  A tab this call's execution opened that remains open at its end —
  the creation delta of the `tabs` inventory, not an event log.

  Carries only the `tab_id`; the tab's `title` and `url` live on its
  `tabs` entry, which must include the same `tab_id`. A tab opened
  during a failed call gets no deferred `tab_opened`; it simply appears
  in the next result's `tabs` inventory.

  - `String tabId`

    The `tab_id` of the opened tab, present in `tabs`.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `JsonValue type = "tab_opened"`

### Browser State Tab Entry

- `class BrowserStateTabEntry:`

  One open browser tab reported in a `browser_state` block's `tabs`
  inventory.

  `tab_id` is the caller-assigned identifier for the tab; `title` and
  `url` describe the page the tab is currently showing and may be empty
  strings (a blank tab legitimately has both empty). `active` marks the
  tab that is active after this call; whenever `tabs` is non-empty,
  exactly one entry is marked.

  - `String tabId`

    The caller-assigned identifier for this tab, unique within the inventory.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `String title`

    The title of the page the tab is showing. May be empty.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `String url`

    The URL of the page the tab is showing. May be empty.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `Optional<Boolean> active`

    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

### Browser Switch Tab Config

- `class BrowserSwitchTabConfig:`

  `switch_tab`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Toolset 20260801

- `class BrowserToolset20260801:`

  The browser toolset: a single `tools[]` entry (carrying no
  `name`) that declares the browser tool family. The model is served
  the family's tool with any members disabled via `configs` removed
  from its schema.

  - `JsonValue type = "browser_toolset_20260801"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<BrowserToolsetConfigs> configs`

    Per-member configuration for `browser_toolset_20260801`: one
    optional field per member tool, keyed by the member name — the same
    name the member's `tool_use` blocks carry. Every member is an
    accepted key, and a member's defaults apply wherever its key is
    absent. Unknown keys are rejected: the field set is this toolset
    version's complete member set.

    - `Optional<BrowserCloseTabConfig> closeTab`

      `close_tab`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserDoubleClickConfig> doubleClick`

      `double_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserFileUploadConfig> fileUpload`

      `file_upload`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserFindConfig> find`

      `find`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserFormInputConfig> formInput`

      `form_input`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserGetPageTextConfig> getPageText`

      `get_page_text`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserHoldKeyConfig> holdKey`

      `hold_key`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserHoverConfig> hover`

      `hover`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserJavascriptExecConfig> javascriptExec`

      `javascript_exec`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserKeyConfig> key`

      `key`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserLeftClickConfig> leftClick`

      `left_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

      `left_click_drag`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

      `left_mouse_down`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

      `left_mouse_up`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserListTabsConfig> listTabs`

      `list_tabs`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserMiddleClickConfig> middleClick`

      `middle_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserMouseMoveConfig> mouseMove`

      `mouse_move`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserNavigateConfig> navigate`

      `navigate`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserNewTabConfig> newTab`

      `new_tab`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserReadConsoleConfig> readConsole`

      `read_console`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserReadNetworkConfig> readNetwork`

      `read_network`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserReadPageConfig> readPage`

      `read_page`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserRightClickConfig> rightClick`

      `right_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserScreenshotConfig> screenshot`

      `screenshot`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserScrollConfig> scroll`

      `scroll`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserScrollToConfig> scrollTo`

      `scroll_to`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserSwitchTabConfig> switchTab`

      `switch_tab`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserTripleClickConfig> tripleClick`

      `triple_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserTypeConfig> type`

      `type`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserWaitConfig> wait`

      `wait`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<BrowserZoomConfig> zoom`

      `zoom`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Toolset Configs

- `class BrowserToolsetConfigs:`

  Per-member configuration for `browser_toolset_20260801`: one
  optional field per member tool, keyed by the member name — the same
  name the member's `tool_use` blocks carry. Every member is an
  accepted key, and a member's defaults apply wherever its key is
  absent. Unknown keys are rejected: the field set is this toolset
  version's complete member set.

  - `Optional<BrowserCloseTabConfig> closeTab`

    `close_tab`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserDoubleClickConfig> doubleClick`

    `double_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserFileUploadConfig> fileUpload`

    `file_upload`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserFindConfig> find`

    `find`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserFormInputConfig> formInput`

    `form_input`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserGetPageTextConfig> getPageText`

    `get_page_text`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserHoldKeyConfig> holdKey`

    `hold_key`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserHoverConfig> hover`

    `hover`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserJavascriptExecConfig> javascriptExec`

    `javascript_exec`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserKeyConfig> key`

    `key`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserLeftClickConfig> leftClick`

    `left_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

    `left_click_drag`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

    `left_mouse_down`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

    `left_mouse_up`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserListTabsConfig> listTabs`

    `list_tabs`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserMiddleClickConfig> middleClick`

    `middle_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserMouseMoveConfig> mouseMove`

    `mouse_move`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserNavigateConfig> navigate`

    `navigate`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserNewTabConfig> newTab`

    `new_tab`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserReadConsoleConfig> readConsole`

    `read_console`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserReadNetworkConfig> readNetwork`

    `read_network`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserReadPageConfig> readPage`

    `read_page`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserRightClickConfig> rightClick`

    `right_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserScreenshotConfig> screenshot`

    `screenshot`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserScrollConfig> scroll`

    `scroll`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserScrollToConfig> scrollTo`

    `scroll_to`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserSwitchTabConfig> switchTab`

    `switch_tab`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserTripleClickConfig> tripleClick`

    `triple_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserTypeConfig> type`

    `type`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserWaitConfig> wait`

    `wait`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<BrowserZoomConfig> zoom`

    `zoom`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Triple Click Config

- `class BrowserTripleClickConfig:`

  `triple_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Type Config

- `class BrowserTypeConfig:`

  `type`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Wait Config

- `class BrowserWaitConfig:`

  `wait`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Zoom Config

- `class BrowserZoomConfig:`

  `zoom`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Cache Control Ephemeral

- `class CacheControlEphemeral:`

  - `JsonValue type = "ephemeral"`

  - `Optional<Ttl> ttl`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `TTL_5M("5m")`

    - `TTL_1H("1h")`

### Cache Creation

- `class CacheCreation:`

  - `long ephemeral1hInputTokens`

    The number of input tokens used to create the 1 hour cache entry.

    minimum: 0

  - `long ephemeral5mInputTokens`

    The number of input tokens used to create the 5 minute cache entry.

    minimum: 0

### Citation Char Location

- `class CitationCharLocation:`

  - `String citedText`

  - `long documentIndex`

    minimum: 0

  - `Optional<String> documentTitle`

  - `long endCharIndex`

  - `Optional<String> fileId`

  - `long startCharIndex`

    minimum: 0

  - `JsonValue type = "char_location"`

### Citation Char Location Param

- `class CitationCharLocationParam:`

  - `String citedText`

  - `long documentIndex`

    minimum: 0

  - `Optional<String> documentTitle`

    maxLength: 500, minLength: 1

  - `long endCharIndex`

  - `long startCharIndex`

    minimum: 0

  - `JsonValue type = "char_location"`

### Citation Content Block Location

- `class CitationContentBlockLocation:`

  - `String citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `long documentIndex`

    minimum: 0

  - `Optional<String> documentTitle`

  - `long endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `Optional<String> fileId`

  - `long startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

    minimum: 0

  - `JsonValue type = "content_block_location"`

### Citation Content Block Location Param

- `class CitationContentBlockLocationParam:`

  - `String citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `long documentIndex`

    minimum: 0

  - `Optional<String> documentTitle`

    maxLength: 500, minLength: 1

  - `long endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `long startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

    minimum: 0

  - `JsonValue type = "content_block_location"`

### Citation Page Location

- `class CitationPageLocation:`

  - `String citedText`

  - `long documentIndex`

    minimum: 0

  - `Optional<String> documentTitle`

  - `long endPageNumber`

  - `Optional<String> fileId`

  - `long startPageNumber`

    minimum: 1

  - `JsonValue type = "page_location"`

### Citation Page Location Param

- `class CitationPageLocationParam:`

  - `String citedText`

  - `long documentIndex`

    minimum: 0

  - `Optional<String> documentTitle`

    maxLength: 500, minLength: 1

  - `long endPageNumber`

  - `long startPageNumber`

    minimum: 1

  - `JsonValue type = "page_location"`

### Citation Search Result Location Param

- `class CitationSearchResultLocationParam:`

  - `String citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `long endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `long searchResultIndex`

    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

    Counted separately from `document_index`; server-side web search results are not included in this count.

    minimum: 0

  - `String source`

  - `long startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

    minimum: 0

  - `Optional<String> title`

  - `JsonValue type = "search_result_location"`

### Citation Web Search Result Location Param

- `class CitationWebSearchResultLocationParam:`

  - `String citedText`

  - `String encryptedIndex`

  - `Optional<String> title`

    maxLength: 512, minLength: 1

  - `JsonValue type = "web_search_result_location"`

  - `String url`

    minLength: 1

### Citations Config

- `class CitationsConfig:`

  - `boolean enabled`

### Citations Config Param

- `class CitationsConfigParam:`

  - `Optional<Boolean> enabled`

### Citations Delta

- `class CitationsDelta:`

  - `Citation citation`

    - `class CitationCharLocation:`

      - `String citedText`

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

      - `long endCharIndex`

      - `Optional<String> fileId`

      - `long startCharIndex`

        minimum: 0

      - `JsonValue type = "char_location"`

    - `class CitationPageLocation:`

      - `String citedText`

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

      - `long endPageNumber`

      - `Optional<String> fileId`

      - `long startPageNumber`

        minimum: 1

      - `JsonValue type = "page_location"`

    - `class CitationContentBlockLocation:`

      - `String citedText`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

      - `long endBlockIndex`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `Optional<String> fileId`

      - `long startBlockIndex`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `JsonValue type = "content_block_location"`

    - `class CitationsWebSearchResultLocation:`

      - `String citedText`

      - `String encryptedIndex`

      - `Optional<String> title`

        maxLength: 512

      - `JsonValue type = "web_search_result_location"`

      - `String url`

    - `class CitationsSearchResultLocation:`

      - `String citedText`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `long endBlockIndex`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `long searchResultIndex`

        0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

        Counted separately from `document_index`; server-side web search results are not included in this count.

        minimum: 0

      - `String source`

      - `long startBlockIndex`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `Optional<String> title`

      - `JsonValue type = "search_result_location"`

  - `JsonValue type = "citations_delta"`

### Citations Search Result Location

- `class CitationsSearchResultLocation:`

  - `String citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `long endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `long searchResultIndex`

    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

    Counted separately from `document_index`; server-side web search results are not included in this count.

    minimum: 0

  - `String source`

  - `long startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

    minimum: 0

  - `Optional<String> title`

  - `JsonValue type = "search_result_location"`

### Citations Web Search Result Location

- `class CitationsWebSearchResultLocation:`

  - `String citedText`

  - `String encryptedIndex`

  - `Optional<String> title`

    maxLength: 512

  - `JsonValue type = "web_search_result_location"`

  - `String url`

### Code Execution Output Block

- `class CodeExecutionOutputBlock:`

  - `String fileId`

  - `JsonValue type = "code_execution_output"`

### Code Execution Output Block Param

- `class CodeExecutionOutputBlockParam:`

  - `String fileId`

  - `JsonValue type = "code_execution_output"`

### Code Execution Result Block

- `class CodeExecutionResultBlock:`

  - `List<CodeExecutionOutputBlock> content`

    - `String fileId`

    - `JsonValue type = "code_execution_output"`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue type = "code_execution_result"`

### Code Execution Result Block Param

- `class CodeExecutionResultBlockParam:`

  - `List<CodeExecutionOutputBlockParam> content`

    - `String fileId`

    - `JsonValue type = "code_execution_output"`

  - `long returnCode`

  - `String stderr`

  - `String stdout`

  - `JsonValue type = "code_execution_result"`

### Code Execution Tool 20250522

- `class CodeExecutionTool20250522:`

  - `JsonValue name = "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "code_execution_20250522"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

- `class CodeExecutionTool20250825:`

  - `JsonValue name = "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "code_execution_20250825"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

- `class CodeExecutionTool20260120:`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `JsonValue name = "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "code_execution_20260120"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260521

- `class CodeExecutionTool20260521:`

  Code execution tool with REPL state persistence.

  - `JsonValue name = "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "code_execution_20260521"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

- `class CodeExecutionToolResultBlock:`

  - `CodeExecutionToolResultBlockContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `class CodeExecutionToolResultError:`

      - `CodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `JsonValue type = "code_execution_tool_result_error"`

    - `class CodeExecutionResultBlock:`

      - `List<CodeExecutionOutputBlock> content`

        - `String fileId`

        - `JsonValue type = "code_execution_output"`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue type = "code_execution_result"`

    - `class EncryptedCodeExecutionResultBlock:`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `List<CodeExecutionOutputBlock> content`

        - `String fileId`

        - `JsonValue type = "code_execution_output"`

      - `String encryptedStdout`

      - `long returnCode`

      - `String stderr`

      - `JsonValue type = "encrypted_code_execution_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "code_execution_tool_result"`

### Code Execution Tool Result Block Content

- `class CodeExecutionToolResultBlockContent: union`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `class CodeExecutionToolResultError:`

    - `CodeExecutionToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `JsonValue type = "code_execution_tool_result_error"`

  - `class CodeExecutionResultBlock:`

    - `List<CodeExecutionOutputBlock> content`

      - `String fileId`

      - `JsonValue type = "code_execution_output"`

    - `long returnCode`

    - `String stderr`

    - `String stdout`

    - `JsonValue type = "code_execution_result"`

  - `class EncryptedCodeExecutionResultBlock:`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `List<CodeExecutionOutputBlock> content`

      - `String fileId`

      - `JsonValue type = "code_execution_output"`

    - `String encryptedStdout`

    - `long returnCode`

    - `String stderr`

    - `JsonValue type = "encrypted_code_execution_result"`

### Code Execution Tool Result Block Param

- `class CodeExecutionToolResultBlockParam:`

  - `CodeExecutionToolResultBlockParamContent content`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `class CodeExecutionToolResultErrorParam:`

      - `CodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `JsonValue type = "code_execution_tool_result_error"`

    - `class CodeExecutionResultBlockParam:`

      - `List<CodeExecutionOutputBlockParam> content`

        - `String fileId`

        - `JsonValue type = "code_execution_output"`

      - `long returnCode`

      - `String stderr`

      - `String stdout`

      - `JsonValue type = "code_execution_result"`

    - `class EncryptedCodeExecutionResultBlockParam:`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `List<CodeExecutionOutputBlockParam> content`

        - `String fileId`

        - `JsonValue type = "code_execution_output"`

      - `String encryptedStdout`

      - `long returnCode`

      - `String stderr`

      - `JsonValue type = "encrypted_code_execution_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "code_execution_tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Code Execution Tool Result Block Param Content

- `class CodeExecutionToolResultBlockParamContent: union`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `class CodeExecutionToolResultErrorParam:`

    - `CodeExecutionToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `JsonValue type = "code_execution_tool_result_error"`

  - `class CodeExecutionResultBlockParam:`

    - `List<CodeExecutionOutputBlockParam> content`

      - `String fileId`

      - `JsonValue type = "code_execution_output"`

    - `long returnCode`

    - `String stderr`

    - `String stdout`

    - `JsonValue type = "code_execution_result"`

  - `class EncryptedCodeExecutionResultBlockParam:`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `List<CodeExecutionOutputBlockParam> content`

      - `String fileId`

      - `JsonValue type = "code_execution_output"`

    - `String encryptedStdout`

    - `long returnCode`

    - `String stderr`

    - `JsonValue type = "encrypted_code_execution_result"`

### Code Execution Tool Result Error

- `class CodeExecutionToolResultError:`

  - `CodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `JsonValue type = "code_execution_tool_result_error"`

### Code Execution Tool Result Error Code

- `enum CodeExecutionToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

### Code Execution Tool Result Error Param

- `class CodeExecutionToolResultErrorParam:`

  - `CodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `JsonValue type = "code_execution_tool_result_error"`

### Computer Cursor Position Config

- `class ComputerCursorPositionConfig:`

  `cursor_position`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Double Click Config

- `class ComputerDoubleClickConfig:`

  `double_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Hold Key Config

- `class ComputerHoldKeyConfig:`

  `hold_key`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Key Config

- `class ComputerKeyConfig:`

  `key`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Config

- `class ComputerLeftClickConfig:`

  `left_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Drag Config

- `class ComputerLeftClickDragConfig:`

  `left_click_drag`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Down Config

- `class ComputerLeftMouseDownConfig:`

  `left_mouse_down`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Up Config

- `class ComputerLeftMouseUpConfig:`

  `left_mouse_up`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Middle Click Config

- `class ComputerMiddleClickConfig:`

  `middle_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Mouse Move Config

- `class ComputerMouseMoveConfig:`

  `mouse_move`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Right Click Config

- `class ComputerRightClickConfig:`

  `right_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Screenshot Config

- `class ComputerScreenshotConfig:`

  `screenshot`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Scroll Config

- `class ComputerScrollConfig:`

  `scroll`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Toolset 20260801

- `class ComputerToolset20260801:`

  The computer toolset: a single `tools[]` entry (carrying no
  `name`) that declares the computer tool family. The model is
  served the family's tool with any members disabled via `configs`
  removed from its schema. Every member is enabled by default, zoom
  included. The single-tool options `display_number` and
  `enable_zoom` are not fields of a toolset entry — it carries only
  `type`, `configs`, and `cache_control`; zoom is controlled
  via `configs.zoom.enabled`.

  - `JsonValue type = "computer_toolset_20260801"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<ComputerToolsetConfigs> configs`

    Per-member configuration for `computer_toolset_20260801`: one
    optional field per member tool, keyed by the member name — the same
    name the member's `tool_use` blocks carry. Every member is an
    accepted key, and a member's defaults apply wherever its key is
    absent. Unknown keys are rejected: the field set is this toolset
    version's complete member set.

    - `Optional<ComputerCursorPositionConfig> cursorPosition`

      `cursor_position`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerDoubleClickConfig> doubleClick`

      `double_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerHoldKeyConfig> holdKey`

      `hold_key`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerKeyConfig> key`

      `key`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerLeftClickConfig> leftClick`

      `left_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

      `left_click_drag`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

      `left_mouse_down`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

      `left_mouse_up`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerMiddleClickConfig> middleClick`

      `middle_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerMouseMoveConfig> mouseMove`

      `mouse_move`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerRightClickConfig> rightClick`

      `right_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerScreenshotConfig> screenshot`

      `screenshot`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerScrollConfig> scroll`

      `scroll`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerTripleClickConfig> tripleClick`

      `triple_click`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerTypeConfig> type`

      `type`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerWaitConfig> wait`

      `wait`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `Optional<ComputerZoomConfig> zoom`

      `zoom`'s config overrides.

      - `Optional<Boolean> deferLoading`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `Optional<Boolean> enabled`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Toolset Configs

- `class ComputerToolsetConfigs:`

  Per-member configuration for `computer_toolset_20260801`: one
  optional field per member tool, keyed by the member name — the same
  name the member's `tool_use` blocks carry. Every member is an
  accepted key, and a member's defaults apply wherever its key is
  absent. Unknown keys are rejected: the field set is this toolset
  version's complete member set.

  - `Optional<ComputerCursorPositionConfig> cursorPosition`

    `cursor_position`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerDoubleClickConfig> doubleClick`

    `double_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerHoldKeyConfig> holdKey`

    `hold_key`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerKeyConfig> key`

    `key`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerLeftClickConfig> leftClick`

    `left_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

    `left_click_drag`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

    `left_mouse_down`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

    `left_mouse_up`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerMiddleClickConfig> middleClick`

    `middle_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerMouseMoveConfig> mouseMove`

    `mouse_move`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerRightClickConfig> rightClick`

    `right_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerScreenshotConfig> screenshot`

    `screenshot`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerScrollConfig> scroll`

    `scroll`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerTripleClickConfig> tripleClick`

    `triple_click`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerTypeConfig> type`

    `type`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerWaitConfig> wait`

    `wait`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `Optional<ComputerZoomConfig> zoom`

    `zoom`'s config overrides.

    - `Optional<Boolean> deferLoading`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `Optional<Boolean> enabled`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Triple Click Config

- `class ComputerTripleClickConfig:`

  `triple_click`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Type Config

- `class ComputerTypeConfig:`

  `type`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Wait Config

- `class ComputerWaitConfig:`

  `wait`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Zoom Config

- `class ComputerZoomConfig:`

  `zoom`'s config overrides.

  - `Optional<Boolean> deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `Optional<Boolean> enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Container

- `class Container:`

  Information about the container used in the request (for the code execution tool)

  - `String id`

    Identifier for the container used in this request

  - `LocalDateTime expiresAt`

    The time at which the container will expire.

    format: date-time

  - `Optional<List<ContainerSkill>> skills`

    Skills loaded in the container

    - `String skillId`

      Skill ID

      maxLength: 64, minLength: 1

    - `Type type`

      Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

      - `ANTHROPIC("anthropic")`

      - `CUSTOM("custom")`

    - `String version`

      The resolved version: a skill version ID for custom skills.

      maxLength: 64, minLength: 1

### Container Params

- `class ContainerParams:`

  Container parameters with skills to be loaded.

  - `Optional<String> id`

    Container id

  - `Optional<List<SkillParams>> skills`

    List of skills to load in the container

    maxItems: 20

    - `String skillId`

      Skill ID

      maxLength: 64, minLength: 1

    - `Type type`

      Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

      - `ANTHROPIC("anthropic")`

      - `CUSTOM("custom")`

    - `Optional<String> version`

      Skill version or 'latest' for most recent version

      maxLength: 64, minLength: 1

### Container Skill

- `class ContainerSkill:`

  A skill that was loaded in a container (response model).

  - `String skillId`

    Skill ID

    maxLength: 64, minLength: 1

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

    - `ANTHROPIC("anthropic")`

    - `CUSTOM("custom")`

  - `String version`

    The resolved version: a skill version ID for custom skills.

    maxLength: 64, minLength: 1

### Container Upload Block

- `class ContainerUploadBlock:`

  Response model for a file uploaded to the container.

  - `String fileId`

  - `JsonValue type = "container_upload"`

### Container Upload Block Param

- `class ContainerUploadBlockParam:`

  A content block that represents a file to be uploaded to the container
  Files uploaded via this block will be available in the container's input directory.

  - `String fileId`

  - `JsonValue type = "container_upload"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Content Block

- `class ContentBlock: union`

  Response model for a file uploaded to the container.

  - `class TextBlock:`

    - `Optional<List<TextCitation>> citations`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

      - `class CitationCharLocation:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `Optional<String> fileId`

        - `long startCharIndex`

          minimum: 0

        - `JsonValue type = "char_location"`

      - `class CitationPageLocation:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `Optional<String> fileId`

        - `long startPageNumber`

          minimum: 1

        - `JsonValue type = "page_location"`

      - `class CitationContentBlockLocation:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `Optional<String> fileId`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `JsonValue type = "content_block_location"`

      - `class CitationsWebSearchResultLocation:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

          maxLength: 512

        - `JsonValue type = "web_search_result_location"`

        - `String url`

      - `class CitationsSearchResultLocation:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long searchResultIndex`

          0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

          Counted separately from `document_index`; server-side web search results are not included in this count.

          minimum: 0

        - `String source`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `Optional<String> title`

        - `JsonValue type = "search_result_location"`

    - `String text`

      maxLength: 5000000, minLength: 0

    - `JsonValue type = "text"`

  - `class ThinkingBlock:`

    - `String signature`

      A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

      This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `String thinking`

      The text of Claude's thinking process for this block.

    - `JsonValue type = "thinking"`

  - `class RedactedThinkingBlock:`

    - `String data`

      The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

      Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

    - `JsonValue type = "redacted_thinking"`

  - `class ToolUseBlock:`

    - `String id`

      pattern: ^[a-zA-Z0-9_-]+$

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue type = "direct"`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "code_execution_20250825"`

      - `class ServerToolCaller20260120:`

        - `String toolId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "code_execution_20260120"`

    - `Input input`

    - `String name`

      minLength: 1

    - `JsonValue type = "tool_use"`

    - `Optional<String> toolsetName`

      For a toolset member tool_use, the toolset family.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

  - `class ServerToolUseBlock:`

    - `String id`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120:`

    - `Input input`

    - `Name name`

      - `WEB_SEARCH("web_search")`

      - `WEB_FETCH("web_fetch")`

      - `CODE_EXECUTION("code_execution")`

      - `BASH_CODE_EXECUTION("bash_code_execution")`

      - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `JsonValue type = "server_tool_use"`

  - `class WebSearchToolResultBlock:`

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120:`

    - `WebSearchToolResultBlockContent content`

      - `class WebSearchToolResultError:`

        - `WebSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `QUERY_TOO_LONG("query_too_long")`

          - `REQUEST_TOO_LARGE("request_too_large")`

        - `JsonValue type = "web_search_tool_result_error"`

      - `List<WebSearchResultBlock>`

        - `String encryptedContent`

        - `Optional<String> pageAge`

        - `String title`

        - `JsonValue type = "web_search_result"`

        - `String url`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "web_search_tool_result"`

  - `class WebFetchToolResultBlock:`

    - `Caller caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120:`

    - `Content content`

      - `class WebFetchToolResultErrorBlock:`

        - `WebFetchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `URL_TOO_LONG("url_too_long")`

          - `URL_NOT_ALLOWED("url_not_allowed")`

          - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

          - `URL_NOT_ACCESSIBLE("url_not_accessible")`

          - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `UNAVAILABLE("unavailable")`

        - `JsonValue type = "web_fetch_tool_result_error"`

      - `class WebFetchBlock:`

        - `DocumentBlock content`

          - `Optional<CitationsConfig> citations`

            Citation configuration for the document

            - `boolean enabled`

          - `Source source`

            - `class Base64PdfSource:`

              - `String data`

                format: byte

              - `JsonValue mediaType = "application/pdf"`

              - `JsonValue type = "base64"`

            - `class PlainTextSource:`

              - `String data`

              - `JsonValue mediaType = "text/plain"`

              - `JsonValue type = "text"`

          - `Optional<String> title`

            The title of the document

          - `JsonValue type = "document"`

        - `Optional<String> retrievedAt`

          ISO 8601 timestamp when the content was retrieved

        - `JsonValue type = "web_fetch_result"`

        - `String url`

          Fetched content URL

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "web_fetch_tool_result"`

  - `class CodeExecutionToolResultBlock:`

    - `CodeExecutionToolResultBlockContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `class CodeExecutionToolResultError:`

        - `CodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `JsonValue type = "code_execution_tool_result_error"`

      - `class CodeExecutionResultBlock:`

        - `List<CodeExecutionOutputBlock> content`

          - `String fileId`

          - `JsonValue type = "code_execution_output"`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue type = "code_execution_result"`

      - `class EncryptedCodeExecutionResultBlock:`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `List<CodeExecutionOutputBlock> content`

          - `String fileId`

          - `JsonValue type = "code_execution_output"`

        - `String encryptedStdout`

        - `long returnCode`

        - `String stderr`

        - `JsonValue type = "encrypted_code_execution_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "code_execution_tool_result"`

  - `class BashCodeExecutionToolResultBlock:`

    - `Content content`

      - `class BashCodeExecutionToolResultError:`

        - `BashCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

        - `JsonValue type = "bash_code_execution_tool_result_error"`

      - `class BashCodeExecutionResultBlock:`

        - `List<BashCodeExecutionOutputBlock> content`

          - `String fileId`

          - `JsonValue type = "bash_code_execution_output"`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue type = "bash_code_execution_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "bash_code_execution_tool_result"`

  - `class TextEditorCodeExecutionToolResultBlock:`

    - `Content content`

      - `class TextEditorCodeExecutionToolResultError:`

        - `TextEditorCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `FILE_NOT_FOUND("file_not_found")`

        - `Optional<String> errorMessage`

        - `JsonValue type = "text_editor_code_execution_tool_result_error"`

      - `class TextEditorCodeExecutionViewResultBlock:`

        - `String content`

        - `FileType fileType`

          - `TEXT("text")`

          - `IMAGE("image")`

          - `PDF("pdf")`

        - `Optional<Long> numLines`

        - `Optional<Long> startLine`

        - `Optional<Long> totalLines`

        - `JsonValue type = "text_editor_code_execution_view_result"`

      - `class TextEditorCodeExecutionCreateResultBlock:`

        - `boolean isFileUpdate`

        - `JsonValue type = "text_editor_code_execution_create_result"`

      - `class TextEditorCodeExecutionStrReplaceResultBlock:`

        - `Optional<List<String>> lines`

        - `Optional<Long> newLines`

        - `Optional<Long> newStart`

        - `Optional<Long> oldLines`

        - `Optional<Long> oldStart`

        - `JsonValue type = "text_editor_code_execution_str_replace_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "text_editor_code_execution_tool_result"`

  - `class ToolSearchToolResultBlock:`

    - `Content content`

      - `class ToolSearchToolResultError:`

        - `ToolSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `Optional<String> errorMessage`

        - `JsonValue type = "tool_search_tool_result_error"`

      - `class ToolSearchToolSearchResultBlock:`

        - `List<ToolReferenceBlock> toolReferences`

          - `String toolName`

            maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `JsonValue type = "tool_reference"`

        - `JsonValue type = "tool_search_tool_search_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "tool_search_tool_result"`

  - `class ContainerUploadBlock:`

    Response model for a file uploaded to the container.

    - `String fileId`

    - `JsonValue type = "container_upload"`

### Content Block Param

- `class ContentBlockParam: union`

  Regular text content.

  - `class TextBlockParam:`

    - `String text`

      minLength: 1

    - `JsonValue type = "text"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue type = "ephemeral"`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<List<TextCitationParam>> citations`

      - `class CitationCharLocationParam:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endCharIndex`

        - `long startCharIndex`

          minimum: 0

        - `JsonValue type = "char_location"`

      - `class CitationPageLocationParam:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endPageNumber`

        - `long startPageNumber`

          minimum: 1

        - `JsonValue type = "page_location"`

      - `class CitationContentBlockLocationParam:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `JsonValue type = "content_block_location"`

      - `class CitationWebSearchResultLocationParam:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

          maxLength: 512, minLength: 1

        - `JsonValue type = "web_search_result_location"`

        - `String url`

          minLength: 1

      - `class CitationSearchResultLocationParam:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long searchResultIndex`

          0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

          Counted separately from `document_index`; server-side web search results are not included in this count.

          minimum: 0

        - `String source`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `Optional<String> title`

        - `JsonValue type = "search_result_location"`

  - `class ImageBlockParam:`

    - `Source source`

      - `class Base64ImageSource:`

        - `String data`

          format: byte

        - `MediaType mediaType`

          - `IMAGE_JPEG("image/jpeg")`

          - `IMAGE_PNG("image/png")`

          - `IMAGE_GIF("image/gif")`

          - `IMAGE_WEBP("image/webp")`

        - `JsonValue type = "base64"`

      - `class UrlImageSource:`

        - `JsonValue type = "url"`

        - `String url`

      - `class FileImageSource:`

        - `String fileId`

        - `JsonValue type = "file"`

    - `JsonValue type = "image"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<ImageTransformationsParam> transformations`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

      - `Optional<OversizedImage> oversizedImage`

        What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

        - `DOWNSIZE("downsize")`

        - `ERROR("error")`

  - `class DocumentBlockParam:`

    - `Source source`

      - `class Base64PdfSource:`

        - `String data`

          format: byte

        - `JsonValue mediaType = "application/pdf"`

        - `JsonValue type = "base64"`

      - `class PlainTextSource:`

        - `String data`

        - `JsonValue mediaType = "text/plain"`

        - `JsonValue type = "text"`

      - `class ContentBlockSource:`

        - `Content content`

          - `String`

          - `List<ContentBlockSourceContent>`

            - `class TextBlockParam:`

            - `class ImageBlockParam:`

        - `JsonValue type = "content"`

      - `class UrlPdfSource:`

        - `JsonValue type = "url"`

        - `String url`

      - `class FileDocumentSource:`

        - `String fileId`

        - `JsonValue type = "file"`

    - `JsonValue type = "document"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      - `Optional<Boolean> enabled`

    - `Optional<String> context`

      minLength: 1

    - `Optional<String> title`

      maxLength: 500, minLength: 1

  - `class SearchResultBlockParam:`

    - `List<TextBlockParam> content`

      - `String text`

        minLength: 1

      - `JsonValue type = "text"`

      - `Optional<CacheControlEphemeral> cacheControl`

        Create a cache control breakpoint at this content block.

      - `Optional<List<TextCitationParam>> citations`

    - `String source`

    - `String title`

    - `JsonValue type = "search_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

  - `class ThinkingBlockParam:`

    - `String signature`

      The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

      Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

    - `String thinking`

      The `thinking` text of this block as returned by the API.

    - `JsonValue type = "thinking"`

  - `class RedactedThinkingBlockParam:`

    - `String data`

      The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

    - `JsonValue type = "redacted_thinking"`

  - `class ToolUseBlockParam:`

    - `String id`

      pattern: ^[a-zA-Z0-9_-]+$

    - `Input input`

    - `String name`

      maxLength: 200, minLength: 1

    - `JsonValue type = "tool_use"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

        - `JsonValue type = "direct"`

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

        - `String toolId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "code_execution_20250825"`

      - `class ServerToolCaller20260120:`

        - `String toolId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "code_execution_20260120"`

    - `Optional<String> toolsetName`

      For a toolset member tool_use, the toolset family this member belongs to.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

  - `class ToolResultBlockParam:`

    - `String toolUseId`

      pattern: ^[a-zA-Z0-9_-]+$

    - `JsonValue type = "tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Content> content`

      - `String`

      - `List<Block>`

        - `class TextBlockParam:`

        - `class ImageBlockParam:`

        - `class SearchResultBlockParam:`

        - `class DocumentBlockParam:`

        - `class ToolReferenceBlockParam:`

          Tool reference block that can be included in tool_result content.

          - `String toolName`

            maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `JsonValue type = "tool_reference"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `class BrowserStateBlockParam:`

          The caller's browser state after a browser toolset member call —
          the full inventory of open tabs, which tab is active, and any side
          effects (tabs opened, download state changes) the call produced.

          At most one per `tool_result`, only on a non-error result answering a
          browser toolset member `tool_use`. The server renders the
          model-visible text from it; the model never sees the raw fields.

          - `List<BrowserStateTabEntry> tabs`

            All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

            maxItems: 100

            - `String tabId`

              The caller-assigned identifier for this tab, unique within the inventory.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `String title`

              The title of the page the tab is showing. May be empty.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `String url`

              The URL of the page the tab is showing. May be empty.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `Optional<Boolean> active`

              Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

          - `JsonValue type = "browser_state"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<List<BrowserStateChange>> stateChanges`

            Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

            maxItems: 200, minItems: 1

            - `class BrowserStateChangeTabOpened:`

              A tab this call's execution opened that remains open at its end —
              the creation delta of the `tabs` inventory, not an event log.

              Carries only the `tab_id`; the tab's `title` and `url` live on its
              `tabs` entry, which must include the same `tab_id`. A tab opened
              during a failed call gets no deferred `tab_opened`; it simply appears
              in the next result's `tabs` inventory.

              - `String tabId`

                The `tab_id` of the opened tab, present in `tabs`.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `JsonValue type = "tab_opened"`

            - `class BrowserStateChangeDownloadStarted:`

              A file download that started during this call.

              - `String downloadId`

                The caller-assigned identifier for this download, stable across the state changes reporting it.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `JsonValue type = "download_started"`

              - `String url`

                The final post-redirect URL the download was served from.

                maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `class BrowserStateChangeDownloadCompleted:`

              A file download that finished during this call, reported with the
              same `download_id` as its `download_started` — or without a prior
              `download_started`, when the download finished during the call that
              started it (at most one state change per `download_id` per result).

              - `String downloadId`

                The caller-assigned identifier for this download, stable across the state changes reporting it.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `JsonValue type = "download_completed"`

              - `String url`

                The final post-redirect URL the download was served from.

                maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `Optional<String> path`

                Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

              - `Optional<Long> sizeBytes`

                The completed download's size.

                minimum: 0

            - `class BrowserStateChangeDownloadFailed:`

              A file download that failed — or was cancelled — during this call.

              - `String downloadId`

                The caller-assigned identifier for this download, stable across the state changes reporting it.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `JsonValue type = "download_failed"`

              - `String url`

                The final post-redirect URL the download was served from.

                maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `Optional<String> error`

                The failure or cancellation detail, when known.

                pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

    - `Optional<Boolean> isError`

    - `Optional<String> toolsetName`

      For a toolset member tool_result, the toolset family of the paired tool_use.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

  - `class ServerToolUseBlockParam:`

    - `String id`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `Input input`

    - `Name name`

      - `WEB_SEARCH("web_search")`

      - `WEB_FETCH("web_fetch")`

      - `CODE_EXECUTION("code_execution")`

      - `BASH_CODE_EXECUTION("bash_code_execution")`

      - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `JsonValue type = "server_tool_use"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120:`

  - `class WebSearchToolResultBlockParam:`

    - `WebSearchToolResultBlockParamContent content`

      - `List<WebSearchResultBlockParam>`

        - `String encryptedContent`

        - `String title`

        - `JsonValue type = "web_search_result"`

        - `String url`

        - `Optional<String> pageAge`

      - `class WebSearchToolRequestError:`

        - `WebSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `QUERY_TOO_LONG("query_too_long")`

          - `REQUEST_TOO_LARGE("request_too_large")`

        - `JsonValue type = "web_search_tool_result_error"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "web_search_tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120:`

  - `class WebFetchToolResultBlockParam:`

    - `Content content`

      - `class WebFetchToolResultErrorBlockParam:`

        - `WebFetchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `URL_TOO_LONG("url_too_long")`

          - `URL_NOT_ALLOWED("url_not_allowed")`

          - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

          - `URL_NOT_ACCESSIBLE("url_not_accessible")`

          - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `MAX_USES_EXCEEDED("max_uses_exceeded")`

          - `UNAVAILABLE("unavailable")`

        - `JsonValue type = "web_fetch_tool_result_error"`

      - `class WebFetchBlockParam:`

        - `DocumentBlockParam content`

        - `JsonValue type = "web_fetch_result"`

        - `String url`

          Fetched content URL

        - `Optional<String> retrievedAt`

          ISO 8601 timestamp when the content was retrieved

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "web_fetch_tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Caller> caller`

      Tool invocation directly from the model.

      - `class DirectCaller:`

        Tool invocation directly from the model.

      - `class ServerToolCaller:`

        Tool invocation generated by a server-side tool.

      - `class ServerToolCaller20260120:`

  - `class CodeExecutionToolResultBlockParam:`

    - `CodeExecutionToolResultBlockParamContent content`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `class CodeExecutionToolResultErrorParam:`

        - `CodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `JsonValue type = "code_execution_tool_result_error"`

      - `class CodeExecutionResultBlockParam:`

        - `List<CodeExecutionOutputBlockParam> content`

          - `String fileId`

          - `JsonValue type = "code_execution_output"`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue type = "code_execution_result"`

      - `class EncryptedCodeExecutionResultBlockParam:`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `List<CodeExecutionOutputBlockParam> content`

          - `String fileId`

          - `JsonValue type = "code_execution_output"`

        - `String encryptedStdout`

        - `long returnCode`

        - `String stderr`

        - `JsonValue type = "encrypted_code_execution_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "code_execution_tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BashCodeExecutionToolResultBlockParam:`

    - `Content content`

      - `class BashCodeExecutionToolResultErrorParam:`

        - `BashCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

        - `JsonValue type = "bash_code_execution_tool_result_error"`

      - `class BashCodeExecutionResultBlockParam:`

        - `List<BashCodeExecutionOutputBlockParam> content`

          - `String fileId`

          - `JsonValue type = "bash_code_execution_output"`

        - `long returnCode`

        - `String stderr`

        - `String stdout`

        - `JsonValue type = "bash_code_execution_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "bash_code_execution_tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

  - `class TextEditorCodeExecutionToolResultBlockParam:`

    - `Content content`

      - `class TextEditorCodeExecutionToolResultErrorParam:`

        - `TextEditorCodeExecutionToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `FILE_NOT_FOUND("file_not_found")`

        - `JsonValue type = "text_editor_code_execution_tool_result_error"`

        - `Optional<String> errorMessage`

      - `class TextEditorCodeExecutionViewResultBlockParam:`

        - `String content`

        - `FileType fileType`

          - `TEXT("text")`

          - `IMAGE("image")`

          - `PDF("pdf")`

        - `JsonValue type = "text_editor_code_execution_view_result"`

        - `Optional<Long> numLines`

        - `Optional<Long> startLine`

        - `Optional<Long> totalLines`

      - `class TextEditorCodeExecutionCreateResultBlockParam:`

        - `boolean isFileUpdate`

        - `JsonValue type = "text_editor_code_execution_create_result"`

      - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

        - `JsonValue type = "text_editor_code_execution_str_replace_result"`

        - `Optional<List<String>> lines`

        - `Optional<Long> newLines`

        - `Optional<Long> newStart`

        - `Optional<Long> oldLines`

        - `Optional<Long> oldStart`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "text_editor_code_execution_tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

  - `class ToolSearchToolResultBlockParam:`

    - `Content content`

      - `class ToolSearchToolResultErrorParam:`

        - `ToolSearchToolResultErrorCode errorCode`

          - `INVALID_TOOL_INPUT("invalid_tool_input")`

          - `UNAVAILABLE("unavailable")`

          - `TOO_MANY_REQUESTS("too_many_requests")`

          - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `JsonValue type = "tool_search_tool_result_error"`

        - `Optional<String> errorMessage`

      - `class ToolSearchToolSearchResultBlockParam:`

        - `List<ToolReferenceBlockParam> toolReferences`

          - `String toolName`

            maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `JsonValue type = "tool_reference"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

        - `JsonValue type = "tool_search_tool_search_result"`

    - `String toolUseId`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `JsonValue type = "tool_search_tool_result"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

  - `class ContainerUploadBlockParam:`

    A content block that represents a file to be uploaded to the container
    Files uploaded via this block will be available in the container's input directory.

    - `String fileId`

    - `JsonValue type = "container_upload"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

### Content Block Source

- `class ContentBlockSource:`

  - `Content content`

    - `String`

    - `List<ContentBlockSourceContent>`

      - `class TextBlockParam:`

        - `String text`

          minLength: 1

        - `JsonValue type = "text"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue type = "ephemeral"`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<List<TextCitationParam>> citations`

          - `class CitationCharLocationParam:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endCharIndex`

            - `long startCharIndex`

              minimum: 0

            - `JsonValue type = "char_location"`

          - `class CitationPageLocationParam:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endPageNumber`

            - `long startPageNumber`

              minimum: 1

            - `JsonValue type = "page_location"`

          - `class CitationContentBlockLocationParam:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `JsonValue type = "content_block_location"`

          - `class CitationWebSearchResultLocationParam:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

              maxLength: 512, minLength: 1

            - `JsonValue type = "web_search_result_location"`

            - `String url`

              minLength: 1

          - `class CitationSearchResultLocationParam:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long searchResultIndex`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `String source`

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `Optional<String> title`

            - `JsonValue type = "search_result_location"`

      - `class ImageBlockParam:`

        - `Source source`

          - `class Base64ImageSource:`

            - `String data`

              format: byte

            - `MediaType mediaType`

              - `IMAGE_JPEG("image/jpeg")`

              - `IMAGE_PNG("image/png")`

              - `IMAGE_GIF("image/gif")`

              - `IMAGE_WEBP("image/webp")`

            - `JsonValue type = "base64"`

          - `class UrlImageSource:`

            - `JsonValue type = "url"`

            - `String url`

          - `class FileImageSource:`

            - `String fileId`

            - `JsonValue type = "file"`

        - `JsonValue type = "image"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<ImageTransformationsParam> transformations`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `Optional<OversizedImage> oversizedImage`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `DOWNSIZE("downsize")`

            - `ERROR("error")`

  - `JsonValue type = "content"`

### Content Block Source Content

- `class ContentBlockSourceContent: union`

  - `class TextBlockParam:`

    - `String text`

      minLength: 1

    - `JsonValue type = "text"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue type = "ephemeral"`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<List<TextCitationParam>> citations`

      - `class CitationCharLocationParam:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endCharIndex`

        - `long startCharIndex`

          minimum: 0

        - `JsonValue type = "char_location"`

      - `class CitationPageLocationParam:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endPageNumber`

        - `long startPageNumber`

          minimum: 1

        - `JsonValue type = "page_location"`

      - `class CitationContentBlockLocationParam:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `JsonValue type = "content_block_location"`

      - `class CitationWebSearchResultLocationParam:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

          maxLength: 512, minLength: 1

        - `JsonValue type = "web_search_result_location"`

        - `String url`

          minLength: 1

      - `class CitationSearchResultLocationParam:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long searchResultIndex`

          0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

          Counted separately from `document_index`; server-side web search results are not included in this count.

          minimum: 0

        - `String source`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `Optional<String> title`

        - `JsonValue type = "search_result_location"`

  - `class ImageBlockParam:`

    - `Source source`

      - `class Base64ImageSource:`

        - `String data`

          format: byte

        - `MediaType mediaType`

          - `IMAGE_JPEG("image/jpeg")`

          - `IMAGE_PNG("image/png")`

          - `IMAGE_GIF("image/gif")`

          - `IMAGE_WEBP("image/webp")`

        - `JsonValue type = "base64"`

      - `class UrlImageSource:`

        - `JsonValue type = "url"`

        - `String url`

      - `class FileImageSource:`

        - `String fileId`

        - `JsonValue type = "file"`

    - `JsonValue type = "image"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<ImageTransformationsParam> transformations`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

      - `Optional<OversizedImage> oversizedImage`

        What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

        - `DOWNSIZE("downsize")`

        - `ERROR("error")`

### Direct Caller

- `class DirectCaller:`

  Tool invocation directly from the model.

  - `JsonValue type = "direct"`

### Document Block

- `class DocumentBlock:`

  - `Optional<CitationsConfig> citations`

    Citation configuration for the document

    - `boolean enabled`

  - `Source source`

    - `class Base64PdfSource:`

      - `String data`

        format: byte

      - `JsonValue mediaType = "application/pdf"`

      - `JsonValue type = "base64"`

    - `class PlainTextSource:`

      - `String data`

      - `JsonValue mediaType = "text/plain"`

      - `JsonValue type = "text"`

  - `Optional<String> title`

    The title of the document

  - `JsonValue type = "document"`

### Document Block Param

- `class DocumentBlockParam:`

  - `Source source`

    - `class Base64PdfSource:`

      - `String data`

        format: byte

      - `JsonValue mediaType = "application/pdf"`

      - `JsonValue type = "base64"`

    - `class PlainTextSource:`

      - `String data`

      - `JsonValue mediaType = "text/plain"`

      - `JsonValue type = "text"`

    - `class ContentBlockSource:`

      - `Content content`

        - `String`

        - `List<ContentBlockSourceContent>`

          - `class TextBlockParam:`

            - `String text`

              minLength: 1

            - `JsonValue type = "text"`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

              - `JsonValue type = "ephemeral"`

              - `Optional<Ttl> ttl`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                - `TTL_5M("5m")`

                - `TTL_1H("1h")`

            - `Optional<List<TextCitationParam>> citations`

              - `class CitationCharLocationParam:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                  maxLength: 500, minLength: 1

                - `long endCharIndex`

                - `long startCharIndex`

                  minimum: 0

                - `JsonValue type = "char_location"`

              - `class CitationPageLocationParam:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                  maxLength: 500, minLength: 1

                - `long endPageNumber`

                - `long startPageNumber`

                  minimum: 1

                - `JsonValue type = "page_location"`

              - `class CitationContentBlockLocationParam:`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                  maxLength: 500, minLength: 1

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `JsonValue type = "content_block_location"`

              - `class CitationWebSearchResultLocationParam:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512, minLength: 1

                - `JsonValue type = "web_search_result_location"`

                - `String url`

                  minLength: 1

              - `class CitationSearchResultLocationParam:`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `long searchResultIndex`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `String source`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `Optional<String> title`

                - `JsonValue type = "search_result_location"`

          - `class ImageBlockParam:`

            - `Source source`

              - `class Base64ImageSource:`

                - `String data`

                  format: byte

                - `MediaType mediaType`

                  - `IMAGE_JPEG("image/jpeg")`

                  - `IMAGE_PNG("image/png")`

                  - `IMAGE_GIF("image/gif")`

                  - `IMAGE_WEBP("image/webp")`

                - `JsonValue type = "base64"`

              - `class UrlImageSource:`

                - `JsonValue type = "url"`

                - `String url`

              - `class FileImageSource:`

                - `String fileId`

                - `JsonValue type = "file"`

            - `JsonValue type = "image"`

            - `Optional<CacheControlEphemeral> cacheControl`

              Create a cache control breakpoint at this content block.

            - `Optional<ImageTransformationsParam> transformations`

              Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

              - `Optional<OversizedImage> oversizedImage`

                What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                - `DOWNSIZE("downsize")`

                - `ERROR("error")`

      - `JsonValue type = "content"`

    - `class UrlPdfSource:`

      - `JsonValue type = "url"`

      - `String url`

    - `class FileDocumentSource:`

      - `String fileId`

      - `JsonValue type = "file"`

  - `JsonValue type = "document"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

  - `Optional<CitationsConfigParam> citations`

    - `Optional<Boolean> enabled`

  - `Optional<String> context`

    minLength: 1

  - `Optional<String> title`

    maxLength: 500, minLength: 1

### Encrypted Code Execution Result Block

- `class EncryptedCodeExecutionResultBlock:`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `List<CodeExecutionOutputBlock> content`

    - `String fileId`

    - `JsonValue type = "code_execution_output"`

  - `String encryptedStdout`

  - `long returnCode`

  - `String stderr`

  - `JsonValue type = "encrypted_code_execution_result"`

### Encrypted Code Execution Result Block Param

- `class EncryptedCodeExecutionResultBlockParam:`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `List<CodeExecutionOutputBlockParam> content`

    - `String fileId`

    - `JsonValue type = "code_execution_output"`

  - `String encryptedStdout`

  - `long returnCode`

  - `String stderr`

  - `JsonValue type = "encrypted_code_execution_result"`

### File Document Source

- `class FileDocumentSource:`

  - `String fileId`

  - `JsonValue type = "file"`

### File Image Source

- `class FileImageSource:`

  - `String fileId`

  - `JsonValue type = "file"`

### Image Block Param

- `class ImageBlockParam:`

  - `Source source`

    - `class Base64ImageSource:`

      - `String data`

        format: byte

      - `MediaType mediaType`

        - `IMAGE_JPEG("image/jpeg")`

        - `IMAGE_PNG("image/png")`

        - `IMAGE_GIF("image/gif")`

        - `IMAGE_WEBP("image/webp")`

      - `JsonValue type = "base64"`

    - `class UrlImageSource:`

      - `JsonValue type = "url"`

      - `String url`

    - `class FileImageSource:`

      - `String fileId`

      - `JsonValue type = "file"`

  - `JsonValue type = "image"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<ImageTransformationsParam> transformations`

    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

    - `Optional<OversizedImage> oversizedImage`

      What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

      - `DOWNSIZE("downsize")`

      - `ERROR("error")`

### Image Transformations Param

- `class ImageTransformationsParam:`

  Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

  - `Optional<OversizedImage> oversizedImage`

    What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

    - `DOWNSIZE("downsize")`

    - `ERROR("error")`

### Input JSON Delta

- `class InputJsonDelta:`

  - `String partialJson`

  - `JsonValue type = "input_json_delta"`

### JSON Output Format

- `class JsonOutputFormat:`

  - `Schema schema`

    The JSON schema of the format

  - `JsonValue type = "json_schema"`

### Memory Tool 20250818

- `class MemoryTool20250818:`

  - `JsonValue name = "memory"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "memory_20250818"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Message

- `class Message:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<Container> container`

    Information about the container used in the request (for the code execution tool)

    - `String id`

      Identifier for the container used in this request

    - `LocalDateTime expiresAt`

      The time at which the container will expire.

      format: date-time

    - `Optional<List<ContainerSkill>> skills`

      Skills loaded in the container

      - `String skillId`

        Skill ID

        maxLength: 64, minLength: 1

      - `Type type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `ANTHROPIC("anthropic")`

        - `CUSTOM("custom")`

      - `String version`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `List<ContentBlock> content`

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

    - `class TextBlock:`

      - `Optional<List<TextCitation>> citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

            minimum: 0

          - `JsonValue type = "char_location"`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

            minimum: 1

          - `JsonValue type = "page_location"`

        - `class CitationContentBlockLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `Optional<String> fileId`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `JsonValue type = "content_block_location"`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

            maxLength: 512

          - `JsonValue type = "web_search_result_location"`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `long searchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `String source`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `Optional<String> title`

          - `JsonValue type = "search_result_location"`

      - `String text`

        maxLength: 5000000, minLength: 0

      - `JsonValue type = "text"`

    - `class ThinkingBlock:`

      - `String signature`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `String thinking`

        The text of Claude's thinking process for this block.

      - `JsonValue type = "thinking"`

    - `class RedactedThinkingBlock:`

      - `String data`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `JsonValue type = "redacted_thinking"`

    - `class ToolUseBlock:`

      - `String id`

        pattern: ^[a-zA-Z0-9_-]+$

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue type = "direct"`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_20250825"`

        - `class ServerToolCaller20260120:`

          - `String toolId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_20260120"`

      - `Input input`

      - `String name`

        minLength: 1

      - `JsonValue type = "tool_use"`

      - `Optional<String> toolsetName`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock:`

      - `String id`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `Input input`

      - `Name name`

        - `WEB_SEARCH("web_search")`

        - `WEB_FETCH("web_fetch")`

        - `CODE_EXECUTION("code_execution")`

        - `BASH_CODE_EXECUTION("bash_code_execution")`

        - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `JsonValue type = "server_tool_use"`

    - `class WebSearchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `WebSearchToolResultBlockContent content`

        - `class WebSearchToolResultError:`

          - `WebSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `QUERY_TOO_LONG("query_too_long")`

            - `REQUEST_TOO_LARGE("request_too_large")`

          - `JsonValue type = "web_search_tool_result_error"`

        - `List<WebSearchResultBlock>`

          - `String encryptedContent`

          - `Optional<String> pageAge`

          - `String title`

          - `JsonValue type = "web_search_result"`

          - `String url`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "web_search_tool_result"`

    - `class WebFetchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `Content content`

        - `class WebFetchToolResultErrorBlock:`

          - `WebFetchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `URL_TOO_LONG("url_too_long")`

            - `URL_NOT_ALLOWED("url_not_allowed")`

            - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

            - `URL_NOT_ACCESSIBLE("url_not_accessible")`

            - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `UNAVAILABLE("unavailable")`

          - `JsonValue type = "web_fetch_tool_result_error"`

        - `class WebFetchBlock:`

          - `DocumentBlock content`

            - `Optional<CitationsConfig> citations`

              Citation configuration for the document

              - `boolean enabled`

            - `Source source`

              - `class Base64PdfSource:`

                - `String data`

                  format: byte

                - `JsonValue mediaType = "application/pdf"`

                - `JsonValue type = "base64"`

              - `class PlainTextSource:`

                - `String data`

                - `JsonValue mediaType = "text/plain"`

                - `JsonValue type = "text"`

            - `Optional<String> title`

              The title of the document

            - `JsonValue type = "document"`

          - `Optional<String> retrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonValue type = "web_fetch_result"`

          - `String url`

            Fetched content URL

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "web_fetch_tool_result"`

    - `class CodeExecutionToolResultBlock:`

      - `CodeExecutionToolResultBlockContent content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `CodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `JsonValue type = "code_execution_tool_result_error"`

        - `class CodeExecutionResultBlock:`

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "code_execution_output"`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue type = "code_execution_result"`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "code_execution_output"`

          - `String encryptedStdout`

          - `long returnCode`

          - `String stderr`

          - `JsonValue type = "encrypted_code_execution_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_tool_result"`

    - `class BashCodeExecutionToolResultBlock:`

      - `Content content`

        - `class BashCodeExecutionToolResultError:`

          - `BashCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

          - `JsonValue type = "bash_code_execution_tool_result_error"`

        - `class BashCodeExecutionResultBlock:`

          - `List<BashCodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "bash_code_execution_output"`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue type = "bash_code_execution_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "bash_code_execution_tool_result"`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `Content content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `TextEditorCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `FILE_NOT_FOUND("file_not_found")`

          - `Optional<String> errorMessage`

          - `JsonValue type = "text_editor_code_execution_tool_result_error"`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `String content`

          - `FileType fileType`

            - `TEXT("text")`

            - `IMAGE("image")`

            - `PDF("pdf")`

          - `Optional<Long> numLines`

          - `Optional<Long> startLine`

          - `Optional<Long> totalLines`

          - `JsonValue type = "text_editor_code_execution_view_result"`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `boolean isFileUpdate`

          - `JsonValue type = "text_editor_code_execution_create_result"`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `Optional<List<String>> lines`

          - `Optional<Long> newLines`

          - `Optional<Long> newStart`

          - `Optional<Long> oldLines`

          - `Optional<Long> oldStart`

          - `JsonValue type = "text_editor_code_execution_str_replace_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "text_editor_code_execution_tool_result"`

    - `class ToolSearchToolResultBlock:`

      - `Content content`

        - `class ToolSearchToolResultError:`

          - `ToolSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `Optional<String> errorMessage`

          - `JsonValue type = "tool_search_tool_result_error"`

        - `class ToolSearchToolSearchResultBlock:`

          - `List<ToolReferenceBlock> toolReferences`

            - `String toolName`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `JsonValue type = "tool_reference"`

          - `JsonValue type = "tool_search_tool_search_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "tool_search_tool_result"`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `String fileId`

      - `JsonValue type = "container_upload"`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

      Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

    - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

      Our most capable model for cybersecurity and biology research, available through trusted access programs

    - `CLAUDE_SONNET_5("claude-sonnet-5")`

      High-performance model for coding and agents

    - `CLAUDE_FABLE_5("claude-fable-5")`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `CLAUDE_MYTHOS_5("claude-mythos-5")`

      Most capable model for cybersecurity and biology research

    - `CLAUDE_OPUS_5("claude-opus-5")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

      New class of intelligence, strongest in coding and cybersecurity

    - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

      Best combination of speed and intelligence

    - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

      Fastest model with near-frontier intelligence

    - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

      Fastest model with near-frontier intelligence

    - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

      Powerful intelligence for long-running agents and coding

    - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

      High-performance model for agents and coding

    - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

      High-performance model for agents and coding

  - `JsonValue role = "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `Optional<RefusalStopDetails> stopDetails`

    Structured information about a refusal.

    - `Optional<Category> category`

      The policy category that triggered a refusal.

      - `CYBER("cyber")`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `BIO("bio")`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `FRONTIER_LLM("frontier_llm")`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `REASONING_EXTRACTION("reasoning_extraction")`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `GENERAL_HARMS("general_harms")`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `Optional<String> explanation`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `JsonValue type = "refusal"`

  - `Optional<StopReason> stopReason`

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

    - `END_TURN("end_turn")`

    - `MAX_TOKENS("max_tokens")`

    - `STOP_SEQUENCE("stop_sequence")`

    - `TOOL_USE("tool_use")`

    - `PAUSE_TURN("pause_turn")`

    - `REFUSAL("refusal")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

  - `Optional<String> stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonValue type = "message"`

    Object type.

    For Messages, this is always `"message"`.

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `Optional<CacheCreation> cacheCreation`

      Breakdown of cached tokens by TTL

      - `long ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `long ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `Optional<Long> cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `Optional<Long> cacheReadInputTokens`

      The number of input tokens read from the cache.

      minimum: 0

    - `Optional<String> inferenceGeo`

      The geographic region where inference was performed for this request.

    - `long inputTokens`

      The number of input tokens which were used.

      minimum: 0

    - `long outputTokens`

      The number of output tokens which were used.

      minimum: 0

    - `Optional<OutputTokensDetails> outputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `long thinkingTokens`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `Optional<ServerToolUsage> serverToolUse`

      The number of server tool requests.

      - `long webFetchRequests`

        The number of web fetch tool requests.

        minimum: 0

      - `long webSearchRequests`

        The number of web search tool requests.

        minimum: 0

    - `Optional<ServiceTier> serviceTier`

      If the request used the priority, standard, or batch tier.

      - `STANDARD("standard")`

      - `PRIORITY("priority")`

      - `BATCH("batch")`

### Message Count Tokens Tool

- `class MessageCountTokensTool: union`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `class Tool:`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `JsonValue type = "object"`

      - `Optional<Properties> properties`

      - `Optional<List<String>> required`

    - `String name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue type = "ephemeral"`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<String> description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `Optional<Boolean> eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Type> type`

  - `class ToolBash20250124:`

    - `JsonValue name = "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "bash_20250124"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250522:`

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20250522"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250825:`

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20250825"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260120:`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20260120"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260521:`

    Code execution tool with REPL state persistence.

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20260521"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BrowserToolset20260801:`

    The browser toolset: a single `tools[]` entry (carrying no
    `name`) that declares the browser tool family. The model is served
    the family's tool with any members disabled via `configs` removed
    from its schema.

    - `JsonValue type = "browser_toolset_20260801"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<BrowserToolsetConfigs> configs`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `Optional<BrowserCloseTabConfig> closeTab`

        `close_tab`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserDoubleClickConfig> doubleClick`

        `double_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserFileUploadConfig> fileUpload`

        `file_upload`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserFindConfig> find`

        `find`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserFormInputConfig> formInput`

        `form_input`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserGetPageTextConfig> getPageText`

        `get_page_text`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserHoldKeyConfig> holdKey`

        `hold_key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserHoverConfig> hover`

        `hover`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserJavascriptExecConfig> javascriptExec`

        `javascript_exec`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserKeyConfig> key`

        `key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftClickConfig> leftClick`

        `left_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

        `left_click_drag`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

        `left_mouse_down`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

        `left_mouse_up`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserListTabsConfig> listTabs`

        `list_tabs`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserMiddleClickConfig> middleClick`

        `middle_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserMouseMoveConfig> mouseMove`

        `mouse_move`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserNavigateConfig> navigate`

        `navigate`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserNewTabConfig> newTab`

        `new_tab`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserReadConsoleConfig> readConsole`

        `read_console`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserReadNetworkConfig> readNetwork`

        `read_network`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserReadPageConfig> readPage`

        `read_page`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserRightClickConfig> rightClick`

        `right_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserScreenshotConfig> screenshot`

        `screenshot`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserScrollConfig> scroll`

        `scroll`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserScrollToConfig> scrollTo`

        `scroll_to`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserSwitchTabConfig> switchTab`

        `switch_tab`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserTripleClickConfig> tripleClick`

        `triple_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserTypeConfig> type`

        `type`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserWaitConfig> wait`

        `wait`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserZoomConfig> zoom`

        `zoom`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class MemoryTool20250818:`

    - `JsonValue name = "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "memory_20250818"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ComputerToolset20260801:`

    The computer toolset: a single `tools[]` entry (carrying no
    `name`) that declares the computer tool family. The model is
    served the family's tool with any members disabled via `configs`
    removed from its schema. Every member is enabled by default, zoom
    included. The single-tool options `display_number` and
    `enable_zoom` are not fields of a toolset entry — it carries only
    `type`, `configs`, and `cache_control`; zoom is controlled
    via `configs.zoom.enabled`.

    - `JsonValue type = "computer_toolset_20260801"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<ComputerToolsetConfigs> configs`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `Optional<ComputerCursorPositionConfig> cursorPosition`

        `cursor_position`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerDoubleClickConfig> doubleClick`

        `double_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerHoldKeyConfig> holdKey`

        `hold_key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerKeyConfig> key`

        `key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftClickConfig> leftClick`

        `left_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

        `left_click_drag`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

        `left_mouse_down`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

        `left_mouse_up`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerMiddleClickConfig> middleClick`

        `middle_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerMouseMoveConfig> mouseMove`

        `mouse_move`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerRightClickConfig> rightClick`

        `right_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerScreenshotConfig> screenshot`

        `screenshot`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerScrollConfig> scroll`

        `scroll`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerTripleClickConfig> tripleClick`

        `triple_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerTypeConfig> type`

        `type`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerWaitConfig> wait`

        `wait`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerZoomConfig> zoom`

        `zoom`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class ToolTextEditor20250124:`

    - `JsonValue name = "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "text_editor_20250124"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250429:`

    - `JsonValue name = "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "text_editor_20250429"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250728:`

    - `JsonValue name = "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "text_editor_20250728"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Long> maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      minimum: 1

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20250305:`

    - `JsonValue name = "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_search_20250305"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `JsonValue type = "approximate"`

      - `Optional<String> city`

        The city of the user.

        maxLength: 255, minLength: 1

      - `Optional<String> country`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `Optional<String> region`

        The region of the user.

        maxLength: 255, minLength: 1

      - `Optional<String> timezone`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `class WebFetchTool20250910:`

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20250910"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> enabled`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20260209:`

    - `JsonValue name = "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_search_20260209"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class WebFetchTool20260209:`

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20260209"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebFetchTool20260309:`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20260309"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Boolean> useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class WebSearchTool20260318:`

    - `JsonValue name = "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_search_20260318"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<ResponseInclusion> responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `FULL("full")`

      - `EXCLUDED("excluded")`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class WebFetchTool20260318:`

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20260318"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<ResponseInclusion> responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `FULL("full")`

      - `EXCLUDED("excluded")`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Boolean> useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class ToolSearchToolBm25_20251119:`

    - `JsonValue name = "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

      - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolRegex20251119:`

    - `JsonValue name = "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

      - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

### Message Create Params Container

- `class MessageCreateParamsContainer: union`

  Container identifier for reuse across requests.

  - `class ContainerParams:`

    Container parameters with skills to be loaded.

    - `Optional<String> id`

      Container id

    - `Optional<List<SkillParams>> skills`

      List of skills to load in the container

      maxItems: 20

      - `String skillId`

        Skill ID

        maxLength: 64, minLength: 1

      - `Type type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `ANTHROPIC("anthropic")`

        - `CUSTOM("custom")`

      - `Optional<String> version`

        Skill version or 'latest' for most recent version

        maxLength: 64, minLength: 1

  - `String`

### Message Delta Usage

- `class MessageDeltaUsage:`

  - `Optional<Long> cacheCreationInputTokens`

    The cumulative number of input tokens used to create the cache entry.

    minimum: 0

  - `Optional<Long> cacheReadInputTokens`

    The cumulative number of input tokens read from the cache.

    minimum: 0

  - `Optional<Long> inputTokens`

    The cumulative number of input tokens which were used.

    minimum: 0

  - `long outputTokens`

    The cumulative number of output tokens which were used.

  - `Optional<OutputTokensDetails> outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

    - `long thinkingTokens`

      Number of output tokens the model generated as internal reasoning, including
      the thinking-block delimiter tokens.

      Reflects the raw reasoning the model produced, not the (possibly shorter)
      summarized thinking text returned in the response body. Computed by
      re-tokenizing the raw reasoning text, so it may differ from the model's exact
      generation count by a small number of tokens. Always ≤ `output_tokens`;
      `output_tokens - thinking_tokens` approximates the non-reasoning output.

      minimum: 0

  - `Optional<ServerToolUsage> serverToolUse`

    The number of server tool requests.

    - `long webFetchRequests`

      The number of web fetch tool requests.

      minimum: 0

    - `long webSearchRequests`

      The number of web search tool requests.

      minimum: 0

### Message Param

- `class MessageParam:`

  - `Content content`

    - `String`

    - `List<ContentBlockParam>`

      - `class TextBlockParam:`

        - `String text`

          minLength: 1

        - `JsonValue type = "text"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue type = "ephemeral"`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

        - `Optional<List<TextCitationParam>> citations`

          - `class CitationCharLocationParam:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endCharIndex`

            - `long startCharIndex`

              minimum: 0

            - `JsonValue type = "char_location"`

          - `class CitationPageLocationParam:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endPageNumber`

            - `long startPageNumber`

              minimum: 1

            - `JsonValue type = "page_location"`

          - `class CitationContentBlockLocationParam:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `JsonValue type = "content_block_location"`

          - `class CitationWebSearchResultLocationParam:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

              maxLength: 512, minLength: 1

            - `JsonValue type = "web_search_result_location"`

            - `String url`

              minLength: 1

          - `class CitationSearchResultLocationParam:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long searchResultIndex`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `String source`

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `Optional<String> title`

            - `JsonValue type = "search_result_location"`

      - `class ImageBlockParam:`

        - `Source source`

          - `class Base64ImageSource:`

            - `String data`

              format: byte

            - `MediaType mediaType`

              - `IMAGE_JPEG("image/jpeg")`

              - `IMAGE_PNG("image/png")`

              - `IMAGE_GIF("image/gif")`

              - `IMAGE_WEBP("image/webp")`

            - `JsonValue type = "base64"`

          - `class UrlImageSource:`

            - `JsonValue type = "url"`

            - `String url`

          - `class FileImageSource:`

            - `String fileId`

            - `JsonValue type = "file"`

        - `JsonValue type = "image"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<ImageTransformationsParam> transformations`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `Optional<OversizedImage> oversizedImage`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `DOWNSIZE("downsize")`

            - `ERROR("error")`

      - `class DocumentBlockParam:`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

              format: byte

            - `JsonValue mediaType = "application/pdf"`

            - `JsonValue type = "base64"`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue mediaType = "text/plain"`

            - `JsonValue type = "text"`

          - `class ContentBlockSource:`

            - `Content content`

              - `String`

              - `List<ContentBlockSourceContent>`

                - `class TextBlockParam:`

                - `class ImageBlockParam:`

            - `JsonValue type = "content"`

          - `class UrlPdfSource:`

            - `JsonValue type = "url"`

            - `String url`

          - `class FileDocumentSource:`

            - `String fileId`

            - `JsonValue type = "file"`

        - `JsonValue type = "document"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

        - `Optional<String> context`

          minLength: 1

        - `Optional<String> title`

          maxLength: 500, minLength: 1

      - `class SearchResultBlockParam:`

        - `List<TextBlockParam> content`

          - `String text`

            minLength: 1

          - `JsonValue type = "text"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<List<TextCitationParam>> citations`

        - `String source`

        - `String title`

        - `JsonValue type = "search_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<CitationsConfigParam> citations`

      - `class ThinkingBlockParam:`

        - `String signature`

          The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

          Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

        - `String thinking`

          The `thinking` text of this block as returned by the API.

        - `JsonValue type = "thinking"`

      - `class RedactedThinkingBlockParam:`

        - `String data`

          The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

        - `JsonValue type = "redacted_thinking"`

      - `class ToolUseBlockParam:`

        - `String id`

          pattern: ^[a-zA-Z0-9_-]+$

        - `Input input`

        - `String name`

          maxLength: 200, minLength: 1

        - `JsonValue type = "tool_use"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue type = "direct"`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "code_execution_20250825"`

          - `class ServerToolCaller20260120:`

            - `String toolId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "code_execution_20260120"`

        - `Optional<String> toolsetName`

          For a toolset member tool_use, the toolset family this member belongs to.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class ToolResultBlockParam:`

        - `String toolUseId`

          pattern: ^[a-zA-Z0-9_-]+$

        - `JsonValue type = "tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<Content> content`

          - `String`

          - `List<Block>`

            - `class TextBlockParam:`

            - `class ImageBlockParam:`

            - `class SearchResultBlockParam:`

            - `class DocumentBlockParam:`

            - `class ToolReferenceBlockParam:`

              Tool reference block that can be included in tool_result content.

              - `String toolName`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `JsonValue type = "tool_reference"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BrowserStateBlockParam:`

              The caller's browser state after a browser toolset member call —
              the full inventory of open tabs, which tab is active, and any side
              effects (tabs opened, download state changes) the call produced.

              At most one per `tool_result`, only on a non-error result answering a
              browser toolset member `tool_use`. The server renders the
              model-visible text from it; the model never sees the raw fields.

              - `List<BrowserStateTabEntry> tabs`

                All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                maxItems: 100

                - `String tabId`

                  The caller-assigned identifier for this tab, unique within the inventory.

                  maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `String title`

                  The title of the page the tab is showing. May be empty.

                  maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `String url`

                  The URL of the page the tab is showing. May be empty.

                  maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `Optional<Boolean> active`

                  Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

              - `JsonValue type = "browser_state"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<List<BrowserStateChange>> stateChanges`

                Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                maxItems: 200, minItems: 1

                - `class BrowserStateChangeTabOpened:`

                  A tab this call's execution opened that remains open at its end —
                  the creation delta of the `tabs` inventory, not an event log.

                  Carries only the `tab_id`; the tab's `title` and `url` live on its
                  `tabs` entry, which must include the same `tab_id`. A tab opened
                  during a failed call gets no deferred `tab_opened`; it simply appears
                  in the next result's `tabs` inventory.

                  - `String tabId`

                    The `tab_id` of the opened tab, present in `tabs`.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `JsonValue type = "tab_opened"`

                - `class BrowserStateChangeDownloadStarted:`

                  A file download that started during this call.

                  - `String downloadId`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `JsonValue type = "download_started"`

                  - `String url`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                - `class BrowserStateChangeDownloadCompleted:`

                  A file download that finished during this call, reported with the
                  same `download_id` as its `download_started` — or without a prior
                  `download_started`, when the download finished during the call that
                  started it (at most one state change per `download_id` per result).

                  - `String downloadId`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `JsonValue type = "download_completed"`

                  - `String url`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `Optional<String> path`

                    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                  - `Optional<Long> sizeBytes`

                    The completed download's size.

                    minimum: 0

                - `class BrowserStateChangeDownloadFailed:`

                  A file download that failed — or was cancelled — during this call.

                  - `String downloadId`

                    The caller-assigned identifier for this download, stable across the state changes reporting it.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `JsonValue type = "download_failed"`

                  - `String url`

                    The final post-redirect URL the download was served from.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `Optional<String> error`

                    The failure or cancellation detail, when known.

                    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

        - `Optional<Boolean> isError`

        - `Optional<String> toolsetName`

          For a toolset member tool_result, the toolset family of the paired tool_use.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class ServerToolUseBlockParam:`

        - `String id`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `Input input`

        - `Name name`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue type = "server_tool_use"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120:`

      - `class WebSearchToolResultBlockParam:`

        - `WebSearchToolResultBlockParamContent content`

          - `List<WebSearchResultBlockParam>`

            - `String encryptedContent`

            - `String title`

            - `JsonValue type = "web_search_result"`

            - `String url`

            - `Optional<String> pageAge`

          - `class WebSearchToolRequestError:`

            - `WebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue type = "web_search_tool_result_error"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "web_search_tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120:`

      - `class WebFetchToolResultBlockParam:`

        - `Content content`

          - `class WebFetchToolResultErrorBlockParam:`

            - `WebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue type = "web_fetch_tool_result_error"`

          - `class WebFetchBlockParam:`

            - `DocumentBlockParam content`

            - `JsonValue type = "web_fetch_result"`

            - `String url`

              Fetched content URL

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "web_fetch_tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120:`

      - `class CodeExecutionToolResultBlockParam:`

        - `CodeExecutionToolResultBlockParamContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultErrorParam:`

            - `CodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue type = "code_execution_tool_result_error"`

          - `class CodeExecutionResultBlockParam:`

            - `List<CodeExecutionOutputBlockParam> content`

              - `String fileId`

              - `JsonValue type = "code_execution_output"`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue type = "code_execution_result"`

          - `class EncryptedCodeExecutionResultBlockParam:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<CodeExecutionOutputBlockParam> content`

              - `String fileId`

              - `JsonValue type = "code_execution_output"`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue type = "encrypted_code_execution_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "code_execution_tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

      - `class BashCodeExecutionToolResultBlockParam:`

        - `Content content`

          - `class BashCodeExecutionToolResultErrorParam:`

            - `BashCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue type = "bash_code_execution_tool_result_error"`

          - `class BashCodeExecutionResultBlockParam:`

            - `List<BashCodeExecutionOutputBlockParam> content`

              - `String fileId`

              - `JsonValue type = "bash_code_execution_output"`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue type = "bash_code_execution_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "bash_code_execution_tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

      - `class TextEditorCodeExecutionToolResultBlockParam:`

        - `Content content`

          - `class TextEditorCodeExecutionToolResultErrorParam:`

            - `TextEditorCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `JsonValue type = "text_editor_code_execution_tool_result_error"`

            - `Optional<String> errorMessage`

          - `class TextEditorCodeExecutionViewResultBlockParam:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `JsonValue type = "text_editor_code_execution_view_result"`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

          - `class TextEditorCodeExecutionCreateResultBlockParam:`

            - `boolean isFileUpdate`

            - `JsonValue type = "text_editor_code_execution_create_result"`

          - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

            - `JsonValue type = "text_editor_code_execution_str_replace_result"`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "text_editor_code_execution_tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

      - `class ToolSearchToolResultBlockParam:`

        - `Content content`

          - `class ToolSearchToolResultErrorParam:`

            - `ToolSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue type = "tool_search_tool_result_error"`

            - `Optional<String> errorMessage`

          - `class ToolSearchToolSearchResultBlockParam:`

            - `List<ToolReferenceBlockParam> toolReferences`

              - `String toolName`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `JsonValue type = "tool_reference"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `JsonValue type = "tool_search_tool_search_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "tool_search_tool_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

      - `class ContainerUploadBlockParam:`

        A content block that represents a file to be uploaded to the container
        Files uploaded via this block will be available in the container's input directory.

        - `String fileId`

        - `JsonValue type = "container_upload"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

  - `Role role`

    - `USER("user")`

    - `ASSISTANT("assistant")`

    - `SYSTEM("system")`

### Message Tokens Count

- `class MessageTokensCount:`

  - `long inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `class Metadata:`

  - `Optional<String> userId`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    maxLength: 512

### Model

- `enum Model:`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

    Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

  - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

    Our most capable model for cybersecurity and biology research, available through trusted access programs

  - `CLAUDE_SONNET_5("claude-sonnet-5")`

    High-performance model for coding and agents

  - `CLAUDE_FABLE_5("claude-fable-5")`

    Next generation of intelligence for the hardest knowledge work and coding problems

  - `CLAUDE_MYTHOS_5("claude-mythos-5")`

    Most capable model for cybersecurity and biology research

  - `CLAUDE_OPUS_5("claude-opus-5")`

    Powerful intelligence for long-running agents and coding

  - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

    Powerful intelligence for long-running agents and coding

  - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

    Powerful intelligence for long-running agents and coding

  - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

    New class of intelligence, strongest in coding and cybersecurity

  - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

    Powerful intelligence for long-running agents and coding

  - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

    Best combination of speed and intelligence

  - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

    Fastest model with near-frontier intelligence

  - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

    Fastest model with near-frontier intelligence

  - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

    Powerful intelligence for long-running agents and coding

  - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

    Powerful intelligence for long-running agents and coding

  - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

    High-performance model for agents and coding

  - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

    High-performance model for agents and coding

### Output Config

- `class OutputConfig:`

  - `Optional<Effort> effort`

    All possible effort levels.

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

    - `XHIGH("xhigh")`

    - `MAX("max")`

  - `Optional<JsonOutputFormat> format`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `Schema schema`

      The JSON schema of the format

    - `JsonValue type = "json_schema"`

### Output Tokens Details

- `class OutputTokensDetails:`

  - `long thinkingTokens`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

    minimum: 0

### Plain Text Source

- `class PlainTextSource:`

  - `String data`

  - `JsonValue mediaType = "text/plain"`

  - `JsonValue type = "text"`

### Raw Content Block Delta

- `class RawContentBlockDelta: union`

  - `class TextDelta:`

    - `String text`

    - `JsonValue type = "text_delta"`

  - `class InputJsonDelta:`

    - `String partialJson`

    - `JsonValue type = "input_json_delta"`

  - `class CitationsDelta:`

    - `Citation citation`

      - `class CitationCharLocation:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

        - `long endCharIndex`

        - `Optional<String> fileId`

        - `long startCharIndex`

          minimum: 0

        - `JsonValue type = "char_location"`

      - `class CitationPageLocation:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

        - `long endPageNumber`

        - `Optional<String> fileId`

        - `long startPageNumber`

          minimum: 1

        - `JsonValue type = "page_location"`

      - `class CitationContentBlockLocation:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `Optional<String> fileId`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `JsonValue type = "content_block_location"`

      - `class CitationsWebSearchResultLocation:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

          maxLength: 512

        - `JsonValue type = "web_search_result_location"`

        - `String url`

      - `class CitationsSearchResultLocation:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long searchResultIndex`

          0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

          Counted separately from `document_index`; server-side web search results are not included in this count.

          minimum: 0

        - `String source`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `Optional<String> title`

        - `JsonValue type = "search_result_location"`

    - `JsonValue type = "citations_delta"`

  - `class ThinkingDelta:`

    - `String thinking`

      The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

    - `JsonValue type = "thinking_delta"`

  - `class SignatureDelta:`

    - `String signature`

      The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

    - `JsonValue type = "signature_delta"`

### Raw Content Block Delta Event

- `class RawContentBlockDeltaEvent:`

  - `RawContentBlockDelta delta`

    - `class TextDelta:`

      - `String text`

      - `JsonValue type = "text_delta"`

    - `class InputJsonDelta:`

      - `String partialJson`

      - `JsonValue type = "input_json_delta"`

    - `class CitationsDelta:`

      - `Citation citation`

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

            minimum: 0

          - `JsonValue type = "char_location"`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

            minimum: 1

          - `JsonValue type = "page_location"`

        - `class CitationContentBlockLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `Optional<String> fileId`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `JsonValue type = "content_block_location"`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

            maxLength: 512

          - `JsonValue type = "web_search_result_location"`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `long searchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `String source`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `Optional<String> title`

          - `JsonValue type = "search_result_location"`

      - `JsonValue type = "citations_delta"`

    - `class ThinkingDelta:`

      - `String thinking`

        The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

      - `JsonValue type = "thinking_delta"`

    - `class SignatureDelta:`

      - `String signature`

        The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

      - `JsonValue type = "signature_delta"`

  - `long index`

  - `JsonValue type = "content_block_delta"`

### Raw Content Block Start Event

- `class RawContentBlockStartEvent:`

  - `ContentBlock contentBlock`

    Response model for a file uploaded to the container.

    - `class TextBlock:`

      - `Optional<List<TextCitation>> citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endCharIndex`

          - `Optional<String> fileId`

          - `long startCharIndex`

            minimum: 0

          - `JsonValue type = "char_location"`

        - `class CitationPageLocation:`

          - `String citedText`

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endPageNumber`

          - `Optional<String> fileId`

          - `long startPageNumber`

            minimum: 1

          - `JsonValue type = "page_location"`

        - `class CitationContentBlockLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long documentIndex`

            minimum: 0

          - `Optional<String> documentTitle`

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `Optional<String> fileId`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `JsonValue type = "content_block_location"`

        - `class CitationsWebSearchResultLocation:`

          - `String citedText`

          - `String encryptedIndex`

          - `Optional<String> title`

            maxLength: 512

          - `JsonValue type = "web_search_result_location"`

          - `String url`

        - `class CitationsSearchResultLocation:`

          - `String citedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `long endBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `long searchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `String source`

          - `long startBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `Optional<String> title`

          - `JsonValue type = "search_result_location"`

      - `String text`

        maxLength: 5000000, minLength: 0

      - `JsonValue type = "text"`

    - `class ThinkingBlock:`

      - `String signature`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `String thinking`

        The text of Claude's thinking process for this block.

      - `JsonValue type = "thinking"`

    - `class RedactedThinkingBlock:`

      - `String data`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `JsonValue type = "redacted_thinking"`

    - `class ToolUseBlock:`

      - `String id`

        pattern: ^[a-zA-Z0-9_-]+$

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonValue type = "direct"`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `String toolId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_20250825"`

        - `class ServerToolCaller20260120:`

          - `String toolId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_20260120"`

      - `Input input`

      - `String name`

        minLength: 1

      - `JsonValue type = "tool_use"`

      - `Optional<String> toolsetName`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock:`

      - `String id`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `Input input`

      - `Name name`

        - `WEB_SEARCH("web_search")`

        - `WEB_FETCH("web_fetch")`

        - `CODE_EXECUTION("code_execution")`

        - `BASH_CODE_EXECUTION("bash_code_execution")`

        - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

        - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

        - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

      - `JsonValue type = "server_tool_use"`

    - `class WebSearchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `WebSearchToolResultBlockContent content`

        - `class WebSearchToolResultError:`

          - `WebSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `QUERY_TOO_LONG("query_too_long")`

            - `REQUEST_TOO_LARGE("request_too_large")`

          - `JsonValue type = "web_search_tool_result_error"`

        - `List<WebSearchResultBlock>`

          - `String encryptedContent`

          - `Optional<String> pageAge`

          - `String title`

          - `JsonValue type = "web_search_result"`

          - `String url`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "web_search_tool_result"`

    - `class WebFetchToolResultBlock:`

      - `Caller caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `Content content`

        - `class WebFetchToolResultErrorBlock:`

          - `WebFetchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `URL_TOO_LONG("url_too_long")`

            - `URL_NOT_ALLOWED("url_not_allowed")`

            - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

            - `URL_NOT_ACCESSIBLE("url_not_accessible")`

            - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `MAX_USES_EXCEEDED("max_uses_exceeded")`

            - `UNAVAILABLE("unavailable")`

          - `JsonValue type = "web_fetch_tool_result_error"`

        - `class WebFetchBlock:`

          - `DocumentBlock content`

            - `Optional<CitationsConfig> citations`

              Citation configuration for the document

              - `boolean enabled`

            - `Source source`

              - `class Base64PdfSource:`

                - `String data`

                  format: byte

                - `JsonValue mediaType = "application/pdf"`

                - `JsonValue type = "base64"`

              - `class PlainTextSource:`

                - `String data`

                - `JsonValue mediaType = "text/plain"`

                - `JsonValue type = "text"`

            - `Optional<String> title`

              The title of the document

            - `JsonValue type = "document"`

          - `Optional<String> retrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonValue type = "web_fetch_result"`

          - `String url`

            Fetched content URL

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "web_fetch_tool_result"`

    - `class CodeExecutionToolResultBlock:`

      - `CodeExecutionToolResultBlockContent content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `CodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `JsonValue type = "code_execution_tool_result_error"`

        - `class CodeExecutionResultBlock:`

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "code_execution_output"`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue type = "code_execution_result"`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `List<CodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "code_execution_output"`

          - `String encryptedStdout`

          - `long returnCode`

          - `String stderr`

          - `JsonValue type = "encrypted_code_execution_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_tool_result"`

    - `class BashCodeExecutionToolResultBlock:`

      - `Content content`

        - `class BashCodeExecutionToolResultError:`

          - `BashCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

          - `JsonValue type = "bash_code_execution_tool_result_error"`

        - `class BashCodeExecutionResultBlock:`

          - `List<BashCodeExecutionOutputBlock> content`

            - `String fileId`

            - `JsonValue type = "bash_code_execution_output"`

          - `long returnCode`

          - `String stderr`

          - `String stdout`

          - `JsonValue type = "bash_code_execution_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "bash_code_execution_tool_result"`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `Content content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `TextEditorCodeExecutionToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `FILE_NOT_FOUND("file_not_found")`

          - `Optional<String> errorMessage`

          - `JsonValue type = "text_editor_code_execution_tool_result_error"`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `String content`

          - `FileType fileType`

            - `TEXT("text")`

            - `IMAGE("image")`

            - `PDF("pdf")`

          - `Optional<Long> numLines`

          - `Optional<Long> startLine`

          - `Optional<Long> totalLines`

          - `JsonValue type = "text_editor_code_execution_view_result"`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `boolean isFileUpdate`

          - `JsonValue type = "text_editor_code_execution_create_result"`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `Optional<List<String>> lines`

          - `Optional<Long> newLines`

          - `Optional<Long> newStart`

          - `Optional<Long> oldLines`

          - `Optional<Long> oldStart`

          - `JsonValue type = "text_editor_code_execution_str_replace_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "text_editor_code_execution_tool_result"`

    - `class ToolSearchToolResultBlock:`

      - `Content content`

        - `class ToolSearchToolResultError:`

          - `ToolSearchToolResultErrorCode errorCode`

            - `INVALID_TOOL_INPUT("invalid_tool_input")`

            - `UNAVAILABLE("unavailable")`

            - `TOO_MANY_REQUESTS("too_many_requests")`

            - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

          - `Optional<String> errorMessage`

          - `JsonValue type = "tool_search_tool_result_error"`

        - `class ToolSearchToolSearchResultBlock:`

          - `List<ToolReferenceBlock> toolReferences`

            - `String toolName`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `JsonValue type = "tool_reference"`

          - `JsonValue type = "tool_search_tool_search_result"`

      - `String toolUseId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "tool_search_tool_result"`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `String fileId`

      - `JsonValue type = "container_upload"`

  - `long index`

  - `JsonValue type = "content_block_start"`

### Raw Content Block Stop Event

- `class RawContentBlockStopEvent:`

  - `long index`

  - `JsonValue type = "content_block_stop"`

### Raw Message Delta Event

- `class RawMessageDeltaEvent:`

  - `Delta delta`

    - `Optional<Container> container`

      Information about the container used in the request (for the code execution tool)

      - `String id`

        Identifier for the container used in this request

      - `LocalDateTime expiresAt`

        The time at which the container will expire.

        format: date-time

      - `Optional<List<ContainerSkill>> skills`

        Skills loaded in the container

        - `String skillId`

          Skill ID

          maxLength: 64, minLength: 1

        - `Type type`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `ANTHROPIC("anthropic")`

          - `CUSTOM("custom")`

        - `String version`

          The resolved version: a skill version ID for custom skills.

          maxLength: 64, minLength: 1

    - `Optional<RefusalStopDetails> stopDetails`

      Structured information about a refusal.

      - `Optional<Category> category`

        The policy category that triggered a refusal.

        - `CYBER("cyber")`

          The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

        - `BIO("bio")`

          The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

        - `FRONTIER_LLM("frontier_llm")`

          The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

        - `REASONING_EXTRACTION("reasoning_extraction")`

          The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

        - `GENERAL_HARMS("general_harms")`

          The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

      - `Optional<String> explanation`

        Human-readable explanation of the refusal.

        This text is not guaranteed to be stable. `null` when no explanation is available for the category.

      - `JsonValue type = "refusal"`

    - `Optional<StopReason> stopReason`

      - `END_TURN("end_turn")`

      - `MAX_TOKENS("max_tokens")`

      - `STOP_SEQUENCE("stop_sequence")`

      - `TOOL_USE("tool_use")`

      - `PAUSE_TURN("pause_turn")`

      - `REFUSAL("refusal")`

      - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

    - `Optional<String> stopSequence`

  - `JsonValue type = "message_delta"`

  - `MessageDeltaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `Optional<Long> cacheCreationInputTokens`

      The cumulative number of input tokens used to create the cache entry.

      minimum: 0

    - `Optional<Long> cacheReadInputTokens`

      The cumulative number of input tokens read from the cache.

      minimum: 0

    - `Optional<Long> inputTokens`

      The cumulative number of input tokens which were used.

      minimum: 0

    - `long outputTokens`

      The cumulative number of output tokens which were used.

    - `Optional<OutputTokensDetails> outputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `long thinkingTokens`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `Optional<ServerToolUsage> serverToolUse`

      The number of server tool requests.

      - `long webFetchRequests`

        The number of web fetch tool requests.

        minimum: 0

      - `long webSearchRequests`

        The number of web search tool requests.

        minimum: 0

### Raw Message Start Event

- `class RawMessageStartEvent:`

  - `Message message`

    - `String id`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `Optional<Container> container`

      Information about the container used in the request (for the code execution tool)

      - `String id`

        Identifier for the container used in this request

      - `LocalDateTime expiresAt`

        The time at which the container will expire.

        format: date-time

      - `Optional<List<ContainerSkill>> skills`

        Skills loaded in the container

        - `String skillId`

          Skill ID

          maxLength: 64, minLength: 1

        - `Type type`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `ANTHROPIC("anthropic")`

          - `CUSTOM("custom")`

        - `String version`

          The resolved version: a skill version ID for custom skills.

          maxLength: 64, minLength: 1

    - `List<ContentBlock> content`

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

      - `class TextBlock:`

        - `Optional<List<TextCitation>> citations`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class CitationCharLocation:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `Optional<String> fileId`

            - `long startCharIndex`

              minimum: 0

            - `JsonValue type = "char_location"`

          - `class CitationPageLocation:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `Optional<String> fileId`

            - `long startPageNumber`

              minimum: 1

            - `JsonValue type = "page_location"`

          - `class CitationContentBlockLocation:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `Optional<String> fileId`

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `JsonValue type = "content_block_location"`

          - `class CitationsWebSearchResultLocation:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

              maxLength: 512

            - `JsonValue type = "web_search_result_location"`

            - `String url`

          - `class CitationsSearchResultLocation:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long searchResultIndex`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `String source`

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `Optional<String> title`

            - `JsonValue type = "search_result_location"`

        - `String text`

          maxLength: 5000000, minLength: 0

        - `JsonValue type = "text"`

      - `class ThinkingBlock:`

        - `String signature`

          A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

          This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `String thinking`

          The text of Claude's thinking process for this block.

        - `JsonValue type = "thinking"`

      - `class RedactedThinkingBlock:`

        - `String data`

          The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

          Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

        - `JsonValue type = "redacted_thinking"`

      - `class ToolUseBlock:`

        - `String id`

          pattern: ^[a-zA-Z0-9_-]+$

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue type = "direct"`

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "code_execution_20250825"`

          - `class ServerToolCaller20260120:`

            - `String toolId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "code_execution_20260120"`

        - `Input input`

        - `String name`

          minLength: 1

        - `JsonValue type = "tool_use"`

        - `Optional<String> toolsetName`

          For a toolset member tool_use, the toolset family.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class ServerToolUseBlock:`

        - `String id`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120:`

        - `Input input`

        - `Name name`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue type = "server_tool_use"`

      - `class WebSearchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120:`

        - `WebSearchToolResultBlockContent content`

          - `class WebSearchToolResultError:`

            - `WebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue type = "web_search_tool_result_error"`

          - `List<WebSearchResultBlock>`

            - `String encryptedContent`

            - `Optional<String> pageAge`

            - `String title`

            - `JsonValue type = "web_search_result"`

            - `String url`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "web_search_tool_result"`

      - `class WebFetchToolResultBlock:`

        - `Caller caller`

          Tool invocation directly from the model.

          - `class DirectCaller:`

            Tool invocation directly from the model.

          - `class ServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class ServerToolCaller20260120:`

        - `Content content`

          - `class WebFetchToolResultErrorBlock:`

            - `WebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue type = "web_fetch_tool_result_error"`

          - `class WebFetchBlock:`

            - `DocumentBlock content`

              - `Optional<CitationsConfig> citations`

                Citation configuration for the document

                - `boolean enabled`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                    format: byte

                  - `JsonValue mediaType = "application/pdf"`

                  - `JsonValue type = "base64"`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue mediaType = "text/plain"`

                  - `JsonValue type = "text"`

              - `Optional<String> title`

                The title of the document

              - `JsonValue type = "document"`

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

            - `JsonValue type = "web_fetch_result"`

            - `String url`

              Fetched content URL

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "web_fetch_tool_result"`

      - `class CodeExecutionToolResultBlock:`

        - `CodeExecutionToolResultBlockContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class CodeExecutionToolResultError:`

            - `CodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue type = "code_execution_tool_result_error"`

          - `class CodeExecutionResultBlock:`

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue type = "code_execution_output"`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue type = "code_execution_result"`

          - `class EncryptedCodeExecutionResultBlock:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<CodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue type = "code_execution_output"`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue type = "encrypted_code_execution_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "code_execution_tool_result"`

      - `class BashCodeExecutionToolResultBlock:`

        - `Content content`

          - `class BashCodeExecutionToolResultError:`

            - `BashCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue type = "bash_code_execution_tool_result_error"`

          - `class BashCodeExecutionResultBlock:`

            - `List<BashCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue type = "bash_code_execution_output"`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue type = "bash_code_execution_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "bash_code_execution_tool_result"`

      - `class TextEditorCodeExecutionToolResultBlock:`

        - `Content content`

          - `class TextEditorCodeExecutionToolResultError:`

            - `TextEditorCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `Optional<String> errorMessage`

            - `JsonValue type = "text_editor_code_execution_tool_result_error"`

          - `class TextEditorCodeExecutionViewResultBlock:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

            - `JsonValue type = "text_editor_code_execution_view_result"`

          - `class TextEditorCodeExecutionCreateResultBlock:`

            - `boolean isFileUpdate`

            - `JsonValue type = "text_editor_code_execution_create_result"`

          - `class TextEditorCodeExecutionStrReplaceResultBlock:`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

            - `JsonValue type = "text_editor_code_execution_str_replace_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "text_editor_code_execution_tool_result"`

      - `class ToolSearchToolResultBlock:`

        - `Content content`

          - `class ToolSearchToolResultError:`

            - `ToolSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `Optional<String> errorMessage`

            - `JsonValue type = "tool_search_tool_result_error"`

          - `class ToolSearchToolSearchResultBlock:`

            - `List<ToolReferenceBlock> toolReferences`

              - `String toolName`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `JsonValue type = "tool_reference"`

            - `JsonValue type = "tool_search_tool_search_result"`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type = "tool_search_tool_result"`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

        - `String fileId`

        - `JsonValue type = "container_upload"`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

        Our most capable model for cybersecurity and biology research, available through trusted access programs

      - `CLAUDE_SONNET_5("claude-sonnet-5")`

        High-performance model for coding and agents

      - `CLAUDE_FABLE_5("claude-fable-5")`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `CLAUDE_MYTHOS_5("claude-mythos-5")`

        Most capable model for cybersecurity and biology research

      - `CLAUDE_OPUS_5("claude-opus-5")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

        New class of intelligence, strongest in coding and cybersecurity

      - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

        Best combination of speed and intelligence

      - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

        Fastest model with near-frontier intelligence

      - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

        Fastest model with near-frontier intelligence

      - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

        High-performance model for agents and coding

      - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

        High-performance model for agents and coding

    - `JsonValue role = "assistant"`

      Conversational role of the generated message.

      This will always be `"assistant"`.

    - `Optional<RefusalStopDetails> stopDetails`

      Structured information about a refusal.

      - `Optional<Category> category`

        The policy category that triggered a refusal.

        - `CYBER("cyber")`

          The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

        - `BIO("bio")`

          The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

        - `FRONTIER_LLM("frontier_llm")`

          The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

        - `REASONING_EXTRACTION("reasoning_extraction")`

          The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

        - `GENERAL_HARMS("general_harms")`

          The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

      - `Optional<String> explanation`

        Human-readable explanation of the refusal.

        This text is not guaranteed to be stable. `null` when no explanation is available for the category.

      - `JsonValue type = "refusal"`

    - `Optional<StopReason> stopReason`

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

      - `END_TURN("end_turn")`

      - `MAX_TOKENS("max_tokens")`

      - `STOP_SEQUENCE("stop_sequence")`

      - `TOOL_USE("tool_use")`

      - `PAUSE_TURN("pause_turn")`

      - `REFUSAL("refusal")`

      - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

    - `Optional<String> stopSequence`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `JsonValue type = "message"`

      Object type.

      For Messages, this is always `"message"`.

    - `Usage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<CacheCreation> cacheCreation`

        Breakdown of cached tokens by TTL

        - `long ephemeral1hInputTokens`

          The number of input tokens used to create the 1 hour cache entry.

          minimum: 0

        - `long ephemeral5mInputTokens`

          The number of input tokens used to create the 5 minute cache entry.

          minimum: 0

      - `Optional<Long> cacheCreationInputTokens`

        The number of input tokens used to create the cache entry.

        minimum: 0

      - `Optional<Long> cacheReadInputTokens`

        The number of input tokens read from the cache.

        minimum: 0

      - `Optional<String> inferenceGeo`

        The geographic region where inference was performed for this request.

      - `long inputTokens`

        The number of input tokens which were used.

        minimum: 0

      - `long outputTokens`

        The number of output tokens which were used.

        minimum: 0

      - `Optional<OutputTokensDetails> outputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

        - `long thinkingTokens`

          Number of output tokens the model generated as internal reasoning, including
          the thinking-block delimiter tokens.

          Reflects the raw reasoning the model produced, not the (possibly shorter)
          summarized thinking text returned in the response body. Computed by
          re-tokenizing the raw reasoning text, so it may differ from the model's exact
          generation count by a small number of tokens. Always ≤ `output_tokens`;
          `output_tokens - thinking_tokens` approximates the non-reasoning output.

          minimum: 0

      - `Optional<ServerToolUsage> serverToolUse`

        The number of server tool requests.

        - `long webFetchRequests`

          The number of web fetch tool requests.

          minimum: 0

        - `long webSearchRequests`

          The number of web search tool requests.

          minimum: 0

      - `Optional<ServiceTier> serviceTier`

        If the request used the priority, standard, or batch tier.

        - `STANDARD("standard")`

        - `PRIORITY("priority")`

        - `BATCH("batch")`

  - `JsonValue type = "message_start"`

### Raw Message Stop Event

- `class RawMessageStopEvent:`

  - `JsonValue type = "message_stop"`

### Raw Message Stream Event

- `class RawMessageStreamEvent: union`

  - `class RawMessageStartEvent:`

    - `Message message`

      - `String id`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `Optional<Container> container`

        Information about the container used in the request (for the code execution tool)

        - `String id`

          Identifier for the container used in this request

        - `LocalDateTime expiresAt`

          The time at which the container will expire.

          format: date-time

        - `Optional<List<ContainerSkill>> skills`

          Skills loaded in the container

          - `String skillId`

            Skill ID

            maxLength: 64, minLength: 1

          - `Type type`

            Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

            - `ANTHROPIC("anthropic")`

            - `CUSTOM("custom")`

          - `String version`

            The resolved version: a skill version ID for custom skills.

            maxLength: 64, minLength: 1

      - `List<ContentBlock> content`

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

        - `class TextBlock:`

          - `Optional<List<TextCitation>> citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class CitationCharLocation:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `Optional<String> fileId`

              - `long startCharIndex`

                minimum: 0

              - `JsonValue type = "char_location"`

            - `class CitationPageLocation:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `Optional<String> fileId`

              - `long startPageNumber`

                minimum: 1

              - `JsonValue type = "page_location"`

            - `class CitationContentBlockLocation:`

              - `String citedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

              - `long endBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `Optional<String> fileId`

              - `long startBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `JsonValue type = "content_block_location"`

            - `class CitationsWebSearchResultLocation:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

                maxLength: 512

              - `JsonValue type = "web_search_result_location"`

              - `String url`

            - `class CitationsSearchResultLocation:`

              - `String citedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `long endBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `long searchResultIndex`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

                minimum: 0

              - `String source`

              - `long startBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `Optional<String> title`

              - `JsonValue type = "search_result_location"`

          - `String text`

            maxLength: 5000000, minLength: 0

          - `JsonValue type = "text"`

        - `class ThinkingBlock:`

          - `String signature`

            A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

            This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

          - `String thinking`

            The text of Claude's thinking process for this block.

          - `JsonValue type = "thinking"`

        - `class RedactedThinkingBlock:`

          - `String data`

            The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

            Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `JsonValue type = "redacted_thinking"`

        - `class ToolUseBlock:`

          - `String id`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue type = "direct"`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_20250825"`

            - `class ServerToolCaller20260120:`

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_20260120"`

          - `Input input`

          - `String name`

            minLength: 1

          - `JsonValue type = "tool_use"`

          - `Optional<String> toolsetName`

            For a toolset member tool_use, the toolset family.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ServerToolUseBlock:`

          - `String id`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

          - `Input input`

          - `Name name`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue type = "server_tool_use"`

        - `class WebSearchToolResultBlock:`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

          - `WebSearchToolResultBlockContent content`

            - `class WebSearchToolResultError:`

              - `WebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue type = "web_search_tool_result_error"`

            - `List<WebSearchResultBlock>`

              - `String encryptedContent`

              - `Optional<String> pageAge`

              - `String title`

              - `JsonValue type = "web_search_result"`

              - `String url`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "web_search_tool_result"`

        - `class WebFetchToolResultBlock:`

          - `Caller caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

          - `Content content`

            - `class WebFetchToolResultErrorBlock:`

              - `WebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue type = "web_fetch_tool_result_error"`

            - `class WebFetchBlock:`

              - `DocumentBlock content`

                - `Optional<CitationsConfig> citations`

                  Citation configuration for the document

                  - `boolean enabled`

                - `Source source`

                  - `class Base64PdfSource:`

                    - `String data`

                      format: byte

                    - `JsonValue mediaType = "application/pdf"`

                    - `JsonValue type = "base64"`

                  - `class PlainTextSource:`

                    - `String data`

                    - `JsonValue mediaType = "text/plain"`

                    - `JsonValue type = "text"`

                - `Optional<String> title`

                  The title of the document

                - `JsonValue type = "document"`

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

              - `JsonValue type = "web_fetch_result"`

              - `String url`

                Fetched content URL

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "web_fetch_tool_result"`

        - `class CodeExecutionToolResultBlock:`

          - `CodeExecutionToolResultBlockContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultError:`

              - `CodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue type = "code_execution_tool_result_error"`

            - `class CodeExecutionResultBlock:`

              - `List<CodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue type = "code_execution_output"`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type = "code_execution_result"`

            - `class EncryptedCodeExecutionResultBlock:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<CodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue type = "code_execution_output"`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue type = "encrypted_code_execution_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "code_execution_tool_result"`

        - `class BashCodeExecutionToolResultBlock:`

          - `Content content`

            - `class BashCodeExecutionToolResultError:`

              - `BashCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue type = "bash_code_execution_tool_result_error"`

            - `class BashCodeExecutionResultBlock:`

              - `List<BashCodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue type = "bash_code_execution_output"`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type = "bash_code_execution_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "bash_code_execution_tool_result"`

        - `class TextEditorCodeExecutionToolResultBlock:`

          - `Content content`

            - `class TextEditorCodeExecutionToolResultError:`

              - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `Optional<String> errorMessage`

              - `JsonValue type = "text_editor_code_execution_tool_result_error"`

            - `class TextEditorCodeExecutionViewResultBlock:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

              - `JsonValue type = "text_editor_code_execution_view_result"`

            - `class TextEditorCodeExecutionCreateResultBlock:`

              - `boolean isFileUpdate`

              - `JsonValue type = "text_editor_code_execution_create_result"`

            - `class TextEditorCodeExecutionStrReplaceResultBlock:`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

              - `JsonValue type = "text_editor_code_execution_str_replace_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "text_editor_code_execution_tool_result"`

        - `class ToolSearchToolResultBlock:`

          - `Content content`

            - `class ToolSearchToolResultError:`

              - `ToolSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `Optional<String> errorMessage`

              - `JsonValue type = "tool_search_tool_result_error"`

            - `class ToolSearchToolSearchResultBlock:`

              - `List<ToolReferenceBlock> toolReferences`

                - `String toolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonValue type = "tool_reference"`

              - `JsonValue type = "tool_search_tool_search_result"`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type = "tool_search_tool_result"`

        - `class ContainerUploadBlock:`

          Response model for a file uploaded to the container.

          - `String fileId`

          - `JsonValue type = "container_upload"`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

          Our most capable model for cybersecurity and biology research, available through trusted access programs

        - `CLAUDE_SONNET_5("claude-sonnet-5")`

          High-performance model for coding and agents

        - `CLAUDE_FABLE_5("claude-fable-5")`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `CLAUDE_MYTHOS_5("claude-mythos-5")`

          Most capable model for cybersecurity and biology research

        - `CLAUDE_OPUS_5("claude-opus-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

          New class of intelligence, strongest in coding and cybersecurity

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `JsonValue role = "assistant"`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `Optional<RefusalStopDetails> stopDetails`

        Structured information about a refusal.

        - `Optional<Category> category`

          The policy category that triggered a refusal.

          - `CYBER("cyber")`

            The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

          - `BIO("bio")`

            The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

          - `FRONTIER_LLM("frontier_llm")`

            The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

          - `REASONING_EXTRACTION("reasoning_extraction")`

            The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

          - `GENERAL_HARMS("general_harms")`

            The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

        - `Optional<String> explanation`

          Human-readable explanation of the refusal.

          This text is not guaranteed to be stable. `null` when no explanation is available for the category.

        - `JsonValue type = "refusal"`

      - `Optional<StopReason> stopReason`

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

        - `END_TURN("end_turn")`

        - `MAX_TOKENS("max_tokens")`

        - `STOP_SEQUENCE("stop_sequence")`

        - `TOOL_USE("tool_use")`

        - `PAUSE_TURN("pause_turn")`

        - `REFUSAL("refusal")`

        - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

      - `Optional<String> stopSequence`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `JsonValue type = "message"`

        Object type.

        For Messages, this is always `"message"`.

      - `Usage usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `Optional<CacheCreation> cacheCreation`

          Breakdown of cached tokens by TTL

          - `long ephemeral1hInputTokens`

            The number of input tokens used to create the 1 hour cache entry.

            minimum: 0

          - `long ephemeral5mInputTokens`

            The number of input tokens used to create the 5 minute cache entry.

            minimum: 0

        - `Optional<Long> cacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `Optional<Long> cacheReadInputTokens`

          The number of input tokens read from the cache.

          minimum: 0

        - `Optional<String> inferenceGeo`

          The geographic region where inference was performed for this request.

        - `long inputTokens`

          The number of input tokens which were used.

          minimum: 0

        - `long outputTokens`

          The number of output tokens which were used.

          minimum: 0

        - `Optional<OutputTokensDetails> outputTokensDetails`

          Breakdown of output tokens by category.

          `output_tokens` remains the inclusive, authoritative total used for billing.
          This object provides a read-only decomposition for observability — for example,
          how many of the billed output tokens were spent on internal reasoning that may
          have been summarized before being returned to you.

          - `long thinkingTokens`

            Number of output tokens the model generated as internal reasoning, including
            the thinking-block delimiter tokens.

            Reflects the raw reasoning the model produced, not the (possibly shorter)
            summarized thinking text returned in the response body. Computed by
            re-tokenizing the raw reasoning text, so it may differ from the model's exact
            generation count by a small number of tokens. Always ≤ `output_tokens`;
            `output_tokens - thinking_tokens` approximates the non-reasoning output.

            minimum: 0

        - `Optional<ServerToolUsage> serverToolUse`

          The number of server tool requests.

          - `long webFetchRequests`

            The number of web fetch tool requests.

            minimum: 0

          - `long webSearchRequests`

            The number of web search tool requests.

            minimum: 0

        - `Optional<ServiceTier> serviceTier`

          If the request used the priority, standard, or batch tier.

          - `STANDARD("standard")`

          - `PRIORITY("priority")`

          - `BATCH("batch")`

    - `JsonValue type = "message_start"`

  - `class RawMessageDeltaEvent:`

    - `Delta delta`

      - `Optional<Container> container`

        Information about the container used in the request (for the code execution tool)

      - `Optional<RefusalStopDetails> stopDetails`

        Structured information about a refusal.

      - `Optional<StopReason> stopReason`

      - `Optional<String> stopSequence`

    - `JsonValue type = "message_delta"`

    - `MessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<Long> cacheCreationInputTokens`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `Optional<Long> cacheReadInputTokens`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `Optional<Long> inputTokens`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `long outputTokens`

        The cumulative number of output tokens which were used.

      - `Optional<OutputTokensDetails> outputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `Optional<ServerToolUsage> serverToolUse`

        The number of server tool requests.

  - `class RawMessageStopEvent:`

    - `JsonValue type = "message_stop"`

  - `class RawContentBlockStartEvent:`

    - `ContentBlock contentBlock`

      Response model for a file uploaded to the container.

      - `class TextBlock:`

      - `class ThinkingBlock:`

      - `class RedactedThinkingBlock:`

      - `class ToolUseBlock:`

      - `class ServerToolUseBlock:`

      - `class WebSearchToolResultBlock:`

      - `class WebFetchToolResultBlock:`

      - `class CodeExecutionToolResultBlock:`

      - `class BashCodeExecutionToolResultBlock:`

      - `class TextEditorCodeExecutionToolResultBlock:`

      - `class ToolSearchToolResultBlock:`

      - `class ContainerUploadBlock:`

        Response model for a file uploaded to the container.

    - `long index`

    - `JsonValue type = "content_block_start"`

  - `class RawContentBlockDeltaEvent:`

    - `RawContentBlockDelta delta`

      - `class TextDelta:`

        - `String text`

        - `JsonValue type = "text_delta"`

      - `class InputJsonDelta:`

        - `String partialJson`

        - `JsonValue type = "input_json_delta"`

      - `class CitationsDelta:`

        - `Citation citation`

          - `class CitationCharLocation:`

          - `class CitationPageLocation:`

          - `class CitationContentBlockLocation:`

          - `class CitationsWebSearchResultLocation:`

          - `class CitationsSearchResultLocation:`

        - `JsonValue type = "citations_delta"`

      - `class ThinkingDelta:`

        - `String thinking`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `JsonValue type = "thinking_delta"`

      - `class SignatureDelta:`

        - `String signature`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `JsonValue type = "signature_delta"`

    - `long index`

    - `JsonValue type = "content_block_delta"`

  - `class RawContentBlockStopEvent:`

    - `long index`

    - `JsonValue type = "content_block_stop"`

### Redacted Thinking Block

- `class RedactedThinkingBlock:`

  - `String data`

    The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

    Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

  - `JsonValue type = "redacted_thinking"`

### Redacted Thinking Block Param

- `class RedactedThinkingBlockParam:`

  - `String data`

    The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

  - `JsonValue type = "redacted_thinking"`

### Refusal Stop Details

- `class RefusalStopDetails:`

  Structured information about a refusal.

  - `Optional<Category> category`

    The policy category that triggered a refusal.

    - `CYBER("cyber")`

      The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

    - `BIO("bio")`

      The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

    - `FRONTIER_LLM("frontier_llm")`

      The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

    - `REASONING_EXTRACTION("reasoning_extraction")`

      The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

    - `GENERAL_HARMS("general_harms")`

      The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

  - `Optional<String> explanation`

    Human-readable explanation of the refusal.

    This text is not guaranteed to be stable. `null` when no explanation is available for the category.

  - `JsonValue type = "refusal"`

### Search Result Block Param

- `class SearchResultBlockParam:`

  - `List<TextBlockParam> content`

    - `String text`

      minLength: 1

    - `JsonValue type = "text"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue type = "ephemeral"`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<List<TextCitationParam>> citations`

      - `class CitationCharLocationParam:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endCharIndex`

        - `long startCharIndex`

          minimum: 0

        - `JsonValue type = "char_location"`

      - `class CitationPageLocationParam:`

        - `String citedText`

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endPageNumber`

        - `long startPageNumber`

          minimum: 1

        - `JsonValue type = "page_location"`

      - `class CitationContentBlockLocationParam:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long documentIndex`

          minimum: 0

        - `Optional<String> documentTitle`

          maxLength: 500, minLength: 1

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `JsonValue type = "content_block_location"`

      - `class CitationWebSearchResultLocationParam:`

        - `String citedText`

        - `String encryptedIndex`

        - `Optional<String> title`

          maxLength: 512, minLength: 1

        - `JsonValue type = "web_search_result_location"`

        - `String url`

          minLength: 1

      - `class CitationSearchResultLocationParam:`

        - `String citedText`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `long endBlockIndex`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `long searchResultIndex`

          0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

          Counted separately from `document_index`; server-side web search results are not included in this count.

          minimum: 0

        - `String source`

        - `long startBlockIndex`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `Optional<String> title`

        - `JsonValue type = "search_result_location"`

  - `String source`

  - `String title`

  - `JsonValue type = "search_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

  - `Optional<CitationsConfigParam> citations`

    - `Optional<Boolean> enabled`

### Server Tool Caller

- `class ServerToolCaller:`

  Tool invocation generated by a server-side tool.

  - `String toolId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "code_execution_20250825"`

### Server Tool Caller 20260120

- `class ServerToolCaller20260120:`

  - `String toolId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "code_execution_20260120"`

### Server Tool Usage

- `class ServerToolUsage:`

  - `long webFetchRequests`

    The number of web fetch tool requests.

    minimum: 0

  - `long webSearchRequests`

    The number of web search tool requests.

    minimum: 0

### Server Tool Use Block

- `class ServerToolUseBlock:`

  - `String id`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

  - `Input input`

  - `Name name`

    - `WEB_SEARCH("web_search")`

    - `WEB_FETCH("web_fetch")`

    - `CODE_EXECUTION("code_execution")`

    - `BASH_CODE_EXECUTION("bash_code_execution")`

    - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `JsonValue type = "server_tool_use"`

### Server Tool Use Block Param

- `class ServerToolUseBlockParam:`

  - `String id`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `Input input`

  - `Name name`

    - `WEB_SEARCH("web_search")`

    - `WEB_FETCH("web_fetch")`

    - `CODE_EXECUTION("code_execution")`

    - `BASH_CODE_EXECUTION("bash_code_execution")`

    - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `JsonValue type = "server_tool_use"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

### Signature Delta

- `class SignatureDelta:`

  - `String signature`

    The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

  - `JsonValue type = "signature_delta"`

### Skill Params

- `class SkillParams:`

  Specification for a skill to be loaded in a container (request model).

  - `String skillId`

    Skill ID

    maxLength: 64, minLength: 1

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

    - `ANTHROPIC("anthropic")`

    - `CUSTOM("custom")`

  - `Optional<String> version`

    Skill version or 'latest' for most recent version

    maxLength: 64, minLength: 1

### Stop Reason

- `enum StopReason:`

  - `END_TURN("end_turn")`

  - `MAX_TOKENS("max_tokens")`

  - `STOP_SEQUENCE("stop_sequence")`

  - `TOOL_USE("tool_use")`

  - `PAUSE_TURN("pause_turn")`

  - `REFUSAL("refusal")`

  - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

### Text Block

- `class TextBlock:`

  - `Optional<List<TextCitation>> citations`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `class CitationCharLocation:`

      - `String citedText`

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

      - `long endCharIndex`

      - `Optional<String> fileId`

      - `long startCharIndex`

        minimum: 0

      - `JsonValue type = "char_location"`

    - `class CitationPageLocation:`

      - `String citedText`

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

      - `long endPageNumber`

      - `Optional<String> fileId`

      - `long startPageNumber`

        minimum: 1

      - `JsonValue type = "page_location"`

    - `class CitationContentBlockLocation:`

      - `String citedText`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

      - `long endBlockIndex`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `Optional<String> fileId`

      - `long startBlockIndex`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `JsonValue type = "content_block_location"`

    - `class CitationsWebSearchResultLocation:`

      - `String citedText`

      - `String encryptedIndex`

      - `Optional<String> title`

        maxLength: 512

      - `JsonValue type = "web_search_result_location"`

      - `String url`

    - `class CitationsSearchResultLocation:`

      - `String citedText`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `long endBlockIndex`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `long searchResultIndex`

        0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

        Counted separately from `document_index`; server-side web search results are not included in this count.

        minimum: 0

      - `String source`

      - `long startBlockIndex`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `Optional<String> title`

      - `JsonValue type = "search_result_location"`

  - `String text`

    maxLength: 5000000, minLength: 0

  - `JsonValue type = "text"`

### Text Block Param

- `class TextBlockParam:`

  - `String text`

    minLength: 1

  - `JsonValue type = "text"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<List<TextCitationParam>> citations`

    - `class CitationCharLocationParam:`

      - `String citedText`

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

        maxLength: 500, minLength: 1

      - `long endCharIndex`

      - `long startCharIndex`

        minimum: 0

      - `JsonValue type = "char_location"`

    - `class CitationPageLocationParam:`

      - `String citedText`

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

        maxLength: 500, minLength: 1

      - `long endPageNumber`

      - `long startPageNumber`

        minimum: 1

      - `JsonValue type = "page_location"`

    - `class CitationContentBlockLocationParam:`

      - `String citedText`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `long documentIndex`

        minimum: 0

      - `Optional<String> documentTitle`

        maxLength: 500, minLength: 1

      - `long endBlockIndex`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `long startBlockIndex`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `JsonValue type = "content_block_location"`

    - `class CitationWebSearchResultLocationParam:`

      - `String citedText`

      - `String encryptedIndex`

      - `Optional<String> title`

        maxLength: 512, minLength: 1

      - `JsonValue type = "web_search_result_location"`

      - `String url`

        minLength: 1

    - `class CitationSearchResultLocationParam:`

      - `String citedText`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `long endBlockIndex`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `long searchResultIndex`

        0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

        Counted separately from `document_index`; server-side web search results are not included in this count.

        minimum: 0

      - `String source`

      - `long startBlockIndex`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `Optional<String> title`

      - `JsonValue type = "search_result_location"`

### Text Citation

- `class TextCitation: union`

  - `class CitationCharLocation:`

    - `String citedText`

    - `long documentIndex`

      minimum: 0

    - `Optional<String> documentTitle`

    - `long endCharIndex`

    - `Optional<String> fileId`

    - `long startCharIndex`

      minimum: 0

    - `JsonValue type = "char_location"`

  - `class CitationPageLocation:`

    - `String citedText`

    - `long documentIndex`

      minimum: 0

    - `Optional<String> documentTitle`

    - `long endPageNumber`

    - `Optional<String> fileId`

    - `long startPageNumber`

      minimum: 1

    - `JsonValue type = "page_location"`

  - `class CitationContentBlockLocation:`

    - `String citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `long documentIndex`

      minimum: 0

    - `Optional<String> documentTitle`

    - `long endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `Optional<String> fileId`

    - `long startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

      minimum: 0

    - `JsonValue type = "content_block_location"`

  - `class CitationsWebSearchResultLocation:`

    - `String citedText`

    - `String encryptedIndex`

    - `Optional<String> title`

      maxLength: 512

    - `JsonValue type = "web_search_result_location"`

    - `String url`

  - `class CitationsSearchResultLocation:`

    - `String citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `long endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `long searchResultIndex`

      0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

      Counted separately from `document_index`; server-side web search results are not included in this count.

      minimum: 0

    - `String source`

    - `long startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

      minimum: 0

    - `Optional<String> title`

    - `JsonValue type = "search_result_location"`

### Text Citation Param

- `class TextCitationParam: union`

  - `class CitationCharLocationParam:`

    - `String citedText`

    - `long documentIndex`

      minimum: 0

    - `Optional<String> documentTitle`

      maxLength: 500, minLength: 1

    - `long endCharIndex`

    - `long startCharIndex`

      minimum: 0

    - `JsonValue type = "char_location"`

  - `class CitationPageLocationParam:`

    - `String citedText`

    - `long documentIndex`

      minimum: 0

    - `Optional<String> documentTitle`

      maxLength: 500, minLength: 1

    - `long endPageNumber`

    - `long startPageNumber`

      minimum: 1

    - `JsonValue type = "page_location"`

  - `class CitationContentBlockLocationParam:`

    - `String citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `long documentIndex`

      minimum: 0

    - `Optional<String> documentTitle`

      maxLength: 500, minLength: 1

    - `long endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `long startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

      minimum: 0

    - `JsonValue type = "content_block_location"`

  - `class CitationWebSearchResultLocationParam:`

    - `String citedText`

    - `String encryptedIndex`

    - `Optional<String> title`

      maxLength: 512, minLength: 1

    - `JsonValue type = "web_search_result_location"`

    - `String url`

      minLength: 1

  - `class CitationSearchResultLocationParam:`

    - `String citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `long endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `long searchResultIndex`

      0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

      Counted separately from `document_index`; server-side web search results are not included in this count.

      minimum: 0

    - `String source`

    - `long startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

      minimum: 0

    - `Optional<String> title`

    - `JsonValue type = "search_result_location"`

### Text Delta

- `class TextDelta:`

  - `String text`

  - `JsonValue type = "text_delta"`

### Text Editor Code Execution Create Result Block

- `class TextEditorCodeExecutionCreateResultBlock:`

  - `boolean isFileUpdate`

  - `JsonValue type = "text_editor_code_execution_create_result"`

### Text Editor Code Execution Create Result Block Param

- `class TextEditorCodeExecutionCreateResultBlockParam:`

  - `boolean isFileUpdate`

  - `JsonValue type = "text_editor_code_execution_create_result"`

### Text Editor Code Execution Str Replace Result Block

- `class TextEditorCodeExecutionStrReplaceResultBlock:`

  - `Optional<List<String>> lines`

  - `Optional<Long> newLines`

  - `Optional<Long> newStart`

  - `Optional<Long> oldLines`

  - `Optional<Long> oldStart`

  - `JsonValue type = "text_editor_code_execution_str_replace_result"`

### Text Editor Code Execution Str Replace Result Block Param

- `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

  - `JsonValue type = "text_editor_code_execution_str_replace_result"`

  - `Optional<List<String>> lines`

  - `Optional<Long> newLines`

  - `Optional<Long> newStart`

  - `Optional<Long> oldLines`

  - `Optional<Long> oldStart`

### Text Editor Code Execution Tool Result Block

- `class TextEditorCodeExecutionToolResultBlock:`

  - `Content content`

    - `class TextEditorCodeExecutionToolResultError:`

      - `TextEditorCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `FILE_NOT_FOUND("file_not_found")`

      - `Optional<String> errorMessage`

      - `JsonValue type = "text_editor_code_execution_tool_result_error"`

    - `class TextEditorCodeExecutionViewResultBlock:`

      - `String content`

      - `FileType fileType`

        - `TEXT("text")`

        - `IMAGE("image")`

        - `PDF("pdf")`

      - `Optional<Long> numLines`

      - `Optional<Long> startLine`

      - `Optional<Long> totalLines`

      - `JsonValue type = "text_editor_code_execution_view_result"`

    - `class TextEditorCodeExecutionCreateResultBlock:`

      - `boolean isFileUpdate`

      - `JsonValue type = "text_editor_code_execution_create_result"`

    - `class TextEditorCodeExecutionStrReplaceResultBlock:`

      - `Optional<List<String>> lines`

      - `Optional<Long> newLines`

      - `Optional<Long> newStart`

      - `Optional<Long> oldLines`

      - `Optional<Long> oldStart`

      - `JsonValue type = "text_editor_code_execution_str_replace_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "text_editor_code_execution_tool_result"`

### Text Editor Code Execution Tool Result Block Param

- `class TextEditorCodeExecutionToolResultBlockParam:`

  - `Content content`

    - `class TextEditorCodeExecutionToolResultErrorParam:`

      - `TextEditorCodeExecutionToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

        - `FILE_NOT_FOUND("file_not_found")`

      - `JsonValue type = "text_editor_code_execution_tool_result_error"`

      - `Optional<String> errorMessage`

    - `class TextEditorCodeExecutionViewResultBlockParam:`

      - `String content`

      - `FileType fileType`

        - `TEXT("text")`

        - `IMAGE("image")`

        - `PDF("pdf")`

      - `JsonValue type = "text_editor_code_execution_view_result"`

      - `Optional<Long> numLines`

      - `Optional<Long> startLine`

      - `Optional<Long> totalLines`

    - `class TextEditorCodeExecutionCreateResultBlockParam:`

      - `boolean isFileUpdate`

      - `JsonValue type = "text_editor_code_execution_create_result"`

    - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

      - `JsonValue type = "text_editor_code_execution_str_replace_result"`

      - `Optional<List<String>> lines`

      - `Optional<Long> newLines`

      - `Optional<Long> newStart`

      - `Optional<Long> oldLines`

      - `Optional<Long> oldStart`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "text_editor_code_execution_tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Text Editor Code Execution Tool Result Error

- `class TextEditorCodeExecutionToolResultError:`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `FILE_NOT_FOUND("file_not_found")`

  - `Optional<String> errorMessage`

  - `JsonValue type = "text_editor_code_execution_tool_result_error"`

### Text Editor Code Execution Tool Result Error Code

- `enum TextEditorCodeExecutionToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `FILE_NOT_FOUND("file_not_found")`

### Text Editor Code Execution Tool Result Error Param

- `class TextEditorCodeExecutionToolResultErrorParam:`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

    - `FILE_NOT_FOUND("file_not_found")`

  - `JsonValue type = "text_editor_code_execution_tool_result_error"`

  - `Optional<String> errorMessage`

### Text Editor Code Execution View Result Block

- `class TextEditorCodeExecutionViewResultBlock:`

  - `String content`

  - `FileType fileType`

    - `TEXT("text")`

    - `IMAGE("image")`

    - `PDF("pdf")`

  - `Optional<Long> numLines`

  - `Optional<Long> startLine`

  - `Optional<Long> totalLines`

  - `JsonValue type = "text_editor_code_execution_view_result"`

### Text Editor Code Execution View Result Block Param

- `class TextEditorCodeExecutionViewResultBlockParam:`

  - `String content`

  - `FileType fileType`

    - `TEXT("text")`

    - `IMAGE("image")`

    - `PDF("pdf")`

  - `JsonValue type = "text_editor_code_execution_view_result"`

  - `Optional<Long> numLines`

  - `Optional<Long> startLine`

  - `Optional<Long> totalLines`

### Thinking Block

- `class ThinkingBlock:`

  - `String signature`

    A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

    This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `String thinking`

    The text of Claude's thinking process for this block.

  - `JsonValue type = "thinking"`

### Thinking Block Param

- `class ThinkingBlockParam:`

  - `String signature`

    The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

    Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

  - `String thinking`

    The `thinking` text of this block as returned by the API.

  - `JsonValue type = "thinking"`

### Thinking Config Adaptive

- `class ThinkingConfigAdaptive:`

  - `JsonValue type = "adaptive"`

  - `Optional<Display> display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `SUMMARIZED("summarized")`

    - `OMITTED("omitted")`

### Thinking Config Disabled

- `class ThinkingConfigDisabled:`

  - `JsonValue type = "disabled"`

### Thinking Config Enabled

- `class ThinkingConfigEnabled:`

  - `long budgetTokens`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    minimum: 1024

  - `JsonValue type = "enabled"`

  - `Optional<Display> display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `SUMMARIZED("summarized")`

    - `OMITTED("omitted")`

### Thinking Config Param

- `class ThinkingConfigParam: union`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `class ThinkingConfigEnabled:`

    - `long budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      minimum: 1024

    - `JsonValue type = "enabled"`

    - `Optional<Display> display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `SUMMARIZED("summarized")`

      - `OMITTED("omitted")`

  - `class ThinkingConfigDisabled:`

    - `JsonValue type = "disabled"`

  - `class ThinkingConfigAdaptive:`

    - `JsonValue type = "adaptive"`

    - `Optional<Display> display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `SUMMARIZED("summarized")`

      - `OMITTED("omitted")`

### Thinking Delta

- `class ThinkingDelta:`

  - `String thinking`

    The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

  - `JsonValue type = "thinking_delta"`

### Tool

- `class Tool:`

  - `InputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `JsonValue type = "object"`

    - `Optional<Properties> properties`

    - `Optional<List<String>> required`

  - `String name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<String> description`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `Optional<Boolean> eagerInputStreaming`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<Type> type`

### Tool Bash 20250124

- `class ToolBash20250124:`

  - `JsonValue name = "bash"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "bash_20250124"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `class ToolChoice: union`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `class ToolChoiceAuto:`

    The model will automatically decide whether to use tools.

    - `JsonValue type = "auto"`

    - `Optional<Boolean> disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `class ToolChoiceAny:`

    The model will use any available tools.

    - `JsonValue type = "any"`

    - `Optional<Boolean> disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceTool:`

    The model will use the specified tool with `tool_choice.name`.

    - `String name`

      The name of the tool to use.

    - `JsonValue type = "tool"`

    - `Optional<Boolean> disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class ToolChoiceNone:`

    The model will not be allowed to use tools.

    - `JsonValue type = "none"`

### Tool Choice Any

- `class ToolChoiceAny:`

  The model will use any available tools.

  - `JsonValue type = "any"`

  - `Optional<Boolean> disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `class ToolChoiceAuto:`

  The model will automatically decide whether to use tools.

  - `JsonValue type = "auto"`

  - `Optional<Boolean> disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `class ToolChoiceNone:`

  The model will not be allowed to use tools.

  - `JsonValue type = "none"`

### Tool Choice Tool

- `class ToolChoiceTool:`

  The model will use the specified tool with `tool_choice.name`.

  - `String name`

    The name of the tool to use.

  - `JsonValue type = "tool"`

  - `Optional<Boolean> disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `class ToolReferenceBlock:`

  - `String toolName`

    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

  - `JsonValue type = "tool_reference"`

### Tool Reference Block Param

- `class ToolReferenceBlockParam:`

  Tool reference block that can be included in tool_result content.

  - `String toolName`

    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

  - `JsonValue type = "tool_reference"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

### Tool Result Block Param

- `class ToolResultBlockParam:`

  - `String toolUseId`

    pattern: ^[a-zA-Z0-9_-]+$

  - `JsonValue type = "tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Content> content`

    - `String`

    - `List<Block>`

      - `class TextBlockParam:`

        - `String text`

          minLength: 1

        - `JsonValue type = "text"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<List<TextCitationParam>> citations`

          - `class CitationCharLocationParam:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endCharIndex`

            - `long startCharIndex`

              minimum: 0

            - `JsonValue type = "char_location"`

          - `class CitationPageLocationParam:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endPageNumber`

            - `long startPageNumber`

              minimum: 1

            - `JsonValue type = "page_location"`

          - `class CitationContentBlockLocationParam:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

              maxLength: 500, minLength: 1

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `JsonValue type = "content_block_location"`

          - `class CitationWebSearchResultLocationParam:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

              maxLength: 512, minLength: 1

            - `JsonValue type = "web_search_result_location"`

            - `String url`

              minLength: 1

          - `class CitationSearchResultLocationParam:`

            - `String citedText`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `long endBlockIndex`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `long searchResultIndex`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `String source`

            - `long startBlockIndex`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `Optional<String> title`

            - `JsonValue type = "search_result_location"`

      - `class ImageBlockParam:`

        - `Source source`

          - `class Base64ImageSource:`

            - `String data`

              format: byte

            - `MediaType mediaType`

              - `IMAGE_JPEG("image/jpeg")`

              - `IMAGE_PNG("image/png")`

              - `IMAGE_GIF("image/gif")`

              - `IMAGE_WEBP("image/webp")`

            - `JsonValue type = "base64"`

          - `class UrlImageSource:`

            - `JsonValue type = "url"`

            - `String url`

          - `class FileImageSource:`

            - `String fileId`

            - `JsonValue type = "file"`

        - `JsonValue type = "image"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<ImageTransformationsParam> transformations`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `Optional<OversizedImage> oversizedImage`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `DOWNSIZE("downsize")`

            - `ERROR("error")`

      - `class SearchResultBlockParam:`

        - `List<TextBlockParam> content`

          - `String text`

            minLength: 1

          - `JsonValue type = "text"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<List<TextCitationParam>> citations`

        - `String source`

        - `String title`

        - `JsonValue type = "search_result"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

      - `class DocumentBlockParam:`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

              format: byte

            - `JsonValue mediaType = "application/pdf"`

            - `JsonValue type = "base64"`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue mediaType = "text/plain"`

            - `JsonValue type = "text"`

          - `class ContentBlockSource:`

            - `Content content`

              - `String`

              - `List<ContentBlockSourceContent>`

                - `class TextBlockParam:`

                - `class ImageBlockParam:`

            - `JsonValue type = "content"`

          - `class UrlPdfSource:`

            - `JsonValue type = "url"`

            - `String url`

          - `class FileDocumentSource:`

            - `String fileId`

            - `JsonValue type = "file"`

        - `JsonValue type = "document"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<CitationsConfigParam> citations`

        - `Optional<String> context`

          minLength: 1

        - `Optional<String> title`

          maxLength: 500, minLength: 1

      - `class ToolReferenceBlockParam:`

        Tool reference block that can be included in tool_result content.

        - `String toolName`

          maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `JsonValue type = "tool_reference"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

      - `class BrowserStateBlockParam:`

        The caller's browser state after a browser toolset member call —
        the full inventory of open tabs, which tab is active, and any side
        effects (tabs opened, download state changes) the call produced.

        At most one per `tool_result`, only on a non-error result answering a
        browser toolset member `tool_use`. The server renders the
        model-visible text from it; the model never sees the raw fields.

        - `List<BrowserStateTabEntry> tabs`

          All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

          maxItems: 100

          - `String tabId`

            The caller-assigned identifier for this tab, unique within the inventory.

            maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `String title`

            The title of the page the tab is showing. May be empty.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `String url`

            The URL of the page the tab is showing. May be empty.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `Optional<Boolean> active`

            Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

        - `JsonValue type = "browser_state"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<List<BrowserStateChange>> stateChanges`

          Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

          maxItems: 200, minItems: 1

          - `class BrowserStateChangeTabOpened:`

            A tab this call's execution opened that remains open at its end —
            the creation delta of the `tabs` inventory, not an event log.

            Carries only the `tab_id`; the tab's `title` and `url` live on its
            `tabs` entry, which must include the same `tab_id`. A tab opened
            during a failed call gets no deferred `tab_opened`; it simply appears
            in the next result's `tabs` inventory.

            - `String tabId`

              The `tab_id` of the opened tab, present in `tabs`.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `JsonValue type = "tab_opened"`

          - `class BrowserStateChangeDownloadStarted:`

            A file download that started during this call.

            - `String downloadId`

              The caller-assigned identifier for this download, stable across the state changes reporting it.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `JsonValue type = "download_started"`

            - `String url`

              The final post-redirect URL the download was served from.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `class BrowserStateChangeDownloadCompleted:`

            A file download that finished during this call, reported with the
            same `download_id` as its `download_started` — or without a prior
            `download_started`, when the download finished during the call that
            started it (at most one state change per `download_id` per result).

            - `String downloadId`

              The caller-assigned identifier for this download, stable across the state changes reporting it.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `JsonValue type = "download_completed"`

            - `String url`

              The final post-redirect URL the download was served from.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `Optional<String> path`

              Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

              pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

            - `Optional<Long> sizeBytes`

              The completed download's size.

              minimum: 0

          - `class BrowserStateChangeDownloadFailed:`

            A file download that failed — or was cancelled — during this call.

            - `String downloadId`

              The caller-assigned identifier for this download, stable across the state changes reporting it.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `JsonValue type = "download_failed"`

            - `String url`

              The final post-redirect URL the download was served from.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `Optional<String> error`

              The failure or cancellation detail, when known.

              pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

  - `Optional<Boolean> isError`

  - `Optional<String> toolsetName`

    For a toolset member tool_result, the toolset family of the paired tool_use.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

### Tool Search Tool Bm25 20251119

- `class ToolSearchToolBm25_20251119:`

  - `JsonValue name = "tool_search_tool_bm25"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Type type`

    - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

    - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

- `class ToolSearchToolRegex20251119:`

  - `JsonValue name = "tool_search_tool_regex"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `Type type`

    - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

    - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

- `class ToolSearchToolResultBlock:`

  - `Content content`

    - `class ToolSearchToolResultError:`

      - `ToolSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `Optional<String> errorMessage`

      - `JsonValue type = "tool_search_tool_result_error"`

    - `class ToolSearchToolSearchResultBlock:`

      - `List<ToolReferenceBlock> toolReferences`

        - `String toolName`

          maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `JsonValue type = "tool_reference"`

      - `JsonValue type = "tool_search_tool_search_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "tool_search_tool_result"`

### Tool Search Tool Result Block Param

- `class ToolSearchToolResultBlockParam:`

  - `Content content`

    - `class ToolSearchToolResultErrorParam:`

      - `ToolSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

      - `JsonValue type = "tool_search_tool_result_error"`

      - `Optional<String> errorMessage`

    - `class ToolSearchToolSearchResultBlockParam:`

      - `List<ToolReferenceBlockParam> toolReferences`

        - `String toolName`

          maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `JsonValue type = "tool_reference"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

          - `JsonValue type = "ephemeral"`

          - `Optional<Ttl> ttl`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `TTL_5M("5m")`

            - `TTL_1H("1h")`

      - `JsonValue type = "tool_search_tool_search_result"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "tool_search_tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

### Tool Search Tool Result Error

- `class ToolSearchToolResultError:`

  - `ToolSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `Optional<String> errorMessage`

  - `JsonValue type = "tool_search_tool_result_error"`

### Tool Search Tool Result Error Code

- `enum ToolSearchToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

### Tool Search Tool Result Error Param

- `class ToolSearchToolResultErrorParam:`

  - `ToolSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

  - `JsonValue type = "tool_search_tool_result_error"`

  - `Optional<String> errorMessage`

### Tool Search Tool Search Result Block

- `class ToolSearchToolSearchResultBlock:`

  - `List<ToolReferenceBlock> toolReferences`

    - `String toolName`

      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

    - `JsonValue type = "tool_reference"`

  - `JsonValue type = "tool_search_tool_search_result"`

### Tool Search Tool Search Result Block Param

- `class ToolSearchToolSearchResultBlockParam:`

  - `List<ToolReferenceBlockParam> toolReferences`

    - `String toolName`

      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

    - `JsonValue type = "tool_reference"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue type = "ephemeral"`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

  - `JsonValue type = "tool_search_tool_search_result"`

### Tool Text Editor 20250124

- `class ToolTextEditor20250124:`

  - `JsonValue name = "str_replace_editor"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "text_editor_20250124"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

- `class ToolTextEditor20250429:`

  - `JsonValue name = "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "text_editor_20250429"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

- `class ToolTextEditor20250728:`

  - `JsonValue name = "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "text_editor_20250728"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<List<InputExample>> inputExamples`

  - `Optional<Long> maxCharacters`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    minimum: 1

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `class ToolUnion: union`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `class Tool:`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `JsonValue type = "object"`

      - `Optional<Properties> properties`

      - `Optional<List<String>> required`

    - `String name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

      - `JsonValue type = "ephemeral"`

      - `Optional<Ttl> ttl`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `TTL_5M("5m")`

        - `TTL_1H("1h")`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<String> description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `Optional<Boolean> eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Type> type`

  - `class ToolBash20250124:`

    - `JsonValue name = "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "bash_20250124"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250522:`

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20250522"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20250825:`

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20250825"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260120:`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20260120"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class CodeExecutionTool20260521:`

    Code execution tool with REPL state persistence.

    - `JsonValue name = "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "code_execution_20260521"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BrowserToolset20260801:`

    The browser toolset: a single `tools[]` entry (carrying no
    `name`) that declares the browser tool family. The model is served
    the family's tool with any members disabled via `configs` removed
    from its schema.

    - `JsonValue type = "browser_toolset_20260801"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<BrowserToolsetConfigs> configs`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `Optional<BrowserCloseTabConfig> closeTab`

        `close_tab`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserDoubleClickConfig> doubleClick`

        `double_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserFileUploadConfig> fileUpload`

        `file_upload`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserFindConfig> find`

        `find`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserFormInputConfig> formInput`

        `form_input`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserGetPageTextConfig> getPageText`

        `get_page_text`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserHoldKeyConfig> holdKey`

        `hold_key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserHoverConfig> hover`

        `hover`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserJavascriptExecConfig> javascriptExec`

        `javascript_exec`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserKeyConfig> key`

        `key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftClickConfig> leftClick`

        `left_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

        `left_click_drag`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

        `left_mouse_down`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

        `left_mouse_up`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserListTabsConfig> listTabs`

        `list_tabs`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserMiddleClickConfig> middleClick`

        `middle_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserMouseMoveConfig> mouseMove`

        `mouse_move`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserNavigateConfig> navigate`

        `navigate`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserNewTabConfig> newTab`

        `new_tab`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserReadConsoleConfig> readConsole`

        `read_console`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserReadNetworkConfig> readNetwork`

        `read_network`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserReadPageConfig> readPage`

        `read_page`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserRightClickConfig> rightClick`

        `right_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserScreenshotConfig> screenshot`

        `screenshot`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserScrollConfig> scroll`

        `scroll`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserScrollToConfig> scrollTo`

        `scroll_to`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserSwitchTabConfig> switchTab`

        `switch_tab`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserTripleClickConfig> tripleClick`

        `triple_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserTypeConfig> type`

        `type`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserWaitConfig> wait`

        `wait`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<BrowserZoomConfig> zoom`

        `zoom`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class MemoryTool20250818:`

    - `JsonValue name = "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "memory_20250818"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ComputerToolset20260801:`

    The computer toolset: a single `tools[]` entry (carrying no
    `name`) that declares the computer tool family. The model is
    served the family's tool with any members disabled via `configs`
    removed from its schema. Every member is enabled by default, zoom
    included. The single-tool options `display_number` and
    `enable_zoom` are not fields of a toolset entry — it carries only
    `type`, `configs`, and `cache_control`; zoom is controlled
    via `configs.zoom.enabled`.

    - `JsonValue type = "computer_toolset_20260801"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<ComputerToolsetConfigs> configs`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `Optional<ComputerCursorPositionConfig> cursorPosition`

        `cursor_position`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerDoubleClickConfig> doubleClick`

        `double_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerHoldKeyConfig> holdKey`

        `hold_key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerKeyConfig> key`

        `key`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftClickConfig> leftClick`

        `left_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

        `left_click_drag`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

        `left_mouse_down`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

        `left_mouse_up`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerMiddleClickConfig> middleClick`

        `middle_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerMouseMoveConfig> mouseMove`

        `mouse_move`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerRightClickConfig> rightClick`

        `right_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerScreenshotConfig> screenshot`

        `screenshot`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerScrollConfig> scroll`

        `scroll`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerTripleClickConfig> tripleClick`

        `triple_click`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerTypeConfig> type`

        `type`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerWaitConfig> wait`

        `wait`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `Optional<ComputerZoomConfig> zoom`

        `zoom`'s config overrides.

        - `Optional<Boolean> deferLoading`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `Optional<Boolean> enabled`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `class ToolTextEditor20250124:`

    - `JsonValue name = "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "text_editor_20250124"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250429:`

    - `JsonValue name = "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "text_editor_20250429"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolTextEditor20250728:`

    - `JsonValue name = "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "text_editor_20250728"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<List<InputExample>> inputExamples`

    - `Optional<Long> maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      minimum: 1

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20250305:`

    - `JsonValue name = "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_search_20250305"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

      - `JsonValue type = "approximate"`

      - `Optional<String> city`

        The city of the user.

        maxLength: 255, minLength: 1

      - `Optional<String> country`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `Optional<String> region`

        The region of the user.

        maxLength: 255, minLength: 1

      - `Optional<String> timezone`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `class WebFetchTool20250910:`

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20250910"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `Optional<Boolean> enabled`

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebSearchTool20260209:`

    - `JsonValue name = "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_search_20260209"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class WebFetchTool20260209:`

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20260209"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class WebFetchTool20260309:`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20260309"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Boolean> useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class WebSearchTool20260318:`

    - `JsonValue name = "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_search_20260318"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `Optional<List<String>> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<ResponseInclusion> responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `FULL("full")`

      - `EXCLUDED("excluded")`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<UserLocation> userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class WebFetchTool20260318:`

    - `JsonValue name = "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `JsonValue type = "web_fetch_20260318"`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<List<String>> allowedDomains`

      List of domains to allow fetching from

    - `Optional<List<String>> blockedDomains`

      List of domains to block fetching from

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Long> maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `Optional<Long> maxUses`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `Optional<ResponseInclusion> responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `FULL("full")`

      - `EXCLUDED("excluded")`

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

    - `Optional<Boolean> useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class ToolSearchToolBm25_20251119:`

    - `JsonValue name = "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

      - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

      - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

  - `class ToolSearchToolRegex20251119:`

    - `JsonValue name = "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `Type type`

      - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

      - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

    - `Optional<List<AllowedCaller>> allowedCallers`

      - `DIRECT("direct")`

      - `CODE_EXECUTION_20250825("code_execution_20250825")`

      - `CODE_EXECUTION_20260120("code_execution_20260120")`

      - `CODE_EXECUTION_20260521("code_execution_20260521")`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<Boolean> deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `Optional<Boolean> strict`

      When true, guarantees schema validation on tool names and inputs

### Tool Use Block

- `class ToolUseBlock:`

  - `String id`

    pattern: ^[a-zA-Z0-9_-]+$

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

  - `Input input`

  - `String name`

    minLength: 1

  - `JsonValue type = "tool_use"`

  - `Optional<String> toolsetName`

    For a toolset member tool_use, the toolset family.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

### Tool Use Block Param

- `class ToolUseBlockParam:`

  - `String id`

    pattern: ^[a-zA-Z0-9_-]+$

  - `Input input`

  - `String name`

    maxLength: 200, minLength: 1

  - `JsonValue type = "tool_use"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

  - `Optional<String> toolsetName`

    For a toolset member tool_use, the toolset family this member belongs to.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

### URL Image Source

- `class UrlImageSource:`

  - `JsonValue type = "url"`

  - `String url`

### URL PDF Source

- `class UrlPdfSource:`

  - `JsonValue type = "url"`

  - `String url`

### Usage

- `class Usage:`

  - `Optional<CacheCreation> cacheCreation`

    Breakdown of cached tokens by TTL

    - `long ephemeral1hInputTokens`

      The number of input tokens used to create the 1 hour cache entry.

      minimum: 0

    - `long ephemeral5mInputTokens`

      The number of input tokens used to create the 5 minute cache entry.

      minimum: 0

  - `Optional<Long> cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

    minimum: 0

  - `Optional<Long> cacheReadInputTokens`

    The number of input tokens read from the cache.

    minimum: 0

  - `Optional<String> inferenceGeo`

    The geographic region where inference was performed for this request.

  - `long inputTokens`

    The number of input tokens which were used.

    minimum: 0

  - `long outputTokens`

    The number of output tokens which were used.

    minimum: 0

  - `Optional<OutputTokensDetails> outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

    - `long thinkingTokens`

      Number of output tokens the model generated as internal reasoning, including
      the thinking-block delimiter tokens.

      Reflects the raw reasoning the model produced, not the (possibly shorter)
      summarized thinking text returned in the response body. Computed by
      re-tokenizing the raw reasoning text, so it may differ from the model's exact
      generation count by a small number of tokens. Always ≤ `output_tokens`;
      `output_tokens - thinking_tokens` approximates the non-reasoning output.

      minimum: 0

  - `Optional<ServerToolUsage> serverToolUse`

    The number of server tool requests.

    - `long webFetchRequests`

      The number of web fetch tool requests.

      minimum: 0

    - `long webSearchRequests`

      The number of web search tool requests.

      minimum: 0

  - `Optional<ServiceTier> serviceTier`

    If the request used the priority, standard, or batch tier.

    - `STANDARD("standard")`

    - `PRIORITY("priority")`

    - `BATCH("batch")`

### User Location

- `class UserLocation:`

  - `JsonValue type = "approximate"`

  - `Optional<String> city`

    The city of the user.

    maxLength: 255, minLength: 1

  - `Optional<String> country`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    maxLength: 2, minLength: 2

  - `Optional<String> region`

    The region of the user.

    maxLength: 255, minLength: 1

  - `Optional<String> timezone`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    maxLength: 255, minLength: 1

### Web Fetch Block

- `class WebFetchBlock:`

  - `DocumentBlock content`

    - `Optional<CitationsConfig> citations`

      Citation configuration for the document

      - `boolean enabled`

    - `Source source`

      - `class Base64PdfSource:`

        - `String data`

          format: byte

        - `JsonValue mediaType = "application/pdf"`

        - `JsonValue type = "base64"`

      - `class PlainTextSource:`

        - `String data`

        - `JsonValue mediaType = "text/plain"`

        - `JsonValue type = "text"`

    - `Optional<String> title`

      The title of the document

    - `JsonValue type = "document"`

  - `Optional<String> retrievedAt`

    ISO 8601 timestamp when the content was retrieved

  - `JsonValue type = "web_fetch_result"`

  - `String url`

    Fetched content URL

### Web Fetch Block Param

- `class WebFetchBlockParam:`

  - `DocumentBlockParam content`

    - `Source source`

      - `class Base64PdfSource:`

        - `String data`

          format: byte

        - `JsonValue mediaType = "application/pdf"`

        - `JsonValue type = "base64"`

      - `class PlainTextSource:`

        - `String data`

        - `JsonValue mediaType = "text/plain"`

        - `JsonValue type = "text"`

      - `class ContentBlockSource:`

        - `Content content`

          - `String`

          - `List<ContentBlockSourceContent>`

            - `class TextBlockParam:`

              - `String text`

                minLength: 1

              - `JsonValue type = "text"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue type = "ephemeral"`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<TextCitationParam>> citations`

                - `class CitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endCharIndex`

                  - `long startCharIndex`

                    minimum: 0

                  - `JsonValue type = "char_location"`

                - `class CitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endPageNumber`

                  - `long startPageNumber`

                    minimum: 1

                  - `JsonValue type = "page_location"`

                - `class CitationContentBlockLocationParam:`

                  - `String citedText`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endBlockIndex`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `long startBlockIndex`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `JsonValue type = "content_block_location"`

                - `class CitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                    maxLength: 512, minLength: 1

                  - `JsonValue type = "web_search_result_location"`

                  - `String url`

                    minLength: 1

                - `class CitationSearchResultLocationParam:`

                  - `String citedText`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `long endBlockIndex`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `long searchResultIndex`

                    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                    Counted separately from `document_index`; server-side web search results are not included in this count.

                    minimum: 0

                  - `String source`

                  - `long startBlockIndex`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `Optional<String> title`

                  - `JsonValue type = "search_result_location"`

            - `class ImageBlockParam:`

              - `Source source`

                - `class Base64ImageSource:`

                  - `String data`

                    format: byte

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue type = "base64"`

                - `class UrlImageSource:`

                  - `JsonValue type = "url"`

                  - `String url`

                - `class FileImageSource:`

                  - `String fileId`

                  - `JsonValue type = "file"`

              - `JsonValue type = "image"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<ImageTransformationsParam> transformations`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `Optional<OversizedImage> oversizedImage`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `DOWNSIZE("downsize")`

                  - `ERROR("error")`

        - `JsonValue type = "content"`

      - `class UrlPdfSource:`

        - `JsonValue type = "url"`

        - `String url`

      - `class FileDocumentSource:`

        - `String fileId`

        - `JsonValue type = "file"`

    - `JsonValue type = "document"`

    - `Optional<CacheControlEphemeral> cacheControl`

      Create a cache control breakpoint at this content block.

    - `Optional<CitationsConfigParam> citations`

      - `Optional<Boolean> enabled`

    - `Optional<String> context`

      minLength: 1

    - `Optional<String> title`

      maxLength: 500, minLength: 1

  - `JsonValue type = "web_fetch_result"`

  - `String url`

    Fetched content URL

  - `Optional<String> retrievedAt`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

- `class WebFetchTool20250910:`

  - `JsonValue name = "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_fetch_20250910"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    List of domains to allow fetching from

  - `Optional<List<String>> blockedDomains`

    List of domains to block fetching from

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> enabled`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260209

- `class WebFetchTool20260209:`

  - `JsonValue name = "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_fetch_20260209"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    List of domains to allow fetching from

  - `Optional<List<String>> blockedDomains`

    List of domains to block fetching from

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> enabled`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260309

- `class WebFetchTool20260309:`

  Web fetch tool with use_cache parameter for bypassing cached content.

  - `JsonValue name = "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_fetch_20260309"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    List of domains to allow fetching from

  - `Optional<List<String>> blockedDomains`

    List of domains to block fetching from

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> enabled`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<Boolean> useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool 20260318

- `class WebFetchTool20260318:`

  - `JsonValue name = "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_fetch_20260318"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    List of domains to allow fetching from

  - `Optional<List<String>> blockedDomains`

    List of domains to block fetching from

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<CitationsConfigParam> citations`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `Optional<Boolean> enabled`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<ResponseInclusion> responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `FULL("full")`

    - `EXCLUDED("excluded")`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<Boolean> useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool Result Block

- `class WebFetchToolResultBlock:`

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

  - `Content content`

    - `class WebFetchToolResultErrorBlock:`

      - `WebFetchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `URL_TOO_LONG("url_too_long")`

        - `URL_NOT_ALLOWED("url_not_allowed")`

        - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

        - `URL_NOT_ACCESSIBLE("url_not_accessible")`

        - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `UNAVAILABLE("unavailable")`

      - `JsonValue type = "web_fetch_tool_result_error"`

    - `class WebFetchBlock:`

      - `DocumentBlock content`

        - `Optional<CitationsConfig> citations`

          Citation configuration for the document

          - `boolean enabled`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

              format: byte

            - `JsonValue mediaType = "application/pdf"`

            - `JsonValue type = "base64"`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue mediaType = "text/plain"`

            - `JsonValue type = "text"`

        - `Optional<String> title`

          The title of the document

        - `JsonValue type = "document"`

      - `Optional<String> retrievedAt`

        ISO 8601 timestamp when the content was retrieved

      - `JsonValue type = "web_fetch_result"`

      - `String url`

        Fetched content URL

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "web_fetch_tool_result"`

### Web Fetch Tool Result Block Param

- `class WebFetchToolResultBlockParam:`

  - `Content content`

    - `class WebFetchToolResultErrorBlockParam:`

      - `WebFetchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `URL_TOO_LONG("url_too_long")`

        - `URL_NOT_ALLOWED("url_not_allowed")`

        - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

        - `URL_NOT_ACCESSIBLE("url_not_accessible")`

        - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `UNAVAILABLE("unavailable")`

      - `JsonValue type = "web_fetch_tool_result_error"`

    - `class WebFetchBlockParam:`

      - `DocumentBlockParam content`

        - `Source source`

          - `class Base64PdfSource:`

            - `String data`

              format: byte

            - `JsonValue mediaType = "application/pdf"`

            - `JsonValue type = "base64"`

          - `class PlainTextSource:`

            - `String data`

            - `JsonValue mediaType = "text/plain"`

            - `JsonValue type = "text"`

          - `class ContentBlockSource:`

            - `Content content`

              - `String`

              - `List<ContentBlockSourceContent>`

                - `class TextBlockParam:`

                  - `String text`

                    minLength: 1

                  - `JsonValue type = "text"`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                    - `JsonValue type = "ephemeral"`

                    - `Optional<Ttl> ttl`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                      - `TTL_5M("5m")`

                      - `TTL_1H("1h")`

                  - `Optional<List<TextCitationParam>> citations`

                    - `class CitationCharLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                        minimum: 0

                      - `Optional<String> documentTitle`

                        maxLength: 500, minLength: 1

                      - `long endCharIndex`

                      - `long startCharIndex`

                        minimum: 0

                      - `JsonValue type = "char_location"`

                    - `class CitationPageLocationParam:`

                      - `String citedText`

                      - `long documentIndex`

                        minimum: 0

                      - `Optional<String> documentTitle`

                        maxLength: 500, minLength: 1

                      - `long endPageNumber`

                      - `long startPageNumber`

                        minimum: 1

                      - `JsonValue type = "page_location"`

                    - `class CitationContentBlockLocationParam:`

                      - `String citedText`

                        The full text of the cited block range, concatenated.

                        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                      - `long documentIndex`

                        minimum: 0

                      - `Optional<String> documentTitle`

                        maxLength: 500, minLength: 1

                      - `long endBlockIndex`

                        Exclusive 0-based end index of the cited block range in the source's `content` array.

                        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                      - `long startBlockIndex`

                        0-based index of the first cited block in the source's `content` array.

                        minimum: 0

                      - `JsonValue type = "content_block_location"`

                    - `class CitationWebSearchResultLocationParam:`

                      - `String citedText`

                      - `String encryptedIndex`

                      - `Optional<String> title`

                        maxLength: 512, minLength: 1

                      - `JsonValue type = "web_search_result_location"`

                      - `String url`

                        minLength: 1

                    - `class CitationSearchResultLocationParam:`

                      - `String citedText`

                        The full text of the cited block range, concatenated.

                        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                      - `long endBlockIndex`

                        Exclusive 0-based end index of the cited block range in the source's `content` array.

                        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                      - `long searchResultIndex`

                        0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                        Counted separately from `document_index`; server-side web search results are not included in this count.

                        minimum: 0

                      - `String source`

                      - `long startBlockIndex`

                        0-based index of the first cited block in the source's `content` array.

                        minimum: 0

                      - `Optional<String> title`

                      - `JsonValue type = "search_result_location"`

                - `class ImageBlockParam:`

                  - `Source source`

                    - `class Base64ImageSource:`

                      - `String data`

                        format: byte

                      - `MediaType mediaType`

                        - `IMAGE_JPEG("image/jpeg")`

                        - `IMAGE_PNG("image/png")`

                        - `IMAGE_GIF("image/gif")`

                        - `IMAGE_WEBP("image/webp")`

                      - `JsonValue type = "base64"`

                    - `class UrlImageSource:`

                      - `JsonValue type = "url"`

                      - `String url`

                    - `class FileImageSource:`

                      - `String fileId`

                      - `JsonValue type = "file"`

                  - `JsonValue type = "image"`

                  - `Optional<CacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                  - `Optional<ImageTransformationsParam> transformations`

                    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                    - `Optional<OversizedImage> oversizedImage`

                      What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                      - `DOWNSIZE("downsize")`

                      - `ERROR("error")`

            - `JsonValue type = "content"`

          - `class UrlPdfSource:`

            - `JsonValue type = "url"`

            - `String url`

          - `class FileDocumentSource:`

            - `String fileId`

            - `JsonValue type = "file"`

        - `JsonValue type = "document"`

        - `Optional<CacheControlEphemeral> cacheControl`

          Create a cache control breakpoint at this content block.

        - `Optional<CitationsConfigParam> citations`

          - `Optional<Boolean> enabled`

        - `Optional<String> context`

          minLength: 1

        - `Optional<String> title`

          maxLength: 500, minLength: 1

      - `JsonValue type = "web_fetch_result"`

      - `String url`

        Fetched content URL

      - `Optional<String> retrievedAt`

        ISO 8601 timestamp when the content was retrieved

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "web_fetch_tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

### Web Fetch Tool Result Error Block

- `class WebFetchToolResultErrorBlock:`

  - `WebFetchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `URL_TOO_LONG("url_too_long")`

    - `URL_NOT_ALLOWED("url_not_allowed")`

    - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `UNAVAILABLE("unavailable")`

  - `JsonValue type = "web_fetch_tool_result_error"`

### Web Fetch Tool Result Error Block Param

- `class WebFetchToolResultErrorBlockParam:`

  - `WebFetchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `URL_TOO_LONG("url_too_long")`

    - `URL_NOT_ALLOWED("url_not_allowed")`

    - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `UNAVAILABLE("unavailable")`

  - `JsonValue type = "web_fetch_tool_result_error"`

### Web Fetch Tool Result Error Code

- `enum WebFetchToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `URL_TOO_LONG("url_too_long")`

  - `URL_NOT_ALLOWED("url_not_allowed")`

  - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

  - `UNAVAILABLE("unavailable")`

### Web Search Result Block

- `class WebSearchResultBlock:`

  - `String encryptedContent`

  - `Optional<String> pageAge`

  - `String title`

  - `JsonValue type = "web_search_result"`

  - `String url`

### Web Search Result Block Param

- `class WebSearchResultBlockParam:`

  - `String encryptedContent`

  - `String title`

  - `JsonValue type = "web_search_result"`

  - `String url`

  - `Optional<String> pageAge`

### Web Search Tool 20250305

- `class WebSearchTool20250305:`

  - `JsonValue name = "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_search_20250305"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `Optional<List<String>> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<UserLocation> userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

    - `JsonValue type = "approximate"`

    - `Optional<String> city`

      The city of the user.

      maxLength: 255, minLength: 1

    - `Optional<String> country`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      maxLength: 2, minLength: 2

    - `Optional<String> region`

      The region of the user.

      maxLength: 255, minLength: 1

    - `Optional<String> timezone`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      maxLength: 255, minLength: 1

### Web Search Tool 20260209

- `class WebSearchTool20260209:`

  - `JsonValue name = "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_search_20260209"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `Optional<List<String>> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<UserLocation> userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

    - `JsonValue type = "approximate"`

    - `Optional<String> city`

      The city of the user.

      maxLength: 255, minLength: 1

    - `Optional<String> country`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      maxLength: 2, minLength: 2

    - `Optional<String> region`

      The region of the user.

      maxLength: 255, minLength: 1

    - `Optional<String> timezone`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      maxLength: 255, minLength: 1

### Web Search Tool 20260318

- `class WebSearchTool20260318:`

  - `JsonValue name = "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `JsonValue type = "web_search_20260318"`

  - `Optional<List<AllowedCaller>> allowedCallers`

    - `DIRECT("direct")`

    - `CODE_EXECUTION_20250825("code_execution_20250825")`

    - `CODE_EXECUTION_20260120("code_execution_20260120")`

    - `CODE_EXECUTION_20260521("code_execution_20260521")`

  - `Optional<List<String>> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `Optional<List<String>> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Boolean> deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `Optional<Long> maxUses`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `Optional<ResponseInclusion> responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `FULL("full")`

    - `EXCLUDED("excluded")`

  - `Optional<Boolean> strict`

    When true, guarantees schema validation on tool names and inputs

  - `Optional<UserLocation> userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

    - `JsonValue type = "approximate"`

    - `Optional<String> city`

      The city of the user.

      maxLength: 255, minLength: 1

    - `Optional<String> country`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      maxLength: 2, minLength: 2

    - `Optional<String> region`

      The region of the user.

      maxLength: 255, minLength: 1

    - `Optional<String> timezone`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      maxLength: 255, minLength: 1

### Web Search Tool Request Error

- `class WebSearchToolRequestError:`

  - `WebSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `QUERY_TOO_LONG("query_too_long")`

    - `REQUEST_TOO_LARGE("request_too_large")`

  - `JsonValue type = "web_search_tool_result_error"`

### Web Search Tool Result Block

- `class WebSearchToolResultBlock:`

  - `Caller caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

  - `WebSearchToolResultBlockContent content`

    - `class WebSearchToolResultError:`

      - `WebSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `QUERY_TOO_LONG("query_too_long")`

        - `REQUEST_TOO_LARGE("request_too_large")`

      - `JsonValue type = "web_search_tool_result_error"`

    - `List<WebSearchResultBlock>`

      - `String encryptedContent`

      - `Optional<String> pageAge`

      - `String title`

      - `JsonValue type = "web_search_result"`

      - `String url`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "web_search_tool_result"`

### Web Search Tool Result Block Content

- `class WebSearchToolResultBlockContent: union`

  - `class WebSearchToolResultError:`

    - `WebSearchToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `MAX_USES_EXCEEDED("max_uses_exceeded")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `QUERY_TOO_LONG("query_too_long")`

      - `REQUEST_TOO_LARGE("request_too_large")`

    - `JsonValue type = "web_search_tool_result_error"`

  - `List<WebSearchResultBlock>`

    - `String encryptedContent`

    - `Optional<String> pageAge`

    - `String title`

    - `JsonValue type = "web_search_result"`

    - `String url`

### Web Search Tool Result Block Param

- `class WebSearchToolResultBlockParam:`

  - `WebSearchToolResultBlockParamContent content`

    - `List<WebSearchResultBlockParam>`

      - `String encryptedContent`

      - `String title`

      - `JsonValue type = "web_search_result"`

      - `String url`

      - `Optional<String> pageAge`

    - `class WebSearchToolRequestError:`

      - `WebSearchToolResultErrorCode errorCode`

        - `INVALID_TOOL_INPUT("invalid_tool_input")`

        - `UNAVAILABLE("unavailable")`

        - `MAX_USES_EXCEEDED("max_uses_exceeded")`

        - `TOO_MANY_REQUESTS("too_many_requests")`

        - `QUERY_TOO_LONG("query_too_long")`

        - `REQUEST_TOO_LARGE("request_too_large")`

      - `JsonValue type = "web_search_tool_result_error"`

  - `String toolUseId`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `JsonValue type = "web_search_tool_result"`

  - `Optional<CacheControlEphemeral> cacheControl`

    Create a cache control breakpoint at this content block.

    - `JsonValue type = "ephemeral"`

    - `Optional<Ttl> ttl`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `TTL_5M("5m")`

      - `TTL_1H("1h")`

  - `Optional<Caller> caller`

    Tool invocation directly from the model.

    - `class DirectCaller:`

      Tool invocation directly from the model.

      - `JsonValue type = "direct"`

    - `class ServerToolCaller:`

      Tool invocation generated by a server-side tool.

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20250825"`

    - `class ServerToolCaller20260120:`

      - `String toolId`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonValue type = "code_execution_20260120"`

### Web Search Tool Result Block Param Content

- `class WebSearchToolResultBlockParamContent: union`

  - `List<WebSearchResultBlockParam>`

    - `String encryptedContent`

    - `String title`

    - `JsonValue type = "web_search_result"`

    - `String url`

    - `Optional<String> pageAge`

  - `class WebSearchToolRequestError:`

    - `WebSearchToolResultErrorCode errorCode`

      - `INVALID_TOOL_INPUT("invalid_tool_input")`

      - `UNAVAILABLE("unavailable")`

      - `MAX_USES_EXCEEDED("max_uses_exceeded")`

      - `TOO_MANY_REQUESTS("too_many_requests")`

      - `QUERY_TOO_LONG("query_too_long")`

      - `REQUEST_TOO_LARGE("request_too_large")`

    - `JsonValue type = "web_search_tool_result_error"`

### Web Search Tool Result Error

- `class WebSearchToolResultError:`

  - `WebSearchToolResultErrorCode errorCode`

    - `INVALID_TOOL_INPUT("invalid_tool_input")`

    - `UNAVAILABLE("unavailable")`

    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

    - `TOO_MANY_REQUESTS("too_many_requests")`

    - `QUERY_TOO_LONG("query_too_long")`

    - `REQUEST_TOO_LARGE("request_too_large")`

  - `JsonValue type = "web_search_tool_result_error"`

### Web Search Tool Result Error Code

- `enum WebSearchToolResultErrorCode:`

  - `INVALID_TOOL_INPUT("invalid_tool_input")`

  - `UNAVAILABLE("unavailable")`

  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

  - `TOO_MANY_REQUESTS("too_many_requests")`

  - `QUERY_TOO_LONG("query_too_long")`

  - `REQUEST_TOO_LARGE("request_too_large")`

## Messages › Batches

### Create a Message Batch

`MessageBatch messages().batches().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchCreateParams params`

  - `Optional<String> userProfileId`

    The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

  - `List<Request> requests`

    List of requests for prompt completion. Each is an individual request to create a Message.

    maxItems: 100000, minItems: 1

    - `String customId`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

    - `Params params`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

      - `long maxTokens`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

        Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

        minimum: 0

      - `List<MessageParam> messages`

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

        - `Content content`

          - `String`

          - `List<ContentBlockParam>`

            - `class TextBlockParam:`

              - `String text`

                minLength: 1

              - `JsonValue type = "text"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue type = "ephemeral"`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<TextCitationParam>> citations`

                - `class CitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endCharIndex`

                  - `long startCharIndex`

                    minimum: 0

                  - `JsonValue type = "char_location"`

                - `class CitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endPageNumber`

                  - `long startPageNumber`

                    minimum: 1

                  - `JsonValue type = "page_location"`

                - `class CitationContentBlockLocationParam:`

                  - `String citedText`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endBlockIndex`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `long startBlockIndex`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `JsonValue type = "content_block_location"`

                - `class CitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                    maxLength: 512, minLength: 1

                  - `JsonValue type = "web_search_result_location"`

                  - `String url`

                    minLength: 1

                - `class CitationSearchResultLocationParam:`

                  - `String citedText`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `long endBlockIndex`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `long searchResultIndex`

                    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                    Counted separately from `document_index`; server-side web search results are not included in this count.

                    minimum: 0

                  - `String source`

                  - `long startBlockIndex`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `Optional<String> title`

                  - `JsonValue type = "search_result_location"`

            - `class ImageBlockParam:`

              - `Source source`

                - `class Base64ImageSource:`

                  - `String data`

                    format: byte

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue type = "base64"`

                - `class UrlImageSource:`

                  - `JsonValue type = "url"`

                  - `String url`

                - `class FileImageSource:`

                  - `String fileId`

                  - `JsonValue type = "file"`

              - `JsonValue type = "image"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<ImageTransformationsParam> transformations`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `Optional<OversizedImage> oversizedImage`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `DOWNSIZE("downsize")`

                  - `ERROR("error")`

            - `class DocumentBlockParam:`

              - `Source source`

                - `class Base64PdfSource:`

                  - `String data`

                    format: byte

                  - `JsonValue mediaType = "application/pdf"`

                  - `JsonValue type = "base64"`

                - `class PlainTextSource:`

                  - `String data`

                  - `JsonValue mediaType = "text/plain"`

                  - `JsonValue type = "text"`

                - `class ContentBlockSource:`

                  - `Content content`

                    - `String`

                    - `List<ContentBlockSourceContent>`

                      - `class TextBlockParam:`

                      - `class ImageBlockParam:`

                  - `JsonValue type = "content"`

                - `class UrlPdfSource:`

                  - `JsonValue type = "url"`

                  - `String url`

                - `class FileDocumentSource:`

                  - `String fileId`

                  - `JsonValue type = "file"`

              - `JsonValue type = "document"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<CitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

              - `Optional<String> context`

                minLength: 1

              - `Optional<String> title`

                maxLength: 500, minLength: 1

            - `class SearchResultBlockParam:`

              - `List<TextBlockParam> content`

                - `String text`

                  minLength: 1

                - `JsonValue type = "text"`

                - `Optional<CacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                - `Optional<List<TextCitationParam>> citations`

              - `String source`

              - `String title`

              - `JsonValue type = "search_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<CitationsConfigParam> citations`

            - `class ThinkingBlockParam:`

              - `String signature`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `String thinking`

                The `thinking` text of this block as returned by the API.

              - `JsonValue type = "thinking"`

            - `class RedactedThinkingBlockParam:`

              - `String data`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `JsonValue type = "redacted_thinking"`

            - `class ToolUseBlockParam:`

              - `String id`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Input input`

              - `String name`

                maxLength: 200, minLength: 1

              - `JsonValue type = "tool_use"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonValue type = "direct"`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `String toolId`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonValue type = "code_execution_20250825"`

                - `class ServerToolCaller20260120:`

                  - `String toolId`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonValue type = "code_execution_20260120"`

              - `Optional<String> toolsetName`

                For a toolset member tool_use, the toolset family this member belongs to.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `class ToolResultBlockParam:`

              - `String toolUseId`

                pattern: ^[a-zA-Z0-9_-]+$

              - `JsonValue type = "tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Content> content`

                - `String`

                - `List<Block>`

                  - `class TextBlockParam:`

                  - `class ImageBlockParam:`

                  - `class SearchResultBlockParam:`

                  - `class DocumentBlockParam:`

                  - `class ToolReferenceBlockParam:`

                    Tool reference block that can be included in tool_result content.

                    - `String toolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonValue type = "tool_reference"`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                  - `class BrowserStateBlockParam:`

                    The caller's browser state after a browser toolset member call —
                    the full inventory of open tabs, which tab is active, and any side
                    effects (tabs opened, download state changes) the call produced.

                    At most one per `tool_result`, only on a non-error result answering a
                    browser toolset member `tool_use`. The server renders the
                    model-visible text from it; the model never sees the raw fields.

                    - `List<BrowserStateTabEntry> tabs`

                      All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                      maxItems: 100

                      - `String tabId`

                        The caller-assigned identifier for this tab, unique within the inventory.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `String title`

                        The title of the page the tab is showing. May be empty.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `String url`

                        The URL of the page the tab is showing. May be empty.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `Optional<Boolean> active`

                        Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                    - `JsonValue type = "browser_state"`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                    - `Optional<List<BrowserStateChange>> stateChanges`

                      Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                      maxItems: 200, minItems: 1

                      - `class BrowserStateChangeTabOpened:`

                        A tab this call's execution opened that remains open at its end —
                        the creation delta of the `tabs` inventory, not an event log.

                        Carries only the `tab_id`; the tab's `title` and `url` live on its
                        `tabs` entry, which must include the same `tab_id`. A tab opened
                        during a failed call gets no deferred `tab_opened`; it simply appears
                        in the next result's `tabs` inventory.

                        - `String tabId`

                          The `tab_id` of the opened tab, present in `tabs`.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type = "tab_opened"`

                      - `class BrowserStateChangeDownloadStarted:`

                        A file download that started during this call.

                        - `String downloadId`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type = "download_started"`

                        - `String url`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `class BrowserStateChangeDownloadCompleted:`

                        A file download that finished during this call, reported with the
                        same `download_id` as its `download_started` — or without a prior
                        `download_started`, when the download finished during the call that
                        started it (at most one state change per `download_id` per result).

                        - `String downloadId`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type = "download_completed"`

                        - `String url`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Optional<String> path`

                          Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                        - `Optional<Long> sizeBytes`

                          The completed download's size.

                          minimum: 0

                      - `class BrowserStateChangeDownloadFailed:`

                        A file download that failed — or was cancelled — during this call.

                        - `String downloadId`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type = "download_failed"`

                        - `String url`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Optional<String> error`

                          The failure or cancellation detail, when known.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

              - `Optional<Boolean> isError`

              - `Optional<String> toolsetName`

                For a toolset member tool_result, the toolset family of the paired tool_use.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `class ServerToolUseBlockParam:`

              - `String id`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Input input`

              - `Name name`

                - `WEB_SEARCH("web_search")`

                - `WEB_FETCH("web_fetch")`

                - `CODE_EXECUTION("code_execution")`

                - `BASH_CODE_EXECUTION("bash_code_execution")`

                - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

                - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

                - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

              - `JsonValue type = "server_tool_use"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class ServerToolCaller20260120:`

            - `class WebSearchToolResultBlockParam:`

              - `WebSearchToolResultBlockParamContent content`

                - `List<WebSearchResultBlockParam>`

                  - `String encryptedContent`

                  - `String title`

                  - `JsonValue type = "web_search_result"`

                  - `String url`

                  - `Optional<String> pageAge`

                - `class WebSearchToolRequestError:`

                  - `WebSearchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `QUERY_TOO_LONG("query_too_long")`

                    - `REQUEST_TOO_LARGE("request_too_large")`

                  - `JsonValue type = "web_search_tool_result_error"`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "web_search_tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class ServerToolCaller20260120:`

            - `class WebFetchToolResultBlockParam:`

              - `Content content`

                - `class WebFetchToolResultErrorBlockParam:`

                  - `WebFetchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `URL_TOO_LONG("url_too_long")`

                    - `URL_NOT_ALLOWED("url_not_allowed")`

                    - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `UNAVAILABLE("unavailable")`

                  - `JsonValue type = "web_fetch_tool_result_error"`

                - `class WebFetchBlockParam:`

                  - `DocumentBlockParam content`

                  - `JsonValue type = "web_fetch_result"`

                  - `String url`

                    Fetched content URL

                  - `Optional<String> retrievedAt`

                    ISO 8601 timestamp when the content was retrieved

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "web_fetch_tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class ServerToolCaller20260120:`

            - `class CodeExecutionToolResultBlockParam:`

              - `CodeExecutionToolResultBlockParamContent content`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `class CodeExecutionToolResultErrorParam:`

                  - `CodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `JsonValue type = "code_execution_tool_result_error"`

                - `class CodeExecutionResultBlockParam:`

                  - `List<CodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue type = "code_execution_output"`

                  - `long returnCode`

                  - `String stderr`

                  - `String stdout`

                  - `JsonValue type = "code_execution_result"`

                - `class EncryptedCodeExecutionResultBlockParam:`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `List<CodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue type = "code_execution_output"`

                  - `String encryptedStdout`

                  - `long returnCode`

                  - `String stderr`

                  - `JsonValue type = "encrypted_code_execution_result"`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "code_execution_tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BashCodeExecutionToolResultBlockParam:`

              - `Content content`

                - `class BashCodeExecutionToolResultErrorParam:`

                  - `BashCodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                  - `JsonValue type = "bash_code_execution_tool_result_error"`

                - `class BashCodeExecutionResultBlockParam:`

                  - `List<BashCodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue type = "bash_code_execution_output"`

                  - `long returnCode`

                  - `String stderr`

                  - `String stdout`

                  - `JsonValue type = "bash_code_execution_result"`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "bash_code_execution_tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class TextEditorCodeExecutionToolResultBlockParam:`

              - `Content content`

                - `class TextEditorCodeExecutionToolResultErrorParam:`

                  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `FILE_NOT_FOUND("file_not_found")`

                  - `JsonValue type = "text_editor_code_execution_tool_result_error"`

                  - `Optional<String> errorMessage`

                - `class TextEditorCodeExecutionViewResultBlockParam:`

                  - `String content`

                  - `FileType fileType`

                    - `TEXT("text")`

                    - `IMAGE("image")`

                    - `PDF("pdf")`

                  - `JsonValue type = "text_editor_code_execution_view_result"`

                  - `Optional<Long> numLines`

                  - `Optional<Long> startLine`

                  - `Optional<Long> totalLines`

                - `class TextEditorCodeExecutionCreateResultBlockParam:`

                  - `boolean isFileUpdate`

                  - `JsonValue type = "text_editor_code_execution_create_result"`

                - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

                  - `JsonValue type = "text_editor_code_execution_str_replace_result"`

                  - `Optional<List<String>> lines`

                  - `Optional<Long> newLines`

                  - `Optional<Long> newStart`

                  - `Optional<Long> oldLines`

                  - `Optional<Long> oldStart`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "text_editor_code_execution_tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class ToolSearchToolResultBlockParam:`

              - `Content content`

                - `class ToolSearchToolResultErrorParam:`

                  - `ToolSearchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `JsonValue type = "tool_search_tool_result_error"`

                  - `Optional<String> errorMessage`

                - `class ToolSearchToolSearchResultBlockParam:`

                  - `List<ToolReferenceBlockParam> toolReferences`

                    - `String toolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonValue type = "tool_reference"`

                    - `Optional<CacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                  - `JsonValue type = "tool_search_tool_search_result"`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type = "tool_search_tool_result"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class ContainerUploadBlockParam:`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `String fileId`

              - `JsonValue type = "container_upload"`

              - `Optional<CacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

        - `Role role`

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

          Our most capable model for cybersecurity and biology research, available through trusted access programs

        - `CLAUDE_SONNET_5("claude-sonnet-5")`

          High-performance model for coding and agents

        - `CLAUDE_FABLE_5("claude-fable-5")`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `CLAUDE_MYTHOS_5("claude-mythos-5")`

          Most capable model for cybersecurity and biology research

        - `CLAUDE_OPUS_5("claude-opus-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

          New class of intelligence, strongest in coding and cybersecurity

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Optional<CacheControlEphemeral> cacheControl`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `Optional<MessageCreateParamsContainer> container`

        Container identifier for reuse across requests.

        - `class ContainerParams:`

          Container parameters with skills to be loaded.

          - `Optional<String> id`

            Container id

          - `Optional<List<SkillParams>> skills`

            List of skills to load in the container

            maxItems: 20

            - `String skillId`

              Skill ID

              maxLength: 64, minLength: 1

            - `Type type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `ANTHROPIC("anthropic")`

              - `CUSTOM("custom")`

            - `Optional<String> version`

              Skill version or 'latest' for most recent version

              maxLength: 64, minLength: 1

        - `String`

      - `Optional<String> inferenceGeo`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Optional<Metadata> metadata`

        An object describing metadata about the request.

        - `Optional<String> userId`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

          maxLength: 512

      - `Optional<OutputConfig> outputConfig`

        Configuration options for the model's output, such as the output format.

        - `Optional<Effort> effort`

          All possible effort levels.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

        - `Optional<JsonOutputFormat> format`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `Schema schema`

            The JSON schema of the format

          - `JsonValue type = "json_schema"`

      - `Optional<ServiceTier> serviceTier`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `AUTO("auto")`

        - `STANDARD_ONLY("standard_only")`

      - `Optional<List<String>> stopSequences`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `Optional<Boolean> stream`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

      - `Optional<System> system`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

        - `String`

        - `List<TextBlockParam>`

          - `String text`

            minLength: 1

          - `JsonValue type = "text"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<List<TextCitationParam>> citations`

      - `Optional<ThinkingConfigParam> thinking`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `class ThinkingConfigEnabled:`

          - `long budgetTokens`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            minimum: 1024

          - `JsonValue type = "enabled"`

          - `Optional<Display> display`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `SUMMARIZED("summarized")`

            - `OMITTED("omitted")`

        - `class ThinkingConfigDisabled:`

          - `JsonValue type = "disabled"`

        - `class ThinkingConfigAdaptive:`

          - `JsonValue type = "adaptive"`

          - `Optional<Display> display`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `SUMMARIZED("summarized")`

            - `OMITTED("omitted")`

      - `Optional<ToolChoice> toolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `class ToolChoiceAuto:`

          The model will automatically decide whether to use tools.

          - `JsonValue type = "auto"`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `class ToolChoiceAny:`

          The model will use any available tools.

          - `JsonValue type = "any"`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceTool:`

          The model will use the specified tool with `tool_choice.name`.

          - `String name`

            The name of the tool to use.

          - `JsonValue type = "tool"`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceNone:`

          The model will not be allowed to use tools.

          - `JsonValue type = "none"`

      - `Optional<List<ToolUnion>> tools`

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

        - `class Tool:`

          - `InputSchema inputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `JsonValue type = "object"`

            - `Optional<Properties> properties`

            - `Optional<List<String>> required`

          - `String name`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<String> description`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `Optional<Boolean> eagerInputStreaming`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<Type> type`

        - `class ToolBash20250124:`

          - `JsonValue name = "bash"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "bash_20250124"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250522:`

          - `JsonValue name = "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "code_execution_20250522"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250825:`

          - `JsonValue name = "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "code_execution_20250825"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20260120:`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `JsonValue name = "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "code_execution_20260120"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20260521:`

          Code execution tool with REPL state persistence.

          - `JsonValue name = "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "code_execution_20260521"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BrowserToolset20260801:`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `JsonValue type = "browser_toolset_20260801"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BrowserToolsetConfigs> configs`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `Optional<BrowserCloseTabConfig> closeTab`

              `close_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserDoubleClickConfig> doubleClick`

              `double_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserFileUploadConfig> fileUpload`

              `file_upload`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserFindConfig> find`

              `find`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserFormInputConfig> formInput`

              `form_input`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserGetPageTextConfig> getPageText`

              `get_page_text`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserHoldKeyConfig> holdKey`

              `hold_key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserHoverConfig> hover`

              `hover`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserJavascriptExecConfig> javascriptExec`

              `javascript_exec`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserKeyConfig> key`

              `key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserLeftClickConfig> leftClick`

              `left_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserLeftClickDragConfig> leftClickDrag`

              `left_click_drag`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserLeftMouseDownConfig> leftMouseDown`

              `left_mouse_down`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserLeftMouseUpConfig> leftMouseUp`

              `left_mouse_up`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserListTabsConfig> listTabs`

              `list_tabs`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserMiddleClickConfig> middleClick`

              `middle_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserMouseMoveConfig> mouseMove`

              `mouse_move`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserNavigateConfig> navigate`

              `navigate`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserNewTabConfig> newTab`

              `new_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserReadConsoleConfig> readConsole`

              `read_console`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserReadNetworkConfig> readNetwork`

              `read_network`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserReadPageConfig> readPage`

              `read_page`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserRightClickConfig> rightClick`

              `right_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserScreenshotConfig> screenshot`

              `screenshot`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserScrollConfig> scroll`

              `scroll`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserScrollToConfig> scrollTo`

              `scroll_to`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserSwitchTabConfig> switchTab`

              `switch_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserTripleClickConfig> tripleClick`

              `triple_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserTypeConfig> type`

              `type`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserWaitConfig> wait`

              `wait`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BrowserZoomConfig> zoom`

              `zoom`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class MemoryTool20250818:`

          - `JsonValue name = "memory"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "memory_20250818"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ComputerToolset20260801:`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `JsonValue type = "computer_toolset_20260801"`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<ComputerToolsetConfigs> configs`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `Optional<ComputerCursorPositionConfig> cursorPosition`

              `cursor_position`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerDoubleClickConfig> doubleClick`

              `double_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerHoldKeyConfig> holdKey`

              `hold_key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerKeyConfig> key`

              `key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftClickConfig> leftClick`

              `left_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftClickDragConfig> leftClickDrag`

              `left_click_drag`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftMouseDownConfig> leftMouseDown`

              `left_mouse_down`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerLeftMouseUpConfig> leftMouseUp`

              `left_mouse_up`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerMiddleClickConfig> middleClick`

              `middle_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerMouseMoveConfig> mouseMove`

              `mouse_move`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerRightClickConfig> rightClick`

              `right_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerScreenshotConfig> screenshot`

              `screenshot`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerScrollConfig> scroll`

              `scroll`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerTripleClickConfig> tripleClick`

              `triple_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerTypeConfig> type`

              `type`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerWaitConfig> wait`

              `wait`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<ComputerZoomConfig> zoom`

              `zoom`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class ToolTextEditor20250124:`

          - `JsonValue name = "str_replace_editor"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "text_editor_20250124"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250429:`

          - `JsonValue name = "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "text_editor_20250429"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250728:`

          - `JsonValue name = "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "text_editor_20250728"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Long> maxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20250305:`

          - `JsonValue name = "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_search_20250305"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonValue type = "approximate"`

            - `Optional<String> city`

              The city of the user.

              maxLength: 255, minLength: 1

            - `Optional<String> country`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

              maxLength: 2, minLength: 2

            - `Optional<String> region`

              The region of the user.

              maxLength: 255, minLength: 1

            - `Optional<String> timezone`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

              maxLength: 255, minLength: 1

        - `class WebFetchTool20250910:`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_fetch_20250910"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20260209:`

          - `JsonValue name = "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_search_20260209"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class WebFetchTool20260209:`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_fetch_20260209"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebFetchTool20260309:`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_fetch_20260309"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<Boolean> useCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class WebSearchTool20260318:`

          - `JsonValue name = "web_search"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_search_20260318"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<ResponseInclusion> responseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `FULL("full")`

            - `EXCLUDED("excluded")`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<UserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class WebFetchTool20260318:`

          - `JsonValue name = "web_fetch"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type = "web_fetch_20260318"`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<CitationsConfigParam> citations`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<ResponseInclusion> responseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `FULL("full")`

            - `EXCLUDED("excluded")`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<Boolean> useCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class ToolSearchToolBm25_20251119:`

          - `JsonValue name = "tool_search_tool_bm25"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type type`

            - `TOOL_SEARCH_TOOL_BM25_20251119("tool_search_tool_bm25_20251119")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolRegex20251119:`

          - `JsonValue name = "tool_search_tool_regex"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type type`

            - `TOOL_SEARCH_TOOL_REGEX_20251119("tool_search_tool_regex_20251119")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<CacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

      - `Optional<Double> temperature`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

        maximum: 1, minimum: 0

      - `Optional<Long> topK`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

        minimum: 0

      - `Optional<Double> topP`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

        maximum: 1, minimum: 0

#### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.Model;
import com.anthropic.models.messages.batches.BatchCreateParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchCreateParams params = BatchCreateParams.builder()
            .addRequest(BatchCreateParams.Request.builder()
                .customId("my-custom-id-1")
                .params(BatchCreateParams.Request.Params.builder()
                    .maxTokens(1024L)
                    .addUserMessage("Hello, world")
                    .model(Model.CLAUDE_OPUS_5)
                    .build())
                .build())
            .build();
        MessageBatch messageBatch = client.messages().batches().create(params);
    }
}
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

`MessageBatch messages().batches().retrieve(params = BatchRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchRetrieveParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

#### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchRetrieveParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageBatch messageBatch = client.messages().batches().retrieve("message_batch_id");
    }
}
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

`BatchListPage messages().batches().list(params = BatchListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchListPage;
import com.anthropic.models.messages.batches.BatchListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchListPage page = client.messages().batches().list();
    }
}
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

`MessageBatch messages().batches().cancel(params = BatchCancelParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchCancelParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

#### Returns

- `class MessageBatch:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `Optional<LocalDateTime> cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

    - `IN_PROGRESS("in_progress")`

    - `CANCELING("canceling")`

    - `ENDED("ended")`

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `long canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `long errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `long expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `long processing`

      Number of requests in the Message Batch that are processing.

    - `long succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `Optional<String> resultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonValue type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchCancelParams;
import com.anthropic.models.messages.batches.MessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MessageBatch messageBatch = client.messages().batches().cancel("message_batch_id");
    }
}
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

`DeletedMessageBatch messages().batches().delete(params = BatchDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchDeleteParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

#### Returns

- `class DeletedMessageBatch:`

  - `String id`

    ID of the Message Batch.

  - `JsonValue type = "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchDeleteParams;
import com.anthropic.models.messages.batches.DeletedMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeletedMessageBatch deletedMessageBatch = client.messages().batches().delete("message_batch_id");
    }
}
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`MessageBatchIndividualResponse messages().batches().resultsStreaming(params = BatchResultsParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `BatchResultsParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

#### Returns

- `class MessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class MessageBatchSucceededResult:`

      - `Message message`

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<Container> container`

          Information about the container used in the request (for the code execution tool)

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

            format: date-time

          - `Optional<List<ContainerSkill>> skills`

            Skills loaded in the container

            - `String skillId`

              Skill ID

              maxLength: 64, minLength: 1

            - `Type type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `ANTHROPIC("anthropic")`

              - `CUSTOM("custom")`

            - `String version`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

        - `List<ContentBlock> content`

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

          - `class TextBlock:`

            - `Optional<List<TextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class CitationCharLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                  minimum: 0

                - `JsonValue type = "char_location"`

              - `class CitationPageLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                  minimum: 1

                - `JsonValue type = "page_location"`

              - `class CitationContentBlockLocation:`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `Optional<String> fileId`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `JsonValue type = "content_block_location"`

              - `class CitationsWebSearchResultLocation:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512

                - `JsonValue type = "web_search_result_location"`

                - `String url`

              - `class CitationsSearchResultLocation:`

                - `String citedText`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `long endBlockIndex`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `long searchResultIndex`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `String source`

                - `long startBlockIndex`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `Optional<String> title`

                - `JsonValue type = "search_result_location"`

            - `String text`

              maxLength: 5000000, minLength: 0

            - `JsonValue type = "text"`

          - `class ThinkingBlock:`

            - `String signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `String thinking`

              The text of Claude's thinking process for this block.

            - `JsonValue type = "thinking"`

          - `class RedactedThinkingBlock:`

            - `String data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `JsonValue type = "redacted_thinking"`

          - `class ToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue type = "direct"`

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type = "code_execution_20250825"`

              - `class ServerToolCaller20260120:`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type = "code_execution_20260120"`

            - `Input input`

            - `String name`

              minLength: 1

            - `JsonValue type = "tool_use"`

            - `Optional<String> toolsetName`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class ServerToolUseBlock:`

            - `String id`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120:`

            - `Input input`

            - `Name name`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

            - `JsonValue type = "server_tool_use"`

          - `class WebSearchToolResultBlock:`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120:`

            - `WebSearchToolResultBlockContent content`

              - `class WebSearchToolResultError:`

                - `WebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

                - `JsonValue type = "web_search_tool_result_error"`

              - `List<WebSearchResultBlock>`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `JsonValue type = "web_search_result"`

                - `String url`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "web_search_tool_result"`

          - `class WebFetchToolResultBlock:`

            - `Caller caller`

              Tool invocation directly from the model.

              - `class DirectCaller:`

                Tool invocation directly from the model.

              - `class ServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class ServerToolCaller20260120:`

            - `Content content`

              - `class WebFetchToolResultErrorBlock:`

                - `WebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                - `JsonValue type = "web_fetch_tool_result_error"`

              - `class WebFetchBlock:`

                - `DocumentBlock content`

                  - `Optional<CitationsConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class Base64PdfSource:`

                      - `String data`

                        format: byte

                      - `JsonValue mediaType = "application/pdf"`

                      - `JsonValue type = "base64"`

                    - `class PlainTextSource:`

                      - `String data`

                      - `JsonValue mediaType = "text/plain"`

                      - `JsonValue type = "text"`

                  - `Optional<String> title`

                    The title of the document

                  - `JsonValue type = "document"`

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonValue type = "web_fetch_result"`

                - `String url`

                  Fetched content URL

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "web_fetch_tool_result"`

          - `class CodeExecutionToolResultBlock:`

            - `CodeExecutionToolResultBlockContent content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class CodeExecutionToolResultError:`

                - `CodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `JsonValue type = "code_execution_tool_result_error"`

              - `class CodeExecutionResultBlock:`

                - `List<CodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type = "code_execution_output"`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type = "code_execution_result"`

              - `class EncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `List<CodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type = "code_execution_output"`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

                - `JsonValue type = "encrypted_code_execution_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "code_execution_tool_result"`

          - `class BashCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BashCodeExecutionToolResultError:`

                - `BashCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                - `JsonValue type = "bash_code_execution_tool_result_error"`

              - `class BashCodeExecutionResultBlock:`

                - `List<BashCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type = "bash_code_execution_output"`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type = "bash_code_execution_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "bash_code_execution_tool_result"`

          - `class TextEditorCodeExecutionToolResultBlock:`

            - `Content content`

              - `class TextEditorCodeExecutionToolResultError:`

                - `TextEditorCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

                - `JsonValue type = "text_editor_code_execution_tool_result_error"`

              - `class TextEditorCodeExecutionViewResultBlock:`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

                - `JsonValue type = "text_editor_code_execution_view_result"`

              - `class TextEditorCodeExecutionCreateResultBlock:`

                - `boolean isFileUpdate`

                - `JsonValue type = "text_editor_code_execution_create_result"`

              - `class TextEditorCodeExecutionStrReplaceResultBlock:`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

                - `JsonValue type = "text_editor_code_execution_str_replace_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "text_editor_code_execution_tool_result"`

          - `class ToolSearchToolResultBlock:`

            - `Content content`

              - `class ToolSearchToolResultError:`

                - `ToolSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

                - `JsonValue type = "tool_search_tool_result_error"`

              - `class ToolSearchToolSearchResultBlock:`

                - `List<ToolReferenceBlock> toolReferences`

                  - `String toolName`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `JsonValue type = "tool_reference"`

                - `JsonValue type = "tool_search_tool_search_result"`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type = "tool_search_tool_result"`

          - `class ContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `String fileId`

            - `JsonValue type = "container_upload"`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `CLAUDE_MYTHOS_5_1("claude-mythos-5-1")`

            Our most capable model for cybersecurity and biology research, available through trusted access programs

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_MYTHOS_5("claude-mythos-5")`

            Most capable model for cybersecurity and biology research

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_MYTHOS_PREVIEW("claude-mythos-preview")`

            New class of intelligence, strongest in coding and cybersecurity

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `JsonValue role = "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `Optional<RefusalStopDetails> stopDetails`

          Structured information about a refusal.

          - `Optional<Category> category`

            The policy category that triggered a refusal.

            - `CYBER("cyber")`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `BIO("bio")`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `FRONTIER_LLM("frontier_llm")`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `REASONING_EXTRACTION("reasoning_extraction")`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `GENERAL_HARMS("general_harms")`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `Optional<String> explanation`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

          - `JsonValue type = "refusal"`

        - `Optional<StopReason> stopReason`

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

          - `END_TURN("end_turn")`

          - `MAX_TOKENS("max_tokens")`

          - `STOP_SEQUENCE("stop_sequence")`

          - `TOOL_USE("tool_use")`

          - `PAUSE_TURN("pause_turn")`

          - `REFUSAL("refusal")`

          - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonValue type = "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `Usage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<CacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

            - `long ephemeral1hInputTokens`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `long ephemeral5mInputTokens`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `Optional<Long> cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `Optional<Long> cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `Optional<OutputTokensDetails> outputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `long thinkingTokens`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `Optional<ServerToolUsage> serverToolUse`

            The number of server tool requests.

            - `long webFetchRequests`

              The number of web fetch tool requests.

              minimum: 0

            - `long webSearchRequests`

              The number of web search tool requests.

              minimum: 0

          - `Optional<ServiceTier> serviceTier`

            If the request used the priority, standard, or batch tier.

            - `STANDARD("standard")`

            - `PRIORITY("priority")`

            - `BATCH("batch")`

      - `JsonValue type = "succeeded"`

    - `class MessageBatchErroredResult:`

      - `ErrorResponse error`

        - `ErrorObject error`

          - `class InvalidRequestError:`

            - `String message`

            - `JsonValue type = "invalid_request_error"`

          - `class AuthenticationError:`

            - `String message`

            - `JsonValue type = "authentication_error"`

          - `class BillingError:`

            - `String message`

            - `JsonValue type = "billing_error"`

          - `class PermissionError:`

            - `String message`

            - `JsonValue type = "permission_error"`

          - `class NotFoundError:`

            - `String message`

            - `JsonValue type = "not_found_error"`

          - `class RateLimitError:`

            - `String message`

            - `JsonValue type = "rate_limit_error"`

          - `class GatewayTimeoutError:`

            - `String message`

            - `JsonValue type = "timeout_error"`

          - `class ApiErrorObject:`

            - `String message`

            - `JsonValue type = "api_error"`

          - `class OverloadedError:`

            - `String message`

            - `JsonValue type = "overloaded_error"`

        - `Optional<String> requestId`

        - `JsonValue type = "error"`

      - `JsonValue type = "errored"`

    - `class MessageBatchCanceledResult:`

      - `JsonValue type = "canceled"`

    - `class MessageBatchExpiredResult:`

      - `JsonValue type = "expired"`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.messages.batches.BatchResultsParams;
import com.anthropic.models.messages.batches.MessageBatchIndividualResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<MessageBatchIndividualResponse> messageBatchIndividualResponse = client.messages().batches().resultsStreaming("message_batch_id");
    }
}
```
