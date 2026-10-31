---
title: Artifacts
url: https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts
---

# Artifacts

## List Code Artifacts

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

### Query parameters

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

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

### Returns

- `data: array of object`

  Page of Artifacts

  - `id: string`

    Artifact identifier (tagged ID)

  - `artifact_type: "claude_dashboards" or "claude_design" or "claude_design_systems" or 5 more`

    Which kind of Artifact this is: `code` for a site published from Claude Code, or the built-in Artifact type it was made from — `claude_docs` (Claude Docs), `claude_slides` (Slides), `claude_design` (Design), `claude_design_systems` (a design system), `claude_motion` (Motion) or `claude_dashboards` (Dashboards). `other` is an Artifact made from a built-in type this list does not name yet.

    - `"claude_dashboards"`

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

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
      "artifact_type": "code",
      "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "owner_user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
      "published_version_id": "1741803761-9f3a",
      "read_mode": "org",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user": {
        "id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
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

## Download Code Artifact Version Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}`

Streams the content of one version of an Artifact as the response body, in chunks with no `Content-Length`. With `multi_file_format=zip`, a version with more than one file, other than a Claude Doc's (an Artifact whose `artifact_type` is `claude_docs`), comes back as a ZIP archive of its files.

Headers: `Content-Type` (`application/zip` for a ZIP archive, otherwise the stored MIME type), `Content-Disposition: attachment; filename*=utf-8''<name>` (RFC 5987), `Cache-Control: no-store, private` and, when available, `Content-MD5` (base64). `<name>` is `{artifact_id}-{version_id}.zip` for a ZIP archive, otherwise `{artifact_id}-{version_id}.txt`, whatever the content is. `Content-MD5` is only on a single file stored uncompressed, so it is never on a ZIP archive. Check the body against it when present.

Errors specific to this download:

- `404`: the Artifact doesn't exist or the API key cannot read it, or the version is no longer kept. Older versions are dropped as new ones are published, so list the Artifact's versions again. You also get this when the organization's customer-managed encryption key can't be used. Retry once the key can be used again.
- `503`: the content can't be served right now, for example because its upload is still in progress or was abandoned. Retry with backoff.
- `422` with `error.details.error_code` `multi_file_unavailable`: the version has more than one file. Add `multi_file_format=zip`. A Claude Doc's version with more than one file gets this error either way, because it holds only the web page that displays the Doc. Download the Doc's text with `GET /v1/compliance/apps/code/artifacts/{artifact_id}/content?multi_file_format=zip`.
- `422` with `file_set_unavailable`: the request sets `multi_file_format=zip`, the version has more than one file, and one of them has a path the API cannot export. Do not retry.

An error after the download has started stops the body early, with the `200` status already sent. For example, this happens to content stored compressed when it is over 16 MiB once decompressed. For a single file with no `Content-MD5`, the only sign is a transfer that aborts before its last chunk, so treat a download that aborts this way as failed.

A ZIP archive of a version's files holds one top-level folder, named for the Artifact and version. That folder holds a `files/` folder and an index, `files.json`. The index is written last, so treat an archive as incomplete if it cannot be opened or has no `files.json` in its top-level folder.

`files.json` has these fields:

