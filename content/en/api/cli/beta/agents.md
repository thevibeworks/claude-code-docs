---
title: Agents
url: https://platform.claude.com/docs/en/api/cli/beta/agents
---

# Agents

## Create Agent

`$ ant beta:agents create`

**post** `/v1/agents`

Create Agent

### Parameters

- `--model: BetaManagedAgentsModelConfigParams`

  Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

- `--name: string`

  Body param: Human-readable name for the agent.

- `--description: optional string`

  Body param: Description of what the agent does.

- `--mcp-server: optional array of BetaManagedAgentsURLMCPServerParams`

  Body param: MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--multiagent: optional object { agents, type }`

  Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

- `--skill: optional array of BetaManagedAgentsSkillParams`

  Body param: Skills available to the agent.

- `--system: optional string`

  Body param: System prompt for the agent.

- `--tool: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Body param: Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: object { id, effort, inference_geo, speed }`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `beta_managed_agents_effort_low: object { type }`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

          - `"low"`

      - `beta_managed_agents_effort_medium: object { type }`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

          - `"medium"`

      - `beta_managed_agents_effort_high: object { type }`

        High effort. Favors reasoning depth.

        - `type: "high"`

          - `"high"`

      - `beta_managed_agents_effort_xhigh: object { type }`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

          - `"xhigh"`

      - `beta_managed_agents_effort_max: object { type }`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

          - `"max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: object { agents, type }`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `beta_managed_agents_agent_reference: object { id, type, version }`

        A resolved agent reference with a concrete version.

        - `id: string`

        - `type: "agent"`

          - `"agent"`

        - `version: number`

      - `beta_managed_agents_advisor: object { model, type }`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

          - `"advisor"`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

          - `type: "bash"`

        - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

        - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object { type, city, country, 2 more }`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: optional string`

              Region or state name.

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { type, properties, required }`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```cli
ant beta:agents create \
  --api-key my-anthropic-api-key \
  --model '{id: claude-opus-5}' \
  --name 'My First Agent'
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

## List Agents

`$ ant beta:agents list`

**get** `/v1/agents`

List Agents

### Parameters

- `--created-at-gte: optional string`

  Query param: Return agents created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return agents created at or before this time (inclusive).

- `--include-archived: optional boolean`

  Query param: Include archived agents in results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListAgents: object { data, next_page }`

  Paginated list of agents.

  - `data: array of BetaManagedAgentsAgent`

    List of agents.

    - `id: string`

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `metadata: map[string]`

    - `model: object { id, effort, inference_geo, speed }`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `beta_managed_agents_effort_low: object { type }`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

            - `"low"`

        - `beta_managed_agents_effort_medium: object { type }`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `beta_managed_agents_effort_high: object { type }`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `beta_managed_agents_effort_xhigh: object { type }`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `beta_managed_agents_effort_max: object { type }`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `inference_geo: optional string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object { agents, type }`

      Resolved coordinator topology with a concrete agent roster.

      - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

        Agents the coordinator may spawn as session threads, each resolved to a specific version.

        - `beta_managed_agents_agent_reference: object { id, type, version }`

          A resolved agent reference with a concrete version.

          - `id: string`

          - `type: "agent"`

            - `"agent"`

          - `version: number`

        - `beta_managed_agents_advisor: object { model, type }`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

            - `"advisor"`

      - `type: "coordinator"`

        - `"coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the bash tool.

            - `enabled: boolean`

            - `name: "bash"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

                  - `"always_allow"`

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

                  - `"always_ask"`

            - `type: "bash"`

          - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the edit tool.

            - `enabled: boolean`

            - `name: "edit"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "edit"`

          - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the read tool.

            - `enabled: boolean`

            - `name: "read"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "read"`

          - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the write tool.

            - `enabled: boolean`

            - `name: "write"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "write"`

          - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the glob tool.

            - `enabled: boolean`

            - `name: "glob"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "glob"`

          - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the grep tool.

            - `enabled: boolean`

            - `name: "grep"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "grep"`

          - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

            Configuration for the web_fetch tool.

            - `enabled: boolean`

            - `name: "web_fetch"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "web_fetch"`

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

            - `max_content_tokens: optional number`

          - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

            Configuration for the web_search tool.

            - `enabled: boolean`

            - `name: "web_search"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "web_search"`

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

            - `user_location: optional object { type, city, country, 2 more }`

              Approximate user location for search result localization.

              - `type: "approximate"`

                Location precision. Only "approximate" is supported.

              - `city: optional string`

                City name.

              - `country: optional string`

                Two-letter ISO 3166-1 country code, uppercase.

              - `region: optional string`

                Region or state name.

              - `timezone: optional string`

                IANA timezone identifier, e.g. "America/Los_Angeles".

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { type, properties, required }`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `version: number`

      The agent's current version. Starts at 1 and increments when the agent is modified.

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:agents list \
  --api-key my-anthropic-api-key
