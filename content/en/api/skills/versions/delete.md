---
title: Delete Skill Version
url: https://platform.claude.com/docs/en/api/skills/versions/delete
---

## Delete Skill Version

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Path Parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Identifies the skill version: a version ID, or — where the endpoint accepts it — the literal `latest` for the skill's most recent version.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

### Returns

- `DeletedSkillVersion object { id, type }`

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `type: "skill_version_deleted"`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

    - `"skill_version_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```
