---
title: Delete Environment
url: https://platform.claude.com/docs/en/api/php/beta/environments/delete
---

# Delete Environment

`$client->beta->environments->delete(string environmentID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaEnvironmentDeleteResponse`

**DELETE** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

## Parameters

- `environmentID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

## Returns

- `BetaEnvironmentDeleteResponse`

  - `Type type`

    The type of response

  - `string id`

    Environment identifier

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaEnvironmentDeleteResponse = $client->beta->environments->delete(
  'env_011CZkZ9X2dpNyB7HsEFoRfW',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaEnvironmentDeleteResponse);
```

### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```
