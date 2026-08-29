# Delete Skill Version

`$client->beta->skills->versions->delete(string version, string skillID, ?list<AnthropicBeta> betas): DeletedSkillVersion`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

## Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `DeletedSkillVersion`

  - `string id`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `"skill_version_deleted" type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedSkillVersion = $client->beta->skills->versions->delete(
  'version',
  skillID: 'skill_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaDeletedSkillVersion);
```

### Response (200)

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```
