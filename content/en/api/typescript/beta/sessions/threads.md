# Threads

## List Session Threads

`client.beta.sessions.threads.list(sessionID, params?, options?): PageCursor<BetaManagedAgentsSessionThread>`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `sessionID: string`

- `params: ThreadListParams`

  - `limit?: number`

    Query param: Maximum results per page. Defaults to 1000.

    format: int32

  - `page?: string`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

### Returns

- `BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

          - `configs: Array<BetaManagedAgentsAgentToolConfig>`

            - `BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains?: Array<string>`

              - `blocked_domains?: Array<string>`

              - `max_content_tokens?: number | null`

                format: int32

            - `BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `BetaManagedAgentsMCPToolset`

          - `configs: Array<BetaManagedAgentsMCPToolConfig>`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties?: Record<string, unknown> | null`

            - `required?: Array<string> | null`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string | null`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats | null`

    Timing statistics for a session thread.

    - `active_seconds?: number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds?: number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds?: number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage | null`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds?: number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost?: BetaMonetaryAmount | null`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens?: number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests?: number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests?: number`

        Number of server-executed web search requests.

        format: int32

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSessionThread of client.beta.sessions.threads.list(
  "sesn_011CZkZAtmR3yMPDzynEDxu7"
)) {
  console.log(betaManagedAgentsSessionThread.id);
}
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

`client.beta.sessions.threads.retrieve(threadID, params, options?): BetaManagedAgentsSessionThread`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `threadID: string`

- `params: ThreadRetrieveParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

### Returns

- `BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

          - `configs: Array<BetaManagedAgentsAgentToolConfig>`

            - `BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains?: Array<string>`

              - `blocked_domains?: Array<string>`

              - `max_content_tokens?: number | null`

                format: int32

            - `BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `BetaManagedAgentsMCPToolset`

          - `configs: Array<BetaManagedAgentsMCPToolConfig>`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties?: Record<string, unknown> | null`

            - `required?: Array<string> | null`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string | null`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats | null`

    Timing statistics for a session thread.

    - `active_seconds?: number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds?: number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds?: number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage | null`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds?: number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost?: BetaMonetaryAmount | null`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens?: number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests?: number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests?: number`

        Number of server-executed web search requests.

        format: int32

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsSessionThread = await client.beta.sessions.threads.retrieve(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  { session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7" }
);

console.log(betaManagedAgentsSessionThread.id);
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

`client.beta.sessions.threads.archive(threadID, params, options?): BetaManagedAgentsSessionThread`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `threadID: string`

- `params: ThreadArchiveParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

### Returns

- `BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

          - `configs: Array<BetaManagedAgentsAgentToolConfig>`

            - `BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains?: Array<string>`

              - `blocked_domains?: Array<string>`

              - `max_content_tokens?: number | null`

                format: int32

            - `BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `BetaManagedAgentsMCPToolset`

          - `configs: Array<BetaManagedAgentsMCPToolConfig>`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties?: Record<string, unknown> | null`

            - `required?: Array<string> | null`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string | null`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats | null`

    Timing statistics for a session thread.

    - `active_seconds?: number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds?: number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds?: number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage | null`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds?: number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost?: BetaMonetaryAmount | null`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens?: number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests?: number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests?: number`

        Number of server-executed web search requests.

        format: int32

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsSessionThread = await client.beta.sessions.threads.archive(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  { session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7" }
);

console.log(betaManagedAgentsSessionThread.id);
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

- `BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

          - `configs: Array<BetaManagedAgentsAgentToolConfig>`

            - `BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains?: Array<string>`

              - `blocked_domains?: Array<string>`

              - `max_content_tokens?: number | null`

                format: int32

            - `BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `BetaManagedAgentsMCPToolset`

          - `configs: Array<BetaManagedAgentsMCPToolConfig>`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties?: Record<string, unknown> | null`

            - `required?: Array<string> | null`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string | null`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats | null`

    Timing statistics for a session thread.

    - `active_seconds?: number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds?: number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds?: number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage | null`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds?: number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost?: BetaMonetaryAmount | null`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens?: number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests?: number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests?: number`

        Number of server-executed web search requests.

        format: int32

### Beta Managed Agents Session Thread Stats

- `BetaManagedAgentsSessionThreadStats`

  Timing statistics for a session thread.

  - `active_seconds?: number`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

    format: double

  - `duration_seconds?: number`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    format: double

  - `startup_seconds?: number`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

    format: double

### Beta Managed Agents Session Thread Status

- `BetaManagedAgentsSessionThreadStatus = "running" | "idle" | "rescheduling" | "terminated"`

  SessionThreadStatus enum

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `BetaManagedAgentsSessionThreadUsage`

  Cumulative token usage for a session thread across all turns.

  - `active_seconds?: number`

    Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

    format: double

  - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens?: number`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `ephemeral_5m_input_tokens?: number`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `cache_read_input_tokens?: number`

    Total tokens read from prompt cache.

    format: int32

  - `input_tokens?: number`

    Total input tokens consumed across all turns.

    format: int32

  - `list_cost?: BetaMonetaryAmount | null`

    A monetary amount in a specific currency.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `output_tokens?: number`

    Total output tokens generated across all turns.

    format: int32

  - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `web_fetch_requests?: number`

      Number of server-executed web fetch requests.

      format: int32

    - `web_search_requests?: number`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Stream Session Thread Events

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in a single thread's stream.

  - `BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" | "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message?: string | null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: Array<BetaManagedAgentsSearchResultContent>`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock>`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name?: string | null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name?: string | null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array<string>`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

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

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

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

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

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

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean | null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

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

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number | null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent?: BetaManagedAgentsSessionAgent | null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string | null`

            - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

              - `BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string | null`

            - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

              - `BetaManagedAgentsAgentToolset20260401`

                - `configs: Array<BetaManagedAgentsAgentToolConfig>`

                  - `BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `max_content_tokens?: number | null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset`

                - `configs: Array<BetaManagedAgentsMCPToolConfig>`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties?: Record<string, unknown> | null`

                  - `required?: Array<string> | null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

        - `BetaManagedAgentsMCPToolset`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata?: Record<string, string>`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title?: string | null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

      - `BetaManagedAgentsAgentThinkingPreview`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

    - `type: "event_start"`

  - `BetaManagedAgentsDeltaEvent`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: "content_delta"`

      - `index?: number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

  - `BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds?: number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens?: number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens?: number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens?: number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens?: number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost?: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens?: number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use?: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests?: number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests?: number`

          Number of server-executed web search requests.

          format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

