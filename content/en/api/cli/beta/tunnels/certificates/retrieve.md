---
title: Get Tunnel Certificate
url: https://platform.claude.com/docs/en/api/cli/beta/tunnels/certificates/retrieve
---

# Get Tunnel Certificate

`$ ant beta:tunnels:certificates retrieve`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

## Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--certificate-id: string`

  Path param: Path parameter certificate_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_tunnel_certificate: object`

  A CA certificate attached to a tunnel.

  - `type: "tunnel_certificate"`

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

## Example

```bash
ant beta:tunnels:certificates retrieve \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --certificate-id certificate_id
```

### Response (200)

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
