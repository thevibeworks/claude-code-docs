# Agents

## Create Agent

`BetaManagedAgentsAgent beta().agents().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/agents`

Create Agent

### Parameters

- `AgentCreateParams params`

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

  - `Model model`

    Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

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

  - `String name`

    Human-readable name for the agent.

    minLength: 1, maxLength: 256

  - `Optional<String> description`

    Description of what the agent does.

    maxLength: 2048

  - `Optional<List<BetaManagedAgentsUrlMcpServerParams>> mcpServers`

    MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `String name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `Type type`

    - `String url`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Optional<BetaManagedAgentsMultiagentParams> multiagent`

    A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Optional<List<BetaManagedAgentsSkillParams>> skills`

    Skills available to the agent.

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

    System prompt for the agent.

    maxLength: 100000

  - `Optional<List<Tool>> tools`

    Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type type`

      - `Optional<List<BetaManagedAgentsAgentToolConfigParams>> configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `Type type`

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentCreateParams;
import com.anthropic.models.beta.agents.BetaManagedAgentsAgent;
import com.anthropic.models.beta.agents.BetaManagedAgentsModel;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        AgentCreateParams params = AgentCreateParams.builder()
            .model(BetaManagedAgentsModel.CLAUDE_OPUS_5)
            .name("My First Agent")
            .build();
        BetaManagedAgentsAgent betaManagedAgentsAgent = client.beta().agents().create(params);
    }
}
```

#### Response (200)

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## List Agents

`AgentListPage beta().agents().list(params = AgentListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/agents`

List Agents

### Parameters

