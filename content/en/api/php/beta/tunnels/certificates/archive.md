---
title: Archive Tunnel Certificate
url: https://platform.claude.com/docs/en/api/php/beta/tunnels/certificates/archive
---

## Archive Tunnel Certificate

`$client->beta->tunnels->certificates->archive(string certificateID, string tunnelID, ?list<AnthropicBeta> betas): TunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `tunnelID: string`

- `certificateID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `TunnelCertificate`

  - `string id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `string tunnelID`

    ID of the tunnel the certificate is registered against.

  - `"tunnel_certificate" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelCertificate = $client->beta->tunnels->certificates->archive(
  'certificate_id',
  tunnelID: 'tunnel_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaTunnelCertificate);
```

#### Response

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
