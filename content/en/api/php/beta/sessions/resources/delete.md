# Delete Session Resource

`$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas): ManagedAgentsDeleteSessionResource`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

## Parameters

- `sessionID: string`

- `resourceID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `ManagedAgentsDeleteSessionResource`

  - `string id`

  - `Type type`

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeleteSessionResource = $client
  ->beta
  ->sessions
  ->resources
  ->delete(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsDeleteSessionResource);
```

### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```
