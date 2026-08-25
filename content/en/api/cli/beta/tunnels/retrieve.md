---
title: Get Tunnel
url: https://platform.claude.com/docs/en/api/cli/beta/tunnels/retrieve
---

## Get Tunnel

`$ ant beta:tunnels retrieve`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel: object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

### Example

```cli
ant beta:tunnels retrieve \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
```

#### Response

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
