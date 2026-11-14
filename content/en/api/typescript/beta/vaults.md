---
title: Vaults
url: https://platform.claude.com/docs/en/api/typescript/beta/vaults
---

# Vaults

## Create a Vault

- Signature: `client.beta.vaults.create(params: VaultCreateParams, options?: RequestOptions): BetaManagedAgentsVault`
- Endpoint: `POST /v1/vaults`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.create({
  display_name: "Example vault"
});

console.log(betaManagedAgentsVault.id);
```

### Example response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

interface VaultCreateParams {
  /** Human-readable name for the vault. 1-255 characters. */
  display_name: string; // minLength: 1, maxLength: 255
  /** Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars. */
  metadata?: Record<string, string>;
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** A vault that stores credentials for use by agents during sessions. */
interface BetaManagedAgentsVault {
  type: "vault";
  /** The unique ID of the vault (`vlt_...`). */
  id: string;
  /** When the vault was archived. Null if not archived. */
  archived_at: string | null; // format: date-time
  /** A timestamp in RFC 3339 format */
  created_at: string; // format: date-time
  /** Human-readable name for the vault. */
  display_name: string;
  /** Arbitrary key-value metadata attached to the vault. */
  metadata: Record<string, string>;
  /** A timestamp in RFC 3339 format */
  updated_at: string; // format: date-time
}
```

