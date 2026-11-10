---
title: Organizations
url: https://platform.claude.com/docs/en/api/compliance/organizations
---

# Organizations

## List organizations

**GET** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns organizations sorted by creation date in ascending order. Use
`limit` and `page` to paginate: each response includes `has_more` and a
`next_page` token to pass on the next request.

### Query parameters

- `limit: optional number`

  Maximum results (default: 1000, max: 1000)

  default: 1000, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

### Returns

- `data: array of object`

  List of organizations sorted by creation date, ascending

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: optional string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456+00:00",
      "name": "Acme Corp",
      "uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Domain types

### Organization List Response

- `OrganizationListResponse object`

  Information about an organization.

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

## Organizations › Users

### List organization users

**GET** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

#### Path parameters

- `org_uuid: string`

  The organization UUID

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of current organization members sorted by organization join date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

    format: date-time

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 8 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"parent_org_admin"`

    - `"parent_org_owner"`

    - `"primary_owner"`

    - `"user"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Organizations › User Preferences

### List organization members' personal preferences

**GET** `/v1/compliance/organizations/{org_uuid}/user_preferences`

This endpoint is in beta.

List the personal preferences of an organization's current members.

Returns each member's "Instructions for Claude" and Cowork "Global
instructions" text. Both are account-level settings: the same text is
returned under every organization the member belongs to. Members are
listed in the order they joined the organization, oldest first; use
`limit` and `page` to paginate. A page may hold fewer than `limit`
rows, or none at all, without being the last page: the server bounds
the work it does per request. Follow `next_page` until it is `null`.

#### Path parameters

- `org_uuid: string`

  The organization's UUID

#### Query parameters

- `include_unset: optional boolean`

  When true, list every current member, with `null` for each value they have not set. By default only members with at least one value set are listed.

  default: false

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Restrict the list to these users (max 10 per request). An entry that does not name a current member of the organization matches nothing. Omit to list every eligible member. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

  maxItems: 10

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Current organization members in the order they joined the organization, oldest first. By default only members with at least one value set are listed; with `include_unset=true` every member is.

  - `conversation_preferences: string or null`

    The member's "Instructions for Claude" text from their personal settings, with leading and trailing whitespace removed. `null` when the member has never set it or has cleared it.

  - `cowork_global_instructions: string or null`

    The member's "Global instructions" text for Cowork, Claude's desktop agent, with leading and trailing whitespace removed. `null` when the member has never set it or has cleared it.

  - `user: object`

    The organization member.

    - `id: string`

      User identifier

    - `email_address: string`

      User's current email address

