---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/java/messages/batches/delete
---

# Delete a Message Batch

`DeletedMessageBatch messages().batches().delete(params = BatchDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `BatchDeleteParams params`

  - `Optional<String> messageBatchId`

    ID of the Message Batch.

  - `Optional<String> workspaceId`

## Returns

- `class DeletedMessageBatch:`

  - `JsonValue type = "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `String id`

    ID of the Message Batch.

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchDeleteParams;
import com.anthropic.models.messages.batches.DeletedMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeletedMessageBatch deletedMessageBatch = client.messages().batches().delete("message_batch_id");
    }
}
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
