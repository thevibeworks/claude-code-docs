---
title: Delete Skill
url: https://platform.claude.com/docs/en/api/php/beta/skills/delete
---

# Delete Skill

`$client->beta->skills->delete(string skillID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaDeletedSkill`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

## Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaDeletedSkill`

  - `"skill_deleted" type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedSkill = $client->beta->skills->delete(
  'skill_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
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
