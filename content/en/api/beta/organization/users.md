---
title: Users
url: https://platform.claude.com/docs/en/api/beta/organization/users
---

# Users

## List Users

**GET** `/v1/organizations/users`

List the organization's members.

### Query parameters

- `after_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: optional string`

  Filter by user email.

  format: email

- `limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, minimum: 1, maximum: 1000

- `roles: optional array of string`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Returns

- `data: array of BetaOrganizationUser`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

- `first_id: string or null`

  First ID in the `data` list. Can be used as the `before_id` for the previous page.

- `has_more: boolean`

  Indicates if there are more results in the requested page direction.

- `last_id: string or null`

  Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/users \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "admin",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Get User

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

### Path parameters

- `user_id: string`

  ID of the User.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Returns

- `BetaOrganizationUser object`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

## Update User

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

### Path parameters

- `user_id: string`

  ID of the User.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Body parameters

- `role: "billing" or "claude_code_user" or "developer" or 2 more`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`; changing a User's role to `managed` requires the `write:rbac_groups` scope in addition to `write:members`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

### Returns

- `BetaOrganizationUser object`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "role": "user"
        }'
```

#### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

## Remove User

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

### Path parameters

- `user_id: string`

  ID of the User.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

### Returns

- `type: "user_deleted"`

  Deleted object type.

  For Users, this is always `"user_deleted"`.

  default: user_deleted

- `id: string`

  ID of the User.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "type": "user_deleted"
}
```

## Sign Out User

**POST** `/v1/organizations/users/{user_id}/sign_out`

Sign a member out of Claude everywhere, without removing them from the organization. This ends their sign-in sessions and removes their trusted devices wherever they use Claude, including other organizations and individual plans. It also ends the OAuth tokens issued to them for this organization, so apps such as Claude Code must sign in again.

A token can take up to an hour to stop working, though it almost always stops at once. The member keeps their role and can sign in again right away. To keep them out, remove them from the organization or, if your organization uses single sign-on, block them in your identity provider. Signing out does not end API keys, OAuth tokens that were not issued for this organization, or the member's Claude Code cloud sessions and routines.

You cannot sign out the organization's primary owner or the person your API key or token acts for, and a request to sign out another owner, a member with owner permissions, or a membership admin may be refused. A refused request returns a `400` or `403` error that says why. If the request returns `503`, send it again to finish; anything already ended stays ended.

Every request must include the beta header `anthropic-beta: admin-user-sign-out-2026-10-08`. A request without it returns `400`. Sign-out is in beta for Claude Enterprise organizations. In an organization where it is not enabled, a request returns `400` with `error_code` `organization_not_enrolled_in_beta`. In a Claude Enterprise organization, an API key needs the `write:members` scope; a key without it gets `403`.

### Path parameters

- `user_id: string`

  ID of the User.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": array of AnthropicBeta`

  This endpoint is in beta: requests must send `admin-user-sign-out-2026-10-08` in this header.

  - `string`

  - `"message-batches-2024-09-24"`

  - `"prompt-caching-2024-07-31"`

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"pdfs-2024-09-25"`

  - `"token-counting-2024-11-01"`

  - `"token-efficient-tools-2025-02-19"`

  - `"output-128k-2025-02-19"`

  - `"files-api-2025-04-14"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"extended-cache-ttl-2025-04-11"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"skills-2025-10-02"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

  - `"cache-diagnosis-2026-04-07"`

  - `"dreaming-2026-04-21"`

  - `"thinking-token-count-2026-05-13"`

  - `"server-side-fallback-2026-06-01"`

  - `"server-side-fallback-2026-07-01"`

  - `"fallback-credit-2026-06-01"`

  - `"fallback-credit-2026-07-01"`

  - `"agent-memory-2026-07-22"`

  - `"mid-conversation-tool-changes-2026-07-01"`

  - `"compact-2026-01-12"`

  - `"computer-use-2025-11-24"`

  - `"mcp-tunnels-2026-06-22"`

  - `"structured-outputs-2025-11-13"`

  - `"task-budgets-2026-03-13"`

  - `"thinking-display-updates-2026-08-18"`

  - `"ce-user-management-2026-07-13"`

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

  - `"admin-user-sign-out-2026-10-08"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

### Returns

- `BetaOrganizationUser object`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

### Example

```bash
curl https://api.anthropic.com/v1/organizations/users/$USER_ID/sign_out \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: admin-user-sign-out-2026-10-08' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

## Domain types

### Beta Cannot Sign Out Managed Member Error Details

- `BetaCannotSignOutManagedMemberErrorDetails object`

  The member has the `managed` role, and this API key or token cannot sign them out. The error message says which keys and tokens can.

  - `error_code: "cannot_sign_out_managed_member"`

### Beta Cannot Sign Out Membership Admin Error Details

- `BetaCannotSignOutMembershipAdminErrorDetails object`

  The member is a membership admin, and the person the API key or token belongs to is not allowed to sign out membership admins.

  - `error_code: "cannot_sign_out_membership_admin"`

### Beta Cannot Sign Out Owner Error Details

- `BetaCannotSignOutOwnerErrorDetails object`

  The member is an owner or has owner permissions, and this API key or token cannot sign them out. In a Claude Enterprise organization, an API key with the `write:members` scope can.

  - `error_code: "cannot_sign_out_owner"`

### Beta Cannot Sign Out Primary Owner Error Details

- `BetaCannotSignOutPrimaryOwnerErrorDetails object`

  The member is the organization's primary owner, whom no API key or token can sign out.

  - `error_code: "cannot_sign_out_primary_owner"`

### Beta Cannot Sign Out Privileged Member Error Details

- `BetaCannotSignOutPrivilegedMemberErrorDetails object`

  This OAuth token cannot sign out a membership admin or a member whose roles grant owner, user management, or identity and access management.

  - `error_code: "cannot_sign_out_privileged_member"`

### Beta Cannot Sign Out Self Error Details

- `BetaCannotSignOutSelfErrorDetails object`

  The member is the user the API key or token belongs to.

  - `error_code: "cannot_sign_out_self"`

### Beta Organization User

- `BetaOrganizationUser object`

  - `type: "user"`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: string`

    ID of the User.

  - `added_at: string`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: string`

    Email of the User.

  - `name: string`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

### User Remove Response

- `UserRemoveResponse object`

  - `type: "user_deleted"`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

    default: user_deleted

  - `id: string`

    ID of the User.