```

#### Response

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

`$ ant beta:agents retrieve`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--version: optional number`

  Query param: Agent version. Omit for the most recent version. Must be at least 1 if specified.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: object { id, effort, inference_geo, speed }`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `beta_managed_agents_effort_low: object { type }`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

          - `"low"`

      - `beta_managed_agents_effort_medium: object { type }`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

          - `"medium"`

      - `beta_managed_agents_effort_high: object { type }`

        High effort. Favors reasoning depth.

        - `type: "high"`

          - `"high"`

      - `beta_managed_agents_effort_xhigh: object { type }`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

          - `"xhigh"`

      - `beta_managed_agents_effort_max: object { type }`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

          - `"max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: object { agents, type }`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `beta_managed_agents_agent_reference: object { id, type, version }`

        A resolved agent reference with a concrete version.

        - `id: string`

        - `type: "agent"`

          - `"agent"`

        - `version: number`

      - `beta_managed_agents_advisor: object { model, type }`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

          - `"advisor"`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

          - `type: "bash"`

        - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

        - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object { type, city, country, 2 more }`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: optional string`

              Region or state name.

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { type, properties, required }`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```cli
ant beta:agents retrieve \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
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

## Update Agent

`$ ant beta:agents update`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--description: optional string`

  Body param: Description. Omit to preserve; send empty string or null to clear.

- `--mcp-server: optional array of BetaManagedAgentsURLMCPServerParams`

  Body param: MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--model: optional BetaManagedAgentsModelConfigParams`

  Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

- `--multiagent: optional object { agents, type }`

  Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

- `--name: optional string`

  Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `--skill: optional array of BetaManagedAgentsSkillParams`

  Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear.

- `--system: optional string`

  Body param: System prompt. Omit to preserve; send empty string or null to clear.

- `--tool: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

- `--version: optional number`

  Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: object { id, effort, inference_geo, speed }`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `beta_managed_agents_effort_low: object { type }`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

          - `"low"`

      - `beta_managed_agents_effort_medium: object { type }`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

          - `"medium"`

      - `beta_managed_agents_effort_high: object { type }`

        High effort. Favors reasoning depth.

        - `type: "high"`

          - `"high"`

      - `beta_managed_agents_effort_xhigh: object { type }`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

          - `"xhigh"`

      - `beta_managed_agents_effort_max: object { type }`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

          - `"max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: object { agents, type }`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `beta_managed_agents_agent_reference: object { id, type, version }`

        A resolved agent reference with a concrete version.

        - `id: string`

        - `type: "agent"`

          - `"agent"`

        - `version: number`

      - `beta_managed_agents_advisor: object { model, type }`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

          - `"advisor"`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

          - `type: "bash"`

        - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

        - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object { type, city, country, 2 more }`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: optional string`

              Region or state name.

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { type, properties, required }`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```cli
ant beta:agents update \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
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

## Archive Agent

`$ ant beta:agents archive`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `--agent-id: string`

  Path parameter agent_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_agent: object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: object { id, effort, inference_geo, speed }`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `beta_managed_agents_effort_low: object { type }`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

          - `"low"`

      - `beta_managed_agents_effort_medium: object { type }`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

          - `"medium"`

      - `beta_managed_agents_effort_high: object { type }`

        High effort. Favors reasoning depth.

        - `type: "high"`

          - `"high"`

      - `beta_managed_agents_effort_xhigh: object { type }`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

          - `"xhigh"`

      - `beta_managed_agents_effort_max: object { type }`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

          - `"max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: object { agents, type }`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `beta_managed_agents_agent_reference: object { id, type, version }`

        A resolved agent reference with a concrete version.

        - `id: string`

        - `type: "agent"`

          - `"agent"`

        - `version: number`

      - `beta_managed_agents_advisor: object { model, type }`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

          - `"advisor"`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

          - `type: "bash"`

        - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

        - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object { type, city, country, 2 more }`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: optional string`

              Region or state name.

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { type, properties, required }`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```cli
ant beta:agents archive \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
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

## Domain Types

### Beta Managed Agents Advisor

- `beta_managed_agents_advisor: object { model, type }`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

  - `model: string`

    The advisor model id.

  - `type: "advisor"`

    - `"advisor"`

### Beta Managed Agents Agent

- `beta_managed_agents_agent: object { id, archived_at, created_at, 12 more }`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `metadata: map[string]`

  - `model: object { id, effort, inference_geo, speed }`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `beta_managed_agents_effort_low: object { type }`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

          - `"low"`

      - `beta_managed_agents_effort_medium: object { type }`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

          - `"medium"`

      - `beta_managed_agents_effort_high: object { type }`

        High effort. Favors reasoning depth.

        - `type: "high"`

          - `"high"`

      - `beta_managed_agents_effort_xhigh: object { type }`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

          - `"xhigh"`

      - `beta_managed_agents_effort_max: object { type }`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

          - `"max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: object { agents, type }`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `beta_managed_agents_agent_reference: object { id, type, version }`

        A resolved agent reference with a concrete version.

        - `id: string`

        - `type: "agent"`

          - `"agent"`

        - `version: number`

      - `beta_managed_agents_advisor: object { model, type }`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

          - `"advisor"`

    - `type: "coordinator"`

      - `"coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

          - `type: "bash"`

        - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

        - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object { type, city, country, 2 more }`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: optional string`

              Region or state name.

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { type, properties, required }`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Reference

- `beta_managed_agents_agent_reference: object { id, type, version }`

  A resolved agent reference with a concrete version.

  - `id: string`

  - `type: "agent"`

    - `"agent"`

  - `version: number`

### Beta Managed Agents Agent Tool Config

