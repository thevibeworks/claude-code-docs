---
title: Update Agent
url: https://platform.claude.com/docs/en/api/typescript/beta/agents/update
---

# Update Agent

- Signature: `client.beta.agents.update(agentID: string, params: AgentUpdateParams, options?: RequestOptions): BetaManagedAgentsAgent`
- Endpoint: `POST /v1/agents/{agent_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsAgent = await client.beta.agents.update(
  "agent_011CZkYpogX7uDKUyvBTophP",
  { description: "updated" }
);

console.log(betaManagedAgentsAgent.id);
```

## Example response (200)

```json
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
```

## Parameters

```ts
/** Unique identifier of the agent to update. */
agentID: string; // path parameter

interface AgentUpdateParams {
  /** Description. Omit to preserve; send empty string or null to clear. */
  description?: string | null; // maxLength: 2048
  /** Execution principal for runs of this agent. Full replacement. Omit to preserve; send null or `{"type": "service_account"}` to restore the default. */
  execution_identity?: BetaManagedAgentsExecutionIdentityParams | null;
  /** MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector?sdk_languages=typescript). */
  mcp_servers?: Array<BetaManagedAgentsURLMCPServerParams> | null;
  /** Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars. */
  metadata?: Record<string, string | null> | null;
  /** Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview?sdk_languages=typescript#latest-models-comparison), e.g. `claude-opus-5-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared. */
  model?: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams;
  /** Multiagent orchestration configuration. Full replacement. Omit to preserve; send null to clear. */
  multiagent?: BetaManagedAgentsMultiagentParams | null;
  /** Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared. */
  name?: string; // maxLength: 256
  /** Skills. Full replacement. Omit to preserve; send empty array or null to clear. */
  skills?: Array<BetaManagedAgentsSkillParams> | null;
  /** System prompt. Omit to preserve; send empty string or null to clear. */
  system?: string | null; // maxLength: 100000
  /** Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 256 tools across all toolsets allowed. */
  tools?: Array<BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams> | null;
  /** The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally. */
  version?: number; // format: int32
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
type BetaManagedAgentsExecutionIdentityParams = BetaManagedAgentsAWSRoleExecutionIdentityParams | BetaManagedAgentsServiceAccountExecutionIdentityParams;

interface BetaManagedAgentsURLMCPServerParams {
  type: "url";
  /** Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters. */
  name: string; // minLength: 1, maxLength: 255
  /** Endpoint URL for the MCP server. */
  url: string; // maxLength: 2048
}

/** The model that will power your agent. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
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

/** An object that defines additional configuration control over model use */
interface BetaManagedAgentsModelConfigParams {
  /** The model that will power your agent. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  id: BetaManagedAgentsModel;
  /**
   * How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.
   * - `"low"`: Low effort. Favors latency over reasoning depth.
   * - `"medium"`: Medium effort. Balances latency and reasoning depth.
   * - `"high"`: High effort. Favors reasoning depth.
   * - `"xhigh"`: Extra-high effort. Not all models accept this level.
   * - `"max"`: Maximum effort. Favors reasoning depth over latency.
   */
  effort?: "low" | "medium" | "high" | "xhigh" | "max" | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | BetaManagedAgentsEffortXhigh | BetaManagedAgentsEffortMax | null;
  /** Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it. */
  inference_geo?: string | null;
  /** Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time. */
  speed?: "standard" | "fast" | null;
}

type BetaManagedAgentsMultiagentParams = BetaManagedAgentsMultiagentCoordinatorParams | BetaManagedAgentsMultiagent20261001Params;

type BetaManagedAgentsSkillParams = BetaManagedAgentsAnthropicSkillParams | BetaManagedAgentsCustomSkillParams;

/** Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent. */
interface BetaManagedAgentsAgentToolset20260401Params {
  type: "agent_toolset_20260401";
  /** Per-tool configuration overrides. */
  configs?: Array<BetaManagedAgentsAgentToolConfigParams>;
  /** Default configuration applied to all tools in this set. */
  default_config?: BetaManagedAgentsAgentToolsetDefaultConfigParams | null;
}

/** Configuration for tools from an MCP server defined in `mcp_servers`. */
interface BetaManagedAgentsMCPToolsetParams {
  type: "mcp_toolset";
  /** Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters. */
  mcp_server_name: string; // minLength: 1, maxLength: 255
  /** Per-tool configuration overrides. */
  configs?: Array<BetaManagedAgentsMCPToolConfigParams>;
  /** Default configuration for all tools from this server. */
  default_config?: BetaManagedAgentsMCPToolsetDefaultConfigParams | null;
}