- `AgentListParams params`

  - `Optional<LocalDateTime> createdAtGte`

    Return agents created at or after this time (inclusive).

    format: date-time

  - `Optional<LocalDateTime> createdAtLte`

    Return agents created at or before this time (inclusive).

    format: date-time

  - `Optional<Boolean> includeArchived`

    Include archived agents in results. Defaults to false.

  - `Optional<Long> limit`

    Maximum results per page. Default 20, maximum 100.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor from a previous response.

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

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentListPage;
import com.anthropic.models.beta.agents.AgentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        AgentListPage page = client.beta().agents().list();
    }
}
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "agent_011CZkYpogX7uDKUyvBTophP",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "A general-purpose starter agent.",
      "mcp_servers": [
        {
          "name": "example-mcp",
          "type": "url",
          "url": "https://example-server.modelcontextprotocol.io/sse"
        }
      ],
      "metadata": {
        "foo": "bar"
      },
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
      "updated_at": "2026-03-15T10:00:00Z",
      "version": 1
    }
  ],
  "next_page": "next_page"
}
```

## Get Agent

`BetaManagedAgentsAgent beta().agents().retrieve(params = AgentRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `AgentRetrieveParams params`

  - `Optional<String> agentId`

  - `Optional<Long> version`

    Agent version. Omit for the most recent version. Must be at least 1 if specified.

    format: int32

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

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentRetrieveParams;
import com.anthropic.models.beta.agents.BetaManagedAgentsAgent;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsAgent betaManagedAgentsAgent = client.beta().agents().retrieve("agent_011CZkYpogX7uDKUyvBTophP");
    }
}
```

#### Response (200)

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## Update Agent

`BetaManagedAgentsAgent beta().agents().update(params = AgentUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `AgentUpdateParams params`

  - `Optional<String> agentId`

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

  - `Optional<String> description`

    Description. Omit to preserve; send empty string or null to clear.

    maxLength: 2048

  - `Optional<List<BetaManagedAgentsUrlMcpServerParams>> mcpServers`

    MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `String name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `Type type`

    - `String url`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<Model> model`

    Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

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

  - `Optional<BetaManagedAgentsMultiagentParams> multiagent`

    A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Optional<String> name`

    Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

    maxLength: 256

  - `Optional<List<BetaManagedAgentsSkillParams>> skills`

    Skills. Full replacement. Omit to preserve; send empty array or null to clear.

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

    System prompt. Omit to preserve; send empty string or null to clear.

    maxLength: 100000

  - `Optional<List<Tool>> tools`

    Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type type`

      - `Optional<List<BetaManagedAgentsAgentToolConfigParams>> configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

          - `JsonValue name constant`

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

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `Type type`

  - `Optional<Long> version`

    The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

    format: int32

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentUpdateParams;
import com.anthropic.models.beta.agents.BetaManagedAgentsAgent;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsAgent betaManagedAgentsAgent = client.beta().agents().update("agent_011CZkYpogX7uDKUyvBTophP");
    }
}
```

#### Response (200)

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## Archive Agent

`BetaManagedAgentsAgent beta().agents().archive(params = AgentArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `AgentArchiveParams params`

  - `Optional<String> agentId`

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

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.AgentArchiveParams;
import com.anthropic.models.beta.agents.BetaManagedAgentsAgent;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsAgent betaManagedAgentsAgent = client.beta().agents().archive("agent_011CZkYpogX7uDKUyvBTophP");
    }
}
```

#### Response (200)

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```

## Domain types

### Beta Managed Agents Advisor

- `class BetaManagedAgentsAdvisor:`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

  - `String model`

    The advisor model id.

  - `Type type`

### Beta Managed Agents Agent

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Beta Managed Agents Agent Reference

- `class BetaManagedAgentsAgentReference:`

  A resolved agent reference with a concrete version.

  - `String id`

  - `Type type`

  - `long version`

    format: int32

### Beta Managed Agents Agent Tool Config

- `class BetaManagedAgentsAgentToolConfig: union`

  Configuration for a specific agent tool.

  - `class BetaManagedAgentsBashToolConfig:`

    Configuration for the bash tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

        - `Type type`

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

        - `Type type`

    - `JsonValue type constant`

  - `class BetaManagedAgentsEditToolConfig:`

    Configuration for the edit tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

  - `class BetaManagedAgentsReadToolConfig:`

    Configuration for the read tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

  - `class BetaManagedAgentsWriteToolConfig:`

    Configuration for the write tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

  - `class BetaManagedAgentsGlobToolConfig:`

    Configuration for the glob tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

  - `class BetaManagedAgentsGrepToolConfig:`

    Configuration for the grep tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

  - `class BetaManagedAgentsWebFetchToolConfig:`

    Configuration for the web_fetch tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

    - `Optional<List<String>> allowedDomains`

    - `Optional<List<String>> blockedDomains`

    - `Optional<Long> maxContentTokens`

      format: int32

  - `class BetaManagedAgentsWebSearchToolConfig:`

    Configuration for the web_search tool.

    - `boolean enabled`

    - `JsonValue name constant`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

    - `JsonValue type constant`

    - `Optional<List<String>> allowedDomains`

    - `Optional<List<String>> blockedDomains`

    - `Optional<BetaManagedAgentsUserLocation> userLocation`

      Approximate user location for search result localization.

      - `JsonValue type constant`

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

### Beta Managed Agents Agent Tool Config Params

- `class BetaManagedAgentsAgentToolConfigParams: union`

  Configuration override for a specific tool within a toolset.

  - `class BetaManagedAgentsBashToolConfigParams:`

    Configuration override for the bash tool.

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

    - `JsonValue name constant`

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

      - `JsonValue type constant`

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

### Beta Managed Agents Agent Toolset Default Config

- `class BetaManagedAgentsAgentToolsetDefaultConfig:`

  Resolved default configuration for agent tools.

  - `boolean enabled`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

### Beta Managed Agents Agent Toolset Default Config Params

- `class BetaManagedAgentsAgentToolsetDefaultConfigParams:`

  Default configuration for all tools in a toolset.

  - `Optional<Boolean> enabled`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `Optional<PermissionPolicy> permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

### Beta Managed Agents Agent Toolset20260401

- `class BetaManagedAgentsAgentToolset20260401:`

  - `List<BetaManagedAgentsAgentToolConfig> configs`

    - `class BetaManagedAgentsBashToolConfig:`

      Configuration for the bash tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

          - `Type type`

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

          - `Type type`

      - `JsonValue type constant`

    - `class BetaManagedAgentsEditToolConfig:`

      Configuration for the edit tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

    - `class BetaManagedAgentsReadToolConfig:`

      Configuration for the read tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

    - `class BetaManagedAgentsWriteToolConfig:`

      Configuration for the write tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

    - `class BetaManagedAgentsGlobToolConfig:`

      Configuration for the glob tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

    - `class BetaManagedAgentsGrepToolConfig:`

      Configuration for the grep tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

    - `class BetaManagedAgentsWebFetchToolConfig:`

      Configuration for the web_fetch tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

      - `Optional<List<String>> allowedDomains`

      - `Optional<List<String>> blockedDomains`

      - `Optional<Long> maxContentTokens`

        format: int32

    - `class BetaManagedAgentsWebSearchToolConfig:`

      Configuration for the web_search tool.

      - `boolean enabled`

      - `JsonValue name constant`

      - `PermissionPolicy permissionPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy:`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy:`

          Tool calls require user confirmation before execution.

      - `JsonValue type constant`

      - `Optional<List<String>> allowedDomains`

      - `Optional<List<String>> blockedDomains`

      - `Optional<BetaManagedAgentsUserLocation> userLocation`

        Approximate user location for search result localization.

        - `JsonValue type constant`

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

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `class BetaManagedAgentsAgentToolset20260401BashInput:`

  Input payload for the `bash` tool of the
  `agent_toolset_20260401` toolset. All fields are optional;
  a normal invocation supplies `command`, while `restart=true`
  (with no `command`) reboots the runner-side bash session.

  - `Optional<String> command`

    Shell command to execute. Omit only when `restart` is true.

  - `Optional<Boolean> restart`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `Optional<Long> timeoutMs`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

    minimum: 0

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `class BetaManagedAgentsAgentToolset20260401EditInput:`

  Input payload for the `edit` tool. Performs a string
  replacement in the named file; by default `old_string` must
  occur exactly once.

  - `String filePath`

    Path of the file to edit.

  - `String newString`

    Replacement text.

  - `String oldString`

    Substring to find and replace.

  - `Optional<Boolean> replaceAll`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `class BetaManagedAgentsAgentToolset20260401GlobInput:`

  Input payload for the `glob` tool. Returns paths matching a
  doublestar glob pattern, newest first.

  - `String pattern`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `Optional<String> path`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `class BetaManagedAgentsAgentToolset20260401GrepInput:`

  Input payload for the `grep` tool. Searches file contents for
  a regular expression, returning matching lines.

  - `String pattern`

    Regular expression to search for.

  - `Optional<String> path`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `class BetaManagedAgentsAgentToolset20260401Params:`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `Type type`

  - `Optional<List<BetaManagedAgentsAgentToolConfigParams>> configs`

    Per-tool configuration overrides.

    - `class BetaManagedAgentsBashToolConfigParams:`

      Configuration override for the bash tool.

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

      - `JsonValue name constant`

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

        - `JsonValue type constant`

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

### Beta Managed Agents Agent Toolset20260401 Read Input

- `class BetaManagedAgentsAgentToolset20260401ReadInput:`

  Input payload for the `read` tool. Reads file contents
  relative to the runner's working directory (or absolute when
  the runner permits).

  - `String filePath`

    Path of the file to read.

  - `Optional<List<Long>> viewRange`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

    minItems: 2, maxItems: 2

### Beta Managed Agents Agent Toolset20260401 Write Input

- `class BetaManagedAgentsAgentToolset20260401WriteInput:`

  Input payload for the `write` tool. Writes (overwriting) the
  entire file contents.

  - `String content`

    Full file contents to write.

  - `String filePath`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `class BetaManagedAgentsAlwaysAllowPolicy:`

  Tool calls are automatically approved without user confirmation.

  - `Type type`

### Beta Managed Agents Always Ask Policy

- `class BetaManagedAgentsAlwaysAskPolicy:`

  Tool calls require user confirmation before execution.

  - `Type type`

### Beta Managed Agents Anthropic Skill

- `class BetaManagedAgentsAnthropicSkill:`

  A resolved Anthropic-managed skill.

  - `String skillId`

  - `Type type`

  - `String version`

### Beta Managed Agents Anthropic Skill Params

- `class BetaManagedAgentsAnthropicSkillParams:`

  An Anthropic-managed skill.

  - `String skillId`

    Identifier of the Anthropic skill (e.g., "xlsx").

    minLength: 1, maxLength: 64

  - `Type type`

  - `Optional<String> version`

    Version to pin. Defaults to latest if omitted.

    minLength: 1, maxLength: 64

### Beta Managed Agents Bash Tool Config

- `class BetaManagedAgentsBashToolConfig:`

  Configuration for the bash tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

### Beta Managed Agents Bash Tool Config Params

- `class BetaManagedAgentsBashToolConfigParams:`

  Configuration override for the bash tool.

  - `JsonValue name constant`

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

### Beta Managed Agents Custom Skill

- `class BetaManagedAgentsCustomSkill:`

  A resolved user-created custom skill.

  - `String skillId`

  - `Type type`

  - `String version`

### Beta Managed Agents Custom Skill Params

- `class BetaManagedAgentsCustomSkillParams:`

  A user-created custom skill.

  - `String skillId`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    minLength: 1, maxLength: 64

  - `Type type`

  - `Optional<String> version`

    Version to pin. Defaults to latest if omitted.

    minLength: 1, maxLength: 64

### Beta Managed Agents Custom Tool

- `class BetaManagedAgentsCustomTool:`

  A custom tool as returned in API responses.

  - `String description`

  - `BetaManagedAgentsCustomToolInputSchema inputSchema`

    JSON Schema for custom tool input parameters.

    - `JsonValue type constant`

    - `Optional<Properties> properties`

    - `Optional<List<String>> required`

  - `String name`

  - `Type type`

### Beta Managed Agents Custom Tool Input Schema

- `class BetaManagedAgentsCustomToolInputSchema:`

  JSON Schema for custom tool input parameters.

  - `JsonValue type constant`

  - `Optional<Properties> properties`

  - `Optional<List<String>> required`

### Beta Managed Agents Custom Tool Params

- `class BetaManagedAgentsCustomToolParams:`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `String description`

    Description of what the tool does, shown to the agent to help it decide when to use the tool.

    minLength: 1

  - `BetaManagedAgentsCustomToolInputSchema inputSchema`

    JSON Schema for custom tool input parameters.

    - `JsonValue type constant`

    - `Optional<Properties> properties`

    - `Optional<List<String>> required`

  - `String name`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    minLength: 1, maxLength: 128

  - `Type type`

### Beta Managed Agents Edit Tool Config

- `class BetaManagedAgentsEditToolConfig:`

  Configuration for the edit tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

### Beta Managed Agents Edit Tool Config Params

- `class BetaManagedAgentsEditToolConfigParams:`

  Configuration override for the edit tool.

  - `JsonValue name constant`

    Must be "edit".

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

### Beta Managed Agents Effort High

- `class BetaManagedAgentsEffortHigh:`

  High effort. Favors reasoning depth.

  - `Type type`

### Beta Managed Agents Effort Low

- `class BetaManagedAgentsEffortLow:`

  Low effort. Favors latency over reasoning depth.

  - `Type type`

### Beta Managed Agents Effort Max

- `class BetaManagedAgentsEffortMax:`

  Maximum effort. Favors reasoning depth over latency.

  - `Type type`

### Beta Managed Agents Effort Medium

- `class BetaManagedAgentsEffortMedium:`

  Medium effort. Balances latency and reasoning depth.

  - `Type type`

### Beta Managed Agents Effort Xhigh

- `class BetaManagedAgentsEffortXhigh:`

  Extra-high effort. Not all models accept this level.

  - `Type type`

### Beta Managed Agents Glob Tool Config

- `class BetaManagedAgentsGlobToolConfig:`

  Configuration for the glob tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

### Beta Managed Agents Glob Tool Config Params

- `class BetaManagedAgentsGlobToolConfigParams:`

  Configuration override for the glob tool.

  - `JsonValue name constant`

    Must be "glob".

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

### Beta Managed Agents Grep Tool Config

- `class BetaManagedAgentsGrepToolConfig:`

  Configuration for the grep tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

### Beta Managed Agents Grep Tool Config Params

- `class BetaManagedAgentsGrepToolConfigParams:`

  Configuration override for the grep tool.

  - `JsonValue name constant`

    Must be "grep".

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

### Beta Managed Agents MCP Server URL Definition

- `class BetaManagedAgentsMcpServerUrlDefinition:`

  URL-based MCP server connection as returned in API responses.

  - `String name`

  - `Type type`

  - `String url`

### Beta Managed Agents MCP Tool Config

- `class BetaManagedAgentsMcpToolConfig:`

  Resolved configuration for a specific MCP tool.

  - `boolean enabled`

  - `String name`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

### Beta Managed Agents MCP Tool Config Params

- `class BetaManagedAgentsMcpToolConfigParams:`

  Configuration override for a specific MCP tool.

  - `String name`

    Name of the MCP tool to configure. 1-128 characters.

    minLength: 1, maxLength: 128

  - `Optional<Boolean> enabled`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `Optional<PermissionPolicy> permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

### Beta Managed Agents MCP Toolset

- `class BetaManagedAgentsMcpToolset:`

  - `List<BetaManagedAgentsMcpToolConfig> configs`

    - `boolean enabled`

    - `String name`

    - `PermissionPolicy permissionPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy:`

        Tool calls are automatically approved without user confirmation.

        - `Type type`

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

        - `Type type`

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

### Beta Managed Agents MCP Toolset Default Config

- `class BetaManagedAgentsMcpToolsetDefaultConfig:`

  Resolved default configuration for all tools from an MCP server.

  - `boolean enabled`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

### Beta Managed Agents MCP Toolset Default Config Params

- `class BetaManagedAgentsMcpToolsetDefaultConfigParams:`

  Default configuration for all tools from an MCP server.

  - `Optional<Boolean> enabled`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `Optional<PermissionPolicy> permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

### Beta Managed Agents MCP Toolset Params

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

        - `Type type`

      - `class BetaManagedAgentsAlwaysAskPolicy:`

        Tool calls require user confirmation before execution.

        - `Type type`

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

### Beta Managed Agents Model

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

### Beta Managed Agents Model Config

- `class BetaManagedAgentsModelConfig:`

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

### Beta Managed Agents Model Config Params

- `class BetaManagedAgentsModelConfigParams:`

  An object that defines additional configuration control over model use

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

### Beta Managed Agents Multiagent Coordinator

- `class BetaManagedAgentsMultiagentCoordinator:`

  Resolved coordinator topology with a concrete agent roster.

  - `List<Agent> agents`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `class BetaManagedAgentsAgentReference:`

      A resolved agent reference with a concrete version.

      - `String id`

      - `Type type`

      - `long version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `String model`

        The advisor model id.

      - `Type type`

  - `Type type`

### Beta Managed Agents Multiagent Coordinator Params

- `class BetaManagedAgentsMultiagentCoordinatorParams:`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `List<BetaManagedAgentsMultiagentRosterEntryParams> agents`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

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

    - `class BetaManagedAgentsMultiagentSelfParams:`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `Type type`

    - `class BetaManagedAgentsAdvisorParams:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `String model`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `Type type`

  - `Type type`

### Beta Managed Agents Multiagent Self Params

- `class BetaManagedAgentsMultiagentSelfParams:`

  Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

  - `Type type`

### Beta Managed Agents Read Tool Config

- `class BetaManagedAgentsReadToolConfig:`

  Configuration for the read tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

### Beta Managed Agents Read Tool Config Params

- `class BetaManagedAgentsReadToolConfigParams:`

  Configuration override for the read tool.

  - `JsonValue name constant`

    Must be "read".

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

### Beta Managed Agents Session Thread Agent

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `long version`

    format: int32

### Beta Managed Agents Skill Params

- `class BetaManagedAgentsSkillParams: union`

  Skill to load in the session container.

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

### Beta Managed Agents URL MCP Server Params

- `class BetaManagedAgentsUrlMcpServerParams:`

  URL-based MCP server connection.

  - `String name`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Type type`

  - `String url`

    Endpoint URL for the MCP server.

    maxLength: 2048

### Beta Managed Agents User Location

- `class BetaManagedAgentsUserLocation:`

  Approximate user location for search result localization.

  - `JsonValue type constant`

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

### Beta Managed Agents Web Fetch Tool Config

- `class BetaManagedAgentsWebFetchToolConfig:`

  Configuration for the web_fetch tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

  - `Optional<List<String>> allowedDomains`

  - `Optional<List<String>> blockedDomains`

  - `Optional<Long> maxContentTokens`

    format: int32

### Beta Managed Agents Web Fetch Tool Config Params

- `class BetaManagedAgentsWebFetchToolConfigParams:`

  Configuration override for the web_fetch tool.

  - `JsonValue name constant`

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

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `Optional<Type> type`

### Beta Managed Agents Web Search Tool Config

- `class BetaManagedAgentsWebSearchToolConfig:`

  Configuration for the web_search tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

  - `Optional<List<String>> allowedDomains`

  - `Optional<List<String>> blockedDomains`

  - `Optional<BetaManagedAgentsUserLocation> userLocation`

    Approximate user location for search result localization.

    - `JsonValue type constant`

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

### Beta Managed Agents Web Search Tool Config Params

- `class BetaManagedAgentsWebSearchToolConfigParams:`

  Configuration override for the web_search tool.

  - `JsonValue name constant`

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

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `Optional<Type> type`

  - `Optional<BetaManagedAgentsUserLocation> userLocation`

    Approximate user location for search result localization.

    - `JsonValue type constant`

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

### Beta Managed Agents Write Tool Config

- `class BetaManagedAgentsWriteToolConfig:`

  Configuration for the write tool.

  - `boolean enabled`

  - `JsonValue name constant`

  - `PermissionPolicy permissionPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy:`

      Tool calls are automatically approved without user confirmation.

      - `Type type`

    - `class BetaManagedAgentsAlwaysAskPolicy:`

      Tool calls require user confirmation before execution.

      - `Type type`

  - `JsonValue type constant`

### Beta Managed Agents Write Tool Config Params

- `class BetaManagedAgentsWriteToolConfigParams:`

  Configuration override for the write tool.

  - `JsonValue name constant`

    Must be "write".

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

## Agents › Versions

### List Agent Versions

`VersionListPage beta().agents().versions().list(params = VersionListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/agents/{agent_id}/versions`

List Agent Versions

#### Parameters

- `VersionListParams params`

  - `Optional<String> agentId`

  - `Optional<Long> limit`

    Maximum results per page. Default 20, maximum 100.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor.

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

#### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

    - `String url`

  - `Metadata metadata`

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

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

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

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

          - `JsonValue type constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue name constant`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue type constant`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue type constant`

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

        - `JsonValue type constant`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.versions.VersionListPage;
import com.anthropic.models.beta.agents.versions.VersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionListPage page = client.beta().agents().versions().list("agent_011CZkYpogX7uDKUyvBTophP");
    }
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "agent_011CZkYpogX7uDKUyvBTophP",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "A general-purpose starter agent.",
      "mcp_servers": [
        {
          "name": "example-mcp",
          "type": "url",
          "url": "https://example-server.modelcontextprotocol.io/sse"
        }
      ],
      "metadata": {
        "foo": "bar"
      },
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
      "updated_at": "2026-03-15T10:00:00Z",
      "version": 1
    }
  ],
  "next_page": "next_page"
}
```
