---
title: List Session Resources
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/resources/list
---

# List Session Resources

- Signature: `client.beta.sessions.resources.list(sessionID: string, params?: ResourceListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsSessionResource>`
- Endpoint: `GET /v1/sessions/{session_id}/resources`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSessionResource of client.beta.sessions.resources.list(
  "sesn_011CZkZAtmR3yMPDzynEDxu7"
)) {
  console.log(betaManagedAgentsSessionResource);
}
```

## Example response (200)

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXym1gWMPdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Parameters

```ts
sessionID: string; // path parameter

interface ResourceListParams {
  /** Maximum number of resources to return per page (max 1000). If omitted, returns all resources. */
  limit?: number; // query parameter, format: int32
  /** Opaque cursor from a previous response's `next_page` field. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
type BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource;
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

interface BetaManagedAgentsGitHubRepositoryResource {
  type: "github_repository";
  id: string;
  /** A timestamp in RFC 3339 format */
  created_at: string; // format: date-time
  mount_path: string;
  /** A timestamp in RFC 3339 format */
  updated_at: string; // format: date-time
  url: string;
  checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null;
}

interface BetaManagedAgentsFileResource {
  type: "file";
  id: string;
  /** A timestamp in RFC 3339 format */
  created_at: string; // format: date-time
  file_id: string;
  mount_path: string;
  /** A timestamp in RFC 3339 format */
  updated_at: string; // format: date-time
}

/** A memory store attached to an agent session. */
interface BetaManagedAgentsMemoryStoreResource {
  type: "memory_store";
  /** The memory store ID (memstore_...). Must belong to the caller's organization and workspace. */
  memory_store_id: string; // pattern: ^memstore_[a-zA-Z0-9_]+$
  /** Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem. */
  access?: "read_write" | "read_only" | null;
  /** Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description. */
  description?: string;
  /** Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars. */
  instructions?: string | null; // maxLength: 4096
  /** Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only. */
  mount_path?: string | null;
  /** Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource. */
  name?: string | null;
}

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
```
