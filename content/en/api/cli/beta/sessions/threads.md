---
title: Threads
url: https://platform.claude.com/docs/en/api/cli/beta/sessions/threads
---

# Threads

## List Session Threads

`$ ant beta:sessions:threads list`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum results per page. Defaults to 1000.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's `next_page`. Forward-only.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsListSessionThreads: object`

  Paginated list of threads within a `session`.

  - `data: optional array of BetaManagedAgentsSessionThread`

    Threads in the session, primary first then children in spawn order.

    - `type: "session_thread"`

    - `id: string`

      Unique identifier for this thread.

    - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

      The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

      - `beta_managed_agents_session_thread_agent: object`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `type: "agent"`

        - `id: string`

        - `description: string`

        - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

          - `type: "url"`

          - `name: string`

          - `url: string`

        - `model: object`

          Model identifier and configuration.

          - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

            - `type: "anthropic"`

            - `skill_id: string`

            - `version: string`

          - `beta_managed_agents_custom_skill: object`

            A resolved user-created custom skill.

            - `type: "custom"`

            - `skill_id: string`

            - `version: string`

        - `system: string`

        - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

          - `beta_managed_agents_agent_toolset20260401: object`

            - `type: "agent_toolset_20260401"`

            - `configs: array of BetaManagedAgentsAgentToolConfig`

              - `beta_managed_agents_bash_tool_config: object`

                Configuration for the bash tool.

                - `type: "bash"`

                - `enabled: boolean`

                - `name: "bash"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                    - `type: "always_allow"`

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                    - `type: "always_ask"`

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `type: "auto"`

              - `beta_managed_agents_edit_tool_config: object`

                Configuration for the edit tool.

                - `type: "edit"`

                - `enabled: boolean`

                - `name: "edit"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_read_tool_config: object`

                Configuration for the read tool.

                - `type: "read"`

                - `enabled: boolean`

                - `name: "read"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_write_tool_config: object`

                Configuration for the write tool.

                - `type: "write"`

                - `enabled: boolean`

                - `name: "write"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_glob_tool_config: object`

                Configuration for the glob tool.

                - `type: "glob"`

                - `enabled: boolean`

                - `name: "glob"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_grep_tool_config: object`

                Configuration for the grep tool.

                - `type: "grep"`

                - `enabled: boolean`

                - `name: "grep"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_web_fetch_tool_config: object`

                Configuration for the web_fetch tool.

                - `type: "web_fetch"`

                - `enabled: boolean`

                - `name: "web_fetch"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `allowed_domains: optional array of string`

                - `blocked_domains: optional array of string`

                - `max_content_tokens: optional number`

                  format: int32

              - `beta_managed_agents_web_search_tool_config: object`

                Configuration for the web_search tool.

                - `type: "web_search"`

                - `enabled: boolean`

                - `name: "web_search"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                  - `beta_managed_agents_auto_policy: object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `beta_managed_agents_mcp_toolset: object`

            - `type: "mcp_toolset"`

            - `configs: array of BetaManagedAgentsMCPToolConfig`

              - `enabled: boolean`

              - `name: string`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `default_config: object`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: boolean`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `mcp_server_name: string`

          - `beta_managed_agents_custom_tool: object`

            A custom tool as returned in API responses.

            - `type: "custom"`

            - `description: string`

            - `input_schema: object`

              JSON Schema for custom tool input parameters.

              - `type: "object"`

              - `properties: optional map[unknown]`

              - `required: optional array of string`

            - `name: string`

        - `version: number`

          format: int32

      - `beta_managed_agents_advisor: object`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `type: "advisor"`

        - `model: string`

          The advisor model id.

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

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```bash
ant beta:sessions:threads list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

#### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Session Thread

`$ ant beta:sessions:threads retrieve`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_session_thread: object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: "session_thread"`

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: "agent"`

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `type: "anthropic"`

          - `skill_id: string`

          - `version: string`

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

          - `type: "custom"`

          - `skill_id: string`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

          - `type: "agent_toolset_20260401"`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `beta_managed_agents_bash_tool_config: object`

              Configuration for the bash tool.

              - `type: "bash"`

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: "auto"`

            - `beta_managed_agents_edit_tool_config: object`

              Configuration for the edit tool.

              - `type: "edit"`

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_read_tool_config: object`

              Configuration for the read tool.

              - `type: "read"`

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_write_tool_config: object`

              Configuration for the write tool.

              - `type: "write"`

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_glob_tool_config: object`

              Configuration for the glob tool.

              - `type: "glob"`

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_grep_tool_config: object`

              Configuration for the grep tool.

              - `type: "grep"`

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_web_fetch_tool_config: object`

              Configuration for the web_fetch tool.

              - `type: "web_fetch"`

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number`

                format: int32

            - `beta_managed_agents_web_search_tool_config: object`

              Configuration for the web_search tool.

              - `type: "web_search"`

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `beta_managed_agents_mcp_toolset: object`

          - `type: "mcp_toolset"`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: object`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: string`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

          - `type: "custom"`

          - `description: string`

          - `input_schema: object`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown]`

            - `required: optional array of string`

          - `name: string`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: "advisor"`

      - `model: string`

        The advisor model id.

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

### Example

```bash
ant beta:sessions:threads retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

