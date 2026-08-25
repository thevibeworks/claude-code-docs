---
title: Delete Session
url: https://platform.claude.com/docs/en/api/php/beta/sessions/delete
---

## Delete Session

`$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeletedSession`

**delete** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeletedSession`

  - `string id`

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedSession = $client->beta->sessions->delete(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsDeletedSession);
```

#### Response

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```