- `beta_managed_agents_agent_tool_config: BetaManagedAgentsBashToolConfig or BetaManagedAgentsEditToolConfig or BetaManagedAgentsReadToolConfig or 5 more`

  Configuration for a specific agent tool.

  - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

    Configuration for the bash tool.

    - `enabled: boolean`

    - `name: "bash"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

    - `type: "bash"`

  - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

    Configuration for the edit tool.

    - `enabled: boolean`

    - `name: "edit"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "edit"`

  - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

    Configuration for the read tool.

    - `enabled: boolean`

    - `name: "read"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "read"`

  - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

    Configuration for the write tool.

    - `enabled: boolean`

    - `name: "write"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "write"`

  - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

    Configuration for the glob tool.

    - `enabled: boolean`

    - `name: "glob"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "glob"`

  - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

    Configuration for the grep tool.

    - `enabled: boolean`

    - `name: "grep"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "grep"`

  - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

    Configuration for the web_fetch tool.

    - `enabled: boolean`

    - `name: "web_fetch"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "web_fetch"`

    - `allowed_domains: optional array of string`

    - `blocked_domains: optional array of string`

    - `max_content_tokens: optional number`

  - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

    Configuration for the web_search tool.

    - `enabled: boolean`

    - `name: "web_search"`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: "web_search"`

    - `allowed_domains: optional array of string`

    - `blocked_domains: optional array of string`

    - `user_location: optional object { type, city, country, 2 more }`

      Approximate user location for search result localization.

      - `type: "approximate"`

        Location precision. Only "approximate" is supported.

      - `city: optional string`

        City name.

      - `country: optional string`

        Two-letter ISO 3166-1 country code, uppercase.

      - `region: optional string`

        Region or state name.

      - `timezone: optional string`

        IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Agent Tool Config Params

- `beta_managed_agents_agent_tool_config_params: BetaManagedAgentsBashToolConfigParams or BetaManagedAgentsEditToolConfigParams or BetaManagedAgentsReadToolConfigParams or 5 more`

  Configuration override for a specific tool within a toolset.

  - `beta_managed_agents_bash_tool_config_params: object { name, enabled, permission_policy, type }`

    Configuration override for the bash tool.

    - `name: "bash"`

      Must be "bash".

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

    - `type: optional "bash"`

      - `"bash"`

  - `beta_managed_agents_edit_tool_config_params: object { name, enabled, permission_policy, type }`

    Configuration override for the edit tool.

    - `name: "edit"`

      Must be "edit".

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "edit"`

      - `"edit"`

  - `beta_managed_agents_read_tool_config_params: object { name, enabled, permission_policy, type }`

    Configuration override for the read tool.

    - `name: "read"`

      Must be "read".

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "read"`

      - `"read"`

  - `beta_managed_agents_write_tool_config_params: object { name, enabled, permission_policy, type }`

    Configuration override for the write tool.

    - `name: "write"`

      Must be "write".

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "write"`

      - `"write"`

  - `beta_managed_agents_glob_tool_config_params: object { name, enabled, permission_policy, type }`

    Configuration override for the glob tool.

    - `name: "glob"`

      Must be "glob".

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "glob"`

      - `"glob"`

  - `beta_managed_agents_grep_tool_config_params: object { name, enabled, permission_policy, type }`

    Configuration override for the grep tool.

    - `name: "grep"`

      Must be "grep".

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "grep"`

      - `"grep"`

  - `beta_managed_agents_web_fetch_tool_config_params: object { name, allowed_domains, blocked_domains, 4 more }`

    Configuration override for the web_fetch tool.

    - `name: "web_fetch"`

      Must be "web_fetch".

    - `allowed_domains: optional array of string`

      Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

    - `blocked_domains: optional array of string`

      Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `max_content_tokens: optional number`

      Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "web_fetch"`

      - `"web_fetch"`

  - `beta_managed_agents_web_search_tool_config_params: object { name, allowed_domains, blocked_domains, 4 more }`

    Configuration override for the web_search tool.

    - `name: "web_search"`

      Must be "web_search".

    - `allowed_domains: optional array of string`

      Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

    - `blocked_domains: optional array of string`

      Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

    - `enabled: optional boolean`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

    - `type: optional "web_search"`

      - `"web_search"`

    - `user_location: optional object { type, city, country, 2 more }`

      Approximate user location for search result localization.

      - `type: "approximate"`

        Location precision. Only "approximate" is supported.

      - `city: optional string`

        City name.

      - `country: optional string`

        Two-letter ISO 3166-1 country code, uppercase.

      - `region: optional string`

        Region or state name.

      - `timezone: optional string`

        IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Agent Toolset Default Config

- `beta_managed_agents_agent_toolset_default_config: object { enabled, permission_policy }`

  Resolved default configuration for agent tools.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset Default Config Params

- `beta_managed_agents_agent_toolset_default_config_params: object { enabled, permission_policy }`

  Default configuration for all tools in a toolset.

  - `enabled: optional boolean`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents Agent Toolset20260401

