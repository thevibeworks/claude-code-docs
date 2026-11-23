---
title: Safety Case files
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files
description: The files that Anthropic writes to your Case bucket and the response file that your team writes back.
---

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

This page describes the Safety Case and Transcript files in your [Case bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) and the format of each. You select that bucket under **Safety Case and Transcript storage**. To set up that bucket, see [Set up customer-owned storage](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage). To learn how your team reviews and responds to a Safety Case, see [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases).

A Safety Case asks your team to investigate a set of messages. It works like this:

1. Anthropic writes the Safety Case to your bucket as a JSON file, with a Transcript file for each message that Anthropic has a copy of.
2. Your team investigates and writes a response file to the same bucket.
3. Anthropic closes the Safety Case.

Anthropic can also write Safety Notices about your Safety Cases.

Some details depend on your storage provider:

* **Amazon S3:** The paths, permissions, and expiry settings on this page are for Amazon S3.
* **Google Cloud Storage:** In a bucket connected in the Claude Console, each path starts with a folder named after your Anthropic organization ID (see [Use your Cloud Storage bucket in a workspace](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#gcs-use-your-bucket-in-a-workspace)).

## What’s in the bucket

| Prefix | What it holds | Who needs it | Expires after |
| ----- | ----- | ----- | ----- |
| `review-cases/` | One [Safety Case file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#safety-case-file) for each Safety Case | Triage and reviewers, to read | 2,555 days (about 7 years) by default |
| `review-notices/` | The [Safety Notices](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#notice) that Anthropic writes as files, one file each | Triage and reviewers, to read | 2,555 days by default |
| `transcripts/flagged/` | A [Transcript](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#transcript) of each message in a Safety Case | Reviewers, to read | Up to 30 days |
| `review-responses/` | Your [response file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#response-file) for each Safety Case | Reviewers, to write | 2,555 days by default |

Anthropic recommends splitting access by prefix, so that the people who triage alerts don’t see prompts and responses. Each role needs these permissions:

* **To read:** A person needs `s3:GetObject` on the prefix, `s3:ListBucket` on the bucket, and `kms:Decrypt` on the bucket’s key. Limit `s3:ListBucket` to the prefix with an `s3:prefix` condition. The rest of `transcripts/` can hold requests that don’t lead to a Safety Case.
* **To write responses:** A reviewer also needs `s3:PutObject` on `review-responses/*` and `kms:GenerateDataKey` on the key.

To keep Safety Cases, Safety Notices, or responses for longer than the default, set `ReviewExpiryDays` (CloudFormation) or `review_expiry_days` (Terraform) when you deploy the [setup file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage#template-reference). After one of these files expires or is replaced or deleted, it stays as a noncurrent version for up to that number of days.

Don’t edit the bucket’s lifecycle rules directly. A bucket that lacks a required rule, or adds an expiry rule, fails **Test setup** or a later check. Transcripts expire after up to 30 days, so copy any that you need for longer to other storage.

## Alerts for new files

Set up an alert for each new Safety Case file and Safety Notice file, so that your team can respond promptly.

### Amazon S3

There are two ways to get alerts without changing the bucket:

* **List on a schedule.** Run a recurring job that lists `review-cases/` and `review-notices/` with `ListObjectsV2`. Have it compare each list with the previous run’s list, and alert on each new object.
* **Match writes in AWS CloudTrail.** [Turn on CloudTrail data events](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/external-storage-manage#cloudtrail) for the two prefixes, and match `PutObject` and `CompleteMultipartUpload` in an Amazon EventBridge rule.

Anthropic doesn’t recommend changing the bucket’s own notification settings to get alerts. The setup file asks you not to edit the bucket’s configuration after you deploy it, except to set `ReviewExpiryDays`.

Anthropic can overwrite a Safety Case file, for example when the Safety Case closes, so an Amazon EventBridge rule can match the same file more than once. Read `status` in the file.

### Google Cloud Storage

In a Google Cloud Storage bucket, `review-cases/` and `review-notices/` are inside a folder named after your Anthropic organization ID. List `<organization ID>/review-cases/` and `<organization ID>/review-notices/` on a schedule with the JSON API’s `Objects: list` method, and alert on each new object.

## Safety Case file

When Anthropic sends you a new Safety Case, it writes it to `review-cases/<id>.json` in the following format:

```json
{
  "schema_version": 1,
  "id": "rvc_01Hq3Zt8KpWv5NcR2yLbXs7D",
  "status": { "type": "open" },
  "created_at": "2026-11-23T18:42:07Z",
  "updated_at": "2026-11-23T18:42:07Z",
  "workspace_id": "wrkspc_01AbCdEfGhJkLmNpQrStUvWx",
  "policy_categories": ["cyber"],
  "enforcement_action": null,
  "transcripts": [
    {
      "item_id": "msg_01XFDUDYJgAACzvnptvVoYEL",
      "object_key": "transcripts/flagged/4da8b33b-8235-3151-ffb5-1e5cc2230505/MESSAGE_SOURCE_PUBLIC_API_SAMPLING_CALL-msg_01XFDUDYJgAACzvnptvVoYEL.json"
    }
  ],
  "derived_data_object_keys": []
}
```

| Field | What it holds |
| ----- | ----- |
| `schema_version` | The format’s version. A later version can add fields. |
| `id` | The Safety Case’s ID, which starts with `rvc_`. It names this file and your response file, and the [Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api) uses the same ID. |
| `status.type` | `open` or `closed` |
| `status.reason` | Only in a closed file. `null` if Anthropic gave no reason. Otherwise, an object whose `type` says why the Safety Case closed. The next table lists the values. |
| `created_at` | When Anthropic sent the Safety Case, in UTC. The 7 calendar days to respond count from this time. |
| `updated_at` | When Anthropic last updated this file, in UTC |
| `workspace_id` | The ID of the workspace that sent the messages, or `null` if the messages name no workspace. The ID starts with `wrkspc_`. |
| `policy_categories` | The kind of risk that automated safety monitoring found, such as `cyber` or `bio`. Anthropic can add values, so route the ones you don’t know to your default queue. |
| `enforcement_action` | An object whose `type` names an action that Anthropic took before it sent the Safety Case, or `null`. Alert on any value other than `null`. |
| `transcripts[].item_id` | A message’s ID: the `id` of the Messages API response |
| `transcripts[].user_profile_id` | The user profile that sent the message. Anthropic can leave the key out, even if you sent a user profile. |
| `transcripts[].object_key` | Where the message’s Transcript is in your bucket, or `null` if Anthropic kept no copy. The object can also be absent. The key’s folder is the workspace’s UUID (not its `wrkspc_` ID), or `default` if the messages name no workspace. |
| `derived_data_object_keys` | The object keys of any extra files that Anthropic adds about the Safety Case. An empty list if there are none. |

`status.reason.type` has these values:

| `status.reason.type` | What it means |
| ----- | ----- |
| `responded` | Anthropic has your response. |
| `window_ended` | No valid response within 7 calendar days of `created_at`. |
| `ended_by_anthropic` | Anthropic ended the Safety Case before the 7 calendar days ended. |

Anthropic can add values.

Don’t move or edit this file, and don’t delete it while its `status.type` is `open`. Anthropic updates it in place, for example when the Safety Case closes. If Anthropic can’t find a valid file, it doesn’t write a closed one.

## Transcript

A Transcript is a readable copy of one message: your prompt and Claude’s response. The Safety Case file gives each Transcript’s location in `object_key`. Each Transcript is a JSON object with these fields:

| Field | What it holds |
| ----- | ----- |
| `id` | The message ID |
| `request`, `response` | The message, in the Messages API’s format. `request` includes the [`metadata`](https://platform.claude.com/docs/en/api/messages/create#create.metadata) parameter that you sent, which holds `user_id`. `response` can be `null`. |
| `request_time` | When Anthropic recorded the message |
| `organization_uuid`, `workspace_uuid` | The organization and workspace that sent it. `workspace_uuid` is the workspace’s UUID, not its `wrkspc_` ID, and it’s `null` if the message names no workspace. |
| `source` | Where the message came from |
| `schema_version` | The format’s version |

A Transcript isn’t an exact copy of the message. Anthropic redacts MCP server tokens and removes thinking blocks, and an image or a document can appear as a placeholder.

## Safety Notice

A Safety Notice is a message from Anthropic about one or more of your Safety Cases, or about your organization as a whole. It can be a request to respond, a warning, or a question. Anthropic doesn’t write every Safety Notice as a file, but the Safety Cases API lists them all (see [Poll for Safety Notices](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#poll-for-notices)). A Safety Notice file is at `review-notices/<id>.json`, and Anthropic never changes it:

```json
{
  "schema_version": 1,
  "id": "rvn_01Jt5Yw2MnQx8VbK4zRcHd6F",
  "case_ids": ["rvc_01Hq3Zt8KpWv5NcR2yLbXs7D"],
  "kind": { "type": "response_requested" },
  "created_at": "2026-11-27T18:00:00Z",
  "message": "Anthropic has found no valid response to the Case in case_ids. Review the Case and write your response file before the time in respond_by. If you wrote a valid response file in the last hour, ignore this notice.",
  "respond_by": "2026-11-30T18:42:07Z"
}
```

| Field | What it holds |
| ----- | ----- |
| `id` | The Safety Notice’s ID, which starts with `rvn_`. It names this file. |
| `case_ids` | The `id` of each Safety Case that the Safety Notice is about. An empty list means your organization as a whole. |
| `kind.type` | `response_requested`, `warning`, or `question` |
| `message` | The text of the request, warning, or question, up to 2,000 characters. It never quotes a Transcript. |
| `respond_by` | When Anthropic asks for an answer, or `null`. It doesn’t extend the 7 calendar days to respond to a Safety Case. |

To answer `response_requested`, write your response file. To answer a question, contact your Anthropic account team.

## Response file

A response file tells Anthropic that your team investigated a Safety Case, and what it found. It’s how you respond to a Safety Case without the [Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api). Write it to `review-responses/<case_id>.json`, or `<organization ID>/review-responses/<case_id>.json` in Google Cloud Storage:

```json
{
  "schema_version": 1,
  "case_id": "rvc_01Hq3Zt8KpWv5NcR2yLbXs7D",
  "submitted_at": "2026-11-25T16:02:10Z",
  "determination": "violation",
  "policy_categories": ["cyber"],
  "verdicts": [
    {
      "item_id": "msg_01XFDUDYJgAACzvnptvVoYEL",
      "determination": "violation",
      "policy_category": "cyber"
    }
  ]
}
```

| Field | What to send |
| ----- | ----- |
| `schema_version` | The schema version of your response. The only accepted value is the number `1`. |
| `case_id` | The Safety Case’s `id`, the same as in the file’s name |
| `submitted_at` | The time you respond, as an ISO 8601 time with an offset, such as `Z` |
| `determination` | `violation` or `no_violation`, for the Safety Case as a whole |
| `policy_categories` | With `violation`, one to four categories that you confirmed. Use values from the Safety Case’s own `policy_categories`, or `other` if none fits. With `no_violation`, leave it out or send an empty list. |
| `verdicts` | Optional, and never `null`. To judge messages separately, give a list with one entry for each message that you judge. Each entry has an `item_id`, a `determination`, and, with `violation`, an optional `policy_category`. The list doesn’t have to cover every message. |

### Rules for a valid file

Anthropic doesn’t tell you when a file is invalid, so check yours against these rules:

* It’s at `review-responses/<case_id>.json` (in Google Cloud Storage, `<organization ID>/review-responses/<case_id>.json`), with the same ID as its `case_id` field. Use the Safety Case’s `id`, which starts with `rvc_`.
* It has the `schema_version`, `case_id`, `submitted_at`, and `determination` fields, and no field that isn’t in the table.
* `policy_categories` has one to four values with `violation` and none with `no_violation`, and no value appears twice. No `item_id` appears twice in `verdicts`.
* Every category is a value that a Safety Case can hold, such as `cyber` or `other`.
* Every `item_id` in `verdicts` is in the Safety Case.
* It’s plain JSON of at most 256 kB, with no byte order mark and no key twice. Windows PowerShell 5.1 adds a byte order mark, which makes the file invalid, so Anthropic treats it as no response.
* It uses your bucket’s default encryption.

Anthropic counts the first valid response that it reads, and you can’t change it after that. Until then, you can replace the file.

Before you change or remove a workspace’s [safety data bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) or Case bucket, respond to its open Safety Cases and wait until they close. If you change or remove the bucket first, Anthropic might not read your response file.

### Why a Safety Case stays open

Anthropic checks `review-responses/` on a schedule, so allow a day. A valid file that you write within the 7 calendar days counts, even if Anthropic reads it later. If `status.type` is still `open` a day after you wrote the file, check your file against [Rules for a valid file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#response-file-rules) and replace it.

When Anthropic reads a valid response, it rewrites the Safety Case file with `status.type` set to `closed`. Read `status.reason` in that file:

* **`status.reason.type` is `responded`:** This confirms that Anthropic has received your response.
* **`status.reason` is `null`:** This can happen even if Anthropic has your response. On Claude Platform, read the Safety Case through the [Safety Cases API](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api), which always gives a reason.

A closed Safety Case doesn’t reopen, and Anthropic ignores a response file written after it closes.
