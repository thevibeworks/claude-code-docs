---
title: Delete Session
url: https://platform.claude.com/docs/en/api/cli/beta/sessions/delete
---

# Delete Session

`$ ant beta:sessions delete`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

## Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_deleted_session: object`

  Confirmation that a `session` has been permanently deleted.

  - `type: "session_deleted"`

  - `id: string`

## Example

```bash
ant beta:sessions delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```
