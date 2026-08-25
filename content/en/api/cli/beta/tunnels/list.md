---
title: List Tunnels
url: https://platform.claude.com/docs/en/api/cli/beta/tunnels/list
---

## List Tunnels

`$ ant beta:tunnels list`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `--include-archived: optional boolean`

  Query param: Whether to include archived tunnels in the results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous `list_tunnels` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListTunnelsResponse: object { data, next_page }`

  A paginated list of tunnels.

  - `data: array of BetaTunnel`

    List of tunnels, ordered by created_at descending.

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

  - `next_page: string`

    Pagination cursor for the next page, or null if no more results.

### Example

```cli
ant beta:tunnels list \
  --api-key my-anthropic-api-key
```

#### Response

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