#### Response (200)

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

## Archive Session Thread

`$ ant beta:sessions:threads archive`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `beta_managed_agents_session_thread: object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: "session_thread"`

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: "agent"`

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `type: "anthropic"`

          - `skill_id: string`

          - `version: string`

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

          - `type: "custom"`

          - `skill_id: string`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

          - `type: "agent_toolset_20260401"`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `beta_managed_agents_bash_tool_config: object`

              Configuration for the bash tool.

              - `type: "bash"`

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: "auto"`

            - `beta_managed_agents_edit_tool_config: object`

              Configuration for the edit tool.

              - `type: "edit"`

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_read_tool_config: object`

              Configuration for the read tool.

              - `type: "read"`

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_write_tool_config: object`

              Configuration for the write tool.

              - `type: "write"`

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_glob_tool_config: object`

              Configuration for the glob tool.

              - `type: "glob"`

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_grep_tool_config: object`

              Configuration for the grep tool.

              - `type: "grep"`

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_web_fetch_tool_config: object`

              Configuration for the web_fetch tool.

              - `type: "web_fetch"`

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number`

                format: int32

            - `beta_managed_agents_web_search_tool_config: object`

              Configuration for the web_search tool.

              - `type: "web_search"`

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `beta_managed_agents_mcp_toolset: object`

          - `type: "mcp_toolset"`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: object`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: string`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

          - `type: "custom"`

          - `description: string`

          - `input_schema: object`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown]`

            - `required: optional array of string`

          - `name: string`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: "advisor"`

      - `model: string`

        The advisor model id.

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

### Example

```bash
ant beta:sessions:threads archive \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Session Thread

- `beta_managed_agents_session_thread: object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: "session_thread"`

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: "agent"`

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `type: "anthropic"`

          - `skill_id: string`

          - `version: string`

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

          - `type: "custom"`

          - `skill_id: string`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

          - `type: "agent_toolset_20260401"`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `beta_managed_agents_bash_tool_config: object`

              Configuration for the bash tool.

              - `type: "bash"`

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: "auto"`

            - `beta_managed_agents_edit_tool_config: object`

              Configuration for the edit tool.

              - `type: "edit"`

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_read_tool_config: object`

              Configuration for the read tool.

              - `type: "read"`

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_write_tool_config: object`

              Configuration for the write tool.

              - `type: "write"`

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_glob_tool_config: object`

              Configuration for the glob tool.

              - `type: "glob"`

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_grep_tool_config: object`

              Configuration for the grep tool.

              - `type: "grep"`

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `beta_managed_agents_web_fetch_tool_config: object`

              Configuration for the web_fetch tool.

              - `type: "web_fetch"`

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number`

                format: int32

            - `beta_managed_agents_web_search_tool_config: object`

              Configuration for the web_search tool.

              - `type: "web_search"`

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                - `beta_managed_agents_auto_policy: object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `beta_managed_agents_mcp_toolset: object`

          - `type: "mcp_toolset"`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: object`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

              - `beta_managed_agents_auto_policy: object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: string`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

          - `type: "custom"`

          - `description: string`

          - `input_schema: object`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown]`

            - `required: optional array of string`

          - `name: string`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: "advisor"`

      - `model: string`

        The advisor model id.

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

### Beta Managed Agents Session Thread Stats

- `beta_managed_agents_session_thread_stats: object`

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

### Beta Managed Agents Session Thread Status

- `beta_managed_agents_session_thread_status: "running" or "idle" or "rescheduling" or "terminated"`

  SessionThreadStatus enum

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `beta_managed_agents_session_thread_usage: object`

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

### Beta Managed Agents Stream Session Thread Events

