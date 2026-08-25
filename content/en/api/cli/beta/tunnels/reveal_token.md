# Reveal Tunnel Token

`$ ant beta:tunnels reveal-token`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

## Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_tunnel_token: object`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

## Example

```bash
ant beta:tunnels reveal-token \
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
