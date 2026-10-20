---
title: List organization members' personal preferences
url: https://platform.claude.com/docs/en/api/compliance/organizations/user_preferences/list
---

# List organization members' personal preferences

**GET** `/v1/compliance/organizations/{org_uuid}/user_preferences`

List the personal preferences of an organization's current members.

Returns each member's "Instructions for Claude" and Cowork "Global
instructions" text. Both are account-level settings: the same text is
returned under every organization the member belongs to. Members are
listed in the order they joined the organization, oldest first; use
`limit` and `page` to paginate. A page may hold fewer than `limit`
rows, or none at all, without being the last page: the server bounds
the work it does per request. Follow `next_page` until it is `null`.

## Path parameters

- `org_uuid: string`

  The organization's UUID

## Query parameters

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

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

## Returns

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

## Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/user_preferences \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "conversation_preferences": "Always answer in British English.",
      "cowork_global_instructions": "Prefer short status updates.",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```
