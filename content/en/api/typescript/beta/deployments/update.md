---
title: Update Deployment
url: https://platform.claude.com/docs/en/api/typescript/beta/deployments/update
---

# Update Deployment

- Signature: `client.beta.deployments.update(deploymentID: string, params: DeploymentUpdateParams, options?: RequestOptions): BetaManagedAgentsDeployment`
- Endpoint: `POST /v1/deployments/{deployment_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeployment = await client.beta.deployments.update(
  "depl_011CZkZcDH3vPqd7xnEfwTai",
  {}
);

console.log(betaManagedAgentsDeployment.id);
```

## Example response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": null,
  "resources": [],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Parameters

```ts
/** Unique identifier of the deployment to update. */
deploymentID: string; // path parameter

interface DeploymentUpdateParams {
  /** Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared. */
  agent?: string | BetaManagedAgentsAgentParams;
  /** Spend ceiling for future sessions. Full replacement. Omit to preserve; send null to clear (sessions created afterwards are uncapped). The deployment agent's model must have a public list price, or the request is rejected; a multiagent roster is re-validated in full when each fire copies the cap, which fails closed the same way. */
  budget?: BetaManagedAgentsBudgetLimit | null;
  /** Description. Omit to preserve; send empty string or null to clear. */
  description?: string | null; // maxLength: 2048
  /** ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared. */
  environment_id?: string; // maxLength: 128
  /** Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50. */
  initial_events?: Array<BetaManagedAgentsDeploymentInitialEventParams>;
  /** Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars. */
  metadata?: Record<string, string | null> | null;
  /** Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared. */
  name?: string; // maxLength: 256
  /** Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500. */
  resources?: Array<BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam> | null;
  /** Cron schedule. Full replacement. Omit to preserve; send null to clear (revert to manual-only). */
  schedule?: BetaManagedAgentsScheduleParams | null;
  /** Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50. */
  vault_ids?: Array<string> | null;
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule. */
interface BetaManagedAgentsDeployment {
  type: "deployment";
  /** Unique identifier for this deployment. */
  id: string;
  /** Reference to the agent this deployment runs, resolved to a concrete version. */
  agent: BetaManagedAgentsAgentReference;
  /** Time the deployment was archived. Null if not archived. */
  archived_at: string | null; // format: date-time
  /** Time the deployment was created. */
  created_at: string; // format: date-time
  /** Description of what the deployment does. */
  description: string | null;
  /** ID of the `environment` where sessions run. */
  environment_id: string;
  /** Events sent to each session immediately after creation. */
  initial_events: Array<BetaManagedAgentsDeploymentInitialEvent>;
  /** Arbitrary key-value metadata. Maximum 16 pairs. */
  metadata: Record<string, string>;
  /** Human-readable name. */
  name: string;
  /** Why the deployment is `paused`. Non-null exactly when `status` is `paused`; null otherwise. */
  paused_reason: BetaManagedAgentsDeploymentPausedReason | null;
  /** Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials. */
  resources: Array<BetaManagedAgentsSessionResourceConfig>;
  /** Recurring cron schedule. Presence enables scheduled execution; null means manual-only. Includes computed timestamps (next fire times, last run) on the cron variant. */
  schedule: BetaManagedAgentsSchedule | null;
  /** Computed status of the deployment: `active` or `paused`. Archived deployments report `active` with `archived_at` set. */
  status: BetaManagedAgentsDeploymentStatus;
  /** Time the deployment was last updated. */
  updated_at: string; // format: date-time
  /** Vault IDs supplying stored credentials for sessions created from this deployment. */
  vault_ids: Array<string>;
  /** Spend ceiling stamped onto each session created from this deployment. Absent when no budget is set. */
  budget?: BetaManagedAgentsBudgetLimit | null;
}
```

## Types

