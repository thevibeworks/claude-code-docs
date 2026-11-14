---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/typescript/messages/batches/delete
---

# Delete a Message Batch

- Signature: `client.messages.batches.delete(messageBatchID: string, params?: BatchDeleteParams, options?: RequestOptions): DeletedMessageBatch`
- Endpoint: `DELETE /v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const deletedMessageBatch = await client.messages.batches.delete("message_batch_id");

console.log(deletedMessageBatch.id);
```

## Example response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchDeleteParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
interface DeletedMessageBatch {
  /** Deleted object type. For Message Batches, this is always `"message_batch_deleted"`. */
  type: "message_batch_deleted";
  /** ID of the Message Batch. */
  id: string;
}
```

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.
