---
title: Redact a Memory Version
url: https://platform.claude.com/docs/en/api/typescript/beta/memory_stores/memory_versions/redact
---

# Redact a Memory Version

- Signature: `client.beta.memoryStores.memoryVersions.redact(memoryVersionID: string, params: MemoryVersionRedactParams, options?: RequestOptions): BetaManagedAgentsMemoryVersion`
- Endpoint: `POST /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`
- Beta header: `anthropic-beta: agent-memory-2026-07-22` or `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsMemoryVersion = await client.beta.memoryStores.memoryVersions.redact(
  "memory_version_id",
  { memory_store_id: "memory_store_id" }
);

console.log(betaManagedAgentsMemoryVersion.id);
```

## Example response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Parameters

```ts
/** The ID of the memory version to redact (`memver_...`). */
memoryVersionID: string; // path parameter

interface MemoryVersionRedactParams {
  /** The ID of the memory store that holds the version (`memstore_...`). */
  memory_store_id: string; // path parameter
  /** This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** One entry in a memory's history, recording a single change and who made it. Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#audit-memory-changes) to learn more about memory versions. */
interface BetaManagedAgentsMemoryVersion {
  type: "memory_version";
  /** Unique identifier for this version (a `memver_...` value). */
  id: string;
  /** When this version was written, in RFC 3339 format. */
  created_at: string; // format: date-time
  /** The ID of the memory that this version belongs to (`mem_...`). The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=typescript) to get the memory's retained versions, including its `deleted` version while the lineage is retained. */
  memory_id: string;
  /** ID of the memory store this version belongs to (a `memstore_...` value). */
  memory_store_id: string;
  /** The kind of mutation this version records: `created`, `modified`, or `deleted`. */
  operation: BetaManagedAgentsMemoryVersionOperation;
  /** The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set. */
  content?: string | null;
  /** Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise. */
  content_sha256?: string | null;
  /** Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise. */
  content_size_bytes?: number | null; // format: int32
  /** Who made this change to the memory, or `null` if the author wasn't recorded. Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it. You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=typescript) to learn more about where the change came from. */
  created_by?: BetaManagedAgentsActor;
  /** The memory's path at the time of this write. `null` if and only if `redacted_at` is set. */
  path?: string | null;
  /** When the version was redacted, in RFC 3339, or `null` if it hasn't been. When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`. See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=typescript#redact-a-version) to learn more about redaction. */
  redacted_at?: string | null; // format: date-time
  /** Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability). */
  redacted_by?: BetaManagedAgentsActor;
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

type BetaManagedAgentsMemoryVersionOperation =
  /** The memory was created. The first version in any memory's lineage. */
  | "created"
  /** The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`. */
  | "modified"
  /** The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash. */
  | "deleted";

type BetaManagedAgentsActor = BetaManagedAgentsSessionActor | BetaManagedAgentsAPIActor | BetaManagedAgentsUserActor | BetaManagedAgentsServiceAccountActor;

/** An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session. */
interface BetaManagedAgentsSessionActor {
  type: "session_actor";
  /** ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=typescript) for further provenance. */
  session_id: string; // minLength: 1
}

/** A direct caller of the public API, identified by the API key that authenticated the request. */
interface BetaManagedAgentsAPIActor {
  type: "api_actor";
  /** ID of the API key (an `apikey_...` value). This identifies the key, not the secret. */
  api_key_id: string; // minLength: 1
}

/** A human user, for example acting through the Anthropic Console. */
interface BetaManagedAgentsUserActor {
  type: "user_actor";
  /** ID of the user (a `user_...` value). */
  user_id: string; // minLength: 1
}

/** A workload authenticated as a service account, for example via Workload Identity Federation. */
interface BetaManagedAgentsServiceAccountActor {
  type: "service_account_actor";
  /** ID of the service account (a `svac_...` value). */
  service_account_id: string; // minLength: 1
}
```
