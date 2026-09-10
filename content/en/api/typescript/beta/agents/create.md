---
title: Create Agent
url: https://platform.claude.com/docs/en/api/typescript/beta/agents/create
---

# Create Agent

`client.beta.agents.create(params, options?): BetaManagedAgentsAgent`

**POST** `/v1/agents`

Create Agent

## Parameters

- `params: AgentCreateParams`

  - `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

    - `BetaManagedAgentsModel = "claude-fable-5-1" | "claude-sonnet-5" | "claude-fable-5" | 11 more | (string & {})`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5-1" | "claude-sonnet-5" | "claude-fable-5" | 11 more`

        - `"claude-fable-5-1"`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `"claude-sonnet-5"`

          High-performance model for coding and agents

        - `"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `(string & {})`

    - `BetaManagedAgentsModelConfigParams`

      An object that defines additional configuration control over model use

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `effort?: "low" | "medium" | "high" | 2 more | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | 3 more | null`

        How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

        - `"low" | "medium" | "high" | 2 more`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `BetaManagedAgentsEffortLow`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

        - `BetaManagedAgentsEffortMedium`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

        - `BetaManagedAgentsEffortHigh`

          High effort. Favors reasoning depth.

          - `type: "high"`

        - `BetaManagedAgentsEffortXhigh`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

        - `BetaManagedAgentsEffortMax`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

      - `inference_geo?: string | null`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `name: string`

    Body param: Human-readable name for the agent.

    minLength: 1, maxLength: 256

  - `description?: string | null`

    Body param: Description of what the agent does.

    maxLength: 2048

  - `mcp_servers?: Array<BetaManagedAgentsURLMCPServerParams>`

    Body param: MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `type: "url"`

    - `name: string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `url: string`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `metadata?: Record<string, string>`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `multiagent?: BetaManagedAgentsMultiagentParams | null`

    Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

    - `type: "coordinator"`

    - `agents: Array<BetaManagedAgentsMultiagentRosterEntryParams>`

      Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

      - `string`

      - `BetaManagedAgentsAgentParams`

        Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

        - `type: "agent"`

        - `id: string`

          The `agent` ID.

          minLength: 1, maxLength: 128

        - `version?: number`

          The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

          format: int32

      - `BetaManagedAgentsMultiagentSelfParams`

        Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

        - `type: "self"`

      - `BetaManagedAgentsAdvisorParams`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

        - `type: "advisor"`

        - `model: string`

          A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

          minLength: 1, maxLength: 256

  - `skills?: Array<BetaManagedAgentsSkillParams>`

    Body param: Skills available to the agent.

    - `BetaManagedAgentsAnthropicSkillParams`

      An Anthropic-managed skill.

      - `type: "anthropic"`

      - `skill_id: string`

        Identifier of the Anthropic skill (e.g., "xlsx").

        minLength: 1, maxLength: 64

      - `version?: string | null`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

    - `BetaManagedAgentsCustomSkillParams`

      A user-created custom skill.

      - `type: "custom"`

      - `skill_id: string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        minLength: 1, maxLength: 64

      - `version?: string | null`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

  - `system?: string | null`

    Body param: System prompt for the agent.

    maxLength: 100000

  - `tools?: Array<BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams>`

    Body param: Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

    - `BetaManagedAgentsAgentToolset20260401Params`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: "agent_toolset_20260401"`

      - `configs?: Array<BetaManagedAgentsAgentToolConfigParams>`

        Per-tool configuration overrides.

        - `BetaManagedAgentsBashToolConfigParams`

          Configuration override for the bash tool.

          - `type?: "bash"`

          - `name: "bash"`

            Must be "bash".

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type: "auto"`

        - `BetaManagedAgentsEditToolConfigParams`

          Configuration override for the edit tool.

          - `type?: "edit"`

          - `name: "edit"`

            Must be "edit".

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsReadToolConfigParams`

          Configuration override for the read tool.

          - `type?: "read"`

          - `name: "read"`

            Must be "read".

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsWriteToolConfigParams`

          Configuration override for the write tool.

          - `type?: "write"`

          - `name: "write"`

            Must be "write".

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsGlobToolConfigParams`

          Configuration override for the glob tool.

          - `type?: "glob"`

          - `name: "glob"`

            Must be "glob".

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsGrepToolConfigParams`

          Configuration override for the grep tool.

          - `type?: "grep"`

          - `name: "grep"`

            Must be "grep".

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsWebFetchToolConfigParams`

          Configuration override for the web_fetch tool.

          - `type?: "web_fetch"`

          - `name: "web_fetch"`

            Must be "web_fetch".

          - `allowed_domains?: Array<string>`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains?: Array<string>`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `max_content_tokens?: number | null`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsWebSearchToolConfigParams`

          Configuration override for the web_search tool.

          - `type?: "web_search"`

          - `name: "web_search"`

            Must be "web_search".

          - `allowed_domains?: Array<string>`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains?: Array<string>`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled?: boolean | null`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `user_location?: BetaManagedAgentsUserLocation | null`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city?: string | null`

              City name.

              minLength: 1, maxLength: 255

            - `country?: string | null`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region?: string | null`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone?: string | null`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config?: BetaManagedAgentsAgentToolsetDefaultConfigParams | null`

        Default configuration for all tools in a toolset.

        - `enabled?: boolean | null`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `BetaManagedAgentsMCPToolsetParams`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `type: "mcp_toolset"`

      - `mcp_server_name: string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `configs?: Array<BetaManagedAgentsMCPToolConfigParams>`

        Per-tool configuration overrides.

        - `name: string`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `enabled?: boolean | null`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `default_config?: BetaManagedAgentsMCPToolsetDefaultConfigParams | null`

        Default configuration for all tools from an MCP server.

        - `enabled?: boolean | null`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `BetaManagedAgentsCustomToolParams`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `type: "custom"`

      - `description: string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties?: Record<string, unknown> | null`

        - `required?: Array<string> | null`

      - `name: string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 42 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"user-profiles-2026-09-04"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

      - `"compact-2026-01-12"`

      - `"computer-use-2025-11-24"`

      - `"mcp-tunnels-2026-06-22"`

      - `"structured-outputs-2025-11-13"`

      - `"task-budgets-2026-03-13"`

      - `"thinking-display-updates-2026-08-18"`

      - `"ce-user-management-2026-07-13"`

      - `"mid-conversation-output-config-2026-07-01"`

      - `"thinking-binding-controls-2026-08-01"`

      - `"mid-conversation-system-clear-at-2026-08-21"`

  - `workspace_id?: string`

    Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `type: "agent"`

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `type: "url"`

    - `name: string`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5-1" | "claude-sonnet-5" | "claude-fable-5" | 11 more`

        - `"claude-fable-5-1"`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `"claude-sonnet-5"`

          High-performance model for coding and agents

        - `"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `(string & {})`

    - `effort?: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

      - `BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

      - `BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: "high"`

      - `BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

      - `BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

    - `inference_geo?: string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent | null`

    Resolved coordinator topology with a concrete agent roster.

    - `type: "coordinator"`

    - `agents: Array<BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor>`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `type: "agent"`

        - `id: string`

        - `version: number`

          format: int32

      - `BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `type: "advisor"`

        - `model: string`

          The advisor model id.

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `type: "anthropic"`

      - `skill_id: string`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `type: "custom"`

      - `skill_id: string`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `type: "agent_toolset_20260401"`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `type: "bash"`

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type: "auto"`

        - `BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `type: "edit"`

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `type: "read"`

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `type: "write"`

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `type: "glob"`

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `type: "grep"`

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `type: "web_fetch"`

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `allowed_domains?: Array<string>`

          - `blocked_domains?: Array<string>`

          - `max_content_tokens?: number | null`

            format: int32

        - `BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `type: "web_search"`

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `allowed_domains?: Array<string>`

          - `blocked_domains?: Array<string>`

          - `user_location?: BetaManagedAgentsUserLocation | null`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city?: string | null`

              City name.

              minLength: 1, maxLength: 255

            - `country?: string | null`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region?: string | null`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone?: string | null`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `BetaManagedAgentsMCPToolset`

      - `type: "mcp_toolset"`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `mcp_server_name: string`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `type: "custom"`

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties?: Record<string, unknown> | null`

        - `required?: Array<string> | null`

      - `name: string`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsAgent = await client.beta.agents.create({
  model: "claude-opus-5",
  name: "My First Agent"
});

console.log(betaManagedAgentsAgent.id);
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
