# Create Session

`BetaManagedAgentsSession beta().sessions().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/sessions`

Create Session

## Parameters

- `SessionCreateParams params`

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

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `Agent agent`

    Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `String`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `String id`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsAgentWithOverridesParams:`

      Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

      - `String id`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<List<BetaManagedAgentsUrlMcpServerParams>> mcpServers`

        Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

        - `String name`

          Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

          minLength: 1, maxLength: 255

        - `Type type`

        - `String url`

          Endpoint URL for the MCP server.

          maxLength: 2048

      - `Optional<Model> model`

        Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

        - `enum BetaManagedAgentsModel:`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

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

        - `class BetaManagedAgentsModelConfigParams:`

          An object that defines additional configuration control over model use

          - `BetaManagedAgentsModel id`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Optional<Effort> effort`

            How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

            - `enum BetaManagedAgentsEffortLevel:`

              How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

              - `XHIGH("xhigh")`

              - `MAX("max")`

            - `class BetaManagedAgentsEffortLow:`

              Low effort. Favors latency over reasoning depth.

              - `Type type`

            - `class BetaManagedAgentsEffortMedium:`

              Medium effort. Balances latency and reasoning depth.

              - `Type type`

            - `class BetaManagedAgentsEffortHigh:`

              High effort. Favors reasoning depth.

              - `Type type`

            - `class BetaManagedAgentsEffortXhigh:`

              Extra-high effort. Not all models accept this level.

              - `Type type`

            - `class BetaManagedAgentsEffortMax:`

              Maximum effort. Favors reasoning depth over latency.

              - `Type type`

          - `Optional<String> inferenceGeo`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

          - `Optional<Speed> speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `STANDARD("standard")`

            - `FAST("fast")`

      - `Optional<List<BetaManagedAgentsSkillParams>> skills`

        Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

        - `class BetaManagedAgentsAnthropicSkillParams:`

          An Anthropic-managed skill.

          - `String skillId`

            Identifier of the Anthropic skill (e.g., "xlsx").

            minLength: 1, maxLength: 64

          - `Type type`

          - `Optional<String> version`

            Version to pin. Defaults to latest if omitted.

            minLength: 1, maxLength: 64

        - `class BetaManagedAgentsCustomSkillParams:`

          A user-created custom skill.

          - `String skillId`

            Tagged ID of the custom skill (e.g., "skill_01XJ5...").

            minLength: 1, maxLength: 64

          - `Type type`

          - `Optional<String> version`

            Version to pin. Defaults to latest if omitted.

            minLength: 1, maxLength: 64

      - `Optional<String> system`

        Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

        maxLength: 100000

      - `Optional<List<Tool>> tools`

        Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

        - `class BetaManagedAgentsAgentToolset20260401Params:`

          Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

          - `Type type`

          - `Optional<List<BetaManagedAgentsAgentToolConfigParams>> configs`

            Per-tool configuration overrides.

            - `class BetaManagedAgentsBashToolConfigParams:`

              Configuration override for the bash tool.

              - `JsonValue name = "bash"`

                Must be "bash".

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `Type type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `Type type`

              - `Optional<Type> type`

            - `class BetaManagedAgentsEditToolConfigParams:`

              Configuration override for the edit tool.

              - `JsonValue name = "edit"`

                Must be "edit".

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

            - `class BetaManagedAgentsReadToolConfigParams:`

              Configuration override for the read tool.

              - `JsonValue name = "read"`

                Must be "read".

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

            - `class BetaManagedAgentsWriteToolConfigParams:`

              Configuration override for the write tool.

              - `JsonValue name = "write"`

                Must be "write".

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

            - `class BetaManagedAgentsGlobToolConfigParams:`

              Configuration override for the glob tool.

              - `JsonValue name = "glob"`

                Must be "glob".

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

            - `class BetaManagedAgentsGrepToolConfigParams:`

              Configuration override for the grep tool.

              - `JsonValue name = "grep"`

                Must be "grep".

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

            - `class BetaManagedAgentsWebFetchToolConfigParams:`

              Configuration override for the web_fetch tool.

              - `JsonValue name = "web_fetch"`

                Must be "web_fetch".

              - `Optional<List<String>> allowedDomains`

                Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

              - `Optional<List<String>> blockedDomains`

                Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<Long> maxContentTokens`

                Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

                format: int32

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

            - `class BetaManagedAgentsWebSearchToolConfigParams:`

              Configuration override for the web_search tool.

              - `JsonValue name = "web_search"`

                Must be "web_search".

              - `Optional<List<String>> allowedDomains`

                Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

              - `Optional<List<String>> blockedDomains`

                Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

              - `Optional<Boolean> enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `Optional<PermissionPolicy> permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Optional<Type> type`

              - `Optional<BetaManagedAgentsUserLocation> userLocation`

                Approximate user location for search result localization.

                - `JsonValue type = "approximate"`

                  Location precision. Only "approximate" is supported.

                - `Optional<String> city`

                  City name.

                  minLength: 1, maxLength: 255

                - `Optional<String> country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Optional<String> region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Optional<String> timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `Optional<BetaManagedAgentsAgentToolsetDefaultConfigParams> defaultConfig`

            Default configuration for all tools in a toolset.

            - `Optional<Boolean> enabled`

              Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

            - `Optional<PermissionPolicy> permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsMcpToolsetParams:`

          Configuration for tools from an MCP server defined in `mcp_servers`.

          - `String mcpServerName`

            Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

            minLength: 1, maxLength: 255

          - `Type type`

          - `Optional<List<BetaManagedAgentsMcpToolConfigParams>> configs`

            Per-tool configuration overrides.

            - `String name`

              Name of the MCP tool to configure. 1-128 characters.

              minLength: 1, maxLength: 128

            - `Optional<Boolean> enabled`

              Whether this tool is enabled. Overrides the `default_config` setting.

            - `Optional<PermissionPolicy> permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `Optional<BetaManagedAgentsMcpToolsetDefaultConfigParams> defaultConfig`

            Default configuration for all tools from an MCP server.

            - `Optional<Boolean> enabled`

              Whether tools are enabled by default. Defaults to true if not specified.

            - `Optional<PermissionPolicy> permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsCustomToolParams:`

          A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

          - `String description`

            Description of what the tool does, shown to the agent to help it decide when to use the tool.

            minLength: 1

          - `BetaManagedAgentsCustomToolInputSchema inputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonValue type = "object"`

            - `Optional<Properties> properties`

            - `Optional<List<String>> required`

          - `String name`

            Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

            minLength: 1, maxLength: 128

          - `Type type`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version.

        format: int32

  - `String environmentId`

    ID of the `environment` defining the container configuration for this session.

    minLength: 1, maxLength: 128

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `Optional<List<InitialEvent>> initialEvents`

    Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Optional<List<Resource>> resources`

    Resources (e.g. repositories, files) to mount into the session's container.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `String authorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `Type type`

      - `String url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `String fileId`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `Optional<String> title`

    Human-readable session title.

    maxLength: 500

  - `Optional<List<String>> vaultIds`

    Vault IDs for stored credentials the agent can use during the session.

## Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `String id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `String id`

    - `Optional<String> description`

    - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

      - `String name`

      - `Type type`

      - `String url`

    - `BetaManagedAgentsModelConfig model`

      Model identifier and configuration.

      - `BetaManagedAgentsModel id`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_FABLE_5_1("claude-fable-5-1")`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `CLAUDE_SONNET_5("claude-sonnet-5")`

          High-performance model for coding and agents

        - `CLAUDE_FABLE_5("claude-fable-5")`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `CLAUDE_OPUS_5("claude-opus-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Powerful intelligence for long-running agents and coding

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

      - `Optional<Effort> effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `Type type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `Type type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `Type type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `Type type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `Type type`

      - `Optional<String> inferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `List<Agent> agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `String id`

          - `Optional<String> description`

          - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

            - `String name`

            - `Type type`

            - `String url`

          - `BetaManagedAgentsModelConfig model`

            Model identifier and configuration.

          - `String name`

          - `List<Skill> skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `String skillId`

              - `Type type`

              - `String version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `String skillId`

              - `Type type`

              - `String version`

          - `Optional<String> system`

          - `List<Tool> tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `List<BetaManagedAgentsAgentToolConfig> configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `boolean enabled`

                  - `JsonValue name = "bash"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `Type type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `Type type`

                  - `JsonValue type = "bash"`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `boolean enabled`

                  - `JsonValue name = "edit"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "edit"`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `boolean enabled`

                  - `JsonValue name = "read"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "read"`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `boolean enabled`

                  - `JsonValue name = "write"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "write"`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `boolean enabled`

                  - `JsonValue name = "glob"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "glob"`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `boolean enabled`

                  - `JsonValue name = "grep"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "grep"`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `boolean enabled`

                  - `JsonValue name = "web_fetch"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "web_fetch"`

                  - `Optional<List<String>> allowedDomains`

                  - `Optional<List<String>> blockedDomains`

                  - `Optional<Long> maxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `boolean enabled`

                  - `JsonValue name = "web_search"`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type = "web_search"`

                  - `Optional<List<String>> allowedDomains`

                  - `Optional<List<String>> blockedDomains`

                  - `Optional<BetaManagedAgentsUserLocation> userLocation`

                    Approximate user location for search result localization.

                    - `JsonValue type = "approximate"`

                      Location precision. Only "approximate" is supported.

                    - `Optional<String> city`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Optional<String> country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Optional<String> region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Optional<String> timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                Resolved default configuration for agent tools.

                - `boolean enabled`

                - `PermissionPolicy permissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `Type type`

            - `class BetaManagedAgentsMcpToolset:`

              - `List<BetaManagedAgentsMcpToolConfig> configs`

                - `boolean enabled`

                - `String name`

                - `PermissionPolicy permissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `boolean enabled`

                - `PermissionPolicy permissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `String mcpServerName`

              - `Type type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `String description`

              - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonValue type = "object"`

                - `Optional<Properties> properties`

                - `Optional<List<String>> required`

              - `String name`

              - `Type type`

          - `Type type`

          - `long version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `String model`

            The advisor model id.

          - `Type type`

      - `Type type`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String environmentId`

  - `Metadata metadata`

  - `List<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `Optional<LocalDateTime> completedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String description`

      What the agent should produce.

    - `Optional<String> explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `long iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `String outcomeId`

      Server-generated outc_ ID for this outcome.

    - `String result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type type`

  - `List<BetaManagedAgentsSessionResource> resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `String id`

      - `LocalDateTime createdAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `String mountPath`

      - `Type type`

      - `LocalDateTime updatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `String url`

      - `Optional<Checkout> checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

    - `class BetaManagedAgentsFileResource:`

      - `String id`

      - `LocalDateTime createdAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `String fileId`

      - `String mountPath`

      - `Type type`

      - `LocalDateTime updatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `Optional<String> mountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Optional<String> name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `Optional<Double> durationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status status`

    SessionStatus enum

    - `RESCHEDULING("rescheduling")`

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `TERMINATED("terminated")`

  - `Optional<String> title`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `Optional<BetaMonetaryAmount> listCost`

      A monetary amount in a specific currency.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Optional<Long> webFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `Optional<Long> webSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `List<String> vaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `Optional<String> deploymentId`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsSession;
import com.anthropic.models.beta.sessions.SessionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SessionCreateParams params = SessionCreateParams.builder()
            .agent("agent_011CZkYpogX7uDKUyvBTophP")
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .build();
        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().create(params);
    }
}
```

### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```
