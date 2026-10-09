---
title: Add Workspace To Service Account
url: https://platform.claude.com/docs/en/api/organization/service_accounts/workspaces/add
---

# Add Workspace To Service Account

**POST** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected.

## Path parameters

- `service_account_id: string`

  ID of the service account.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning).

## Body parameters

- `workspace_id: string`

  Tagged workspace ID to add the service account to.

- `workspace_role: NoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

## Returns

- `ServiceAccountWorkspaceMember object`

  - `type: "service_account_workspace_member"`

    default: service_account_workspace_member

  - `created_by_actor_id: string or null`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: boolean or null`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: string`

    Tagged service account ID (`svac_...`).

  - `workspace_id: string`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

## Example

```bash
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_id": "workspace_id",
          "workspace_role": "workspace_admin"
        }'
```

### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```
