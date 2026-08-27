# Batches

## Create a Message Batch

`BetaMessageBatch beta().messages().batches().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `BatchCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

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

      - `List<BetaMessageParam> messages`

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

          - `List<BetaContentBlockParam>`

            - `class BetaTextBlockParam:`

              - `String text`

                minLength: 1

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonValue type constant`

                - `Optional<Ttl> ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `TTL_5M("5m")`

                  - `TTL_1H("1h")`

              - `Optional<List<BetaTextCitationParam>> citations`

                - `class BetaCitationCharLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endCharIndex`

                  - `long startCharIndex`

                    minimum: 0

                  - `JsonValue type constant`

                - `class BetaCitationPageLocationParam:`

                  - `String citedText`

                  - `long documentIndex`

                    minimum: 0

                  - `Optional<String> documentTitle`

                    maxLength: 500, minLength: 1

                  - `long endPageNumber`

                  - `long startPageNumber`

                    minimum: 1

                  - `JsonValue type constant`

                - `class BetaCitationContentBlockLocationParam:`

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

                  - `JsonValue type constant`

                - `class BetaCitationWebSearchResultLocationParam:`

                  - `String citedText`

                  - `String encryptedIndex`

                  - `Optional<String> title`

                    maxLength: 512, minLength: 1

                  - `JsonValue type constant`

                  - `String url`

                    minLength: 1

                - `class BetaCitationSearchResultLocationParam:`

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

                  - `JsonValue type constant`

            - `class BetaImageBlockParam:`

              - `Source source`

                - `class BetaBase64ImageSource:`

                  - `String data`

                    format: byte

                  - `MediaType mediaType`

                    - `IMAGE_JPEG("image/jpeg")`

                    - `IMAGE_PNG("image/png")`

                    - `IMAGE_GIF("image/gif")`

                    - `IMAGE_WEBP("image/webp")`

                  - `JsonValue type constant`

                - `class BetaUrlImageSource:`

                  - `JsonValue type constant`

                  - `String url`

                - `class BetaFileImageSource:`

                  - `String fileId`

                  - `JsonValue type constant`

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<BetaImageTransformationsParam> transformations`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `Optional<OversizedImage> oversizedImage`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `DOWNSIZE("downsize")`

                  - `ERROR("error")`

            - `class BetaRequestDocumentBlock:`

              - `Source source`

                - `class BetaBase64PdfSource:`

                  - `String data`

                    format: byte

                  - `JsonValue mediaType constant`

                  - `JsonValue type constant`

                - `class BetaPlainTextSource:`

                  - `String data`

                  - `JsonValue mediaType constant`

                  - `JsonValue type constant`

                - `class BetaContentBlockSource:`

                  - `Content content`

                    - `String`

                    - `List<BetaContentBlockSourceContent>`

                      - `class BetaTextBlockParam:`

                      - `class BetaImageBlockParam:`

                  - `JsonValue type constant`

                - `class BetaUrlPdfSource:`

                  - `JsonValue type constant`

                  - `String url`

                - `class BetaFileDocumentSource:`

                  - `String fileId`

                  - `JsonValue type constant`

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<BetaCitationsConfigParam> citations`

                - `Optional<Boolean> enabled`

              - `Optional<String> context`

                minLength: 1

              - `Optional<String> title`

                maxLength: 500, minLength: 1

            - `class BetaSearchResultBlockParam:`

              - `List<BetaTextBlockParam> content`

                - `String text`

                  minLength: 1

                - `JsonValue type constant`

                - `Optional<BetaCacheControlEphemeral> cacheControl`

                  Create a cache control breakpoint at this content block.

                - `Optional<List<BetaTextCitationParam>> citations`

              - `String source`

              - `String title`

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<BetaCitationsConfigParam> citations`

            - `class BetaThinkingBlockParam:`

              - `String signature`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `String thinking`

                The `thinking` text of this block as returned by the API.

              - `JsonValue type constant`

            - `class BetaRedactedThinkingBlockParam:`

              - `String data`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `JsonValue type constant`

            - `class BetaToolUseBlockParam:`

              - `String id`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Input input`

              - `String name`

                maxLength: 200, minLength: 1

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class BetaDirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonValue type constant`

                - `class BetaServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `String toolId`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonValue type constant`

                - `class BetaServerToolCaller20260120:`

                  - `String toolId`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonValue type constant`

              - `Optional<String> toolsetName`

                For a toolset member tool_use, the toolset family this member belongs to.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `class BetaToolResultBlockParam:`

              - `String toolUseId`

                pattern: ^[a-zA-Z0-9_-]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Content> content`

                - `String`

                - `List<Block>`

                  - `class BetaTextBlockParam:`

                  - `class BetaImageBlockParam:`

                  - `class BetaSearchResultBlockParam:`

                  - `class BetaRequestDocumentBlock:`

                  - `class BetaToolReferenceBlockParam:`

                    Tool reference block that can be included in tool_result content.

                    - `String toolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonValue type constant`

                    - `Optional<BetaCacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                  - `class BetaBrowserStateBlockParam:`

                    The caller's browser state after a browser toolset member call —
                    the full inventory of open tabs, which tab is active, and any side
                    effects (tabs opened, download state changes) the call produced.

                    At most one per `tool_result`, only on a non-error result answering a
                    browser toolset member `tool_use`. The server renders the
                    model-visible text from it; the model never sees the raw fields.

                    - `List<BetaBrowserStateTabEntry> tabs`

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

                    - `JsonValue type constant`

                    - `Optional<BetaCacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                    - `Optional<List<BetaBrowserStateChange>> stateChanges`

                      Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                      maxItems: 200, minItems: 1

                      - `class BetaBrowserStateChangeTabOpened:`

                        A tab this call's execution opened that remains open at its end —
                        the creation delta of the `tabs` inventory, not an event log.

                        Carries only the `tab_id`; the tab's `title` and `url` live on its
                        `tabs` entry, which must include the same `tab_id`. A tab opened
                        during a failed call gets no deferred `tab_opened`; it simply appears
                        in the next result's `tabs` inventory.

                        - `String tabId`

                          The `tab_id` of the opened tab, present in `tabs`.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type constant`

                      - `class BetaBrowserStateChangeDownloadStarted:`

                        A file download that started during this call.

                        - `String downloadId`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type constant`

                        - `String url`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `class BetaBrowserStateChangeDownloadCompleted:`

                        A file download that finished during this call, reported with the
                        same `download_id` as its `download_started` — or without a prior
                        `download_started`, when the download finished during the call that
                        started it (at most one state change per `download_id` per result).

                        - `String downloadId`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type constant`

                        - `String url`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Optional<String> path`

                          Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                        - `Optional<Long> sizeBytes`

                          The completed download's size.

                          minimum: 0

                      - `class BetaBrowserStateChangeDownloadFailed:`

                        A file download that failed — or was cancelled — during this call.

                        - `String downloadId`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonValue type constant`

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

            - `class BetaServerToolUseBlockParam:`

              - `String id`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Input input`

              - `Name name`

                - `ADVISOR("advisor")`

                - `WEB_SEARCH("web_search")`

                - `WEB_FETCH("web_fetch")`

                - `CODE_EXECUTION("code_execution")`

                - `BASH_CODE_EXECUTION("bash_code_execution")`

                - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

                - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

                - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class BetaDirectCaller:`

                  Tool invocation directly from the model.

                - `class BetaServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class BetaServerToolCaller20260120:`

            - `class BetaWebSearchToolResultBlockParam:`

              - `BetaWebSearchToolResultBlockParamContent content`

                - `List<BetaWebSearchResultBlockParam>`

                  - `String encryptedContent`

                  - `String title`

                  - `JsonValue type constant`

                  - `String url`

                  - `Optional<String> pageAge`

                - `class BetaWebSearchToolRequestError:`

                  - `BetaWebSearchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `QUERY_TOO_LONG("query_too_long")`

                    - `REQUEST_TOO_LARGE("request_too_large")`

                  - `JsonValue type constant`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class BetaDirectCaller:`

                  Tool invocation directly from the model.

                - `class BetaServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class BetaServerToolCaller20260120:`

            - `class BetaWebFetchToolResultBlockParam:`

              - `Content content`

                - `class BetaWebFetchToolResultErrorBlockParam:`

                  - `BetaWebFetchToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `URL_TOO_LONG("url_too_long")`

                    - `URL_NOT_ALLOWED("url_not_allowed")`

                    - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                    - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                    - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `UNAVAILABLE("unavailable")`

                  - `JsonValue type constant`

                - `class BetaWebFetchBlockParam:`

                  - `BetaRequestDocumentBlock content`

                  - `JsonValue type constant`

                  - `String url`

                    Fetched content URL

                  - `Optional<String> retrievedAt`

                    ISO 8601 timestamp when the content was retrieved

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Caller> caller`

                Tool invocation directly from the model.

                - `class BetaDirectCaller:`

                  Tool invocation directly from the model.

                - `class BetaServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class BetaServerToolCaller20260120:`

            - `class BetaAdvisorToolResultBlockParam:`

              - `Content content`

                - `class BetaAdvisorToolResultErrorParam:`

                  - `ErrorCode errorCode`

                    - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                    - `PROMPT_TOO_LONG("prompt_too_long")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `OVERLOADED("overloaded")`

                    - `UNAVAILABLE("unavailable")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `MODEL_NOT_FOUND("model_not_found")`

                  - `JsonValue type constant`

                - `class BetaAdvisorResultBlockParam:`

                  - `String text`

                  - `JsonValue type constant`

                  - `Optional<String> stopReason`

                - `class BetaAdvisorRedactedResultBlockParam:`

                  - `String encryptedContent`

                    Opaque blob produced by a prior response; must be round-tripped verbatim.

                  - `JsonValue type constant`

                  - `Optional<String> stopReason`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaCodeExecutionToolResultBlockParam:`

              - `BetaCodeExecutionToolResultBlockParamContent content`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `class BetaCodeExecutionToolResultErrorParam:`

                  - `BetaCodeExecutionToolResultErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `JsonValue type constant`

                - `class BetaCodeExecutionResultBlockParam:`

                  - `List<BetaCodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue type constant`

                  - `long returnCode`

                  - `String stderr`

                  - `String stdout`

                  - `JsonValue type constant`

                - `class BetaEncryptedCodeExecutionResultBlockParam:`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `List<BetaCodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue type constant`

                  - `String encryptedStdout`

                  - `long returnCode`

                  - `String stderr`

                  - `JsonValue type constant`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaBashCodeExecutionToolResultBlockParam:`

              - `Content content`

                - `class BetaBashCodeExecutionToolResultErrorParam:`

                  - `ErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                  - `JsonValue type constant`

                - `class BetaBashCodeExecutionResultBlockParam:`

                  - `List<BetaBashCodeExecutionOutputBlockParam> content`

                    - `String fileId`

                    - `JsonValue type constant`

                  - `long returnCode`

                  - `String stderr`

                  - `String stdout`

                  - `JsonValue type constant`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaTextEditorCodeExecutionToolResultBlockParam:`

              - `Content content`

                - `class BetaTextEditorCodeExecutionToolResultErrorParam:`

                  - `ErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                    - `FILE_NOT_FOUND("file_not_found")`

                  - `JsonValue type constant`

                  - `Optional<String> errorMessage`

                - `class BetaTextEditorCodeExecutionViewResultBlockParam:`

                  - `String content`

                  - `FileType fileType`

                    - `TEXT("text")`

                    - `IMAGE("image")`

                    - `PDF("pdf")`

                  - `JsonValue type constant`

                  - `Optional<Long> numLines`

                  - `Optional<Long> startLine`

                  - `Optional<Long> totalLines`

                - `class BetaTextEditorCodeExecutionCreateResultBlockParam:`

                  - `boolean isFileUpdate`

                  - `JsonValue type constant`

                - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:`

                  - `JsonValue type constant`

                  - `Optional<List<String>> lines`

                  - `Optional<Long> newLines`

                  - `Optional<Long> newStart`

                  - `Optional<Long> oldLines`

                  - `Optional<Long> oldStart`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaToolSearchToolResultBlockParam:`

              - `Content content`

                - `class BetaToolSearchToolResultErrorParam:`

                  - `ErrorCode errorCode`

                    - `INVALID_TOOL_INPUT("invalid_tool_input")`

                    - `UNAVAILABLE("unavailable")`

                    - `TOO_MANY_REQUESTS("too_many_requests")`

                    - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `JsonValue type constant`

                  - `Optional<String> errorMessage`

                - `class BetaToolSearchToolSearchResultBlockParam:`

                  - `List<BetaToolReferenceBlockParam> toolReferences`

                    - `String toolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonValue type constant`

                    - `Optional<BetaCacheControlEphemeral> cacheControl`

                      Create a cache control breakpoint at this content block.

                  - `JsonValue type constant`

              - `String toolUseId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaMcpToolUseBlockParam:`

              - `String id`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Input input`

              - `String name`

              - `String serverName`

                The name of the MCP server

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaRequestMcpToolResultBlockParam:`

              - `String toolUseId`

                pattern: ^[a-zA-Z0-9_-]+$

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<Content> content`

                - `String`

                - `List<BetaTextBlockParam>`

                  - `String text`

                    minLength: 1

                  - `JsonValue type constant`

                  - `Optional<BetaCacheControlEphemeral> cacheControl`

                    Create a cache control breakpoint at this content block.

                  - `Optional<List<BetaTextCitationParam>> citations`

              - `Optional<Boolean> isError`

            - `class BetaContainerUploadBlockParam:`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `String fileId`

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaCompactionBlockParam:`

              A compaction block containing summary of previous context.

              Users should round-trip these blocks from responses to subsequent requests
              to maintain context across compaction boundaries.

              When content is None, the block represents a failed compaction. The server
              treats these as no-ops. Empty string content is not allowed.

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

              - `Optional<String> content`

                Summary of previously compacted content, or null if compaction failed

              - `Optional<String> encryptedContent`

                Opaque metadata from prior compaction, to be round-tripped verbatim

            - `class BetaRequestToolAdditionBlock:`

              Mid-conversation directive to surface a declared tool.

              `tool` references a tool (or MCP toolset) by name from the request's
              `tools`; it is offered to the model from this point in the
              conversation onward.

              - `Tool tool`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

                - `class BetaToolChangeToolReference:`

                  Reference to a single tool the caller declared directly in
                  `tools[]`. Does not accept the composed `{server}_{name}` form the
                  server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                  `mcp_toolset_reference` for those.

                  - `String name`

                    pattern: ^[a-zA-Z0-9_-]{1,128}$

                  - `JsonValue type constant`

                - `class BetaToolChangeMcpToolReference:`

                  Reference to a single MCP tool by its server and remote name — the
                  same `server_name`/`name` pair `mcp_tool_use` carries.

                  - `String name`

                  - `String serverName`

                  - `JsonValue type constant`

                - `class BetaToolChangeMcpToolsetReference:`

                  Reference to every tool in the named MCP server's toolset.

                  - `String serverName`

                  - `JsonValue type constant`

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaRequestToolRemovalBlock:`

              Mid-conversation directive to withdraw a tool.

              `tool` references a tool (or MCP toolset) by name from the request's
              `tools`; it is no longer offered to the model from this point in the
              conversation onward.

              - `Tool tool`

                Reference to a single tool the caller declared directly in
                `tools[]`. Does not accept the composed `{server}_{name}` form the
                server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                `mcp_toolset_reference` for those.

                - `class BetaToolChangeToolReference:`

                  Reference to a single tool the caller declared directly in
                  `tools[]`. Does not accept the composed `{server}_{name}` form the
                  server assigns to MCP-resolved tools — use `mcp_tool_reference` or
                  `mcp_toolset_reference` for those.

                - `class BetaToolChangeMcpToolReference:`

                  Reference to a single MCP tool by its server and remote name — the
                  same `server_name`/`name` pair `mcp_tool_use` carries.

                - `class BetaToolChangeMcpToolsetReference:`

                  Reference to every tool in the named MCP server's toolset.

              - `JsonValue type constant`

              - `Optional<BetaCacheControlEphemeral> cacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaFallbackBlockParam:`

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

              - `BetaFallbackInfoParam from`

                Identifies one hop of a fallback transition.

                - `Model model`

                  The model that will complete your prompt.

                  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

              - `BetaFallbackInfoParam to`

                Identifies one hop of a fallback transition.

              - `JsonValue type constant`

              - `Optional<JsonValue> trigger`

                The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

        - `Role role`

          - `USER("user")`

          - `ASSISTANT("assistant")`

          - `SYSTEM("system")`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `Optional<BetaCacheControlEphemeral> cacheControl`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `Optional<Container> container`

        Container identifier for reuse across requests.

        - `class BetaContainerParams:`

          Container parameters with skills to be loaded.

          - `Optional<String> id`

            Container id

          - `Optional<List<BetaSkillParams>> skills`

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

      - `Optional<BetaContextManagementConfig> contextManagement`

        Context management configuration.

        This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

        - `Optional<List<Edit>> edits`

          List of context management edits to apply

          minItems: 0

          - `class BetaClearToolUses20250919Edit:`

            - `JsonValue type constant`

            - `Optional<BetaInputTokensClearAtLeast> clearAtLeast`

              Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

              - `JsonValue type constant`

              - `long value`

                minimum: 0

            - `Optional<ClearToolInputs> clearToolInputs`

              Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

              - `boolean`

              - `List<String>`

            - `Optional<List<String>> excludeTools`

              Tool names whose uses are preserved from clearing

            - `Optional<BetaToolUsesKeep> keep`

              Number of tool uses to retain in the conversation

              - `JsonValue type constant`

              - `long value`

                minimum: 0

            - `Optional<Trigger> trigger`

              Condition that triggers the context management strategy

              - `class BetaInputTokensTrigger:`

                - `JsonValue type constant`

                - `long value`

                  minimum: 1

              - `class BetaToolUsesTrigger:`

                - `JsonValue type constant`

                - `long value`

                  minimum: 1

          - `class BetaClearThinking20251015Edit:`

            - `JsonValue type constant`

            - `Optional<Keep> keep`

              Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

              - `class BetaThinkingTurns:`

                - `JsonValue type constant`

                - `long value`

                  minimum: 1

              - `class BetaAllThinkingTurns:`

                - `JsonValue type constant`

              - `JsonValue`

          - `class BetaCompact20260112Edit:`

            Automatically compact older context when reaching the configured trigger threshold.

            - `JsonValue type constant`

            - `Optional<String> instructions`

              Additional instructions for summarization.

            - `Optional<Boolean> pauseAfterCompaction`

              Whether to pause after compaction and return the compaction block to the user.

            - `Optional<BetaInputTokensTrigger> trigger`

              When to trigger compaction. Defaults to 150000 input tokens.

      - `Optional<BetaDiagnosticsParam> diagnostics`

        Request-level diagnostics. Currently carries the previous response
        id for prompt-cache divergence reporting.

        - `Optional<String> previousMessageId`

          The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

          maxLength: 256

      - `Optional<FallbackCreditToken> fallbackCreditToken`

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

        - `String`

        - `class BetaFallbackCreditTokenParam:`

          Object form of `fallback_credit_token`: the token plus a redemption
          mode.

          Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
          header the field accepts the bare string only. The bare string and the
          mode-less object are equivalent (both select `strict`), so wrapping
          an existing token changes nothing by itself.

          - `String token`

            The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

            maxLength: 2048, minLength: 1

          - `Optional<Mode> mode`

            How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

            - `STRICT("strict")`

            - `BEST_EFFORT("best_effort")`

      - `Optional<BetaFallbacksParam> fallbacks`

        Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

        - `List<BetaFallbackParam>`

          - `Model model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Optional<Long> maxTokens`

          - `Optional<BetaOutputConfig> outputConfig`

            - `Optional<Effort> effort`

              All possible effort levels.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

              - `MAX("max")`

            - `Optional<BetaJsonOutputFormat> format`

              A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

              - `Schema schema`

                The JSON schema of the format

              - `JsonValue type constant`

            - `Optional<BetaTokenTaskBudget> taskBudget`

              User-configurable total token budget across contexts.

              - `long total`

                Total token budget across all contexts in the session.

                minimum: 1024

              - `JsonValue type constant`

                The budget type. Currently only 'tokens' is supported.

              - `Optional<Long> remaining`

                Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

                minimum: 0

          - `Optional<Speed> speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `STANDARD("standard")`

            - `FAST("fast")`

          - `Optional<Thinking> thinking`

            - `class BetaThinkingConfigEnabled:`

              - `long budgetTokens`

                Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

                Must be ≥1024 and less than `max_tokens`.

                See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

                minimum: 1024

              - `JsonValue type constant`

              - `Optional<Display> display`

                Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

                - `SUMMARIZED("summarized")`

                - `OMITTED("omitted")`

                - `UPDATES("updates")`

            - `class BetaThinkingConfigDisabled:`

              - `JsonValue type constant`

            - `class BetaThinkingConfigAdaptive:`

              - `JsonValue type constant`

              - `Optional<Display> display`

                Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

                - `SUMMARIZED("summarized")`

                - `OMITTED("omitted")`

                - `UPDATES("updates")`

        - `JsonValue`

      - `Optional<String> inferenceGeo`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Optional<List<BetaRequestMcpServerUrlDefinition>> mcpServers`

        MCP servers to be utilized in this request

        maxItems: 20

        - `String name`

        - `JsonValue type constant`

        - `String url`

        - `Optional<String> authorizationToken`

        - `Optional<BetaRequestMcpServerToolConfiguration> toolConfiguration`

          - `Optional<List<String>> allowedTools`

          - `Optional<Boolean> enabled`

      - `Optional<BetaMetadata> metadata`

        An object describing metadata about the request.

        - `Optional<String> userId`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

          maxLength: 512

      - `Optional<BetaOutputConfig> outputConfig`

        Configuration options for the model's output, such as the output format.

      - `Optional<ServiceTier> serviceTier`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `AUTO("auto")`

        - `STANDARD_ONLY("standard_only")`

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

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

        - `List<BetaTextBlockParam>`

          - `String text`

            minLength: 1

          - `JsonValue type constant`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<List<BetaTextCitationParam>> citations`

      - `Optional<BetaThinkingConfigParam> thinking`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `class BetaThinkingConfigEnabled:`

        - `class BetaThinkingConfigDisabled:`

        - `class BetaThinkingConfigAdaptive:`

      - `Optional<BetaToolChoice> toolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `class BetaToolChoiceAuto:`

          The model will automatically decide whether to use tools.

          - `JsonValue type constant`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `class BetaToolChoiceAny:`

          The model will use any available tools.

          - `JsonValue type constant`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class BetaToolChoiceTool:`

          The model will use the specified tool with `tool_choice.name`.

          - `String name`

            The name of the tool to use.

          - `JsonValue type constant`

          - `Optional<Boolean> disableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class BetaToolChoiceNone:`

          The model will not be allowed to use tools.

          - `JsonValue type constant`

      - `Optional<List<BetaToolUnion>> tools`

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

        - `class BetaTool:`

          - `InputSchema inputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `JsonValue type constant`

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

          - `Optional<BetaCacheControlEphemeral> cacheControl`

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

        - `class BetaToolBash20241022:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolBash20250124:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20250522:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20250825:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20260120:`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20260521:`

          Code execution tool with REPL state persistence.

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaBrowserToolset20260801:`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaBrowserToolsetConfigs> configs`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `Optional<BetaBrowserCloseTabConfig> closeTab`

              `close_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserDoubleClickConfig> doubleClick`

              `double_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserFileUploadConfig> fileUpload`

              `file_upload`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserFindConfig> find`

              `find`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserFormInputConfig> formInput`

              `form_input`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserGetPageTextConfig> getPageText`

              `get_page_text`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserHoldKeyConfig> holdKey`

              `hold_key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserHoverConfig> hover`

              `hover`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserJavascriptExecConfig> javascriptExec`

              `javascript_exec`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserKeyConfig> key`

              `key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserLeftClickConfig> leftClick`

              `left_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserLeftClickDragConfig> leftClickDrag`

              `left_click_drag`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserLeftMouseDownConfig> leftMouseDown`

              `left_mouse_down`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserLeftMouseUpConfig> leftMouseUp`

              `left_mouse_up`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserListTabsConfig> listTabs`

              `list_tabs`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserMiddleClickConfig> middleClick`

              `middle_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserMouseMoveConfig> mouseMove`

              `mouse_move`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserNavigateConfig> navigate`

              `navigate`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserNewTabConfig> newTab`

              `new_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserReadConsoleConfig> readConsole`

              `read_console`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserReadNetworkConfig> readNetwork`

              `read_network`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserReadPageConfig> readPage`

              `read_page`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserRightClickConfig> rightClick`

              `right_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserScreenshotConfig> screenshot`

              `screenshot`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserScrollConfig> scroll`

              `scroll`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserScrollToConfig> scrollTo`

              `scroll_to`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserSwitchTabConfig> switchTab`

              `switch_tab`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserTripleClickConfig> tripleClick`

              `triple_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserTypeConfig> type`

              `type`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserWaitConfig> wait`

              `wait`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaBrowserZoomConfig> zoom`

              `zoom`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class BetaToolComputerUse20241022:`

          - `long displayHeightPx`

            The height of the display in pixels.

            minimum: 1

          - `long displayWidthPx`

            The width of the display in pixels.

            minimum: 1

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> displayNumber`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaMemoryTool20250818:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolComputerUse20250124:`

          - `long displayHeightPx`

            The height of the display in pixels.

            minimum: 1

          - `long displayWidthPx`

            The width of the display in pixels.

            minimum: 1

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> displayNumber`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20241022:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolComputerUse20251124:`

          - `long displayHeightPx`

            The height of the display in pixels.

            minimum: 1

          - `long displayWidthPx`

            The width of the display in pixels.

            minimum: 1

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> displayNumber`

            The X11 display number (e.g. 0, 1) for the display.

            minimum: 0

          - `Optional<Boolean> enableZoom`

            Whether to enable an action to take a zoomed-in screenshot of the screen.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaComputerToolset20260801:`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaComputerToolsetConfigs> configs`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `Optional<BetaComputerCursorPositionConfig> cursorPosition`

              `cursor_position`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerDoubleClickConfig> doubleClick`

              `double_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerHoldKeyConfig> holdKey`

              `hold_key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerKeyConfig> key`

              `key`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerLeftClickConfig> leftClick`

              `left_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerLeftClickDragConfig> leftClickDrag`

              `left_click_drag`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerLeftMouseDownConfig> leftMouseDown`

              `left_mouse_down`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerLeftMouseUpConfig> leftMouseUp`

              `left_mouse_up`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerMiddleClickConfig> middleClick`

              `middle_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerMouseMoveConfig> mouseMove`

              `mouse_move`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerRightClickConfig> rightClick`

              `right_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerScreenshotConfig> screenshot`

              `screenshot`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerScrollConfig> scroll`

              `scroll`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerTripleClickConfig> tripleClick`

              `triple_click`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerTypeConfig> type`

              `type`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerWaitConfig> wait`

              `wait`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Optional<BetaComputerZoomConfig> zoom`

              `zoom`'s config overrides.

              - `Optional<Boolean> deferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Optional<Boolean> enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class BetaToolTextEditor20250124:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20250429:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20250728:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<List<InputExample>> inputExamples`

          - `Optional<Long> maxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaWebSearchTool20250305:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<BetaUserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

            - `JsonValue type constant`

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

        - `class BetaWebFetchTool20250910:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaCitationsConfigParam> citations`

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

        - `class BetaWebSearchTool20260209:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

          - `Optional<BetaUserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class BetaWebFetchTool20260209:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaCitationsConfigParam> citations`

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

        - `class BetaWebFetchTool20260309:`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaCitationsConfigParam> citations`

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

        - `class BetaWebSearchTool20260318:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `Optional<List<String>> blockedDomains`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `Optional<BetaCacheControlEphemeral> cacheControl`

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

          - `Optional<BetaUserLocation> userLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class BetaWebFetchTool20260318:`

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<List<String>> allowedDomains`

            List of domains to allow fetching from

          - `Optional<List<String>> blockedDomains`

            List of domains to block fetching from

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaCitationsConfigParam> citations`

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

        - `class BetaAdvisorTool20260301:`

          - `Model model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `JsonValue name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonValue type constant`

          - `Optional<List<AllowedCaller>> allowedCallers`

            - `DIRECT("direct")`

            - `CODE_EXECUTION_20250825("code_execution_20250825")`

            - `CODE_EXECUTION_20260120("code_execution_20260120")`

            - `CODE_EXECUTION_20260521("code_execution_20260521")`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<BetaCacheControlEphemeral> caching`

            Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Long> maxTokens`

            Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

            minimum: 1024

          - `Optional<Long> maxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolSearchToolBm25_20251119:`

          - `JsonValue name constant`

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

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolSearchToolRegex20251119:`

          - `JsonValue name constant`

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

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Boolean> deferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Optional<Boolean> strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaMcpToolset:`

          Configuration for a group of tools from an MCP server.

          Allows configuring enabled status and defer_loading for all tools
          from an MCP server, with optional per-tool overrides.

          - `String mcpServerName`

            Name of the MCP server to configure tools for

            maxLength: 255, minLength: 1

          - `JsonValue type constant`

          - `Optional<BetaCacheControlEphemeral> cacheControl`

            Create a cache control breakpoint at this content block.

          - `Optional<Configs> configs`

            Configuration overrides for specific tools, keyed by tool name

            - `Optional<Boolean> deferLoading`

            - `Optional<Boolean> enabled`

          - `Optional<BetaMcpToolDefaultConfig> defaultConfig`

            Default configuration applied to all tools from this server

            - `Optional<Boolean> deferLoading`

            - `Optional<Boolean> enabled`

      - `Optional<BetaJsonOutputFormat> outputFormat`

        **Deprecated**

        Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

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

- `class BetaMessageBatch:`

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

  - `BetaMessageBatchRequestCounts requestCounts`

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

  - `JsonValue type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchCreateParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatch;