/** A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event. */
interface BetaManagedAgentsCustomToolParams {
  type: "custom";
  /** Description of what the tool does, shown to the agent to help it decide when to use the tool. */
  description: string; // minLength: 1
  /** JSON Schema defining the expected input parameters for the tool. */
  input_schema: BetaManagedAgentsCustomToolInputSchema;
  /** Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens. */
  name: string; // minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$
}

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

/** An AWS IAM role principal. */
interface BetaManagedAgentsAWSRoleExecutionIdentityParams {
  type: "aws_role";
  /** The IAM role's ARN, e.g. "arn:aws:iam::123456789012:role/my-agent-runner". Maximum 2048 characters. */
  role_arn: string; // maxLength: 2048, pattern: ^arn:aws(-[a-z]+)*:iam::[0-9]{12}:role/[\w+=,.@/-]+$
}

/** The Anthropic-managed service account — the default execution principal. Carries no identifier. */
interface BetaManagedAgentsServiceAccountExecutionIdentityParams {
  type: "service_account";
}

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

/** A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster. */
interface BetaManagedAgentsMultiagentCoordinatorParams {
  type: "coordinator";
  /** Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1). */
  agents: Array<BetaManagedAgentsMultiagentRosterEntryParams>;
}

/** Multiagent configuration with three members, each enabled or disabled on its own. On an update, if the agent's stored `multiagent` also has type `multiagent_20261001`, this configuration is merged into the stored one, level by level, instead of replacing it. A key that the update omits keeps its stored value. A key sent as null takes its default, on create as well, so `"workflows": null` enables workflows. An object sent with a `type` other than the stored one replaces the stored object, and the keys that it omits take their defaults. A `predefined_agents` list that is sent replaces the stored list. Every object that is sent needs its `type`, and an enabled `advisor` needs its `model`. Other validation applies to the merged result. */
interface BetaManagedAgentsMultiagent20261001Params {
  type: "multiagent_20261001";
  /** Whether the session's primary thread can consult an advisor model. Defaults to disabled. */
  advisor?: BetaManagedAgentsMultiagentAdvisorParams | null;
  /** Whether the agent can spawn session threads. Defaults to enabled. */
  subagents?: BetaManagedAgentsMultiagentSubagentsParams | null;
  /** Whether the agent can start workflow runs. Defaults to enabled. */
  workflows?: BetaManagedAgentsMultiagentWorkflowsParams | null;
}

type BetaManagedAgentsMultiagentRosterEntryParams = string | BetaManagedAgentsAgentParams | BetaManagedAgentsMultiagentSelfParams | BetaManagedAgentsAdvisorParams;

/** Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version */
interface BetaManagedAgentsAgentParams {
  type: "agent";
  /** The `agent` ID. */
  id: string; // minLength: 1, maxLength: 128
  /** The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified. */
  version?: number; // format: int32
}

/** Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference. */
interface BetaManagedAgentsMultiagentSelfParams {
  type: "self";
}

/** Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`. */
interface BetaManagedAgentsAdvisorParams {
  type: "advisor";
  /** A Claude model id. The model must be permitted as an advisor for this agent's model. */
  model: string; // minLength: 1, maxLength: 256
}

type BetaManagedAgentsMultiagentAdvisorParams = BetaManagedAgentsMultiagentAdvisorEnabledParams | BetaManagedAgentsMultiagentAdvisorDisabledParams;

type BetaManagedAgentsMultiagentSubagentsParams = BetaManagedAgentsMultiagentSubagentsEnabledParams | BetaManagedAgentsMultiagentSubagentsDisabledParams;

type BetaManagedAgentsMultiagentWorkflowsParams = BetaManagedAgentsMultiagentWorkflowsEnabledParams | BetaManagedAgentsMultiagentWorkflowsDisabledParams;

/** The session's primary thread can consult `model` mid-turn. */
interface BetaManagedAgentsMultiagentAdvisorEnabledParams {
  type: "enabled";
  /** A Claude model id. The model must be permitted as an advisor for this agent's model. */
  model: string; // minLength: 1, maxLength: 256
}

/** The agent has no advisor. */
interface BetaManagedAgentsMultiagentAdvisorDisabledParams {
  type: "disabled";
}

