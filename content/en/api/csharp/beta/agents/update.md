# Update Agent

`BetaManagedAgentsAgent Beta.Agents.Update(parameters, cancellationToken = default)`

**POST** `/v1/agents/{agent_id}`

Update Agent

## Parameters

- `AgentUpdateParams parameters`

  - `required string agentID`

    Path param: Path parameter agent_id

  - `string? description`

    Body param: Description. Omit to preserve; send empty string or null to clear.

    maxLength: 2048

  - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams>? mcpServers`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `required string Name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `required Type Type`

    - `required string Url`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Model model`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `enum BetaManagedAgentsModel:`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `ClaudeFable5_1("claude-fable-5-1")`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `ClaudeSonnet5("claude-sonnet-5")`

        High-performance model for coding and agents

      - `ClaudeFable5("claude-fable-5")`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `ClaudeOpus5("claude-opus-5")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_8("claude-opus-4-8")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_7("claude-opus-4-7")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_6("claude-opus-4-6")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeSonnet4_6("claude-sonnet-4-6")`

        Best combination of speed and intelligence

      - `ClaudeHaiku4_5("claude-haiku-4-5")`

        Fastest model with near-frontier intelligence

      - `ClaudeHaiku4_5_20251001("claude-haiku-4-5-20251001")`

        Fastest model with near-frontier intelligence

      - `ClaudeOpus4_5("claude-opus-4-5")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_5_20251101("claude-opus-4-5-20251101")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeSonnet4_5("claude-sonnet-4-5")`

        High-performance model for agents and coding

      - `ClaudeSonnet4_5_20250929("claude-sonnet-4-5-20250929")`

        High-performance model for agents and coding

    - `class BetaManagedAgentsModelConfigParams:`

      An object that defines additional configuration control over model use

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1("claude-fable-5-1")`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5("claude-sonnet-5")`

          High-performance model for coding and agents

        - `ClaudeFable5("claude-fable-5")`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5("claude-opus-5")`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8("claude-opus-4-8")`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7("claude-opus-4-7")`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_6("claude-opus-4-6")`

          Powerful intelligence for long-running agents and coding

        - `ClaudeSonnet4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `ClaudeHaiku4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `ClaudeHaiku4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `ClaudeOpus4_5("claude-opus-4-5")`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_5_20251101("claude-opus-4-5-20251101")`

          Powerful intelligence for long-running agents and coding

        - `ClaudeSonnet4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `ClaudeSonnet4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Effort? Effort`

        How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

        - `enum BetaManagedAgentsEffortLevel:`

          How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

          - `Low("low")`

          - `Medium("medium")`

          - `High("high")`

          - `Xhigh("xhigh")`

          - `Max("max")`

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string? InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard("standard")`

        - `Fast("fast")`

  - `BetaManagedAgentsMultiagentParams? multiagent`

    Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `string name`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

    maxLength: 256

  - `IReadOnlyList<BetaManagedAgentsSkillParams>? skills`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear.

    - `class BetaManagedAgentsAnthropicSkillParams:`

      An Anthropic-managed skill.

      - `required string SkillID`

        Identifier of the Anthropic skill (e.g., "xlsx").

        minLength: 1, maxLength: 64

      - `required Type Type`

      - `string? Version`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

    - `class BetaManagedAgentsCustomSkillParams:`

      A user-created custom skill.

      - `required string SkillID`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        minLength: 1, maxLength: 64

      - `required Type Type`

      - `string? Version`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

  - `string? system`

    Body param: System prompt. Omit to preserve; send empty string or null to clear.

    maxLength: 100000

  - `IReadOnlyList<Tool>? tools`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsAgentToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonElement Name = "bash"`

            Must be "bash".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `required Type Type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

          - `Type Type`

        - `class BetaManagedAgentsEditToolConfigParams:`

          Configuration override for the edit tool.

          - `JsonElement Name = "edit"`

            Must be "edit".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsReadToolConfigParams:`

          Configuration override for the read tool.

          - `JsonElement Name = "read"`

            Must be "read".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWriteToolConfigParams:`

          Configuration override for the write tool.

          - `JsonElement Name = "write"`

            Must be "write".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsGlobToolConfigParams:`

          Configuration override for the glob tool.

          - `JsonElement Name = "glob"`

            Must be "glob".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsGrepToolConfigParams:`

          Configuration override for the grep tool.

          - `JsonElement Name = "grep"`

            Must be "grep".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWebFetchToolConfigParams:`

          Configuration override for the web_fetch tool.

          - `JsonElement Name = "web_fetch"`

            Must be "web_fetch".

          - `IReadOnlyList<string> AllowedDomains`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `int? MaxContentTokens`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWebSearchToolConfigParams:`

          Configuration override for the web_search tool.

          - `JsonElement Name = "web_search"`

            Must be "web_search".

          - `IReadOnlyList<string> AllowedDomains`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

          - `BetaManagedAgentsUserLocation? UserLocation`

            Approximate user location for search result localization.

            - `JsonElement Type = "approximate"`

              Location precision. Only "approximate" is supported.

            - `string? City`

              City name.

              minLength: 1, maxLength: 255

            - `string? Country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `string? Region`

              Region or state name.

              minLength: 1, maxLength: 255

            - `string? Timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `BetaManagedAgentsAgentToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools in a toolset.

        - `bool? Enabled`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsMcpToolsetParams:`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `required string McpServerName`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsMcpToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `required string Name`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `bool? Enabled`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools from an MCP server.

        - `bool? Enabled`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsCustomToolParams:`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `required string Description`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonElement Type = "object"`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `required Type Type`

  - `int version`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

    format: int32

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

## Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? Description`

  - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

    - `required string Name`

    - `required Type Type`

    - `required string Url`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required BetaManagedAgentsModelConfig Model`

    Model identifier and configuration.

    - `required BetaManagedAgentsModel ID`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `ClaudeFable5_1("claude-fable-5-1")`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `ClaudeSonnet5("claude-sonnet-5")`

        High-performance model for coding and agents

      - `ClaudeFable5("claude-fable-5")`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `ClaudeOpus5("claude-opus-5")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_8("claude-opus-4-8")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_7("claude-opus-4-7")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_6("claude-opus-4-6")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeSonnet4_6("claude-sonnet-4-6")`

        Best combination of speed and intelligence

      - `ClaudeHaiku4_5("claude-haiku-4-5")`

        Fastest model with near-frontier intelligence

      - `ClaudeHaiku4_5_20251001("claude-haiku-4-5-20251001")`

        Fastest model with near-frontier intelligence

      - `ClaudeOpus4_5("claude-opus-4-5")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_5_20251101("claude-opus-4-5-20251101")`

        Powerful intelligence for long-running agents and coding

      - `ClaudeSonnet4_5("claude-sonnet-4-5")`

        High-performance model for agents and coding

      - `ClaudeSonnet4_5_20250929("claude-sonnet-4-5-20250929")`

        High-performance model for agents and coding

    - `Effort Effort`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow:`

        Low effort. Favors latency over reasoning depth.

        - `required Type Type`

      - `class BetaManagedAgentsEffortMedium:`

        Medium effort. Balances latency and reasoning depth.

        - `required Type Type`

      - `class BetaManagedAgentsEffortHigh:`

        High effort. Favors reasoning depth.

        - `required Type Type`

      - `class BetaManagedAgentsEffortXhigh:`

        Extra-high effort. Not all models accept this level.

        - `required Type Type`

      - `class BetaManagedAgentsEffortMax:`

        Maximum effort. Favors reasoning depth over latency.

        - `required Type Type`

    - `string InferenceGeo`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard("standard")`

      - `Fast("fast")`

  - `required BetaManagedAgentsMultiagent? Multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `required IReadOnlyList<Agent> Agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `required string ID`

        - `required Type Type`

        - `required int Version`

          format: int32

      - `class BetaManagedAgentsAdvisor:`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `required string Model`

          The advisor model id.

        - `required Type Type`

    - `required Type Type`

  - `required string Name`

  - `required IReadOnlyList<Skill> Skills`

    - `class BetaManagedAgentsAnthropicSkill:`

      A resolved Anthropic-managed skill.

      - `required string SkillID`

      - `required Type Type`

      - `required string Version`

    - `class BetaManagedAgentsCustomSkill:`

      A resolved user-created custom skill.

      - `required string SkillID`

      - `required Type Type`

      - `required string Version`

  - `required string? System`

  - `required IReadOnlyList<Tool> Tools`

    - `class BetaManagedAgentsAgentToolset20260401:`

      - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

        - `class BetaManagedAgentsBashToolConfig:`

          Configuration for the bash tool.

          - `required bool Enabled`

          - `JsonElement Name = "bash"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `required Type Type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

          - `JsonElement Type = "bash"`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `required bool Enabled`

          - `JsonElement Name = "edit"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "edit"`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `required bool Enabled`

          - `JsonElement Name = "read"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "read"`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `required bool Enabled`

          - `JsonElement Name = "write"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "write"`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `required bool Enabled`

          - `JsonElement Name = "glob"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "glob"`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `required bool Enabled`

          - `JsonElement Name = "grep"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "grep"`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `required bool Enabled`

          - `JsonElement Name = "web_fetch"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "web_fetch"`

          - `IReadOnlyList<string> AllowedDomains`

          - `IReadOnlyList<string> BlockedDomains`

          - `int? MaxContentTokens`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `required bool Enabled`

          - `JsonElement Name = "web_search"`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type = "web_search"`

          - `IReadOnlyList<string> AllowedDomains`

          - `IReadOnlyList<string> BlockedDomains`

          - `BetaManagedAgentsUserLocation? UserLocation`

            Approximate user location for search result localization.

            - `JsonElement Type = "approximate"`

              Location precision. Only "approximate" is supported.

            - `string? City`

              City name.

              minLength: 1, maxLength: 255

            - `string? Country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `string? Region`

              Region or state name.

              minLength: 1, maxLength: 255

            - `string? Timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

        Resolved default configuration for agent tools.

        - `required bool Enabled`

        - `required PermissionPolicy PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `required Type Type`

    - `class BetaManagedAgentsMcpToolset:`

      - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

        - `required bool Enabled`

        - `required string Name`

        - `required PermissionPolicy PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `required bool Enabled`

        - `required PermissionPolicy PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `required string McpServerName`

      - `required Type Type`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

      - `required string Description`

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonElement Type = "object"`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

      - `required Type Type`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required int Version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```csharp
AgentUpdateParams parameters = new()
{
    AgentID = "agent_011CZkYpogX7uDKUyvBTophP"
};

var betaManagedAgentsAgent = await client.Beta.Agents.Update(parameters);

Console.WriteLine(betaManagedAgentsAgent);
```

### Response (200)

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
