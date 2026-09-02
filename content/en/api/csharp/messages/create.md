# Create a Message

`Message Messages.Create(parameters, cancellationToken = default)`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

## Parameters

- `MessageCreateParams parameters`

  - `required long maxTokens`

    Body param: The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

    Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

    minimum: 0

  - `required IReadOnlyList<MessageParam> messages`

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

    - `required Content Content`

      - `string`

      - `IReadOnlyList<ContentBlockParam>`

        - `class TextBlockParam:`

          - `required string Text`

            minLength: 1

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type constant`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `Ttl5m`

              - `Ttl1h`

          - `IReadOnlyList<TextCitationParam>? Citations`

            - `class CitationCharLocationParam:`

              - `required string CitedText`

              - `required long DocumentIndex`

                minimum: 0

              - `required string? DocumentTitle`

                maxLength: 500, minLength: 1

              - `required long EndCharIndex`

              - `required long StartCharIndex`

                minimum: 0

              - `JsonElement Type constant`

            - `class CitationPageLocationParam:`

              - `required string CitedText`

              - `required long DocumentIndex`

                minimum: 0

              - `required string? DocumentTitle`

                maxLength: 500, minLength: 1

              - `required long EndPageNumber`

              - `required long StartPageNumber`

                minimum: 1

              - `JsonElement Type constant`

            - `class CitationContentBlockLocationParam:`

              - `required string CitedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `required long DocumentIndex`

                minimum: 0

              - `required string? DocumentTitle`

                maxLength: 500, minLength: 1

              - `required long EndBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `required long StartBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `JsonElement Type constant`

            - `class CitationWebSearchResultLocationParam:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

                maxLength: 512, minLength: 1

              - `JsonElement Type constant`

              - `required string Url`

                minLength: 1

            - `class CitationSearchResultLocationParam:`

              - `required string CitedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `required long EndBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `required long SearchResultIndex`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

                minimum: 0

              - `required string Source`

              - `required long StartBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `required string? Title`

              - `JsonElement Type constant`

        - `class ImageBlockParam:`

          - `required Source Source`

            - `class Base64ImageSource:`

              - `required string Data`

                format: byte

              - `required MediaType MediaType`

                - `ImageJpeg`

                - `ImagePng`

                - `ImageGif`

                - `ImageWebP`

              - `JsonElement Type constant`

            - `class UrlImageSource:`

              - `JsonElement Type constant`

              - `required string Url`

            - `class FileImageSource:`

              - `required string FileID`

              - `JsonElement Type constant`

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `ImageTransformationsParam? Transformations`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

            - `OversizedImage OversizedImage`

              What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

              - `Downsize`

              - `Error`

        - `class DocumentBlockParam:`

          - `required Source Source`

            - `class Base64PdfSource:`

              - `required string Data`

                format: byte

              - `JsonElement MediaType constant`

              - `JsonElement Type constant`

            - `class PlainTextSource:`

              - `required string Data`

              - `JsonElement MediaType constant`

              - `JsonElement Type constant`

            - `class ContentBlockSource:`

              - `required Content Content`

                - `string`

                - `IReadOnlyList<ContentBlockSourceContent>`

                  - `class TextBlockParam:`

                  - `class ImageBlockParam:`

              - `JsonElement Type constant`

            - `class UrlPdfSource:`

              - `JsonElement Type constant`

              - `required string Url`

            - `class FileDocumentSource:`

              - `required string FileID`

              - `JsonElement Type constant`

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `CitationsConfigParam? Citations`

            - `bool Enabled`

          - `string? Context`

            minLength: 1

          - `string? Title`

            maxLength: 500, minLength: 1

        - `class SearchResultBlockParam:`

          - `required IReadOnlyList<TextBlockParam> Content`

            - `required string Text`

              minLength: 1

            - `JsonElement Type constant`

            - `CacheControlEphemeral? CacheControl`

              Create a cache control breakpoint at this content block.

            - `IReadOnlyList<TextCitationParam>? Citations`

          - `required string Source`

          - `required string Title`

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `CitationsConfigParam Citations`

        - `class ThinkingBlockParam:`

          - `required string Signature`

            The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

            Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

          - `required string Thinking`

            The `thinking` text of this block as returned by the API.

          - `JsonElement Type constant`

        - `class RedactedThinkingBlockParam:`

          - `required string Data`

            The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `JsonElement Type constant`

        - `class ToolUseBlockParam:`

          - `required string ID`

            pattern: ^[a-zA-Z0-9_-]+$

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

            maxLength: 200, minLength: 1

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type constant`

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

            - `class ServerToolCaller20260120:`

              - `required string ToolID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

          - `string? ToolsetName`

            For a toolset member tool_use, the toolset family this member belongs to.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ToolResultBlockParam:`

          - `required string ToolUseID`

            pattern: ^[a-zA-Z0-9_-]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Content Content`

            - `string`

            - `IReadOnlyList<Block>`

              - `class TextBlockParam:`

              - `class ImageBlockParam:`

              - `class SearchResultBlockParam:`

              - `class DocumentBlockParam:`

              - `class ToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `required string ToolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonElement Type constant`

                - `CacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

              - `class BrowserStateBlockParam:`

                The caller's browser state after a browser toolset member call —
                the full inventory of open tabs, which tab is active, and any side
                effects (tabs opened, download state changes) the call produced.

                At most one per `tool_result`, only on a non-error result answering a
                browser toolset member `tool_use`. The server renders the
                model-visible text from it; the model never sees the raw fields.

                - `required IReadOnlyList<BrowserStateTabEntry> Tabs`

                  All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                  maxItems: 100

                  - `required string TabID`

                    The caller-assigned identifier for this tab, unique within the inventory.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `required string Title`

                    The title of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `required string Url`

                    The URL of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `bool Active`

                    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                - `JsonElement Type constant`

                - `CacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

                - `IReadOnlyList<BrowserStateChange>? StateChanges`

                  Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                  maxItems: 200, minItems: 1

                  - `class BrowserStateChangeTabOpened:`

                    A tab this call's execution opened that remains open at its end —
                    the creation delta of the `tabs` inventory, not an event log.

                    Carries only the `tab_id`; the tab's `title` and `url` live on its
                    `tabs` entry, which must include the same `tab_id`. A tab opened
                    during a failed call gets no deferred `tab_opened`; it simply appears
                    in the next result's `tabs` inventory.

                    - `required string TabID`

                      The `tab_id` of the opened tab, present in `tabs`.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type constant`

                  - `class BrowserStateChangeDownloadStarted:`

                    A file download that started during this call.

                    - `required string DownloadID`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type constant`

                    - `required string Url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `class BrowserStateChangeDownloadCompleted:`

                    A file download that finished during this call, reported with the
                    same `download_id` as its `download_started` — or without a prior
                    `download_started`, when the download finished during the call that
                    started it (at most one state change per `download_id` per result).

                    - `required string DownloadID`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type constant`

                    - `required string Url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `string? Path`

                      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                    - `long? SizeBytes`

                      The completed download's size.

                      minimum: 0

                  - `class BrowserStateChangeDownloadFailed:`

                    A file download that failed — or was cancelled — during this call.

                    - `required string DownloadID`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type constant`

                    - `required string Url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `string? Error`

                      The failure or cancellation detail, when known.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

          - `bool IsError`

          - `string? ToolsetName`

            For a toolset member tool_result, the toolset family of the paired tool_use.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class ServerToolUseBlockParam:`

          - `required string ID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required Name Name`

            - `WebSearch`

            - `WebFetch`

            - `CodeExecution`

            - `BashCodeExecution`

            - `TextEditorCodeExecution`

            - `ToolSearchToolRegex`

            - `ToolSearchToolBm25`

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class WebSearchToolResultBlockParam:`

          - `required WebSearchToolResultBlockParamContent Content`

            - `IReadOnlyList<WebSearchResultBlockParam>`

              - `required string EncryptedContent`

              - `required string Title`

              - `JsonElement Type constant`

              - `required string Url`

              - `string? PageAge`

            - `class WebSearchToolRequestError:`

              - `required WebSearchToolResultErrorCode ErrorCode`

                - `InvalidToolInput`

                - `Unavailable`

                - `MaxUsesExceeded`

                - `TooManyRequests`

                - `QueryTooLong`

                - `RequestTooLarge`

              - `JsonElement Type constant`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class WebFetchToolResultBlockParam:`

          - `required Content Content`

            - `class WebFetchToolResultErrorBlockParam:`

              - `required WebFetchToolResultErrorCode ErrorCode`

                - `InvalidToolInput`

                - `UrlTooLong`

                - `UrlNotAllowed`

                - `UrlNotInPriorContext`

                - `UrlNotAccessible`

                - `UnsupportedContentType`

                - `TooManyRequests`

                - `MaxUsesExceeded`

                - `Unavailable`

              - `JsonElement Type constant`

            - `class WebFetchBlockParam:`

              - `required DocumentBlockParam Content`

              - `JsonElement Type constant`

              - `required string Url`

                Fetched content URL

              - `string? RetrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class DirectCaller:`

              Tool invocation directly from the model.

            - `class ServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class ServerToolCaller20260120:`

        - `class CodeExecutionToolResultBlockParam:`

          - `required CodeExecutionToolResultBlockParamContent Content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class CodeExecutionToolResultErrorParam:`

              - `required CodeExecutionToolResultErrorCode ErrorCode`

                - `InvalidToolInput`

                - `Unavailable`

                - `TooManyRequests`

                - `ExecutionTimeExceeded`

              - `JsonElement Type constant`

            - `class CodeExecutionResultBlockParam:`

              - `required IReadOnlyList<CodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type constant`

              - `required long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type constant`

            - `class EncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `required IReadOnlyList<CodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type constant`

              - `required string EncryptedStdout`

              - `required long ReturnCode`

              - `required string Stderr`

              - `JsonElement Type constant`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BashCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BashCodeExecutionToolResultErrorParam:`

              - `required BashCodeExecutionToolResultErrorCode ErrorCode`

                - `InvalidToolInput`

                - `Unavailable`

                - `TooManyRequests`

                - `ExecutionTimeExceeded`

                - `OutputFileTooLarge`

              - `JsonElement Type constant`

            - `class BashCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BashCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type constant`

              - `required long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type constant`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class TextEditorCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class TextEditorCodeExecutionToolResultErrorParam:`

              - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

                - `InvalidToolInput`

                - `Unavailable`

                - `TooManyRequests`

                - `ExecutionTimeExceeded`

                - `FileNotFound`

              - `JsonElement Type constant`

              - `string? ErrorMessage`

            - `class TextEditorCodeExecutionViewResultBlockParam:`

              - `required string Content`

              - `required FileType FileType`

                - `Text`

                - `Image`

                - `Pdf`

              - `JsonElement Type constant`

              - `long? NumLines`

              - `long? StartLine`

              - `long? TotalLines`

            - `class TextEditorCodeExecutionCreateResultBlockParam:`

              - `required bool IsFileUpdate`

              - `JsonElement Type constant`

            - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonElement Type constant`

              - `IReadOnlyList<string>? Lines`

              - `long? NewLines`

              - `long? NewStart`

              - `long? OldLines`

              - `long? OldStart`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class ToolSearchToolResultBlockParam:`

          - `required Content Content`

            - `class ToolSearchToolResultErrorParam:`

              - `required ToolSearchToolResultErrorCode ErrorCode`

                - `InvalidToolInput`

                - `Unavailable`

                - `TooManyRequests`

                - `ExecutionTimeExceeded`

              - `JsonElement Type constant`

              - `string? ErrorMessage`

            - `class ToolSearchToolSearchResultBlockParam:`

              - `required IReadOnlyList<ToolReferenceBlockParam> ToolReferences`

                - `required string ToolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonElement Type constant`

                - `CacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

              - `JsonElement Type constant`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class ContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `required string FileID`

          - `JsonElement Type constant`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

    - `required Role Role`

      - `User`

      - `Assistant`

      - `System`

  - `required Model model`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `CacheControlEphemeral? cacheControl`

    Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `MessageCreateParamsContainer? container`

    Body param: Container identifier for reuse across requests.

  - `string? inferenceGeo`

    Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `Metadata metadata`

    Body param: An object describing metadata about the request.

  - `OutputConfig outputConfig`

    Body param: Configuration options for the model's output, such as the output format.

  - `ServiceTier serviceTier`

    Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

    - `Auto`

    - `StandardOnly`

  - `IReadOnlyList<string> stopSequences`

    Body param: Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `System system`

    Body param: System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `string`

    - `IReadOnlyList<TextBlockParam>`

      - `required string Text`

        minLength: 1

      - `JsonElement Type constant`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `IReadOnlyList<TextCitationParam>? Citations`

  - `ThinkingConfigParam thinking`

    Body param: Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `ToolChoice toolChoice`

    Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `IReadOnlyList<ToolUnion> tools`

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

    - `class Tool:`

      - `required InputSchema InputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonElement Type constant`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `string Description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `bool? EagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `Type? Type`

    - `class ToolBash20250124:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250522:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20250825:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class CodeExecutionTool20260521:`

      Code execution tool with REPL state persistence.

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BrowserToolset20260801:`

      The browser toolset: a single `tools[]` entry (carrying no
      `name`) that declares the browser tool family. The model is served
      the family's tool with any members disabled via `configs` removed
      from its schema.

      - `JsonElement Type constant`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BrowserToolsetConfigs? Configs`

        Per-member configuration for `browser_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `BrowserCloseTabConfig? CloseTab`

          `close_tab`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserDoubleClickConfig? DoubleClick`

          `double_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserFileUploadConfig? FileUpload`

          `file_upload`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserFindConfig? Find`

          `find`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserFormInputConfig? FormInput`

          `form_input`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserGetPageTextConfig? GetPageText`

          `get_page_text`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserHoldKeyConfig? HoldKey`

          `hold_key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserHoverConfig? Hover`

          `hover`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserJavascriptExecConfig? JavascriptExec`

          `javascript_exec`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserKeyConfig? Key`

          `key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserLeftClickConfig? LeftClick`

          `left_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserLeftClickDragConfig? LeftClickDrag`

          `left_click_drag`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserLeftMouseDownConfig? LeftMouseDown`

          `left_mouse_down`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserLeftMouseUpConfig? LeftMouseUp`

          `left_mouse_up`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserListTabsConfig? ListTabs`

          `list_tabs`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserMiddleClickConfig? MiddleClick`

          `middle_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserMouseMoveConfig? MouseMove`

          `mouse_move`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserNavigateConfig? Navigate`

          `navigate`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserNewTabConfig? NewTab`

          `new_tab`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserReadConsoleConfig? ReadConsole`

          `read_console`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserReadNetworkConfig? ReadNetwork`

          `read_network`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserReadPageConfig? ReadPage`

          `read_page`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserRightClickConfig? RightClick`

          `right_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserScreenshotConfig? Screenshot`

          `screenshot`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserScrollConfig? Scroll`

          `scroll`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserScrollToConfig? ScrollTo`

          `scroll_to`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserSwitchTabConfig? SwitchTab`

          `switch_tab`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserTripleClickConfig? TripleClick`

          `triple_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserTypeConfig? Type`

          `type`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserWaitConfig? Wait`

          `wait`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BrowserZoomConfig? Zoom`

          `zoom`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class MemoryTool20250818:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

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

      - `JsonElement Type constant`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `ComputerToolsetConfigs? Configs`

        Per-member configuration for `computer_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `ComputerCursorPositionConfig? CursorPosition`

          `cursor_position`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerDoubleClickConfig? DoubleClick`

          `double_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerHoldKeyConfig? HoldKey`

          `hold_key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerKeyConfig? Key`

          `key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerLeftClickConfig? LeftClick`

          `left_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerLeftClickDragConfig? LeftClickDrag`

          `left_click_drag`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerLeftMouseDownConfig? LeftMouseDown`

          `left_mouse_down`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerLeftMouseUpConfig? LeftMouseUp`

          `left_mouse_up`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerMiddleClickConfig? MiddleClick`

          `middle_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerMouseMoveConfig? MouseMove`

          `mouse_move`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerRightClickConfig? RightClick`

          `right_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerScreenshotConfig? Screenshot`

          `screenshot`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerScrollConfig? Scroll`

          `scroll`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerTripleClickConfig? TripleClick`

          `triple_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerTypeConfig? Type`

          `type`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerWaitConfig? Wait`

          `wait`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ComputerZoomConfig? Zoom`

          `zoom`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class ToolTextEditor20250124:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250429:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolTextEditor20250728:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `long? MaxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        minimum: 1

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20250305:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `UserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonElement Type constant`

        - `string? City`

          The city of the user.

          maxLength: 255, minLength: 1

        - `string? Country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          maxLength: 2, minLength: 2

        - `string? Region`

          The region of the user.

          maxLength: 255, minLength: 1

        - `string? Timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

          maxLength: 255, minLength: 1

    - `class WebFetchTool20250910:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `CitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebSearchTool20260209:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `UserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class WebFetchTool20260209:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `CitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class WebFetchTool20260309:`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `CitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `bool UseCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class WebSearchTool20260318:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `ResponseInclusion ResponseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `Full`

        - `Excluded`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `UserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class WebFetchTool20260318:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type constant`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `CitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `ResponseInclusion ResponseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `Full`

        - `Excluded`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `bool UseCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class ToolSearchToolBm25_20251119:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `required Type Type`

        - `ToolSearchToolBm25_20251119`

        - `ToolSearchToolBm25`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class ToolSearchToolRegex20251119:`

      - `JsonElement Name constant`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `required Type Type`

        - `ToolSearchToolRegex20251119`

        - `ToolSearchToolRegex`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct`

        - `CodeExecution20250825`

        - `CodeExecution20260120`

        - `CodeExecution20260521`

      - `CacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

  - `string userProfileID`

    Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

  - `double temperature`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    maximum: 1, minimum: 0

  - `long topK`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

    Body param: Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

    minimum: 0

  - `double topP`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

    maximum: 1, minimum: 0