- `beta_managed_agents_stream_session_thread_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in a single thread's stream.

  - `beta_managed_agents_user_message_event: object`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_user_interrupt_event: object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `beta_managed_agents_user_tool_confirmation_event: object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `beta_managed_agents_user_custom_tool_result_event: object`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

        - `type: "search_result"`

        - `citations: object`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `beta_managed_agents_agent_custom_tool_use_event: object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `beta_managed_agents_agent_message_event: object`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_agent_thinking_event: object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_agent_mcp_tool_use_event: object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `beta_managed_agents_agent_tool_evaluation_always_allow: object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `beta_managed_agents_agent_tool_evaluation_always_ask: object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `beta_managed_agents_agent_tool_evaluation_auto: object`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermissionAllow or BetaManagedAgentsAgentAutoEvaluatedPermissionAsk or BetaManagedAgentsAgentAutoEvaluatedPermissionDeny`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `beta_managed_agents_agent_auto_evaluated_permission_allow: object`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `beta_managed_agents_agent_auto_evaluated_permission_ask: object`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `beta_managed_agents_agent_auto_evaluated_permission_deny: object`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_mcp_tool_result_event: object`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `beta_managed_agents_agent_tool_evaluation_always_allow: object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

      - `beta_managed_agents_agent_tool_evaluation_always_ask: object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

      - `beta_managed_agents_agent_tool_evaluation_auto: object`

        The resolved permission_policy was auto: the server judged this invocation individually.

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_tool_result_event: object`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_message_received_event: object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: "agent.thread_message_received"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `beta_managed_agents_agent_thread_message_sent_event: object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `beta_managed_agents_agent_thread_context_compacted_event: object`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_error_event: object`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      - `beta_managed_agents_unknown_error: object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `beta_managed_agents_model_overloaded_error: object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_model_rate_limited_error: object`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_model_request_failed_error: object`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_mcp_connection_failed_error: object`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_mcp_authentication_failed_error: object`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_billing_error: object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_credential_host_unreachable_error: object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_status_rescheduled_event: object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_status_running_event: object`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_status_idle_event: object`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

  - `beta_managed_agents_session_status_terminated_event: object`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_thread_created_event: object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

  - `beta_managed_agents_span_outcome_evaluation_start_event: object`

    Emitted when an outcome evaluation cycle begins.

    - `type: "span.outcome_evaluation_start"`

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_span_outcome_evaluation_end_event: object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: "span.outcome_evaluation_end"`

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `beta_managed_agents_span_model_request_start_event: object`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_span_model_request_end_event: object`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: "span.outcome_evaluation_ongoing"`

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_user_define_outcome_event: object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric: object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `beta_managed_agents_text_rubric: object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `beta_managed_agents_session_deleted_event: object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_thread_status_running_event: object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `beta_managed_agents_session_thread_status_idle_event: object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `beta_managed_agents_session_thread_status_terminated_event: object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `beta_managed_agents_user_tool_result_event: object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `beta_managed_agents_session_thread_status_rescheduled_event: object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `beta_managed_agents_session_updated_event: object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent: optional object`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: "agent"`

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: "coordinator"`

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `beta_managed_agents_session_thread_agent: object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: "agent"`

            - `id: string`

            - `description: string`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `type: "url"`

              - `name: string`

              - `url: string`

            - `model: object`

              Model identifier and configuration.

              - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

                The model that will power your agent.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

              - `inference_geo: optional string`

                Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

              - `speed: optional "standard" or "fast"`

                Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `beta_managed_agents_anthropic_skill: object`

                A resolved Anthropic-managed skill.

                - `type: "anthropic"`

                - `skill_id: string`

                - `version: string`

              - `beta_managed_agents_custom_skill: object`

                A resolved user-created custom skill.

                - `type: "custom"`

                - `skill_id: string`

                - `version: string`

            - `system: string`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `beta_managed_agents_agent_toolset20260401: object`

                - `type: "agent_toolset_20260401"`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `beta_managed_agents_bash_tool_config: object`

                    Configuration for the bash tool.

                    - `type: "bash"`

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: "auto"`

                  - `beta_managed_agents_edit_tool_config: object`

                    Configuration for the edit tool.

                    - `type: "edit"`

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_read_tool_config: object`

                    Configuration for the read tool.

                    - `type: "read"`

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_write_tool_config: object`

                    Configuration for the write tool.

                    - `type: "write"`

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_glob_tool_config: object`

                    Configuration for the glob tool.

                    - `type: "glob"`

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_grep_tool_config: object`

                    Configuration for the grep tool.

                    - `type: "grep"`

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_web_fetch_tool_config: object`

                    Configuration for the web_fetch tool.

                    - `type: "web_fetch"`

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number`

                      format: int32

                  - `beta_managed_agents_web_search_tool_config: object`

                    Configuration for the web_search tool.

                    - `type: "web_search"`

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                    - `beta_managed_agents_auto_policy: object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_mcp_toolset: object`

                - `type: "mcp_toolset"`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                    - `beta_managed_agents_auto_policy: object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: object`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                    - `beta_managed_agents_auto_policy: object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: string`

              - `beta_managed_agents_custom_tool: object`

                A custom tool as returned in API responses.

                - `type: "custom"`

                - `description: string`

                - `input_schema: object`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown]`

                  - `required: optional array of string`

                - `name: string`

            - `version: number`

              format: int32

          - `beta_managed_agents_advisor: object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: "advisor"`

            - `model: string`

              The advisor model id.

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

        - `beta_managed_agents_mcp_toolset: object`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

      - `version: number`

        format: int32

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: "limit"`

      - `max_list_cost: object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `beta_managed_agents_start_event: object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_start"`

    - `event: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `beta_managed_agents_agent_message_preview: object`

        - `type: "agent.message"`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `beta_managed_agents_agent_thinking_preview: object`

        - `type: "agent.thinking"`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `beta_managed_agents_delta_event: object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_delta"`

    - `delta: object`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: "content_delta"`

      - `content: object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `beta_managed_agents_system_message_event: object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_usage_event: object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: object`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

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

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: "limit"`

      - `max_list_cost: object`

        A monetary amount in a specific currency.

## Threads › Events

### List Session Thread Events

`$ ant beta:sessions:threads:events list`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsListSessionThreadEvents: object`

  Paginated list of events for a single thread within a `session`.

  - `data: optional array of BetaManagedAgentsSessionEvent`

    Events for the thread, ordered by `processed_at`.

    - `beta_managed_agents_user_message_event: object`

      A user message event in the session conversation.

      - `type: "user.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: "image"`

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: "document"`

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `type: "base64"`

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `type: "text"`

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `type: "file"`

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_user_interrupt_event: object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `type: "user.interrupt"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `beta_managed_agents_user_tool_confirmation_event: object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `type: "user.tool_confirmation"`

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `beta_managed_agents_user_custom_tool_result_event: object`

      Event sent by the client providing the result of a custom tool execution.

      - `type: "user.custom_tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

          - `type: "search_result"`

          - `citations: object`

            Citation settings for a search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `type: "text"`

            - `text: string`

              The text content.

              minLength: 1

          - `source: string`

            The URL source of the search result.

            minLength: 1

          - `title: string`

            The title of the search result.

            minLength: 1

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `beta_managed_agents_agent_custom_tool_use_event: object`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `type: "agent.custom_tool_use"`

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the custom tool being called.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

    - `beta_managed_agents_agent_message_event: object`

      An agent response event in the session conversation.

      - `type: "agent.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

        Array of text blocks comprising the agent response.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_agent_thinking_event: object`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `type: "agent.thinking"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_agent_mcp_tool_use_event: object`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `type: "agent.mcp_tool_use"`

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `mcp_server_name: string`

        Name of the MCP server providing the tool.

      - `name: string`

        Name of the MCP tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

      - `evaluation: optional BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

        Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

        - `beta_managed_agents_agent_tool_evaluation_always_allow: object`

          The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

          - `type: "always_allow"`

        - `beta_managed_agents_agent_tool_evaluation_always_ask: object`

          The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

          - `type: "always_ask"`

        - `beta_managed_agents_agent_tool_evaluation_auto: object`

          The resolved permission_policy was auto: the server judged this invocation individually.

          - `type: "auto"`

          - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermissionAllow or BetaManagedAgentsAgentAutoEvaluatedPermissionAsk or BetaManagedAgentsAgentAutoEvaluatedPermissionDeny`

            The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

            - `beta_managed_agents_agent_auto_evaluated_permission_allow: object`

              The server judged the invocation safe to execute without client approval.

              - `type: "allow"`

            - `beta_managed_agents_agent_auto_evaluated_permission_ask: object`

              The server reached no judgement; the invocation is held for client approval.

              - `type: "ask"`

              - `reason_code: string`

                The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

                maxLength: 64

            - `beta_managed_agents_agent_auto_evaluated_permission_deny: object`

              The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

              - `type: "deny"`

              - `reason_code: string`

                The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

                maxLength: 64

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `beta_managed_agents_agent_mcp_tool_result_event: object`

      Event representing the result of an MCP tool execution.

      - `type: "agent.mcp_tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `mcp_tool_use_id: string`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_tool_use_event: object`

      Event emitted when the agent invokes a built-in agent tool.

      - `type: "agent.tool_use"`

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the agent tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

      - `evaluation: optional BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

        Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

        - `beta_managed_agents_agent_tool_evaluation_always_allow: object`

          The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `beta_managed_agents_agent_tool_evaluation_always_ask: object`

          The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `beta_managed_agents_agent_tool_evaluation_auto: object`

          The resolved permission_policy was auto: the server judged this invocation individually.

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `beta_managed_agents_agent_tool_result_event: object`

      Event representing the result of an agent tool execution.

      - `type: "agent.tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to.

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_thread_message_received_event: object`

      Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

      - `type: "agent.thread_message_received"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Message content blocks.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `from_session_thread_id: string`

        Public `sthr_` ID of the thread that sent the message.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `from_agent_name: optional string`

        Name of the callable agent this message came from. Absent when received from the primary agent.

    - `beta_managed_agents_agent_thread_message_sent_event: object`

      Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

      - `type: "agent.thread_message_sent"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Message content blocks.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `to_session_thread_id: string`

        Public `sthr_` ID of the thread the message was sent to.

      - `to_agent_name: optional string`

        Name of the callable agent this message was sent to. Absent when sent to the primary agent.

    - `beta_managed_agents_agent_thread_context_compacted_event: object`

      Indicates that context compaction (summarization) occurred during the session.

      - `type: "agent.thread_context_compacted"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_error_event: object`

      An error event indicating a problem occurred during session execution.

      - `type: "session.error"`

      - `id: string`

        Unique identifier for this event.

      - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

        - `beta_managed_agents_unknown_error: object`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `type: "unknown_error"`

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

        - `beta_managed_agents_model_overloaded_error: object`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `type: "model_overloaded_error"`

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

        - `beta_managed_agents_model_rate_limited_error: object`

          The model request was rate-limited.

          - `type: "model_rate_limited_error"`

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

        - `beta_managed_agents_model_request_failed_error: object`

          A model request failed for a reason other than overload or rate-limiting.

          - `type: "model_request_failed_error"`

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

        - `beta_managed_agents_mcp_connection_failed_error: object`

          Failed to connect to an MCP server.

          - `type: "mcp_connection_failed_error"`

          - `mcp_server_name: string`

            Name of the MCP server that failed to connect.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

        - `beta_managed_agents_mcp_authentication_failed_error: object`

          Authentication to an MCP server failed.

          - `type: "mcp_authentication_failed_error"`

          - `mcp_server_name: string`

            Name of the MCP server that failed authentication.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

        - `beta_managed_agents_billing_error: object`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `type: "billing_error"`

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

        - `beta_managed_agents_credential_host_unreachable_error: object`

          An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

          - `type: "credential_host_unreachable_error"`

          - `credential_id: string`

            ID of the affected credential.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `vault_id: string`

            ID of the vault containing the affected credential.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_status_rescheduled_event: object`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `type: "session.status_rescheduled"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_status_running_event: object`

      Indicates the session is actively running and the agent is working.

      - `type: "session.status_running"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_status_idle_event: object`

      Indicates the agent has paused and is awaiting user input.

      - `type: "session.status_idle"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

        - `beta_managed_agents_session_end_turn: object`

          The agent completed its turn naturally and is ready for the next user message.

          - `type: "end_turn"`

        - `beta_managed_agents_session_requires_action: object`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `type: "requires_action"`

          - `event_ids: array of string`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `beta_managed_agents_session_retries_exhausted: object`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

          - `type: "retries_exhausted"`

        - `beta_managed_agents_session_budget_reached: object`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

          - `type: "budget_reached"`

    - `beta_managed_agents_session_status_terminated_event: object`

      Indicates the session has terminated, either due to an error or completion.

      - `type: "session.status_terminated"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_thread_created_event: object`

      Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

      - `type: "session.thread_created"`

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the callable agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public `sthr_` ID of the newly created thread.

    - `beta_managed_agents_span_outcome_evaluation_start_event: object`

      Emitted when an outcome evaluation cycle begins.

      - `type: "span.outcome_evaluation_start"`

      - `id: string`

        Unique identifier for this event.

      - `iteration: number`

        0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

        format: int32

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_span_outcome_evaluation_end_event: object`

      Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

      - `type: "span.outcome_evaluation_end"`

      - `id: string`

        Unique identifier for this event.

      - `explanation: string`

        Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

      - `iteration: number`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `outcome_evaluation_start_id: string`

        The id of the corresponding `span.outcome_evaluation_start` event.

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `result: string`

        Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

      - `usage: object`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

          format: int32

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

          format: int32

        - `input_tokens: number`

          Input tokens consumed by this request.

          format: int32

        - `output_tokens: number`

          Output tokens generated by this request.

          format: int32

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

    - `beta_managed_agents_span_model_request_start_event: object`

      Emitted when a model request is initiated by the agent.

      - `type: "span.model_request_start"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_span_model_request_end_event: object`

      Emitted when a model request completes.

      - `type: "span.model_request_end"`

      - `id: string`

        Unique identifier for this event.

      - `is_error: boolean`

        Whether the model request resulted in an error.

      - `model_request_start_id: string`

        The id of the corresponding `span.model_request_start` event.

      - `model_usage: object`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

          format: int32

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

          format: int32

        - `input_tokens: number`

          Input tokens consumed by this request.

          format: int32

        - `output_tokens: number`

          Output tokens generated by this request.

          format: int32

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

      Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

      - `type: "span.outcome_evaluation_ongoing"`

      - `id: string`

        Unique identifier for this event.

      - `iteration: number`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_user_define_outcome_event: object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `type: "user.define_outcome"`

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `type: "file"`

          - `file_id: string`

            ID of the rubric file.

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `type: "text"`

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

    - `beta_managed_agents_session_deleted_event: object`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `type: "session.deleted"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_thread_status_running_event: object`

      A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `type: "session.thread_status_running"`

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that started running.

    - `beta_managed_agents_session_thread_status_idle_event: object`

      A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `type: "session.thread_status_idle"`

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that went idle.

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

        - `beta_managed_agents_session_end_turn: object`

          The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_requires_action: object`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `beta_managed_agents_session_retries_exhausted: object`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `beta_managed_agents_session_budget_reached: object`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `beta_managed_agents_session_thread_status_terminated_event: object`

      A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `type: "session.thread_status_terminated"`

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that terminated.

    - `beta_managed_agents_user_tool_result_event: object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `type: "user.tool_result"`

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `beta_managed_agents_session_thread_status_rescheduled_event: object`

      A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `type: "session.thread_status_rescheduled"`

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that is retrying.

    - `beta_managed_agents_session_updated_event: object`

      Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

      - `type: "session.updated"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `agent: optional object`

        Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

        - `type: "agent"`

        - `id: string`

        - `description: string`

        - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

          - `type: "url"`

          - `name: string`

          - `url: string`

        - `model: object`

          Model identifier and configuration.

          - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          Resolved coordinator topology with full agent definitions for each roster member.

          - `type: "coordinator"`

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `beta_managed_agents_session_thread_agent: object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `type: "agent"`

              - `id: string`

              - `description: string`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `type: "url"`

                - `name: string`

                - `url: string`

              - `model: object`

                Model identifier and configuration.

                - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

                  The model that will power your agent.

                  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                  How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

                - `inference_geo: optional string`

                  Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

                - `speed: optional "standard" or "fast"`

                  Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `beta_managed_agents_anthropic_skill: object`

                  A resolved Anthropic-managed skill.

                  - `type: "anthropic"`

                  - `skill_id: string`

                  - `version: string`

                - `beta_managed_agents_custom_skill: object`

                  A resolved user-created custom skill.

                  - `type: "custom"`

                  - `skill_id: string`

                  - `version: string`

              - `system: string`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `beta_managed_agents_agent_toolset20260401: object`

                  - `type: "agent_toolset_20260401"`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `beta_managed_agents_bash_tool_config: object`

                      Configuration for the bash tool.

                      - `type: "bash"`

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                          - `type: "auto"`

                    - `beta_managed_agents_edit_tool_config: object`

                      Configuration for the edit tool.

                      - `type: "edit"`

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `beta_managed_agents_read_tool_config: object`

                      Configuration for the read tool.

                      - `type: "read"`

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `beta_managed_agents_write_tool_config: object`

                      Configuration for the write tool.

                      - `type: "write"`

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `beta_managed_agents_glob_tool_config: object`

                      Configuration for the glob tool.

                      - `type: "glob"`

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `beta_managed_agents_grep_tool_config: object`

                      Configuration for the grep tool.

                      - `type: "grep"`

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `beta_managed_agents_web_fetch_tool_config: object`

                      Configuration for the web_fetch tool.

                      - `type: "web_fetch"`

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number`

                        format: int32

                    - `beta_managed_agents_web_search_tool_config: object`

                      Configuration for the web_search tool.

                      - `type: "web_search"`

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                        - `beta_managed_agents_auto_policy: object`

                          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `beta_managed_agents_mcp_toolset: object`

                  - `type: "mcp_toolset"`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `default_config: object`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `mcp_server_name: string`

                - `beta_managed_agents_custom_tool: object`

                  A custom tool as returned in API responses.

                  - `type: "custom"`

                  - `description: string`

                  - `input_schema: object`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown]`

                    - `required: optional array of string`

                  - `name: string`

              - `version: number`

                format: int32

            - `beta_managed_agents_advisor: object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `type: "advisor"`

              - `model: string`

                The advisor model id.

        - `name: string`

        - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

          - `beta_managed_agents_anthropic_skill: object`

            A resolved Anthropic-managed skill.

          - `beta_managed_agents_custom_skill: object`

            A resolved user-created custom skill.

        - `system: string`

        - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

          - `beta_managed_agents_agent_toolset20260401: object`

          - `beta_managed_agents_mcp_toolset: object`

          - `beta_managed_agents_custom_tool: object`

            A custom tool as returned in API responses.

        - `version: number`

          format: int32

      - `budget: optional object`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `type: "limit"`

        - `max_list_cost: object`

          A monetary amount in a specific currency.

          - `amount: string`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `currency: "USD"`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `metadata: optional map[string]`

        The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

      - `title: optional string`

        The session's new title. Present only when the update changed it.

    - `beta_managed_agents_system_message_event: object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `type: "system.message"`

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_usage_event: object`

      Periodic snapshot of the session's cumulative usage and tracked list cost.

      - `type: "session.usage"`

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `usage: object`

        Point-in-time snapshot of a session's cumulative usage.

        - `active_seconds: optional number`

          Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

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

      - `budget: optional object`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `type: "limit"`

        - `max_list_cost: object`

          A monetary amount in a specific currency.

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

#### Example

```bash
ant beta:sessions:threads:events list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

