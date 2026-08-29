# Delete Skill

`$ ant beta:skills delete`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

## Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

## Returns

- `beta_deleted_skill: object`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: "skill_deleted"`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

## Example

```bash
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```
