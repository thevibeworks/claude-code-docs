---
title: Download Code Artifact Content
url: https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/download
---

# Download Code Artifact Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/content`

Streams an Artifact's current content as the response body, in chunks with no `Content-Length`.

For a Claude Doc (an Artifact whose `artifact_type` is `claude_docs`), the request must set `multi_file_format=zip`, and the content is the Doc's text as a ZIP archive of Word files. That ZIP has no `files.json`. It holds one Word file per text tab, in tab order, named `NN-<tab id>.docx`, where `NN` counts from `01`. A Doc with one text tab gets one file, `01-document.docx`.

For a Claude Sheet (an Artifact whose `artifact_type` is `claude_sheets`), the request must set `multi_file_format=zip` too, and the content is the Sheet's data as a ZIP archive that holds one .xlsx file, named `01-<id>.xlsx`, where `<id>` is an opaque identifier. The file has all of the Sheet's tabs and, when the Sheet has dropdowns, one more hidden tab that lists their options. It leaves out charts, conditional formatting and comments, among other things. A formula that an .xlsx file cannot hold is written as its result. If the Sheet's formulas cannot be calculated in time, every formula comes with `#VALUE!` in place of its result. That ZIP has no `files.json` either.

For any other Artifact, the download is of the latest version. With `multi_file_format=zip`, when the latest version has more than one file, it comes back as a ZIP archive of its files. Some Artifacts keep content outside their versions' files, such as data saved while people use them and files uploaded separately from a version. A single file does not include that content. A ZIP archive of a version's files includes it only if its index, `files.json`, lists it.

Headers: `Content-Type` (`application/zip` for a ZIP archive, otherwise the stored MIME type), `Content-Disposition: attachment; filename*=utf-8''<name>` (RFC 5987), `Cache-Control: no-store, private` and, when available, `Content-MD5` (base64). `<name>` is `{artifact_id}.zip` for a ZIP archive, otherwise `{artifact_id}.txt`, whatever the content is. `Content-MD5` is always on a Claude Doc's or a Claude Sheet's ZIP, only on a single file stored uncompressed, and never on a ZIP archive of a version's files. Check the body against it when present.

Errors specific to this download:

- `404`: the Artifact doesn't exist, or the API key cannot read it.
- `400` with `error.details.error_code` `cmek_key_disabled`: the organization's customer-managed encryption key can't be used, for example because it is disabled or revoked. Retry once the key can be used again.
- `503`: the content can't be produced right now. Wait the number of seconds in the `Retry-After` header, or retry with backoff when it is absent.
- `422` with `multi_file_unavailable`: the Artifact is a Claude Doc or a Claude Sheet and the request does not set `multi_file_format=zip`, or the latest version cannot be returned as a single file. Add the parameter when the error's message says to.
- `422` with `file_set_unavailable`: the request sets `multi_file_format=zip`, the Artifact is neither a Claude Doc nor a Claude Sheet, and one of the latest version's files has a path the API cannot export. Do not retry.
- `422` with `document_unavailable`: Claude Docs has no document it can export for the Doc, for example because it has no text tab or is in the trash. For a Claude Sheet, nothing can be returned as an .xlsx file, for example because the Sheet is in the trash. Retrying will not help unless that changes.
- `422` with `document_too_large`: the Doc's or the Sheet's export is over 16 MiB. Do not retry.
- `422` with `cmek_org_unsupported`: the organization uses customer-managed encryption keys and the export can't be served for it right now. Try again later, and contact Anthropic support if this continues.

An error after the download has started stops the body early, with the `200` status already sent. For example, this happens when a file stored compressed is too large once decompressed. A download that runs past a time limit stops the same way, so a large ZIP archive can end early, for example on a slow connection. For a single file with no `Content-MD5`, the only sign is a transfer that aborts before its last chunk, so treat a download that aborts this way as failed.

A ZIP archive of a version's files holds one top-level folder, named for the Artifact. That folder holds an index, `files.json`, and, under `files/`, the version's files that the archive includes. The index is written last, so treat an archive as incomplete if it cannot be opened or has no `files.json` in its top-level folder.

An archive can leave out some of the version's files, even all of them, and the response is still a `200`. Read `files` and `omitted_files` in the index to see which of them the archive holds and which it leaves out. An archive that leaves out all of them has no `files/` folder. Neither field lists content kept outside the version's files.

`files.json` includes these fields:

- `artifact_id`: the Artifact ID, as in the request.
- `version_id`: null.
- `title`: the title of the version in the archive, or that version's ID when no title is kept.
- `created_at`: when the version was published (RFC 3339, UTC), or null when that is not known.
- `files`: one entry for each file under `files/`, with `original_path` (the file's path in the version), `exported_as` (its path in the archive), `sha256` (lowercase hex), `size_bytes` (before compression) and `mime_type`. `exported_as` is the top-level folder, then `files/`, then `original_path`. A name that could not be saved or opened safely on every operating system is changed. Use `exported_as`, not `original_path`, to find a file in the archive.
- `omitted_files`: the version's files left out of the archive, each with `original_path`, `sha256`, `size_bytes` and `mime_type`. Some Artifacts are made from an Artifact type, which is itself an Artifact and holds files shared by everything made from it, such as the app that displays every Slides deck. Those shared files can be left out when an organization other than the Artifact's owns the type, as Anthropic does for its built-in types, or when the type has access rules the API does not recognize. Any other file the version points to in another Artifact can also be left out.

`files` and `omitted_files` together list at most 4,096 files, none over 32 MiB, and the `size_bytes` of the files in `files` add up to at most 1 GiB.

## Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

## Query parameters

- `multi_file_format: optional string`

  Set to `zip`, its only value. A Claude Doc downloads only this way, as a ZIP archive of Word files, one per text tab. So does a Claude Sheet, as a ZIP archive that holds one .xlsx file. For any other Artifact, when the latest version has more than one file, it comes back as a ZIP archive of its files with an index, `files.json`. Otherwise the latest version can still come back as a single file, so check whether the file name in `Content-Disposition` ends in `.zip`.

## Headers

- `"anthropic-version": string`

  The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

  See [API versions](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http) for the available versions.

- `"x-api-key": optional string`

## Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/content \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```
