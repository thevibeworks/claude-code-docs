---
title: Archive Tunnel
url: https://platform.claude.com/docs/en/api/php/beta/tunnels/archive
---

## Archive Tunnel

`$client->beta->tunnels->archive(string tunnelID, ?list<AnthropicBeta> betas): BetaTunnel`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnelID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnel`

  - `string id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `string domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `"tunnel" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnel = $client->beta->tunnels->archive(
  'tunnel_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaTunnel);
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
