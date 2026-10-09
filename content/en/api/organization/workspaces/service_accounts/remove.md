---
title: Delete Service Account Workspace Member
url: https://platform.claude.com/docs/en/api/organization/workspaces/service_accounts/remove
---

# Delete Service Account Workspace Member

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

## Path parameters

- `workspace_id: string`

  ID of the workspace.

- `service_account_id: string`

  ID of the service account.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

## Returns

- `type: "service_account_workspace_member_deleted"`

  default: service_account_workspace_member_deleted

- `service_account_id: string`

  Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

- `workspace_id: string`

  Tagged workspace ID (`wrkspc_...`) named in the delete request.

## Example

```bash
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/service_accounts/$SERVICE_ACCOUNT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```
