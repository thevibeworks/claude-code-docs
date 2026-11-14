---
title: List Agent Versions
url: https://platform.claude.com/docs/en/api/typescript/beta/agents/versions/list
---

# List Agent Versions

- Signature: `client.beta.agents.versions.list(agentID: string, params?: VersionListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsAgent>`
- Endpoint: `GET /v1/agents/{agent_id}/versions`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsAgent of client.beta.agents.versions.list(
  "agent_011CZkYpogX7uDKUyvBTophP"
)) {
  console.log(betaManagedAgentsAgent.id);
}
```

## Example response (200)

```json
{
  "data": [
    {
      "id": "agent_011CZkYpogX7uDKUyvBTophP",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "A general-purpose starter agent.",
      "execution_identity": {
        "type": "service_account"
      },
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
        "id": "claude-opus-5-5",
        "effort": {
          "type": "low"
        },
        "inference_geo": "inference_geo",
        "speed": "standard"
      },
      "multiagent": null,
      "name": "My First Agent",
      "skills": [
        {
          "skill_id": "xlsx",
          "type": "anthropic",
          "version": "1"
        },
        {
          "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTmx",
          "type": "custom",
          "version": "2"
        }
      ],
      "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
      "tools": [
        {
          "configs": [],
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

## Parameters

```ts
/** Agent ID to list versions for. */
agentID: string; // path parameter

interface VersionListParams {
  /** Maximum results per page. Default 20, maximum 100. */
  limit?: number; // query parameter, format: int32
  /** Opaque pagination cursor. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** A Managed Agents `agent`. */
interface BetaManagedAgentsAgent {
  type: "agent";
  id: string;
  /** When the agent was archived. Null if not archived. */
  archived_at: string | null; // format: date-time
  /** A timestamp in RFC 3339 format */
  created_at: string; // format: date-time
  description: string | null;
  /** Execution principal for runs of this agent. Always present; `{"type": "service_account"}` when runs carry no customer-named principal. */
  execution_identity: BetaManagedAgentsExecutionIdentity;
  mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>;
  metadata: Record<string, string>;
  /** Model identifier and configuration. */
  model: BetaManagedAgentsModelConfig;
  /** Multiagent orchestration configuration. Null when the agent is single-threaded. */
  multiagent: BetaManagedAgentsMultiagent | null;
  name: string;
  skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>;
  system: string | null;
  tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>;
  /** A timestamp in RFC 3339 format */
  updated_at: string; // format: date-time
  /** The agent's current version. Starts at 1 and increments when the agent is modified. */
  version: number; // format: int32
}
```

## Types

```ts
type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";

type BetaManagedAgentsExecutionIdentity = BetaManagedAgentsAWSRoleExecutionIdentity | BetaManagedAgentsServiceAccountExecutionIdentity;

/** URL-based MCP server connection as returned in API responses. */
interface BetaManagedAgentsMCPServerURLDefinition {
  type: "url";
  name: string;
  url: string;
}

interface BetaManagedAgentsModelConfig {
  /** The model that will power your agent. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  id: BetaManagedAgentsModel;
  /** How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied. */
  effort?: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | BetaManagedAgentsEffortXhigh | BetaManagedAgentsEffortMax;
  /** Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. */
  inference_geo?: string;
  /** Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time. */
  speed?: "standard" | "fast";
}

type BetaManagedAgentsMultiagent = BetaManagedAgentsMultiagentCoordinator | BetaManagedAgentsMultiagent20261001;

/** A resolved Anthropic-managed skill. */
interface BetaManagedAgentsAnthropicSkill {
  type: "anthropic";
  skill_id: string;
  version: string;
}

/** A resolved user-created custom skill. */
interface BetaManagedAgentsCustomSkill {
  type: "custom";
  skill_id: string;
  version: string;
}

interface BetaManagedAgentsAgentToolset20260401 {
  type: "agent_toolset_20260401";
  configs: Array<BetaManagedAgentsAgentToolConfig>;
  /** Resolved default configuration for agent tools. */
  default_config: BetaManagedAgentsAgentToolsetDefaultConfig;
}

interface BetaManagedAgentsMCPToolset {
  type: "mcp_toolset";
  configs: Array<BetaManagedAgentsMCPToolConfig>;
  /** Resolved default configuration for all tools from an MCP server. */
  default_config: BetaManagedAgentsMCPToolsetDefaultConfig;
  mcp_server_name: string;
}

/** A custom tool as returned in API responses. */
interface BetaManagedAgentsCustomTool {
  type: "custom";
  description: string;
  /** JSON Schema for custom tool input parameters. */
  input_schema: BetaManagedAgentsCustomToolInputSchema;
  name: string;
}

/** An AWS IAM role principal as returned in API responses. */
interface BetaManagedAgentsAWSRoleExecutionIdentity {
  type: "aws_role";
  /** The IAM role's ARN. */
  role_arn: string;
}

/** The Anthropic-managed service account as returned in API responses. */
interface BetaManagedAgentsServiceAccountExecutionIdentity {
  type: "service_account";
}

type BetaManagedAgentsModel =
  /** Built for the most ambitious work in coding, enterprise workflows, and the sciences */
  | "claude-fable-5-2"
  /** Fastest model for high-volume, real-time tasks */
  | "claude-haiku-5-5"
  /** Efficient model for coding and agents */
  | "claude-sonnet-5-5"
  /** Powerful intelligence for coding, knowledge work, and long-running agents */
  | "claude-opus-5-5"
  /** Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows */
  | "claude-fable-5-1"
  /** Efficient model for coding and agents */
  | "claude-sonnet-5"
  /** Next generation of intelligence for the hardest knowledge work and coding problems */
  | "claude-fable-5"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-5"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-8"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-7"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-6"
  /** Best combination of speed and intelligence */
  | "claude-sonnet-4-6"
  | "claude-haiku-4-5"
  | "claude-haiku-4-5-20251001"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-5"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-5-20251101"
  /**
   * High-performance model for agents and coding
   * @deprecated Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
   */
  | "claude-sonnet-4-5"
  /**
   * High-performance model for agents and coding
   * @deprecated Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
   */
  | "claude-sonnet-4-5-20250929"
  | (string & {});

/** Low effort. Favors latency over reasoning depth. */
interface BetaManagedAgentsEffortLow {
  type: "low";
}

/** Medium effort. Balances latency and reasoning depth. */
interface BetaManagedAgentsEffortMedium {
  type: "medium";
}

/** High effort. Favors reasoning depth. */
interface BetaManagedAgentsEffortHigh {
  type: "high";
}

/** Extra-high effort. Not all models accept this level. */
interface BetaManagedAgentsEffortXhigh {
  type: "xhigh";
}

/** Maximum effort. Favors reasoning depth over latency. */
interface BetaManagedAgentsEffortMax {
  type: "max";
}

/** Resolved coordinator topology with a concrete agent roster. */
interface BetaManagedAgentsMultiagentCoordinator {
  type: "coordinator";
  /** Agents the coordinator may spawn as session threads, each resolved to a specific version. */
  agents: Array<BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor>;
}

/** Resolved multiagent configuration with three members, each enabled or disabled on its own. */
interface BetaManagedAgentsMultiagent20261001 {
  type: "multiagent_20261001";
  /** Whether the session's primary thread can consult an advisor model. */
  advisor: BetaManagedAgentsMultiagentAdvisor;
  /** Whether the agent can spawn session threads. */
  subagents: BetaManagedAgentsMultiagentSubagents;
  /** Whether the agent can start workflow runs. */
  workflows: BetaManagedAgentsMultiagentWorkflows;
}

/** A resolved agent reference with a concrete version. */
interface BetaManagedAgentsAgentReference {
  type: "agent";
  id: string;
  version: number; // format: int32
}

/** Platform advisor roster entry: a model the session's primary thread may consult mid-turn. */
interface BetaManagedAgentsAdvisor {
  type: "advisor";
  /** The advisor model id. */
  model: string;
}

type BetaManagedAgentsMultiagentAdvisor = BetaManagedAgentsMultiagentAdvisorEnabled | BetaManagedAgentsMultiagentAdvisorDisabled;

type BetaManagedAgentsMultiagentSubagents = BetaManagedAgentsMultiagentSubagentsEnabled | BetaManagedAgentsMultiagentSubagentsDisabled;

type BetaManagedAgentsMultiagentWorkflows = BetaManagedAgentsMultiagentWorkflowsEnabled | BetaManagedAgentsMultiagentWorkflowsDisabled;

/** The session's primary thread can consult `model` mid-turn. */
interface BetaManagedAgentsMultiagentAdvisorEnabled {
  type: "enabled";
  /** The advisor model id. */
  model: string;
}

/** The agent has no advisor. */
interface BetaManagedAgentsMultiagentAdvisorDisabled {
  type: "disabled";
}

/** The agent can start workflow runs. */
interface BetaManagedAgentsMultiagentWorkflowsEnabled {
  type: "enabled";
  /** Whether a run's plan can define inline agents, which are not saved. */
  inline_agents: BetaManagedAgentsMultiagentInlineAgents;
  /** Predefined agents, which are saved agents that a run's plan can use, each resolved to a specific version. */
  predefined_agents: Array<BetaManagedAgentsAgentReference>;
}

/** The agent cannot start workflow runs. */
interface BetaManagedAgentsMultiagentWorkflowsDisabled {
  type: "disabled";
}

/** The agent can spawn session threads. */
interface BetaManagedAgentsMultiagentSubagentsEnabled {
  type: "enabled";
  /** Whether the agent can define inline agents, which are not saved, when it spawns session threads. */
  inline_agents: BetaManagedAgentsMultiagentInlineAgents;
  /** Predefined agents, which are saved agents that this agent can spawn as session threads, each resolved to a specific version. */
  predefined_agents: Array<BetaManagedAgentsAgentReference>;
}

/** The agent cannot spawn session threads. */
interface BetaManagedAgentsMultiagentSubagentsDisabled {
  type: "disabled";
}

type BetaManagedAgentsMultiagentInlineAgents = BetaManagedAgentsMultiagentInlineAgentsEnabled | BetaManagedAgentsMultiagentInlineAgentsDisabled;

/** The agent can define inline agents. */
interface BetaManagedAgentsMultiagentInlineAgentsEnabled {
  type: "enabled";
}

/** The agent cannot define inline agents. */
interface BetaManagedAgentsMultiagentInlineAgentsDisabled {
  type: "disabled";
}

/** Resolved configuration for a specific MCP tool. */
interface BetaManagedAgentsMCPToolConfig {
  enabled: boolean;
  name: string;
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

interface BetaManagedAgentsMCPToolsetDefaultConfig {
  enabled: boolean;
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

interface BetaManagedAgentsCustomToolInputSchema {
  type: "object";
  properties?: Record<string, unknown> | null;
  required?: Array<string> | null;
}

/** Configuration for a specific agent tool. */
type BetaManagedAgentsAgentToolConfig = BetaManagedAgentsBashToolConfig | BetaManagedAgentsEditToolConfig | BetaManagedAgentsReadToolConfig | BetaManagedAgentsWriteToolConfig | BetaManagedAgentsGlobToolConfig | BetaManagedAgentsGrepToolConfig | BetaManagedAgentsWebFetchToolConfig | BetaManagedAgentsWebSearchToolConfig;

interface BetaManagedAgentsAgentToolsetDefaultConfig {
  enabled: boolean;
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the bash tool. */
interface BetaManagedAgentsBashToolConfig {
  type: "bash";
  enabled: boolean;
  name: "bash";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the edit tool. */
interface BetaManagedAgentsEditToolConfig {
  type: "edit";
  enabled: boolean;
  name: "edit";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the read tool. */
interface BetaManagedAgentsReadToolConfig {
  type: "read";
  enabled: boolean;
  name: "read";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the write tool. */
interface BetaManagedAgentsWriteToolConfig {
  type: "write";
  enabled: boolean;
  name: "write";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the glob tool. */
interface BetaManagedAgentsGlobToolConfig {
  type: "glob";
  enabled: boolean;
  name: "glob";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the grep tool. */
interface BetaManagedAgentsGrepToolConfig {
  type: "grep";
  enabled: boolean;
  name: "grep";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the web_fetch tool. */
interface BetaManagedAgentsWebFetchToolConfig {
  type: "web_fetch";
  enabled: boolean;
  name: "web_fetch";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
  /** Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source. */
  url_sources: BetaManagedAgentsWebFetchURLSources | null;
  allowed_domains?: Array<string>;
  blocked_domains?: Array<string>;
  max_content_tokens?: number | null; // format: int32
}

/** Configuration for the web_search tool. */
interface BetaManagedAgentsWebSearchToolConfig {
  type: "web_search";
  enabled: boolean;
  name: "web_search";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
  allowed_domains?: Array<string>;
  blocked_domains?: Array<string>;
  /** Approximate user location for search result localization. */
  user_location?: BetaManagedAgentsUserLocation | null;
}

/** Tool calls are automatically approved without user confirmation. */
interface BetaManagedAgentsAlwaysAllowPolicy {
  type: "always_allow";
}

/** Tool calls require user confirmation before execution. */
interface BetaManagedAgentsAlwaysAskPolicy {
  type: "always_ask";
}

/** The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit. */
interface BetaManagedAgentsAutoPolicy {
  type: "auto";
}

interface BetaManagedAgentsUserLocation {
  /** Location precision. Only "approximate" is supported. */
  type: "approximate";
  /** City name. */
  city?: string | null; // minLength: 1, maxLength: 255
  /** Two-letter ISO 3166-1 country code, uppercase. */
  country?: string | null; // pattern: ^[A-Z]{2}$
  /** Region or state name. */
  region?: string | null; // minLength: 1, maxLength: 255
  /** IANA timezone identifier, e.g. "America/Los_Angeles". */
  timezone?: string | null; // minLength: 1, maxLength: 255
}

interface BetaManagedAgentsWebFetchURLSources {
  /** Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results. */
  client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | null;
  /** Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both. */
  server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | null;
  /** Whether URLs in the text of user messages may be fetched. Null when not set, which allows them. */
  user_input: BetaManagedAgentsWebFetchURLSourceUserInput | null;
}

type BetaManagedAgentsWebFetchURLSourceToolFilter = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone | BetaManagedAgentsWebFetchURLSourceOnly | BetaManagedAgentsWebFetchURLSourceExcept;

type BetaManagedAgentsWebFetchURLSourceUserInput = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone;

/** Every URL from this source may be fetched. This is the default. */
interface BetaManagedAgentsWebFetchURLSourceAll {
  type: "all";
}

/** This source contributes no URLs that may be fetched. */
interface BetaManagedAgentsWebFetchURLSourceNone {
  type: "none";
}

/** Only the named tools' results contribute URLs that may be fetched. */
interface BetaManagedAgentsWebFetchURLSourceOnly {
  type: "only";
  /** The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results. */
  tools: Array<BetaManagedAgentsWebFetchURLSourceToolReference>;
}

/** Every tool's results contribute URLs that may be fetched, except the named tools' results. */
interface BetaManagedAgentsWebFetchURLSourceExcept {
  type: "except";
  /** The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results. */
  tools: Array<BetaManagedAgentsWebFetchURLSourceToolReference>;
}

interface BetaManagedAgentsWebFetchURLSourceToolReference {
  /** Must be "tool_reference". */
  type: "tool_reference";
  /** Name of the tool. Compared exactly, so upper and lower case letters are different. */
  name: string; // minLength: 1, maxLength: 128
}
```
