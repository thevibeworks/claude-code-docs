---
title: Reveal Tunnel Token
url: https://platform.claude.com/docs/en/api/php/beta/tunnels/reveal_token
---

## Reveal Tunnel Token

`$client->beta->tunnels->revealToken(string tunnelID, ?list<AnthropicBeta> betas): BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnelID: string`

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

$betaTunnelToken = $client->beta->tunnels->revealToken(
  'tunnel_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
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
