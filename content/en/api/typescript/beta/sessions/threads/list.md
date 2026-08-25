---
title: List Session Threads
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/threads/list
---

## List Session Threads

`client.beta.sessions.threads.list(stringsessionID, ThreadListParamsparams?, RequestOptionsoptions?): PageCursor<BetaManagedAgentsSessionThread>`

**get** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `sessionID: string`

- `params: ThreadListParams`

  - `limit?: number`

    Query param: Maximum results per page. Defaults to 1000.

  - `page?: string`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

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

### Returns

- `BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    A session-resolved multiagent roster entry.

    - `BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string | null`

      - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

        - `name: string`

        - `type: "url"`

          - `"url"`

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

              - `"low"`

          - `BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

              - `"medium"`

          - `BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: "high"`

              - `"high"`

          - `BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

              - `"xhigh"`

          - `BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

              - `"max"`

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

            - `"anthropic"`

          - `version: string`

        - `BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

            - `"custom"`

          - `version: string`

      - `system: string | null`

      - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

        - `BetaManagedAgentsAgentToolset20260401`

          - `configs: Array<BetaManagedAgentsAgentToolConfig>`

            - `BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

                - `"bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                    - `"always_allow"`

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

                    - `"always_ask"`

              - `type: "bash"`

                - `"bash"`

            - `BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

                - `"edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

                - `"edit"`

            - `BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

                - `"read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

                - `"read"`

            - `BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

                - `"write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

                - `"write"`

            - `BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

                - `"glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

                - `"glob"`

            - `BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

                - `"grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

                - `"grep"`

            - `BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

                - `"web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

                - `"web_fetch"`

              - `allowed_domains?: Array<string>`

              - `blocked_domains?: Array<string>`

              - `max_content_tokens?: number | null`

            - `BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

                - `"web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

                - `"web_search"`

              - `allowed_domains?: Array<string>`

              - `blocked_domains?: Array<string>`

              - `user_location?: BetaManagedAgentsUserLocation | null`

                Approximate user location for search result localization.

                - `type: "approximate"`

                  Location precision. Only "approximate" is supported.

                  - `"approximate"`

                - `city?: string | null`

                  City name.

                - `country?: string | null`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region?: string | null`

                  Region or state name.

                - `timezone?: string | null`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

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

            - `"agent_toolset_20260401"`

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

            - `"mcp_toolset"`

        - `BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

              - `"object"`

            - `properties?: Record<string, unknown> | null`

            - `required?: Array<string> | null`

          - `name: string`

          - `type: "custom"`

            - `"custom"`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

        - `"advisor"`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `parent_thread_id: string | null`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats | null`

    Timing statistics for a session thread.

    - `active_seconds?: number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

    - `duration_seconds?: number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

    - `startup_seconds?: number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

    - `"session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionThreadUsage | null`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds?: number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

    - `list_cost?: BetaMonetaryAmount | null`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"`

    - `output_tokens?: number`

      Total output tokens generated across all turns.

    - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests?: number`

        Number of server-executed web fetch requests.

      - `web_search_requests?: number`

        Number of server-executed web search requests.

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

#### Response

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