/** The agent can start workflow runs. Each run follows a plan, a program that the agent writes. A plan can use predefined agents, which are the saved agents in `predefined_agents`, and inline agents, which it defines itself and which are not saved. If `inline_agents` is disabled, `predefined_agents` must name at least one agent. */
interface BetaManagedAgentsMultiagentWorkflowsEnabledParams {
  type: "enabled";
  /** Whether a run's plan can define inline agents. Defaults to enabled. */
  inline_agents?: BetaManagedAgentsMultiagentInlineAgentsParams | null;
  /** Predefined agents that a run's plan can use. At most 20. Defaults to null. Null and an empty list both mean no predefined agents. This list is separate from `subagents.predefined_agents`, and an agent in one list is not added to the other. */
  predefined_agents?: Array<BetaManagedAgentsMultiagentPredefinedAgentParams> | null;
}

/** The agent cannot start workflow runs. */
interface BetaManagedAgentsMultiagentWorkflowsDisabledParams {
  type: "disabled";
}

/** The agent can spawn session threads. Each thread runs a predefined agent, which is a saved agent in `predefined_agents`, or an inline agent, which the agent defines when it spawns the thread and which is not saved. If `inline_agents` is disabled, `predefined_agents` must name at least one agent. */
interface BetaManagedAgentsMultiagentSubagentsEnabledParams {
  type: "enabled";
  /** Whether the agent can define inline agents when it spawns session threads. Defaults to enabled. */
  inline_agents?: BetaManagedAgentsMultiagentInlineAgentsParams | null;
  /** Predefined agents that this agent can spawn as session threads. At most 20. Defaults to null. Null and an empty list both mean no predefined agents. This list is separate from `workflows.predefined_agents`, and an agent in one list is not added to the other. */
  predefined_agents?: Array<BetaManagedAgentsMultiagentPredefinedAgentParams> | null;
}

/** The agent cannot spawn session threads. */
interface BetaManagedAgentsMultiagentSubagentsDisabledParams {
  type: "disabled";
}

type BetaManagedAgentsMultiagentInlineAgentsParams = BetaManagedAgentsMultiagentInlineAgentsEnabledParams | BetaManagedAgentsMultiagentInlineAgentsDisabledParams;

type BetaManagedAgentsMultiagentPredefinedAgentParams = string | BetaManagedAgentsAgentParams | BetaManagedAgentsMultiagentSelfParams;

/** The agent can define inline agents. */
interface BetaManagedAgentsMultiagentInlineAgentsEnabledParams {
  type: "enabled";
}

/** The agent cannot define inline agents. */
interface BetaManagedAgentsMultiagentInlineAgentsDisabledParams {
  type: "disabled";
}

/** An Anthropic-managed skill. */
interface BetaManagedAgentsAnthropicSkillParams {
  type: "anthropic";
  /** Identifier of the Anthropic skill (e.g., "xlsx"). */
  skill_id: string; // minLength: 1, maxLength: 64
  /** Version to pin. Defaults to latest if omitted. */
  version?: string | null; // minLength: 1, maxLength: 64
}

