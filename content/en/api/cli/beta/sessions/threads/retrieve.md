# Get Session Thread

`$ ant beta:sessions:threads retrieve`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

## Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_managed_agents_session_thread: object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    A session-resolved multiagent roster entry.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

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

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: object`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: "running" or "idle" or "rescheduling" or "terminated"`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

## Example

```bash
ant beta:sessions:threads retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
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
  }
}
```
