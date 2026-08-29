# List Skill Versions

`$ ant beta:skills:versions list`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

## Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--limit: optional number`

  Query param: Number of results to return per page.

  Ranges from `1` to `1000`. Defaults to `20`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaListSkillVersionsResponse: object`

  - `data: array of BetaSkillVersion`

    List of skills.

    - `id: string`

      Unique identifier for this Skill Version. The id addresses the version in
      paths and pins it in references.

    - `created_at: string`

      ISO 8601 timestamp of when the skill was created.

      format: date-time

    - `description: string`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `name: string`

      The Skill's immutable kebab-case slug, set at creation from the first
      upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
      later upload must resolve to the same value. Also the top-level directory
      of the Skill's mounted files and the base name of a downloaded archive.

    - `skill_id: string`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `type: "skill_version"`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

  - `next_page: string`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

## Example

```bash
ant beta:skills:versions list \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
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
