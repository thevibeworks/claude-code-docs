---
title: Tunnels
url: https://platform.claude.com/docs/en/api/typescript/beta/tunnels
---

# Tunnels

## Create Tunnel

- Signature: `client.beta.tunnels.create(params: TunnelCreateParams, options?: RequestOptions): BetaTunnel`
- Endpoint: `POST /v1/tunnels`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.create({});

console.log(betaTunnel.id);
```

### Example response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

### Parameters

```ts
// This page declares each type one time, in the first method that uses it.

interface TunnelCreateParams {
  /** Optional human-readable name for the tunnel (1-255 characters). */
  display_name?: string | null; // minLength: 1, maxLength: 255
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** An MCP tunnel. */
interface BetaTunnel {
  type: "tunnel";
  /** Unique identifier for the tunnel, prefixed with `tnl_`. */
  id: string;
  /** RFC 3339 datetime string indicating when the tunnel was archived. Null if it is not archived. */
  archived_at: string | null; // format: date-time
  /** RFC 3339 datetime string indicating when the tunnel was created. */
  created_at: string; // format: date-time
  /** Human-readable name for the tunnel (1-255 characters). Null if unset. */
  display_name: string | null;
  /** Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived. */
  domain: string;
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

## Get Tunnel

- Signature: `client.beta.tunnels.retrieve(tunnelID: string, params?: TunnelRetrieveParams, options?: RequestOptions): BetaTunnel`
- Endpoint: `GET /v1/tunnels/{tunnel_id}`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.retrieve("tunnel_id");

console.log(betaTunnel.id);
```

### Example response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

### Parameters

```ts
/** ID of the tunnel (`tnl_...`). */
tunnelID: string; // path parameter

interface TunnelRetrieveParams {
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## List Tunnels

- Signature: `client.beta.tunnels.list(params?: TunnelListParams, options?: RequestOptions): PageCursor<BetaTunnel>`
- Endpoint: `GET /v1/tunnels`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaTunnel of client.beta.tunnels.list()) {
  console.log(betaTunnel.id);
}
```

### Example response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

### Parameters

```ts
interface TunnelListParams {
  /** Whether to include archived tunnels in the results. Defaults to false. */
  include_archived?: boolean; // query parameter
  /** Maximum number of tunnels to return per page. Defaults to 20, maximum 1000. */
  limit?: number; // query parameter, format: int32
  /** Opaque pagination cursor from a previous `list_tunnels` response. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Archive Tunnel

- Signature: `client.beta.tunnels.archive(tunnelID: string, params?: TunnelArchiveParams, options?: RequestOptions): BetaTunnel`
- Endpoint: `POST /v1/tunnels/{tunnel_id}/archive`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.archive("tunnel_id");

console.log(betaTunnel.id);
```

### Example response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

### Parameters

```ts
/** ID of the tunnel (`tnl_...`). */
tunnelID: string; // path parameter

interface TunnelArchiveParams {
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Reveal Tunnel Token

- Signature: `client.beta.tunnels.revealToken(tunnelID: string, params?: TunnelRevealTokenParams, options?: RequestOptions): BetaTunnelToken`
- Endpoint: `POST /v1/tunnels/{tunnel_id}/reveal_token`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelToken = await client.beta.tunnels.revealToken("tunnel_id");

console.log(betaTunnelToken.id);
```

### Example response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

### Parameters

```ts
/** ID of the tunnel (`tnl_...`). */
tunnelID: string; // path parameter

interface TunnelRevealTokenParams {
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Returns

```ts
/** A tunnel's connector token. */
interface BetaTunnelToken {
  type: "tunnel_token";
  /** Stable identifier for the current token value. Changes when the token is rotated. */
  id: string;
  /** The connector token used to run the tunnel. Treat as a credential. */
  tunnel_token: string;
}
```

## Rotate Tunnel Token

- Signature: `client.beta.tunnels.rotateToken(tunnelID: string, params: TunnelRotateTokenParams, options?: RequestOptions): BetaTunnelToken`
- Endpoint: `POST /v1/tunnels/{tunnel_id}/rotate_token`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelToken = await client.beta.tunnels.rotateToken("tunnel_id", {});

console.log(betaTunnelToken.id);
```

### Example response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

### Parameters

```ts
/** ID of the tunnel (`tnl_...`). */
tunnelID: string; // path parameter

interface TunnelRotateTokenParams {
  /** Optional free-text reason for the rotation, recorded for audit. */
  reason?: string | null; // maxLength: 1024
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Tunnels › Certificates

### Create Tunnel Certificate

- Signature: `client.beta.tunnels.certificates.create(tunnelID: string, params: CertificateCreateParams, options?: RequestOptions): BetaTunnelCertificate`
- Endpoint: `POST /v1/tunnels/{tunnel_id}/certificates`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.create("tunnel_id", {
  ca_certificate_pem: "ca_certificate_pem"
});

console.log(betaTunnelCertificate.id);
```

#### Example response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

#### Parameters

```ts
/** ID of the tunnel (`tnl_...`). */
tunnelID: string; // path parameter

interface CertificateCreateParams {
  /** PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB. */
  ca_certificate_pem: string; // maxLength: 8192
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** A CA certificate attached to a tunnel. */
interface BetaTunnelCertificate {
  type: "tunnel_certificate";
  /** Unique identifier for the certificate, prefixed with `tcrt_`. */
  id: string;
  /** RFC 3339 datetime string indicating when the certificate was archived. Null if it is still in the trusted set. */
  archived_at: string | null; // format: date-time
  /** RFC 3339 datetime string indicating when the certificate was registered. */
  created_at: string; // format: date-time
  /** RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire. */
  expires_at: string | null; // format: date-time
  /** Lowercase hex SHA-256 fingerprint of the certificate's DER encoding. */
  fingerprint: string;
  /** ID of the tunnel the certificate is registered against. */
  tunnel_id: string;
}
```

### Get Tunnel Certificate

- Signature: `client.beta.tunnels.certificates.retrieve(certificateID: string, params: CertificateRetrieveParams, options?: RequestOptions): BetaTunnelCertificate`
- Endpoint: `GET /v1/tunnels/{tunnel_id}/certificates/{certificate_id}`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.retrieve(
  "certificate_id",
  { tunnel_id: "tunnel_id" }
);

console.log(betaTunnelCertificate.id);
```

#### Example response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

#### Parameters

```ts
/** ID of the certificate (`tcrt_...`). */
certificateID: string; // path parameter

interface CertificateRetrieveParams {
  /** ID of the tunnel (`tnl_...`). */
  tunnel_id: string; // path parameter
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### List Tunnel Certificates

- Signature: `client.beta.tunnels.certificates.list(tunnelID: string, params?: CertificateListParams, options?: RequestOptions): PageCursor<BetaTunnelCertificate>`
- Endpoint: `GET /v1/tunnels/{tunnel_id}/certificates`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaTunnelCertificate of client.beta.tunnels.certificates.list("tunnel_id")) {
  console.log(betaTunnelCertificate.id);
}
```

#### Example response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

#### Parameters

```ts
/** ID of the tunnel (`tnl_...`). */
tunnelID: string; // path parameter

interface CertificateListParams {
  /** Whether to include archived certificates in the results. Defaults to false. */
  include_archived?: boolean; // query parameter
  /** Maximum number of certificates to return per page. Defaults to 20, maximum 1000. */
  limit?: number; // query parameter, format: int32
  /** Opaque pagination cursor from a previous `list_tunnel_certificates` response. */
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

### Archive Tunnel Certificate

- Signature: `client.beta.tunnels.certificates.archive(certificateID: string, params: CertificateArchiveParams, options?: RequestOptions): BetaTunnelCertificate`
- Endpoint: `POST /v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`
- Beta header: `anthropic-beta: mcp-tunnels-2026-06-22`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.archive(
  "certificate_id",
  { tunnel_id: "tunnel_id" }
);

console.log(betaTunnelCertificate.id);
```

#### Example response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

#### Parameters

```ts
/** ID of the certificate to archive (`tcrt_...`). */
certificateID: string; // path parameter

interface CertificateArchiveParams {
  /** ID of the tunnel (`tnl_...`). */
  tunnel_id: string; // path parameter
  /** This endpoint is in beta: requests must send `mcp-tunnels-2026-06-22` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```
