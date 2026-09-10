---
title: Rotate Tunnel Token
url: https://platform.claude.com/docs/en/api/cli/beta/tunnels/rotate_token
---

# Rotate Tunnel Token

`$ ant beta:tunnels rotate-token`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

## Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--reason: optional string`

  Body param: Optional free-text reason for the rotation, recorded for audit.

  maxLength: 1024

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_tunnel_token: object`

  A tunnel's connector token.

  - `type: "tunnel_token"`

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

## Example

```bash
ant beta:tunnels rotate-token \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
```

### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```
