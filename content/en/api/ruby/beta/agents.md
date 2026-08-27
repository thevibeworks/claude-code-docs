# Agents

## Create Agent

`beta.agents.create(**kwargs) -> BetaManagedAgentsAgent`

**POST** `/v1/agents`

Create Agent

### Parameters

- `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

  - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-8"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-7"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String = String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `effort: :low | :medium | :high | 2 more | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | 3 more`

      How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

      - `BetaManagedAgentsEffortLevel = :low | :medium | :high | 2 more`

        How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `name: String`

  Human-readable name for the agent.

  minLength: 1, maxLength: 256

- `description: String`

  Description of what the agent does.

  maxLength: 2048

- `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    minLength: 1, maxLength: 255

  - `type: :url`

  - `url: String`

    Endpoint URL for the MCP server.

    maxLength: 2048

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `multiagent: BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `String = String`

    - `class BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: String`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `type: :agent`

      - `version: Integer`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsMultiagentSelfParams`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: :self`

    - `class BetaManagedAgentsAdvisorParams`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `model: String`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `type: :advisor`

  - `type: :coordinator`

- `skills: Array[BetaManagedAgentsSkillParams]`

  Skills available to the agent.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

      minLength: 1, maxLength: 64

    - `type: :anthropic`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      minLength: 1, maxLength: 64

    - `type: :custom`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

- `system_: String`

  System prompt for the agent.

  maxLength: 100000

- `tools: Array[BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams]`

  Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

  - `class BetaManagedAgentsAgentToolset20260401Params`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: :agent_toolset_20260401`

    - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

      Per-tool configuration overrides.

      - `class BetaManagedAgentsBashToolConfigParams`

        Configuration override for the bash tool.

        - `name: :bash`

          Must be "bash".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

        - `type: :bash`

      - `class BetaManagedAgentsEditToolConfigParams`

        Configuration override for the edit tool.

        - `name: :edit`

          Must be "edit".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :edit`

      - `class BetaManagedAgentsReadToolConfigParams`

        Configuration override for the read tool.

        - `name: :read`

          Must be "read".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :read`

      - `class BetaManagedAgentsWriteToolConfigParams`

        Configuration override for the write tool.

        - `name: :write`

          Must be "write".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :write`

      - `class BetaManagedAgentsGlobToolConfigParams`

        Configuration override for the glob tool.

        - `name: :glob`

          Must be "glob".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :glob`

      - `class BetaManagedAgentsGrepToolConfigParams`

        Configuration override for the grep tool.

        - `name: :grep`

          Must be "grep".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :grep`

      - `class BetaManagedAgentsWebFetchToolConfigParams`

        Configuration override for the web_fetch tool.

        - `name: :web_fetch`

          Must be "web_fetch".

        - `allowed_domains: Array[String]`

          Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: Array[String]`

          Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `max_content_tokens: Integer`

          Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          format: int32

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :web_fetch`

      - `class BetaManagedAgentsWebSearchToolConfigParams`

        Configuration override for the web_search tool.

        - `name: :web_search`

          Must be "web_search".

        - `allowed_domains: Array[String]`

          Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: Array[String]`

          Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :web_search`

        - `user_location: BetaManagedAgentsUserLocation`

          Approximate user location for search result localization.

          - `type: :approximate`

            Location precision. Only "approximate" is supported.

          - `city: String`

            City name.

            minLength: 1, maxLength: 255

          - `country: String`

            Two-letter ISO 3166-1 country code, uppercase.

          - `region: String`

            Region or state name.

            minLength: 1, maxLength: 255

          - `timezone: String`

            IANA timezone identifier, e.g. "America/Los_Angeles".

            minLength: 1, maxLength: 255

    - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

      Default configuration for all tools in a toolset.

      - `enabled: bool`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

  - `class BetaManagedAgentsMCPToolsetParams`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: String`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      minLength: 1, maxLength: 255

    - `type: :mcp_toolset`

    - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

      Per-tool configuration overrides.

      - `name: String`

        Name of the MCP tool to configure. 1-128 characters.

        minLength: 1, maxLength: 128

      - `enabled: bool`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

    - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: bool`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool.

      minLength: 1

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `type: :object`

      - `properties: Hash[Symbol, untyped]`

      - `required: Array[String]`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      minLength: 1, maxLength: 128

    - `type: :custom`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.create(
  model: Anthropic::Beta::BetaManagedAgentsModel::CLAUDE_OPUS_5,
  name: "My First Agent"
)

puts(beta_managed_agents_agent)
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

`beta.agents.list(**kwargs) -> PageCursor<BetaManagedAgentsAgent>`

**GET** `/v1/agents`

List Agents

### Parameters

- `created_at_gte: Time`

  Return agents created at or after this time (inclusive).

  format: date-time

- `created_at_lte: Time`

  Return agents created at or before this time (inclusive).

  format: date-time

- `include_archived: bool`

  Include archived agents in results. Defaults to false.

- `limit: Integer`

  Maximum results per page. Default 20, maximum 100.

  format: int32

- `page: String`

  Opaque pagination cursor from a previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.agents.list

puts(page)
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

`beta.agents.retrieve(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**GET** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agent_id: String`

- `version: Integer`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

  format: int32

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.retrieve("agent_011CZkYpogX7uDKUyvBTophP")

puts(beta_managed_agents_agent)
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

`beta.agents.update(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**POST** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agent_id: String`

- `description: String`

  Description. Omit to preserve; send empty string or null to clear.

  maxLength: 2048

- `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

  MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    minLength: 1, maxLength: 255

  - `type: :url`

  - `url: String`

    Endpoint URL for the MCP server.

    maxLength: 2048

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

  - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-8"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-7"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String = String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `effort: :low | :medium | :high | 2 more | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | 3 more`

      How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

      - `BetaManagedAgentsEffortLevel = :low | :medium | :high | 2 more`

        How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `multiagent: BetaManagedAgentsMultiagentParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `String = String`

    - `class BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: String`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `type: :agent`

      - `version: Integer`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsMultiagentSelfParams`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: :self`

    - `class BetaManagedAgentsAdvisorParams`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `model: String`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `type: :advisor`

  - `type: :coordinator`

- `name: String`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  maxLength: 256

- `skills: Array[BetaManagedAgentsSkillParams]`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

      minLength: 1, maxLength: 64

    - `type: :anthropic`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      minLength: 1, maxLength: 64

    - `type: :custom`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

- `system_: String`

  System prompt. Omit to preserve; send empty string or null to clear.

  maxLength: 100000

- `tools: Array[BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams]`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

  - `class BetaManagedAgentsAgentToolset20260401Params`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: :agent_toolset_20260401`

    - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

      Per-tool configuration overrides.

      - `class BetaManagedAgentsBashToolConfigParams`

        Configuration override for the bash tool.

        - `name: :bash`

          Must be "bash".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

        - `type: :bash`

      - `class BetaManagedAgentsEditToolConfigParams`

        Configuration override for the edit tool.

        - `name: :edit`

          Must be "edit".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :edit`

      - `class BetaManagedAgentsReadToolConfigParams`

        Configuration override for the read tool.

        - `name: :read`

          Must be "read".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :read`

      - `class BetaManagedAgentsWriteToolConfigParams`

        Configuration override for the write tool.

        - `name: :write`

          Must be "write".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :write`

      - `class BetaManagedAgentsGlobToolConfigParams`

        Configuration override for the glob tool.

        - `name: :glob`

          Must be "glob".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :glob`

      - `class BetaManagedAgentsGrepToolConfigParams`

        Configuration override for the grep tool.

        - `name: :grep`

          Must be "grep".

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :grep`

      - `class BetaManagedAgentsWebFetchToolConfigParams`

        Configuration override for the web_fetch tool.

        - `name: :web_fetch`

          Must be "web_fetch".

        - `allowed_domains: Array[String]`

          Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: Array[String]`

          Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `max_content_tokens: Integer`

          Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          format: int32

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :web_fetch`

      - `class BetaManagedAgentsWebSearchToolConfigParams`

        Configuration override for the web_search tool.

        - `name: :web_search`

          Must be "web_search".

        - `allowed_domains: Array[String]`

          Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: Array[String]`

          Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: bool`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

        - `type: :web_search`

        - `user_location: BetaManagedAgentsUserLocation`

          Approximate user location for search result localization.

          - `type: :approximate`

            Location precision. Only "approximate" is supported.

          - `city: String`

            City name.

            minLength: 1, maxLength: 255

          - `country: String`

            Two-letter ISO 3166-1 country code, uppercase.

          - `region: String`

            Region or state name.

            minLength: 1, maxLength: 255

          - `timezone: String`

            IANA timezone identifier, e.g. "America/Los_Angeles".

            minLength: 1, maxLength: 255

    - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

      Default configuration for all tools in a toolset.

      - `enabled: bool`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

  - `class BetaManagedAgentsMCPToolsetParams`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `mcp_server_name: String`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      minLength: 1, maxLength: 255

    - `type: :mcp_toolset`

    - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

      Per-tool configuration overrides.

      - `name: String`

        Name of the MCP tool to configure. 1-128 characters.

        minLength: 1, maxLength: 128

      - `enabled: bool`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

    - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

      Default configuration for all tools from an MCP server.

      - `enabled: bool`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool.

      minLength: 1

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema for custom tool input parameters.

      - `type: :object`

      - `properties: Hash[Symbol, untyped]`

      - `required: Array[String]`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      minLength: 1, maxLength: 128

    - `type: :custom`

- `version: Integer`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

  format: int32

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.update("agent_011CZkYpogX7uDKUyvBTophP")

puts(beta_managed_agents_agent)
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

`beta.agents.archive(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**POST** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agent_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.archive("agent_011CZkYpogX7uDKUyvBTophP")

puts(beta_managed_agents_agent)
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

- `class BetaManagedAgentsAdvisor`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

  - `model: String`

    The advisor model id.

  - `type: :advisor`

### Beta Managed Agents Agent

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

### Beta Managed Agents Agent Reference

- `class BetaManagedAgentsAgentReference`

  A resolved agent reference with a concrete version.

  - `id: String`

  - `type: :agent`

  - `version: Integer`

    format: int32

### Beta Managed Agents Agent Tool Config

- `BetaManagedAgentsAgentToolConfig = BetaManagedAgentsBashToolConfig | BetaManagedAgentsEditToolConfig | BetaManagedAgentsReadToolConfig | 5 more`

  Configuration for a specific agent tool.

  - `class BetaManagedAgentsBashToolConfig`

    Configuration for the bash tool.

    - `enabled: bool`

    - `name: :bash`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

    - `type: :bash`

  - `class BetaManagedAgentsEditToolConfig`

    Configuration for the edit tool.

    - `enabled: bool`

    - `name: :edit`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :edit`

  - `class BetaManagedAgentsReadToolConfig`

    Configuration for the read tool.

    - `enabled: bool`

    - `name: :read`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :read`

  - `class BetaManagedAgentsWriteToolConfig`

    Configuration for the write tool.

    - `enabled: bool`

    - `name: :write`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :write`

  - `class BetaManagedAgentsGlobToolConfig`

    Configuration for the glob tool.

    - `enabled: bool`

    - `name: :glob`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :glob`

  - `class BetaManagedAgentsGrepToolConfig`

    Configuration for the grep tool.

    - `enabled: bool`

    - `name: :grep`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :grep`

  - `class BetaManagedAgentsWebFetchToolConfig`

    Configuration for the web_fetch tool.

    - `enabled: bool`

    - `name: :web_fetch`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :web_fetch`

    - `allowed_domains: Array[String]`

    - `blocked_domains: Array[String]`

    - `max_content_tokens: Integer`

      format: int32

  - `class BetaManagedAgentsWebSearchToolConfig`

    Configuration for the web_search tool.

    - `enabled: bool`

    - `name: :web_search`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :web_search`

    - `allowed_domains: Array[String]`

    - `blocked_domains: Array[String]`

    - `user_location: BetaManagedAgentsUserLocation`

      Approximate user location for search result localization.

      - `type: :approximate`

        Location precision. Only "approximate" is supported.

      - `city: String`

        City name.

        minLength: 1, maxLength: 255

      - `country: String`

        Two-letter ISO 3166-1 country code, uppercase.

      - `region: String`

        Region or state name.

        minLength: 1, maxLength: 255

      - `timezone: String`

        IANA timezone identifier, e.g. "America/Los_Angeles".

        minLength: 1, maxLength: 255

### Beta Managed Agents Agent Tool Config Params

- `BetaManagedAgentsAgentToolConfigParams = BetaManagedAgentsBashToolConfigParams | BetaManagedAgentsEditToolConfigParams | BetaManagedAgentsReadToolConfigParams | 5 more`

  Configuration override for a specific tool within a toolset.

  - `class BetaManagedAgentsBashToolConfigParams`

    Configuration override for the bash tool.

    - `name: :bash`

      Must be "bash".

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

    - `type: :bash`

  - `class BetaManagedAgentsEditToolConfigParams`

    Configuration override for the edit tool.

    - `name: :edit`

      Must be "edit".

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :edit`

  - `class BetaManagedAgentsReadToolConfigParams`

    Configuration override for the read tool.

    - `name: :read`

      Must be "read".

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :read`

  - `class BetaManagedAgentsWriteToolConfigParams`

    Configuration override for the write tool.

    - `name: :write`

      Must be "write".

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :write`

  - `class BetaManagedAgentsGlobToolConfigParams`

    Configuration override for the glob tool.

    - `name: :glob`

      Must be "glob".

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :glob`

  - `class BetaManagedAgentsGrepToolConfigParams`

    Configuration override for the grep tool.

    - `name: :grep`

      Must be "grep".

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :grep`

  - `class BetaManagedAgentsWebFetchToolConfigParams`

    Configuration override for the web_fetch tool.

    - `name: :web_fetch`

      Must be "web_fetch".

    - `allowed_domains: Array[String]`

      Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

    - `blocked_domains: Array[String]`

      Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `max_content_tokens: Integer`

      Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

      format: int32

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :web_fetch`

  - `class BetaManagedAgentsWebSearchToolConfigParams`

    Configuration override for the web_search tool.

    - `name: :web_search`

      Must be "web_search".

    - `allowed_domains: Array[String]`

      Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

    - `blocked_domains: Array[String]`

      Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

    - `enabled: bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

    - `type: :web_search`

    - `user_location: BetaManagedAgentsUserLocation`

      Approximate user location for search result localization.

      - `type: :approximate`

        Location precision. Only "approximate" is supported.

      - `city: String`

        City name.

        minLength: 1, maxLength: 255

      - `country: String`

        Two-letter ISO 3166-1 country code, uppercase.

      - `region: String`

        Region or state name.

        minLength: 1, maxLength: 255

      - `timezone: String`

        IANA timezone identifier, e.g. "America/Los_Angeles".

        minLength: 1, maxLength: 255

### Beta Managed Agents Agent Toolset Default Config

- `class BetaManagedAgentsAgentToolsetDefaultConfig`

  Resolved default configuration for agent tools.

  - `enabled: bool`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

### Beta Managed Agents Agent Toolset Default Config Params

- `class BetaManagedAgentsAgentToolsetDefaultConfigParams`

  Default configuration for all tools in a toolset.

  - `enabled: bool`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

### Beta Managed Agents Agent Toolset20260401

- `class BetaManagedAgentsAgentToolset20260401`

  - `configs: Array[BetaManagedAgentsAgentToolConfig]`

    - `class BetaManagedAgentsBashToolConfig`

      Configuration for the bash tool.

      - `enabled: bool`

      - `name: :bash`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

      - `type: :bash`

    - `class BetaManagedAgentsEditToolConfig`

      Configuration for the edit tool.

      - `enabled: bool`

      - `name: :edit`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :edit`

    - `class BetaManagedAgentsReadToolConfig`

      Configuration for the read tool.

      - `enabled: bool`

      - `name: :read`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :read`

    - `class BetaManagedAgentsWriteToolConfig`

      Configuration for the write tool.

      - `enabled: bool`

      - `name: :write`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :write`

    - `class BetaManagedAgentsGlobToolConfig`

      Configuration for the glob tool.

      - `enabled: bool`

      - `name: :glob`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :glob`

    - `class BetaManagedAgentsGrepToolConfig`

      Configuration for the grep tool.

      - `enabled: bool`

      - `name: :grep`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :grep`

    - `class BetaManagedAgentsWebFetchToolConfig`

      Configuration for the web_fetch tool.

      - `enabled: bool`

      - `name: :web_fetch`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :web_fetch`

      - `allowed_domains: Array[String]`

      - `blocked_domains: Array[String]`

      - `max_content_tokens: Integer`

        format: int32

    - `class BetaManagedAgentsWebSearchToolConfig`

      Configuration for the web_search tool.

      - `enabled: bool`

      - `name: :web_search`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :web_search`

      - `allowed_domains: Array[String]`

      - `blocked_domains: Array[String]`

      - `user_location: BetaManagedAgentsUserLocation`

        Approximate user location for search result localization.

        - `type: :approximate`

          Location precision. Only "approximate" is supported.

        - `city: String`

          City name.

          minLength: 1, maxLength: 255

        - `country: String`

          Two-letter ISO 3166-1 country code, uppercase.

        - `region: String`

          Region or state name.

          minLength: 1, maxLength: 255

        - `timezone: String`

          IANA timezone identifier, e.g. "America/Los_Angeles".

          minLength: 1, maxLength: 255

  - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

    Resolved default configuration for agent tools.

    - `enabled: bool`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

  - `type: :agent_toolset_20260401`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `class BetaManagedAgentsAgentToolset20260401BashInput`

  Input payload for the `bash` tool of the
  `agent_toolset_20260401` toolset. All fields are optional;
  a normal invocation supplies `command`, while `restart=true`
  (with no `command`) reboots the runner-side bash session.

  - `command: String`

    Shell command to execute. Omit only when `restart` is true.

  - `restart: bool`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `timeout_ms: Integer`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

    minimum: 0

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `class BetaManagedAgentsAgentToolset20260401EditInput`

  Input payload for the `edit` tool. Performs a string
  replacement in the named file; by default `old_string` must
  occur exactly once.

  - `file_path: String`

    Path of the file to edit.

  - `new_string: String`

    Replacement text.

  - `old_string: String`

    Substring to find and replace.

  - `replace_all: bool`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `class BetaManagedAgentsAgentToolset20260401GlobInput`

  Input payload for the `glob` tool. Returns paths matching a
  doublestar glob pattern, newest first.

  - `pattern: String`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `path: String`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `class BetaManagedAgentsAgentToolset20260401GrepInput`

  Input payload for the `grep` tool. Searches file contents for
  a regular expression, returning matching lines.

  - `pattern: String`

    Regular expression to search for.

  - `path: String`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `class BetaManagedAgentsAgentToolset20260401Params`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `type: :agent_toolset_20260401`

  - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

    Per-tool configuration overrides.

    - `class BetaManagedAgentsBashToolConfigParams`

      Configuration override for the bash tool.

      - `name: :bash`

        Must be "bash".

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

          - `type: :always_allow`

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

          - `type: :always_ask`

      - `type: :bash`

    - `class BetaManagedAgentsEditToolConfigParams`

      Configuration override for the edit tool.

      - `name: :edit`

        Must be "edit".

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :edit`

    - `class BetaManagedAgentsReadToolConfigParams`

      Configuration override for the read tool.

      - `name: :read`

        Must be "read".

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :read`

    - `class BetaManagedAgentsWriteToolConfigParams`

      Configuration override for the write tool.

      - `name: :write`

        Must be "write".

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :write`

    - `class BetaManagedAgentsGlobToolConfigParams`

      Configuration override for the glob tool.

      - `name: :glob`

        Must be "glob".

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :glob`

    - `class BetaManagedAgentsGrepToolConfigParams`

      Configuration override for the grep tool.

      - `name: :grep`

        Must be "grep".

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :grep`

    - `class BetaManagedAgentsWebFetchToolConfigParams`

      Configuration override for the web_fetch tool.

      - `name: :web_fetch`

        Must be "web_fetch".

      - `allowed_domains: Array[String]`

        Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

      - `blocked_domains: Array[String]`

        Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `max_content_tokens: Integer`

        Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

        format: int32

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :web_fetch`

    - `class BetaManagedAgentsWebSearchToolConfigParams`

      Configuration override for the web_search tool.

      - `name: :web_search`

        Must be "web_search".

      - `allowed_domains: Array[String]`

        Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

      - `blocked_domains: Array[String]`

        Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

      - `enabled: bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

      - `type: :web_search`

      - `user_location: BetaManagedAgentsUserLocation`

        Approximate user location for search result localization.

        - `type: :approximate`

          Location precision. Only "approximate" is supported.

        - `city: String`

          City name.

          minLength: 1, maxLength: 255

        - `country: String`

          Two-letter ISO 3166-1 country code, uppercase.

        - `region: String`

          Region or state name.

          minLength: 1, maxLength: 255

        - `timezone: String`

          IANA timezone identifier, e.g. "America/Los_Angeles".

          minLength: 1, maxLength: 255

  - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

    Default configuration for all tools in a toolset.

    - `enabled: bool`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `class BetaManagedAgentsAgentToolset20260401ReadInput`

  Input payload for the `read` tool. Reads file contents
  relative to the runner's working directory (or absolute when
  the runner permits).

  - `file_path: String`

    Path of the file to read.

  - `view_range: Array[Integer]`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

    minItems: 2, maxItems: 2

### Beta Managed Agents Agent Toolset20260401 Write Input

- `class BetaManagedAgentsAgentToolset20260401WriteInput`

  Input payload for the `write` tool. Writes (overwriting) the
  entire file contents.

  - `content: String`

    Full file contents to write.

  - `file_path: String`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `class BetaManagedAgentsAlwaysAllowPolicy`

  Tool calls are automatically approved without user confirmation.

  - `type: :always_allow`

### Beta Managed Agents Always Ask Policy

- `class BetaManagedAgentsAlwaysAskPolicy`

  Tool calls require user confirmation before execution.

  - `type: :always_ask`

### Beta Managed Agents Anthropic Skill

- `class BetaManagedAgentsAnthropicSkill`

  A resolved Anthropic-managed skill.

  - `skill_id: String`

  - `type: :anthropic`

  - `version: String`

### Beta Managed Agents Anthropic Skill Params

- `class BetaManagedAgentsAnthropicSkillParams`

  An Anthropic-managed skill.

  - `skill_id: String`

    Identifier of the Anthropic skill (e.g., "xlsx").

    minLength: 1, maxLength: 64

  - `type: :anthropic`

  - `version: String`

    Version to pin. Defaults to latest if omitted.

    minLength: 1, maxLength: 64

### Beta Managed Agents Bash Tool Config

- `class BetaManagedAgentsBashToolConfig`

  Configuration for the bash tool.

  - `enabled: bool`

  - `name: :bash`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :bash`

### Beta Managed Agents Bash Tool Config Params

- `class BetaManagedAgentsBashToolConfigParams`

  Configuration override for the bash tool.

  - `name: :bash`

    Must be "bash".

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :bash`

### Beta Managed Agents Custom Skill

- `class BetaManagedAgentsCustomSkill`

  A resolved user-created custom skill.

  - `skill_id: String`

  - `type: :custom`

  - `version: String`

### Beta Managed Agents Custom Skill Params

- `class BetaManagedAgentsCustomSkillParams`

  A user-created custom skill.

  - `skill_id: String`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    minLength: 1, maxLength: 64

  - `type: :custom`

  - `version: String`

    Version to pin. Defaults to latest if omitted.

    minLength: 1, maxLength: 64

### Beta Managed Agents Custom Tool

- `class BetaManagedAgentsCustomTool`

  A custom tool as returned in API responses.

  - `description: String`

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `type: :object`

    - `properties: Hash[Symbol, untyped]`

    - `required: Array[String]`

  - `name: String`

  - `type: :custom`

### Beta Managed Agents Custom Tool Input Schema

- `class BetaManagedAgentsCustomToolInputSchema`

  JSON Schema for custom tool input parameters.

  - `type: :object`

  - `properties: Hash[Symbol, untyped]`

  - `required: Array[String]`

### Beta Managed Agents Custom Tool Params

- `class BetaManagedAgentsCustomToolParams`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: String`

    Description of what the tool does, shown to the agent to help it decide when to use the tool.

    minLength: 1

  - `input_schema: BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `type: :object`

    - `properties: Hash[Symbol, untyped]`

    - `required: Array[String]`

  - `name: String`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

    minLength: 1, maxLength: 128

  - `type: :custom`

### Beta Managed Agents Edit Tool Config

- `class BetaManagedAgentsEditToolConfig`

  Configuration for the edit tool.

  - `enabled: bool`

  - `name: :edit`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :edit`

### Beta Managed Agents Edit Tool Config Params

- `class BetaManagedAgentsEditToolConfigParams`

  Configuration override for the edit tool.

  - `name: :edit`

    Must be "edit".

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :edit`

### Beta Managed Agents Effort High

- `class BetaManagedAgentsEffortHigh`

  High effort. Favors reasoning depth.

  - `type: :high`

### Beta Managed Agents Effort Low

- `class BetaManagedAgentsEffortLow`

  Low effort. Favors latency over reasoning depth.

  - `type: :low`

### Beta Managed Agents Effort Max

- `class BetaManagedAgentsEffortMax`

  Maximum effort. Favors reasoning depth over latency.

  - `type: :max`

### Beta Managed Agents Effort Medium

- `class BetaManagedAgentsEffortMedium`

  Medium effort. Balances latency and reasoning depth.

  - `type: :medium`

### Beta Managed Agents Effort Xhigh

- `class BetaManagedAgentsEffortXhigh`

  Extra-high effort. Not all models accept this level.

  - `type: :xhigh`

### Beta Managed Agents Glob Tool Config

- `class BetaManagedAgentsGlobToolConfig`

  Configuration for the glob tool.

  - `enabled: bool`

  - `name: :glob`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :glob`

### Beta Managed Agents Glob Tool Config Params

- `class BetaManagedAgentsGlobToolConfigParams`

  Configuration override for the glob tool.

  - `name: :glob`

    Must be "glob".

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :glob`

### Beta Managed Agents Grep Tool Config

- `class BetaManagedAgentsGrepToolConfig`

  Configuration for the grep tool.

  - `enabled: bool`

  - `name: :grep`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :grep`

### Beta Managed Agents Grep Tool Config Params

- `class BetaManagedAgentsGrepToolConfigParams`

  Configuration override for the grep tool.

  - `name: :grep`

    Must be "grep".

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :grep`

### Beta Managed Agents MCP Server URL Definition

- `class BetaManagedAgentsMCPServerURLDefinition`

  URL-based MCP server connection as returned in API responses.

  - `name: String`

  - `type: :url`

  - `url: String`

### Beta Managed Agents MCP Tool Config

- `class BetaManagedAgentsMCPToolConfig`

  Resolved configuration for a specific MCP tool.

  - `enabled: bool`

  - `name: String`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

### Beta Managed Agents MCP Tool Config Params

- `class BetaManagedAgentsMCPToolConfigParams`

  Configuration override for a specific MCP tool.

  - `name: String`

    Name of the MCP tool to configure. 1-128 characters.

    minLength: 1, maxLength: 128

  - `enabled: bool`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

### Beta Managed Agents MCP Toolset

- `class BetaManagedAgentsMCPToolset`

  - `configs: Array[BetaManagedAgentsMCPToolConfig]`

    - `enabled: bool`

    - `name: String`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

    Resolved default configuration for all tools from an MCP server.

    - `enabled: bool`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

  - `mcp_server_name: String`

  - `type: :mcp_toolset`

### Beta Managed Agents MCP Toolset Default Config

- `class BetaManagedAgentsMCPToolsetDefaultConfig`

  Resolved default configuration for all tools from an MCP server.

  - `enabled: bool`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

### Beta Managed Agents MCP Toolset Default Config Params

- `class BetaManagedAgentsMCPToolsetDefaultConfigParams`

  Default configuration for all tools from an MCP server.

  - `enabled: bool`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

### Beta Managed Agents MCP Toolset Params

- `class BetaManagedAgentsMCPToolsetParams`

  Configuration for tools from an MCP server defined in `mcp_servers`.

  - `mcp_server_name: String`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

    minLength: 1, maxLength: 255

  - `type: :mcp_toolset`

  - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

    Per-tool configuration overrides.

    - `name: String`

      Name of the MCP tool to configure. 1-128 characters.

      minLength: 1, maxLength: 128

    - `enabled: bool`

      Whether this tool is enabled. Overrides the `default_config` setting.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

        - `type: :always_allow`

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

        - `type: :always_ask`

  - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

    Default configuration for all tools from an MCP server.

    - `enabled: bool`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `class BetaManagedAgentsAlwaysAllowPolicy`

        Tool calls are automatically approved without user confirmation.

      - `class BetaManagedAgentsAlwaysAskPolicy`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Model

- `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more | String`

  The model that will power your agent.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-sonnet-5"`

      High-performance model for coding and agents

    - `:"claude-fable-5"`

      Next generation of intelligence for the hardest knowledge work and coding problems

    - `:"claude-opus-5"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-opus-4-8"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-opus-4-7"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-opus-4-6"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-sonnet-4-6"`

      Best combination of speed and intelligence

    - `:"claude-haiku-4-5"`

      Fastest model with near-frontier intelligence

    - `:"claude-haiku-4-5-20251001"`

      Fastest model with near-frontier intelligence

    - `:"claude-opus-4-5"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-opus-4-5-20251101"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-sonnet-4-5"`

      High-performance model for agents and coding

    - `:"claude-sonnet-4-5-20250929"`

      High-performance model for agents and coding

  - `String = String`

### Beta Managed Agents Model Config

- `class BetaManagedAgentsModelConfig`

  Model identifier and configuration.

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-8"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-7"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String = String`

  - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

    How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

    - `class BetaManagedAgentsEffortLow`

      Low effort. Favors latency over reasoning depth.

      - `type: :low`

    - `class BetaManagedAgentsEffortMedium`

      Medium effort. Balances latency and reasoning depth.

      - `type: :medium`

    - `class BetaManagedAgentsEffortHigh`

      High effort. Favors reasoning depth.

      - `type: :high`

    - `class BetaManagedAgentsEffortXhigh`

      Extra-high effort. Not all models accept this level.

      - `type: :xhigh`

    - `class BetaManagedAgentsEffortMax`

      Maximum effort. Favors reasoning depth over latency.

      - `type: :max`

  - `inference_geo: String`

    Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Model Config Params

- `class BetaManagedAgentsModelConfigParams`

  An object that defines additional configuration control over model use

  - `id: BetaManagedAgentsModel`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-sonnet-5"`

        High-performance model for coding and agents

      - `:"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `:"claude-opus-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-8"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-7"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-6"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `:"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `:"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `:"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `String = String`

  - `effort: :low | :medium | :high | 2 more | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | 3 more`

    How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

    - `BetaManagedAgentsEffortLevel = :low | :medium | :high | 2 more`

      How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `class BetaManagedAgentsEffortLow`

      Low effort. Favors latency over reasoning depth.

      - `type: :low`

    - `class BetaManagedAgentsEffortMedium`

      Medium effort. Balances latency and reasoning depth.

      - `type: :medium`

    - `class BetaManagedAgentsEffortHigh`

      High effort. Favors reasoning depth.

      - `type: :high`

    - `class BetaManagedAgentsEffortXhigh`

      Extra-high effort. Not all models accept this level.

      - `type: :xhigh`

    - `class BetaManagedAgentsEffortMax`

      Maximum effort. Favors reasoning depth over latency.

      - `type: :max`

  - `inference_geo: String`

    Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

  - `speed: :standard | :fast`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `:standard`

    - `:fast`

### Beta Managed Agents Multiagent Coordinator

- `class BetaManagedAgentsMultiagentCoordinator`

  Resolved coordinator topology with a concrete agent roster.

  - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `class BetaManagedAgentsAgentReference`

      A resolved agent reference with a concrete version.

      - `id: String`

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `class BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: String`

        The advisor model id.

      - `type: :advisor`

  - `type: :coordinator`

### Beta Managed Agents Multiagent Coordinator Params

- `class BetaManagedAgentsMultiagentCoordinatorParams`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `String = String`

    - `class BetaManagedAgentsAgentParams`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: String`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `type: :agent`

      - `version: Integer`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsMultiagentSelfParams`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: :self`

    - `class BetaManagedAgentsAdvisorParams`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `model: String`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `type: :advisor`

  - `type: :coordinator`

### Beta Managed Agents Multiagent Self Params

- `class BetaManagedAgentsMultiagentSelfParams`

  Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

  - `type: :self`

### Beta Managed Agents Read Tool Config

- `class BetaManagedAgentsReadToolConfig`

  Configuration for the read tool.

  - `enabled: bool`

  - `name: :read`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :read`

### Beta Managed Agents Read Tool Config Params

- `class BetaManagedAgentsReadToolConfigParams`

  Configuration override for the read tool.

  - `name: :read`

    Must be "read".

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :read`

### Beta Managed Agents Session Thread Agent

- `class BetaManagedAgentsSessionThreadAgent`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `id: String`

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `version: Integer`

    format: int32

### Beta Managed Agents Skill Params

- `BetaManagedAgentsSkillParams = BetaManagedAgentsAnthropicSkillParams | BetaManagedAgentsCustomSkillParams`

  Skill to load in the session container.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

      minLength: 1, maxLength: 64

    - `type: :anthropic`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      minLength: 1, maxLength: 64

    - `type: :custom`

    - `version: String`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

### Beta Managed Agents URL MCP Server Params

- `class BetaManagedAgentsURLMCPServerParams`

  URL-based MCP server connection.

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    minLength: 1, maxLength: 255

  - `type: :url`

  - `url: String`

    Endpoint URL for the MCP server.

    maxLength: 2048

### Beta Managed Agents User Location

- `class BetaManagedAgentsUserLocation`

  Approximate user location for search result localization.

  - `type: :approximate`

    Location precision. Only "approximate" is supported.

  - `city: String`

    City name.

    minLength: 1, maxLength: 255

  - `country: String`

    Two-letter ISO 3166-1 country code, uppercase.

  - `region: String`

    Region or state name.

    minLength: 1, maxLength: 255

  - `timezone: String`

    IANA timezone identifier, e.g. "America/Los_Angeles".

    minLength: 1, maxLength: 255

### Beta Managed Agents Web Fetch Tool Config

- `class BetaManagedAgentsWebFetchToolConfig`

  Configuration for the web_fetch tool.

  - `enabled: bool`

  - `name: :web_fetch`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :web_fetch`

  - `allowed_domains: Array[String]`

  - `blocked_domains: Array[String]`

  - `max_content_tokens: Integer`

    format: int32

### Beta Managed Agents Web Fetch Tool Config Params

- `class BetaManagedAgentsWebFetchToolConfigParams`

  Configuration override for the web_fetch tool.

  - `name: :web_fetch`

    Must be "web_fetch".

  - `allowed_domains: Array[String]`

    Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

  - `blocked_domains: Array[String]`

    Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `max_content_tokens: Integer`

    Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

    format: int32

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :web_fetch`

### Beta Managed Agents Web Search Tool Config

- `class BetaManagedAgentsWebSearchToolConfig`

  Configuration for the web_search tool.

  - `enabled: bool`

  - `name: :web_search`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :web_search`

  - `allowed_domains: Array[String]`

  - `blocked_domains: Array[String]`

  - `user_location: BetaManagedAgentsUserLocation`

    Approximate user location for search result localization.

    - `type: :approximate`

      Location precision. Only "approximate" is supported.

    - `city: String`

      City name.

      minLength: 1, maxLength: 255

    - `country: String`

      Two-letter ISO 3166-1 country code, uppercase.

    - `region: String`

      Region or state name.

      minLength: 1, maxLength: 255

    - `timezone: String`

      IANA timezone identifier, e.g. "America/Los_Angeles".

      minLength: 1, maxLength: 255

### Beta Managed Agents Web Search Tool Config Params

- `class BetaManagedAgentsWebSearchToolConfigParams`

  Configuration override for the web_search tool.

  - `name: :web_search`

    Must be "web_search".

  - `allowed_domains: Array[String]`

    Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

  - `blocked_domains: Array[String]`

    Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :web_search`

  - `user_location: BetaManagedAgentsUserLocation`

    Approximate user location for search result localization.

    - `type: :approximate`

      Location precision. Only "approximate" is supported.

    - `city: String`

      City name.

      minLength: 1, maxLength: 255

    - `country: String`

      Two-letter ISO 3166-1 country code, uppercase.

    - `region: String`

      Region or state name.

      minLength: 1, maxLength: 255

    - `timezone: String`

      IANA timezone identifier, e.g. "America/Los_Angeles".

      minLength: 1, maxLength: 255

### Beta Managed Agents Write Tool Config

- `class BetaManagedAgentsWriteToolConfig`

  Configuration for the write tool.

  - `enabled: bool`

  - `name: :write`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :write`

### Beta Managed Agents Write Tool Config Params

- `class BetaManagedAgentsWriteToolConfigParams`

  Configuration override for the write tool.

  - `name: :write`

    Must be "write".

  - `enabled: bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `class BetaManagedAgentsAlwaysAllowPolicy`

      Tool calls are automatically approved without user confirmation.

      - `type: :always_allow`

    - `class BetaManagedAgentsAlwaysAskPolicy`

      Tool calls require user confirmation before execution.

      - `type: :always_ask`

  - `type: :write`

## Agents › Versions

### List Agent Versions

`beta.agents.versions.list(agent_id, **kwargs) -> PageCursor<BetaManagedAgentsAgent>`

**GET** `/v1/agents/{agent_id}/versions`

List Agent Versions

#### Parameters

- `agent_id: String`

- `limit: Integer`

  Maximum results per page. Default 20, maximum 100.

  format: int32

- `page: String`

  Opaque pagination cursor.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

#### Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: String`

    - `type: :url`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `:"claude-sonnet-5"`

          High-performance model for coding and agents

        - `:"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `:"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `:"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `:"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `:"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `:"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `:"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `String = String`

    - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: String`

        - `type: :agent`

        - `version: Integer`

          format: int32

      - `class BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: String`

          The advisor model id.

        - `type: :advisor`

    - `type: :coordinator`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: String`

      - `type: :anthropic`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: String`

      - `type: :custom`

      - `version: String`

  - `system_: String`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

          - `type: :bash`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :edit`

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :read`

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :write`

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :glob`

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :grep`

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_fetch`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `max_content_tokens: Integer`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: :web_search`

          - `allowed_domains: Array[String]`

          - `blocked_domains: Array[String]`

          - `user_location: BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: String`

              City name.

              minLength: 1, maxLength: 255

            - `country: String`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: String`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: String`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: :agent_toolset_20260401`

    - `class BetaManagedAgentsMCPToolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: String`

      - `type: :mcp_toolset`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: Hash[Symbol, untyped]`

        - `required: Array[String]`

      - `name: String`

      - `type: :custom`

  - `type: :agent`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.agents.versions.list("agent_011CZkYpogX7uDKUyvBTophP")

puts(page)
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
