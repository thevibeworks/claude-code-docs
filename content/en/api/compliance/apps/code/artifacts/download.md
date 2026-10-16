---
title: Download Code Artifact Content
url: https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/download
---

# Download Code Artifact Content

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

## Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

## Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value. A Claude Doc downloads only this way, as a ZIP archive of Word files, one per text tab. For any other Artifact it works as on the version download: when the latest version has more than one file, it comes back as a ZIP archive of its files with an index, `files.json`.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
