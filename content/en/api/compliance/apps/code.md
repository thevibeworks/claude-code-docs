---
title: Code
url: https://platform.claude.com/docs/en/api/compliance/apps/code
---

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

  default: 20, minimum: 1, maximum: 100

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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Page of Artifacts

  - `id: string`

    Artifact identifier (tagged ID)

  - `artifact_type: "claude_design" or "claude_design_systems" or "claude_docs" or 4 more`

    Which kind of Artifact this is: `code` for a site published from Claude Code, or the built-in Artifact type it was made from — `claude_docs` (Claude Docs), `claude_slides` (Slides), `claude_design` (Design), `claude_design_systems` (a design system) or `claude_motion` (Motion). `other` is an Artifact made from a built-in type this list does not name yet.

    - `"claude_design"`

    - `"claude_design_systems"`

    - `"claude_docs"`

    - `"claude_motion"`

    - `"claude_slides"`

    - `"code"`

    - `"other"`

  - `organization_uuid: string`

    Organization UUID this Artifact belongs to

  - `owner_user_id: string or null`

    Artifact owner's user identifier (tagged ID), or null for Artifacts published by an agent session rather than a user account. When set, it survives after the owner's account is deleted or the owner leaves every organization under the parent.

  - `published_version_id: string or null`

    Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened. Null for a Claude Doc; see `versions`.

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

    Artifact owner with email, or null if the Artifact was published by an agent session, the owner's account has been deleted, or the owner is no longer a member of an organization the key may read

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `versions: array of object`

    Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content. Empty for a Claude Doc, because a Doc's versions hold only the web page that displays it, not its text. Download a Doc's text with `GET /v1/compliance/apps/code/artifacts/{artifact_id}/content?multi_file_format=zip`.

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
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
      "artifact_type": "code",
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
503 while the version's content upload is still in flight or was
abandoned — retry with backoff. Returns 422 with
`error.details.error_code` `multi_file_unavailable` for a version that
has more than one file, unless the request sets `multi_file_format=zip`,
which returns those files as a ZIP archive. With `multi_file_format=zip`,
a version with more than one file, one of them with a name the API cannot
export, gets 422 `file_set_unavailable`. Do not retry a 422. A Claude
Doc's versions hold only the web page that displays the Doc and never come
back as a ZIP. That page usually has more than one file, so a Doc's version
usually gets the 422 `multi_file_unavailable`. Download the Doc's text with
`GET /v1/compliance/apps/code/artifacts/{artifact_id}/content?multi_file_format=zip`.
Oversized encoded content aborts mid-stream: headers and initial bytes arrive
but the body terminates early — an aborted chunked transfer is the
only truncation signal for encoded content. `Content-MD5` is emitted
only for identity-stored content; validate against it when present.

#### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

#### Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value, to receive a version that has more than one file as a ZIP archive of its files with an index, `files.json`. Files the artifact copied from its type (the app that displays every artifact of that type) are listed under `omitted_files` in the index, and left out of the archive, when an organization other than the artifact's owns that type. A Claude Doc's version never comes back as a ZIP: it is answered as without this parameter, except that a version with more than one file, one of them with a name the API cannot export, gets 422 `file_set_unavailable`. A version with one file is returned as that file, as without this parameter.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Download Code Artifact Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/content`

Streams an Artifact's current content as the response body. For a
Claude Doc, that is the Doc's text as a ZIP archive of Word files, one per
text tab, and the request must set `multi_file_format=zip`. For any other
Artifact, it is the latest version, as
`GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}`
returns it.

Returns 404 for Artifacts that don't exist or that the API key cannot read.
Returns 400 with `error.details.error_code` `cmek_key_disabled` when the
organization's customer-managed encryption key can't be used, for example
because it is disabled or revoked. Returns 503 when the content can't be
produced right now; wait the number of seconds in the `Retry-After`
header, or retry with backoff when it is absent. For a Claude Doc, a 422's
`error.details.error_code` is `multi_file_unavailable` when the request
does not set `multi_file_format=zip`, `document_unavailable` when the Doc
has no text to export (for example, it has no text tab or is in the trash),
`document_too_large` when the export is over 16 MiB, or
`cmek_org_unsupported` when the organization uses customer-managed
encryption keys and the export can't be served for it right now. For any
other Artifact, the 422s are the version download's.

#### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

#### Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value. A Claude Doc downloads only this way, as a ZIP archive of Word files, one per text tab. For any other Artifact it works as on the version download: when the latest version has more than one file, it comes back as a ZIP archive of its files with an index, `files.json`.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/content \
    -H 'anthropic-version: 2023-06-01' \
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

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

#### Returns

- `type: "code_artifact_deleted"`

  Constant string confirming deletion

  default: code_artifact_deleted

- `id: string`

  The ID of the Artifact that was deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```