### Stream Session Thread Events

`$ ant beta:sessions:threads:events stream`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--event-delta: optional array of BetaManagedAgentsDeltaType`

  Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `beta_managed_agents_stream_session_thread_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in a single thread's stream.

  - `beta_managed_agents_user_message_event: object`

    A user message event in the session conversation.

    - `type: "user.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_user_interrupt_event: object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: "user.interrupt"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `beta_managed_agents_user_tool_confirmation_event: object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: "user.tool_confirmation"`

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `beta_managed_agents_user_custom_tool_result_event: object`

    Event sent by the client providing the result of a custom tool execution.

    - `type: "user.custom_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

        - `type: "search_result"`

        - `citations: object`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `type: "text"`

          - `text: string`

            The text content.

            minLength: 1

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `beta_managed_agents_agent_custom_tool_use_event: object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: "agent.custom_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `beta_managed_agents_agent_message_event: object`

    An agent response event in the session conversation.

    - `type: "agent.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_agent_thinking_event: object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: "agent.thinking"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_agent_mcp_tool_use_event: object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: "agent.mcp_tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `beta_managed_agents_agent_tool_evaluation_always_allow: object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: "always_allow"`

      - `beta_managed_agents_agent_tool_evaluation_always_ask: object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: "always_ask"`

      - `beta_managed_agents_agent_tool_evaluation_auto: object`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: "auto"`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermissionAllow or BetaManagedAgentsAgentAutoEvaluatedPermissionAsk or BetaManagedAgentsAgentAutoEvaluatedPermissionDeny`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `beta_managed_agents_agent_auto_evaluated_permission_allow: object`

            The server judged the invocation safe to execute without client approval.

            - `type: "allow"`

          - `beta_managed_agents_agent_auto_evaluated_permission_ask: object`

            The server reached no judgement; the invocation is held for client approval.

            - `type: "ask"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `beta_managed_agents_agent_auto_evaluated_permission_deny: object`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: "deny"`

            - `reason_code: string`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_mcp_tool_result_event: object`

    Event representing the result of an MCP tool execution.

    - `type: "agent.mcp_tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: "agent.tool_use"`

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: optional BetaManagedAgentsAgentToolEvaluationAlwaysAllow or BetaManagedAgentsAgentToolEvaluationAlwaysAsk or BetaManagedAgentsAgentToolEvaluationAuto`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `beta_managed_agents_agent_tool_evaluation_always_allow: object`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

      - `beta_managed_agents_agent_tool_evaluation_always_ask: object`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

      - `beta_managed_agents_agent_tool_evaluation_auto: object`

        The resolved permission_policy was auto: the server judged this invocation individually.

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_tool_result_event: object`

    Event representing the result of an agent tool execution.

    - `type: "agent.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_message_received_event: object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: "agent.thread_message_received"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `beta_managed_agents_agent_thread_message_sent_event: object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: "agent.thread_message_sent"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `beta_managed_agents_agent_thread_context_compacted_event: object`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: "agent.thread_context_compacted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_error_event: object`

    An error event indicating a problem occurred during session execution.

    - `type: "session.error"`

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      - `beta_managed_agents_unknown_error: object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: "unknown_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

      - `beta_managed_agents_model_overloaded_error: object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: "model_overloaded_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_model_rate_limited_error: object`

        The model request was rate-limited.

        - `type: "model_rate_limited_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_model_request_failed_error: object`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: "model_request_failed_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_mcp_connection_failed_error: object`

        Failed to connect to an MCP server.

        - `type: "mcp_connection_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_mcp_authentication_failed_error: object`

        Authentication to an MCP server failed.

        - `type: "mcp_authentication_failed_error"`

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_billing_error: object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: "billing_error"`

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

      - `beta_managed_agents_credential_host_unreachable_error: object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: "credential_host_unreachable_error"`

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_status_rescheduled_event: object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: "session.status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_status_running_event: object`

    Indicates the session is actively running and the agent is working.

    - `type: "session.status_running"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_status_idle_event: object`

    Indicates the agent has paused and is awaiting user input.

    - `type: "session.status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: "requires_action"`

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

  - `beta_managed_agents_session_status_terminated_event: object`

    Indicates the session has terminated, either due to an error or completion.

    - `type: "session.status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_thread_created_event: object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: "session.thread_created"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

  - `beta_managed_agents_span_outcome_evaluation_start_event: object`

    Emitted when an outcome evaluation cycle begins.

    - `type: "span.outcome_evaluation_start"`

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_span_outcome_evaluation_end_event: object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: "span.outcome_evaluation_end"`

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `beta_managed_agents_span_model_request_start_event: object`

    Emitted when a model request is initiated by the agent.

    - `type: "span.model_request_start"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_span_model_request_end_event: object`

    Emitted when a model request completes.

    - `type: "span.model_request_end"`

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: "span.outcome_evaluation_ongoing"`

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_user_define_outcome_event: object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: "user.define_outcome"`

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric: object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `beta_managed_agents_text_rubric: object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `beta_managed_agents_session_deleted_event: object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: "session.deleted"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_thread_status_running_event: object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_running"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

  - `beta_managed_agents_session_thread_status_idle_event: object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_idle"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `beta_managed_agents_session_thread_status_terminated_event: object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_terminated"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

  - `beta_managed_agents_user_tool_result_event: object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: "user.tool_result"`

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `beta_managed_agents_session_thread_status_rescheduled_event: object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: "session.thread_status_rescheduled"`

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

  - `beta_managed_agents_session_updated_event: object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: "session.updated"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent: optional object`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: "agent"`

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: "coordinator"`

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `beta_managed_agents_session_thread_agent: object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: "agent"`

            - `id: string`

            - `description: string`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `type: "url"`

              - `name: string`

              - `url: string`

            - `model: object`

              Model identifier and configuration.

              - `id: "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

                The model that will power your agent.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

              - `inference_geo: optional string`

                Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

              - `speed: optional "standard" or "fast"`

                Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `beta_managed_agents_anthropic_skill: object`

                A resolved Anthropic-managed skill.

                - `type: "anthropic"`

                - `skill_id: string`

                - `version: string`

              - `beta_managed_agents_custom_skill: object`

                A resolved user-created custom skill.

                - `type: "custom"`

                - `skill_id: string`

                - `version: string`

            - `system: string`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `beta_managed_agents_agent_toolset20260401: object`

                - `type: "agent_toolset_20260401"`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `beta_managed_agents_bash_tool_config: object`

                    Configuration for the bash tool.

                    - `type: "bash"`

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: "auto"`

                  - `beta_managed_agents_edit_tool_config: object`

                    Configuration for the edit tool.

                    - `type: "edit"`

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_read_tool_config: object`

                    Configuration for the read tool.

                    - `type: "read"`

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_write_tool_config: object`

                    Configuration for the write tool.

                    - `type: "write"`

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_glob_tool_config: object`

                    Configuration for the glob tool.

                    - `type: "glob"`

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_grep_tool_config: object`

                    Configuration for the grep tool.

                    - `type: "grep"`

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `beta_managed_agents_web_fetch_tool_config: object`

                    Configuration for the web_fetch tool.

                    - `type: "web_fetch"`

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number`

                      format: int32

                  - `beta_managed_agents_web_search_tool_config: object`

                    Configuration for the web_search tool.

                    - `type: "web_search"`

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                      - `beta_managed_agents_auto_policy: object`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                    - `beta_managed_agents_auto_policy: object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `beta_managed_agents_mcp_toolset: object`

                - `type: "mcp_toolset"`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                    - `beta_managed_agents_auto_policy: object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: object`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                    - `beta_managed_agents_auto_policy: object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: string`

              - `beta_managed_agents_custom_tool: object`

                A custom tool as returned in API responses.

                - `type: "custom"`

                - `description: string`

                - `input_schema: object`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown]`

                  - `required: optional array of string`

                - `name: string`

            - `version: number`

              format: int32

          - `beta_managed_agents_advisor: object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: "advisor"`

            - `model: string`

              The advisor model id.

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

        - `beta_managed_agents_mcp_toolset: object`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

      - `version: number`

        format: int32

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: "limit"`

      - `max_list_cost: object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `beta_managed_agents_start_event: object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_start"`

    - `event: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `beta_managed_agents_agent_message_preview: object`

        - `type: "agent.message"`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `beta_managed_agents_agent_thinking_preview: object`

        - `type: "agent.thinking"`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `beta_managed_agents_delta_event: object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: "event_delta"`

    - `delta: object`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: "content_delta"`

      - `content: object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `beta_managed_agents_system_message_event: object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: "system.message"`

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `type: "text"`

      - `text: string`

        The text content.

        minLength: 1

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_usage_event: object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: "session.usage"`

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: object`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

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

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: "limit"`

      - `max_list_cost: object`

        A monetary amount in a specific currency.

#### Example

```bash
ant beta:sessions:threads:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
