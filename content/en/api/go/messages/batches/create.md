---
title: Create a Message Batch
url: https://platform.claude.com/docs/en/api/go/messages/batches/create
---

## Create a Message Batch

`client.Messages.Batches.New(ctx, params) (*MessageBatch, error)`

**post** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `params MessageBatchNewParams`

  - `Requests param.Field[[]MessageBatchNewParamsRequest]`

    Body param: List of requests for prompt completion. Each is an individual request to create a Message.

    - `CustomID string`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

    - `Params MessageBatchNewParamsRequestParams`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

      - `MaxTokens int64`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

        Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

      - `Messages []MessageParamResp`

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

        - `Content []ContentBlockParamUnionResp`

          - `[]ContentBlockParamUnionResp`

            - `type TextBlockParamResp struct{…}`

              - `Text string`

              - `Type Text`

                - `const TextText Text = "text"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

                - `Type Ephemeral`

                  - `const EphemeralEphemeral Ephemeral = "ephemeral"`

                - `TTL CacheControlEphemeralTTL`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"`

                  - `const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"`

              - `Citations []TextCitationParamUnionResp`

                - `type CitationCharLocationParamResp struct{…}`

                  - `CitedText string`

                  - `DocumentIndex int64`

                  - `DocumentTitle string`

                  - `EndCharIndex int64`

                  - `StartCharIndex int64`

                  - `Type CharLocation`

                    - `const CharLocationCharLocation CharLocation = "char_location"`

                - `type CitationPageLocationParamResp struct{…}`

                  - `CitedText string`

                  - `DocumentIndex int64`

                  - `DocumentTitle string`

                  - `EndPageNumber int64`

                  - `StartPageNumber int64`

                  - `Type PageLocation`

                    - `const PageLocationPageLocation PageLocation = "page_location"`

                - `type CitationContentBlockLocationParamResp struct{…}`

                  - `CitedText string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `DocumentIndex int64`

                  - `DocumentTitle string`

                  - `EndBlockIndex int64`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `StartBlockIndex int64`

                    0-based index of the first cited block in the source's `content` array.

                  - `Type ContentBlockLocation`

                    - `const ContentBlockLocationContentBlockLocation ContentBlockLocation = "content_block_location"`

                - `type CitationWebSearchResultLocationParamResp struct{…}`

                  - `CitedText string`

                  - `EncryptedIndex string`

                  - `Title string`

                  - `Type WebSearchResultLocation`

                    - `const WebSearchResultLocationWebSearchResultLocation WebSearchResultLocation = "web_search_result_location"`

                  - `URL string`

                - `type CitationSearchResultLocationParamResp struct{…}`

                  - `CitedText string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `EndBlockIndex int64`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `SearchResultIndex int64`

                    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                    Counted separately from `document_index`; server-side web search results are not included in this count.

                  - `Source string`

                  - `StartBlockIndex int64`

                    0-based index of the first cited block in the source's `content` array.

                  - `Title string`

                  - `Type SearchResultLocation`

                    - `const SearchResultLocationSearchResultLocation SearchResultLocation = "search_result_location"`

            - `type ImageBlockParamResp struct{…}`

              - `Source ImageBlockParamSourceUnionResp`

                - `type Base64ImageSource struct{…}`

                  - `Data string`

                  - `MediaType Base64ImageSourceMediaType`

                    - `const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"`

                    - `const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"`

                    - `const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"`

                    - `const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"`

                  - `Type Base64`

                    - `const Base64Base64 Base64 = "base64"`

                - `type URLImageSource struct{…}`

                  - `Type URL`

                    - `const URLURL URL = "url"`

                  - `URL string`

                - `type FileImageSource struct{…}`

                  - `FileID string`

                  - `Type File`

                    - `const FileFile File = "file"`

              - `Type Image`

                - `const ImageImage Image = "image"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Transformations ImageTransformationsParamResp`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `OversizedImage ImageTransformationsParamOversizedImage`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `const ImageTransformationsParamOversizedImageDownsize ImageTransformationsParamOversizedImage = "downsize"`

                  - `const ImageTransformationsParamOversizedImageError ImageTransformationsParamOversizedImage = "error"`

            - `type DocumentBlockParamResp struct{…}`

              - `Source DocumentBlockParamSourceUnionResp`

                - `type Base64PDFSource struct{…}`

                  - `Data string`

                  - `MediaType ApplicationPDF`

                    - `const ApplicationPDFApplicationPDF ApplicationPDF = "application/pdf"`

                  - `Type Base64`

                    - `const Base64Base64 Base64 = "base64"`

                - `type PlainTextSource struct{…}`

                  - `Data string`

                  - `MediaType TextPlain`

                    - `const TextPlainTextPlain TextPlain = "text/plain"`

                  - `Type Text`

                    - `const TextText Text = "text"`

                - `type ContentBlockSource struct{…}`

                  - `Content ContentBlockSourceContentUnion`

                    - `string`

                    - `[]ContentBlockSourceContentItemUnion`

                      - `type TextBlockParamResp struct{…}`

                      - `type ImageBlockParamResp struct{…}`

                  - `Type Content`

                    - `const ContentContent Content = "content"`

                - `type URLPDFSource struct{…}`

                  - `Type URL`

                    - `const URLURL URL = "url"`

                  - `URL string`

                - `type FileDocumentSource struct{…}`

                  - `FileID string`

                  - `Type File`

                    - `const FileFile File = "file"`

              - `Type Document`

                - `const DocumentDocument Document = "document"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Citations CitationsConfigParamResp`

                - `Enabled bool`

              - `Context string`

              - `Title string`

            - `type SearchResultBlockParamResp struct{…}`

              - `Content []TextBlockParamResp`

                - `Text string`

                - `Type Text`

                - `CacheControl CacheControlEphemeral`

                  Create a cache control breakpoint at this content block.

                - `Citations []TextCitationParamUnionResp`

              - `Source string`

              - `Title string`

              - `Type SearchResult`

                - `const SearchResultSearchResult SearchResult = "search_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Citations CitationsConfigParamResp`

            - `type ThinkingBlockParamResp struct{…}`

              - `Signature string`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `Thinking string`

                The `thinking` text of this block as returned by the API.

              - `Type Thinking`

                - `const ThinkingThinking Thinking = "thinking"`

            - `type RedactedThinkingBlockParamResp struct{…}`

              - `Data string`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `Type RedactedThinking`

                - `const RedactedThinkingRedactedThinking RedactedThinking = "redacted_thinking"`

            - `type ToolUseBlockParamResp struct{…}`

              - `ID string`

              - `Input map[string, any]`

              - `Name string`

              - `Type ToolUse`

                - `const ToolUseToolUse ToolUse = "tool_use"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Caller ToolUseBlockParamCallerUnionResp`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                  - `Type Direct`

                    - `const DirectDirect Direct = "direct"`

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                  - `ToolID string`

                  - `Type CodeExecution20250825`

                    - `const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"`

                - `type ServerToolCaller20260120 struct{…}`

                  - `ToolID string`

                  - `Type CodeExecution20260120`

                    - `const CodeExecution20260120CodeExecution20260120 CodeExecution20260120 = "code_execution_20260120"`

              - `ToolsetName string`

                For a toolset member tool_use, the toolset family this member belongs to.

            - `type ToolResultBlockParamResp struct{…}`

              - `ToolUseID string`

              - `Type ToolResult`

                - `const ToolResultToolResult ToolResult = "tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Content []ToolResultBlockParamContentUnionResp`

                - `[]ToolResultBlockParamContentUnionResp`

                  - `type TextBlockParamResp struct{…}`

                  - `type ImageBlockParamResp struct{…}`

                  - `type SearchResultBlockParamResp struct{…}`

                  - `type DocumentBlockParamResp struct{…}`

                  - `type ToolReferenceBlockParamResp struct{…}`

                    Tool reference block that can be included in tool_result content.

                    - `ToolName string`

                    - `Type ToolReference`

                      - `const ToolReferenceToolReference ToolReference = "tool_reference"`

                    - `CacheControl CacheControlEphemeral`

                      Create a cache control breakpoint at this content block.

                  - `type BrowserStateBlockParamResp struct{…}`

                    The caller's browser state after a browser toolset member call —
                    the full inventory of open tabs, which tab is active, and any side
                    effects (tabs opened, download state changes) the call produced.

                    At most one per `tool_result`, only on a non-error result answering a
                    browser toolset member `tool_use`. The server renders the
                    model-visible text from it; the model never sees the raw fields.

                    - `Tabs []BrowserStateTabEntry`

                      All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                      - `TabID string`

                        The caller-assigned identifier for this tab, unique within the inventory.

                      - `Title string`

                        The title of the page the tab is showing. May be empty.

                      - `URL string`

                        The URL of the page the tab is showing. May be empty.

                      - `Active bool`

                        Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                    - `Type BrowserState`

                      - `const BrowserStateBrowserState BrowserState = "browser_state"`

                    - `CacheControl CacheControlEphemeral`

                      Create a cache control breakpoint at this content block.

                    - `StateChanges []BrowserStateChangeUnion`

                      Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                      - `type BrowserStateChangeTabOpened struct{…}`

                        A tab this call's execution opened that remains open at its end —
                        the creation delta of the `tabs` inventory, not an event log.

                        Carries only the `tab_id`; the tab's `title` and `url` live on its
                        `tabs` entry, which must include the same `tab_id`. A tab opened
                        during a failed call gets no deferred `tab_opened`; it simply appears
                        in the next result's `tabs` inventory.

                        - `TabID string`

                          The `tab_id` of the opened tab, present in `tabs`.

                        - `Type TabOpened`

                          - `const TabOpenedTabOpened TabOpened = "tab_opened"`

                      - `type BrowserStateChangeDownloadStarted struct{…}`

                        A file download that started during this call.

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                        - `Type DownloadStarted`

                          - `const DownloadStartedDownloadStarted DownloadStarted = "download_started"`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                      - `type BrowserStateChangeDownloadCompleted struct{…}`

                        A file download that finished during this call, reported with the
                        same `download_id` as its `download_started` — or without a prior
                        `download_started`, when the download finished during the call that
                        started it (at most one state change per `download_id` per result).

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                        - `Type DownloadCompleted`

                          - `const DownloadCompletedDownloadCompleted DownloadCompleted = "download_completed"`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                        - `Path string`

                          Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                        - `SizeBytes int64`

                          The completed download's size.

                      - `type BrowserStateChangeDownloadFailed struct{…}`

                        A file download that failed — or was cancelled — during this call.

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                        - `Type DownloadFailed`

                          - `const DownloadFailedDownloadFailed DownloadFailed = "download_failed"`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                        - `Error string`

                          The failure or cancellation detail, when known.

              - `IsError bool`

              - `ToolsetName string`

                For a toolset member tool_result, the toolset family of the paired tool_use.

            - `type ServerToolUseBlockParamResp struct{…}`

              - `ID string`

              - `Input map[string, any]`

              - `Name ServerToolUseBlockParamName`

                - `const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web_search"`

                - `const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web_fetch"`

                - `const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code_execution"`

                - `const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash_code_execution"`

                - `const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text_editor_code_execution"`

                - `const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool_search_tool_regex"`

                - `const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool_search_tool_bm25"`

              - `Type ServerToolUse`

                - `const ServerToolUseServerToolUse ServerToolUse = "server_tool_use"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Caller ServerToolUseBlockParamCallerUnionResp`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type ServerToolCaller20260120 struct{…}`

            - `type WebSearchToolResultBlockParamResp struct{…}`

              - `Content WebSearchToolResultBlockParamContentUnionResp`

                - `[]WebSearchResultBlockParamResp`

                  - `EncryptedContent string`

                  - `Title string`

                  - `Type WebSearchResult`

                    - `const WebSearchResultWebSearchResult WebSearchResult = "web_search_result"`

                  - `URL string`

                  - `PageAge string`

                - `type WebSearchToolRequestError struct{…}`

                  - `ErrorCode WebSearchToolResultErrorCode`

                    - `const WebSearchToolResultErrorCodeInvalidToolInput WebSearchToolResultErrorCode = "invalid_tool_input"`

                    - `const WebSearchToolResultErrorCodeUnavailable WebSearchToolResultErrorCode = "unavailable"`

                    - `const WebSearchToolResultErrorCodeMaxUsesExceeded WebSearchToolResultErrorCode = "max_uses_exceeded"`

                    - `const WebSearchToolResultErrorCodeTooManyRequests WebSearchToolResultErrorCode = "too_many_requests"`

                    - `const WebSearchToolResultErrorCodeQueryTooLong WebSearchToolResultErrorCode = "query_too_long"`

                    - `const WebSearchToolResultErrorCodeRequestTooLarge WebSearchToolResultErrorCode = "request_too_large"`

                  - `Type WebSearchToolResultError`

                    - `const WebSearchToolResultErrorWebSearchToolResultError WebSearchToolResultError = "web_search_tool_result_error"`

              - `ToolUseID string`

              - `Type WebSearchToolResult`

                - `const WebSearchToolResultWebSearchToolResult WebSearchToolResult = "web_search_tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Caller WebSearchToolResultBlockParamCallerUnionResp`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type ServerToolCaller20260120 struct{…}`

            - `type WebFetchToolResultBlockParamResp struct{…}`

              - `Content WebFetchToolResultBlockParamContentUnionResp`

                - `type WebFetchToolResultErrorBlockParamResp struct{…}`

                  - `ErrorCode WebFetchToolResultErrorCode`

                    - `const WebFetchToolResultErrorCodeInvalidToolInput WebFetchToolResultErrorCode = "invalid_tool_input"`

                    - `const WebFetchToolResultErrorCodeURLTooLong WebFetchToolResultErrorCode = "url_too_long"`

                    - `const WebFetchToolResultErrorCodeURLNotAllowed WebFetchToolResultErrorCode = "url_not_allowed"`

                    - `const WebFetchToolResultErrorCodeURLNotInPriorContext WebFetchToolResultErrorCode = "url_not_in_prior_context"`

                    - `const WebFetchToolResultErrorCodeURLNotAccessible WebFetchToolResultErrorCode = "url_not_accessible"`

                    - `const WebFetchToolResultErrorCodeUnsupportedContentType WebFetchToolResultErrorCode = "unsupported_content_type"`

                    - `const WebFetchToolResultErrorCodeTooManyRequests WebFetchToolResultErrorCode = "too_many_requests"`

                    - `const WebFetchToolResultErrorCodeMaxUsesExceeded WebFetchToolResultErrorCode = "max_uses_exceeded"`

                    - `const WebFetchToolResultErrorCodeUnavailable WebFetchToolResultErrorCode = "unavailable"`

                  - `Type WebFetchToolResultError`

                    - `const WebFetchToolResultErrorWebFetchToolResultError WebFetchToolResultError = "web_fetch_tool_result_error"`

                - `type WebFetchBlockParamResp struct{…}`

                  - `Content DocumentBlockParamResp`

                  - `Type WebFetchResult`

                    - `const WebFetchResultWebFetchResult WebFetchResult = "web_fetch_result"`

                  - `URL string`

                    Fetched content URL

                  - `RetrievedAt string`

                    ISO 8601 timestamp when the content was retrieved

              - `ToolUseID string`

              - `Type WebFetchToolResult`

                - `const WebFetchToolResultWebFetchToolResult WebFetchToolResult = "web_fetch_tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

              - `Caller WebFetchToolResultBlockParamCallerUnionResp`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type ServerToolCaller20260120 struct{…}`

            - `type CodeExecutionToolResultBlockParamResp struct{…}`

              - `Content CodeExecutionToolResultBlockParamContentUnionResp`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type CodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode CodeExecutionToolResultErrorCode`

                    - `const CodeExecutionToolResultErrorCodeInvalidToolInput CodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const CodeExecutionToolResultErrorCodeUnavailable CodeExecutionToolResultErrorCode = "unavailable"`

                    - `const CodeExecutionToolResultErrorCodeTooManyRequests CodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const CodeExecutionToolResultErrorCodeExecutionTimeExceeded CodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                  - `Type CodeExecutionToolResultError`

                    - `const CodeExecutionToolResultErrorCodeExecutionToolResultError CodeExecutionToolResultError = "code_execution_tool_result_error"`

                - `type CodeExecutionResultBlockParamResp struct{…}`

                  - `Content []CodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type CodeExecutionOutput`

                      - `const CodeExecutionOutputCodeExecutionOutput CodeExecutionOutput = "code_execution_output"`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Stdout string`

                  - `Type CodeExecutionResult`

                    - `const CodeExecutionResultCodeExecutionResult CodeExecutionResult = "code_execution_result"`

                - `type EncryptedCodeExecutionResultBlockParamResp struct{…}`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `Content []CodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type CodeExecutionOutput`

                  - `EncryptedStdout string`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Type EncryptedCodeExecutionResult`

                    - `const EncryptedCodeExecutionResultEncryptedCodeExecutionResult EncryptedCodeExecutionResult = "encrypted_code_execution_result"`

              - `ToolUseID string`

              - `Type CodeExecutionToolResult`

                - `const CodeExecutionToolResultCodeExecutionToolResult CodeExecutionToolResult = "code_execution_tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `type BashCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content BashCodeExecutionToolResultBlockParamContentUnionResp`

                - `type BashCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode BashCodeExecutionToolResultErrorCode`

                    - `const BashCodeExecutionToolResultErrorCodeInvalidToolInput BashCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const BashCodeExecutionToolResultErrorCodeUnavailable BashCodeExecutionToolResultErrorCode = "unavailable"`

                    - `const BashCodeExecutionToolResultErrorCodeTooManyRequests BashCodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded BashCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                    - `const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge BashCodeExecutionToolResultErrorCode = "output_file_too_large"`

                  - `Type BashCodeExecutionToolResultError`

                    - `const BashCodeExecutionToolResultErrorBashCodeExecutionToolResultError BashCodeExecutionToolResultError = "bash_code_execution_tool_result_error"`

                - `type BashCodeExecutionResultBlockParamResp struct{…}`

                  - `Content []BashCodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type BashCodeExecutionOutput`

                      - `const BashCodeExecutionOutputBashCodeExecutionOutput BashCodeExecutionOutput = "bash_code_execution_output"`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Stdout string`

                  - `Type BashCodeExecutionResult`

                    - `const BashCodeExecutionResultBashCodeExecutionResult BashCodeExecutionResult = "bash_code_execution_result"`

              - `ToolUseID string`

              - `Type BashCodeExecutionToolResult`

                - `const BashCodeExecutionToolResultBashCodeExecutionToolResult BashCodeExecutionToolResult = "bash_code_execution_tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `type TextEditorCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp`

                - `type TextEditorCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode TextEditorCodeExecutionToolResultErrorCode`

                    - `const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeUnavailable TextEditorCodeExecutionToolResultErrorCode = "unavailable"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests TextEditorCodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded TextEditorCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeFileNotFound TextEditorCodeExecutionToolResultErrorCode = "file_not_found"`

                  - `Type TextEditorCodeExecutionToolResultError`

                    - `const TextEditorCodeExecutionToolResultErrorTextEditorCodeExecutionToolResultError TextEditorCodeExecutionToolResultError = "text_editor_code_execution_tool_result_error"`

                  - `ErrorMessage string`

                - `type TextEditorCodeExecutionViewResultBlockParamResp struct{…}`

                  - `Content string`

                  - `FileType TextEditorCodeExecutionViewResultBlockParamFileType`

                    - `const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"`

                    - `const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"`

                    - `const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"`

                  - `Type TextEditorCodeExecutionViewResult`

                    - `const TextEditorCodeExecutionViewResultTextEditorCodeExecutionViewResult TextEditorCodeExecutionViewResult = "text_editor_code_execution_view_result"`

                  - `NumLines int64`

                  - `StartLine int64`

                  - `TotalLines int64`

                - `type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}`

                  - `IsFileUpdate bool`

                  - `Type TextEditorCodeExecutionCreateResult`

                    - `const TextEditorCodeExecutionCreateResultTextEditorCodeExecutionCreateResult TextEditorCodeExecutionCreateResult = "text_editor_code_execution_create_result"`

                - `type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}`

                  - `Type TextEditorCodeExecutionStrReplaceResult`

                    - `const TextEditorCodeExecutionStrReplaceResultTextEditorCodeExecutionStrReplaceResult TextEditorCodeExecutionStrReplaceResult = "text_editor_code_execution_str_replace_result"`

                  - `Lines []string`

                  - `NewLines int64`

                  - `NewStart int64`

                  - `OldLines int64`

                  - `OldStart int64`

              - `ToolUseID string`

              - `Type TextEditorCodeExecutionToolResult`

                - `const TextEditorCodeExecutionToolResultTextEditorCodeExecutionToolResult TextEditorCodeExecutionToolResult = "text_editor_code_execution_tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `type ToolSearchToolResultBlockParamResp struct{…}`

              - `Content ToolSearchToolResultBlockParamContentUnionResp`

                - `type ToolSearchToolResultErrorParamResp struct{…}`

                  - `ErrorCode ToolSearchToolResultErrorCode`

                    - `const ToolSearchToolResultErrorCodeInvalidToolInput ToolSearchToolResultErrorCode = "invalid_tool_input"`

                    - `const ToolSearchToolResultErrorCodeUnavailable ToolSearchToolResultErrorCode = "unavailable"`

                    - `const ToolSearchToolResultErrorCodeTooManyRequests ToolSearchToolResultErrorCode = "too_many_requests"`

                    - `const ToolSearchToolResultErrorCodeExecutionTimeExceeded ToolSearchToolResultErrorCode = "execution_time_exceeded"`

                  - `Type ToolSearchToolResultError`

                    - `const ToolSearchToolResultErrorToolSearchToolResultError ToolSearchToolResultError = "tool_search_tool_result_error"`

                  - `ErrorMessage string`

                - `type ToolSearchToolSearchResultBlockParamResp struct{…}`

                  - `ToolReferences []ToolReferenceBlockParamResp`

                    - `ToolName string`

                    - `Type ToolReference`

                    - `CacheControl CacheControlEphemeral`

                      Create a cache control breakpoint at this content block.

                  - `Type ToolSearchToolSearchResult`

                    - `const ToolSearchToolSearchResultToolSearchToolSearchResult ToolSearchToolSearchResult = "tool_search_tool_search_result"`

              - `ToolUseID string`

              - `Type ToolSearchToolResult`

                - `const ToolSearchToolResultToolSearchToolResult ToolSearchToolResult = "tool_search_tool_result"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

            - `type ContainerUploadBlockParamResp struct{…}`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `FileID string`

              - `Type ContainerUpload`

                - `const ContainerUploadContainerUpload ContainerUpload = "container_upload"`

              - `CacheControl CacheControlEphemeral`

                Create a cache control breakpoint at this content block.

        - `Role MessageParamRole`

          - `const MessageParamRoleUser MessageParamRole = "user"`

          - `const MessageParamRoleAssistant MessageParamRole = "assistant"`

          - `const MessageParamRoleSystem MessageParamRole = "system"`

      - `Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type Model string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const ModelClaudeSonnet5 Model = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const ModelClaudeFable5 Model = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const ModelClaudeMythos5 Model = "claude-mythos-5"`

            Most capable model for cybersecurity and biology research

          - `const ModelClaudeOpus5 Model = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeOpus4_8 Model = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeOpus4_7 Model = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeMythosPreview Model = "claude-mythos-preview"`

            New class of intelligence, strongest in coding and cybersecurity

          - `const ModelClaudeOpus4_6 Model = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const ModelClaudeOpus4_5 Model = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `CacheControl CacheControlEphemeral`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `Container MessageCreateParamsContainerUnionResp`

        Container identifier for reuse across requests.

        - `type ContainerParamsResp struct{…}`

          Container parameters with skills to be loaded.

          - `ID string`

            Container id

          - `Skills []SkillParamsResp`

            List of skills to load in the container

            - `SkillID string`

              Skill ID

            - `Type SkillParamsType`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `const SkillParamsTypeAnthropic SkillParamsType = "anthropic"`

              - `const SkillParamsTypeCustom SkillParamsType = "custom"`

            - `Version string`

              Skill version or 'latest' for most recent version

        - `string`

      - `InferenceGeo string`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Metadata Metadata`

        An object describing metadata about the request.

        - `UserID string`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

      - `OutputConfig OutputConfig`

        Configuration options for the model's output, such as the output format.

        - `Effort OutputConfigEffort`

          All possible effort levels.

          - `const OutputConfigEffortLow OutputConfigEffort = "low"`

          - `const OutputConfigEffortMedium OutputConfigEffort = "medium"`

          - `const OutputConfigEffortHigh OutputConfigEffort = "high"`

          - `const OutputConfigEffortXhigh OutputConfigEffort = "xhigh"`

          - `const OutputConfigEffortMax OutputConfigEffort = "max"`

        - `Format JSONOutputFormat`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `Schema map[string, any]`

            The JSON schema of the format

          - `Type JSONSchema`

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `ServiceTier string`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `const MessageBatchNewParamsRequestParamsServiceTierAuto MessageBatchNewParamsRequestParamsServiceTier = "auto"`

        - `const MessageBatchNewParamsRequestParamsServiceTierStandardOnly MessageBatchNewParamsRequestParamsServiceTier = "standard_only"`

      - `StopSequences []string`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `Stream bool`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

      - `System []TextBlockParamResp`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

        - `[]TextBlockParam`

          - `Text string`

          - `Type Text`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Citations []TextCitationParamUnionResp`

      - `Temperature float64`

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

      - `Thinking ThinkingConfigParamUnionResp`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `type ThinkingConfigEnabled struct{…}`

          - `BudgetTokens int64`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

          - `Type Enabled`

            - `const EnabledEnabled Enabled = "enabled"`

          - `Display ThinkingConfigEnabledDisplay`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `const ThinkingConfigEnabledDisplaySummarized ThinkingConfigEnabledDisplay = "summarized"`

            - `const ThinkingConfigEnabledDisplayOmitted ThinkingConfigEnabledDisplay = "omitted"`

        - `type ThinkingConfigDisabled struct{…}`

          - `Type Disabled`

            - `const DisabledDisabled Disabled = "disabled"`

        - `type ThinkingConfigAdaptive struct{…}`

          - `Type Adaptive`

            - `const AdaptiveAdaptive Adaptive = "adaptive"`

          - `Display ThinkingConfigAdaptiveDisplay`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `const ThinkingConfigAdaptiveDisplaySummarized ThinkingConfigAdaptiveDisplay = "summarized"`

            - `const ThinkingConfigAdaptiveDisplayOmitted ThinkingConfigAdaptiveDisplay = "omitted"`

      - `ToolChoice ToolChoiceUnion`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `type ToolChoiceAuto struct{…}`

          The model will automatically decide whether to use tools.

          - `Type Auto`

            - `const AutoAuto Auto = "auto"`

          - `DisableParallelToolUse bool`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `type ToolChoiceAny struct{…}`

          The model will use any available tools.

          - `Type Any`

            - `const AnyAny Any = "any"`

          - `DisableParallelToolUse bool`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `type ToolChoiceTool struct{…}`

          The model will use the specified tool with `tool_choice.name`.

          - `Name string`

            The name of the tool to use.

          - `Type Tool`

            - `const ToolTool Tool = "tool"`

          - `DisableParallelToolUse bool`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `type ToolChoiceNone struct{…}`

          The model will not be allowed to use tools.

          - `Type None`

            - `const NoneNone None = "none"`

      - `Tools []ToolUnion`

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

        - `type Tool struct{…}`

          - `InputSchema ToolInputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `Type Object`

              - `const ObjectObject Object = "object"`

            - `Properties map[string, any]`

            - `Required []string`

          - `Name string`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `AllowedCallers []string`

            - `const ToolAllowedCallerDirect ToolAllowedCaller = "direct"`

            - `const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code_execution_20250825"`

            - `const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code_execution_20260120"`

            - `const ToolAllowedCallerCodeExecution20260521 ToolAllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Description string`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `EagerInputStreaming bool`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `InputExamples []map[string, any]`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

          - `Type ToolType`

            - `const ToolTypeCustom ToolType = "custom"`

        - `type ToolBash20250124 struct{…}`

          - `Name Bash`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const BashBash Bash = "bash"`

          - `Type Bash20250124`

            - `const Bash20250124Bash20250124 Bash20250124 = "bash_20250124"`

          - `AllowedCallers []string`

            - `const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"`

            - `const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code_execution_20250825"`

            - `const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code_execution_20260120"`

            - `const ToolBash20250124AllowedCallerCodeExecution20260521 ToolBash20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any]`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20250522 struct{…}`

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const CodeExecutionCodeExecution CodeExecution = "code_execution"`

          - `Type CodeExecution20250522`

            - `const CodeExecution20250522CodeExecution20250522 CodeExecution20250522 = "code_execution_20250522"`

          - `AllowedCallers []string`

            - `const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"`

            - `const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20250522AllowedCallerCodeExecution20260521 CodeExecutionTool20250522AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20250825 struct{…}`

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const CodeExecutionCodeExecution CodeExecution = "code_execution"`

          - `Type CodeExecution20250825`

            - `const CodeExecution20250825CodeExecution20250825 CodeExecution20250825 = "code_execution_20250825"`

          - `AllowedCallers []string`

            - `const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"`

            - `const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20250825AllowedCallerCodeExecution20260521 CodeExecutionTool20250825AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20260120 struct{…}`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const CodeExecutionCodeExecution CodeExecution = "code_execution"`

          - `Type CodeExecution20260120`

            - `const CodeExecution20260120CodeExecution20260120 CodeExecution20260120 = "code_execution_20260120"`

          - `AllowedCallers []string`

            - `const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"`

            - `const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20260120AllowedCallerCodeExecution20260521 CodeExecutionTool20260120AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20260521 struct{…}`

          Code execution tool with REPL state persistence.

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const CodeExecutionCodeExecution CodeExecution = "code_execution"`

          - `Type CodeExecution20260521`

            - `const CodeExecution20260521CodeExecution20260521 CodeExecution20260521 = "code_execution_20260521"`

          - `AllowedCallers []string`

            - `const CodeExecutionTool20260521AllowedCallerDirect CodeExecutionTool20260521AllowedCaller = "direct"`

            - `const CodeExecutionTool20260521AllowedCallerCodeExecution20250825 CodeExecutionTool20260521AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20260521AllowedCallerCodeExecution20260120 CodeExecutionTool20260521AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20260521AllowedCallerCodeExecution20260521 CodeExecutionTool20260521AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type BrowserToolset20260801 struct{…}`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `Type BrowserToolset20260801`

            - `const BrowserToolset20260801BrowserToolset20260801 BrowserToolset20260801 = "browser_toolset_20260801"`

          - `AllowedCallers []string`

            - `const BrowserToolset20260801AllowedCallerDirect BrowserToolset20260801AllowedCaller = "direct"`

            - `const BrowserToolset20260801AllowedCallerCodeExecution20250825 BrowserToolset20260801AllowedCaller = "code_execution_20250825"`

            - `const BrowserToolset20260801AllowedCallerCodeExecution20260120 BrowserToolset20260801AllowedCaller = "code_execution_20260120"`

            - `const BrowserToolset20260801AllowedCallerCodeExecution20260521 BrowserToolset20260801AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Configs BrowserToolsetConfigs`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `CloseTab BrowserCloseTabConfig`

              `close_tab`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `DoubleClick BrowserDoubleClickConfig`

              `double_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `FileUpload BrowserFileUploadConfig`

              `file_upload`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Find BrowserFindConfig`

              `find`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `FormInput BrowserFormInputConfig`

              `form_input`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `GetPageText BrowserGetPageTextConfig`

              `get_page_text`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `HoldKey BrowserHoldKeyConfig`

              `hold_key`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Hover BrowserHoverConfig`

              `hover`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `JavascriptExec BrowserJavascriptExecConfig`

              `javascript_exec`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Key BrowserKeyConfig`

              `key`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClick BrowserLeftClickConfig`

              `left_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClickDrag BrowserLeftClickDragConfig`

              `left_click_drag`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseDown BrowserLeftMouseDownConfig`

              `left_mouse_down`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseUp BrowserLeftMouseUpConfig`

              `left_mouse_up`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ListTabs BrowserListTabsConfig`

              `list_tabs`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MiddleClick BrowserMiddleClickConfig`

              `middle_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MouseMove BrowserMouseMoveConfig`

              `mouse_move`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Navigate BrowserNavigateConfig`

              `navigate`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `NewTab BrowserNewTabConfig`

              `new_tab`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadConsole BrowserReadConsoleConfig`

              `read_console`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadNetwork BrowserReadNetworkConfig`

              `read_network`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadPage BrowserReadPageConfig`

              `read_page`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `RightClick BrowserRightClickConfig`

              `right_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Screenshot BrowserScreenshotConfig`

              `screenshot`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Scroll BrowserScrollConfig`

              `scroll`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ScrollTo BrowserScrollToConfig`

              `scroll_to`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `SwitchTab BrowserSwitchTabConfig`

              `switch_tab`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `TripleClick BrowserTripleClickConfig`

              `triple_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Type BrowserTypeConfig`

              `type`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Wait BrowserWaitConfig`

              `wait`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Zoom BrowserZoomConfig`

              `zoom`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type MemoryTool20250818 struct{…}`

          - `Name Memory`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const MemoryMemory Memory = "memory"`

          - `Type Memory20250818`

            - `const Memory20250818Memory20250818 Memory20250818 = "memory_20250818"`

          - `AllowedCallers []string`

            - `const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"`

            - `const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code_execution_20250825"`

            - `const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code_execution_20260120"`

            - `const MemoryTool20250818AllowedCallerCodeExecution20260521 MemoryTool20250818AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any]`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type ComputerToolset20260801 struct{…}`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `Type ComputerToolset20260801`

            - `const ComputerToolset20260801ComputerToolset20260801 ComputerToolset20260801 = "computer_toolset_20260801"`

          - `AllowedCallers []string`

            - `const ComputerToolset20260801AllowedCallerDirect ComputerToolset20260801AllowedCaller = "direct"`

            - `const ComputerToolset20260801AllowedCallerCodeExecution20250825 ComputerToolset20260801AllowedCaller = "code_execution_20250825"`

            - `const ComputerToolset20260801AllowedCallerCodeExecution20260120 ComputerToolset20260801AllowedCaller = "code_execution_20260120"`

            - `const ComputerToolset20260801AllowedCallerCodeExecution20260521 ComputerToolset20260801AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Configs ComputerToolsetConfigs`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `CursorPosition ComputerCursorPositionConfig`

              `cursor_position`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `DoubleClick ComputerDoubleClickConfig`

              `double_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `HoldKey ComputerHoldKeyConfig`

              `hold_key`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Key ComputerKeyConfig`

              `key`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClick ComputerLeftClickConfig`

              `left_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClickDrag ComputerLeftClickDragConfig`

              `left_click_drag`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseDown ComputerLeftMouseDownConfig`

              `left_mouse_down`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseUp ComputerLeftMouseUpConfig`

              `left_mouse_up`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MiddleClick ComputerMiddleClickConfig`

              `middle_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MouseMove ComputerMouseMoveConfig`

              `mouse_move`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `RightClick ComputerRightClickConfig`

              `right_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Screenshot ComputerScreenshotConfig`

              `screenshot`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Scroll ComputerScrollConfig`

              `scroll`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `TripleClick ComputerTripleClickConfig`

              `triple_click`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Type ComputerTypeConfig`

              `type`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Wait ComputerWaitConfig`

              `wait`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Zoom ComputerZoomConfig`

              `zoom`'s config overrides.

              - `DeferLoading bool`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type ToolTextEditor20250124 struct{…}`

          - `Name StrReplaceEditor`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const StrReplaceEditorStrReplaceEditor StrReplaceEditor = "str_replace_editor"`

          - `Type TextEditor20250124`

            - `const TextEditor20250124TextEditor20250124 TextEditor20250124 = "text_editor_20250124"`

          - `AllowedCallers []string`

            - `const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"`

            - `const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code_execution_20250825"`

            - `const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code_execution_20260120"`

            - `const ToolTextEditor20250124AllowedCallerCodeExecution20260521 ToolTextEditor20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any]`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type ToolTextEditor20250429 struct{…}`

          - `Name StrReplaceBasedEditTool`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"`

          - `Type TextEditor20250429`

            - `const TextEditor20250429TextEditor20250429 TextEditor20250429 = "text_editor_20250429"`

          - `AllowedCallers []string`

            - `const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"`

            - `const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code_execution_20250825"`

            - `const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code_execution_20260120"`

            - `const ToolTextEditor20250429AllowedCallerCodeExecution20260521 ToolTextEditor20250429AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any]`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type ToolTextEditor20250728 struct{…}`

          - `Name StrReplaceBasedEditTool`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const StrReplaceBasedEditToolStrReplaceBasedEditTool StrReplaceBasedEditTool = "str_replace_based_edit_tool"`

          - `Type TextEditor20250728`

            - `const TextEditor20250728TextEditor20250728 TextEditor20250728 = "text_editor_20250728"`

          - `AllowedCallers []string`

            - `const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"`

            - `const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code_execution_20250825"`

            - `const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code_execution_20260120"`

            - `const ToolTextEditor20250728AllowedCallerCodeExecution20260521 ToolTextEditor20250728AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any]`

          - `MaxCharacters int64`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type WebSearchTool20250305 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `Type WebSearch20250305`

            - `const WebSearch20250305WebSearch20250305 WebSearch20250305 = "web_search_20250305"`

          - `AllowedCallers []string`

            - `const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"`

            - `const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code_execution_20250825"`

            - `const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code_execution_20260120"`

            - `const WebSearchTool20250305AllowedCallerCodeExecution20260521 WebSearchTool20250305AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `Type Approximate`

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              The city of the user.

            - `Country string`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

            - `Region string`

              The region of the user.

            - `Timezone string`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        - `type WebFetchTool20250910 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `Type WebFetch20250910`

            - `const WebFetch20250910WebFetch20250910 WebFetch20250910 = "web_fetch_20250910"`

          - `AllowedCallers []string`

            - `const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"`

            - `const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20250910AllowedCallerCodeExecution20260521 WebFetchTool20250910AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            List of domains to allow fetching from

          - `BlockedDomains []string`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type WebSearchTool20260209 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `Type WebSearch20260209`

            - `const WebSearch20260209WebSearch20260209 WebSearch20260209 = "web_search_20260209"`

          - `AllowedCallers []string`

            - `const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"`

            - `const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code_execution_20250825"`

            - `const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code_execution_20260120"`

            - `const WebSearchTool20260209AllowedCallerCodeExecution20260521 WebSearchTool20260209AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `type WebFetchTool20260209 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `Type WebFetch20260209`

            - `const WebFetch20260209WebFetch20260209 WebFetch20260209 = "web_fetch_20260209"`

          - `AllowedCallers []string`

            - `const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"`

            - `const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20260209AllowedCallerCodeExecution20260521 WebFetchTool20260209AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            List of domains to allow fetching from

          - `BlockedDomains []string`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type WebFetchTool20260309 struct{…}`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `Type WebFetch20260309`

            - `const WebFetch20260309WebFetch20260309 WebFetch20260309 = "web_fetch_20260309"`

          - `AllowedCallers []string`

            - `const WebFetchTool20260309AllowedCallerDirect WebFetchTool20260309AllowedCaller = "direct"`

            - `const WebFetchTool20260309AllowedCallerCodeExecution20250825 WebFetchTool20260309AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20260309AllowedCallerCodeExecution20260120 WebFetchTool20260309AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20260309AllowedCallerCodeExecution20260521 WebFetchTool20260309AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            List of domains to allow fetching from

          - `BlockedDomains []string`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

          - `UseCache bool`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `type WebSearchTool20260318 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `Type WebSearch20260318`

            - `const WebSearch20260318WebSearch20260318 WebSearch20260318 = "web_search_20260318"`

          - `AllowedCallers []string`

            - `const WebSearchTool20260318AllowedCallerDirect WebSearchTool20260318AllowedCaller = "direct"`

            - `const WebSearchTool20260318AllowedCallerCodeExecution20250825 WebSearchTool20260318AllowedCaller = "code_execution_20250825"`

            - `const WebSearchTool20260318AllowedCallerCodeExecution20260120 WebSearchTool20260318AllowedCaller = "code_execution_20260120"`

            - `const WebSearchTool20260318AllowedCallerCodeExecution20260521 WebSearchTool20260318AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `ResponseInclusion WebSearchTool20260318ResponseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `const WebSearchTool20260318ResponseInclusionFull WebSearchTool20260318ResponseInclusion = "full"`

            - `const WebSearchTool20260318ResponseInclusionExcluded WebSearchTool20260318ResponseInclusion = "excluded"`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `type WebFetchTool20260318 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `Type WebFetch20260318`

            - `const WebFetch20260318WebFetch20260318 WebFetch20260318 = "web_fetch_20260318"`

          - `AllowedCallers []string`

            - `const WebFetchTool20260318AllowedCallerDirect WebFetchTool20260318AllowedCaller = "direct"`

            - `const WebFetchTool20260318AllowedCallerCodeExecution20250825 WebFetchTool20260318AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20260318AllowedCallerCodeExecution20260120 WebFetchTool20260318AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20260318AllowedCallerCodeExecution20260521 WebFetchTool20260318AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string`

            List of domains to allow fetching from

          - `BlockedDomains []string`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

          - `MaxUses int64`

            Maximum number of times the tool can be used in the API request.

          - `ResponseInclusion WebFetchTool20260318ResponseInclusion`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `const WebFetchTool20260318ResponseInclusionFull WebFetchTool20260318ResponseInclusion = "full"`

            - `const WebFetchTool20260318ResponseInclusionExcluded WebFetchTool20260318ResponseInclusion = "excluded"`

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

          - `UseCache bool`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `type ToolSearchToolBm25_20251119 struct{…}`

          - `Name ToolSearchToolBm25`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const ToolSearchToolBm25ToolSearchToolBm25 ToolSearchToolBm25 = "tool_search_tool_bm25"`

          - `Type ToolSearchToolBm25_20251119Type`

            - `const ToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"`

            - `const ToolSearchToolBm25_20251119TypeToolSearchToolBm25 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"`

          - `AllowedCallers []string`

            - `const ToolSearchToolBm25_20251119AllowedCallerDirect ToolSearchToolBm25_20251119AllowedCaller = "direct"`

            - `const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"`

            - `const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"`

            - `const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260521 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

        - `type ToolSearchToolRegex20251119 struct{…}`

          - `Name ToolSearchToolRegex`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            - `const ToolSearchToolRegexToolSearchToolRegex ToolSearchToolRegex = "tool_search_tool_regex"`

          - `Type ToolSearchToolRegex20251119Type`

            - `const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"`

            - `const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool_search_tool_regex"`

          - `AllowedCallers []string`

            - `const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"`

            - `const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"`

            - `const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"`

            - `const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool`

            When true, guarantees schema validation on tool names and inputs

      - `TopK int64`

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

      - `TopP float64`

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

  - `UserProfileID param.Field[string]`

    Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

