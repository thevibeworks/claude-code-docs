# Create Skill

**POST** `/v1/skills`

Create Skill

## Body parameters (form-data)

- `files: array of string`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `display_name: optional string or null`

  Human-readable, single-line label for the Skill. Maximum 255 characters.
  Always set: derived from the SKILL.md frontmatter `name` when omitted at
  creation. Not unique.

## Returns

- `Skill object`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `display_name: string`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `latest_version_id: string`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `source: SkillSource`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `type: "custom" or "anthropic" or "anthropic_example" or "plugin"`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `"custom"`

      - `"anthropic"`

      - `"anthropic_example"`

      - `"plugin"`

  - `type: "skill"`

    Object type.

    For Skills, this is always `"skill"`.

    default: skill

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

## Example

```bash
curl https://api.anthropic.com/v1/skills \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F files='["Example data"]'
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
