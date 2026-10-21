---
title: Download Code Artifact Content
url: https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/download
---

# Download Code Artifact Content

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

## Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

## Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value. A Claude Doc downloads only this way, as a ZIP archive of Word files, one per text tab. For any other Artifact, when the latest version has more than one file, it comes back as a ZIP archive of its files with an index, `files.json`.

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
