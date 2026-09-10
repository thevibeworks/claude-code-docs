---
title: Get Skill Version
url: https://platform.claude.com/docs/en/api/cli/beta/skills/versions/retrieve
---

# Get Skill Version

`$ ant beta:skills:versions retrieve`

**GET** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

## Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Identifies the skill version: a version ID, or the literal `latest` for the skill's most recent version.

  Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_skill_version: object`

  - `type: "skill_version"`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

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

## Example

```bash
ant beta:skills:versions retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
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