### Types

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
```

## List Vaults

- Signature: `client.beta.vaults.list(params?: VaultListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsVault>`
- Endpoint: `GET /v1/vaults`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsVault of client.beta.vaults.list()) {
  console.log(betaManagedAgentsVault.id);
}
```

### Example response (200)

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Parameters

```ts
interface VaultListParams {
  /** Whether to include archived vaults in the results. Defaults to `false`. */
  include_archived?: boolean; // query parameter
  /** Maximum number of vaults to return per page. Defaults to 20, maximum 100. */
  limit?: number; // query parameter, format: int32
  /** The `next_page` value from a previous [List Vaults](https://platform.claude.com/docs/en/api/beta/vaults/list?sdk_languages=typescript) response, to get the next page. Leave it out to get the first page. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Retrieve a Vault

- Signature: `client.beta.vaults.retrieve(vaultID: string, params?: VaultRetrieveParams, options?: RequestOptions): BetaManagedAgentsVault`
- Endpoint: `GET /v1/vaults/{vault_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.retrieve(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
);

console.log(betaManagedAgentsVault.id);
```

### Example response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### Parameters

```ts
/** Unique identifier of the vault to retrieve. */
vaultID: string; // path parameter

interface VaultRetrieveParams {
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Update a Vault

- Signature: `client.beta.vaults.update(vaultID: string, params: VaultUpdateParams, options?: RequestOptions): BetaManagedAgentsVault`
- Endpoint: `POST /v1/vaults/{vault_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.update(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  {}
);

console.log(betaManagedAgentsVault.id);
```

### Example response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### Parameters

```ts
/** Unique identifier of the vault to update. */
vaultID: string; // path parameter

interface VaultUpdateParams {
  /** Updated human-readable name for the vault. 1-255 characters. */
  display_name?: string | null; // minLength: 1, maxLength: 255
  /** Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved. */
  metadata?: Record<string, string | null> | null;
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Delete a Vault

- Signature: `client.beta.vaults.delete(vaultID: string, params?: VaultDeleteParams, options?: RequestOptions): BetaManagedAgentsDeletedVault`
- Endpoint: `DELETE /v1/vaults/{vault_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedVault = await client.beta.vaults.delete(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
);

console.log(betaManagedAgentsDeletedVault.id);
```

### Example response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

### Parameters

```ts
/** Unique identifier of the vault to delete. */
vaultID: string; // path parameter

interface VaultDeleteParams {
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** Confirmation of a deleted vault. */
interface BetaManagedAgentsDeletedVault {
  type: "vault_deleted";
  /** The unique ID of the deleted vault (`vlt_...`). */
  id: string;
}
```

## Archive a Vault

- Signature: `client.beta.vaults.archive(vaultID: string, params?: VaultArchiveParams, options?: RequestOptions): BetaManagedAgentsVault`
- Endpoint: `POST /v1/vaults/{vault_id}/archive`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.archive(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
);

console.log(betaManagedAgentsVault.id);
```

### Example response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### Parameters

```ts
/** Unique identifier of the vault to archive. */
vaultID: string; // path parameter

interface VaultArchiveParams {
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Vaults › Credentials

### Create a Credential

- Signature: `client.beta.vaults.credentials.create(vaultID: string, params: CredentialCreateParams, options?: RequestOptions): BetaManagedAgentsCredential`
- Endpoint: `POST /v1/vaults/{vault_id}/credentials`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.create(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  {
    auth: {
      token: "bearer_exampletoken",
      mcp_server_url: "https://example-server.modelcontextprotocol.io/sse",
      type: "static_bearer"
    }
  }
);

console.log(betaManagedAgentsCredential.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** Identifier of the vault to create the credential in. */
vaultID: string; // path parameter

interface CredentialCreateParams {
  /** Authentication configuration for the credential. */
  auth: BetaManagedAgentsMCPOAuthCreateParams | BetaManagedAgentsStaticBearerCreateParams | BetaManagedAgentsEnvironmentVariableCreateParams;
  /** Human-readable name for the credential. Up to 255 characters. */
  display_name?: string | null; // maxLength: 255
  /** Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars. */
  metadata?: Record<string, string>;
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

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

#### Types

```ts
/** Parameters for creating an MCP OAuth credential. */
interface BetaManagedAgentsMCPOAuthCreateParams {
  type: "mcp_oauth";
  /** The OAuth access token to send to the MCP server. */
  access_token: string; // minLength: 1, maxLength: 8192, pattern: ^[^\x00-\x1f\x7f]*$
  /** URL of the MCP server this credential authenticates against. */
  mcp_server_url: string; // minLength: 1, maxLength: 2047
  /** When `access_token` expires, in RFC 3339. Must be in the future. */
  expires_at?: string | null; // format: date-time
  /** Refresh token configuration, if the credential supports token refresh. */
  refresh?: BetaManagedAgentsMCPOAuthRefreshParams | null;
}

/** Parameters for creating a static bearer token credential. */
interface BetaManagedAgentsStaticBearerCreateParams {
  type: "static_bearer";
  /** The static bearer token to send to the MCP server, such as an API key or personal access token. */
  token: string; // minLength: 1, maxLength: 8192, pattern: ^[^\x00-\x1f\x7f]*$
  /** URL of the MCP server this credential authenticates against. */
  mcp_server_url: string; // minLength: 1, maxLength: 2047
}

/** Parameters for creating an environment variable credential. */
interface BetaManagedAgentsEnvironmentVariableCreateParams {
  type: "environment_variable";
  /** Outbound hosts the secret value is substituted on. */
  networking: BetaManagedAgentsCredentialNetworkingParams;
  /** Name of the environment variable. Immutable after create. */
  secret_name: string; // minLength: 1, maxLength: 255, pattern: ^[A-Z_][A-Z0-9_]*$
  /** The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses. */
  secret_value: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f]*$
  /** Where in the outbound request the secret value may be substituted. */
  injection_location?: BetaManagedAgentsInjectionLocationParams;
}

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

type BetaManagedAgentsCredentialNetworkingParams = BetaManagedAgentsUnrestrictedCredentialNetworkingParams | BetaManagedAgentsLimitedCredentialNetworkingParams;

interface BetaManagedAgentsInjectionLocationParams {
  /** Substitute when the placeholder appears in the request body. */
  body?: boolean;
  /** Substitute when the placeholder appears in a request header value. */
  header?: boolean;
}

/** Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach. */
interface BetaManagedAgentsUnrestrictedCredentialNetworkingParams {
  type: "unrestricted";
}

/** Substitute the secret only on requests to the listed hosts. */
interface BetaManagedAgentsLimitedCredentialNetworkingParams {
  type: "limited";
  /** The destination hosts of the outbound requests that the credential's secret is substituted into. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries. */
  allowed_hosts: Array<string>;
}

interface BetaManagedAgentsMCPOAuthRefreshParams {
  /** The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created. */
  client_id: string; // minLength: 1, maxLength: 1024
  /** The OAuth refresh token that the API uses to get a new access token when the current one expires. */
  refresh_token: string; // minLength: 1, maxLength: 8192
  /** Token endpoint URL used to refresh the access token. */
  token_endpoint: string; // minLength: 1, maxLength: 2047
  token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam;
  /** OAuth resource indicator. */
  resource?: string | null; // minLength: 1, maxLength: 2047
  /** OAuth scope for the refresh request. */
  scope?: string | null; // minLength: 1, maxLength: 8192
}

/** Token endpoint requires no client authentication. */
interface BetaManagedAgentsTokenEndpointAuthNoneParam {
  type: "none";
}

/** Token endpoint uses HTTP Basic authentication with client credentials. */
interface BetaManagedAgentsTokenEndpointAuthBasicParam {
  type: "client_secret_basic";
  /** The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication. */
  client_secret: string; // minLength: 1, maxLength: 512
}

/** Token endpoint uses POST body authentication with client credentials. */
interface BetaManagedAgentsTokenEndpointAuthPostParam {
  type: "client_secret_post";
  /** The OAuth client secret, sent to `token_endpoint` in the POST body. */
  client_secret: string; // minLength: 1, maxLength: 512
}
```

### List Credentials

- Signature: `client.beta.vaults.credentials.list(vaultID: string, params?: CredentialListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsCredential>`
- Endpoint: `GET /v1/vaults/{vault_id}/credentials`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsCredential of client.beta.vaults.credentials.list(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)) {
  console.log(betaManagedAgentsCredential.id);
}
```

#### Example response (200)

```json
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

#### Parameters

```ts
/** Identifier of the vault to list credentials for. */
vaultID: string; // path parameter

interface CredentialListParams {
  /** Whether to include archived credentials in the results. Defaults to `false`. */
  include_archived?: boolean; // query parameter
  /** Maximum number of credentials to return per page. Defaults to 20, maximum 100. */
  limit?: number; // query parameter, format: int32
  /** The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=typescript) response, to get the next page. Leave it out to get the first page. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Retrieve a Credential

- Signature: `client.beta.vaults.credentials.retrieve(credentialID: string, params: CredentialRetrieveParams, options?: RequestOptions): BetaManagedAgentsCredential`
- Endpoint: `GET /v1/vaults/{vault_id}/credentials/{credential_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

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

#### Example response (200)

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

#### Parameters

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

### Update a Credential

- Signature: `client.beta.vaults.credentials.update(credentialID: string, params: CredentialUpdateParams, options?: RequestOptions): BetaManagedAgentsCredential`
- Endpoint: `POST /v1/vaults/{vault_id}/credentials/{credential_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsCredential.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** Unique identifier of the credential to update. */
credentialID: string; // path parameter

interface CredentialUpdateParams {
  /** Identifier of the vault containing the credential. */
  vault_id: string; // path parameter
  /** New authentication settings for the credential. The `type` must match the credential's current type, which can't be changed. */
  auth?: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams | BetaManagedAgentsEnvironmentVariableUpdateParams;
  /** Updated human-readable name for the credential. 1-255 characters. */
  display_name?: string | null; // minLength: 1, maxLength: 255
  /** Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved. */
  metadata?: Record<string, string | null> | null;
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Types

```ts
/** Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable. */
interface BetaManagedAgentsMCPOAuthUpdateParams {
  type: "mcp_oauth";
  /** The new OAuth access token to replace the stored one. */
  access_token?: string | null; // minLength: 1, maxLength: 8192, pattern: ^[^\x00-\x1f\x7f]*$
  /** When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry. If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry. Must be in the future. */
  expires_at?: string | null; // format: date-time
  /** Updated refresh token configuration. */
  refresh?: BetaManagedAgentsMCPOAuthRefreshUpdateParams | null;
}

/** Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable. */
interface BetaManagedAgentsStaticBearerUpdateParams {
  type: "static_bearer";
  /** The new static bearer token to replace the stored one. */
  token?: string | null; // minLength: 1, maxLength: 8192, pattern: ^[^\x00-\x1f\x7f]*$
}

/** Parameters for updating an environment variable credential. `secret_name` is immutable. */
interface BetaManagedAgentsEnvironmentVariableUpdateParams {
  type: "environment_variable";
  /** Updated injection location. */
  injection_location?: BetaManagedAgentsInjectionLocationUpdateParams;
  /** The new networking scope, which replaces the stored one as a whole. */
  networking?: BetaManagedAgentsCredentialNetworkingParams | null;
  /** The new secret value to replace the stored one. */
  secret_value?: string | null; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f]*$
}

interface BetaManagedAgentsInjectionLocationUpdateParams {
  /** Substitute when the placeholder appears in the request body. */
  body?: boolean;
  /** Substitute when the placeholder appears in a request header value. */
  header?: boolean;
}

interface BetaManagedAgentsMCPOAuthRefreshUpdateParams {
  /** The new OAuth refresh token to replace the stored one. */
  refresh_token?: string | null; // minLength: 1, maxLength: 8192
  /** The new OAuth scope for refresh requests. Send an empty string to clear the stored scope. */
  scope?: string | null; // maxLength: 8192
  token_endpoint_auth?: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam;
}

/** Updated HTTP Basic authentication parameters for the token endpoint. */
interface BetaManagedAgentsTokenEndpointAuthBasicUpdateParam {
  type: "client_secret_basic";
  /** A new OAuth client secret to replace the stored one. The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one. */
  client_secret?: string | null; // minLength: 1, maxLength: 512
}

/** Updated POST body authentication parameters for the token endpoint. */
interface BetaManagedAgentsTokenEndpointAuthPostUpdateParam {
  type: "client_secret_post";
  /** A new OAuth client secret to replace the stored one. The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one. */
  client_secret?: string | null; // minLength: 1, maxLength: 512
}
```

### Delete a Credential

- Signature: `client.beta.vaults.credentials.delete(credentialID: string, params: CredentialDeleteParams, options?: RequestOptions): BetaManagedAgentsDeletedCredential`
- Endpoint: `DELETE /v1/vaults/{vault_id}/credentials/{credential_id}`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedCredential = await client.beta.vaults.credentials.delete(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsDeletedCredential.id);
```

#### Example response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```

#### Parameters

```ts
/** Unique identifier of the credential to delete. */
credentialID: string; // path parameter

interface CredentialDeleteParams {
  /** Identifier of the vault containing the credential. */
  vault_id: string; // path parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** Confirmation of a deleted credential. */
interface BetaManagedAgentsDeletedCredential {
  type: "vault_credential_deleted";
  /** The unique ID of the deleted credential (`vcrd_...`). */
  id: string;
}
```

### Archive a Credential

- Signature: `client.beta.vaults.credentials.archive(credentialID: string, params: CredentialArchiveParams, options?: RequestOptions): BetaManagedAgentsCredential`
- Endpoint: `POST /v1/vaults/{vault_id}/credentials/{credential_id}/archive`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.archive(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsCredential.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** Unique identifier of the credential to archive. */
credentialID: string; // path parameter

interface CredentialArchiveParams {
  /** Identifier of the vault containing the credential. */
  vault_id: string; // path parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Validate an MCP OAuth Credential

- Signature: `client.beta.vaults.credentials.mcpOAuthValidate(credentialID: string, params: CredentialMCPOAuthValidateParams, options?: RequestOptions): BetaManagedAgentsCredentialValidation`
- Endpoint: `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

#### Example request

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

#### Example response (200)

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

#### Parameters

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

#### Returns

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

#### Types

```ts
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
