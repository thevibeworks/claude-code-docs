---
title: Retrieve a Credential
url: https://platform.claude.com/docs/en/api/typescript/beta/vaults/credentials/retrieve
---

# Retrieve a Credential

- Signature: `client.beta.vaults.credentials.retrieve(credentialID: string, params: CredentialRetrieveParams, options?: RequestOptions): BetaManagedAgentsCredential`
- Endpoint: `GET /v1/vaults/{vault_id}/credentials/{credential_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.retrieve(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsCredential.id);
```

## Example response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

## Parameters

```ts
/** Unique identifier of the credential to retrieve. */
credentialID: string; // path parameter

interface CredentialRetrieveParams {
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
/** A credential stored in a vault. Sensitive fields are never returned in responses. */
interface BetaManagedAgentsCredential {
  type: "vault_credential";
  /** The unique ID of the credential (`vcrd_...`). */
  id: string;
  /** When the credential was archived. Null if not archived. */
  archived_at: string | null; // format: date-time
  /** Authentication configuration for this credential. */
  auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse;
  /** A timestamp in RFC 3339 format */
  created_at: string; // format: date-time
  /** Arbitrary key-value metadata attached to the credential. */
  metadata: Record<string, string>;
  /** A timestamp in RFC 3339 format */
  updated_at: string; // format: date-time
  /** Identifier of the vault this credential belongs to. */
  vault_id: string;
  /** Human-readable name for the credential. */
  display_name?: string | null;
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

/** OAuth credential details for an MCP server. */
interface BetaManagedAgentsMCPOAuthAuthResponse {
  type: "mcp_oauth";
  /** URL of the MCP server this credential authenticates against. */
  mcp_server_url: string;
  /** When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known. */
  expires_at?: string | null; // format: date-time
  /** Refresh token configuration, if the credential supports token refresh. */
  refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null;
}

/** Static bearer token credential details for an MCP server. */
interface BetaManagedAgentsStaticBearerAuthResponse {
  type: "static_bearer";
  /** URL of the MCP server this credential authenticates against. */
  mcp_server_url: string;
}

/** Environment variable credential details. The secret value is never returned. */
interface BetaManagedAgentsEnvironmentVariableAuthResponse {
  type: "environment_variable";
  /** Where in the outbound request the secret value is substituted. */
  injection_location: BetaManagedAgentsInjectionLocationResponse;
  /** Outbound hosts the secret value is substituted on. */
  networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse;
  /** Name of the environment variable. */
  secret_name: string;
}

interface BetaManagedAgentsInjectionLocationResponse {
  /** Whether the placeholder is substituted in the request body. */
  body: boolean;
  /** Whether the placeholder is substituted in request header values. */
  header: boolean;
}

/** The secret is substituted on any host the session's Environment network policy permits egress to. */
interface BetaManagedAgentsUnrestrictedCredentialNetworkingResponse {
  type: "unrestricted";
}

/** The secret is substituted only on requests to the listed hosts. */
interface BetaManagedAgentsLimitedCredentialNetworkingResponse {
  type: "limited";
  /** The destination hosts of the outbound requests that the credential's secret is substituted into. An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself. */
  allowed_hosts: Array<string>;
}

interface BetaManagedAgentsMCPOAuthRefreshResponse {
  /** The OAuth client ID used when refreshing the access token. */
  client_id: string;
  /** Token endpoint URL used to refresh the access token. */
  token_endpoint: string;
  token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse;
  /** OAuth resource indicator. */
  resource?: string | null;
  /** OAuth scope for the refresh request. */
  scope?: string | null;
}

/** Token endpoint requires no client authentication. */
interface BetaManagedAgentsTokenEndpointAuthNoneResponse {
  type: "none";
}

/** Token endpoint uses HTTP Basic authentication with client credentials. */
interface BetaManagedAgentsTokenEndpointAuthBasicResponse {
  type: "client_secret_basic";
}

/** Token endpoint uses POST body authentication with client credentials. */
interface BetaManagedAgentsTokenEndpointAuthPostResponse {
  type: "client_secret_post";
}
```
