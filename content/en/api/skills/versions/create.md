# Create Skill Version

**POST** `/v1/skills/{skill_id}/versions`

Create Skill Version

## Path parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

## Body parameters (form-data)

- `files: array of string`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

## Returns

- `SkillVersion object`

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

    default: skill_version

## Example

```bash
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F files='["Example data"]'
```

### Response (200)

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
