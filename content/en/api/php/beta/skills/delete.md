# Delete Skill

`$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas): BetaDeletedSkill`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

## Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaDeletedSkill`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `"skill_deleted" type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedSkill = $client->beta->skills->delete(
  'skill_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaDeletedSkill);
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```
