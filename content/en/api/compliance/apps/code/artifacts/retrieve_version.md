---
title: Download Code Artifact Version Content
url: https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/retrieve_version
---

# Download Code Artifact Version Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}`

Streams the content of one version of an Artifact as the response body, in chunks with no `Content-Length`. With `multi_file_format=zip`, a version with more than one file, other than a Claude Doc's or a Claude Sheet's (an Artifact whose `artifact_type` is `claude_docs` or `claude_sheets`), comes back as a ZIP archive of its files.

Some Artifacts keep content outside their versions' files, such as data saved while people use them and files uploaded separately from a version. A download of a version does not include that content, and a ZIP archive's index, `files.json`, does not list it.

Headers: `Content-Type` (`application/zip` for a ZIP archive, otherwise the stored MIME type), `Content-Disposition: attachment; filename*=utf-8''<name>` (RFC 5987), `Cache-Control: no-store, private` and, when available, `Content-MD5` (base64). `<name>` is `{artifact_id}-{version_id}.zip` for a ZIP archive, otherwise `{artifact_id}-{version_id}.txt`, whatever the content is. `Content-MD5` is only on a single file stored uncompressed, so it is never on a ZIP archive. Check the body against it when present.

Errors specific to this download:

- `404`: the Artifact doesn't exist or the API key cannot read it, or the version is no longer kept. Older versions are dropped as new ones are published, so list the Artifact's versions again. You also get this when the organization's customer-managed encryption key can't be used. Retry once the key can be used again.
- `503`: the content can't be served right now, for example because its upload is still in progress or was abandoned. Retry with backoff.
- `422` with `error.details.error_code` `multi_file_unavailable`: the version cannot be returned as a single file, for example because it has more than one file. Add `multi_file_format=zip` when the error's message says to. A Claude Doc's or a Claude Sheet's version with more than one file gets this error with or without `multi_file_format=zip`, because it holds only the web page that displays the Doc or the Sheet. Download the Doc's text or the Sheet's data with `GET /v1/compliance/apps/code/artifacts/{artifact_id}/content?multi_file_format=zip`.
- `422` with `file_set_unavailable`: the request sets `multi_file_format=zip`, the version has more than one file, and one of them has a path the API cannot export. Do not retry.

An error after the download has started stops the body early, with the `200` status already sent. For example, this happens when a file stored compressed is too large once decompressed. A download that runs past a time limit stops the same way, so a large ZIP archive can end early, for example on a slow connection. For a single file with no `Content-MD5`, the only sign is a transfer that aborts before its last chunk, so treat a download that aborts this way as failed.

A ZIP archive of a version's files holds one top-level folder, named for the Artifact and version. That folder holds an index, `files.json`, and, under `files/`, the version's files that the archive includes. The index is written last, so treat an archive as incomplete if it cannot be opened or has no `files.json` in its top-level folder.

An archive can leave out some of the version's files, even all of them, and the response is still a `200`. Read `files` and `omitted_files` in the index to see which of them the archive holds and which it leaves out. An archive that leaves out all of them has no `files/` folder. Neither field lists content kept outside the version's files.

`files.json` includes these fields:

- `artifact_id`: the Artifact ID, as in the request.
- `version_id`: the version ID, as in the request.
- `title`: the title of the version in the archive, or that version's ID when no title is kept.
- `created_at`: when the version was published (RFC 3339, UTC), or null when that is not known.
- `files`: one entry for each file under `files/`, with `original_path` (the file's path in the version), `exported_as` (its path in the archive), `sha256` (lowercase hex), `size_bytes` (before compression) and `mime_type`. `exported_as` is the top-level folder, then `files/`, then `original_path`. A name that could not be saved or opened safely on every operating system is changed. Use `exported_as`, not `original_path`, to find a file in the archive.
- `omitted_files`: the version's files left out of the archive, each with `original_path`, `sha256`, `size_bytes` and `mime_type`. Some Artifacts are made from an Artifact type, which is itself an Artifact and holds files shared by everything made from it, such as the app that displays every Slides deck. Those shared files can be left out when an organization other than the Artifact's owns the type, as Anthropic does for its built-in types, or when the type has access rules the API does not recognize. Any other file the version points to in another Artifact can also be left out.

`files` and `omitted_files` together list at most 4,096 files, none over 32 MiB, and the `size_bytes` of the files in `files` add up to at most 1 GiB.

## Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

## Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value, to ask for a ZIP archive with an index, `files.json`, when a version cannot be returned as a single file, such as when it has more than one file. Any other version can still come back as a single file, so check whether the file name in `Content-Disposition` ends in `.zip`. A Claude Doc's or a Claude Sheet's version never comes back as a ZIP.

## Headers

- `"anthropic-version": string`

  The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

  See [API versions](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http) for the available versions.

- `"x-api-key": optional string`

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
