---
title: List Files
url: https://platform.claude.com/docs/en/api/typescript/beta/files/list
---

# List Files

- Signature: `client.beta.files.list(params?: FileListParams, options?: RequestOptions): PageCursor<BetaFileMetadata>`
- Endpoint: `GET /v1/files`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaFileMetadata of client.beta.files.list()) {
  console.log(betaFileMetadata.id);
}
```

## Example response (200)

```json
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "expires_at": "2025-05-15T18:37:24.100435Z",
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Parameters

```ts
interface FileListParams {
  /** Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted. */
  ids?: Array<string> | null; // query parameter
  /** Number of items to return per page. Defaults to `20`. Ranges from `1` to `1000`. */
  limit?: number; // query parameter, minimum: 1, maximum: 1000
  /** Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`. */
  page?: string | null; // query parameter
  /** Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID). */
  scope_id?: string; // query parameter
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
interface BetaFileMetadata {
  /** Object type. For files, this is always `"file"`. */
  type: "file";
  /** Unique object identifier. The format and length of IDs may change over time. */
  id: string;
  /** RFC 3339 datetime string representing when the file was created. */
  created_at: string; // format: date-time
  /** Original filename of the uploaded file. */
  filename: string; // minLength: 1, maxLength: 500
  /** MIME type of the file. */
  mime_type: string; // minLength: 1, maxLength: 255
  /** Size of the file in bytes. */
  size_bytes: number; // minimum: 0
  /** Whether the file can be downloaded. */
  downloadable?: boolean; // default: false
  /** RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value. */
  expires_at?: string | null; // format: date-time
  /** The scope of this file, indicating the context in which it was created (e.g., a session). */
  scope?: BetaFileScope | null;
}
```

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

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

interface BetaFileScope {
  /** The type of scope (e.g., `"session"`). */
  type: "session";
  /** The ID of the scoping resource (e.g., the session ID). */
  id: string;
}
```