/** A user-created custom skill. */
interface BetaManagedAgentsCustomSkillParams {
  type: "custom";
  /** Tagged ID of the custom skill (e.g., "skill_01XJ5..."). */
  skill_id: string; // minLength: 1, maxLength: 64
  /** Version to pin. Defaults to latest if omitted. */
  version?: string | null; // minLength: 1, maxLength: 64
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

interface BetaManagedAgentsWebFetchURLSources {
  /** Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results. */
  client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | null;
  /** Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both. */
  server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | null;
  /** Whether URLs in the text of user messages may be fetched. Null when not set, which allows them. */
  user_input: BetaManagedAgentsWebFetchURLSourceUserInput | null;
}

interface BetaManagedAgentsMCPToolConfigParams {
  /** Name of the MCP tool to configure. 1-128 characters. */
  name: string; // minLength: 1, maxLength: 128
  /** Whether this tool is enabled. Overrides the `default_config` setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Overrides the `default_config` setting. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

interface BetaManagedAgentsMCPToolsetDefaultConfigParams {
  /** Whether tools are enabled by default. Defaults to true if not specified. */
  enabled?: boolean | null;
  /** Default permission policy for tools from this server. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

interface BetaManagedAgentsCustomToolInputSchema {
  type: "object";
  properties?: Record<string, unknown> | null;
  required?: Array<string> | null;
}

type BetaManagedAgentsAgentToolConfigParams = BetaManagedAgentsBashToolConfigParams | BetaManagedAgentsEditToolConfigParams | BetaManagedAgentsReadToolConfigParams | BetaManagedAgentsWriteToolConfigParams | BetaManagedAgentsGlobToolConfigParams | BetaManagedAgentsGrepToolConfigParams | BetaManagedAgentsWebFetchToolConfigParams | BetaManagedAgentsWebSearchToolConfigParams;

interface BetaManagedAgentsAgentToolsetDefaultConfigParams {
  /** Whether tools are enabled and available to Claude by default. Defaults to true if not specified. */
  enabled?: boolean | null;
  /** Default permission policy for tools. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the bash tool. */
interface BetaManagedAgentsBashToolConfigParams {
  type?: "bash";
  /** Must be "bash". */
  name: "bash";
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the edit tool. */
interface BetaManagedAgentsEditToolConfigParams {
  type?: "edit";
  /** Must be "edit". */
  name: "edit";
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the read tool. */
interface BetaManagedAgentsReadToolConfigParams {
  type?: "read";
  /** Must be "read". */
  name: "read";
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the write tool. */
interface BetaManagedAgentsWriteToolConfigParams {
  type?: "write";
  /** Must be "write". */
  name: "write";
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the glob tool. */
interface BetaManagedAgentsGlobToolConfigParams {
  type?: "glob";
  /** Must be "glob". */
  name: "glob";
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the grep tool. */
interface BetaManagedAgentsGrepToolConfigParams {
  type?: "grep";
  /** Must be "grep". */
  name: "grep";
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
}

/** Configuration override for the web_fetch tool. */
interface BetaManagedAgentsWebFetchToolConfigParams {
  type?: "web_fetch";
  /** Must be "web_fetch". */
  name: "web_fetch";
  /** Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains. */
  allowed_domains?: Array<string>;
  /** Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains. */
  blocked_domains?: Array<string>;
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // format: int32
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
  /** Which sources contribute URLs the tool may fetch. Omit to allow every source. */
  url_sources?: BetaManagedAgentsWebFetchURLSourcesParams | null;
}

/** Configuration override for the web_search tool. */
interface BetaManagedAgentsWebSearchToolConfigParams {
  type?: "web_search";
  /** Must be "web_search". */
  name: "web_search";
  /** Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains. */
  allowed_domains?: Array<string>;
  /** Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains. */
  blocked_domains?: Array<string>;
  /** Whether this tool is enabled and available to Claude. Overrides the default_config setting. */
  enabled?: boolean | null;
  /** Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation. */
  permission_policy?: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | null;
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

interface BetaManagedAgentsWebFetchURLSourcesParams {
  /** Which custom tools' results contribute URLs that may be fetched: "all" (the default), "none", or an only or except list. Each name in a list must be a custom tool in the same tools array. */
  client_tool_results?: BetaManagedAgentsWebFetchURLSourceToolFilterParams | null;
  /** Which of the web_search and web_fetch tools' results contribute URLs that may be fetched: "all" (the default), "none", or an only or except list. Each name in a list must be "web_search" or "web_fetch". */
  server_tool_results?: BetaManagedAgentsWebFetchURLSourceToolFilterParams | null;
  /** Whether URLs in the text of user messages may be fetched: "all" (the default) or "none". */
  user_input?: BetaManagedAgentsWebFetchURLSourceUserInputParams | null;
}

type BetaManagedAgentsWebFetchURLSourceToolFilterParams = BetaManagedAgentsWebFetchURLSourceShorthand | BetaManagedAgentsWebFetchURLSourceToolFilter;

type BetaManagedAgentsWebFetchURLSourceUserInputParams = BetaManagedAgentsWebFetchURLSourceShorthand | BetaManagedAgentsWebFetchURLSourceUserInput;

/** Whether URLs in the text of user messages may be fetched. */
type BetaManagedAgentsWebFetchURLSourceUserInput = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone;

/** String form of a url_sources value that has no field other than its type: "all" means {"type": "all"} and "none" means {"type": "none"}. */
type BetaManagedAgentsWebFetchURLSourceShorthand = "all" | "none";

/** Which tools' results contribute URLs that may be fetched. */
type BetaManagedAgentsWebFetchURLSourceToolFilter = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone | BetaManagedAgentsWebFetchURLSourceOnly | BetaManagedAgentsWebFetchURLSourceExcept;

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