## Returns

- `class Message:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required Container? Container`

    Information about the container used in the request (for the code execution tool)

    - `required string ID`

      Identifier for the container used in this request

    - `required DateTimeOffset ExpiresAt`

      The time at which the container will expire.

      format: date-time

    - `required IReadOnlyList<ContainerSkill>? Skills`

      Skills loaded in the container

      - `required string SkillID`

        Skill ID

        maxLength: 64, minLength: 1

      - `required ContainerSkillType Type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `Anthropic`

        - `Custom`

      - `required string Version`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `required IReadOnlyList<ContentBlock> Content`

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

      - `required IReadOnlyList<TextCitation>? Citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class CitationCharLocation:`

          - `required string CitedText`

          - `required long DocumentIndex`

            minimum: 0

          - `required string? DocumentTitle`

          - `required long EndCharIndex`

          - `required string? FileID`

          - `required long StartCharIndex`

            minimum: 0

          - `JsonElement Type constant`

        - `class CitationPageLocation:`

          - `required string CitedText`

          - `required long DocumentIndex`

            minimum: 0

          - `required string? DocumentTitle`

          - `required long EndPageNumber`

          - `required string? FileID`

          - `required long StartPageNumber`

            minimum: 1

          - `JsonElement Type constant`

        - `class CitationContentBlockLocation:`

          - `required string CitedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `required long DocumentIndex`

            minimum: 0

          - `required string? DocumentTitle`

          - `required long EndBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `required string? FileID`

          - `required long StartBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `JsonElement Type constant`

        - `class CitationsWebSearchResultLocation:`

          - `required string CitedText`

          - `required string EncryptedIndex`

          - `required string? Title`

            maxLength: 512

          - `JsonElement Type constant`

          - `required string Url`

        - `class CitationsSearchResultLocation:`

          - `required string CitedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `required long EndBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `required long SearchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `required string Source`

          - `required long StartBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `required string? Title`

          - `JsonElement Type constant`

      - `required string Text`

        maxLength: 5000000, minLength: 0

      - `JsonElement Type constant`

    - `class ThinkingBlock:`

      - `required string Signature`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `required string Thinking`

        The text of Claude's thinking process for this block.

      - `JsonElement Type constant`

    - `class RedactedThinkingBlock:`

      - `required string Data`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `JsonElement Type constant`

    - `class ToolUseBlock:`

      - `required string ID`

        pattern: ^[a-zA-Z0-9_-]+$

      - `required Caller Caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type constant`

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

        - `class ServerToolCaller20260120:`

          - `required string ToolID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type constant`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

        minLength: 1

      - `JsonElement Type constant`

      - `string? ToolsetName`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class ServerToolUseBlock:`

      - `required string ID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `required Caller Caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required Name Name`

        - `WebSearch`

        - `WebFetch`

        - `CodeExecution`

        - `BashCodeExecution`

        - `TextEditorCodeExecution`

        - `ToolSearchToolRegex`

        - `ToolSearchToolBm25`

      - `JsonElement Type constant`

    - `class WebSearchToolResultBlock:`

      - `required Caller Caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `required WebSearchToolResultBlockContent Content`

        - `class WebSearchToolResultError:`

          - `required WebSearchToolResultErrorCode ErrorCode`

            - `InvalidToolInput`

            - `Unavailable`

            - `MaxUsesExceeded`

            - `TooManyRequests`

            - `QueryTooLong`

            - `RequestTooLarge`

          - `JsonElement Type constant`

        - `IReadOnlyList<WebSearchResultBlock>`

          - `required string EncryptedContent`

          - `required string? PageAge`

          - `required string Title`

          - `JsonElement Type constant`

          - `required string Url`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type constant`

    - `class WebFetchToolResultBlock:`

      - `required Caller Caller`

        Tool invocation directly from the model.

        - `class DirectCaller:`

          Tool invocation directly from the model.

        - `class ServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class ServerToolCaller20260120:`

      - `required Content Content`

        - `class WebFetchToolResultErrorBlock:`

          - `required WebFetchToolResultErrorCode ErrorCode`

            - `InvalidToolInput`

            - `UrlTooLong`

            - `UrlNotAllowed`

            - `UrlNotInPriorContext`

            - `UrlNotAccessible`

            - `UnsupportedContentType`

            - `TooManyRequests`

            - `MaxUsesExceeded`

            - `Unavailable`

          - `JsonElement Type constant`

        - `class WebFetchBlock:`

          - `required DocumentBlock Content`

            - `required CitationsConfig? Citations`

              Citation configuration for the document

              - `required bool Enabled`

            - `required Source Source`

              - `class Base64PdfSource:`

                - `required string Data`

                  format: byte

                - `JsonElement MediaType constant`

                - `JsonElement Type constant`

              - `class PlainTextSource:`

                - `required string Data`

                - `JsonElement MediaType constant`

                - `JsonElement Type constant`

            - `required string? Title`

              The title of the document

            - `JsonElement Type constant`

          - `required string? RetrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonElement Type constant`

          - `required string Url`

            Fetched content URL

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type constant`

    - `class CodeExecutionToolResultBlock:`

      - `required CodeExecutionToolResultBlockContent Content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class CodeExecutionToolResultError:`

          - `required CodeExecutionToolResultErrorCode ErrorCode`

            - `InvalidToolInput`

            - `Unavailable`

            - `TooManyRequests`

            - `ExecutionTimeExceeded`

          - `JsonElement Type constant`

        - `class CodeExecutionResultBlock:`

          - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type constant`

          - `required long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type constant`

        - `class EncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `required IReadOnlyList<CodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type constant`

          - `required string EncryptedStdout`

          - `required long ReturnCode`

          - `required string Stderr`

          - `JsonElement Type constant`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type constant`

    - `class BashCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BashCodeExecutionToolResultError:`

          - `required BashCodeExecutionToolResultErrorCode ErrorCode`

            - `InvalidToolInput`

            - `Unavailable`

            - `TooManyRequests`

            - `ExecutionTimeExceeded`

            - `OutputFileTooLarge`

          - `JsonElement Type constant`

        - `class BashCodeExecutionResultBlock:`

          - `required IReadOnlyList<BashCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type constant`

          - `required long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type constant`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type constant`

    - `class TextEditorCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class TextEditorCodeExecutionToolResultError:`

          - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

            - `InvalidToolInput`

            - `Unavailable`

            - `TooManyRequests`

            - `ExecutionTimeExceeded`

            - `FileNotFound`

          - `required string? ErrorMessage`

          - `JsonElement Type constant`

        - `class TextEditorCodeExecutionViewResultBlock:`

          - `required string Content`

          - `required FileType FileType`

            - `Text`

            - `Image`

            - `Pdf`

          - `required long? NumLines`

          - `required long? StartLine`

          - `required long? TotalLines`

          - `JsonElement Type constant`

        - `class TextEditorCodeExecutionCreateResultBlock:`

          - `required bool IsFileUpdate`

          - `JsonElement Type constant`

        - `class TextEditorCodeExecutionStrReplaceResultBlock:`

          - `required IReadOnlyList<string>? Lines`

          - `required long? NewLines`

          - `required long? NewStart`

          - `required long? OldLines`

          - `required long? OldStart`

          - `JsonElement Type constant`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type constant`

    - `class ToolSearchToolResultBlock:`

      - `required Content Content`

        - `class ToolSearchToolResultError:`

          - `required ToolSearchToolResultErrorCode ErrorCode`

            - `InvalidToolInput`

            - `Unavailable`

            - `TooManyRequests`

            - `ExecutionTimeExceeded`

          - `required string? ErrorMessage`

          - `JsonElement Type constant`

        - `class ToolSearchToolSearchResultBlock:`

          - `required IReadOnlyList<ToolReferenceBlock> ToolReferences`

            - `required string ToolName`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `JsonElement Type constant`

          - `JsonElement Type constant`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type constant`

    - `class ContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `required string FileID`

      - `JsonElement Type constant`

  - `required Model Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `ClaudeFable5_1`

      Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

    - `ClaudeMythos5_1`

      Our most capable model for cybersecurity and biology research, available through trusted access programs

    - `ClaudeSonnet5`

      High-performance model for coding and agents

    - `ClaudeFable5`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `ClaudeMythos5`

      Most capable model for cybersecurity and biology research

    - `ClaudeOpus5`

      Powerful intelligence for long-running agents and coding

    - `ClaudeOpus4_8`

      Powerful intelligence for long-running agents and coding

    - `ClaudeOpus4_7`

      Powerful intelligence for long-running agents and coding

    - `ClaudeMythosPreview`

      New class of intelligence, strongest in coding and cybersecurity

    - `ClaudeOpus4_6`

      Powerful intelligence for long-running agents and coding

    - `ClaudeSonnet4_6`

      Best combination of speed and intelligence

    - `ClaudeHaiku4_5`

      Fastest model with near-frontier intelligence

    - `ClaudeHaiku4_5_20251001`

      Fastest model with near-frontier intelligence

    - `ClaudeOpus4_5`

      Powerful intelligence for long-running agents and coding

    - `ClaudeOpus4_5_20251101`

      Powerful intelligence for long-running agents and coding

    - `ClaudeSonnet4_5`

      High-performance model for agents and coding

    - `ClaudeSonnet4_5_20250929`

      High-performance model for agents and coding

  - `JsonElement Role constant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `required RefusalStopDetails? StopDetails`

    Structured information about a refusal.

    - `required Category? Category`

      The policy category that triggered a refusal.

      - `Cyber`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `Bio`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `FrontierLlm`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `ReasoningExtraction`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `GeneralHarms`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `required string? Explanation`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `JsonElement Type constant`

  - `required StopReason? StopReason`

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

    - `EndTurn`

    - `MaxTokens`

    - `StopSequence`

    - `ToolUse`

    - `PauseTurn`

    - `Refusal`

    - `ModelContextWindowExceeded`

  - `required string? StopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonElement Type constant`

    Object type.

    For Messages, this is always `"message"`.

  - `required Usage Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `required CacheCreation? CacheCreation`

      Breakdown of cached tokens by TTL

      - `required long Ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `required long Ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `required long? CacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `required long? CacheReadInputTokens`

      The number of input tokens read from the cache.

      minimum: 0

    - `required string? InferenceGeo`

      The geographic region where inference was performed for this request.

    - `required long InputTokens`

      The number of input tokens which were used.

      minimum: 0

    - `required long OutputTokens`

      The number of output tokens which were used.

      minimum: 0

    - `required OutputTokensDetails? OutputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `required long ThinkingTokens`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `required ServerToolUsage? ServerToolUse`

      The number of server tool requests.

      - `required long WebFetchRequests`

        The number of web fetch tool requests.

        minimum: 0

      - `required long WebSearchRequests`

        The number of web search tool requests.

        minimum: 0

    - `required ServiceTier? ServiceTier`

      If the request used the priority, standard, or batch tier.

      - `Standard`

      - `Priority`

      - `Batch`

- `class RawMessageStreamEvent: union`

  - `class RawMessageStartEvent:`

    - `required Message Message`

    - `JsonElement Type constant`

  - `class RawMessageDeltaEvent:`

    - `required Delta Delta`

      - `required Container? Container`

        Information about the container used in the request (for the code execution tool)

      - `required RefusalStopDetails? StopDetails`

        Structured information about a refusal.

      - `required StopReason? StopReason`

      - `required string? StopSequence`

    - `JsonElement Type constant`

    - `required MessageDeltaUsage Usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `required long? CacheCreationInputTokens`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `required long? CacheReadInputTokens`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `required long? InputTokens`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `required long OutputTokens`

        The cumulative number of output tokens which were used.

      - `required OutputTokensDetails? OutputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `required ServerToolUsage? ServerToolUse`

        The number of server tool requests.

  - `class RawMessageStopEvent:`

    - `JsonElement Type constant`

  - `class RawContentBlockStartEvent:`

    - `required ContentBlock ContentBlock`

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

    - `required long Index`

    - `JsonElement Type constant`

  - `class RawContentBlockDeltaEvent:`

    - `required RawContentBlockDelta Delta`

      - `class TextDelta:`

        - `required string Text`

        - `JsonElement Type constant`

      - `class InputJsonDelta:`

        - `required string PartialJson`

        - `JsonElement Type constant`

      - `class CitationsDelta:`

        - `required Citation Citation`

          - `class CitationCharLocation:`

          - `class CitationPageLocation:`

          - `class CitationContentBlockLocation:`

          - `class CitationsWebSearchResultLocation:`

          - `class CitationsSearchResultLocation:`

        - `JsonElement Type constant`

      - `class ThinkingDelta:`

        - `required string Thinking`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `JsonElement Type constant`

      - `class SignatureDelta:`

        - `required string Signature`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `JsonElement Type constant`

    - `required long Index`

    - `JsonElement Type constant`

  - `class RawContentBlockStopEvent:`

    - `required long Index`

    - `JsonElement Type constant`

## Example

```csharp
MessageCreateParams parameters = new()
{
    MaxTokens = 1024,
    Messages =
    [
        new()
        {
            Content = "Hello, world",
            Role = Role.User,
        },
    ],
    Model = Model.ClaudeOpus5,
};

var message = await client.Messages.Create(parameters);

Console.WriteLine(message);
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
