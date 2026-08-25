---
title: Update Agent
url: https://platform.claude.com/docs/en/api/csharp/beta/agents/update
---

## Update Agent

`BetaManagedAgentsAgent Beta.Agents.Update(AgentUpdateParamsparameters, CancellationTokencancellationToken = default)`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `AgentUpdateParams parameters`

  - `required string agentID`

    Path param: Path parameter agent_id

  - `string? description`

    Body param: Description. Omit to preserve; send empty string or null to clear.

  - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams>? mcpServers`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `required string Name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `required Type Type`

      - `"url"Url`

    - `required string Url`

      Endpoint URL for the MCP server.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Model model`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

    - `enum BetaManagedAgentsModel:`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-sonnet-5"ClaudeSonnet5`

        High-performance model for coding and agents

      - `"claude-fable-5"ClaudeFable5`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `"claude-opus-5"ClaudeOpus5`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-8"ClaudeOpus4_8`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-7"ClaudeOpus4_7`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-6"ClaudeOpus4_6`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-6"ClaudeSonnet4_6`

        Best combination of speed and intelligence

      - `"claude-haiku-4-5"ClaudeHaiku4_5`

        Fastest model with near-frontier intelligence

      - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

        Fastest model with near-frontier intelligence

      - `"claude-opus-4-5"ClaudeOpus4_5`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-5"ClaudeSonnet4_5`

        High-performance model for agents and coding

      - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

        High-performance model for agents and coding

    - `class BetaManagedAgentsModelConfigParams:`

      An object that defines additional configuration control over model use

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-sonnet-5"ClaudeSonnet5`

          High-performance model for coding and agents

        - `"claude-fable-5"ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-opus-5"ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-8"ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-7"ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-6"ClaudeOpus4_6`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-6"ClaudeSonnet4_6`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"ClaudeHaiku4_5`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"ClaudeOpus4_5`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-5"ClaudeSonnet4_5`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

          High-performance model for agents and coding

      - `Effort? Effort`

        How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

        - `enum BetaManagedAgentsEffortLevel:`

          How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

          - `"low"Low`

          - `"medium"Medium`

          - `"high"High`

          - `"xhigh"Xhigh`

          - `"max"Max`

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

            - `"low"Low`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

            - `"medium"Medium`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

            - `"high"High`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

            - `"xhigh"Xhigh`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

            - `"max"Max`

      - `string? InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"Standard`

        - `"fast"Fast`

  - `BetaManagedAgentsMultiagentParams? multiagent`

    Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `string name`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  - `IReadOnlyList<BetaManagedAgentsSkillParams>? skills`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear.

    - `class BetaManagedAgentsAnthropicSkillParams:`

      An Anthropic-managed skill.

      - `required string SkillID`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `required Type Type`

        - `"anthropic"Anthropic`

      - `string? Version`

        Version to pin. Defaults to latest if omitted.

    - `class BetaManagedAgentsCustomSkillParams:`

      A user-created custom skill.

      - `required string SkillID`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `required Type Type`

        - `"custom"Custom`

      - `string? Version`

        Version to pin. Defaults to latest if omitted.

  - `string? system`

    Body param: System prompt. Omit to preserve; send empty string or null to clear.

  - `IReadOnlyList<Tool>? tools`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `required Type Type`

        - `"agent_toolset_20260401"AgentToolset20260401`

      - `IReadOnlyList<BetaManagedAgentsAgentToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonElement Name "bash"constant`

            Must be "bash".

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

          - `Type Type`

            - `"bash"Bash`

        - `class BetaManagedAgentsEditToolConfigParams:`

          Configuration override for the edit tool.

          - `JsonElement Name "edit"constant`

            Must be "edit".

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"edit"Edit`

        - `class BetaManagedAgentsReadToolConfigParams:`

          Configuration override for the read tool.

          - `JsonElement Name "read"constant`

            Must be "read".

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"read"Read`

        - `class BetaManagedAgentsWriteToolConfigParams:`

          Configuration override for the write tool.

          - `JsonElement Name "write"constant`

            Must be "write".

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"write"Write`

        - `class BetaManagedAgentsGlobToolConfigParams:`

          Configuration override for the glob tool.

          - `JsonElement Name "glob"constant`

            Must be "glob".

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"glob"Glob`

        - `class BetaManagedAgentsGrepToolConfigParams:`

          Configuration override for the grep tool.

          - `JsonElement Name "grep"constant`

            Must be "grep".

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"grep"Grep`

        - `class BetaManagedAgentsWebFetchToolConfigParams:`

          Configuration override for the web_fetch tool.

          - `JsonElement Name "web_fetch"constant`

            Must be "web_fetch".

          - `IReadOnlyList<string> AllowedDomains`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `Int? MaxContentTokens`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"web_fetch"WebFetch`

        - `class BetaManagedAgentsWebSearchToolConfigParams:`

          Configuration override for the web_search tool.

          - `JsonElement Name "web_search"constant`

            Must be "web_search".

          - `IReadOnlyList<string> AllowedDomains`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Boolean? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

            - `"web_search"WebSearch`

          - `BetaManagedAgentsUserLocation? UserLocation`

            Approximate user location for search result localization.

            - `JsonElement Type "approximate"constant`

              Location precision. Only "approximate" is supported.

            - `string? City`

              City name.

            - `string? Country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `string? Region`

              Region or state name.

            - `string? Timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `BetaManagedAgentsAgentToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools in a toolset.

        - `Boolean? Enabled`

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

      - `required Type Type`

        - `"mcp_toolset"McpToolset`

      - `IReadOnlyList<BetaManagedAgentsMcpToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `required string Name`

          Name of the MCP tool to configure. 1-128 characters.

        - `Boolean? Enabled`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools from an MCP server.

        - `Boolean? Enabled`

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

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonElement Type "object"constant`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `required Type Type`

        - `"custom"Custom`

  - `Int version`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `"message-batches-2024-09-24"MessageBatches2024_09_24`

    - `"prompt-caching-2024-07-31"PromptCaching2024_07_31`

    - `"computer-use-2024-10-22"ComputerUse2024_10_22`

    - `"computer-use-2025-01-24"ComputerUse2025_01_24`

    - `"pdfs-2024-09-25"Pdfs2024_09_25`

    - `"token-counting-2024-11-01"TokenCounting2024_11_01`

    - `"token-efficient-tools-2025-02-19"TokenEfficientTools2025_02_19`

    - `"output-128k-2025-02-19"Output128k2025_02_19`

    - `"files-api-2025-04-14"FilesApi2025_04_14`

    - `"mcp-client-2025-04-04"McpClient2025_04_04`

    - `"mcp-client-2025-11-20"McpClient2025_11_20`

    - `"dev-full-thinking-2025-05-14"DevFullThinking2025_05_14`

    - `"interleaved-thinking-2025-05-14"InterleavedThinking2025_05_14`

    - `"code-execution-2025-05-22"CodeExecution2025_05_22`

    - `"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025_04_11`

    - `"context-1m-2025-08-07"Context1m2025_08_07`

    - `"context-management-2025-06-27"ContextManagement2025_06_27`

    - `"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025_08_26`

    - `"skills-2025-10-02"Skills2025_10_02`

    - `"fast-mode-2026-02-01"FastMode2026_02_01`

    - `"output-300k-2026-03-24"Output300k2026_03_24`

    - `"user-profiles-2026-03-24"UserProfiles2026_03_24`

    - `"user-profiles-2026-08-18"UserProfiles2026_08_18`

    - `"advisor-tool-2026-03-01"AdvisorTool2026_03_01`

    - `"managed-agents-2026-04-01"ManagedAgents2026_04_01`

    - `"cache-diagnosis-2026-04-07"CacheDiagnosis2026_04_07`

    - `"dreaming-2026-04-21"Dreaming2026_04_21`

    - `"thinking-token-count-2026-05-13"ThinkingTokenCount2026_05_13`

    - `"server-side-fallback-2026-06-01"ServerSideFallback2026_06_01`

    - `"server-side-fallback-2026-07-01"ServerSideFallback2026_07_01`

    - `"fallback-credit-2026-06-01"FallbackCredit2026_06_01`

    - `"fallback-credit-2026-07-01"FallbackCredit2026_07_01`

    - `"agent-memory-2026-07-22"AgentMemory2026_07_22`

    - `"mid-conversation-tool-changes-2026-07-01"MidConversationToolChanges2026_07_01`

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

  - `required string? Description`

  - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

    - `required string Name`

    - `required Type Type`

      - `"url"Url`

    - `required string Url`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required BetaManagedAgentsModelConfig Model`

    Model identifier and configuration.

    - `required BetaManagedAgentsModel ID`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-sonnet-5"ClaudeSonnet5`

        High-performance model for coding and agents

      - `"claude-fable-5"ClaudeFable5`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `"claude-opus-5"ClaudeOpus5`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-8"ClaudeOpus4_8`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-7"ClaudeOpus4_7`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-6"ClaudeOpus4_6`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-6"ClaudeSonnet4_6`

        Best combination of speed and intelligence

      - `"claude-haiku-4-5"ClaudeHaiku4_5`

        Fastest model with near-frontier intelligence

      - `"claude-haiku-4-5-20251001"ClaudeHaiku4_5_20251001`

        Fastest model with near-frontier intelligence

      - `"claude-opus-4-5"ClaudeOpus4_5`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-5-20251101"ClaudeOpus4_5_20251101`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-5"ClaudeSonnet4_5`

        High-performance model for agents and coding

      - `"claude-sonnet-4-5-20250929"ClaudeSonnet4_5_20250929`

        High-performance model for agents and coding

    - `Effort Effort`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow:`

        Low effort. Favors latency over reasoning depth.

        - `required Type Type`

          - `"low"Low`

      - `class BetaManagedAgentsEffortMedium:`

        Medium effort. Balances latency and reasoning depth.

        - `required Type Type`

          - `"medium"Medium`

      - `class BetaManagedAgentsEffortHigh:`

        High effort. Favors reasoning depth.

        - `required Type Type`

          - `"high"High`

      - `class BetaManagedAgentsEffortXhigh:`

        Extra-high effort. Not all models accept this level.

        - `required Type Type`

          - `"xhigh"Xhigh`

      - `class BetaManagedAgentsEffortMax:`

        Maximum effort. Favors reasoning depth over latency.

        - `required Type Type`

          - `"max"Max`

    - `string InferenceGeo`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"Standard`

      - `"fast"Fast`

  - `required BetaManagedAgentsMultiagent? Multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `required IReadOnlyList<Agent> Agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `required string ID`

        - `required Type Type`

          - `"agent"Agent`

        - `required Int Version`

      - `class BetaManagedAgentsAdvisor:`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `required string Model`

          The advisor model id.

        - `required Type Type`

          - `"advisor"Advisor`

    - `required Type Type`

      - `"coordinator"Coordinator`

  - `required string Name`

  - `required IReadOnlyList<Skill> Skills`

    - `class BetaManagedAgentsAnthropicSkill:`

      A resolved Anthropic-managed skill.

      - `required string SkillID`

      - `required Type Type`

        - `"anthropic"Anthropic`

      - `required string Version`

    - `class BetaManagedAgentsCustomSkill:`

      A resolved user-created custom skill.

      - `required string SkillID`

      - `required Type Type`

        - `"custom"Custom`

      - `required string Version`

  - `required string? System`

  - `required IReadOnlyList<Tool> Tools`

    - `class BetaManagedAgentsAgentToolset20260401:`

      - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

        - `class BetaManagedAgentsBashToolConfig:`

          Configuration for the bash tool.

          - `required Boolean Enabled`

          - `JsonElement Name "bash"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `required Type Type`

                - `"always_allow"AlwaysAllow`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

                - `"always_ask"AlwaysAsk`

          - `JsonElement Type "bash"constant`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `required Boolean Enabled`

          - `JsonElement Name "edit"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "edit"constant`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `required Boolean Enabled`

          - `JsonElement Name "read"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "read"constant`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `required Boolean Enabled`

          - `JsonElement Name "write"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "write"constant`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `required Boolean Enabled`

          - `JsonElement Name "glob"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "glob"constant`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `required Boolean Enabled`

          - `JsonElement Name "grep"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "grep"constant`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `required Boolean Enabled`

          - `JsonElement Name "web_fetch"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "web_fetch"constant`

          - `IReadOnlyList<string> AllowedDomains`

          - `IReadOnlyList<string> BlockedDomains`

          - `Int? MaxContentTokens`

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `required Boolean Enabled`

          - `JsonElement Name "web_search"constant`

          - `required PermissionPolicy PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonElement Type "web_search"constant`

          - `IReadOnlyList<string> AllowedDomains`

          - `IReadOnlyList<string> BlockedDomains`

          - `BetaManagedAgentsUserLocation? UserLocation`

            Approximate user location for search result localization.

            - `JsonElement Type "approximate"constant`

              Location precision. Only "approximate" is supported.

            - `string? City`

              City name.

            - `string? Country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `string? Region`

              Region or state name.

            - `string? Timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

        Resolved default configuration for agent tools.

        - `required Boolean Enabled`

        - `required PermissionPolicy PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `required Type Type`

        - `"agent_toolset_20260401"AgentToolset20260401`

    - `class BetaManagedAgentsMcpToolset:`

      - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

        - `required Boolean Enabled`

        - `required string Name`

        - `required PermissionPolicy PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `required Boolean Enabled`

        - `required PermissionPolicy PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `required string McpServerName`

      - `required Type Type`

        - `"mcp_toolset"McpToolset`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

      - `required string Description`

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonElement Type "object"constant`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

      - `required Type Type`

        - `"custom"Custom`

  - `required Type Type`

    - `"agent"Agent`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

  - `required Int Version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```csharp
AgentUpdateParams parameters = new()
{
    AgentID = "agent_011CZkYpogX7uDKUyvBTophP"
};

var betaManagedAgentsAgent = await client.Beta.Agents.Update(parameters);

Console.WriteLine(betaManagedAgentsAgent);
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