- `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

  - `configs: array of BetaManagedAgentsAgentToolConfig`

    - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

      Configuration for the bash tool.

      - `enabled: boolean`

      - `name: "bash"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

          - `type: "always_allow"`

            - `"always_allow"`

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

          - `type: "always_ask"`

            - `"always_ask"`

      - `type: "bash"`

    - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

      Configuration for the edit tool.

      - `enabled: boolean`

      - `name: "edit"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "edit"`

    - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

      Configuration for the read tool.

      - `enabled: boolean`

      - `name: "read"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "read"`

    - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

      Configuration for the write tool.

      - `enabled: boolean`

      - `name: "write"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "write"`

    - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

      Configuration for the glob tool.

      - `enabled: boolean`

      - `name: "glob"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "glob"`

    - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

      Configuration for the grep tool.

      - `enabled: boolean`

      - `name: "grep"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "grep"`

    - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

      Configuration for the web_fetch tool.

      - `enabled: boolean`

      - `name: "web_fetch"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "web_fetch"`

      - `allowed_domains: optional array of string`

      - `blocked_domains: optional array of string`

      - `max_content_tokens: optional number`

    - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

      Configuration for the web_search tool.

      - `enabled: boolean`

      - `name: "web_search"`

      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: "web_search"`

      - `allowed_domains: optional array of string`

      - `blocked_domains: optional array of string`

      - `user_location: optional object { type, city, country, 2 more }`

        Approximate user location for search result localization.

        - `type: "approximate"`

          Location precision. Only "approximate" is supported.

        - `city: optional string`

          City name.

        - `country: optional string`

          Two-letter ISO 3166-1 country code, uppercase.

        - `region: optional string`

          Region or state name.

        - `timezone: optional string`

          IANA timezone identifier, e.g. "America/Los_Angeles".

  - `default_config: object { enabled, permission_policy }`

    Resolved default configuration for agent tools.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `beta_managed_agents_agent_toolset20260401_bash_input: object { command, restart, timeout_ms }`

  Input payload for the `bash` tool of the
  `agent_toolset_20260401` toolset. All fields are optional;
  a normal invocation supplies `command`, while `restart=true`
  (with no `command`) reboots the runner-side bash session.

  - `command: optional string`

    Shell command to execute. Omit only when `restart` is true.

  - `restart: optional boolean`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `timeout_ms: optional number`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `beta_managed_agents_agent_toolset20260401_edit_input: object { file_path, new_string, old_string, replace_all }`

  Input payload for the `edit` tool. Performs a string
  replacement in the named file; by default `old_string` must
  occur exactly once.

  - `file_path: string`

    Path of the file to edit.

  - `new_string: string`

    Replacement text.

  - `old_string: string`

    Substring to find and replace.

  - `replace_all: optional boolean`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `beta_managed_agents_agent_toolset20260401_glob_input: object { pattern, path }`

  Input payload for the `glob` tool. Returns paths matching a
  doublestar glob pattern, newest first.

  - `pattern: string`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `path: optional string`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `beta_managed_agents_agent_toolset20260401_grep_input: object { pattern, path }`

  Input payload for the `grep` tool. Searches file contents for
  a regular expression, returning matching lines.

  - `pattern: string`

    Regular expression to search for.

  - `path: optional string`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `beta_managed_agents_agent_toolset20260401_params: object { type, configs, default_config }`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `type: "agent_toolset_20260401"`

    - `"agent_toolset_20260401"`

  - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

    Per-tool configuration overrides.

    - `beta_managed_agents_bash_tool_config_params: object { name, enabled, permission_policy, type }`

      Configuration override for the bash tool.

      - `name: "bash"`

        Must be "bash".

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

          - `type: "always_allow"`

            - `"always_allow"`

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

          - `type: "always_ask"`

            - `"always_ask"`

      - `type: optional "bash"`

        - `"bash"`

    - `beta_managed_agents_edit_tool_config_params: object { name, enabled, permission_policy, type }`

      Configuration override for the edit tool.

      - `name: "edit"`

        Must be "edit".

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "edit"`

        - `"edit"`

    - `beta_managed_agents_read_tool_config_params: object { name, enabled, permission_policy, type }`

      Configuration override for the read tool.

      - `name: "read"`

        Must be "read".

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "read"`

        - `"read"`

    - `beta_managed_agents_write_tool_config_params: object { name, enabled, permission_policy, type }`

      Configuration override for the write tool.

      - `name: "write"`

        Must be "write".

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "write"`

        - `"write"`

    - `beta_managed_agents_glob_tool_config_params: object { name, enabled, permission_policy, type }`

      Configuration override for the glob tool.

      - `name: "glob"`

        Must be "glob".

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "glob"`

        - `"glob"`

    - `beta_managed_agents_grep_tool_config_params: object { name, enabled, permission_policy, type }`

      Configuration override for the grep tool.

      - `name: "grep"`

        Must be "grep".

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "grep"`

        - `"grep"`

    - `beta_managed_agents_web_fetch_tool_config_params: object { name, allowed_domains, blocked_domains, 4 more }`

      Configuration override for the web_fetch tool.

      - `name: "web_fetch"`

        Must be "web_fetch".

      - `allowed_domains: optional array of string`

        Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

      - `blocked_domains: optional array of string`

        Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `max_content_tokens: optional number`

        Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "web_fetch"`

        - `"web_fetch"`

    - `beta_managed_agents_web_search_tool_config_params: object { name, allowed_domains, blocked_domains, 4 more }`

      Configuration override for the web_search tool.

      - `name: "web_search"`

        Must be "web_search".

      - `allowed_domains: optional array of string`

        Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

      - `blocked_domains: optional array of string`

        Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

      - `enabled: optional boolean`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

        Permission policy for tool execution.

        - `beta_managed_agents_always_allow_policy: object { type }`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object { type }`

          Tool calls require user confirmation before execution.

      - `type: optional "web_search"`

        - `"web_search"`

      - `user_location: optional object { type, city, country, 2 more }`

        Approximate user location for search result localization.

        - `type: "approximate"`

          Location precision. Only "approximate" is supported.

        - `city: optional string`

          City name.

        - `country: optional string`

          Two-letter ISO 3166-1 country code, uppercase.

        - `region: optional string`

          Region or state name.

        - `timezone: optional string`

          IANA timezone identifier, e.g. "America/Los_Angeles".

  - `default_config: optional object { enabled, permission_policy }`

    Default configuration for all tools in a toolset.

    - `enabled: optional boolean`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `beta_managed_agents_agent_toolset20260401_read_input: object { file_path, view_range }`

  Input payload for the `read` tool. Reads file contents
  relative to the runner's working directory (or absolute when
  the runner permits).

  - `file_path: string`

    Path of the file to read.

  - `view_range: optional array of number`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

