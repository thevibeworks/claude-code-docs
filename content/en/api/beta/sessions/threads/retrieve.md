---
title: Get Session Thread
url: https://platform.claude.com/docs/en/api/beta/sessions/threads/retrieve
---

# Get Session Thread

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

## Path parameters

- `session_id: string`

- `thread_id: string`

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 45 more`

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

    - `"compact-2026-09-04"`

    - `"inline-tools-2026-09-15"`

    - `"mcp-client-2026-09-15"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaManagedAgentsSessionThread object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: "session_thread"`

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

    - `BetaManagedAgentsSessionThreadAgent object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: "agent"`

      - `id: string`

      - `description: string or null`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `type: "url"`

        - `name: string`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `string`

          - `"claude-opus-5-5" or "claude-fable-5-1" or "claude-sonnet-5" or 12 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `"claude-opus-5-5"`

              Powerful intelligence for coding, knowledge work, and long-running agents

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

          How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

          - `BetaManagedAgentsEffortLow object`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium object`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh object`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh object`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax object`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo: optional string`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `BetaManagedAgentsAnthropicSkill object`

          A resolved Anthropic-managed skill.

          - `type: "anthropic"`

          - `skill_id: string`

          - `version: string`

        - `BetaManagedAgentsCustomSkill object`

          A resolved user-created custom skill.

          - `type: "custom"`

          - `skill_id: string`

          - `version: string`

      - `system: string or null`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `BetaManagedAgentsAgentToolset20260401 object`

          - `type: "agent_toolset_20260401"`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `BetaManagedAgentsBashToolConfig object`

              Configuration for the bash tool.

              - `type: "bash"`

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: "auto"`

            - `BetaManagedAgentsEditToolConfig object`

              Configuration for the edit tool.

              - `type: "edit"`

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `BetaManagedAgentsReadToolConfig object`

              Configuration for the read tool.

              - `type: "read"`

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `BetaManagedAgentsWriteToolConfig object`

              Configuration for the write tool.

              - `type: "write"`

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `BetaManagedAgentsGlobToolConfig object`

              Configuration for the glob tool.

              - `type: "glob"`

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `BetaManagedAgentsGrepToolConfig object`

              Configuration for the grep tool.

              - `type: "grep"`

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `BetaManagedAgentsWebFetchToolConfig object`

              Configuration for the web_fetch tool.

              - `type: "web_fetch"`

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number or null`

                format: int32

            - `BetaManagedAgentsWebSearchToolConfig object`

              Configuration for the web_search tool.

              - `type: "web_search"`

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy object`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy object`

                  Tool calls require user confirmation before execution.

                - `BetaManagedAgentsAutoPolicy object`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `user_location: optional BetaManagedAgentsUserLocation or null`

                Approximate user location for search result localization.

                - `type: "approximate"`

                  Location precision. Only "approximate" is supported.

                - `city: optional string or null`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: optional string or null`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: optional string or null`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: optional string or null`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `BetaManagedAgentsMCPToolset object`

          - `type: "mcp_toolset"`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: string`

        - `BetaManagedAgentsCustomTool object`

          A custom tool as returned in API responses.

          - `type: "custom"`

          - `description: string`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown] or null`

            - `required: optional array of string or null`

          - `name: string`

      - `version: number`

        format: int32

    - `BetaManagedAgentsAdvisor object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: "advisor"`

      - `model: string`

        The advisor model id.

  - `archived_at: string or null`

    When the thread was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    When the thread was created.

    format: date-time

  - `parent_thread_id: string or null`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats or null`

    Timing statistics for this thread. Null until the thread's first status transition.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    Current execution status of the thread.

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `updated_at: string`

    When the thread was last updated.

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage or null`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

    - `active_seconds: optional number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Tokens used to create prompt cache entries, broken down by cache TTL.

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

    - `list_cost: optional BetaMonetaryAmount or null`

      Cumulative list cost of this thread across all turns, priced at public list rates. Absent until cost tracking is available for the thread. Each figure is rounded to the nearest cent independently and the session's aggregate `usage.list_cost` additionally includes session runtime, so per-thread costs do not sum exactly to the session figure; the session figure is authoritative and is what a budget is enforced against.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional BetaManagedAgentsServerToolUsage or null`

      Cumulative server-executed tool usage across all turns of this thread. Absent until server-tool tracking is available for the thread.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

## Example

```bash
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/threads/$THREAD_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
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