### Returns

- `type MessageBatch struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `ArchivedAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `CancelInitiatedAt Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `EndedAt Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `ExpiresAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus MessageBatchProcessingStatus`

    Processing status of the Message Batch.

    - `const MessageBatchProcessingStatusInProgress MessageBatchProcessingStatus = "in_progress"`

    - `const MessageBatchProcessingStatusCanceling MessageBatchProcessingStatus = "canceling"`

    - `const MessageBatchProcessingStatusEnded MessageBatchProcessingStatus = "ended"`

  - `RequestCounts MessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `Canceled int64`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `Errored int64`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `Expired int64`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `Processing int64`

      Number of requests in the Message Batch that are processing.

    - `Succeeded int64`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `ResultsURL string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `Type MessageBatch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    - `const MessageBatchMessageBatch MessageBatch = "message_batch"`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	messageBatch, err := client.Messages.Batches.New(context.TODO(), anthropic.MessageBatchNewParams{
		Requests: []anthropic.MessageBatchNewParamsRequest{anthropic.MessageBatchNewParamsRequest{
			CustomID: "my-custom-id-1",
			Params: anthropic.MessageBatchNewParamsRequestParams{
				MaxTokens: 1024,
				Messages: []anthropic.MessageParam{anthropic.MessageParam{
					Content: []anthropic.ContentBlockParamUnion{anthropic.ContentBlockParamUnion{
						OfText: &anthropic.TextBlockParam{
							Text: "x",
						},
					}},
					Role: anthropic.MessageParamRoleUser,
				}},
				Model: anthropic.ModelClaudeOpus5,
			},
		}},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messageBatch.ID)
}
```

#### Response

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
