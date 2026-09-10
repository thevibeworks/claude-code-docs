---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/messages/batches/delete
---

# Delete a Message Batch

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Path parameters

- `message_batch_id: string`

  ID of the Message Batch.

## Headers

- `"anthropic-workspace-id": optional string`

## Returns

- `DeletedMessageBatch object`

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    default: message_batch_deleted

  - `id: string`

    ID of the Message Batch.

## Example

```bash
curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