```ts
/** Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version */
interface BetaManagedAgentsAgentParams {
  type: "agent";
  /** The `agent` ID. */
  id: string; // minLength: 1, maxLength: 128
  /** The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified. */
  version?: number; // format: int32
}

interface BetaManagedAgentsBudgetLimit {
  type: "limit";
  /** Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge. */
  max_list_cost: BetaMonetaryAmount;
}

type BetaManagedAgentsDeploymentInitialEventParams = BetaManagedAgentsUserMessageEventParams | BetaManagedAgentsUserDefineOutcomeEventParams | BetaManagedAgentsSystemMessageEventParams;

/** Mount a GitHub repository into the session's container. */
interface BetaManagedAgentsGitHubRepositoryResourceParams {
  type: "github_repository";
  /** Github URL of the repository */
  url: string; // minLength: 1, maxLength: 2048
  /** GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones. */
  authorization_token?: string; // minLength: 1, maxLength: 4096
  /** Branch or commit to check out. Defaults to the repository's default branch. */
  checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null;
  /** Mount path in the container. Defaults to `/workspace/<repo-name>`. */
  mount_path?: string | null; // minLength: 1, maxLength: 4096
}

/** Mount a file uploaded via the Files API into the session. */
interface BetaManagedAgentsFileResourceParams {
  type: "file";
  /** ID of a previously uploaded file. */
  file_id: string; // minLength: 1, maxLength: 128
  /** Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`. */
  mount_path?: string | null; // minLength: 1, maxLength: 4096
}

/** Parameters for attaching a memory store to an agent session. */
interface BetaManagedAgentsMemoryStoreResourceParam {
  type: "memory_store";
  /** The memory store ID (memstore_...). Must belong to the caller's organization and workspace. */
  memory_store_id: string; // pattern: ^memstore_[a-zA-Z0-9_]+$
  /** Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem. */
  access?: "read_write" | "read_only" | null;
  /** Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars. */
  instructions?: string | null; // maxLength: 4096
}

