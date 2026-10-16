---
title: Download Code Artifact Version Content
url: https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/retrieve_version
---

# Download Code Artifact Version Content

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

## Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

## Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value, to receive a version that has more than one file as a ZIP archive of its files with an index, `files.json`. Files the artifact copied from its type (the app that displays every artifact of that type) are listed under `omitted_files` in the index, and left out of the archive, when an organization other than the artifact's owns that type. A Claude Doc's version never comes back as a ZIP: it is answered as without this parameter, except that a version with more than one file, one of them with a name the API cannot export, gets 422 `file_set_unavailable`. A version with one file is returned as that file, as without this parameter.

## Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"x-api-key": optional string`

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
