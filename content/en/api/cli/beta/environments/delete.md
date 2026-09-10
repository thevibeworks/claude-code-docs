---
title: Delete Environment
url: https://platform.claude.com/docs/en/api/cli/beta/environments/delete
---

# Delete Environment

`$ ant beta:environments delete`

**DELETE** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

## Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_environment_delete_response: object`

  Response after deleting an environment.

  - `type: "environment_deleted"`

    The type of response

  - `id: string`

    Environment identifier

## Example

```bash
ant beta:environments delete \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```
