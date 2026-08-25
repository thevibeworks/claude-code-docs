---
title: Rotate Tunnel Token
url: https://platform.claude.com/docs/en/api/php/beta/tunnels/rotate_token
---

## Rotate Tunnel Token

`$client->beta->tunnels->rotateToken(string tunnelID, ?string reason, ?list<AnthropicBeta> betas): BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnelID: string`

- `reason?:optional string`

  Optional free-text reason for the rotation, recorded for audit.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnelToken`

  - `string id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `string tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `"tunnel_token" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelToken = $client->beta->tunnels->rotateToken(
  'tunnel_id',
  reason: 'reason',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaTunnelToken);
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```
