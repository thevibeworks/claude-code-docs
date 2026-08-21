---
title: Get Skill Version
url: https://platform.claude.com/docs/en/api/skills/versions/retrieve
---

## Get Skill Version

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Identifies the skill version: a version ID, or — where the endpoint accepts it — the literal `latest` for the skill's most recent version.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

### Returns

- `SkillVersion object { id, created_at, description, 3 more }`

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

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

    - `"skill_version"`

### Example

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```