### Beta Managed Agents Agent Toolset20260401 Write Input

- `beta_managed_agents_agent_toolset20260401_write_input: object { content, file_path }`

  Input payload for the `write` tool. Writes (overwriting) the
  entire file contents.

  - `content: string`

    Full file contents to write.

  - `file_path: string`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `beta_managed_agents_always_allow_policy: object { type }`

  Tool calls are automatically approved without user confirmation.

  - `type: "always_allow"`

    - `"always_allow"`

### Beta Managed Agents Always Ask Policy

- `beta_managed_agents_always_ask_policy: object { type }`

  Tool calls require user confirmation before execution.

  - `type: "always_ask"`

    - `"always_ask"`

### Beta Managed Agents Anthropic Skill

- `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

  A resolved Anthropic-managed skill.

  - `skill_id: string`

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: string`

### Beta Managed Agents Anthropic Skill Params

- `beta_managed_agents_anthropic_skill_params: object { skill_id, type, version }`

  An Anthropic-managed skill.

  - `skill_id: string`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `type: "anthropic"`

    - `"anthropic"`

  - `version: optional string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Bash Tool Config

- `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

  Configuration for the bash tool.

  - `enabled: boolean`

  - `name: "bash"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "bash"`

### Beta Managed Agents Bash Tool Config Params

- `beta_managed_agents_bash_tool_config_params: object { name, enabled, permission_policy, type }`

  Configuration override for the bash tool.

  - `name: "bash"`

    Must be "bash".

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "bash"`

    - `"bash"`

### Beta Managed Agents Custom Skill

- `beta_managed_agents_custom_skill: object { skill_id, type, version }`

  A resolved user-created custom skill.

  - `skill_id: string`

  - `type: "custom"`

    - `"custom"`

  - `version: string`

### Beta Managed Agents Custom Skill Params

- `beta_managed_agents_custom_skill_params: object { skill_id, type, version }`

  A user-created custom skill.

  - `skill_id: string`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `type: "custom"`

    - `"custom"`

  - `version: optional string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

  A custom tool as returned in API responses.

  - `description: string`

  - `input_schema: object { type, properties, required }`

    JSON Schema for custom tool input parameters.

    - `type: "object"`

    - `properties: optional map[unknown]`

    - `required: optional array of string`

  - `name: string`

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents Custom Tool Input Schema

- `beta_managed_agents_custom_tool_input_schema: object { type, properties, required }`

  JSON Schema for custom tool input parameters.

  - `type: "object"`

  - `properties: optional map[unknown]`

  - `required: optional array of string`

### Beta Managed Agents Custom Tool Params

- `beta_managed_agents_custom_tool_params: object { description, input_schema, name, type }`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `description: string`

    Description of what the tool does, shown to the agent to help it decide when to use the tool.

  - `input_schema: object { type, properties, required }`

    JSON Schema for custom tool input parameters.

    - `type: "object"`

    - `properties: optional map[unknown]`

    - `required: optional array of string`

  - `name: string`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `type: "custom"`

    - `"custom"`

### Beta Managed Agents Edit Tool Config

- `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

  Configuration for the edit tool.

  - `enabled: boolean`

  - `name: "edit"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "edit"`

### Beta Managed Agents Edit Tool Config Params

- `beta_managed_agents_edit_tool_config_params: object { name, enabled, permission_policy, type }`

  Configuration override for the edit tool.

  - `name: "edit"`

    Must be "edit".

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "edit"`

    - `"edit"`

### Beta Managed Agents Effort High

- `beta_managed_agents_effort_high: object { type }`

  High effort. Favors reasoning depth.

  - `type: "high"`

    - `"high"`

### Beta Managed Agents Effort Low

- `beta_managed_agents_effort_low: object { type }`

  Low effort. Favors latency over reasoning depth.

  - `type: "low"`

    - `"low"`

### Beta Managed Agents Effort Max

- `beta_managed_agents_effort_max: object { type }`

  Maximum effort. Favors reasoning depth over latency.

  - `type: "max"`

    - `"max"`

### Beta Managed Agents Effort Medium

- `beta_managed_agents_effort_medium: object { type }`

  Medium effort. Balances latency and reasoning depth.

  - `type: "medium"`

    - `"medium"`

### Beta Managed Agents Effort Xhigh

- `beta_managed_agents_effort_xhigh: object { type }`

  Extra-high effort. Not all models accept this level.

  - `type: "xhigh"`

    - `"xhigh"`

