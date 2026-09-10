---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/python/messages/batches/delete
---

# Delete a Message Batch

`messages.batches.delete(message_batch_id, **kwargs)  -> DeletedMessageBatch`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `message_batch_id: str`

  ID of the Message Batch.

- `workspace_id: Optional[str]`

## Returns

- `class DeletedMessageBatch: …`

  - `type: Literal["message_batch_deleted"]`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    default: message_batch_deleted

  - `id: str`

    ID of the Message Batch.

## Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
deleted_message_batch = client.messages.batches.delete(
    message_batch_id="message_batch_id",
)
print(deleted_message_batch.id)
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
