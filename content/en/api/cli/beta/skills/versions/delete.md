---
title: Delete Skill Version
url: https://platform.claude.com/docs/en/api/cli/beta/skills/versions/delete
---

# Delete Skill Version

`$ ant beta:skills:versions delete`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

## Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Identifies the skill version by its version ID.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_deleted_skill_version: object`

  - `type: "skill_version_deleted"`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

  - `id: string`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

## Example

```bash
ant beta:skills:versions delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

### Response (200)

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```
