---
title: Delete Skill
url: https://platform.claude.com/docs/en/api/cli/beta/skills/delete
---

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

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_deleted_skill: object`

  - `type: "skill_deleted"`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

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