- `has_more: boolean`

  Whether there is a further page to request. A page can hold fewer records than `limit`, or none, and still have more: the server bounds the work it does per request.

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request; `null` on the last page.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/user_preferences \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "conversation_preferences": "Always answer in British English.",
      "cowork_global_instructions": "Prefer short status updates.",
      "user": {
        "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
        "email_address": "jane.doe@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Organizations › Roles

### List Compliance Roles

**GET** `/v1/compliance/organizations/{org_uuid}/roles`

List Compliance Roles

#### Path parameters

- `org_uuid: string`

  The organization UUID

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of roles

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (RFC 3339)

    format: date-time

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (RFC 3339)

    format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789Z"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

### Get Compliance Role

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

#### Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Role identifier (tagged ID)

- `created_at: string or null`

  Role creation timestamp (RFC 3339)

  format: date-time

- `description: string`

  Role description

- `name: string`

  Role name

- `updated_at: string or null`

  Role last-updated timestamp (RFC 3339)

  format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```

## Organizations › Roles › Permissions

### List Compliance Role Permissions

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`

List Compliance Role Permissions

#### Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of permissions

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "action": "claude_code",
      "resource_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "resource_type": "organization"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Organizations › Settings

### Get effective organization settings

**GET** `/v1/compliance/organizations/{organization_id}/settings`

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the
enforced state after all policies are applied, which may differ from what
is configured in the admin console. Settings an organization's
administrators cannot change (for example, ones controlled by Anthropic
policy or not available to the organization) are omitted from the list.
Settings that report a compliance arrangement with Anthropic are the
exception: the HIPAA and Access Transparency settings are always included;
the API zero data retention setting is reported for Claude Console
organizations, and the Claude Code zero data retention and customer-managed
encryption keys (CMEK) settings for Claude Enterprise organizations. Each
reports whether the arrangement is in place at the organization level; a
retention setting on an individual workspace is not reflected.

The organization must belong to the API key's organization hierarchy;
unknown organizations and organizations outside the hierarchy return 404.
The verified_domains and identity_providers settings describe the whole
parent organization and are returned only to API keys that are not
restricted to a single organization.

#### Path parameters

- `organization_id: string`

  The organization's UUID

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `type: optional "effective_organization_settings"`

  default: effective_organization_settings

- `api_keys: array of object`

  Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

  - `type: optional "compliance_api_key"`

    default: compliance_api_key

  - `id: string`

    Unique identifier for the API key.

  - `created_at: string`

    When the key was created.

    format: date-time

  - `created_by_id: string or null`

    Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

  - `is_active: boolean`

    Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

  - `name: string`

    The name given to the API key when it was created.

  - `scopes: array of string`

    The permission scopes granted to the key.

  - `expires_at: optional string or null`

    When the key will stop authenticating, or null when the key does not expire.

    format: date-time

- `organization_id: string`

- `settings: array of Boolean or Integer or String or 5 more`

  - `Boolean object`

    A setting whose enforced value is a single true/false flag.

    - `type: optional "boolean"`

      default: boolean

    - `name: "access_transparency_enabled" or "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or 64 more`

      - `"access_transparency_enabled"`

      - `"ai_powered_artifacts_enabled"`

      - `"api_workbench_feedback_collection_enabled"`

      - `"api_zero_data_retention_enabled"`

      - `"artifact_connectors_enabled"`

      - `"ask_your_org_enabled"`

      - `"chat_cowork_unified_enabled"`

      - `"chat_enabled"`

      - `"claude_academy_inference_enabled"`

      - `"claude_ai_ccr_support_sharing_enabled"`

      - `"claude_ai_chat_external_sharing_enabled"`

      - `"claude_ai_chat_org_sharing_enabled"`

      - `"claude_ai_chat_sharing_enabled"`

      - `"claude_ai_feedback_collection_enabled"`

      - `"claude_ai_integration_sharing_enabled"`

      - `"claude_ai_skill_plugins_scanning_enabled"`

      - `"claude_code_desktop_bypass_permissions_enabled"`

      - `"claude_code_desktop_enabled"`

      - `"claude_code_fast_mode_enabled"`

      - `"claude_code_metrics_logging_enabled"`

      - `"claude_code_remote_control_enabled"`

      - `"claude_code_review_enabled"`

      - `"claude_code_routines_enabled"`

      - `"claude_code_security_enabled"`

      - `"claude_code_trusted_devices_required"`

      - `"claude_code_web_enabled"`

      - `"claude_code_workflows_enabled"`

      - `"claude_design_enabled"`

      - `"claude_enterprise_claude_code_zero_data_retention_enabled"`

      - `"claude_in_slack_enabled"`

      - `"claude_science_auto_mode_enabled"`

      - `"claude_science_custom_connectors_enabled"`

      - `"claude_science_custom_skills_enabled"`

      - `"claude_science_enabled"`

      - `"claude_science_local_work_import_enabled"`

      - `"claude_science_managed_network_allowlist_enabled"`

      - `"claude_science_memory_enabled"`

      - `"claude_science_modal_enabled"`

      - `"claude_science_scientific_model_endpoints_enabled"`

      - `"claude_science_ssh_hosts_enabled"`

      - `"cmek_enabled"`

      - `"code_execution_enabled"`

      - `"code_execution_network_egress_enabled"`

      - `"connector_tools_default_always_allow"`

      - `"content_redaction_enabled"`

      - `"desktop_extension_allowlist_enabled"`

      - `"directory_sync_enabled"`

      - `"frontier_data_use_enabled"`

      - `"group_skill_sharing_enabled"`

      - `"hipaa_compliance_enabled"`

      - `"inline_visualizations_enabled"`

      - `"ip_allowlist_enabled"`

      - `"location_metadata_enabled"`

      - `"member_usage_dashboard_visible"`

      - `"memory_enabled"`

      - `"org_wide_skill_sharing_enabled"`

      - `"project_sharing_enabled"`

      - `"public_projects_enabled"`

      - `"skill_sharing_enabled"`

      - `"skills_enabled"`

      - `"sso_claude_ai_enforced"`

      - `"sso_console_enforced"`

      - `"sso_enabled"`

      - `"third_party_interactive_content_enabled"`

      - `"user_skill_creation_enabled"`

      - `"web_search_enabled"`

      - `"work_across_apps_enabled"`

    - `value: boolean`

  - `Integer object`

    A setting whose enforced value is a whole number; null means no limit
    is in force.

    - `type: optional "integer"`

      default: integer

    - `name: "account_session_duration_seconds"`

    - `value: number or null`

  - `String object`

    A setting whose enforced value is a single string; null means no value
    is configured.

    - `type: optional "string"`

      default: string

    - `name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"`

      - `"claude_code_default_worker_environment_id"`

      - `"claude_code_default_worker_pool_id"`

    - `value: string or null`

  - `StringList object`

    A setting whose enforced value is a list of strings.

    - `type: optional "string_list"`

      default: string_list

    - `name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"`

      - `"allowed_invite_domains"`

      - `"disabled_admin_request_types"`

      - `"ip_allowlist_ip_ranges"`

    - `value: array of string`

  - `ProvisioningMode object`

    How organization members are provisioned, resolved to the enforced mode.

    A configured mode is reported only while the mechanism that enforces it is
    active: just-in-time modes require single sign-on to be enabled, and SCIM
    modes require directory sync to be enabled. Otherwise `login_only` is
    reported, regardless of any stored configuration.

    - `type: optional "provisioning_mode"`

      default: provisioning_mode

    - `value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more`

      How organization members are provisioned under SSO.

      - `"jit_advanced"`

      - `"jit_permissive"`

      - `"login_only"`

      - `"scim_advanced"`

      - `"scim_permissive"`

    - `name: optional "sso_provisioning_mode"`

      default: sso_provisioning_mode

  - `DataRetention object`

    The data retention periods in force, keyed by the type of data they
    apply to.

    A key of `all` covers every data type and is exclusive: when present it
    is the only key. A missing key means no organization-level
    administrator-configured retention period is in force for that data type;
    Anthropic's service defaults may still apply.

    - `type: optional "data_retention"`

      default: data_retention

    - `value: map[Fixed or Indefinite]`

      - `Fixed object`

        A fixed retention window measured from each item's last activity.

        - `type: optional "fixed"`

          default: fixed

        - `duration: number`

        - `timescale: "day" or "month"`

          - `"day"`

          - `"month"`

      - `Indefinite object`

        An indefinite retention period: data is kept with no time limit.

        - `type: optional "indefinite"`

          default: indefinite

    - `name: optional "data_retention_periods"`

      default: data_retention_periods

  - `VerifiedDomains object`

    The domains verified for the organization's parent organization. The
    same for every organization under that parent, and returned only to API
    keys that are not restricted to a single organization.

    - `type: optional "verified_domains"`

      default: verified_domains

    - `value: array of object`

      - `domain: string`

        The verified domain name.

      - `sso_claude_ai_enforced: boolean`

        Whether single sign-on is required to sign in to Claude.ai with an email address on this domain.

      - `sso_console_enforced: boolean`

        Whether single sign-on is required to sign in to the Claude Console with an email address on this domain.

    - `name: optional "verified_domains"`

      default: verified_domains

  - `IdentityProviders object`

    The IdP connections of the organization's parent organization, oldest
    first. The same for every organization under that parent, and returned
    only to API keys that are not restricted to a single organization.

    - `type: optional "identity_providers"`

      default: identity_providers

    - `value: array of object`

      - `id: string`

        Unique identifier for the IdP connection.

      - `directory_sync_enabled: boolean`

        Whether directory sync through this IdP connection is enabled.

      - `sso_enabled: boolean`

        Whether single sign-on through this IdP connection is enabled.

    - `name: optional "identity_providers"`

      default: identity_providers

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "access_transparency_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

## Organizations › Security Posture

### Get an organization's security posture

**GET** `/v1/compliance/organizations/{organization_id}/security_posture`

Get an organization's security controls and their current results.

Returns the organization's security controls, evaluated at the time of the
request, each with its attestation when this endpoint returns one. The controls come
in one `controls` list, which is not paginated. A control can have no entry, for
example when it is about a feature that the organization cannot have, so a missing
control is not a pass.

The `anthropic-version` header is required: a request without it returns 400.
The endpoint takes no query parameters, so there is no filter, and a request with
any query parameter also returns 400. A request also returns 400 when the Compliance
API is not enabled for the API key's parent organization.
The request returns 404 when `organization_id` names no organization, names one
that the API key cannot read, or names one whose security controls are not
available. A request over a rate limit returns 429.

One error has an `error_code` in `error.details`. A 503 with
`posture_evaluation_failed` means that the evaluation could not be completed.
Wait for the time in the `Retry-After` header before trying again. A 504 means
that the evaluation did not finish in time, and the request can be tried again.

#### Path parameters

- `organization_id: string`

  The organization's UUID

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `type: "security_posture"`

  Always `security_posture`.

- `comments_status: "available" or "not_enabled" or "not_permitted" or 2 more`

  Whether attestation comments were read. More values can be added; read an unknown one as `unavailable`.

  - `"available"`

    Comments were read, so a null `comment` means that there is none, or that the attestation was saved moments ago.

  - `"not_enabled"`

    This endpoint does not return comments for the organization, so every `comment` is null.

  - `"not_permitted"`

    The API key holds neither `read:compliance_user_data` nor `read:org_audit`, so every `comment` and every `attested_by` is null.

  - `"requires_organization_key"`

    The API key was not created in the organization, for example because it was created for the parent organization, so no comment is read and every `comment` is null. `attested_by` is returned as it is to a key created in the organization. This value does not say whether this endpoint returns comments for the organization. Retrying does not help: only a key created in the organization can read its comments.

  - `"unavailable"`

    Comments could not be read for this response. A later request may succeed, but some causes persist, for example when the organization's customer-managed encryption key cannot be used.

- `controls: array of object`

  The organization's controls, never empty. A control can have no entry, for example when it is about a feature that the organization cannot have, so a missing control is not a pass.

  - `id: string`

    The control's identifier, which is the same for every organization and never changes.

  - `attestation: object or null`

    The attestation of this control. It is still returned after it stops being in effect; see its `state`. Null when nobody has attested, when attestations of this kind are not enabled for the organization, and while the status is `descriptive`, `not_applicable` or `not_evaluated`. It is also null when the attestation stored for the control is of a kind that this endpoint does not return, so null does not prove that nobody has attested.

    - `attested_at: string`

      When the attestation was made.

      format: date-time

    - `attested_by: object or null`

      Who made the attestation. Null when the response's `comments_status` is `not_permitted`, when showing who attested is not enabled for the organization, when the person's account has been deleted, or while Anthropic holds back who attested for every organization.

      - `type: "user_actor"`

        Always `user_actor`.

      - `user_id: string`

        User identifier (tagged ID, prefixed `user_`).

    - `comment: string or null`

      The comment saved with the attestation, of at most 2,000 characters. It is the text of the last save, which can keep words that an earlier administrator wrote. Null if there is none, or if the response's `comments_status` is not `available`.

    - `state: "check_passing" or "in_force" or "review_due" or "setting_changed" or null`

      Whether the attestation is still in effect. Null only on a manual control, and only when end dates do not apply to the organization; the attestation is then in effect. More values can be added; read an unknown one as not in effect.

      - `"check_passing"`

        Not in effect: the automatic check passes.

      - `"in_force"`

        The attestation is in effect.

      - `"review_due"`

        Not in effect: the attestation's end date, also called its review date, has come, so it is due for review.

      - `"setting_changed"`

        Not in effect: the automatic check fails, either on a different value from the one whose risk was accepted, or after the accepted risk was recorded as ended.

  - `current_value: string or null`

    The value read for the control, as display text whose wording can change. It is in English, apart from values taken from the organization's settings, such as its allowed email domains. A list names only the entries that this endpoint recognizes, followed by the number of other entries, if any. Null on a manual control, while the status is `not_evaluated`, and while the status is `not_applicable` because the control applies only when another setting has a certain value.

  - `desired_state: string or null`

    The recommended value, as display text whose wording can change. It is in English, apart from values such as the organization's ID. Null when there is none for this organization.

  - `display_name: string`

    The control's display name, in English.

  - `rating: "descriptive" or "failed" or "not_attested" or "passed"`

    The control's overall result, which follows from `status`. More values can be added; read an unknown one as not passed.

    - `"descriptive"`

      Descriptive: not rated, which includes controls that do not apply or could not be read.

    - `"failed"`

      Failed. Because of an attestation that this endpoint does not return, a control can have this rating while the Security posture page shows it as Passed.

    - `"not_attested"`

      Not attested: a manual control with no attestation in effect.

    - `"passed"`

      Passed. This includes a control with an accepted risk in effect, whether automatic or manual.

  - `section: "capabilities" or "chats_desktop_mdm" or "claude_code_admin_console" or 7 more`

    The section that this control belongs to. More values can be added; treat an unknown one as a section of its own.

    - `"capabilities"`

      Capabilities

    - `"chats_desktop_mdm"`

      Chats: desktop device management

    - `"claude_code_admin_console"`

      Claude Code: admin console

    - `"claude_code_managed_settings"`

      Claude Code: managed settings

    - `"connectors_integrations"`

      Connectors and integrations

    - `"cowork_admin_console"`

      Cowork: admin console

    - `"cowork_desktop_mdm"`

      Cowork: desktop device management

    - `"data_privacy"`

      Data and privacy

    - `"healthy_adoption"`

      Healthy adoption

    - `"identity_access"`

      Identity and access

  - `setting_name: string or null`

    The `name` of the entry in the organization's effective settings that this control reads. Null when it reads no such entry.

  - `status: "attestation_not_enabled" or "attested_accepted_risk" or "attested_completed" or 10 more`

    Why the control has its rating. A manual control is one that only a person can check. An automatic control reads a value from the organization, usually one of its settings, and some are checked against a recommended value. The recommended values are those of the standard profile, which every organization is rated under. More values can be added; count a control with an unknown one by its `rating`.

    - `"attestation_not_enabled"`

      A manual control that nobody in the organization can attest to.

    - `"attested_accepted_risk"`

      A manual control attested as Accepted risk, with the attestation in effect.

    - `"attested_completed"`

      A manual control attested as Completed, with the attestation in effect.

    - `"descriptive"`

      The control is reported for information only.

    - `"exceeds_baseline"`

      The current value is stricter than the recommended value.

    - `"failed"`

      The current value does not meet the recommended value. An attestation that this endpoint does not return can also give a control this status.

    - `"failed_check_accepted_risk"`

      The automatic check fails, and an accepted risk is in effect.

    - `"matches_profile"`

      The current value equals the recommended value.

    - `"not_applicable"`

      The control does not apply to the organization.

    - `"not_attested"`

      A manual control that can be attested to, with no attestation in effect.

    - `"not_evaluated"`

      The setting behind the control, or another setting that decides whether the control applies, could not be read.

    - `"passed"`

      The current value meets the recommended value.

    - `"review"`

      The current value is looser than the recommended value.

- `evaluated_at: string`

  The time at which every control was evaluated.

  format: date-time

- `organization_id: string`

  The organization's UUID.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/security_posture \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "comments_status": "not_enabled",
  "controls": [
    {
      "id": "sso_enabled",
      "attestation": {
        "attested_at": "2025-03-12T18:22:41.123456Z",
        "attested_by": {
          "type": "user_actor",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        },
        "comment": null,
        "state": "in_force"
      },
      "current_value": "On",
      "desired_state": "On",
      "display_name": "Single sign-on (SSO)",
      "rating": "passed",
      "section": "identity_access",
      "setting_name": "sso_enabled",
      "status": "passed"
    }
  ],
  "evaluated_at": "2025-03-12T18:22:41.123456Z",
  "organization_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "type": "security_posture"
}
```
