---
title: Get Tunnel
url: https://platform.claude.com/docs/en/api/php/beta/tunnels/retrieve
---

## Get Tunnel

`$client->beta->tunnels->retrieve(string tunnelID, ?list<AnthropicBeta> betas): BetaTunnel`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

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

$betaTunnel = $client->beta->tunnels->retrieve(
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
