---
title: List Agent Versions
url: https://platform.claude.com/docs/en/api/java/beta/agents/versions/list
---

## List Agent Versions

`VersionListPage beta().agents().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `VersionListParams params`

  - `Optional<String> agentId`

  - `Optional<Long> limit`

    Maximum results per page. Default 20, maximum 100.

  - `Optional<String> page`

    Opaque pagination cursor.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

### Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

  - `Optional<String> description`

  - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

    - `String name`

    - `Type type`

      - `URL("url")`

    - `String url`

  - `Metadata metadata`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

    - `BetaManagedAgentsModel id`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `CLAUDE_SONNET_5("claude-sonnet-5")`

        High-performance model for coding and agents

      - `CLAUDE_FABLE_5("claude-fable-5")`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `CLAUDE_OPUS_5("claude-opus-5")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

        Best combination of speed and intelligence

      - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

        Fastest model with near-frontier intelligence

      - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

        Fastest model with near-frontier intelligence

      - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

        Powerful intelligence for long-running agents and coding

      - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

        High-performance model for agents and coding

      - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

        High-performance model for agents and coding

    - `Optional<Effort> effort`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow:`

        Low effort. Favors latency over reasoning depth.

        - `Type type`

          - `LOW("low")`

      - `class BetaManagedAgentsEffortMedium:`

        Medium effort. Balances latency and reasoning depth.

        - `Type type`

          - `MEDIUM("medium")`

      - `class BetaManagedAgentsEffortHigh:`

        High effort. Favors reasoning depth.

        - `Type type`

          - `HIGH("high")`

      - `class BetaManagedAgentsEffortXhigh:`

        Extra-high effort. Not all models accept this level.

        - `Type type`

          - `XHIGH("xhigh")`

      - `class BetaManagedAgentsEffortMax:`

        Maximum effort. Favors reasoning depth over latency.

        - `Type type`

          - `MAX("max")`

    - `Optional<String> inferenceGeo`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `Optional<BetaManagedAgentsMultiagent> multiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `List<Agent> agents`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference:`

        A resolved agent reference with a concrete version.

        - `String id`

        - `Type type`

          - `AGENT("agent")`

        - `long version`

      - `class BetaManagedAgentsAdvisor:`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `String model`

          The advisor model id.

        - `Type type`

          - `ADVISOR("advisor")`

    - `Type type`

      - `COORDINATOR("coordinator")`

  - `String name`

  - `List<Skill> skills`

    - `class BetaManagedAgentsAnthropicSkill:`

      A resolved Anthropic-managed skill.

      - `String skillId`

      - `Type type`

        - `ANTHROPIC("anthropic")`

      - `String version`

    - `class BetaManagedAgentsCustomSkill:`

      A resolved user-created custom skill.

      - `String skillId`

      - `Type type`

        - `CUSTOM("custom")`

      - `String version`

  - `Optional<String> system`

  - `List<Tool> tools`

    - `class BetaManagedAgentsAgentToolset20260401:`

      - `List<BetaManagedAgentsAgentToolConfig> configs`

        - `class BetaManagedAgentsBashToolConfig:`

          Configuration for the bash tool.

          - `boolean enabled`

          - `JsonValue; name "bash"constant`

            - `BASH("bash")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `Type type`

                - `ALWAYS_ALLOW("always_allow")`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `Type type`

                - `ALWAYS_ASK("always_ask")`

          - `JsonValue; type "bash"constant`

            - `BASH("bash")`

        - `class BetaManagedAgentsEditToolConfig:`

          Configuration for the edit tool.

          - `boolean enabled`

          - `JsonValue; name "edit"constant`

            - `EDIT("edit")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "edit"constant`

            - `EDIT("edit")`

        - `class BetaManagedAgentsReadToolConfig:`

          Configuration for the read tool.

          - `boolean enabled`

          - `JsonValue; name "read"constant`

            - `READ("read")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "read"constant`

            - `READ("read")`

        - `class BetaManagedAgentsWriteToolConfig:`

          Configuration for the write tool.

          - `boolean enabled`

          - `JsonValue; name "write"constant`

            - `WRITE("write")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "write"constant`

            - `WRITE("write")`

        - `class BetaManagedAgentsGlobToolConfig:`

          Configuration for the glob tool.

          - `boolean enabled`

          - `JsonValue; name "glob"constant`

            - `GLOB("glob")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "glob"constant`

            - `GLOB("glob")`

        - `class BetaManagedAgentsGrepToolConfig:`

          Configuration for the grep tool.

          - `boolean enabled`

          - `JsonValue; name "grep"constant`

            - `GREP("grep")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "grep"constant`

            - `GREP("grep")`

        - `class BetaManagedAgentsWebFetchToolConfig:`

          Configuration for the web_fetch tool.

          - `boolean enabled`

          - `JsonValue; name "web_fetch"constant`

            - `WEB_FETCH("web_fetch")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "web_fetch"constant`

            - `WEB_FETCH("web_fetch")`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<Long> maxContentTokens`

        - `class BetaManagedAgentsWebSearchToolConfig:`

          Configuration for the web_search tool.

          - `boolean enabled`

          - `JsonValue; name "web_search"constant`

            - `WEB_SEARCH("web_search")`

          - `PermissionPolicy permissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `JsonValue; type "web_search"constant`

            - `WEB_SEARCH("web_search")`

          - `Optional<List<String>> allowedDomains`

          - `Optional<List<String>> blockedDomains`

          - `Optional<BetaManagedAgentsUserLocation> userLocation`

            Approximate user location for search result localization.

            - `JsonValue; type "approximate"constant`

              Location precision. Only "approximate" is supported.

              - `APPROXIMATE("approximate")`

            - `Optional<String> city`

              City name.

            - `Optional<String> country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Optional<String> region`

              Region or state name.

            - `Optional<String> timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

        Resolved default configuration for agent tools.

        - `boolean enabled`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `Type type`

        - `AGENT_TOOLSET_20260401("agent_toolset_20260401")`

    - `class BetaManagedAgentsMcpToolset:`

      - `List<BetaManagedAgentsMcpToolConfig> configs`

        - `boolean enabled`

        - `String name`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `boolean enabled`

        - `PermissionPolicy permissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `String mcpServerName`

      - `Type type`

        - `MCP_TOOLSET("mcp_toolset")`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

      - `String description`

      - `BetaManagedAgentsCustomToolInputSchema inputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonValue; type "object"constant`

          - `OBJECT("object")`

        - `Optional<Properties> properties`

        - `Optional<List<String>> required`

      - `String name`

      - `Type type`

        - `CUSTOM("custom")`

  - `Type type`

    - `AGENT("agent")`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

  - `long version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.agents.versions.VersionListPage;
import com.anthropic.models.beta.agents.versions.VersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VersionListPage page = client.beta().agents().versions().list("agent_011CZkYpogX7uDKUyvBTophP");
    }
}
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