interface BetaManagedAgentsScheduleParams {
  type: "cron";
  /** 5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily). */
  expression: string; // minLength: 1, maxLength: 256
  /** Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database. */
  timezone: string; // minLength: 1
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

interface BetaManagedAgentsAgentReference {
  type: "agent";
  id: string;
  version: number; // format: int32
}

type BetaManagedAgentsDeploymentInitialEvent = BetaManagedAgentsDeploymentUserMessageEvent | BetaManagedAgentsDeploymentUserDefineOutcomeEvent | BetaManagedAgentsDeploymentSystemMessageEvent;

type BetaManagedAgentsDeploymentPausedReason = BetaManagedAgentsManualDeploymentPausedReason | BetaManagedAgentsErrorDeploymentPausedReason;

type BetaManagedAgentsSessionResourceConfig = BetaManagedAgentsGitHubRepositoryResourceConfig | BetaManagedAgentsFileResourceConfig | BetaManagedAgentsMemoryStoreResourceConfig;

interface BetaManagedAgentsSchedule {
  type: "cron";
  /** 5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily). */
  expression: string; // minLength: 1, maxLength: 256
  /** IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). */
  timezone: string; // minLength: 1
  /** Time the most recent scheduled run actually started. Null until one completes; preserved after the deployment is archived. Manual runs do not update this. */
  last_run_at?: string | null; // format: date-time
  /** Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time. */
  upcoming_runs_at?: Array<string>;
}

type BetaManagedAgentsDeploymentStatus =
  /** The deployment is active and can run sessions. Archived deployments also report this status; check `archived_at` to distinguish them. */
  | "active"
  /** The deployment is paused. Autonomous triggers are suppressed; manual runs are still permitted. */
  | "paused";

interface BetaMonetaryAmount {
  /** Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied. */
  amount: string; // pattern: ^(0|[1-9]\d*)$
  /** Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced. */
  currency: BetaCurrency;
}

type BetaCurrency = "USD";

interface BetaManagedAgentsBranchCheckout {
  type: "branch";
  /** Branch name to check out. */
  name: string; // minLength: 1, maxLength: 255
}

interface BetaManagedAgentsCommitCheckout {
  type: "commit";
  /** Full commit SHA to check out. */
  sha: string; // minLength: 7, maxLength: 64, pattern: ^[0-9a-fA-F]+$
}

/** A user message sent to the session. */
interface BetaManagedAgentsDeploymentUserMessageEvent {
  type: "user.message";
  /** Array of content blocks for the user message. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>;
}

/** An outcome the agent should work toward. The agent begins work on receipt. */
interface BetaManagedAgentsDeploymentUserDefineOutcomeEvent {
  type: "user.define_outcome";
  /** What the agent should produce. This is the task specification. */
  description: string;
  /** How to grade the outcome. Text or file reference. */
  rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric;
  /** Eval→revision cycles before giving up. Default 3, max 20. */
  max_iterations?: number | null; // format: int32
}

/** Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. */
interface BetaManagedAgentsDeploymentSystemMessageEvent {
  type: "system.message";
  /** System content blocks to append. Text-only. */
  content: Array<BetaManagedAgentsSystemContentBlock>;
}

/** Rubric referenced by a file uploaded via the Files API. */
interface BetaManagedAgentsFileRubric {
  type: "file";
  /** ID of the rubric file. */
  file_id: string;
}

/** Rubric content provided inline as text. */
interface BetaManagedAgentsTextRubric {
  type: "text";
  /** Rubric content. Plain text or markdown — the grader treats it as freeform text. */
  content: string;
}

/** The caller invoked the pause endpoint on the deployment. */
interface BetaManagedAgentsManualDeploymentPausedReason {
  type: "manual";
}

/** A scheduled fire recorded a failed run whose error auto-pauses the deployment. */
interface BetaManagedAgentsErrorDeploymentPausedReason {
  type: "error";
  /** The failed run's error. */
  error: BetaManagedAgentsDeploymentPausedReasonError;
}

type BetaManagedAgentsDeploymentPausedReasonError = BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError | BetaManagedAgentsAgentArchivedDeploymentPausedReasonError | BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError | BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError | BetaManagedAgentsFileNotFoundDeploymentPausedReasonError | BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError | BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError | BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError | BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError | BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError | BetaManagedAgentsVaultArchivedDeploymentPausedReasonError | BetaManagedAgentsUnknownDeploymentPausedReasonError | BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError | BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError;

/** The deployment's environment was archived. */
interface BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError {
  type: "environment_archived_error";
}

/** The deployment's agent was archived. */
interface BetaManagedAgentsAgentArchivedDeploymentPausedReasonError {
  type: "agent_archived_error";
}

/** The deployment's environment no longer exists. */
interface BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError {
  type: "environment_not_found_error";
}

/** A vault referenced by the deployment no longer exists. */
interface BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError {
  type: "vault_not_found_error";
}

/** A file resource referenced by the deployment no longer exists. */
interface BetaManagedAgentsFileNotFoundDeploymentPausedReasonError {
  type: "file_not_found_error";
}

/** A referenced resource no longer exists and its kind was not reported. */
interface BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError {
  type: "session_resource_not_found_error";
}

/** The deployment's workspace was archived. */
interface BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError {
  type: "workspace_archived_error";
}

/** The deployment's organization is disabled. */
interface BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError {
  type: "organization_disabled_error";
}

/** A memory store referenced by the deployment is archived. */
interface BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError {
  type: "memory_store_archived_error";
}

/** A skill referenced by the deployment's agent no longer exists. */
interface BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError {
  type: "skill_not_found_error";
}

/** A vault referenced by the deployment is archived. */
interface BetaManagedAgentsVaultArchivedDeploymentPausedReasonError {
  type: "vault_archived_error";
}

/** An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`. */
interface BetaManagedAgentsUnknownDeploymentPausedReasonError {
  type: "unknown_error";
}

/** The deployment configures resources, but its environment is self-hosted and cannot mount them. */
interface BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError {
  type: "self_hosted_resources_unsupported_error";
}

/** An MCP server host used by the deployment's agent is blocked by the environment's network policy. */
interface BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError {
  type: "mcp_egress_blocked_error";
}

/** A GitHub repository mounted into each session's container. The authorization token is write-only and never returned. */
interface BetaManagedAgentsGitHubRepositoryResourceConfig {
  type: "github_repository";
  /** Github URL of the repository */
  url: string;
  /** Branch or commit to check out. Defaults to the repository's default branch. */
  checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null;
  /** Mount path in the container. Defaults to `/workspace/<repo-name>`. */
  mount_path?: string | null;
}

/** A file mounted into each session's container. */
interface BetaManagedAgentsFileResourceConfig {
  type: "file";
  /** ID of a previously uploaded file. */
  file_id: string;
  /** Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`. */
  mount_path?: string | null;
}

/** A memory store attached to each session created from this deployment. */
interface BetaManagedAgentsMemoryStoreResourceConfig {
  type: "memory_store";
  /** The memory store ID (memstore_...). Must belong to the caller's organization and workspace. */
  memory_store_id: string;
  /** Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem. */
  access?: "read_write" | "read_only" | null;
  /** Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars. */
  instructions?: string | null;
}

/** Parameters for sending a user message to the session. */
interface BetaManagedAgentsUserMessageEventParams {
  type: "user.message";
  /** Array of content blocks for the user message. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>;
}

/** Parameters for defining an outcome the agent should work toward. The agent begins work on receipt. */
interface BetaManagedAgentsUserDefineOutcomeEventParams {
  type: "user.define_outcome";
  /** What the agent should produce. This is the task specification. */
  description: string;
  /** How to grade the outcome. Text or file reference. */
  rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams;
  /** Eval→revision cycles before giving up. Default 3, max 20. */
  max_iterations?: number | null; // format: int32
}

/** Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages. */
interface BetaManagedAgentsSystemMessageEventParams {
  type: "system.message";
  /** System content blocks to append. Text-only. */
  content: Array<BetaManagedAgentsSystemContentBlock>;
}

/** Rubric referenced by a file uploaded via the Files API. */
interface BetaManagedAgentsFileRubricParams {
  type: "file";
  /** ID of the rubric file. */
  file_id: string;
}

/** Rubric content provided inline as text. */
interface BetaManagedAgentsTextRubricParams {
  type: "text";
  /** Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters. */
  content: string; // maxLength: 262144
}

interface BetaManagedAgentsSystemContentBlock {
  type: "text";
  /** The text content. */
  text: string; // minLength: 1
}

/** Regular text content. */
interface BetaManagedAgentsTextBlock {
  type: "text";
  /** The text content. */
  text: string; // minLength: 1
}

/** Image content specified directly as base64 data or as a reference via a URL. */
interface BetaManagedAgentsImageBlock {
  type: "image";
  /** The source of the image data. */
  source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource;
}

/** Document content, either specified directly as base64 data, as text, or as a reference via a URL. */
interface BetaManagedAgentsDocumentBlock {
  type: "document";
  /** The source of the document data. */
  source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource;
  /** Additional context about the document for the model. */
  context?: string | null;
  /** The title of the document. */
  title?: string | null;
}

/** Placeholder for content withheld by Anthropic model policy. */
interface BetaManagedAgentsRedactedBlock {
  type: "redacted";
}

/** Base64-encoded image data. */
interface BetaManagedAgentsBase64ImageSource {
  type: "base64";
  /** Base64-encoded image data. */
  data: string; // minLength: 1
  /** MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp"). */
  media_type: string; // minLength: 1
}

/** Image referenced by URL. */
interface BetaManagedAgentsURLImageSource {
  type: "url";
  /** URL of the image to fetch. */
  url: string; // minLength: 1
}

/** Image referenced by file ID. */
interface BetaManagedAgentsFileImageSource {
  type: "file";
  /** ID of a previously uploaded file. */
  file_id: string; // minLength: 1
}

/** Base64-encoded document data. */
interface BetaManagedAgentsBase64DocumentSource {
  type: "base64";
  /** Base64-encoded document data. */
  data: string; // minLength: 1
  /** MIME type of the document (e.g., "application/pdf"). */
  media_type: string; // minLength: 1
}

/** Plain text document content. */
interface BetaManagedAgentsPlainTextDocumentSource {
  type: "text";
  /** The plain text content. */
  data: string; // minLength: 1
  /** MIME type of the text content. Must be "text/plain". */
  media_type: "text/plain";
}

/** Document referenced by URL. */
interface BetaManagedAgentsURLDocumentSource {
  type: "url";
  /** URL of the document to fetch. */
  url: string; // minLength: 1
}

/** Document referenced by file ID. */
interface BetaManagedAgentsFileDocumentSource {
  type: "file";
  /** ID of a previously uploaded file. */
  file_id: string; // minLength: 1
}
```
