# Get Session Thread

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

## Parameters

- `ThreadRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

## Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    A session-resolved multiagent roster entry.

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

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929`

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

          - `Standard`

          - `Fast`

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

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

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

            - `JsonElement Type constant`

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

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

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
ThreadRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
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