import com.anthropic.models.messages.Model;

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
        BetaMessageBatch betaMessageBatch = client.beta().messages().batches().create(params);
    }
}
```

#### Response (200)

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

## Retrieve a Message Batch

`BetaMessageBatch beta().messages().batches().retrieve(params = BatchRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `BatchRetrieveParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

### Returns

- `class BetaMessageBatch:`

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

  - `BetaMessageBatchRequestCounts requestCounts`

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

  - `JsonValue type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchRetrieveParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaMessageBatch betaMessageBatch = client.beta().messages().batches().retrieve("message_batch_id");
    }
}
```

#### Response (200)

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

## List Message Batches

`BatchListPage beta().messages().batches().list(params = BatchListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `BatchListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

### Returns

- `class BetaMessageBatch:`

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

  - `BetaMessageBatchRequestCounts requestCounts`

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

  - `JsonValue type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchListPage;
import com.anthropic.models.beta.messages.batches.BatchListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BatchListPage page = client.beta().messages().batches().list();
    }
}
```

#### Response (200)

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

## Cancel a Message Batch

`BetaMessageBatch beta().messages().batches().cancel(params = BatchCancelParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `BatchCancelParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

### Returns

- `class BetaMessageBatch:`

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

  - `BetaMessageBatchRequestCounts requestCounts`

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

  - `JsonValue type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchCancelParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaMessageBatch betaMessageBatch = client.beta().messages().batches().cancel("message_batch_id");
    }
}
```

#### Response (200)

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

## Delete a Message Batch

`BetaDeletedMessageBatch beta().messages().batches().delete(params = BatchDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `BatchDeleteParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

### Returns

- `class BetaDeletedMessageBatch:`

  - `String id`

    ID of the Message Batch.

  - `JsonValue type constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.messages.batches.BatchDeleteParams;
import com.anthropic.models.beta.messages.batches.BetaDeletedMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDeletedMessageBatch betaDeletedMessageBatch = client.beta().messages().batches().delete("message_batch_id");
    }
}
```

#### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Retrieve Message Batch results

`BetaMessageBatchIndividualResponse beta().messages().batches().resultsStreaming(params = BatchResultsParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `BatchResultsParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

### Returns

- `class BetaMessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `BetaMessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class BetaMessageBatchSucceededResult:`

      - `BetaMessage message`

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<BetaContainer> container`

          Information about the container used in the request (for the code execution tool)

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

            format: date-time

          - `Optional<List<BetaSkill>> skills`

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

        - `List<BetaContentBlock> content`

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

          - `class BetaTextBlock:`

            - `Optional<List<BetaTextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class BetaCitationCharLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                  minimum: 0

                - `JsonValue type constant`

              - `class BetaCitationPageLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                  minimum: 1

                - `JsonValue type constant`

              - `class BetaCitationContentBlockLocation:`

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

                - `JsonValue type constant`

              - `class BetaCitationsWebSearchResultLocation:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512

                - `JsonValue type constant`

                - `String url`

              - `class BetaCitationSearchResultLocation:`

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

                - `JsonValue type constant`

            - `String text`

              maxLength: 5000000, minLength: 0

            - `JsonValue type constant`

          - `class BetaThinkingBlock:`

            - `String signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `String thinking`

              The text of Claude's thinking process for this block.

            - `JsonValue type constant`

          - `class BetaRedactedThinkingBlock:`

            - `String data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `JsonValue type constant`

          - `class BetaToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              minLength: 1

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue type constant`

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type constant`

              - `class BetaServerToolCaller20260120:`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type constant`

            - `Optional<String> toolsetName`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaServerToolUseBlock:`

            - `String id`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Input input`

            - `Name name`

              - `ADVISOR("advisor")`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebSearchToolResultBlock:`

            - `BetaWebSearchToolResultBlockContent content`

              - `class BetaWebSearchToolResultError:`

                - `BetaWebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

                - `JsonValue type constant`

              - `List<BetaWebSearchResultBlock>`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `JsonValue type constant`

                - `String url`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebFetchToolResultBlock:`

            - `Content content`

              - `class BetaWebFetchToolResultErrorBlock:`

                - `BetaWebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                - `JsonValue type constant`

              - `class BetaWebFetchBlock:`

                - `BetaDocumentBlock content`

                  - `Optional<BetaCitationConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class BetaBase64PdfSource:`

                      - `String data`

                        format: byte

                      - `JsonValue mediaType constant`

                      - `JsonValue type constant`

                    - `class BetaPlainTextSource:`

                      - `String data`

                      - `JsonValue mediaType constant`

                      - `JsonValue type constant`

                  - `Optional<String> title`

                    The title of the document

                  - `JsonValue type constant`

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonValue type constant`

                - `String url`

                  Fetched content URL

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaAdvisorToolResultBlock:`

            - `Content content`

              - `class BetaAdvisorToolResultError:`

                - `ErrorCode errorCode`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `PROMPT_TOO_LONG("prompt_too_long")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `OVERLOADED("overloaded")`

                  - `UNAVAILABLE("unavailable")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `MODEL_NOT_FOUND("model_not_found")`

                - `JsonValue type constant`

              - `class BetaAdvisorResultBlock:`

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `String text`

                - `JsonValue type constant`

              - `class BetaAdvisorRedactedResultBlock:`

                - `String encryptedContent`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaCodeExecutionToolResultBlock:`

            - `BetaCodeExecutionToolResultBlockContent content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class BetaCodeExecutionToolResultError:`

                - `BetaCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `JsonValue type constant`

              - `class BetaCodeExecutionResultBlock:`

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type constant`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type constant`

              - `class BetaEncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type constant`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaBashCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BetaBashCodeExecutionToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                - `JsonValue type constant`

              - `class BetaBashCodeExecutionResultBlock:`

                - `List<BetaBashCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type constant`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaTextEditorCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BetaTextEditorCodeExecutionToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

                - `JsonValue type constant`

              - `class BetaTextEditorCodeExecutionViewResultBlock:`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

                - `JsonValue type constant`

              - `class BetaTextEditorCodeExecutionCreateResultBlock:`

                - `boolean isFileUpdate`

                - `JsonValue type constant`

              - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaToolSearchToolResultBlock:`

            - `Content content`

              - `class BetaToolSearchToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

                - `JsonValue type constant`

              - `class BetaToolSearchToolSearchResultBlock:`

                - `List<BetaToolReferenceBlock> toolReferences`

                  - `String toolName`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `JsonValue type constant`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaMcpToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              The name of the MCP tool

            - `String serverName`

              The name of the MCP server

            - `JsonValue type constant`

          - `class BetaMcpToolResultBlock:`

            - `Content content`

              - `String`

              - `List<BetaTextBlock>`

                - `Optional<List<BetaTextCitation>> citations`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `String text`

                  maxLength: 5000000, minLength: 0

                - `JsonValue type constant`

            - `boolean isError`

            - `String toolUseId`

              pattern: ^[a-zA-Z0-9_-]+$

            - `JsonValue type constant`

          - `class BetaContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `String fileId`

            - `JsonValue type constant`

          - `class BetaCompactionBlock:`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `Optional<String> content`

              Summary of compacted content, or null if compaction failed

            - `Optional<String> encryptedContent`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `JsonValue type constant`

          - `class BetaFallbackBlock:`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `BetaFallbackInfo from`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

            - `BetaFallbackInfo to`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `BetaFallbackRefusalTrigger trigger`

              What caused the `from` model to hand over at this hop.

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

              - `JsonValue type constant`

            - `JsonValue type constant`

        - `Optional<BetaContextManagementResponse> contextManagement`

          Context management response.

          Information about context management strategies applied during the request.

          - `List<AppliedEdit> appliedEdits`

            List of context management edits that were applied.

            - `class BetaClearToolUses20250919EditResponse:`

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedToolUses`

                Number of tool uses that were cleared.

                minimum: 0

              - `JsonValue type constant`

                The type of context management edit applied.

            - `class BetaClearThinking20251015EditResponse:`

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedThinkingTurns`

                Number of thinking turns that were cleared.

                minimum: 0

              - `JsonValue type constant`

                The type of context management edit applied.

        - `Optional<BetaDiagnostics> diagnostics`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `Optional<CacheMissReason> cacheMissReason`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `class BetaCacheMissModelChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissSystemChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissToolsChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissMessagesChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissPreviousMessageNotFound:`

              - `JsonValue type constant`

            - `class BetaCacheMissUnavailable:`

              - `JsonValue type constant`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `JsonValue role constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `Optional<BetaRefusalStopDetails> stopDetails`

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

          - `Optional<String> fallbackCreditToken`

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

          - `Optional<Boolean> fallbackHasPrefillClaim`

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

          - `Optional<String> recommendedModel`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `JsonValue type constant`

        - `Optional<BetaStopReason> stopReason`

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

          - `COMPACTION("compaction")`

          - `REFUSAL("refusal")`

          - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonValue type constant`

          Object type.

          For Messages, this is always `"message"`.

        - `BetaUsage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<BetaCacheCreation> cacheCreation`

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

          - `Optional<BetaFallbackCreditUsage> fallbackCredit`

            Outcome of the `fallback_credit_token` presented on this request.

            - `Status status`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `class BetaFallbackCreditRedeemed:`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `JsonValue type constant`

              - `class BetaFallbackCreditNotApplied:`

                No reprice was applied; `reason` says why.

                - `Reason reason`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `BODY_MISMATCH("body_mismatch")`

                  - `CONTINUATION_EXCLUDED("continuation_excluded")`

                  - `CONTINUATION_ONLY("continuation_only")`

                  - `EXPIRED("expired")`

                  - `INVALID_TARGET_MODEL("invalid_target_model")`

                  - `NOT_ENABLED("not_enabled")`

                  - `REPRICE_UNAVAILABLE("reprice_unavailable")`

                  - `TEMPORARILY_UNAVAILABLE("temporarily_unavailable")`

                  - `VARIANT_FIELDS_PRESENT("variant_fields_present")`

                  - `WRONG_ORGANIZATION("wrong_organization")`

                  - `WRONG_PLATFORM("wrong_platform")`

                  - `WRONG_WORKSPACE("wrong_workspace")`

                - `JsonValue type constant`

                - `Optional<List<String>> removeToRedeem`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `Optional<List<BetaIterationsUsageItems>> iterations`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `class BetaMessageIterationUsage:`

              Token usage for a sampling iteration.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for a sampling iteration

            - `class BetaCompactionIterationUsage:`

              Token usage for a compaction iteration.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for a compaction iteration

            - `class BetaAdvisorMessageIterationUsage:`

              Token usage for an advisor sub-inference iteration.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for an advisor sub-inference iteration

            - `class BetaFallbackMessageIterationUsage:`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for the fallback-model attempt that served the response

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `Optional<BetaOutputTokensDetails> outputTokensDetails`

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

          - `Optional<BetaServerToolUsage> serverToolUse`

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

          - `Optional<Speed> speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `STANDARD("standard")`

            - `FAST("fast")`

      - `JsonValue type constant`

    - `class BetaMessageBatchErroredResult:`

      - `BetaErrorResponse error`

        - `BetaError error`

          - `class BetaInvalidRequestError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaAuthenticationError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaBillingError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaPermissionError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaNotFoundError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaRateLimitError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaGatewayTimeoutError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaApiError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaOverloadedError:`

            - `String message`

            - `JsonValue type constant`

        - `Optional<String> requestId`

        - `JsonValue type constant`

      - `JsonValue type constant`

    - `class BetaMessageBatchCanceledResult:`

      - `JsonValue type constant`

    - `class BetaMessageBatchExpiredResult:`

      - `JsonValue type constant`

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.messages.batches.BatchResultsParams;
import com.anthropic.models.beta.messages.batches.BetaMessageBatchIndividualResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<BetaMessageBatchIndividualResponse> betaMessageBatchIndividualResponse = client.beta().messages().batches().resultsStreaming("message_batch_id");
    }
}
```

## Domain types

### Beta Deleted Message Batch

- `class BetaDeletedMessageBatch:`

  - `String id`

    ID of the Message Batch.

  - `JsonValue type constant`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

### Beta Message Batch

- `class BetaMessageBatch:`

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

  - `BetaMessageBatchRequestCounts requestCounts`

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

  - `JsonValue type constant`

    Object type.

    For Message Batches, this is always `"message_batch"`.

### Beta Message Batch Canceled Result

- `class BetaMessageBatchCanceledResult:`

  - `JsonValue type constant`

### Beta Message Batch Errored Result

- `class BetaMessageBatchErroredResult:`

  - `BetaErrorResponse error`

    - `BetaError error`

      - `class BetaInvalidRequestError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaAuthenticationError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaBillingError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaPermissionError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaNotFoundError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaRateLimitError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaGatewayTimeoutError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaApiError:`

        - `String message`

        - `JsonValue type constant`

      - `class BetaOverloadedError:`

        - `String message`

        - `JsonValue type constant`

    - `Optional<String> requestId`

    - `JsonValue type constant`

  - `JsonValue type constant`

### Beta Message Batch Expired Result

- `class BetaMessageBatchExpiredResult:`

  - `JsonValue type constant`

### Beta Message Batch Individual Response

- `class BetaMessageBatchIndividualResponse:`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `String customId`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `BetaMessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `class BetaMessageBatchSucceededResult:`

      - `BetaMessage message`

        - `String id`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `Optional<BetaContainer> container`

          Information about the container used in the request (for the code execution tool)

          - `String id`

            Identifier for the container used in this request

          - `LocalDateTime expiresAt`

            The time at which the container will expire.

            format: date-time

          - `Optional<List<BetaSkill>> skills`

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

        - `List<BetaContentBlock> content`

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

          - `class BetaTextBlock:`

            - `Optional<List<BetaTextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `class BetaCitationCharLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endCharIndex`

                - `Optional<String> fileId`

                - `long startCharIndex`

                  minimum: 0

                - `JsonValue type constant`

              - `class BetaCitationPageLocation:`

                - `String citedText`

                - `long documentIndex`

                  minimum: 0

                - `Optional<String> documentTitle`

                - `long endPageNumber`

                - `Optional<String> fileId`

                - `long startPageNumber`

                  minimum: 1

                - `JsonValue type constant`

              - `class BetaCitationContentBlockLocation:`

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

                - `JsonValue type constant`

              - `class BetaCitationsWebSearchResultLocation:`

                - `String citedText`

                - `String encryptedIndex`

                - `Optional<String> title`

                  maxLength: 512

                - `JsonValue type constant`

                - `String url`

              - `class BetaCitationSearchResultLocation:`

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

                - `JsonValue type constant`

            - `String text`

              maxLength: 5000000, minLength: 0

            - `JsonValue type constant`

          - `class BetaThinkingBlock:`

            - `String signature`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `String thinking`

              The text of Claude's thinking process for this block.

            - `JsonValue type constant`

          - `class BetaRedactedThinkingBlock:`

            - `String data`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

            - `JsonValue type constant`

          - `class BetaToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              minLength: 1

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

                - `JsonValue type constant`

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type constant`

              - `class BetaServerToolCaller20260120:`

                - `String toolId`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                - `JsonValue type constant`

            - `Optional<String> toolsetName`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `class BetaServerToolUseBlock:`

            - `String id`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `Input input`

            - `Name name`

              - `ADVISOR("advisor")`

              - `WEB_SEARCH("web_search")`

              - `WEB_FETCH("web_fetch")`

              - `CODE_EXECUTION("code_execution")`

              - `BASH_CODE_EXECUTION("bash_code_execution")`

              - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

              - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

              - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebSearchToolResultBlock:`

            - `BetaWebSearchToolResultBlockContent content`

              - `class BetaWebSearchToolResultError:`

                - `BetaWebSearchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `QUERY_TOO_LONG("query_too_long")`

                  - `REQUEST_TOO_LARGE("request_too_large")`

                - `JsonValue type constant`

              - `List<BetaWebSearchResultBlock>`

                - `String encryptedContent`

                - `Optional<String> pageAge`

                - `String title`

                - `JsonValue type constant`

                - `String url`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaWebFetchToolResultBlock:`

            - `Content content`

              - `class BetaWebFetchToolResultErrorBlock:`

                - `BetaWebFetchToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `URL_TOO_LONG("url_too_long")`

                  - `URL_NOT_ALLOWED("url_not_allowed")`

                  - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                  - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                  - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `UNAVAILABLE("unavailable")`

                - `JsonValue type constant`

              - `class BetaWebFetchBlock:`

                - `BetaDocumentBlock content`

                  - `Optional<BetaCitationConfig> citations`

                    Citation configuration for the document

                    - `boolean enabled`

                  - `Source source`

                    - `class BetaBase64PdfSource:`

                      - `String data`

                        format: byte

                      - `JsonValue mediaType constant`

                      - `JsonValue type constant`

                    - `class BetaPlainTextSource:`

                      - `String data`

                      - `JsonValue mediaType constant`

                      - `JsonValue type constant`

                  - `Optional<String> title`

                    The title of the document

                  - `JsonValue type constant`

                - `Optional<String> retrievedAt`

                  ISO 8601 timestamp when the content was retrieved

                - `JsonValue type constant`

                - `String url`

                  Fetched content URL

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

            - `Optional<Caller> caller`

              Tool invocation directly from the model.

              - `class BetaDirectCaller:`

                Tool invocation directly from the model.

              - `class BetaServerToolCaller:`

                Tool invocation generated by a server-side tool.

              - `class BetaServerToolCaller20260120:`

          - `class BetaAdvisorToolResultBlock:`

            - `Content content`

              - `class BetaAdvisorToolResultError:`

                - `ErrorCode errorCode`

                  - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                  - `PROMPT_TOO_LONG("prompt_too_long")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `OVERLOADED("overloaded")`

                  - `UNAVAILABLE("unavailable")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `MODEL_NOT_FOUND("model_not_found")`

                - `JsonValue type constant`

              - `class BetaAdvisorResultBlock:`

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

                - `String text`

                - `JsonValue type constant`

              - `class BetaAdvisorRedactedResultBlock:`

                - `String encryptedContent`

                  Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

                - `Optional<String> stopReason`

                  The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaCodeExecutionToolResultBlock:`

            - `BetaCodeExecutionToolResultBlockContent content`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `class BetaCodeExecutionToolResultError:`

                - `BetaCodeExecutionToolResultErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `JsonValue type constant`

              - `class BetaCodeExecutionResultBlock:`

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type constant`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type constant`

              - `class BetaEncryptedCodeExecutionResultBlock:`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `List<BetaCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type constant`

                - `String encryptedStdout`

                - `long returnCode`

                - `String stderr`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaBashCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BetaBashCodeExecutionToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

                - `JsonValue type constant`

              - `class BetaBashCodeExecutionResultBlock:`

                - `List<BetaBashCodeExecutionOutputBlock> content`

                  - `String fileId`

                  - `JsonValue type constant`

                - `long returnCode`

                - `String stderr`

                - `String stdout`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaTextEditorCodeExecutionToolResultBlock:`

            - `Content content`

              - `class BetaTextEditorCodeExecutionToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                  - `FILE_NOT_FOUND("file_not_found")`

                - `Optional<String> errorMessage`

                - `JsonValue type constant`

              - `class BetaTextEditorCodeExecutionViewResultBlock:`

                - `String content`

                - `FileType fileType`

                  - `TEXT("text")`

                  - `IMAGE("image")`

                  - `PDF("pdf")`

                - `Optional<Long> numLines`

                - `Optional<Long> startLine`

                - `Optional<Long> totalLines`

                - `JsonValue type constant`

              - `class BetaTextEditorCodeExecutionCreateResultBlock:`

                - `boolean isFileUpdate`

                - `JsonValue type constant`

              - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

                - `Optional<List<String>> lines`

                - `Optional<Long> newLines`

                - `Optional<Long> newStart`

                - `Optional<Long> oldLines`

                - `Optional<Long> oldStart`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaToolSearchToolResultBlock:`

            - `Content content`

              - `class BetaToolSearchToolResultError:`

                - `ErrorCode errorCode`

                  - `INVALID_TOOL_INPUT("invalid_tool_input")`

                  - `UNAVAILABLE("unavailable")`

                  - `TOO_MANY_REQUESTS("too_many_requests")`

                  - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `Optional<String> errorMessage`

                - `JsonValue type constant`

              - `class BetaToolSearchToolSearchResultBlock:`

                - `List<BetaToolReferenceBlock> toolReferences`

                  - `String toolName`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                  - `JsonValue type constant`

                - `JsonValue type constant`

            - `String toolUseId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaMcpToolUseBlock:`

            - `String id`

              pattern: ^[a-zA-Z0-9_-]+$

            - `Input input`

            - `String name`

              The name of the MCP tool

            - `String serverName`

              The name of the MCP server

            - `JsonValue type constant`

          - `class BetaMcpToolResultBlock:`

            - `Content content`

              - `String`

              - `List<BetaTextBlock>`

                - `Optional<List<BetaTextCitation>> citations`

                  Citations supporting the text block.

                  The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

                - `String text`

                  maxLength: 5000000, minLength: 0

                - `JsonValue type constant`

            - `boolean isError`

            - `String toolUseId`

              pattern: ^[a-zA-Z0-9_-]+$

            - `JsonValue type constant`

          - `class BetaContainerUploadBlock:`

            Response model for a file uploaded to the container.

            - `String fileId`

            - `JsonValue type constant`

          - `class BetaCompactionBlock:`

            A compaction block returned when autocompact is triggered.

            When content is None, it indicates the compaction failed to produce a valid
            summary (e.g., malformed output from the model). Clients may round-trip
            compaction blocks with null content; the server treats them as no-ops.

            - `Optional<String> content`

              Summary of compacted content, or null if compaction failed

            - `Optional<String> encryptedContent`

              Opaque metadata from prior compaction, to be round-tripped verbatim

            - `JsonValue type constant`

          - `class BetaFallbackBlock:`

            Marks the point in `content` where one model's output gives way to the next.

            One block appears per hop where a preceding model actually ran this turn and
            declined. A turn where no preceding model ran and declined has no such
            boundary and carries no block — the signal for whether a fallback model
            served the response is the presence of a `fallback_message` entry in
            `usage.iterations`, not this block.

            The block is treated like a server-tool content block for streaming: it
            arrives via the standard `content_block_start` / `content_block_stop`
            pair and carries no deltas.

            - `BetaFallbackInfo from`

              The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

            - `BetaFallbackInfo to`

              The fallback model producing the content that follows this block. Its `model` is always the canonical id.

            - `BetaFallbackRefusalTrigger trigger`

              What caused the `from` model to hand over at this hop.

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

              - `JsonValue type constant`

            - `JsonValue type constant`

        - `Optional<BetaContextManagementResponse> contextManagement`

          Context management response.

          Information about context management strategies applied during the request.

          - `List<AppliedEdit> appliedEdits`

            List of context management edits that were applied.

            - `class BetaClearToolUses20250919EditResponse:`

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedToolUses`

                Number of tool uses that were cleared.

                minimum: 0

              - `JsonValue type constant`

                The type of context management edit applied.

            - `class BetaClearThinking20251015EditResponse:`

              - `long clearedInputTokens`

                Number of input tokens cleared by this edit.

                minimum: 0

              - `long clearedThinkingTurns`

                Number of thinking turns that were cleared.

                minimum: 0

              - `JsonValue type constant`

                The type of context management edit applied.

        - `Optional<BetaDiagnostics> diagnostics`

          Response envelope for request-level diagnostics. Present (possibly
          null) whenever the caller supplied `diagnostics` on the request.

          - `Optional<CacheMissReason> cacheMissReason`

            Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

            - `class BetaCacheMissModelChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissSystemChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissToolsChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissMessagesChanged:`

              - `long cacheMissedInputTokens`

                Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

              - `JsonValue type constant`

            - `class BetaCacheMissPreviousMessageNotFound:`

              - `JsonValue type constant`

            - `class BetaCacheMissUnavailable:`

              - `JsonValue type constant`

        - `Model model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `JsonValue role constant`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `Optional<BetaRefusalStopDetails> stopDetails`

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

          - `Optional<String> fallbackCreditToken`

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

          - `Optional<Boolean> fallbackHasPrefillClaim`

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

          - `Optional<String> recommendedModel`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `JsonValue type constant`

        - `Optional<BetaStopReason> stopReason`

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

          - `COMPACTION("compaction")`

          - `REFUSAL("refusal")`

          - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

        - `Optional<String> stopSequence`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `JsonValue type constant`

          Object type.

          For Messages, this is always `"message"`.

        - `BetaUsage usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `Optional<BetaCacheCreation> cacheCreation`

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

          - `Optional<BetaFallbackCreditUsage> fallbackCredit`

            Outcome of the `fallback_credit_token` presented on this request.

            - `Status status`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `class BetaFallbackCreditRedeemed:`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `JsonValue type constant`

              - `class BetaFallbackCreditNotApplied:`

                No reprice was applied; `reason` says why.

                - `Reason reason`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `BODY_MISMATCH("body_mismatch")`

                  - `CONTINUATION_EXCLUDED("continuation_excluded")`

                  - `CONTINUATION_ONLY("continuation_only")`

                  - `EXPIRED("expired")`

                  - `INVALID_TARGET_MODEL("invalid_target_model")`

                  - `NOT_ENABLED("not_enabled")`

                  - `REPRICE_UNAVAILABLE("reprice_unavailable")`

                  - `TEMPORARILY_UNAVAILABLE("temporarily_unavailable")`

                  - `VARIANT_FIELDS_PRESENT("variant_fields_present")`

                  - `WRONG_ORGANIZATION("wrong_organization")`

                  - `WRONG_PLATFORM("wrong_platform")`

                  - `WRONG_WORKSPACE("wrong_workspace")`

                - `JsonValue type constant`

                - `Optional<List<String>> removeToRedeem`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `Optional<String> inferenceGeo`

            The geographic region where inference was performed for this request.

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `Optional<List<BetaIterationsUsageItems>> iterations`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `class BetaMessageIterationUsage:`

              Token usage for a sampling iteration.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for a sampling iteration

            - `class BetaCompactionIterationUsage:`

              Token usage for a compaction iteration.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for a compaction iteration

            - `class BetaAdvisorMessageIterationUsage:`

              Token usage for an advisor sub-inference iteration.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for an advisor sub-inference iteration

            - `class BetaFallbackMessageIterationUsage:`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `Optional<BetaCacheCreation> cacheCreation`

                Breakdown of cached tokens by TTL

              - `long cacheCreationInputTokens`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `long cacheReadInputTokens`

                The number of input tokens read from the cache.

                minimum: 0

              - `long inputTokens`

                The number of input tokens which were used.

                minimum: 0

              - `Model model`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `long outputTokens`

                The number of output tokens which were used.

                minimum: 0

              - `JsonValue type constant`

                Usage for the fallback-model attempt that served the response

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `Optional<BetaOutputTokensDetails> outputTokensDetails`

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

          - `Optional<BetaServerToolUsage> serverToolUse`

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

          - `Optional<Speed> speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `STANDARD("standard")`

            - `FAST("fast")`

      - `JsonValue type constant`

    - `class BetaMessageBatchErroredResult:`

      - `BetaErrorResponse error`

        - `BetaError error`

          - `class BetaInvalidRequestError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaAuthenticationError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaBillingError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaPermissionError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaNotFoundError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaRateLimitError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaGatewayTimeoutError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaApiError:`

            - `String message`

            - `JsonValue type constant`

          - `class BetaOverloadedError:`

            - `String message`

            - `JsonValue type constant`

        - `Optional<String> requestId`

        - `JsonValue type constant`

      - `JsonValue type constant`

    - `class BetaMessageBatchCanceledResult:`

      - `JsonValue type constant`

    - `class BetaMessageBatchExpiredResult:`

      - `JsonValue type constant`

