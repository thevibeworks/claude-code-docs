# Create Skill

`$client->beta->skills->create(list<string> files, ?string displayName, ?list<AnthropicBeta> betas): BetaSkill`

**POST** `/v1/skills`

Create Skill

## Parameters

- `files: list<string>`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `displayName?:optional string`

  Human-readable, single-line label for the Skill. Maximum 255 characters.
  Always set: derived from the SKILL.md frontmatter `name` when omitted at
  creation. Not unique.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaSkill`

  - `string id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `\Datetime createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `string displayName`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `string latestVersionID`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `BetaSkillSource source`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

  - `"skill" type`

    Object type.

    For Skills, this is always `"skill"`.

  - `\Datetime updatedAt`

    ISO 8601 timestamp of when the skill was last updated.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaSkill = $client->beta->skills->create(
  files: [
    FileParam::fromString('Example data', filename: uniqid('file-upload-', true)),
  ],
  displayName: 'display_name',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaSkill);
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
