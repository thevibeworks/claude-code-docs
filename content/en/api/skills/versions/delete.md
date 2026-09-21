---
title: Delete Skill Version
url: https://platform.claude.com/docs/en/api/skills/versions/delete
---

# Delete Skill Version

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

## Path parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: string`

  Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

## Headers

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `DeletedSkillVersion object`

  - `type: "skill_version_deleted"`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

    default: skill_version_deleted

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

## Example

```bash
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```
