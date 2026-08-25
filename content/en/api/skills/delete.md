# Delete Skill

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

## Path parameters

- `skill_id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

## Returns

- `DeletedSkill object`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: "skill_deleted"`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

    default: skill_deleted

## Example

```bash
curl https://api.anthropic.com/v1/skills/$SKILL_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```