### Beta Managed Agents Glob Tool Config

- `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

  Configuration for the glob tool.

  - `enabled: boolean`

  - `name: "glob"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "glob"`

### Beta Managed Agents Glob Tool Config Params

- `beta_managed_agents_glob_tool_config_params: object { name, enabled, permission_policy, type }`

  Configuration override for the glob tool.

  - `name: "glob"`

    Must be "glob".

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "glob"`

    - `"glob"`

### Beta Managed Agents Grep Tool Config

- `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

  Configuration for the grep tool.

  - `enabled: boolean`

  - `name: "grep"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "grep"`

### Beta Managed Agents Grep Tool Config Params

- `beta_managed_agents_grep_tool_config_params: object { name, enabled, permission_policy, type }`

  Configuration override for the grep tool.

  - `name: "grep"`

    Must be "grep".

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "grep"`

    - `"grep"`

### Beta Managed Agents MCP Server URL Definition

- `beta_managed_agents_mcp_server_url_definition: object { name, type, url }`

  URL-based MCP server connection as returned in API responses.

  - `name: string`

  - `type: "url"`

    - `"url"`

  - `url: string`

### Beta Managed Agents MCP Tool Config

- `beta_managed_agents_mcp_tool_config: object { enabled, name, permission_policy }`

  Resolved configuration for a specific MCP tool.

  - `enabled: boolean`

  - `name: string`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Tool Config Params

- `beta_managed_agents_mcp_tool_config_params: object { name, enabled, permission_policy }`

  Configuration override for a specific MCP tool.

  - `name: string`

    Name of the MCP tool to configure. 1-128 characters.

  - `enabled: optional boolean`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset

- `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

  - `configs: array of BetaManagedAgentsMCPToolConfig`

    - `enabled: boolean`

    - `name: string`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: object { enabled, permission_policy }`

    Resolved default configuration for all tools from an MCP server.

    - `enabled: boolean`

    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

  - `mcp_server_name: string`

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

### Beta Managed Agents MCP Toolset Default Config

- `beta_managed_agents_mcp_toolset_default_config: object { enabled, permission_policy }`

  Resolved default configuration for all tools from an MCP server.

  - `enabled: boolean`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Default Config Params

- `beta_managed_agents_mcp_toolset_default_config_params: object { enabled, permission_policy }`

  Default configuration for all tools from an MCP server.

  - `enabled: optional boolean`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

### Beta Managed Agents MCP Toolset Params

- `beta_managed_agents_mcp_toolset_params: object { mcp_server_name, type, configs, default_config }`

  Configuration for tools from an MCP server defined in `mcp_servers`.

  - `mcp_server_name: string`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `type: "mcp_toolset"`

    - `"mcp_toolset"`

  - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

    Per-tool configuration overrides.

    - `name: string`

      Name of the MCP tool to configure. 1-128 characters.

    - `enabled: optional boolean`

      Whether this tool is enabled. Overrides the `default_config` setting.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

        - `type: "always_allow"`

          - `"always_allow"`

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

        - `type: "always_ask"`

          - `"always_ask"`

  - `default_config: optional object { enabled, permission_policy }`

    Default configuration for all tools from an MCP server.

    - `enabled: optional boolean`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

      Permission policy for tool execution.

      - `beta_managed_agents_always_allow_policy: object { type }`

        Tool calls are automatically approved without user confirmation.

      - `beta_managed_agents_always_ask_policy: object { type }`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Model Config

- `beta_managed_agents_model_config: object { id, effort, inference_geo, speed }`

  Model identifier and configuration.

  - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

    How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

    - `beta_managed_agents_effort_low: object { type }`

      Low effort. Favors latency over reasoning depth.

      - `type: "low"`

        - `"low"`

    - `beta_managed_agents_effort_medium: object { type }`

      Medium effort. Balances latency and reasoning depth.

      - `type: "medium"`

        - `"medium"`

    - `beta_managed_agents_effort_high: object { type }`

      High effort. Favors reasoning depth.

      - `type: "high"`

        - `"high"`

    - `beta_managed_agents_effort_xhigh: object { type }`

      Extra-high effort. Not all models accept this level.

      - `type: "xhigh"`

        - `"xhigh"`

    - `beta_managed_agents_effort_max: object { type }`

      Maximum effort. Favors reasoning depth over latency.

      - `type: "max"`

        - `"max"`

  - `inference_geo: optional string`

    Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Model Config Params

- `beta_managed_agents_model_config_params: object { id, effort, inference_geo, speed }`

  An object that defines additional configuration control over model use

  - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `effort: optional "low" or "medium" or "high" or 2 more or BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or 3 more`

    How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

    - `BetaManagedAgentsEffortLevel: "low" or "medium" or "high" or 2 more`

      How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `beta_managed_agents_effort_low: object { type }`

      Low effort. Favors latency over reasoning depth.

      - `type: "low"`

        - `"low"`

    - `beta_managed_agents_effort_medium: object { type }`

      Medium effort. Balances latency and reasoning depth.

      - `type: "medium"`

        - `"medium"`

    - `beta_managed_agents_effort_high: object { type }`

      High effort. Favors reasoning depth.

      - `type: "high"`

        - `"high"`

    - `beta_managed_agents_effort_xhigh: object { type }`

      Extra-high effort. Not all models accept this level.

      - `type: "xhigh"`

        - `"xhigh"`

    - `beta_managed_agents_effort_max: object { type }`

      Maximum effort. Favors reasoning depth over latency.

      - `type: "max"`

        - `"max"`

  - `inference_geo: optional string`

    Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Managed Agents Multiagent Coordinator

