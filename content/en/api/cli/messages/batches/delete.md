---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/cli/messages/batches/delete
---

# Delete a Message Batch

`$ ant messages:batches delete`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `deleted_message_batch: object`

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `id: string`

    ID of the Message Batch.

## Example

```bash
ant messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