- `artifact_id`: the Artifact ID, as in the request.
- `version_id`: the version ID, as in the request.
- `title`: the title of the version in the archive, or that version's ID when no title is kept.
- `created_at`: when the version was published (RFC 3339, UTC), or null when that is not known.
- `files`: one entry for each file under `files/`, with `original_path` (the file's path in the version), `exported_as` (its path in the archive), `sha256` (lowercase hex), `size_bytes` (before compression) and `mime_type`. `exported_as` is the top-level folder, then `files/`, then `original_path`. A name that could not be saved or opened safely on every operating system is changed. Use `exported_as`, not `original_path`, to find a file in the archive.
- `omitted_files`: the files left out of the archive, each with `original_path`, `sha256`, `size_bytes` and `mime_type`. They include files the version uses from another Artifact. They also include files copied from the Artifact type the Artifact was made from, such as the app that displays it, when another organization owns that type.

`files` and `omitted_files` together list at most 4,096 files, their `size_bytes` add up to at most 1 GiB, and no file is over 20 MiB.

### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

### Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value, to receive a version that has more than one file as a ZIP archive of its files with an index, `files.json`. A version with one file is returned as that file. A Claude Doc's version never comes back as a ZIP.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Download Code Artifact Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/content`

Streams an Artifact's current content as the response body, in chunks with no `Content-Length`.

For a Claude Doc (an Artifact whose `artifact_type` is `claude_docs`), the request must set `multi_file_format=zip`, and the content is the Doc's text as a ZIP archive of Word files. That ZIP has no `files.json`. It holds one Word file per text tab, in tab order, named `NN-<tab id>.docx`, where `NN` counts from `01`. A Doc with one text tab gets one file, `01-document.docx`.

For any other Artifact, the content is the latest version. With `multi_file_format=zip`, when the latest version has more than one file, it comes back as a ZIP archive of its files.

Headers: `Content-Type` (`application/zip` for a ZIP archive, otherwise the stored MIME type), `Content-Disposition: attachment; filename*=utf-8''<name>` (RFC 5987), `Cache-Control: no-store, private` and, when available, `Content-MD5` (base64). `<name>` is `{artifact_id}.zip` for a ZIP archive, otherwise `{artifact_id}.txt`, whatever the content is. `Content-MD5` is always on a Claude Doc's ZIP, only on a single file stored uncompressed, and never on a ZIP archive of a version's files. Check the body against it when present.

Errors specific to this download:

- `404`: the Artifact doesn't exist, or the API key cannot read it.
- `400` with `error.details.error_code` `cmek_key_disabled`: the organization's customer-managed encryption key can't be used, for example because it is disabled or revoked. Retry once the key can be used again.
- `503`: the content can't be produced right now. Wait the number of seconds in the `Retry-After` header, or retry with backoff when it is absent.
- `422` with `multi_file_unavailable`: the request does not set `multi_file_format=zip`, and the Artifact is a Claude Doc or its latest version has more than one file. Add the parameter.
- `422` with `file_set_unavailable`: the request sets `multi_file_format=zip`, the Artifact is not a Claude Doc, and one of the latest version's files has a path the API cannot export. Do not retry.
- `422` with `document_unavailable`: Claude Docs has no document it can export for the Doc, for example because it has no text tab or is in the trash. Retrying will not help unless that changes.
- `422` with `document_too_large`: the Doc's export is over 16 MiB. Do not retry.
- `422` with `cmek_org_unsupported`: the organization uses customer-managed encryption keys and the export can't be served for it right now. Try again later, and contact Anthropic support if this continues.

An error after the download has started stops the body early, with the `200` status already sent. For example, this happens to content stored compressed when it is over 16 MiB once decompressed. For a single file with no `Content-MD5`, the only sign is a transfer that aborts before its last chunk, so treat a download that aborts this way as failed.

A ZIP archive of a version's files holds one top-level folder, named for the Artifact. That folder holds a `files/` folder and an index, `files.json`. The index is written last, so treat an archive as incomplete if it cannot be opened or has no `files.json` in its top-level folder.

`files.json` has these fields:

- `artifact_id`: the Artifact ID, as in the request.
- `version_id`: null.
- `title`: the title of the version in the archive, or that version's ID when no title is kept.
- `created_at`: when the version was published (RFC 3339, UTC), or null when that is not known.
- `files`: one entry for each file under `files/`, with `original_path` (the file's path in the version), `exported_as` (its path in the archive), `sha256` (lowercase hex), `size_bytes` (before compression) and `mime_type`. `exported_as` is the top-level folder, then `files/`, then `original_path`. A name that could not be saved or opened safely on every operating system is changed. Use `exported_as`, not `original_path`, to find a file in the archive.
- `omitted_files`: the files left out of the archive, each with `original_path`, `sha256`, `size_bytes` and `mime_type`. They include files the version uses from another Artifact. They also include files copied from the Artifact type the Artifact was made from, such as the app that displays it, when another organization owns that type.

`files` and `omitted_files` together list at most 4,096 files, their `size_bytes` add up to at most 1 GiB, and no file is over 20 MiB.

### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

### Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value. A Claude Doc downloads only this way, as a ZIP archive of Word files, one per text tab. For any other Artifact, when the latest version has more than one file, it comes back as a ZIP archive of its files with an index, `files.json`.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete Code Artifact

**DELETE** `/v1/compliance/apps/code/artifacts/{artifact_id}`

Permanently deletes a Code Artifact and all its versions. This is a
destructive operation that cannot be undone. A 200 response means the
deletion is initiated and the Artifact is claimed; content removal
completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. Returns 404 on a repeated delete of an already-deleted
Artifact.

### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

### Returns

- `type: "code_artifact_deleted"`

  Constant string confirming deletion

  default: code_artifact_deleted

- `id: string`

  The ID of the Artifact that was deleted

### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response (200)

```json
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```

## Domain types

### Artifact List Response

- `ArtifactListResponse object`

  An Artifact: a site published from Claude Code, or a document made
  from one of Anthropic's built-in Artifact types (Claude Docs, Slides,
  Design, …). `artifact_type` says which.

  - `id: string`

    Artifact identifier (tagged ID)

  - `artifact_type: "claude_dashboards" or "claude_design" or "claude_design_systems" or 5 more`

    Which kind of Artifact this is: `code` for a site published from Claude Code, or the built-in Artifact type it was made from — `claude_docs` (Claude Docs), `claude_slides` (Slides), `claude_design` (Design), `claude_design_systems` (a design system), `claude_motion` (Motion) or `claude_dashboards` (Dashboards). `other` is an Artifact made from a built-in type this list does not name yet.

    - `"claude_dashboards"`

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

### Artifact Delete Response

- `ArtifactDeleteResponse object`

  Response for deleting a Code Artifact.

  - `type: "code_artifact_deleted"`

    Constant string confirming deletion

    default: code_artifact_deleted

  - `id: string`

    The ID of the Artifact that was deleted