- `beta_managed_agents_multiagent_coordinator: object { agents, type }`

  Resolved coordinator topology with a concrete agent roster.

  - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `beta_managed_agents_agent_reference: object { id, type, version }`

      A resolved agent reference with a concrete version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `beta_managed_agents_advisor: object { model, type }`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

        - `"advisor"`

  - `type: "coordinator"`

    - `"coordinator"`

### Beta Managed Agents Multiagent Coordinator Params

- `beta_managed_agents_multiagent_coordinator_params: object { agents, type }`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: array of BetaManagedAgentsMultiagentRosterEntryParams`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `union_member_0: string`

    - `beta_managed_agents_agent_params: object { id, type, version }`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

      - `type: "agent"`

        - `"agent"`

      - `version: optional number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `beta_managed_agents_multiagent_self_params: object { type }`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: "self"`

        - `"self"`

    - `beta_managed_agents_advisor_params: object { model, type }`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `model: string`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

      - `type: "advisor"`

        - `"advisor"`

  - `type: "coordinator"`

    - `"coordinator"`

### Beta Managed Agents Multiagent Self Params

- `beta_managed_agents_multiagent_self_params: object { type }`

  Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

  - `type: "self"`

    - `"self"`

### Beta Managed Agents Read Tool Config

- `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

  Configuration for the read tool.

  - `enabled: boolean`

  - `name: "read"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "read"`

### Beta Managed Agents Read Tool Config Params

- `beta_managed_agents_read_tool_config_params: object { name, enabled, permission_policy, type }`

  Configuration override for the read tool.

  - `name: "read"`

    Must be "read".

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "read"`

    - `"read"`

### Beta Managed Agents Session Thread Agent

- `beta_managed_agents_session_thread_agent: object { id, description, mcp_servers, 7 more }`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `id: string`

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

      - `"url"`

    - `url: string`

  - `model: object { id, effort, inference_geo, speed }`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `beta_managed_agents_effort_low: object { type }`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

          - `"low"`

      - `beta_managed_agents_effort_medium: object { type }`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

          - `"medium"`

      - `beta_managed_agents_effort_high: object { type }`

        High effort. Favors reasoning depth.

        - `type: "high"`

          - `"high"`

      - `beta_managed_agents_effort_xhigh: object { type }`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

          - `"xhigh"`

      - `beta_managed_agents_effort_max: object { type }`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

          - `"max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

        - `"anthropic"`

      - `version: string`

    - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

        - `"custom"`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

                - `"always_allow"`

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

                - `"always_ask"`

          - `type: "bash"`

        - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

        - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object { type, city, country, 2 more }`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: optional string`

              Region or state name.

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

        - `"agent_toolset_20260401"`

    - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `default_config: object { enabled, permission_policy }`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object { type }`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object { type }`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

        - `"mcp_toolset"`

    - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: object { type, properties, required }`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

      - `type: "custom"`

        - `"custom"`

  - `type: "agent"`

    - `"agent"`

  - `version: number`

### Beta Managed Agents Skill Params

- `beta_managed_agents_skill_params: BetaManagedAgentsAnthropicSkillParams or BetaManagedAgentsCustomSkillParams`

  Skill to load in the session container.

  - `beta_managed_agents_anthropic_skill_params: object { skill_id, type, version }`

    An Anthropic-managed skill.

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `type: "anthropic"`

      - `"anthropic"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

  - `beta_managed_agents_custom_skill_params: object { skill_id, type, version }`

    A user-created custom skill.

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `type: "custom"`

      - `"custom"`

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `beta_managed_agents_url_mcp_server_params: object { name, type, url }`

  URL-based MCP server connection.

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `type: "url"`

    - `"url"`

  - `url: string`

    Endpoint URL for the MCP server.

### Beta Managed Agents User Location

- `beta_managed_agents_user_location: object { type, city, country, 2 more }`

  Approximate user location for search result localization.

  - `type: "approximate"`

    Location precision. Only "approximate" is supported.

  - `city: optional string`

    City name.

  - `country: optional string`

    Two-letter ISO 3166-1 country code, uppercase.

  - `region: optional string`

    Region or state name.

  - `timezone: optional string`

    IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Web Fetch Tool Config

- `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

  Configuration for the web_fetch tool.

  - `enabled: boolean`

  - `name: "web_fetch"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "web_fetch"`

  - `allowed_domains: optional array of string`

  - `blocked_domains: optional array of string`

  - `max_content_tokens: optional number`

### Beta Managed Agents Web Fetch Tool Config Params

- `beta_managed_agents_web_fetch_tool_config_params: object { name, allowed_domains, blocked_domains, 4 more }`

  Configuration override for the web_fetch tool.

  - `name: "web_fetch"`

    Must be "web_fetch".

  - `allowed_domains: optional array of string`

    Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

  - `blocked_domains: optional array of string`

    Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `max_content_tokens: optional number`

    Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "web_fetch"`

    - `"web_fetch"`

### Beta Managed Agents Web Search Tool Config