### Beta Message Batch Request Counts

- `class BetaMessageBatchRequestCounts:`

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

### Beta Message Batch Result

- `class BetaMessageBatchResult: union`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `class BetaMessageBatchSucceededResult:`

    - `BetaMessage message`

      - `String id`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `Optional<BetaContainer> container`

        Information about the container used in the request (for the code execution tool)

        - `String id`

          Identifier for the container used in this request

        - `LocalDateTime expiresAt`

          The time at which the container will expire.

          format: date-time

        - `Optional<List<BetaSkill>> skills`

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

      - `List<BetaContentBlock> content`

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

        - `class BetaTextBlock:`

          - `Optional<List<BetaTextCitation>> citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `class BetaCitationCharLocation:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

              - `long endCharIndex`

              - `Optional<String> fileId`

              - `long startCharIndex`

                minimum: 0

              - `JsonValue type constant`

            - `class BetaCitationPageLocation:`

              - `String citedText`

              - `long documentIndex`

                minimum: 0

              - `Optional<String> documentTitle`

              - `long endPageNumber`

              - `Optional<String> fileId`

              - `long startPageNumber`

                minimum: 1

              - `JsonValue type constant`

            - `class BetaCitationContentBlockLocation:`

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

              - `JsonValue type constant`

            - `class BetaCitationsWebSearchResultLocation:`

              - `String citedText`

              - `String encryptedIndex`

              - `Optional<String> title`

                maxLength: 512

              - `JsonValue type constant`

              - `String url`

            - `class BetaCitationSearchResultLocation:`

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

              - `JsonValue type constant`

          - `String text`

            maxLength: 5000000, minLength: 0

          - `JsonValue type constant`

        - `class BetaThinkingBlock:`

          - `String signature`

            A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

            This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

          - `String thinking`

            The text of Claude's thinking process for this block.

          - `JsonValue type constant`

        - `class BetaRedactedThinkingBlock:`

          - `String data`

            The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

            Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `JsonValue type constant`

        - `class BetaToolUseBlock:`

          - `String id`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Input input`

          - `String name`

            minLength: 1

          - `JsonValue type constant`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonValue type constant`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

            - `class BetaServerToolCaller20260120:`

              - `String toolId`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonValue type constant`

          - `Optional<String> toolsetName`

            For a toolset member tool_use, the toolset family.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class BetaServerToolUseBlock:`

          - `String id`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Input input`

          - `Name name`

            - `ADVISOR("advisor")`

            - `WEB_SEARCH("web_search")`

            - `WEB_FETCH("web_fetch")`

            - `CODE_EXECUTION("code_execution")`

            - `BASH_CODE_EXECUTION("bash_code_execution")`

            - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

            - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

            - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

          - `JsonValue type constant`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaWebSearchToolResultBlock:`

          - `BetaWebSearchToolResultBlockContent content`

            - `class BetaWebSearchToolResultError:`

              - `BetaWebSearchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `QUERY_TOO_LONG("query_too_long")`

                - `REQUEST_TOO_LARGE("request_too_large")`

              - `JsonValue type constant`

            - `List<BetaWebSearchResultBlock>`

              - `String encryptedContent`

              - `Optional<String> pageAge`

              - `String title`

              - `JsonValue type constant`

              - `String url`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaWebFetchToolResultBlock:`

          - `Content content`

            - `class BetaWebFetchToolResultErrorBlock:`

              - `BetaWebFetchToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `URL_TOO_LONG("url_too_long")`

                - `URL_NOT_ALLOWED("url_not_allowed")`

                - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

                - `URL_NOT_ACCESSIBLE("url_not_accessible")`

                - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `UNAVAILABLE("unavailable")`

              - `JsonValue type constant`

            - `class BetaWebFetchBlock:`

              - `BetaDocumentBlock content`

                - `Optional<BetaCitationConfig> citations`

                  Citation configuration for the document

                  - `boolean enabled`

                - `Source source`

                  - `class BetaBase64PdfSource:`

                    - `String data`

                      format: byte

                    - `JsonValue mediaType constant`

                    - `JsonValue type constant`

                  - `class BetaPlainTextSource:`

                    - `String data`

                    - `JsonValue mediaType constant`

                    - `JsonValue type constant`

                - `Optional<String> title`

                  The title of the document

                - `JsonValue type constant`

              - `Optional<String> retrievedAt`

                ISO 8601 timestamp when the content was retrieved

              - `JsonValue type constant`

              - `String url`

                Fetched content URL

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

          - `Optional<Caller> caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaAdvisorToolResultBlock:`

          - `Content content`

            - `class BetaAdvisorToolResultError:`

              - `ErrorCode errorCode`

                - `MAX_USES_EXCEEDED("max_uses_exceeded")`

                - `PROMPT_TOO_LONG("prompt_too_long")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `OVERLOADED("overloaded")`

                - `UNAVAILABLE("unavailable")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `MODEL_NOT_FOUND("model_not_found")`

              - `JsonValue type constant`

            - `class BetaAdvisorResultBlock:`

              - `Optional<String> stopReason`

                The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

              - `String text`

              - `JsonValue type constant`

            - `class BetaAdvisorRedactedResultBlock:`

              - `String encryptedContent`

                Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

              - `Optional<String> stopReason`

                The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

              - `JsonValue type constant`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

        - `class BetaCodeExecutionToolResultBlock:`

          - `BetaCodeExecutionToolResultBlockContent content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class BetaCodeExecutionToolResultError:`

              - `BetaCodeExecutionToolResultErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `JsonValue type constant`

            - `class BetaCodeExecutionResultBlock:`

              - `List<BetaCodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue type constant`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type constant`

            - `class BetaEncryptedCodeExecutionResultBlock:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `List<BetaCodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue type constant`

              - `String encryptedStdout`

              - `long returnCode`

              - `String stderr`

              - `JsonValue type constant`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

        - `class BetaBashCodeExecutionToolResultBlock:`

          - `Content content`

            - `class BetaBashCodeExecutionToolResultError:`

              - `ErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

              - `JsonValue type constant`

            - `class BetaBashCodeExecutionResultBlock:`

              - `List<BetaBashCodeExecutionOutputBlock> content`

                - `String fileId`

                - `JsonValue type constant`

              - `long returnCode`

              - `String stderr`

              - `String stdout`

              - `JsonValue type constant`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

        - `class BetaTextEditorCodeExecutionToolResultBlock:`

          - `Content content`

            - `class BetaTextEditorCodeExecutionToolResultError:`

              - `ErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

                - `FILE_NOT_FOUND("file_not_found")`

              - `Optional<String> errorMessage`

              - `JsonValue type constant`

            - `class BetaTextEditorCodeExecutionViewResultBlock:`

              - `String content`

              - `FileType fileType`

                - `TEXT("text")`

                - `IMAGE("image")`

                - `PDF("pdf")`

              - `Optional<Long> numLines`

              - `Optional<Long> startLine`

              - `Optional<Long> totalLines`

              - `JsonValue type constant`

            - `class BetaTextEditorCodeExecutionCreateResultBlock:`

              - `boolean isFileUpdate`

              - `JsonValue type constant`

            - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

              - `Optional<List<String>> lines`

              - `Optional<Long> newLines`

              - `Optional<Long> newStart`

              - `Optional<Long> oldLines`

              - `Optional<Long> oldStart`

              - `JsonValue type constant`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

        - `class BetaToolSearchToolResultBlock:`

          - `Content content`

            - `class BetaToolSearchToolResultError:`

              - `ErrorCode errorCode`

                - `INVALID_TOOL_INPUT("invalid_tool_input")`

                - `UNAVAILABLE("unavailable")`

                - `TOO_MANY_REQUESTS("too_many_requests")`

                - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `Optional<String> errorMessage`

              - `JsonValue type constant`

            - `class BetaToolSearchToolSearchResultBlock:`

              - `List<BetaToolReferenceBlock> toolReferences`

                - `String toolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonValue type constant`

              - `JsonValue type constant`

          - `String toolUseId`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonValue type constant`

        - `class BetaMcpToolUseBlock:`

          - `String id`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Input input`

          - `String name`

            The name of the MCP tool

          - `String serverName`

            The name of the MCP server

          - `JsonValue type constant`

        - `class BetaMcpToolResultBlock:`

          - `Content content`

            - `String`

            - `List<BetaTextBlock>`

              - `Optional<List<BetaTextCitation>> citations`

                Citations supporting the text block.

                The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `String text`

                maxLength: 5000000, minLength: 0

              - `JsonValue type constant`

          - `boolean isError`

          - `String toolUseId`

            pattern: ^[a-zA-Z0-9_-]+$

          - `JsonValue type constant`

        - `class BetaContainerUploadBlock:`

          Response model for a file uploaded to the container.

          - `String fileId`

          - `JsonValue type constant`

        - `class BetaCompactionBlock:`

          A compaction block returned when autocompact is triggered.

          When content is None, it indicates the compaction failed to produce a valid
          summary (e.g., malformed output from the model). Clients may round-trip
          compaction blocks with null content; the server treats them as no-ops.

          - `Optional<String> content`

            Summary of compacted content, or null if compaction failed

          - `Optional<String> encryptedContent`

            Opaque metadata from prior compaction, to be round-tripped verbatim

          - `JsonValue type constant`

        - `class BetaFallbackBlock:`

          Marks the point in `content` where one model's output gives way to the next.

          One block appears per hop where a preceding model actually ran this turn and
          declined. A turn where no preceding model ran and declined has no such
          boundary and carries no block — the signal for whether a fallback model
          served the response is the presence of a `fallback_message` entry in
          `usage.iterations`, not this block.

          The block is treated like a server-tool content block for streaming: it
          arrives via the standard `content_block_start` / `content_block_stop`
          pair and carries no deltas.

          - `BetaFallbackInfo from`

            The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

            - `Model model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `BetaFallbackInfo to`

            The fallback model producing the content that follows this block. Its `model` is always the canonical id.

          - `BetaFallbackRefusalTrigger trigger`

            What caused the `from` model to hand over at this hop.

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

            - `JsonValue type constant`

          - `JsonValue type constant`

      - `Optional<BetaContextManagementResponse> contextManagement`

        Context management response.

        Information about context management strategies applied during the request.

        - `List<AppliedEdit> appliedEdits`

          List of context management edits that were applied.

          - `class BetaClearToolUses20250919EditResponse:`

            - `long clearedInputTokens`

              Number of input tokens cleared by this edit.

              minimum: 0

            - `long clearedToolUses`

              Number of tool uses that were cleared.

              minimum: 0

            - `JsonValue type constant`

              The type of context management edit applied.

          - `class BetaClearThinking20251015EditResponse:`

            - `long clearedInputTokens`

              Number of input tokens cleared by this edit.

              minimum: 0

            - `long clearedThinkingTurns`

              Number of thinking turns that were cleared.

              minimum: 0

            - `JsonValue type constant`

              The type of context management edit applied.

      - `Optional<BetaDiagnostics> diagnostics`

        Response envelope for request-level diagnostics. Present (possibly
        null) whenever the caller supplied `diagnostics` on the request.

        - `Optional<CacheMissReason> cacheMissReason`

          Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

          - `class BetaCacheMissModelChanged:`

            - `long cacheMissedInputTokens`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `JsonValue type constant`

          - `class BetaCacheMissSystemChanged:`

            - `long cacheMissedInputTokens`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `JsonValue type constant`

          - `class BetaCacheMissToolsChanged:`

            - `long cacheMissedInputTokens`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `JsonValue type constant`

          - `class BetaCacheMissMessagesChanged:`

            - `long cacheMissedInputTokens`

              Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

            - `JsonValue type constant`

          - `class BetaCacheMissPreviousMessageNotFound:`

            - `JsonValue type constant`

          - `class BetaCacheMissUnavailable:`

            - `JsonValue type constant`

      - `Model model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `JsonValue role constant`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `Optional<BetaRefusalStopDetails> stopDetails`

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

        - `Optional<String> fallbackCreditToken`

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

        - `Optional<Boolean> fallbackHasPrefillClaim`

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

        - `Optional<String> recommendedModel`

          The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

        - `JsonValue type constant`

      - `Optional<BetaStopReason> stopReason`

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

        - `COMPACTION("compaction")`

        - `REFUSAL("refusal")`

        - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

      - `Optional<String> stopSequence`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `JsonValue type constant`

        Object type.

        For Messages, this is always `"message"`.

      - `BetaUsage usage`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `Optional<BetaCacheCreation> cacheCreation`

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

        - `Optional<BetaFallbackCreditUsage> fallbackCredit`

          Outcome of the `fallback_credit_token` presented on this request.

          - `Status status`

            Whether the fallback-credit reprice was applied to this response's billing.

            A union discriminated on `type`. `redeemed`: the retry is billed as if
            the conversation had been on the retry model all along — including when the
            resulting shift is zero because there was nothing to move. `not_applied`:
            no reprice was applied; the arm's `reason` says why.

            - `class BetaFallbackCreditRedeemed:`

              The reprice was applied: the retry is billed as if the conversation
              had been on the retry model all along.

              - `JsonValue type constant`

            - `class BetaFallbackCreditNotApplied:`

              No reprice was applied; `reason` says why.

              - `Reason reason`

                Why the reprice was not applied.

                A closed enum; additions to the redemption-check vocabulary arrive as
                deliberate schema updates.

                - `BODY_MISMATCH("body_mismatch")`

                - `CONTINUATION_EXCLUDED("continuation_excluded")`

                - `CONTINUATION_ONLY("continuation_only")`

                - `EXPIRED("expired")`

                - `INVALID_TARGET_MODEL("invalid_target_model")`

                - `NOT_ENABLED("not_enabled")`

                - `REPRICE_UNAVAILABLE("reprice_unavailable")`

                - `TEMPORARILY_UNAVAILABLE("temporarily_unavailable")`

                - `VARIANT_FIELDS_PRESENT("variant_fields_present")`

                - `WRONG_ORGANIZATION("wrong_organization")`

                - `WRONG_PLATFORM("wrong_platform")`

                - `WRONG_WORKSPACE("wrong_workspace")`

              - `JsonValue type constant`

              - `Optional<List<String>> removeToRedeem`

                Request fields to remove before retrying, so the retry can redeem this
                token.

                Present exactly when `reason` is `variant_fields_present` — never null,
                never an empty array; absent otherwise. Fields are named only from your own request, and only after
                the sealed variant hash matched. A served best-effort retry has already
                been billed at normal price; nothing redeems retroactively, but a corrected
                re-send inside the token's five-minute window can still redeem.

        - `Optional<String> inferenceGeo`

          The geographic region where inference was performed for this request.

        - `long inputTokens`

          The number of input tokens which were used.

          minimum: 0

        - `Optional<List<BetaIterationsUsageItems>> iterations`

          Per-iteration token usage breakdown.

          Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

          - Determine which iterations exceeded long context thresholds (>=200k tokens)
          - Calculate the context window size from the last `message` entry
          - Understand token accumulation across server-side tool use loops

          A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

          - `class BetaMessageIterationUsage:`

            Token usage for a sampling iteration.

            - `Optional<BetaCacheCreation> cacheCreation`

              Breakdown of cached tokens by TTL

            - `long cacheCreationInputTokens`

              The number of input tokens used to create the cache entry.

              minimum: 0

            - `long cacheReadInputTokens`

              The number of input tokens read from the cache.

              minimum: 0

            - `long inputTokens`

              The number of input tokens which were used.

              minimum: 0

            - `Model model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `long outputTokens`

              The number of output tokens which were used.

              minimum: 0

            - `JsonValue type constant`

              Usage for a sampling iteration

          - `class BetaCompactionIterationUsage:`

            Token usage for a compaction iteration.

            - `Optional<BetaCacheCreation> cacheCreation`

              Breakdown of cached tokens by TTL

            - `long cacheCreationInputTokens`

              The number of input tokens used to create the cache entry.

              minimum: 0

            - `long cacheReadInputTokens`

              The number of input tokens read from the cache.

              minimum: 0

            - `long inputTokens`

              The number of input tokens which were used.

              minimum: 0

            - `long outputTokens`

              The number of output tokens which were used.

              minimum: 0

            - `JsonValue type constant`

              Usage for a compaction iteration

          - `class BetaAdvisorMessageIterationUsage:`

            Token usage for an advisor sub-inference iteration.

            - `Optional<BetaCacheCreation> cacheCreation`

              Breakdown of cached tokens by TTL

            - `long cacheCreationInputTokens`

              The number of input tokens used to create the cache entry.

              minimum: 0

            - `long cacheReadInputTokens`

              The number of input tokens read from the cache.

              minimum: 0

            - `long inputTokens`

              The number of input tokens which were used.

              minimum: 0

            - `Model model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `long outputTokens`

              The number of output tokens which were used.

              minimum: 0

            - `JsonValue type constant`

              Usage for an advisor sub-inference iteration

          - `class BetaFallbackMessageIterationUsage:`

            Token usage for the fallback-model attempt of a server-side fallback request.

            Produced in place of a `message` entry for whichever hop served the
            response. A declined hop produces the existing `message` entry. Whether
            a fallback model served the response is signalled by the presence of this
            entry in `usage.iterations`.

            - `Optional<BetaCacheCreation> cacheCreation`

              Breakdown of cached tokens by TTL

            - `long cacheCreationInputTokens`

              The number of input tokens used to create the cache entry.

              minimum: 0

            - `long cacheReadInputTokens`

              The number of input tokens read from the cache.

              minimum: 0

            - `long inputTokens`

              The number of input tokens which were used.

              minimum: 0

            - `Model model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `long outputTokens`

              The number of output tokens which were used.

              minimum: 0

            - `JsonValue type constant`

              Usage for the fallback-model attempt that served the response

        - `long outputTokens`

          The number of output tokens which were used.

          minimum: 0

        - `Optional<BetaOutputTokensDetails> outputTokensDetails`

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

        - `Optional<BetaServerToolUsage> serverToolUse`

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

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

    - `JsonValue type constant`

  - `class BetaMessageBatchErroredResult:`

    - `BetaErrorResponse error`

      - `BetaError error`

        - `class BetaInvalidRequestError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaAuthenticationError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaBillingError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaPermissionError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaNotFoundError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaRateLimitError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaGatewayTimeoutError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaApiError:`

          - `String message`

          - `JsonValue type constant`

        - `class BetaOverloadedError:`

          - `String message`

          - `JsonValue type constant`

      - `Optional<String> requestId`

      - `JsonValue type constant`

    - `JsonValue type constant`

  - `class BetaMessageBatchCanceledResult:`

    - `JsonValue type constant`

  - `class BetaMessageBatchExpiredResult:`

    - `JsonValue type constant`

### Beta Message Batch Succeeded Result

- `class BetaMessageBatchSucceededResult:`

  - `BetaMessage message`

    - `String id`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `Optional<BetaContainer> container`

      Information about the container used in the request (for the code execution tool)

      - `String id`

        Identifier for the container used in this request

      - `LocalDateTime expiresAt`

        The time at which the container will expire.

        format: date-time

      - `Optional<List<BetaSkill>> skills`

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

    - `List<BetaContentBlock> content`

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

      - `class BetaTextBlock:`

        - `Optional<List<BetaTextCitation>> citations`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `class BetaCitationCharLocation:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

            - `long endCharIndex`

            - `Optional<String> fileId`

            - `long startCharIndex`

              minimum: 0

            - `JsonValue type constant`

          - `class BetaCitationPageLocation:`

            - `String citedText`

            - `long documentIndex`

              minimum: 0

            - `Optional<String> documentTitle`

            - `long endPageNumber`

            - `Optional<String> fileId`

            - `long startPageNumber`

              minimum: 1

            - `JsonValue type constant`

          - `class BetaCitationContentBlockLocation:`

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

            - `JsonValue type constant`

          - `class BetaCitationsWebSearchResultLocation:`

            - `String citedText`

            - `String encryptedIndex`

            - `Optional<String> title`

              maxLength: 512

            - `JsonValue type constant`

            - `String url`

          - `class BetaCitationSearchResultLocation:`

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

            - `JsonValue type constant`

        - `String text`

          maxLength: 5000000, minLength: 0

        - `JsonValue type constant`

      - `class BetaThinkingBlock:`

        - `String signature`

          A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

          This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `String thinking`

          The text of Claude's thinking process for this block.

        - `JsonValue type constant`

      - `class BetaRedactedThinkingBlock:`

        - `String data`

          The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

          Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

        - `JsonValue type constant`

      - `class BetaToolUseBlock:`

        - `String id`

          pattern: ^[a-zA-Z0-9_-]+$

        - `Input input`

        - `String name`

          minLength: 1

        - `JsonValue type constant`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class BetaDirectCaller:`

            Tool invocation directly from the model.

            - `JsonValue type constant`

          - `class BetaServerToolCaller:`

            Tool invocation generated by a server-side tool.

            - `String toolId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

          - `class BetaServerToolCaller20260120:`

            - `String toolId`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `JsonValue type constant`

        - `Optional<String> toolsetName`

          For a toolset member tool_use, the toolset family.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `class BetaServerToolUseBlock:`

        - `String id`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `Input input`

        - `Name name`

          - `ADVISOR("advisor")`

          - `WEB_SEARCH("web_search")`

          - `WEB_FETCH("web_fetch")`

          - `CODE_EXECUTION("code_execution")`

          - `BASH_CODE_EXECUTION("bash_code_execution")`

          - `TEXT_EDITOR_CODE_EXECUTION("text_editor_code_execution")`

          - `TOOL_SEARCH_TOOL_REGEX("tool_search_tool_regex")`

          - `TOOL_SEARCH_TOOL_BM25("tool_search_tool_bm25")`

        - `JsonValue type constant`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class BetaDirectCaller:`

            Tool invocation directly from the model.

          - `class BetaServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class BetaServerToolCaller20260120:`

      - `class BetaWebSearchToolResultBlock:`

        - `BetaWebSearchToolResultBlockContent content`

          - `class BetaWebSearchToolResultError:`

            - `BetaWebSearchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `QUERY_TOO_LONG("query_too_long")`

              - `REQUEST_TOO_LARGE("request_too_large")`

            - `JsonValue type constant`

          - `List<BetaWebSearchResultBlock>`

            - `String encryptedContent`

            - `Optional<String> pageAge`

            - `String title`

            - `JsonValue type constant`

            - `String url`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class BetaDirectCaller:`

            Tool invocation directly from the model.

          - `class BetaServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class BetaServerToolCaller20260120:`

      - `class BetaWebFetchToolResultBlock:`

        - `Content content`

          - `class BetaWebFetchToolResultErrorBlock:`

            - `BetaWebFetchToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `URL_TOO_LONG("url_too_long")`

              - `URL_NOT_ALLOWED("url_not_allowed")`

              - `URL_NOT_IN_PRIOR_CONTEXT("url_not_in_prior_context")`

              - `URL_NOT_ACCESSIBLE("url_not_accessible")`

              - `UNSUPPORTED_CONTENT_TYPE("unsupported_content_type")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `UNAVAILABLE("unavailable")`

            - `JsonValue type constant`

          - `class BetaWebFetchBlock:`

            - `BetaDocumentBlock content`

              - `Optional<BetaCitationConfig> citations`

                Citation configuration for the document

                - `boolean enabled`

              - `Source source`

                - `class BetaBase64PdfSource:`

                  - `String data`

                    format: byte

                  - `JsonValue mediaType constant`

                  - `JsonValue type constant`

                - `class BetaPlainTextSource:`

                  - `String data`

                  - `JsonValue mediaType constant`

                  - `JsonValue type constant`

              - `Optional<String> title`

                The title of the document

              - `JsonValue type constant`

            - `Optional<String> retrievedAt`

              ISO 8601 timestamp when the content was retrieved

            - `JsonValue type constant`

            - `String url`

              Fetched content URL

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

        - `Optional<Caller> caller`

          Tool invocation directly from the model.

          - `class BetaDirectCaller:`

            Tool invocation directly from the model.

          - `class BetaServerToolCaller:`

            Tool invocation generated by a server-side tool.

          - `class BetaServerToolCaller20260120:`

      - `class BetaAdvisorToolResultBlock:`

        - `Content content`

          - `class BetaAdvisorToolResultError:`

            - `ErrorCode errorCode`

              - `MAX_USES_EXCEEDED("max_uses_exceeded")`

              - `PROMPT_TOO_LONG("prompt_too_long")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `OVERLOADED("overloaded")`

              - `UNAVAILABLE("unavailable")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `MODEL_NOT_FOUND("model_not_found")`

            - `JsonValue type constant`

          - `class BetaAdvisorResultBlock:`

            - `Optional<String> stopReason`

              The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

            - `String text`

            - `JsonValue type constant`

          - `class BetaAdvisorRedactedResultBlock:`

            - `String encryptedContent`

              Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

            - `Optional<String> stopReason`

              The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

            - `JsonValue type constant`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

      - `class BetaCodeExecutionToolResultBlock:`

        - `BetaCodeExecutionToolResultBlockContent content`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `class BetaCodeExecutionToolResultError:`

            - `BetaCodeExecutionToolResultErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `JsonValue type constant`

          - `class BetaCodeExecutionResultBlock:`

            - `List<BetaCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue type constant`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue type constant`

          - `class BetaEncryptedCodeExecutionResultBlock:`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `List<BetaCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue type constant`

            - `String encryptedStdout`

            - `long returnCode`

            - `String stderr`

            - `JsonValue type constant`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

      - `class BetaBashCodeExecutionToolResultBlock:`

        - `Content content`

          - `class BetaBashCodeExecutionToolResultError:`

            - `ErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `OUTPUT_FILE_TOO_LARGE("output_file_too_large")`

            - `JsonValue type constant`

          - `class BetaBashCodeExecutionResultBlock:`

            - `List<BetaBashCodeExecutionOutputBlock> content`

              - `String fileId`

              - `JsonValue type constant`

            - `long returnCode`

            - `String stderr`

            - `String stdout`

            - `JsonValue type constant`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

      - `class BetaTextEditorCodeExecutionToolResultBlock:`

        - `Content content`

          - `class BetaTextEditorCodeExecutionToolResultError:`

            - `ErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

              - `FILE_NOT_FOUND("file_not_found")`

            - `Optional<String> errorMessage`

            - `JsonValue type constant`

          - `class BetaTextEditorCodeExecutionViewResultBlock:`

            - `String content`

            - `FileType fileType`

              - `TEXT("text")`

              - `IMAGE("image")`

              - `PDF("pdf")`

            - `Optional<Long> numLines`

            - `Optional<Long> startLine`

            - `Optional<Long> totalLines`

            - `JsonValue type constant`

          - `class BetaTextEditorCodeExecutionCreateResultBlock:`

            - `boolean isFileUpdate`

            - `JsonValue type constant`

          - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

            - `Optional<List<String>> lines`

            - `Optional<Long> newLines`

            - `Optional<Long> newStart`

            - `Optional<Long> oldLines`

            - `Optional<Long> oldStart`

            - `JsonValue type constant`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

      - `class BetaToolSearchToolResultBlock:`

        - `Content content`

          - `class BetaToolSearchToolResultError:`

            - `ErrorCode errorCode`

              - `INVALID_TOOL_INPUT("invalid_tool_input")`

              - `UNAVAILABLE("unavailable")`

              - `TOO_MANY_REQUESTS("too_many_requests")`

              - `EXECUTION_TIME_EXCEEDED("execution_time_exceeded")`

            - `Optional<String> errorMessage`

            - `JsonValue type constant`

          - `class BetaToolSearchToolSearchResultBlock:`

            - `List<BetaToolReferenceBlock> toolReferences`

              - `String toolName`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

              - `JsonValue type constant`

            - `JsonValue type constant`

        - `String toolUseId`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `JsonValue type constant`

      - `class BetaMcpToolUseBlock:`

        - `String id`

          pattern: ^[a-zA-Z0-9_-]+$

        - `Input input`

        - `String name`

          The name of the MCP tool

        - `String serverName`

          The name of the MCP server

        - `JsonValue type constant`

      - `class BetaMcpToolResultBlock:`

        - `Content content`

          - `String`

          - `List<BetaTextBlock>`

            - `Optional<List<BetaTextCitation>> citations`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `String text`

              maxLength: 5000000, minLength: 0

            - `JsonValue type constant`

        - `boolean isError`

        - `String toolUseId`

          pattern: ^[a-zA-Z0-9_-]+$

        - `JsonValue type constant`

      - `class BetaContainerUploadBlock:`

        Response model for a file uploaded to the container.

        - `String fileId`

        - `JsonValue type constant`

      - `class BetaCompactionBlock:`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

        - `Optional<String> content`

          Summary of compacted content, or null if compaction failed

        - `Optional<String> encryptedContent`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `JsonValue type constant`

      - `class BetaFallbackBlock:`

        Marks the point in `content` where one model's output gives way to the next.

        One block appears per hop where a preceding model actually ran this turn and
        declined. A turn where no preceding model ran and declined has no such
        boundary and carries no block — the signal for whether a fallback model
        served the response is the presence of a `fallback_message` entry in
        `usage.iterations`, not this block.

        The block is treated like a server-tool content block for streaming: it
        arrives via the standard `content_block_start` / `content_block_stop`
        pair and carries no deltas.

        - `BetaFallbackInfo from`

          The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

          - `Model model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `BetaFallbackInfo to`

          The fallback model producing the content that follows this block. Its `model` is always the canonical id.

        - `BetaFallbackRefusalTrigger trigger`

          What caused the `from` model to hand over at this hop.

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

          - `JsonValue type constant`

        - `JsonValue type constant`

    - `Optional<BetaContextManagementResponse> contextManagement`

      Context management response.

      Information about context management strategies applied during the request.

      - `List<AppliedEdit> appliedEdits`

        List of context management edits that were applied.

        - `class BetaClearToolUses20250919EditResponse:`

          - `long clearedInputTokens`

            Number of input tokens cleared by this edit.

            minimum: 0

          - `long clearedToolUses`

            Number of tool uses that were cleared.

            minimum: 0

          - `JsonValue type constant`

            The type of context management edit applied.

        - `class BetaClearThinking20251015EditResponse:`

          - `long clearedInputTokens`

            Number of input tokens cleared by this edit.

            minimum: 0

          - `long clearedThinkingTurns`

            Number of thinking turns that were cleared.

            minimum: 0

          - `JsonValue type constant`

            The type of context management edit applied.

    - `Optional<BetaDiagnostics> diagnostics`

      Response envelope for request-level diagnostics. Present (possibly
      null) whenever the caller supplied `diagnostics` on the request.

      - `Optional<CacheMissReason> cacheMissReason`

        Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

        - `class BetaCacheMissModelChanged:`

          - `long cacheMissedInputTokens`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `JsonValue type constant`

        - `class BetaCacheMissSystemChanged:`

          - `long cacheMissedInputTokens`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `JsonValue type constant`

        - `class BetaCacheMissToolsChanged:`

          - `long cacheMissedInputTokens`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `JsonValue type constant`

        - `class BetaCacheMissMessagesChanged:`

          - `long cacheMissedInputTokens`

            Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

          - `JsonValue type constant`

        - `class BetaCacheMissPreviousMessageNotFound:`

          - `JsonValue type constant`

        - `class BetaCacheMissUnavailable:`

          - `JsonValue type constant`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `JsonValue role constant`

      Conversational role of the generated message.

      This will always be `"assistant"`.

    - `Optional<BetaRefusalStopDetails> stopDetails`

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

      - `Optional<String> fallbackCreditToken`

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

      - `Optional<Boolean> fallbackHasPrefillClaim`

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

      - `Optional<String> recommendedModel`

        The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

      - `JsonValue type constant`

    - `Optional<BetaStopReason> stopReason`

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

      - `COMPACTION("compaction")`

      - `REFUSAL("refusal")`

      - `MODEL_CONTEXT_WINDOW_EXCEEDED("model_context_window_exceeded")`

    - `Optional<String> stopSequence`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `JsonValue type constant`

      Object type.

      For Messages, this is always `"message"`.

    - `BetaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `Optional<BetaCacheCreation> cacheCreation`

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

      - `Optional<BetaFallbackCreditUsage> fallbackCredit`

        Outcome of the `fallback_credit_token` presented on this request.

        - `Status status`

          Whether the fallback-credit reprice was applied to this response's billing.

          A union discriminated on `type`. `redeemed`: the retry is billed as if
          the conversation had been on the retry model all along — including when the
          resulting shift is zero because there was nothing to move. `not_applied`:
          no reprice was applied; the arm's `reason` says why.

          - `class BetaFallbackCreditRedeemed:`

            The reprice was applied: the retry is billed as if the conversation
            had been on the retry model all along.

            - `JsonValue type constant`

          - `class BetaFallbackCreditNotApplied:`

            No reprice was applied; `reason` says why.

            - `Reason reason`

              Why the reprice was not applied.

              A closed enum; additions to the redemption-check vocabulary arrive as
              deliberate schema updates.

              - `BODY_MISMATCH("body_mismatch")`

              - `CONTINUATION_EXCLUDED("continuation_excluded")`

              - `CONTINUATION_ONLY("continuation_only")`

              - `EXPIRED("expired")`

              - `INVALID_TARGET_MODEL("invalid_target_model")`

              - `NOT_ENABLED("not_enabled")`

              - `REPRICE_UNAVAILABLE("reprice_unavailable")`

              - `TEMPORARILY_UNAVAILABLE("temporarily_unavailable")`

              - `VARIANT_FIELDS_PRESENT("variant_fields_present")`

              - `WRONG_ORGANIZATION("wrong_organization")`

              - `WRONG_PLATFORM("wrong_platform")`

              - `WRONG_WORKSPACE("wrong_workspace")`

            - `JsonValue type constant`

            - `Optional<List<String>> removeToRedeem`

              Request fields to remove before retrying, so the retry can redeem this
              token.

              Present exactly when `reason` is `variant_fields_present` — never null,
              never an empty array; absent otherwise. Fields are named only from your own request, and only after
              the sealed variant hash matched. A served best-effort retry has already
              been billed at normal price; nothing redeems retroactively, but a corrected
              re-send inside the token's five-minute window can still redeem.

      - `Optional<String> inferenceGeo`

        The geographic region where inference was performed for this request.

      - `long inputTokens`

        The number of input tokens which were used.

        minimum: 0

      - `Optional<List<BetaIterationsUsageItems>> iterations`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the context window size from the last `message` entry
        - Understand token accumulation across server-side tool use loops

        A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

        - `class BetaMessageIterationUsage:`

          Token usage for a sampling iteration.

          - `Optional<BetaCacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

          - `long cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `long cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `Model model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `JsonValue type constant`

            Usage for a sampling iteration

        - `class BetaCompactionIterationUsage:`

          Token usage for a compaction iteration.

          - `Optional<BetaCacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

          - `long cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `long cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `JsonValue type constant`

            Usage for a compaction iteration

        - `class BetaAdvisorMessageIterationUsage:`

          Token usage for an advisor sub-inference iteration.

          - `Optional<BetaCacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

          - `long cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `long cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `Model model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `JsonValue type constant`

            Usage for an advisor sub-inference iteration

        - `class BetaFallbackMessageIterationUsage:`

          Token usage for the fallback-model attempt of a server-side fallback request.

          Produced in place of a `message` entry for whichever hop served the
          response. A declined hop produces the existing `message` entry. Whether
          a fallback model served the response is signalled by the presence of this
          entry in `usage.iterations`.

          - `Optional<BetaCacheCreation> cacheCreation`

            Breakdown of cached tokens by TTL

          - `long cacheCreationInputTokens`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `long cacheReadInputTokens`

            The number of input tokens read from the cache.

            minimum: 0

          - `long inputTokens`

            The number of input tokens which were used.

            minimum: 0

          - `Model model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `long outputTokens`

            The number of output tokens which were used.

            minimum: 0

          - `JsonValue type constant`

            Usage for the fallback-model attempt that served the response

      - `long outputTokens`

        The number of output tokens which were used.

        minimum: 0

      - `Optional<BetaOutputTokensDetails> outputTokensDetails`

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

      - `Optional<BetaServerToolUsage> serverToolUse`

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

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `JsonValue type constant`
