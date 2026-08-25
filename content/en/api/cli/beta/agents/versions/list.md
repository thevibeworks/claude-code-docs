# List Agent Versions

`$ ant beta:agents:versions list`

**GET** `/v1/agents/{agent_id}/versions`

List Agent Versions

## Parameters

- `--agent-id: string`

  Path param: Path parameter agent_id

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaManagedAgentsListAgentVersions: object`

  Paginated list of agent versions.

  - `data: array of BetaManagedAgentsAgent`

    Agent versions.

    - `id: string`

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `metadata: map[string]`

    - `model: object`

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

        - `beta_managed_agents_effort_low: object`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

        - `beta_managed_agents_effort_medium: object`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

        - `beta_managed_agents_effort_high: object`

          High effort. Favors reasoning depth.

          - `type: "high"`

        - `beta_managed_agents_effort_xhigh: object`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

        - `beta_managed_agents_effort_max: object`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

      - `inference_geo: optional string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with a concrete agent roster.

      - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

        Agents the coordinator may spawn as session threads, each resolved to a specific version.

        - `beta_managed_agents_agent_reference: object`

          A resolved agent reference with a concrete version.

          - `id: string`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

        - `skill_id: string`

        - `type: "anthropic"`

        - `version: string`

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

        - `skill_id: string`

        - `type: "custom"`

        - `version: string`

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

        - `configs: array of BetaManagedAgentsAgentToolConfig`

          - `beta_managed_agents_bash_tool_config: object`

            Configuration for the bash tool.

            - `enabled: boolean`

            - `name: "bash"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

            - `type: "bash"`

          - `beta_managed_agents_edit_tool_config: object`

            Configuration for the edit tool.

            - `enabled: boolean`

            - `name: "edit"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "edit"`

          - `beta_managed_agents_read_tool_config: object`

            Configuration for the read tool.

            - `enabled: boolean`

            - `name: "read"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "read"`

          - `beta_managed_agents_write_tool_config: object`

            Configuration for the write tool.

            - `enabled: boolean`

            - `name: "write"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "write"`

          - `beta_managed_agents_glob_tool_config: object`

            Configuration for the glob tool.

            - `enabled: boolean`

            - `name: "glob"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "glob"`

          - `beta_managed_agents_grep_tool_config: object`

            Configuration for the grep tool.

            - `enabled: boolean`

            - `name: "grep"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "grep"`

          - `beta_managed_agents_web_fetch_tool_config: object`

            Configuration for the web_fetch tool.

            - `enabled: boolean`

            - `name: "web_fetch"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "web_fetch"`

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

            - `max_content_tokens: optional number`

              format: int32

          - `beta_managed_agents_web_search_tool_config: object`

            Configuration for the web_search tool.

            - `enabled: boolean`

            - `name: "web_search"`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

            - `type: "web_search"`

            - `allowed_domains: optional array of string`

            - `blocked_domains: optional array of string`

            - `user_location: optional object`

              Approximate user location for search result localization.

              - `type: "approximate"`

                Location precision. Only "approximate" is supported.

              - `city: optional string`

                City name.

                minLength: 1, maxLength: 255

              - `country: optional string`

                Two-letter ISO 3166-1 country code, uppercase.

              - `region: optional string`

                Region or state name.

                minLength: 1, maxLength: 255

              - `timezone: optional string`

                IANA timezone identifier, e.g. "America/Los_Angeles".

                minLength: 1, maxLength: 255

        - `default_config: object`

          Resolved default configuration for agent tools.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

        - `type: "agent_toolset_20260401"`

      - `beta_managed_agents_mcp_toolset: object`

        - `configs: array of BetaManagedAgentsMCPToolConfig`

          - `enabled: boolean`

          - `name: string`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

        - `default_config: object`

          Resolved default configuration for all tools from an MCP server.

          - `enabled: boolean`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

        - `mcp_server_name: string`

        - `type: "mcp_toolset"`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

        - `description: string`

        - `input_schema: object`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

          - `properties: optional map[unknown]`

          - `required: optional array of string`

        - `name: string`

        - `type: "custom"`

    - `type: "agent"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `version: number`

      The agent's current version. Starts at 1 and increments when the agent is modified.

      format: int32

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

## Example

```bash
ant beta:agents:versions list \
  --api-key my-anthropic-api-key \
  --agent-id agent_011CZkYpogX7uDKUyvBTophP
```

### Response (200)

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
