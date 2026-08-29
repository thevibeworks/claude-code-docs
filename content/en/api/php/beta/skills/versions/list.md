# List Skill Versions

`$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<SkillVersion>`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

## Parameters

- `skillID: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit?:optional int`

  Number of results to return per page.

  Ranges from `1` to `1000`. Defaults to `20`.

  default: 20

- `page?:optional string`

  Optionally set to the `next_page` token from the previous response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `SkillVersion`

  - `string id`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `\Datetime createdAt`

    ISO 8601 timestamp of when the skill was created.

  - `string description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `string name`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `"skill_version" type`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->skills->versions->list(
  'skill_id',
  limit: 1,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($page);
```

### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```
