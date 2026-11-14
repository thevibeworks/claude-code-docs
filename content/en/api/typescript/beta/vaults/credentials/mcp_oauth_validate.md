---
title: Validate an MCP OAuth Credential
url: https://platform.claude.com/docs/en/api/typescript/beta/vaults/credentials/mcp_oauth_validate
---

# Validate an MCP OAuth Credential

- Signature: `client.beta.vaults.credentials.mcpOAuthValidate(credentialID: string, params: CredentialMCPOAuthValidateParams, options?: RequestOptions): BetaManagedAgentsCredentialValidation`
- Endpoint: `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredentialValidation =
  await client.beta.vaults.credentials.mcpOAuthValidate("vcrd_011CZkZEMt8gZan2iYPQfSkw", {
    vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  });

console.log(betaManagedAgentsCredentialValidation.credential_id);
```

## Example response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "has_refresh_token": true,
  "mcp_probe": null,
  "refresh": null,
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

## Parameters

```ts
/** Unique identifier of the credential to validate. */
credentialID: string; // path parameter

interface CredentialMCPOAuthValidateParams {
  /** Identifier of the vault containing the credential. */
  vault_id: string; // path parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** Result of live-probing a credential against its configured MCP server. */
interface BetaManagedAgentsCredentialValidation {
  type: "vault_credential_validation";
  /** Unique identifier of the credential that was validated. */
  credential_id: string;
  /** Whether the credential has a refresh token configured. */
  has_refresh_token: boolean;
  /** Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test. */
  mcp_probe: BetaManagedAgentsMCPProbe | null;
  /** Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted. */
  refresh: BetaManagedAgentsRefreshObject | null;
  /** Overall verdict of the validation probe. */
  status: BetaManagedAgentsCredentialValidationStatus;
  /** When the validation probe was performed. */
  validated_at: string; // format: date-time
  /** Identifier of the vault containing the credential. */
  vault_id: string;
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

interface BetaManagedAgentsMCPProbe {
  /** The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure. */
  http_response: BetaManagedAgentsRefreshHTTPResponse | null;
  /** The MCP method that failed (for example `initialize` or `tools/list`). */
  method: string;
}

interface BetaManagedAgentsRefreshObject {
  /** The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`. */
  http_response: BetaManagedAgentsRefreshHTTPResponse | null;
  /**
   * Outcome of the refresh attempt.
   * - `"succeeded"`: The token endpoint returned a new access token.
   * - `"failed"`: The token endpoint returned an error response. See `http_response` for detail.
   * - `"connect_error"`: The token endpoint could not be reached (DNS, TLS, or connection error).
   * - `"no_refresh_token"`: No refresh token is stored for the credential, so no exchange was attempted.
   */
  status: "succeeded" | "failed" | "connect_error" | "no_refresh_token";
}

type BetaManagedAgentsCredentialValidationStatus =
  /** The credential successfully authenticated against its MCP server. */
  | "valid"
  /** The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again. */
  | "invalid"
  /** The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out. */
  | "unknown";

interface BetaManagedAgentsRefreshHTTPResponse {
  /** Response body. May be truncated and has sensitive values scrubbed. */
  body: string;
  /** Whether `body` was truncated. */
  body_truncated: boolean;
  /** Value of the `Content-Type` response header. */
  content_type: string;
  /** HTTP status code. */
  status_code: number; // format: int32
}
```
