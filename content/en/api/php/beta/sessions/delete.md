---
title: Delete Session
url: https://platform.claude.com/docs/en/api/php/beta/sessions/delete
---

# Delete Session

`$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeletedSession`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

## Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsDeletedSession`

  - `Type type`

  - `string id`

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedSession = $client->beta->sessions->delete(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedSession);
```

### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```
