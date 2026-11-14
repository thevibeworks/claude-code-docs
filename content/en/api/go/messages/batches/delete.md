---
title: Delete a Message Batch
url: https://platform.claude.com/docs/en/api/go/messages/batches/delete
---

# Delete a Message Batch

`client.Messages.Batches.Delete(ctx, messageBatchID, body) (*DeletedMessageBatch, error)`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=go)

## Parameters

- `messageBatchID string` (path parameter)

  ID of the Message Batch.

- `body MessageBatchDeleteParams`

  - `WorkspaceID param.Opt[string] Optional` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `type DeletedMessageBatch`

  - `Type MessageBatchDeleted`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

    default: message_batch_deleted

  - `ID string`

    ID of the Message Batch.

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=go).

- `ErrorCodeClaudeCodeKeyCreatorNotMember` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `ErrorCodeOrganizationOnHold` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go/v2"
	"github.com/anthropics/anthropic-sdk-go/v2/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	deletedMessageBatch, err := client.Messages.Batches.Delete(
		context.TODO(),
		"message_batch_id",
		anthropic.MessageBatchDeleteParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", deletedMessageBatch.ID)
}
```

### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
