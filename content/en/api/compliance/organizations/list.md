---
title: List organizations
url: https://platform.claude.com/docs/en/api/compliance/organizations/list
---

# List organizations

**GET** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns organizations sorted by creation date in ascending order. Use
`limit` and `page` to paginate: each response includes `has_more` and a
`next_page` token to pass on the next request.

## Query parameters

- `limit: optional number`

  Maximum results (default: 1000, max: 1000)

  default: 1000, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

## Headers

- `"anthropic-version": string`

  The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

  See [API versions](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http) for the available versions.

- `"x-api-key": optional string`

## Returns

- `data: array of object`

  List of organizations sorted by creation date, ascending

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

  - `organization_type: optional "claude_enterprise" or "claude_platform" or "claude_team" or null`

    The kind of organization: `claude_enterprise` for a claude.ai organization on the Enterprise plan, `claude_team` for a claude.ai organization on the Team plan, or `claude_platform` for a Claude Console organization. Null for an organization of any other kind. More values can be added; treat a value you don't recognize as you would null.

    - `"claude_enterprise"`

    - `"claude_platform"`

    - `"claude_team"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: optional string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

## Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456+00:00",
      "name": "Acme Corp",
      "uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "organization_type": "claude_enterprise"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```
