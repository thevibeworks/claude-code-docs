---
title: Update Agent
url: https://platform.claude.com/docs/en/api/java/beta/agents/update
---

## Update Agent

`BetaManagedAgentsAgent beta().agents().update(AgentUpdateParamsparams = AgentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/v1/agents/{agent_id}`

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

  - `Optional<String> description`

    Description. Omit to preserve; send empty string or null to clear.

  - `Optional<List<BetaManagedAgentsUrlMcpServerParams>> mcpServers`

    MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `String name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `Type type`

      - `URL("url")`

    - `String url`

      Endpoint URL for the MCP server.

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<Model> model`

    Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `enum BetaManagedAgentsModel:`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

            - `LOW("low")`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `Type type`

            - `MEDIUM("medium")`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `Type type`

            - `HIGH("high")`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `Type type`

            - `XHIGH("xhigh")`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `Type type`

            - `MAX("max")`

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

  - `Optional<List<BetaManagedAgentsSkillParams>> skills`

    Skills. Full replacement. Omit to preserve; send empty array or null to clear.

    - `class BetaManagedAgentsAnthropicSkillParams:`

      An Anthropic-managed skill.

      - `String skillId`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `Type type`

        - `ANTHROPIC("anthropic")`

      - `Optional<String> version`

        Version to pin. Defaults to latest if omitted.

    - `class BetaManagedAgentsCustomSkillParams:`

      A user-created custom skill.

      - `String skillId`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `Type type`

        - `CUSTOM("custom")`

      - `Optional<String> version`

        Version to pin. Defaults to latest if omitted.

  - `Optional<String> system`

    System prompt. Omit to preserve; send empty string or null to clear.

  - `Optional<List<Tool>> tools`

    Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type type`

        - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

      - `Optional<List<BetaManagedAgentsAgentToolConfigParams>> configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonValue; name "bash"constant`

            Must be "bash".

            - `BASH("bash")`

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

          - `Optional<Type> type`

            - `BASH("bash")`

        - `class BetaManagedAgentsEditToolConfigParams:`

          Configuration override for the edit tool.

          - `JsonValue; name "edit"constant`

            Must be "edit".

            - `EDIT("edit")`

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Optional<Type> type`

            - `EDIT("edit")`

        - `class BetaManagedAgentsReadToolConfigParams:`

          Configuration override for the read tool.

          - `JsonValue; name "read"constant`

            Must be "read".

            - `READ("read")`

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Optional<Type> type`

            - `READ("read")`

        - `class BetaManagedAgentsWriteToolConfigParams:`

          Configuration override for the write tool.

          - `JsonValue; name "write"constant`

            Must be "write".

            - `WRITE("write")`

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Optional<Type> type`

            - `WRITE("write")`

        - `class BetaManagedAgentsGlobToolConfigParams:`

          Configuration override for the glob tool.

          - `JsonValue; name "glob"constant`

            Must be "glob".

            - `GLOB("glob")`

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Optional<Type> type`

            - `GLOB("glob")`

        - `class BetaManagedAgentsGrepToolConfigParams:`

          Configuration override for the grep tool.

          - `JsonValue; name "grep"constant`

            Must be "grep".

            - `GREP("grep")`

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Optional<Type> type`

            - `GREP("grep")`

        - `class BetaManagedAgentsWebFetchToolConfigParams:`

          Configuration override for the web_fetch tool.

          - `JsonValue; name "web_fetch"constant`

            Must be "web_fetch".

            - `WEB_FETCH("web_fetch")`

          - `Optional<List<String>> allowedDomains`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `Optional<List<String>> blockedDomains`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Optional<Boolean> enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Optional<Long> maxContentTokens`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          - `Optional<PermissionPolicy> permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Optional<Type> type`

            - `WEB_FETCH("web_fetch")`

        - `class BetaManagedAgentsWebSearchToolConfigParams:`

          Configuration override for the web_search tool.

          - `JsonValue; name "web_search"constant`

            Must be "web_search".

            - `WEB_SEARCH("web_search")`

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

            - `WEB_SEARCH("web_search")`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue; type "approximate"constant`

              Location precision. Only "approximate" is supported.

              - `APPROXIMATE("approximate")`

            - `Optional<String> city`

              City name.

            - `Optional<String> country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Optional<String> region`

              Region or state name.

            - `Optional<String> timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

      - `Type type`

        - `MCP_TOOLSET("mcp_toolset")`

      - `Optional<List<BetaManagedAgentsMcpToolConfigParams>> configs`

        Per-tool configuration overrides.

        - `String name`

          Name of the MCP tool to configure. 1-128 characters.

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

      - `BetaManagedAgentsCustomToolInputSchema inputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonValue; type "object"constant`

          - `OBJECT("object")`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `Type type`

        - `CUSTOM("custom")`

  - `Optional<Long> version`

    The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

      - `URL("url")`

    - `String url`

  - `Metadata metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

    - `BetaManagedAgentsModel id`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `LOW("low")`

      - `class BetaManagedAgentsEffortMedium:`

        Medium effort. Balances latency and reasoning depth.

        - `Type type`

          - `MEDIUM("medium")`

      - `class BetaManagedAgentsEffortHigh:`

        High effort. Favors reasoning depth.

        - `Type type`

          - `HIGH("high")`

      - `class BetaManagedAgentsEffortXhigh:`

        Extra-high effort. Not all models accept this level.

        - `Type type`

          - `XHIGH("xhigh")`

      - `class BetaManagedAgentsEffortMax:`

        Maximum effort. Favors reasoning depth over latency.

        - `Type type`

          - `MAX("max")`

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

          - `AGENT("agent")`

        - `long version`

      - `class BetaManagedAgentsAdvisor:`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `String model`

          The advisor model id.

        - `Type type`

          - `ADVISOR("advisor")`

    - `Type type`

      - `COORDINATOR("coordinator")`

  - `String name`

  - `List<Skill> skills`

    - `class BetaManagedAgentsAnthropicSkill:`

      A resolved Anthropic-managed skill.

      - `String skillId`

      - `Type type`

        - `ANTHROPIC("anthropic")`

      - `String version`

    - `class BetaManagedAgentsCustomSkill:`

      A resolved user-created custom skill.

      - `String skillId`

      - `Type type`

        - `CUSTOM("custom")`

      - `String version`

  - `Optional<String> system`

  - `List<Tool> tools`

    - `class BetaManagedAgentsAgentToolset20260401:`

      - `List<BetaManagedAgentsAgentToolConfig> configs`

        - `class BetaManagedAgentsBashToolConfig:`

          Configuration for the bash tool.

          - `boolean enabled`

          - `JsonValue; name "bash"constant`

            - `BASH("bash")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

          - `JsonValue; type "bash"constant`

            - `BASH("bash")`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue; name "edit"constant`

            - `EDIT("edit")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "edit"constant`

            - `EDIT("edit")`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue; name "read"constant`

            - `READ("read")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "read"constant`

            - `READ("read")`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue; name "write"constant`

            - `WRITE("write")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "write"constant`

            - `WRITE("write")`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue; name "glob"constant`

            - `GLOB("glob")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "glob"constant`

            - `GLOB("glob")`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue; name "grep"constant`

            - `GREP("grep")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "grep"constant`

            - `GREP("grep")`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue; name "web_fetch"constant`

            - `WEB_FETCH("web_fetch")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "web_fetch"constant`

            - `WEB_FETCH("web_fetch")`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue; name "web_search"constant`

            - `WEB_SEARCH("web_search")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "web_search"constant`

            - `WEB_SEARCH("web_search")`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue; type "approximate"constant`

              Location precision. Only "approximate" is supported.

              - `APPROXIMATE("approximate")`

            - `Optional<String> city`

              City name.

            - `Optional<String> country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Optional<String> region`

              Region or state name.

            - `Optional<String> timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

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

        - `MCP_TOOLSET("mcp_toolset")`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

      - `String description`

      - `BetaManagedAgentsCustomToolInputSchema inputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonValue; type "object"constant`

          - `OBJECT("object")`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

        - `CUSTOM("custom")`

  - `Type type`

    - `AGENT("agent")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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

#### Response

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
