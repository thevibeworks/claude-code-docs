# Code

## Code › Artifacts

### List Code Artifacts

**GET** `/v1/compliance/apps/code/artifacts`

List Claude Code Artifacts owned by organizations under the parent
organization.

Results are sorted by Artifact identifier. Pages may be short or empty
while `next_page` is still set — continue until `next_page` is absent.
Artifacts are sorted by identifier (not creation time): an Artifact
published during an export may land before the cursor and be omitted, so
for a point-in-time-complete export re-enumerate after publishing
quiesces.

Artifacts owned by a since-deleted child organization are not
returned.

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, maximum: 100, minimum: 1

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.

  maxItems: 500

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gt: optional string`

    Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

    format: date-time

  - `gte: optional string`

    Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.

    format: date-time

  - `lt: optional string`

    Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.

    format: date-time

  - `lte: optional string`

    Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

    format: date-time

- `user_ids: optional array of string`

  Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

  maxItems: 200

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Page of Artifacts

  - `id: string`

    Artifact identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this Artifact belongs to

  - `owner_user_id: string or null`

    Artifact owner's user identifier (tagged ID), or null for Artifacts published by an agent session rather than a user account. When set, it survives after the owner's account is deleted or the owner leaves every organization under the parent.

  - `published_version_id: string or null`

    Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened.

  - `read_mode: "org" or "owner" or "public" or "users"`

    Who can view this Artifact: only its owner, a named set of users, every member of its organization, or anyone on the internet (`public`)

    - `"org"`

    - `"owner"`

    - `"public"`

    - `"users"`

  - `updated_at: string or null`

    Artifact last update timestamp, or null for Artifacts published before this field was recorded

    format: date-time

  - `user: object or null`

    The user who owns a Code Artifact.

    Fields that reference this type are null when the Artifact was
    published by an agent session rather than a user account, when the
    owner's account has been deleted, or when the owner is no longer a
    member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `versions: array of object`

    Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

    - `id: string`

      Opaque version identifier

    - `created_at: string or null`

      When this version was published

      format: date-time

    - `name: string`

      Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

- `has_more: boolean`

  Whether `next_page` is set. May be true for a page whose next page is empty — continue until `next_page` is absent.

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
      "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "owner_user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "published_version_id": "1741803761-9f3a",
      "read_mode": "org",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      },
      "versions": [
        {
          "id": "1741803761-9f3a",
          "created_at": "2025-03-12T18:22:41.123456Z",
          "name": "Team dashboard"
        }
      ]
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

### Download Code Artifact Version Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}`

Streams the content of one version of a Claude Code Artifact as the
response body.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. A listed version id can start returning 404 if subsequent
publishes rotated it out of retained history — re-list on 404. Returns
503 while the version's content upload is
still in flight or was abandoned — retry with backoff. Oversized
encoded content aborts mid-stream: headers and initial bytes arrive
but the body terminates early — an aborted chunked transfer is the
only truncation signal for encoded content. `Content-MD5` is emitted
only for identity-stored content; validate against it when present.

#### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Delete Code Artifact

**DELETE** `/v1/compliance/apps/code/artifacts/{artifact_id}`

Permanently deletes a Code Artifact and all its versions. This is a
destructive operation that cannot be undone. A 200 response means the
deletion is initiated and the Artifact is claimed; content removal
completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. Returns 404 on a repeated delete of an already-deleted
Artifact.

#### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  The ID of the Artifact that was deleted

- `type: "code_artifact_deleted"`

  Constant string confirming deletion

  default: code_artifact_deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```