- `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

  Configuration for the web_search tool.

  - `enabled: boolean`

  - `name: "web_search"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "web_search"`

  - `allowed_domains: optional array of string`

  - `blocked_domains: optional array of string`

  - `user_location: optional object { type, city, country, 2 more }`

    Approximate user location for search result localization.

    - `type: "approximate"`

      Location precision. Only "approximate" is supported.

    - `city: optional string`

      City name.

    - `country: optional string`

      Two-letter ISO 3166-1 country code, uppercase.

    - `region: optional string`

      Region or state name.

    - `timezone: optional string`

      IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Web Search Tool Config Params

- `beta_managed_agents_web_search_tool_config_params: object { name, allowed_domains, blocked_domains, 4 more }`

  Configuration override for the web_search tool.

  - `name: "web_search"`

    Must be "web_search".

  - `allowed_domains: optional array of string`

    Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

  - `blocked_domains: optional array of string`

    Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "web_search"`

    - `"web_search"`

  - `user_location: optional object { type, city, country, 2 more }`

    Approximate user location for search result localization.

    - `type: "approximate"`

      Location precision. Only "approximate" is supported.

    - `city: optional string`

      City name.

    - `country: optional string`

      Two-letter ISO 3166-1 country code, uppercase.

    - `region: optional string`

      Region or state name.

    - `timezone: optional string`

      IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Write Tool Config

- `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

  Configuration for the write tool.

  - `enabled: boolean`

  - `name: "write"`

  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: "write"`

### Beta Managed Agents Write Tool Config Params

- `beta_managed_agents_write_tool_config_params: object { name, enabled, permission_policy, type }`

  Configuration override for the write tool.

  - `name: "write"`

    Must be "write".

  - `enabled: optional boolean`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

    Permission policy for tool execution.

    - `beta_managed_agents_always_allow_policy: object { type }`

      Tool calls are automatically approved without user confirmation.

      - `type: "always_allow"`

        - `"always_allow"`

    - `beta_managed_agents_always_ask_policy: object { type }`

      Tool calls require user confirmation before execution.

      - `type: "always_ask"`

        - `"always_ask"`

  - `type: optional "write"`

    - `"write"`

# Versions

## List Agent Versions

`$ ant beta:agents:versions list`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination cursor.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListAgentVersions: object { data, next_page }`

  Paginated list of agent versions.

  - `data: array of BetaManagedAgentsAgent`

    Agent versions.

    - `id: string`

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

    - `metadata: map[string]`

    - `model: object { id, effort, inference_geo, speed }`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `beta_managed_agents_effort_low: object { type }`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

            - `"low"`

        - `beta_managed_agents_effort_medium: object { type }`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `beta_managed_agents_effort_high: object { type }`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `beta_managed_agents_effort_xhigh: object { type }`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `beta_managed_agents_effort_max: object { type }`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `inference_geo: optional string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object { agents, type }`

      Resolved coordinator topology with a concrete agent roster.

      - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

        Agents the coordinator may spawn as session threads, each resolved to a specific version.

        - `beta_managed_agents_agent_reference: object { id, type, version }`

          A resolved agent reference with a concrete version.

          - `id: string`

          - `type: "agent"`

            - `"agent"`

          - `version: number`

        - `beta_managed_agents_advisor: object { model, type }`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

            - `"advisor"`

      - `type: "coordinator"`

        - `"coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

          - `"anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

          - `"custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `beta_managed_agents_bash_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the bash tool.

            - `enabled: boolean`

            - `name: "bash"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

                  - `"always_allow"`

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

                  - `"always_ask"`

            - `type: "bash"`

          - `beta_managed_agents_edit_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the edit tool.

            - `enabled: boolean`

            - `name: "edit"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "edit"`

          - `beta_managed_agents_read_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the read tool.

            - `enabled: boolean`

            - `name: "read"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "read"`

          - `beta_managed_agents_write_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the write tool.

            - `enabled: boolean`

            - `name: "write"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "write"`

          - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the glob tool.

            - `enabled: boolean`

            - `name: "glob"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "glob"`

          - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

            Configuration for the grep tool.

            - `enabled: boolean`

            - `name: "grep"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "grep"`

          - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

            Configuration for the web_fetch tool.

            - `enabled: boolean`

            - `name: "web_fetch"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "web_fetch"`

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

            - `max_content_tokens: optional number`

          - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

            Configuration for the web_search tool.

            - `enabled: boolean`

            - `name: "web_search"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object { type }`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object { type }`

                Tool calls require user confirmation before execution.

            - `type: "web_search"`

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

            - `user_location: optional object { type, city, country, 2 more }`

              Approximate user location for search result localization.

              - `type: "approximate"`

                Location precision. Only "approximate" is supported.

              - `city: optional string`

                City name.

              - `country: optional string`

                Two-letter ISO 3166-1 country code, uppercase.

              - `region: optional string`

                Region or state name.

              - `timezone: optional string`

                IANA timezone identifier, e.g. "America/Los_Angeles".

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

          - `"agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

        - `default_config: object { enabled, permission_policy }`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object { type }`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object { type }`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

          - `"mcp_toolset"`

      - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object { type, properties, required }`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

          - `"custom"`

    - `type: "agent"`

      - `"agent"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `version: number`

      The agent's current version. Starts at 1 and increments when the agent is modified.

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:agents:versions list \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
```

#### Response

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
