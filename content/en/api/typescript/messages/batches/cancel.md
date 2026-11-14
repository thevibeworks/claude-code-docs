---
title: Cancel a Message Batch
url: https://platform.claude.com/docs/en/api/typescript/messages/batches/cancel
---

# Cancel a Message Batch

- Signature: `client.messages.batches.cancel(messageBatchID: string, params?: BatchCancelParams, options?: RequestOptions): MessageBatch`
- Endpoint: `POST /v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.cancel("message_batch_id");

console.log(messageBatch.id);
```

## Example response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchCancelParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
interface MessageBatch {
  /** Object type. For Message Batches, this is always `"message_batch"`. */
  type: "message_batch";
  /** Unique object identifier. The format and length of IDs may change over time. */
  id: string;
  /** RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable. */
  archived_at: string | null; // format: date-time
  /** RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated. */
  cancel_initiated_at: string | null; // format: date-time
  /** RFC 3339 datetime string representing the time at which the Message Batch was created. */
  created_at: string; // format: date-time
  /** RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends. Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired. */
  ended_at: string | null; // format: date-time
  /** RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation. */
  expires_at: string; // format: date-time
  /** Processing status of the Message Batch. */
  processing_status: "in_progress" | "canceling" | "ended";
  /** Tallies requests within the Message Batch, categorized by their status. Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch. */
  request_counts: MessageBatchRequestCounts;
  /** URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends. Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests. */
  results_url: string | null;
}
```

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Types

```ts
interface MessageBatchRequestCounts {
  /** Number of requests in the Message Batch that have been canceled. This is zero until processing of the entire Message Batch has ended. */
  canceled: number; // default: 0
  /** Number of requests in the Message Batch that encountered an error. This is zero until processing of the entire Message Batch has ended. */
  errored: number; // default: 0
  /** Number of requests in the Message Batch that have expired. This is zero until processing of the entire Message Batch has ended. */
  expired: number; // default: 0
  /** Number of requests in the Message Batch that are processing. */
  processing: number; // default: 0
  /** Number of requests in the Message Batch that have completed successfully. This is zero until processing of the entire Message Batch has ended. */
  succeeded: number; // default: 0
}
```
