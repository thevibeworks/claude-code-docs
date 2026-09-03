# List Session Threads

`ThreadListPage Beta.Sessions.Threads.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

## Parameters

- `ThreadListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `int limit`

    Query param: Maximum results per page. Defaults to 1000.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor from a previous response's `next_page`. Forward-only.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

## Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1("claude-fable-5-1")`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `ClaudeFable5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard("standard")`

          - `Fast("fast")`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name = "bash"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type = "bash"`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name = "edit"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "edit"`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name = "read"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "read"`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name = "write"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "write"`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name = "glob"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "glob"`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name = "grep"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "grep"`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name = "web_fetch"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "web_fetch"`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name = "web_search"`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type = "web_search"`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type = "approximate"`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type = "object"`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running("running")`

    - `Idle("idle")`

    - `Rescheduling("rescheduling")`

    - `Terminated("terminated")`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

## Example

```csharp
ThreadListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Threads.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

### Response (200)

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
