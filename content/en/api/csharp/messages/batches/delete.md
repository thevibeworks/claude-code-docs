---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/csharp/messages/batches/delete
---

# Delete a Message Batch

`DeletedMessageBatch Messages.Batches.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `BatchDeleteParams parameters`

  - `required string messageBatchID`

    ID of the Message Batch.

  - `string workspaceID`

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class DeletedMessageBatch:`

  - `JsonElement Type = "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `required string ID`

    ID of the Message Batch.

## Example

```csharp
BatchDeleteParams parameters = new() { MessageBatchID = "message_batch_id" };

var deletedMessageBatch = await client.Messages.Batches.Delete(parameters);

Console.WriteLine(deletedMessageBatch);
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