## Threads › Events

### List Session Thread Events

`client.beta.sessions.threads.events.list(threadID, params, options?): PageCursor<BetaManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `threadID: string`

- `params: EventListParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `limit?: number`

    Query param: Query parameter for limit

    format: int32

  - `page?: string`

    Query param: Query parameter for page

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

#### Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 32 more`

  Union type for all event types in a session.

  - `BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" | "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message?: string | null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: Array<BetaManagedAgentsSearchResultContent>`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock>`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name?: string | null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name?: string | null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array<string>`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

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

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

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

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

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

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean | null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

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

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number | null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent?: BetaManagedAgentsSessionAgent | null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string | null`

            - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

              - `BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string | null`

            - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

              - `BetaManagedAgentsAgentToolset20260401`

                - `configs: Array<BetaManagedAgentsAgentToolConfig>`

                  - `BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `max_content_tokens?: number | null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset`

                - `configs: Array<BetaManagedAgentsMCPToolConfig>`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties?: Record<string, unknown> | null`

                  - `required?: Array<string> | null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

        - `BetaManagedAgentsMCPToolset`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata?: Record<string, string>`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title?: string | null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds?: number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens?: number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens?: number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens?: number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens?: number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost?: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens?: number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use?: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests?: number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests?: number`

          Number of server-executed web search requests.

          format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSessionEvent of client.beta.sessions.threads.events.list(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  { session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7" }
)) {
  console.log(betaManagedAgentsSessionEvent);
}
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

`client.beta.sessions.threads.events.stream(threadID, params, options?): BetaManagedAgentsStreamSessionThreadEvents | Stream<BetaManagedAgentsStreamSessionThreadEvents>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `threadID: string`

- `params: EventStreamParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `event_deltas?: Array<BetaManagedAgentsDeltaType>`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `"agent.message"`

    - `"agent.thinking"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

#### Returns

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in a single thread's stream.

  - `BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Array of content blocks comprising the user message.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context?: string | null`

          Additional context about the document for the model.

        - `title?: string | null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" | "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message?: string | null`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: Array<BetaManagedAgentsSearchResultContent>`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock>`

      Array of text blocks comprising the agent response.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: Record<string, unknown>`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission?: "allow" | "ask" | "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id?: string | null`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

  - `BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name?: string | null`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>`

      Message content blocks.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name?: string | null`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array<string>`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

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

    - `type: "span.outcome_evaluation_start"`

  - `BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

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

    - `type: "span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

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

      - `speed?: "standard" | "fast" | null`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean | null`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

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

    - `type: "span.outcome_evaluation_ongoing"`

  - `BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number | null`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>`

      The result content returned by the tool.

      - `BetaManagedAgentsTextBlock`

        Regular text content.

      - `BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error?: boolean | null`

      Whether the tool execution resulted in an error.

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id?: string | null`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent?: BetaManagedAgentsSessionAgent | null`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string | null`

            - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: string`

            - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

              - `BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string | null`

            - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

              - `BetaManagedAgentsAgentToolset20260401`

                - `configs: Array<BetaManagedAgentsAgentToolConfig>`

                  - `BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains?: Array<string>`

                    - `blocked_domains?: Array<string>`

                    - `max_content_tokens?: number | null`

                      format: int32

                  - `BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `BetaManagedAgentsMCPToolset`

                - `configs: Array<BetaManagedAgentsMCPToolConfig>`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties?: Record<string, unknown> | null`

                  - `required?: Array<string> | null`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

        - `BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

        - `BetaManagedAgentsMCPToolset`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata?: Record<string, string>`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title?: string | null`

      The session's new title. Present only when the update changed it.

  - `BetaManagedAgentsStartEvent`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `BetaManagedAgentsAgentMessagePreview`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

      - `BetaManagedAgentsAgentThinkingPreview`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

    - `type: "event_start"`

  - `BetaManagedAgentsDeltaEvent`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: "content_delta"`

      - `index?: number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

  - `BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: Array<BetaManagedAgentsSystemContentBlock>`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at?: string | null`

      A timestamp in RFC 3339 format

      format: date-time

  - `BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds?: number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens?: number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens?: number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens?: number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens?: number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost?: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens?: number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use?: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests?: number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests?: number`

          Number of server-executed web search requests.

          format: int32

    - `budget?: BetaManagedAgentsBudgetLimit | null`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in a single thread's stream.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsStreamSessionThreadEvents =
  await client.beta.sessions.threads.events.stream("sthr_011CZkZVWa6oIjw0rgXZpnBt", {
    session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
  });

console.log(betaManagedAgentsStreamSessionThreadEvents);
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
