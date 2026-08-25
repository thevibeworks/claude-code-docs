# Create a Message Batch

`client.Beta.Messages.Batches.New(ctx, params) (*BetaMessageBatch, error)`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `params BetaMessageBatchNewParams`

  - `Requests param.Field[[]BetaMessageBatchNewParamsRequest]`

    Body param: List of requests for prompt completion. Each is an individual request to create a Message.

    maxItems: 100000, minItems: 1

    - `CustomID string`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

    - `Params BetaMessageBatchNewParamsRequestParams`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

      - `MaxTokens int64`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

        Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

        minimum: 0

      - `Messages []BetaMessageParamResp`

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

        - `Content []BetaContentBlockParamUnionResp`

          - `[]BetaContentBlockParamUnionResp`

            - `type BetaTextBlockParamResp struct{…}`

              - `Text string`

                minLength: 1

              - `Type Text`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

                - `Type Ephemeral`

                - `TTL BetaCacheControlEphemeralTTL Optional`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"`

                  - `const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"`

              - `Citations []BetaTextCitationParamUnionResp Optional`

                - `type BetaCitationCharLocationParamResp struct{…}`

                  - `CitedText string`

                  - `DocumentIndex int64`

                    minimum: 0

                  - `DocumentTitle string`

                    maxLength: 500, minLength: 1

                  - `EndCharIndex int64`

                  - `StartCharIndex int64`

                    minimum: 0

                  - `Type CharLocation`

                - `type BetaCitationPageLocationParamResp struct{…}`

                  - `CitedText string`

                  - `DocumentIndex int64`

                    minimum: 0

                  - `DocumentTitle string`

                    maxLength: 500, minLength: 1

                  - `EndPageNumber int64`

                  - `StartPageNumber int64`

                    minimum: 1

                  - `Type PageLocation`

                - `type BetaCitationContentBlockLocationParamResp struct{…}`

                  - `CitedText string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `DocumentIndex int64`

                    minimum: 0

                  - `DocumentTitle string`

                    maxLength: 500, minLength: 1

                  - `EndBlockIndex int64`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `StartBlockIndex int64`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `Type ContentBlockLocation`

                - `type BetaCitationWebSearchResultLocationParamResp struct{…}`

                  - `CitedText string`

                  - `EncryptedIndex string`

                  - `Title string`

                    maxLength: 512, minLength: 1

                  - `Type WebSearchResultLocation`

                  - `URL string`

                    minLength: 1

                - `type BetaCitationSearchResultLocationParamResp struct{…}`

                  - `CitedText string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `EndBlockIndex int64`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `SearchResultIndex int64`

                    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                    Counted separately from `document_index`; server-side web search results are not included in this count.

                    minimum: 0

                  - `Source string`

                  - `StartBlockIndex int64`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `Title string`

                  - `Type SearchResultLocation`

            - `type BetaImageBlockParamResp struct{…}`

              - `Source BetaImageBlockParamSourceUnionResp`

                - `type BetaBase64ImageSource struct{…}`

                  - `Data string`

                    format: byte

                  - `MediaType BetaBase64ImageSourceMediaType`

                    - `const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"`

                    - `const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"`

                    - `const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"`

                    - `const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"`

                  - `Type Base64`

                - `type BetaURLImageSource struct{…}`

                  - `Type URL`

                  - `URL string`

                - `type BetaFileImageSource struct{…}`

                  - `FileID string`

                  - `Type File`

              - `Type Image`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Transformations BetaImageTransformationsParamResp Optional`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `OversizedImage BetaImageTransformationsParamOversizedImage Optional`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `const BetaImageTransformationsParamOversizedImageDownsize BetaImageTransformationsParamOversizedImage = "downsize"`

                  - `const BetaImageTransformationsParamOversizedImageError BetaImageTransformationsParamOversizedImage = "error"`

            - `type BetaRequestDocumentBlock struct{…}`

              - `Source BetaRequestDocumentBlockSourceUnion`

                - `type BetaBase64PDFSource struct{…}`

                  - `Data string`

                    format: byte

                  - `MediaType ApplicationPDF`

                  - `Type Base64`

                - `type BetaPlainTextSource struct{…}`

                  - `Data string`

                  - `MediaType TextPlain`

                  - `Type Text`

                - `type BetaContentBlockSource struct{…}`

                  - `Content BetaContentBlockSourceContentUnion`

                    - `string`

                    - `[]BetaContentBlockSourceContentUnion`

                      - `type BetaTextBlockParamResp struct{…}`

                      - `type BetaImageBlockParamResp struct{…}`

                  - `Type Content`

                - `type BetaURLPDFSource struct{…}`

                  - `Type URL`

                  - `URL string`

                - `type BetaFileDocumentSource struct{…}`

                  - `FileID string`

                  - `Type File`

              - `Type Document`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Citations BetaCitationsConfigParamResp Optional`

                - `Enabled bool Optional`

              - `Context string Optional`

                minLength: 1

              - `Title string Optional`

                maxLength: 500, minLength: 1

            - `type BetaSearchResultBlockParamResp struct{…}`

              - `Content []BetaTextBlockParamResp`

                - `Text string`

                  minLength: 1

                - `Type Text`

                - `CacheControl BetaCacheControlEphemeral Optional`

                  Create a cache control breakpoint at this content block.

                - `Citations []BetaTextCitationParamUnionResp Optional`

              - `Source string`

              - `Title string`

              - `Type SearchResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Citations BetaCitationsConfigParamResp Optional`

            - `type BetaThinkingBlockParamResp struct{…}`

              - `Signature string`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `Thinking string`

                The `thinking` text of this block as returned by the API.

              - `Type Thinking`

            - `type BetaRedactedThinkingBlockParamResp struct{…}`

              - `Data string`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `Type RedactedThinking`

            - `type BetaToolUseBlockParamResp struct{…}`

              - `ID string`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Input map[string, any]`

              - `Name string`

                maxLength: 200, minLength: 1

              - `Type ToolUse`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller BetaToolUseBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type BetaDirectCaller struct{…}`

                  Tool invocation directly from the model.

                  - `Type Direct`

                - `type BetaServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                  - `ToolID string`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `Type CodeExecution20250825`

                - `type BetaServerToolCaller20260120 struct{…}`

                  - `ToolID string`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `Type CodeExecution20260120`

              - `ToolsetName string Optional`

                For a toolset member tool_use, the toolset family this member belongs to.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `type BetaToolResultBlockParamResp struct{…}`

              - `ToolUseID string`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Type ToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Content []BetaToolResultBlockParamContentUnionResp Optional`

                - `[]BetaToolResultBlockParamContentUnionResp`

                  - `type BetaTextBlockParamResp struct{…}`

                  - `type BetaImageBlockParamResp struct{…}`

                  - `type BetaSearchResultBlockParamResp struct{…}`

                  - `type BetaRequestDocumentBlock struct{…}`

                  - `type BetaToolReferenceBlockParamResp struct{…}`

                    Tool reference block that can be included in tool_result content.

                    - `ToolName string`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `Type ToolReference`

                    - `CacheControl BetaCacheControlEphemeral Optional`

                      Create a cache control breakpoint at this content block.

                  - `type BetaBrowserStateBlockParamResp struct{…}`

                    The caller's browser state after a browser toolset member call —
                    the full inventory of open tabs, which tab is active, and any side
                    effects (tabs opened, download state changes) the call produced.

                    At most one per `tool_result`, only on a non-error result answering a
                    browser toolset member `tool_use`. The server renders the
                    model-visible text from it; the model never sees the raw fields.

                    - `Tabs []BetaBrowserStateTabEntry`

                      All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                      maxItems: 100

                      - `TabID string`

                        The caller-assigned identifier for this tab, unique within the inventory.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `Title string`

                        The title of the page the tab is showing. May be empty.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `URL string`

                        The URL of the page the tab is showing. May be empty.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `Active bool Optional`

                        Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                    - `Type BrowserState`

                    - `CacheControl BetaCacheControlEphemeral Optional`

                      Create a cache control breakpoint at this content block.

                    - `StateChanges []BetaBrowserStateChangeUnion Optional`

                      Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                      maxItems: 200, minItems: 1

                      - `type BetaBrowserStateChangeTabOpened struct{…}`

                        A tab this call's execution opened that remains open at its end —
                        the creation delta of the `tabs` inventory, not an event log.

                        Carries only the `tab_id`; the tab's `title` and `url` live on its
                        `tabs` entry, which must include the same `tab_id`. A tab opened
                        during a failed call gets no deferred `tab_opened`; it simply appears
                        in the next result's `tabs` inventory.

                        - `TabID string`

                          The `tab_id` of the opened tab, present in `tabs`.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type TabOpened`

                      - `type BetaBrowserStateChangeDownloadStarted struct{…}`

                        A file download that started during this call.

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type DownloadStarted`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type BetaBrowserStateChangeDownloadCompleted struct{…}`

                        A file download that finished during this call, reported with the
                        same `download_id` as its `download_started` — or without a prior
                        `download_started`, when the download finished during the call that
                        started it (at most one state change per `download_id` per result).

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type DownloadCompleted`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Path string Optional`

                          Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                        - `SizeBytes int64 Optional`

                          The completed download's size.

                          minimum: 0

                      - `type BetaBrowserStateChangeDownloadFailed struct{…}`

                        A file download that failed — or was cancelled — during this call.

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type DownloadFailed`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Error string Optional`

                          The failure or cancellation detail, when known.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

              - `IsError bool Optional`

              - `ToolsetName string Optional`

                For a toolset member tool_result, the toolset family of the paired tool_use.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `type BetaServerToolUseBlockParamResp struct{…}`

              - `ID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Input map[string, any]`

              - `Name BetaServerToolUseBlockParamName`

                - `const BetaServerToolUseBlockParamNameAdvisor BetaServerToolUseBlockParamName = "advisor"`

                - `const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web_search"`

                - `const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web_fetch"`

                - `const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code_execution"`

                - `const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash_code_execution"`

                - `const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text_editor_code_execution"`

                - `const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool_search_tool_regex"`

                - `const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool_search_tool_bm25"`

              - `Type ServerToolUse`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller BetaServerToolUseBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type BetaDirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type BetaServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type BetaServerToolCaller20260120 struct{…}`

            - `type BetaWebSearchToolResultBlockParamResp struct{…}`

              - `Content BetaWebSearchToolResultBlockParamContentUnionResp`

                - `[]BetaWebSearchResultBlockParamResp`

                  - `EncryptedContent string`

                  - `Title string`

                  - `Type WebSearchResult`

                  - `URL string`

                  - `PageAge string Optional`

                - `type BetaWebSearchToolRequestError struct{…}`

                  - `ErrorCode BetaWebSearchToolResultErrorCode`

                    - `const BetaWebSearchToolResultErrorCodeInvalidToolInput BetaWebSearchToolResultErrorCode = "invalid_tool_input"`

                    - `const BetaWebSearchToolResultErrorCodeUnavailable BetaWebSearchToolResultErrorCode = "unavailable"`

                    - `const BetaWebSearchToolResultErrorCodeMaxUsesExceeded BetaWebSearchToolResultErrorCode = "max_uses_exceeded"`

                    - `const BetaWebSearchToolResultErrorCodeTooManyRequests BetaWebSearchToolResultErrorCode = "too_many_requests"`

                    - `const BetaWebSearchToolResultErrorCodeQueryTooLong BetaWebSearchToolResultErrorCode = "query_too_long"`

                    - `const BetaWebSearchToolResultErrorCodeRequestTooLarge BetaWebSearchToolResultErrorCode = "request_too_large"`

                  - `Type WebSearchToolResultError`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type WebSearchToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller BetaWebSearchToolResultBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type BetaDirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type BetaServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type BetaServerToolCaller20260120 struct{…}`

            - `type BetaWebFetchToolResultBlockParamResp struct{…}`

              - `Content BetaWebFetchToolResultBlockParamContentUnionResp`

                - `type BetaWebFetchToolResultErrorBlockParamResp struct{…}`

                  - `ErrorCode BetaWebFetchToolResultErrorCode`

                    - `const BetaWebFetchToolResultErrorCodeInvalidToolInput BetaWebFetchToolResultErrorCode = "invalid_tool_input"`

                    - `const BetaWebFetchToolResultErrorCodeURLTooLong BetaWebFetchToolResultErrorCode = "url_too_long"`

                    - `const BetaWebFetchToolResultErrorCodeURLNotAllowed BetaWebFetchToolResultErrorCode = "url_not_allowed"`

                    - `const BetaWebFetchToolResultErrorCodeURLNotInPriorContext BetaWebFetchToolResultErrorCode = "url_not_in_prior_context"`

                    - `const BetaWebFetchToolResultErrorCodeURLNotAccessible BetaWebFetchToolResultErrorCode = "url_not_accessible"`

                    - `const BetaWebFetchToolResultErrorCodeUnsupportedContentType BetaWebFetchToolResultErrorCode = "unsupported_content_type"`

                    - `const BetaWebFetchToolResultErrorCodeTooManyRequests BetaWebFetchToolResultErrorCode = "too_many_requests"`

                    - `const BetaWebFetchToolResultErrorCodeMaxUsesExceeded BetaWebFetchToolResultErrorCode = "max_uses_exceeded"`

                    - `const BetaWebFetchToolResultErrorCodeUnavailable BetaWebFetchToolResultErrorCode = "unavailable"`

                  - `Type WebFetchToolResultError`

                - `type BetaWebFetchBlockParamResp struct{…}`

                  - `Content BetaRequestDocumentBlock`

                  - `Type WebFetchResult`

                  - `URL string`

                    Fetched content URL

                  - `RetrievedAt string Optional`

                    ISO 8601 timestamp when the content was retrieved

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type WebFetchToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller BetaWebFetchToolResultBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type BetaDirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type BetaServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type BetaServerToolCaller20260120 struct{…}`

            - `type BetaAdvisorToolResultBlockParamResp struct{…}`

              - `Content BetaAdvisorToolResultBlockParamContentUnionResp`

                - `type BetaAdvisorToolResultErrorParamResp struct{…}`

                  - `ErrorCode BetaAdvisorToolResultErrorParamErrorCode`

                    - `const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max_uses_exceeded"`

                    - `const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt_too_long"`

                    - `const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too_many_requests"`

                    - `const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"`

                    - `const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"`

                    - `const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution_time_exceeded"`

                    - `const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model_not_found"`

                  - `Type AdvisorToolResultError`

                - `type BetaAdvisorResultBlockParamResp struct{…}`

                  - `Text string`

                  - `Type AdvisorResult`

                  - `StopReason string Optional`

                - `type BetaAdvisorRedactedResultBlockParamResp struct{…}`

                  - `EncryptedContent string`

                    Opaque blob produced by a prior response; must be round-tripped verbatim.

                  - `Type AdvisorRedactedResult`

                  - `StopReason string Optional`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type AdvisorToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content BetaCodeExecutionToolResultBlockParamContentUnionResp`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type BetaCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode BetaCodeExecutionToolResultErrorCode`

                    - `const BetaCodeExecutionToolResultErrorCodeInvalidToolInput BetaCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const BetaCodeExecutionToolResultErrorCodeUnavailable BetaCodeExecutionToolResultErrorCode = "unavailable"`

                    - `const BetaCodeExecutionToolResultErrorCodeTooManyRequests BetaCodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded BetaCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                  - `Type CodeExecutionToolResultError`

                - `type BetaCodeExecutionResultBlockParamResp struct{…}`

                  - `Content []BetaCodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type CodeExecutionOutput`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Stdout string`

                  - `Type CodeExecutionResult`

                - `type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `Content []BetaCodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type CodeExecutionOutput`

                  - `EncryptedStdout string`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Type EncryptedCodeExecutionResult`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type CodeExecutionToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaBashCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp`

                - `type BetaBashCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode`

                    - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid_tool_input"`

                    - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"`

                    - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too_many_requests"`

                    - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution_time_exceeded"`

                    - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output_file_too_large"`

                  - `Type BashCodeExecutionToolResultError`

                - `type BetaBashCodeExecutionResultBlockParamResp struct{…}`

                  - `Content []BetaBashCodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type BashCodeExecutionOutput`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Stdout string`

                  - `Type BashCodeExecutionResult`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type BashCodeExecutionToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp`

                - `type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode`

                    - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid_tool_input"`

                    - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"`

                    - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too_many_requests"`

                    - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution_time_exceeded"`

                    - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file_not_found"`

                  - `Type TextEditorCodeExecutionToolResultError`

                  - `ErrorMessage string Optional`

                - `type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}`

                  - `Content string`

                  - `FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType`

                    - `const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"`

                    - `const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"`

                    - `const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"`

                  - `Type TextEditorCodeExecutionViewResult`

                  - `NumLines int64 Optional`

                  - `StartLine int64 Optional`

                  - `TotalLines int64 Optional`

                - `type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}`

                  - `IsFileUpdate bool`

                  - `Type TextEditorCodeExecutionCreateResult`

                - `type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}`

                  - `Type TextEditorCodeExecutionStrReplaceResult`

                  - `Lines []string Optional`

                  - `NewLines int64 Optional`

                  - `NewStart int64 Optional`

                  - `OldLines int64 Optional`

                  - `OldStart int64 Optional`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type TextEditorCodeExecutionToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaToolSearchToolResultBlockParamResp struct{…}`

              - `Content BetaToolSearchToolResultBlockParamContentUnionResp`

                - `type BetaToolSearchToolResultErrorParamResp struct{…}`

                  - `ErrorCode BetaToolSearchToolResultErrorParamErrorCode`

                    - `const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid_tool_input"`

                    - `const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"`

                    - `const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too_many_requests"`

                    - `const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution_time_exceeded"`

                  - `Type ToolSearchToolResultError`

                  - `ErrorMessage string Optional`

                - `type BetaToolSearchToolSearchResultBlockParamResp struct{…}`

                  - `ToolReferences []BetaToolReferenceBlockParamResp`

                    - `ToolName string`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `Type ToolReference`

                    - `CacheControl BetaCacheControlEphemeral Optional`

                      Create a cache control breakpoint at this content block.

                  - `Type ToolSearchToolSearchResult`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type ToolSearchToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaMCPToolUseBlockParamResp struct{…}`

              - `ID string`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Input map[string, any]`

              - `Name string`

              - `ServerName string`

                The name of the MCP server

              - `Type MCPToolUse`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaRequestMCPToolResultBlockParamResp struct{…}`

              - `ToolUseID string`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Type MCPToolResult`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Content BetaRequestMCPToolResultBlockParamContentUnionResp Optional`

                - `string`

                - `[]BetaTextBlockParamResp`

                  - `Text string`

                    minLength: 1

                  - `Type Text`

                  - `CacheControl BetaCacheControlEphemeral Optional`

                    Create a cache control breakpoint at this content block.

                  - `Citations []BetaTextCitationParamUnionResp Optional`

              - `IsError bool Optional`

            - `type BetaContainerUploadBlockParamResp struct{…}`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `FileID string`

              - `Type ContainerUpload`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaCompactionBlockParamResp struct{…}`

              A compaction block containing summary of previous context.

              Users should round-trip these blocks from responses to subsequent requests
              to maintain context across compaction boundaries.

              When content is None, the block represents a failed compaction. The server
              treats these as no-ops. Empty string content is not allowed.

              - `Type Compaction`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Content string Optional`

                Summary of previously compacted content, or null if compaction failed

              - `EncryptedContent string Optional`

                Opaque metadata from prior compaction, to be round-tripped verbatim

            - `type BetaRequestToolAdditionBlock struct{…}`

              Mid-conversation directive to surface a declared tool.

              `tool` references a tool (or MCP toolset) by name from the request's
              `tools`; it is offered to the model from this point in the
              conversation onward.

              - `Tool BetaRequestToolAdditionBlockToolUnion`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

                - `type BetaToolChangeToolReference struct{…}`

                  Reference to a single tool the caller declared directly in
                  `tools[]`. Does not accept the composed `{server}_{name}` form the
                  server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                  `mcp_toolset_reference` for those.

                  - `Name string`

                    pattern: ^[a-zA-Z0-9_-]{1,128}$

                  - `Type ToolReference`

                - `type BetaToolChangeMCPToolReference struct{…}`

                  Reference to a single MCP tool by its server and remote name — the
                  same `server_name`/`name` pair `mcp_tool_use` carries.

                  - `Name string`

                  - `ServerName string`

                  - `Type MCPToolReference`

                - `type BetaToolChangeMCPToolsetReference struct{…}`

                  Reference to every tool in the named MCP server's toolset.

                  - `ServerName string`

                  - `Type MCPToolsetReference`

              - `Type ToolAddition`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaRequestToolRemovalBlock struct{…}`

              Mid-conversation directive to withdraw a tool.

              `tool` references a tool (or MCP toolset) by name from the request's
              `tools`; it is no longer offered to the model from this point in the
              conversation onward.

              - `Tool BetaRequestToolRemovalBlockToolUnion`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

                - `type BetaToolChangeToolReference struct{…}`

                  Reference to a single tool the caller declared directly in
                  `tools[]`. Does not accept the composed `{server}_{name}` form the
                  server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                  `mcp_toolset_reference` for those.

                - `type BetaToolChangeMCPToolReference struct{…}`

                  Reference to a single MCP tool by its server and remote name — the
                  same `server_name`/`name` pair `mcp_tool_use` carries.

                - `type BetaToolChangeMCPToolsetReference struct{…}`

                  Reference to every tool in the named MCP server's toolset.

              - `Type ToolRemoval`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BetaFallbackBlockParamResp struct{…}`

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

              - `From BetaFallbackInfoParamResp`

                Identifies one hop of a fallback transition.

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

              - `To BetaFallbackInfoParamResp`

                Identifies one hop of a fallback transition.

              - `Type Fallback`

              - `Trigger any Optional`

                The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

        - `Role BetaMessageParamRole`

          - `const BetaMessageParamRoleUser BetaMessageParamRole = "user"`

          - `const BetaMessageParamRoleAssistant BetaMessageParamRole = "assistant"`

          - `const BetaMessageParamRoleSystem BetaMessageParamRole = "system"`

      - `Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `CacheControl BetaCacheControlEphemeral Optional`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `Container BetaMessageBatchNewParamsRequestParamsContainerUnion Optional`

        Container identifier for reuse across requests.

        - `type BetaContainerParamsResp struct{…}`

          Container parameters with skills to be loaded.

          - `ID string Optional`

            Container id

          - `Skills []BetaSkillParamsResp Optional`

            List of skills to load in the container

            maxItems: 20

            - `SkillID string`

              Skill ID

              maxLength: 64, minLength: 1

            - `Type BetaSkillParamsType`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `const BetaSkillParamsTypeAnthropic BetaSkillParamsType = "anthropic"`

              - `const BetaSkillParamsTypeCustom BetaSkillParamsType = "custom"`

            - `Version string Optional`

              Skill version or 'latest' for most recent version

              maxLength: 64, minLength: 1

        - `string`

      - `ContextManagement BetaContextManagementConfig Optional`

        Context management configuration.

        This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

        - `Edits []BetaContextManagementConfigEditUnion Optional`

          List of context management edits to apply

          minItems: 0

          - `type BetaClearToolUses20250919Edit struct{…}`

            - `Type ClearToolUses20250919`

            - `ClearAtLeast BetaInputTokensClearAtLeast Optional`

              Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

              - `Type InputTokens`

              - `Value int64`

                minimum: 0

            - `ClearToolInputs BetaClearToolUses20250919EditClearToolInputsUnion Optional`

              Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

              - `bool`

              - `[]string`

            - `ExcludeTools []string Optional`

              Tool names whose uses are preserved from clearing

            - `Keep BetaToolUsesKeep Optional`

              Number of tool uses to retain in the conversation

              - `Type ToolUses`

              - `Value int64`

                minimum: 0

            - `Trigger BetaClearToolUses20250919EditTriggerUnion Optional`

              Condition that triggers the context management strategy

              - `type BetaInputTokensTrigger struct{…}`

                - `Type InputTokens`

                - `Value int64`

                  minimum: 1

              - `type BetaToolUsesTrigger struct{…}`

                - `Type ToolUses`

                - `Value int64`

                  minimum: 1

          - `type BetaClearThinking20251015Edit struct{…}`

            - `Type ClearThinking20251015`

            - `Keep BetaClearThinking20251015EditKeepUnion Optional`

              Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

              - `type BetaThinkingTurns struct{…}`

                - `Type ThinkingTurns`

                - `Value int64`

                  minimum: 1

              - `type BetaAllThinkingTurns struct{…}`

                - `Type All`

              - `All`

          - `type BetaCompact20260112Edit struct{…}`

            Automatically compact older context when reaching the configured trigger threshold.

            - `Type Compact20260112`

            - `Instructions string Optional`

              Additional instructions for summarization.

            - `PauseAfterCompaction bool Optional`

              Whether to pause after compaction and return the compaction block to the user.

            - `Trigger BetaInputTokensTrigger Optional`

              When to trigger compaction. Defaults to 150000 input tokens.

      - `Diagnostics BetaDiagnosticsParamResp Optional`

        Request-level diagnostics. Currently carries the previous response
        id for prompt-cache divergence reporting.

        - `PreviousMessageID string Optional`

          The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

          maxLength: 256

      - `FallbackCreditToken BetaMessageBatchNewParamsRequestParamsFallbackCreditTokenUnion Optional`

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

        - `type BetaFallbackCreditTokenParamResp struct{…}`

          Object form of `fallback_credit_token`: the token plus a redemption
          mode.

          Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
          header the field accepts the bare string only. The bare string and the
          mode-less object are equivalent (both select `strict`), so wrapping
          an existing token changes nothing by itself.

          - `Token string`

            The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

            maxLength: 2048, minLength: 1

          - `Mode BetaFallbackCreditTokenParamMode Optional`

            How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

            - `const BetaFallbackCreditTokenParamModeStrict BetaFallbackCreditTokenParamMode = "strict"`

            - `const BetaFallbackCreditTokenParamModeBestEffort BetaFallbackCreditTokenParamMode = "best_effort"`

      - `Fallbacks BetaFallbacksParamUnionResp Optional`

        Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

        - `[]BetaFallbackParamResp`

          - `Model Model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `MaxTokens int64 Optional`

          - `OutputConfig BetaOutputConfig Optional`

            - `Effort BetaOutputConfigEffort Optional`

              All possible effort levels.

              - `const BetaOutputConfigEffortLow BetaOutputConfigEffort = "low"`

              - `const BetaOutputConfigEffortMedium BetaOutputConfigEffort = "medium"`

              - `const BetaOutputConfigEffortHigh BetaOutputConfigEffort = "high"`

              - `const BetaOutputConfigEffortXhigh BetaOutputConfigEffort = "xhigh"`

              - `const BetaOutputConfigEffortMax BetaOutputConfigEffort = "max"`

            - `Format BetaJSONOutputFormat Optional`

              A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

              - `Schema map[string, any]`

                The JSON schema of the format

              - `Type JSONSchema`

            - `TaskBudget BetaTokenTaskBudget Optional`

              User-configurable total token budget across contexts.

              - `Total int64`

                Total token budget across all contexts in the session.

                minimum: 1024

              - `Type Tokens`

                The budget type. Currently only 'tokens' is supported.

              - `Remaining int64 Optional`

                Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

                minimum: 0

          - `Speed BetaFallbackParamSpeed Optional`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `const BetaFallbackParamSpeedStandard BetaFallbackParamSpeed = "standard"`

            - `const BetaFallbackParamSpeedFast BetaFallbackParamSpeed = "fast"`

          - `Thinking BetaFallbackParamThinkingUnionResp Optional`

            - `type BetaThinkingConfigEnabled struct{…}`

              - `BudgetTokens int64`

                Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

                Must be ≥1024 and less than `max_tokens`.

                See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

                minimum: 1024

              - `Type Enabled`

              - `Display BetaThinkingConfigEnabledDisplay Optional`

                Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

                - `const BetaThinkingConfigEnabledDisplaySummarized BetaThinkingConfigEnabledDisplay = "summarized"`

                - `const BetaThinkingConfigEnabledDisplayOmitted BetaThinkingConfigEnabledDisplay = "omitted"`

            - `type BetaThinkingConfigDisabled struct{…}`

              - `Type Disabled`

            - `type BetaThinkingConfigAdaptive struct{…}`

              - `Type Adaptive`

              - `Display BetaThinkingConfigAdaptiveDisplay Optional`

                Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

                - `const BetaThinkingConfigAdaptiveDisplaySummarized BetaThinkingConfigAdaptiveDisplay = "summarized"`

                - `const BetaThinkingConfigAdaptiveDisplayOmitted BetaThinkingConfigAdaptiveDisplay = "omitted"`

        - `Default`

      - `InferenceGeo string Optional`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `MCPServers []BetaRequestMCPServerURLDefinition Optional`

        MCP servers to be utilized in this request

        maxItems: 20

        - `Name string`

        - `Type URL`

        - `URL string`

        - `AuthorizationToken string Optional`

        - `ToolConfiguration BetaRequestMCPServerToolConfiguration Optional`

          - `AllowedTools []string Optional`

          - `Enabled bool Optional`

      - `Metadata BetaMetadata Optional`

        An object describing metadata about the request.

        - `UserID string Optional`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

          maxLength: 512

      - `OutputConfig BetaOutputConfig Optional`

        Configuration options for the model's output, such as the output format.

      - `ServiceTier string Optional`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `const BetaMessageBatchNewParamsRequestParamsServiceTierAuto BetaMessageBatchNewParamsRequestParamsServiceTier = "auto"`

        - `const BetaMessageBatchNewParamsRequestParamsServiceTierStandardOnly BetaMessageBatchNewParamsRequestParamsServiceTier = "standard_only"`

      - `Speed string Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaMessageBatchNewParamsRequestParamsSpeedStandard BetaMessageBatchNewParamsRequestParamsSpeed = "standard"`

        - `const BetaMessageBatchNewParamsRequestParamsSpeedFast BetaMessageBatchNewParamsRequestParamsSpeed = "fast"`

      - `StopSequences []string Optional`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `Stream bool Optional`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

      - `System []BetaTextBlockParamResp Optional`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

        - `[]BetaTextBlockParam`

          - `Text string`

            minLength: 1

          - `Type Text`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations []BetaTextCitationParamUnionResp Optional`

      - `Thinking BetaThinkingConfigParamUnionResp Optional`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `type BetaThinkingConfigEnabled struct{…}`

        - `type BetaThinkingConfigDisabled struct{…}`

        - `type BetaThinkingConfigAdaptive struct{…}`

      - `ToolChoice BetaToolChoiceUnion Optional`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `type BetaToolChoiceAuto struct{…}`

          The model will automatically decide whether to use tools.

          - `Type Auto`

          - `DisableParallelToolUse bool Optional`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `type BetaToolChoiceAny struct{…}`

          The model will use any available tools.

          - `Type Any`

          - `DisableParallelToolUse bool Optional`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `type BetaToolChoiceTool struct{…}`

          The model will use the specified tool with `tool_choice.name`.

          - `Name string`

            The name of the tool to use.

          - `Type Tool`

          - `DisableParallelToolUse bool Optional`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `type BetaToolChoiceNone struct{…}`

          The model will not be allowed to use tools.

          - `Type None`

      - `Tools []BetaToolUnion Optional`

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

        - `type BetaTool struct{…}`

          - `InputSchema BetaToolInputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

          - `AllowedCallers []string Optional`

            - `const BetaToolAllowedCallerDirect BetaToolAllowedCaller = "direct"`

            - `const BetaToolAllowedCallerCodeExecution20250825 BetaToolAllowedCaller = "code_execution_20250825"`

            - `const BetaToolAllowedCallerCodeExecution20260120 BetaToolAllowedCaller = "code_execution_20260120"`

            - `const BetaToolAllowedCallerCodeExecution20260521 BetaToolAllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Description string Optional`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `EagerInputStreaming bool Optional`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `Type BetaToolType Optional`

        - `type BetaToolBash20241022 struct{…}`

          - `Name Bash`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Bash20241022`

          - `AllowedCallers []string Optional`

            - `const BetaToolBash20241022AllowedCallerDirect BetaToolBash20241022AllowedCaller = "direct"`

            - `const BetaToolBash20241022AllowedCallerCodeExecution20250825 BetaToolBash20241022AllowedCaller = "code_execution_20250825"`

            - `const BetaToolBash20241022AllowedCallerCodeExecution20260120 BetaToolBash20241022AllowedCaller = "code_execution_20260120"`

            - `const BetaToolBash20241022AllowedCallerCodeExecution20260521 BetaToolBash20241022AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolBash20250124 struct{…}`

          - `Name Bash`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Bash20250124`

          - `AllowedCallers []string Optional`

            - `const BetaToolBash20250124AllowedCallerDirect BetaToolBash20250124AllowedCaller = "direct"`

            - `const BetaToolBash20250124AllowedCallerCodeExecution20250825 BetaToolBash20250124AllowedCaller = "code_execution_20250825"`

            - `const BetaToolBash20250124AllowedCallerCodeExecution20260120 BetaToolBash20250124AllowedCaller = "code_execution_20260120"`

            - `const BetaToolBash20250124AllowedCallerCodeExecution20260521 BetaToolBash20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaCodeExecutionTool20250522 struct{…}`

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20250522`

          - `AllowedCallers []string Optional`

            - `const BetaCodeExecutionTool20250522AllowedCallerDirect BetaCodeExecutionTool20250522AllowedCaller = "direct"`

            - `const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20250825"`

            - `const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20260120"`

            - `const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaCodeExecutionTool20250825 struct{…}`

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20250825`

          - `AllowedCallers []string Optional`

            - `const BetaCodeExecutionTool20250825AllowedCallerDirect BetaCodeExecutionTool20250825AllowedCaller = "direct"`

            - `const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20250825"`

            - `const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20260120"`

            - `const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaCodeExecutionTool20260120 struct{…}`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20260120`

          - `AllowedCallers []string Optional`

            - `const BetaCodeExecutionTool20260120AllowedCallerDirect BetaCodeExecutionTool20260120AllowedCaller = "direct"`

            - `const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260120AllowedCaller = "code_execution_20250825"`

            - `const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260120AllowedCaller = "code_execution_20260120"`

            - `const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260120AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaCodeExecutionTool20260521 struct{…}`

          Code execution tool with REPL state persistence.

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20260521`

          - `AllowedCallers []string Optional`

            - `const BetaCodeExecutionTool20260521AllowedCallerDirect BetaCodeExecutionTool20260521AllowedCaller = "direct"`

            - `const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260521AllowedCaller = "code_execution_20250825"`

            - `const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260521AllowedCaller = "code_execution_20260120"`

            - `const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260521AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaBrowserToolset20260801 struct{…}`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `Type BrowserToolset20260801`

          - `AllowedCallers []string Optional`

            - `const BetaBrowserToolset20260801AllowedCallerDirect BetaBrowserToolset20260801AllowedCaller = "direct"`

            - `const BetaBrowserToolset20260801AllowedCallerCodeExecution20250825 BetaBrowserToolset20260801AllowedCaller = "code_execution_20250825"`

            - `const BetaBrowserToolset20260801AllowedCallerCodeExecution20260120 BetaBrowserToolset20260801AllowedCaller = "code_execution_20260120"`

            - `const BetaBrowserToolset20260801AllowedCallerCodeExecution20260521 BetaBrowserToolset20260801AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Configs BetaBrowserToolsetConfigs Optional`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `CloseTab BetaBrowserCloseTabConfig Optional`

              `close_tab`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `DoubleClick BetaBrowserDoubleClickConfig Optional`

              `double_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `FileUpload BetaBrowserFileUploadConfig Optional`

              `file_upload`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Find BetaBrowserFindConfig Optional`

              `find`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `FormInput BetaBrowserFormInputConfig Optional`

              `form_input`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `GetPageText BetaBrowserGetPageTextConfig Optional`

              `get_page_text`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `HoldKey BetaBrowserHoldKeyConfig Optional`

              `hold_key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Hover BetaBrowserHoverConfig Optional`

              `hover`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `JavascriptExec BetaBrowserJavascriptExecConfig Optional`

              `javascript_exec`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Key BetaBrowserKeyConfig Optional`

              `key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClick BetaBrowserLeftClickConfig Optional`

              `left_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClickDrag BetaBrowserLeftClickDragConfig Optional`

              `left_click_drag`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseDown BetaBrowserLeftMouseDownConfig Optional`

              `left_mouse_down`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseUp BetaBrowserLeftMouseUpConfig Optional`

              `left_mouse_up`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ListTabs BetaBrowserListTabsConfig Optional`

              `list_tabs`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MiddleClick BetaBrowserMiddleClickConfig Optional`

              `middle_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MouseMove BetaBrowserMouseMoveConfig Optional`

              `mouse_move`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Navigate BetaBrowserNavigateConfig Optional`

              `navigate`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `NewTab BetaBrowserNewTabConfig Optional`

              `new_tab`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadConsole BetaBrowserReadConsoleConfig Optional`

              `read_console`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadNetwork BetaBrowserReadNetworkConfig Optional`

              `read_network`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadPage BetaBrowserReadPageConfig Optional`

              `read_page`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `RightClick BetaBrowserRightClickConfig Optional`

              `right_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Screenshot BetaBrowserScreenshotConfig Optional`

              `screenshot`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Scroll BetaBrowserScrollConfig Optional`

              `scroll`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ScrollTo BetaBrowserScrollToConfig Optional`

              `scroll_to`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `SwitchTab BetaBrowserSwitchTabConfig Optional`

              `switch_tab`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `TripleClick BetaBrowserTripleClickConfig Optional`

              `triple_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Type BetaBrowserTypeConfig Optional`

              `type`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Wait BetaBrowserWaitConfig Optional`

              `wait`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Zoom BetaBrowserZoomConfig Optional`

              `zoom`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type BetaToolComputerUse20241022 struct{…}`

          - `DisplayHeightPx int64`

            The height of the display in pixels.

            minimum: 1

          - `DisplayWidthPx int64`

            The width of the display in pixels.

            minimum: 1

          - `Name Computer`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Computer20241022`

          - `AllowedCallers []string Optional`

            - `const BetaToolComputerUse20241022AllowedCallerDirect BetaToolComputerUse20241022AllowedCaller = "direct"`

            - `const BetaToolComputerUse20241022AllowedCallerCodeExecution20250825 BetaToolComputerUse20241022AllowedCaller = "code_execution_20250825"`

            - `const BetaToolComputerUse20241022AllowedCallerCodeExecution20260120 BetaToolComputerUse20241022AllowedCaller = "code_execution_20260120"`

            - `const BetaToolComputerUse20241022AllowedCallerCodeExecution20260521 BetaToolComputerUse20241022AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `DisplayNumber int64 Optional`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaMemoryTool20250818 struct{…}`

          - `Name Memory`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Memory20250818`

          - `AllowedCallers []string Optional`

            - `const BetaMemoryTool20250818AllowedCallerDirect BetaMemoryTool20250818AllowedCaller = "direct"`

            - `const BetaMemoryTool20250818AllowedCallerCodeExecution20250825 BetaMemoryTool20250818AllowedCaller = "code_execution_20250825"`

            - `const BetaMemoryTool20250818AllowedCallerCodeExecution20260120 BetaMemoryTool20250818AllowedCaller = "code_execution_20260120"`

            - `const BetaMemoryTool20250818AllowedCallerCodeExecution20260521 BetaMemoryTool20250818AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolComputerUse20250124 struct{…}`

          - `DisplayHeightPx int64`

            The height of the display in pixels.

            minimum: 1

          - `DisplayWidthPx int64`

            The width of the display in pixels.

            minimum: 1

          - `Name Computer`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Computer20250124`

          - `AllowedCallers []string Optional`

            - `const BetaToolComputerUse20250124AllowedCallerDirect BetaToolComputerUse20250124AllowedCaller = "direct"`

            - `const BetaToolComputerUse20250124AllowedCallerCodeExecution20250825 BetaToolComputerUse20250124AllowedCaller = "code_execution_20250825"`

            - `const BetaToolComputerUse20250124AllowedCallerCodeExecution20260120 BetaToolComputerUse20250124AllowedCaller = "code_execution_20260120"`

            - `const BetaToolComputerUse20250124AllowedCallerCodeExecution20260521 BetaToolComputerUse20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `DisplayNumber int64 Optional`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolTextEditor20241022 struct{…}`

          - `Name StrReplaceEditor`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20241022`

          - `AllowedCallers []string Optional`

            - `const BetaToolTextEditor20241022AllowedCallerDirect BetaToolTextEditor20241022AllowedCaller = "direct"`

            - `const BetaToolTextEditor20241022AllowedCallerCodeExecution20250825 BetaToolTextEditor20241022AllowedCaller = "code_execution_20250825"`

            - `const BetaToolTextEditor20241022AllowedCallerCodeExecution20260120 BetaToolTextEditor20241022AllowedCaller = "code_execution_20260120"`

            - `const BetaToolTextEditor20241022AllowedCallerCodeExecution20260521 BetaToolTextEditor20241022AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolComputerUse20251124 struct{…}`

          - `DisplayHeightPx int64`

            The height of the display in pixels.

            minimum: 1

          - `DisplayWidthPx int64`

            The width of the display in pixels.

            minimum: 1

          - `Name Computer`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Computer20251124`

          - `AllowedCallers []string Optional`

            - `const BetaToolComputerUse20251124AllowedCallerDirect BetaToolComputerUse20251124AllowedCaller = "direct"`

            - `const BetaToolComputerUse20251124AllowedCallerCodeExecution20250825 BetaToolComputerUse20251124AllowedCaller = "code_execution_20250825"`

            - `const BetaToolComputerUse20251124AllowedCallerCodeExecution20260120 BetaToolComputerUse20251124AllowedCaller = "code_execution_20260120"`

            - `const BetaToolComputerUse20251124AllowedCallerCodeExecution20260521 BetaToolComputerUse20251124AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `DisplayNumber int64 Optional`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `EnableZoom bool Optional`

            Whether to enable an action to take a zoomed-in screenshot of the screen.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaComputerToolset20260801 struct{…}`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `Type ComputerToolset20260801`

          - `AllowedCallers []string Optional`

            - `const BetaComputerToolset20260801AllowedCallerDirect BetaComputerToolset20260801AllowedCaller = "direct"`

            - `const BetaComputerToolset20260801AllowedCallerCodeExecution20250825 BetaComputerToolset20260801AllowedCaller = "code_execution_20250825"`

            - `const BetaComputerToolset20260801AllowedCallerCodeExecution20260120 BetaComputerToolset20260801AllowedCaller = "code_execution_20260120"`

            - `const BetaComputerToolset20260801AllowedCallerCodeExecution20260521 BetaComputerToolset20260801AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Configs BetaComputerToolsetConfigs Optional`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `CursorPosition BetaComputerCursorPositionConfig Optional`

              `cursor_position`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `DoubleClick BetaComputerDoubleClickConfig Optional`

              `double_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `HoldKey BetaComputerHoldKeyConfig Optional`

              `hold_key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Key BetaComputerKeyConfig Optional`

              `key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClick BetaComputerLeftClickConfig Optional`

              `left_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClickDrag BetaComputerLeftClickDragConfig Optional`

              `left_click_drag`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseDown BetaComputerLeftMouseDownConfig Optional`

              `left_mouse_down`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseUp BetaComputerLeftMouseUpConfig Optional`

              `left_mouse_up`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MiddleClick BetaComputerMiddleClickConfig Optional`

              `middle_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MouseMove BetaComputerMouseMoveConfig Optional`

              `mouse_move`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `RightClick BetaComputerRightClickConfig Optional`

              `right_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Screenshot BetaComputerScreenshotConfig Optional`

              `screenshot`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Scroll BetaComputerScrollConfig Optional`

              `scroll`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `TripleClick BetaComputerTripleClickConfig Optional`

              `triple_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Type BetaComputerTypeConfig Optional`

              `type`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Wait BetaComputerWaitConfig Optional`

              `wait`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Zoom BetaComputerZoomConfig Optional`

              `zoom`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type BetaToolTextEditor20250124 struct{…}`

          - `Name StrReplaceEditor`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20250124`

          - `AllowedCallers []string Optional`

            - `const BetaToolTextEditor20250124AllowedCallerDirect BetaToolTextEditor20250124AllowedCaller = "direct"`

            - `const BetaToolTextEditor20250124AllowedCallerCodeExecution20250825 BetaToolTextEditor20250124AllowedCaller = "code_execution_20250825"`

            - `const BetaToolTextEditor20250124AllowedCallerCodeExecution20260120 BetaToolTextEditor20250124AllowedCaller = "code_execution_20260120"`

            - `const BetaToolTextEditor20250124AllowedCallerCodeExecution20260521 BetaToolTextEditor20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolTextEditor20250429 struct{…}`

          - `Name StrReplaceBasedEditTool`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20250429`

          - `AllowedCallers []string Optional`

            - `const BetaToolTextEditor20250429AllowedCallerDirect BetaToolTextEditor20250429AllowedCaller = "direct"`

            - `const BetaToolTextEditor20250429AllowedCallerCodeExecution20250825 BetaToolTextEditor20250429AllowedCaller = "code_execution_20250825"`

            - `const BetaToolTextEditor20250429AllowedCallerCodeExecution20260120 BetaToolTextEditor20250429AllowedCaller = "code_execution_20260120"`

            - `const BetaToolTextEditor20250429AllowedCallerCodeExecution20260521 BetaToolTextEditor20250429AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolTextEditor20250728 struct{…}`

          - `Name StrReplaceBasedEditTool`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20250728`

          - `AllowedCallers []string Optional`

            - `const BetaToolTextEditor20250728AllowedCallerDirect BetaToolTextEditor20250728AllowedCaller = "direct"`

            - `const BetaToolTextEditor20250728AllowedCallerCodeExecution20250825 BetaToolTextEditor20250728AllowedCaller = "code_execution_20250825"`

            - `const BetaToolTextEditor20250728AllowedCallerCodeExecution20260120 BetaToolTextEditor20250728AllowedCaller = "code_execution_20260120"`

            - `const BetaToolTextEditor20250728AllowedCallerCodeExecution20260521 BetaToolTextEditor20250728AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `MaxCharacters int64 Optional`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaWebSearchTool20250305 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebSearch20250305`

          - `AllowedCallers []string Optional`

            - `const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"`

            - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code_execution_20250825"`

            - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20260120 BetaWebSearchTool20250305AllowedCaller = "code_execution_20260120"`

            - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20260521 BetaWebSearchTool20250305AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string Optional`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation BetaUserLocation Optional`

            Parameters for the user's location. Used to provide more relevant search results.

            - `Type Approximate`

            - `City string Optional`

              The city of the user.

              maxLength: 255, minLength: 1

            - `Country string Optional`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

              maxLength: 2, minLength: 2

            - `Region string Optional`

              The region of the user.

              maxLength: 255, minLength: 1

            - `Timezone string Optional`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

              maxLength: 255, minLength: 1

        - `type BetaWebFetchTool20250910 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20250910`

          - `AllowedCallers []string Optional`

            - `const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"`

            - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code_execution_20250825"`

            - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20260120 BetaWebFetchTool20250910AllowedCaller = "code_execution_20260120"`

            - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20260521 BetaWebFetchTool20250910AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations BetaCitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaWebSearchTool20260209 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebSearch20260209`

          - `AllowedCallers []string Optional`

            - `const BetaWebSearchTool20260209AllowedCallerDirect BetaWebSearchTool20260209AllowedCaller = "direct"`

            - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20250825 BetaWebSearchTool20260209AllowedCaller = "code_execution_20250825"`

            - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20260120 BetaWebSearchTool20260209AllowedCaller = "code_execution_20260120"`

            - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20260521 BetaWebSearchTool20260209AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string Optional`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation BetaUserLocation Optional`

            Parameters for the user's location. Used to provide more relevant search results.

        - `type BetaWebFetchTool20260209 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20260209`

          - `AllowedCallers []string Optional`

            - `const BetaWebFetchTool20260209AllowedCallerDirect BetaWebFetchTool20260209AllowedCaller = "direct"`

            - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20250825 BetaWebFetchTool20260209AllowedCaller = "code_execution_20250825"`

            - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20260120 BetaWebFetchTool20260209AllowedCaller = "code_execution_20260120"`

            - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20260521 BetaWebFetchTool20260209AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations BetaCitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaWebFetchTool20260309 struct{…}`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20260309`

          - `AllowedCallers []string Optional`

            - `const BetaWebFetchTool20260309AllowedCallerDirect BetaWebFetchTool20260309AllowedCaller = "direct"`

            - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20250825 BetaWebFetchTool20260309AllowedCaller = "code_execution_20250825"`

            - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20260120 BetaWebFetchTool20260309AllowedCaller = "code_execution_20260120"`

            - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20260521 BetaWebFetchTool20260309AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations BetaCitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UseCache bool Optional`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `type BetaWebSearchTool20260318 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebSearch20260318`

          - `AllowedCallers []string Optional`

            - `const BetaWebSearchTool20260318AllowedCallerDirect BetaWebSearchTool20260318AllowedCaller = "direct"`

            - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20250825 BetaWebSearchTool20260318AllowedCaller = "code_execution_20250825"`

            - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20260120 BetaWebSearchTool20260318AllowedCaller = "code_execution_20260120"`

            - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20260521 BetaWebSearchTool20260318AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string Optional`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `ResponseInclusion BetaWebSearchTool20260318ResponseInclusion Optional`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `const BetaWebSearchTool20260318ResponseInclusionFull BetaWebSearchTool20260318ResponseInclusion = "full"`

            - `const BetaWebSearchTool20260318ResponseInclusionExcluded BetaWebSearchTool20260318ResponseInclusion = "excluded"`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation BetaUserLocation Optional`

            Parameters for the user's location. Used to provide more relevant search results.

        - `type BetaWebFetchTool20260318 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20260318`

          - `AllowedCallers []string Optional`

            - `const BetaWebFetchTool20260318AllowedCallerDirect BetaWebFetchTool20260318AllowedCaller = "direct"`

            - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20250825 BetaWebFetchTool20260318AllowedCaller = "code_execution_20250825"`

            - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20260120 BetaWebFetchTool20260318AllowedCaller = "code_execution_20260120"`

            - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20260521 BetaWebFetchTool20260318AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations BetaCitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `ResponseInclusion BetaWebFetchTool20260318ResponseInclusion Optional`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `const BetaWebFetchTool20260318ResponseInclusionFull BetaWebFetchTool20260318ResponseInclusion = "full"`

            - `const BetaWebFetchTool20260318ResponseInclusionExcluded BetaWebFetchTool20260318ResponseInclusion = "excluded"`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UseCache bool Optional`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `type BetaAdvisorTool20260301 struct{…}`

          - `Model Model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Name Advisor`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Advisor20260301`

          - `AllowedCallers []string Optional`

            - `const BetaAdvisorTool20260301AllowedCallerDirect BetaAdvisorTool20260301AllowedCaller = "direct"`

            - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20250825 BetaAdvisorTool20260301AllowedCaller = "code_execution_20250825"`

            - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20260120 BetaAdvisorTool20260301AllowedCaller = "code_execution_20260120"`

            - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20260521 BetaAdvisorTool20260301AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Caching BetaCacheControlEphemeral Optional`

            Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxTokens int64 Optional`

            Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

            minimum: 1024

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolSearchToolBm25_20251119 struct{…}`

          - `Name ToolSearchToolBm25`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type BetaToolSearchToolBm25_20251119Type`

            - `const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"`

            - `const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"`

          - `AllowedCallers []string Optional`

            - `const BetaToolSearchToolBm25_20251119AllowedCallerDirect BetaToolSearchToolBm25_20251119AllowedCaller = "direct"`

            - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"`

            - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"`

            - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaToolSearchToolRegex20251119 struct{…}`

          - `Name ToolSearchToolRegex`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type BetaToolSearchToolRegex20251119Type`

            - `const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"`

            - `const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex"`

          - `AllowedCallers []string Optional`

            - `const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"`

            - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"`

            - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"`

            - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20260521"`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BetaMCPToolset struct{…}`

          Configuration for a group of tools from an MCP server.

          Allows configuring enabled status and defer_loading for all tools
          from an MCP server, with optional per-tool overrides.

          - `MCPServerName string`

            Name of the MCP server to configure tools for

            maxLength: 255, minLength: 1

          - `Type MCPToolset`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Configs map[string, BetaMCPToolConfig] Optional`

            Configuration overrides for specific tools, keyed by tool name

            - `DeferLoading bool Optional`

            - `Enabled bool Optional`

          - `DefaultConfig BetaMCPToolDefaultConfig Optional`

            Default configuration applied to all tools from this server

            - `DeferLoading bool Optional`

            - `Enabled bool Optional`

      - `OutputFormat BetaJSONOutputFormat Optional`

        **Deprecated**

        Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

      - `Temperature float64 Optional`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

        maximum: 1, minimum: 0

      - `TopK int64 Optional`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

        minimum: 0

      - `TopP float64 Optional`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

        maximum: 1, minimum: 0

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

  - `UserProfileID param.Field[string] Optional`

    Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

## Returns

- `type BetaMessageBatch struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `ArchivedAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `CancelInitiatedAt Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `EndedAt Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `ExpiresAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus BetaMessageBatchProcessingStatus`

    Processing status of the Message Batch.

    - `const BetaMessageBatchProcessingStatusInProgress BetaMessageBatchProcessingStatus = "in_progress"`

    - `const BetaMessageBatchProcessingStatusCanceling BetaMessageBatchProcessingStatus = "canceling"`

    - `const BetaMessageBatchProcessingStatusEnded BetaMessageBatchProcessingStatus = "ended"`

  - `RequestCounts BetaMessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `Canceled int64`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `Errored int64`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `Expired int64`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `Processing int64`

      Number of requests in the Message Batch that are processing.

      default: 0

    - `Succeeded int64`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

  - `ResultsURL string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `Type MessageBatch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    default: message_batch

## Example

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
	betaMessageBatch, err := client.Beta.Messages.Batches.New(context.TODO(), anthropic.BetaMessageBatchNewParams{
		Requests: []anthropic.BetaMessageBatchNewParamsRequest{anthropic.BetaMessageBatchNewParamsRequest{
			CustomID: "my-custom-id-1",
			Params: anthropic.BetaMessageBatchNewParamsRequestParams{
				MaxTokens: 1024,
				Messages: []anthropic.BetaMessageParam{anthropic.BetaMessageParam{
					Content: []anthropic.BetaContentBlockParamUnion{anthropic.BetaContentBlockParamUnion{
						OfText: &anthropic.BetaTextBlockParam{
							Text: "x",
						},
					}},
					Role: anthropic.BetaMessageParamRoleUser,
				}},
				Model: anthropic.ModelClaudeOpus5,
			},
		}},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaMessageBatch.ID)
}
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
