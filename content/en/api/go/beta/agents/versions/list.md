---
title: List Agent Versions
url: https://platform.claude.com/docs/en/api/go/beta/agents/versions/list
---

## List Agent Versions

`client.Beta.Agents.Versions.List(ctx, agentID, params) (*PageCursor[BetaManagedAgentsAgent], error)`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `agentID string`

- `params BetaAgentVersionListParams`

  - `Limit param.Field[int64]`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

    - `URL string`

  - `Metadata map[string, string]`

  - `Model BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `ID BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `type BetaManagedAgentsModel string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

          High-performance model for coding and agents

        - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `string`

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

      - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

  - `Multiagent BetaManagedAgentsMultiagent`

    Resolved coordinator topology with a concrete agent roster.

    - `Agents []BetaManagedAgentsMultiagentAgentUnion`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `type BetaManagedAgentsAgentReference struct{…}`

        A resolved agent reference with a concrete version.

        - `ID string`

        - `Type BetaManagedAgentsAgentReferenceType`

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `Enabled bool`

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAgentToolset20260401Type`

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

    - `type BetaManagedAgentsMCPToolset struct{…}`

      - `Configs []BetaManagedAgentsMCPToolConfig`

        - `Enabled bool`

        - `Name string`

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `Enabled bool`

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `MCPServerName string`

      - `Type BetaManagedAgentsMCPToolsetType`

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Agents.Versions.List(
		context.TODO(),
		"agent_011CZkYpogX7uDKUyvBTophP",
		anthropic.BetaAgentVersionListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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
