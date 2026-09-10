---
title: Batches
url: https://platform.claude.com/docs/en/api/cli/messages/batches
---

# Batches

## Create a Message Batch

`$ ant messages:batches create`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `--request: array of object`

  Body param: List of requests for prompt completion. Each is an individual request to create a Message.

  maxItems: 100000, minItems: 1

- `--user-profile-id: optional string`

  Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `message_batch: object`

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

### Example

```bash
ant messages:batches create \
  --api-key my-anthropic-api-key \
  --request '{custom_id: my-custom-id-1, params: {max_tokens: 1024, messages: [{content: [{text: x, type: text}], role: user}], model: claude-opus-5}}'
```

#### Response (200)

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

## Retrieve a Message Batch

`$ ant messages:batches retrieve`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `message_batch: object`

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

### Example

```bash
ant messages:batches retrieve \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

#### Response (200)

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

## List Message Batches

`$ ant messages:batches list`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `--workspace-id: optional string`

  Header param: Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `ListResponse_MessageBatch_: object`

  - `data: array of MessageBatch`

    - `type: "message_batch"`

      Object type.

      For Message Batches, this is always `"message_batch"`.

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `archived_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

      format: date-time

    - `cancel_initiated_at: string`

      RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

      format: date-time

    - `created_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was created.

      format: date-time

    - `ended_at: string`

      RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

      Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

      format: date-time

    - `expires_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

      format: date-time

    - `processing_status: "in_progress" or "canceling" or "ended"`

      Processing status of the Message Batch.

      - `"in_progress"`

      - `"canceling"`

      - `"ended"`

    - `request_counts: object`

      Tallies requests within the Message Batch, categorized by their status.

      Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

      - `canceled: number`

        Number of requests in the Message Batch that have been canceled.

        This is zero until processing of the entire Message Batch has ended.

      - `errored: number`

        Number of requests in the Message Batch that encountered an error.

        This is zero until processing of the entire Message Batch has ended.

      - `expired: number`

        Number of requests in the Message Batch that have expired.

        This is zero until processing of the entire Message Batch has ended.

      - `processing: number`

        Number of requests in the Message Batch that are processing.

      - `succeeded: number`

        Number of requests in the Message Batch that have completed successfully.

        This is zero until processing of the entire Message Batch has ended.

    - `results_url: string`

      URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

      Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

### Example

```bash
ant messages:batches list \
  --api-key my-anthropic-api-key
```

#### Response (200)

```json
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

## Cancel a Message Batch

`$ ant messages:batches cancel`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `message_batch: object`

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

### Example

```bash
ant messages:batches cancel \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

#### Response (200)

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

## Delete a Message Batch

`$ ant messages:batches delete`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `deleted_message_batch: object`

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `id: string`

    ID of the Message Batch.

### Example

```bash
ant messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

#### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

## Retrieve Message Batch results

`$ ant messages:batches results`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `message_batch_individual_response: object`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: MessageBatchSucceededResult or MessageBatchErroredResult or MessageBatchCanceledResult or MessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `message_batch_succeeded_result: object`

      - `type: "succeeded"`

      - `message: object`

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: object`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

            format: date-time

          - `skills: array of ContainerSkill`

            Skills loaded in the container

            - `type: "anthropic" or "custom"`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `"anthropic"`

              - `"custom"`

            - `skill_id: string`

              Skill ID

              maxLength: 64, minLength: 1

            - `version: string`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

        - `content: array of ContentBlock`

          Content generated by the model.

          This is an array of content blocks, each of which has a `type` that determines its shape.

          Example:

          ```json
          [{"type": "text", "text": "Hi, I'm Claude."}]
          ```

          If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

          For example, if the input `messages` were:

          ```json
          [
            {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
            {"role": "assistant", "content": "The best answer is ("}
          ]
          ```

          Then the response `content` might be:

          ```json
          [{"type": "text", "text": "B)"}]
          ```

          - `text_block: object`

            - `type: "text"`

            - `citations: array of TextCitation`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `citation_char_location: object`

                - `type: "char_location"`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                - `end_char_index: number`

                - `file_id: string`

                - `start_char_index: number`

                  minimum: 0

              - `citation_page_location: object`

                - `type: "page_location"`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                - `end_page_number: number`

                - `file_id: string`

                - `start_page_number: number`

                  minimum: 1

              - `citation_content_block_location: object`

                - `type: "content_block_location"`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `file_id: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

              - `citations_web_search_result_location: object`

                - `type: "web_search_result_location"`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                  maxLength: 512

                - `url: string`

              - `citations_search_result_location: object`

                - `type: "search_result_location"`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `search_result_index: number`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `source: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `title: string`

            - `text: string`

              minLength: 0

          - `thinking_block: object`

            - `type: "thinking"`

            - `signature: string`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `thinking: string`

              The text of Claude's thinking process for this block.

          - `redacted_thinking_block: object`

            - `type: "redacted_thinking"`

            - `data: string`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `tool_use_block: object`

            - `type: "tool_use"`

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

                - `type: "code_execution_20250825"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `server_tool_caller_20260120: object`

                - `type: "code_execution_20260120"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `input: map[unknown]`

            - `name: string`

              minLength: 1

            - `toolset_name: optional string`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `server_tool_use_block: object`

            - `type: "server_tool_use"`

            - `id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

              - `server_tool_caller_20260120: object`

            - `input: map[unknown]`

            - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

          - `web_search_tool_result_block: object`

            - `type: "web_search_tool_result"`

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

              - `server_tool_caller_20260120: object`

            - `content: WebSearchToolResultError or array of WebSearchResultBlock`

              - `web_search_tool_result_error: object`

                - `type: "web_search_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

              - `union_member_1: array of WebSearchResultBlock`

                - `type: "web_search_result"`

                - `encrypted_content: string`

                - `page_age: string`

                - `title: string`

                - `url: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `web_fetch_tool_result_block: object`

            - `type: "web_fetch_tool_result"`

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

              - `server_tool_caller_20260120: object`

            - `content: WebFetchToolResultErrorBlock or WebFetchBlock`

              - `web_fetch_tool_result_error_block: object`

                - `type: "web_fetch_tool_result_error"`

                - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 7 more`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_in_prior_context"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                  - `"content_too_large"`

              - `web_fetch_block: object`

                - `type: "web_fetch_result"`

                - `content: object`

                  - `type: "document"`

                  - `citations: object`

                    Citation configuration for the document

                    - `enabled: boolean`

                  - `source: Base64PDFSource or PlainTextSource`

                    - `base64_pdf_source: object`

                      - `type: "base64"`

                      - `data: string`

                        format: byte

                      - `media_type: "application/pdf"`

                    - `plain_text_source: object`

                      - `type: "text"`

                      - `data: string`

                      - `media_type: "text/plain"`

                  - `title: string`

                    The title of the document

                - `retrieved_at: string`

                  ISO 8601 timestamp when the content was retrieved

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `code_execution_tool_result_block: object`

            - `type: "code_execution_tool_result"`

            - `content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `code_execution_tool_result_error: object`

                - `type: "code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

              - `code_execution_result_block: object`

                - `type: "code_execution_result"`

                - `content: array of CodeExecutionOutputBlock`

                  - `type: "code_execution_output"`

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

              - `encrypted_code_execution_result_block: object`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type: "encrypted_code_execution_result"`

                - `content: array of CodeExecutionOutputBlock`

                  - `type: "code_execution_output"`

                  - `file_id: string`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `bash_code_execution_tool_result_block: object`

            - `type: "bash_code_execution_tool_result"`

            - `content: BashCodeExecutionToolResultError or BashCodeExecutionResultBlock`

              - `bash_code_execution_tool_result_error: object`

                - `type: "bash_code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

              - `bash_code_execution_result_block: object`

                - `type: "bash_code_execution_result"`

                - `content: array of BashCodeExecutionOutputBlock`

                  - `type: "bash_code_execution_output"`

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `text_editor_code_execution_tool_result_block: object`

            - `type: "text_editor_code_execution_tool_result"`

            - `content: TextEditorCodeExecutionToolResultError or TextEditorCodeExecutionViewResultBlock or TextEditorCodeExecutionCreateResultBlock or TextEditorCodeExecutionStrReplaceResultBlock`

              - `text_editor_code_execution_tool_result_error: object`

                - `type: "text_editor_code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string`

              - `text_editor_code_execution_view_result_block: object`

                - `type: "text_editor_code_execution_view_result"`

                - `content: string`

                - `file_type: "text" or "image" or "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number`

                - `start_line: number`

                - `total_lines: number`

              - `text_editor_code_execution_create_result_block: object`

                - `type: "text_editor_code_execution_create_result"`

                - `is_file_update: boolean`

              - `text_editor_code_execution_str_replace_result_block: object`

                - `type: "text_editor_code_execution_str_replace_result"`

                - `lines: array of string`

                - `new_lines: number`

                - `new_start: number`

                - `old_lines: number`

                - `old_start: number`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `tool_search_tool_result_block: object`

            - `type: "tool_search_tool_result"`

            - `content: ToolSearchToolResultError or ToolSearchToolSearchResultBlock`

              - `tool_search_tool_result_error: object`

                - `type: "tool_search_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string`

              - `tool_search_tool_search_result_block: object`

                - `type: "tool_search_tool_search_result"`

                - `tool_references: array of ToolReferenceBlock`

                  - `type: "tool_reference"`

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `container_upload_block: object`

            Response model for a file uploaded to the container.

            - `type: "container_upload"`

            - `file_id: string`

        - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-mythos-5-1"`

            Our most capable model for cybersecurity and biology research, available through trusted access programs

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-mythos-5"`

            Most capable model for cybersecurity and biology research

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-mythos-preview"`

            New class of intelligence, strongest in coding and cybersecurity

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `stop_details: object`

          Structured information about a refusal.

          - `type: "refusal"`

          - `category: "cyber" or "bio" or "frontier_llm" or 2 more`

            The policy category that triggered a refusal.

            - `"cyber"`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `"bio"`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `"frontier_llm"`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `"reasoning_extraction"`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `"general_harms"`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `explanation: string`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

        - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
          * `"model_context_window_exceeded"`: we exceeded the model's context window

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"`

          - `"max_tokens"`

          - `"stop_sequence"`

          - `"tool_use"`

          - `"pause_turn"`

          - `"refusal"`

          - `"model_context_window_exceeded"`

        - `stop_sequence: string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `usage: object`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: object`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

            minimum: 0

          - `inference_geo: string`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

            minimum: 0

          - `output_tokens: number`

            The number of output tokens which were used.

            minimum: 0

          - `output_tokens_details: object`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `thinking_tokens: number`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `server_tool_use: object`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

              minimum: 0

            - `web_search_requests: number`

              The number of web search tool requests.

              minimum: 0

          - `service_tier: "standard" or "priority" or "batch"`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

    - `message_batch_errored_result: object`

      - `type: "errored"`

      - `error: object`

        - `type: "error"`

        - `error: InvalidRequestError or AuthenticationError or BillingError or 6 more`

          - `invalid_request_error: object`

            - `type: "invalid_request_error"`

            - `message: string`

          - `authentication_error: object`

            - `type: "authentication_error"`

            - `message: string`

          - `billing_error: object`

            - `type: "billing_error"`

            - `message: string`

          - `permission_error: object`

            - `type: "permission_error"`

            - `message: string`

          - `not_found_error: object`

            - `type: "not_found_error"`

            - `message: string`

          - `rate_limit_error: object`

            - `type: "rate_limit_error"`

            - `message: string`

          - `gateway_timeout_error: object`

            - `type: "timeout_error"`

            - `message: string`

          - `api_error_object: object`

            - `type: "api_error"`

            - `message: string`

          - `overloaded_error: object`

            - `type: "overloaded_error"`

            - `message: string`

        - `request_id: string`

    - `message_batch_canceled_result: object`

      - `type: "canceled"`

    - `message_batch_expired_result: object`

      - `type: "expired"`

### Example

```bash
ant messages:batches results \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

## Domain types

### Deleted Message Batch

- `deleted_message_batch: object`

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `id: string`

    ID of the Message Batch.

### Message Batch

- `message_batch: object`

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

### Message Batch Canceled Result

- `message_batch_canceled_result: object`

  - `type: "canceled"`

### Message Batch Errored Result

- `message_batch_errored_result: object`

  - `type: "errored"`

  - `error: object`

    - `type: "error"`

    - `error: InvalidRequestError or AuthenticationError or BillingError or 6 more`

      - `invalid_request_error: object`

        - `type: "invalid_request_error"`

        - `message: string`

      - `authentication_error: object`

        - `type: "authentication_error"`

        - `message: string`

      - `billing_error: object`

        - `type: "billing_error"`

        - `message: string`

      - `permission_error: object`

        - `type: "permission_error"`

        - `message: string`

      - `not_found_error: object`

        - `type: "not_found_error"`

        - `message: string`

      - `rate_limit_error: object`

        - `type: "rate_limit_error"`

        - `message: string`

      - `gateway_timeout_error: object`

        - `type: "timeout_error"`

        - `message: string`

      - `api_error_object: object`

        - `type: "api_error"`

        - `message: string`

      - `overloaded_error: object`

        - `type: "overloaded_error"`

        - `message: string`

    - `request_id: string`

### Message Batch Expired Result

- `message_batch_expired_result: object`

  - `type: "expired"`

### Message Batch Individual Response

- `message_batch_individual_response: object`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: MessageBatchSucceededResult or MessageBatchErroredResult or MessageBatchCanceledResult or MessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `message_batch_succeeded_result: object`

      - `type: "succeeded"`

      - `message: object`

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `id: string`

          Unique object identifier.

          The format and length of IDs may change over time.

        - `container: object`

          Information about the container used in the request (for the code execution tool)

          - `id: string`

            Identifier for the container used in this request

          - `expires_at: string`

            The time at which the container will expire.

            format: date-time

          - `skills: array of ContainerSkill`

            Skills loaded in the container

            - `type: "anthropic" or "custom"`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `"anthropic"`

              - `"custom"`

            - `skill_id: string`

              Skill ID

              maxLength: 64, minLength: 1

            - `version: string`

              The resolved version: a skill version ID for custom skills.

              maxLength: 64, minLength: 1

        - `content: array of ContentBlock`

          Content generated by the model.

          This is an array of content blocks, each of which has a `type` that determines its shape.

          Example:

          ```json
          [{"type": "text", "text": "Hi, I'm Claude."}]
          ```

          If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

          For example, if the input `messages` were:

          ```json
          [
            {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
            {"role": "assistant", "content": "The best answer is ("}
          ]
          ```

          Then the response `content` might be:

          ```json
          [{"type": "text", "text": "B)"}]
          ```

          - `text_block: object`

            - `type: "text"`

            - `citations: array of TextCitation`

              Citations supporting the text block.

              The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

              - `citation_char_location: object`

                - `type: "char_location"`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                - `end_char_index: number`

                - `file_id: string`

                - `start_char_index: number`

                  minimum: 0

              - `citation_page_location: object`

                - `type: "page_location"`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                - `end_page_number: number`

                - `file_id: string`

                - `start_page_number: number`

                  minimum: 1

              - `citation_content_block_location: object`

                - `type: "content_block_location"`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `file_id: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

              - `citations_web_search_result_location: object`

                - `type: "web_search_result_location"`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                  maxLength: 512

                - `url: string`

              - `citations_search_result_location: object`

                - `type: "search_result_location"`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `search_result_index: number`

                  0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                  Counted separately from `document_index`; server-side web search results are not included in this count.

                  minimum: 0

                - `source: string`

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `title: string`

            - `text: string`

              minLength: 0

          - `thinking_block: object`

            - `type: "thinking"`

            - `signature: string`

              A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

              This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            - `thinking: string`

              The text of Claude's thinking process for this block.

          - `redacted_thinking_block: object`

            - `type: "redacted_thinking"`

            - `data: string`

              The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

              Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

              See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

          - `tool_use_block: object`

            - `type: "tool_use"`

            - `id: string`

              pattern: ^[a-zA-Z0-9_-]+$

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

                - `type: "direct"`

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

                - `type: "code_execution_20250825"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `server_tool_caller_20260120: object`

                - `type: "code_execution_20260120"`

                - `tool_id: string`

                  pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `input: map[unknown]`

            - `name: string`

              minLength: 1

            - `toolset_name: optional string`

              For a toolset member tool_use, the toolset family.

              maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

          - `server_tool_use_block: object`

            - `type: "server_tool_use"`

            - `id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

              - `server_tool_caller_20260120: object`

            - `input: map[unknown]`

            - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

              - `"web_search"`

              - `"web_fetch"`

              - `"code_execution"`

              - `"bash_code_execution"`

              - `"text_editor_code_execution"`

              - `"tool_search_tool_regex"`

              - `"tool_search_tool_bm25"`

          - `web_search_tool_result_block: object`

            - `type: "web_search_tool_result"`

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

              - `server_tool_caller_20260120: object`

            - `content: WebSearchToolResultError or array of WebSearchResultBlock`

              - `web_search_tool_result_error: object`

                - `type: "web_search_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"max_uses_exceeded"`

                  - `"too_many_requests"`

                  - `"query_too_long"`

                  - `"request_too_large"`

              - `union_member_1: array of WebSearchResultBlock`

                - `type: "web_search_result"`

                - `encrypted_content: string`

                - `page_age: string`

                - `title: string`

                - `url: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `web_fetch_tool_result_block: object`

            - `type: "web_fetch_tool_result"`

            - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

              Tool invocation directly from the model.

              - `direct_caller: object`

                Tool invocation directly from the model.

              - `server_tool_caller: object`

                Tool invocation generated by a server-side tool.

              - `server_tool_caller_20260120: object`

            - `content: WebFetchToolResultErrorBlock or WebFetchBlock`

              - `web_fetch_tool_result_error_block: object`

                - `type: "web_fetch_tool_result_error"`

                - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 7 more`

                  - `"invalid_tool_input"`

                  - `"url_too_long"`

                  - `"url_not_allowed"`

                  - `"url_not_in_prior_context"`

                  - `"url_not_accessible"`

                  - `"unsupported_content_type"`

                  - `"too_many_requests"`

                  - `"max_uses_exceeded"`

                  - `"unavailable"`

                  - `"content_too_large"`

              - `web_fetch_block: object`

                - `type: "web_fetch_result"`

                - `content: object`

                  - `type: "document"`

                  - `citations: object`

                    Citation configuration for the document

                    - `enabled: boolean`

                  - `source: Base64PDFSource or PlainTextSource`

                    - `base64_pdf_source: object`

                      - `type: "base64"`

                      - `data: string`

                        format: byte

                      - `media_type: "application/pdf"`

                    - `plain_text_source: object`

                      - `type: "text"`

                      - `data: string`

                      - `media_type: "text/plain"`

                  - `title: string`

                    The title of the document

                - `retrieved_at: string`

                  ISO 8601 timestamp when the content was retrieved

                - `url: string`

                  Fetched content URL

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `code_execution_tool_result_block: object`

            - `type: "code_execution_tool_result"`

            - `content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `code_execution_tool_result_error: object`

                - `type: "code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

              - `code_execution_result_block: object`

                - `type: "code_execution_result"`

                - `content: array of CodeExecutionOutputBlock`

                  - `type: "code_execution_output"`

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

              - `encrypted_code_execution_result_block: object`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type: "encrypted_code_execution_result"`

                - `content: array of CodeExecutionOutputBlock`

                  - `type: "code_execution_output"`

                  - `file_id: string`

                - `encrypted_stdout: string`

                - `return_code: number`

                - `stderr: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `bash_code_execution_tool_result_block: object`

            - `type: "bash_code_execution_tool_result"`

            - `content: BashCodeExecutionToolResultError or BashCodeExecutionResultBlock`

              - `bash_code_execution_tool_result_error: object`

                - `type: "bash_code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"output_file_too_large"`

              - `bash_code_execution_result_block: object`

                - `type: "bash_code_execution_result"`

                - `content: array of BashCodeExecutionOutputBlock`

                  - `type: "bash_code_execution_output"`

                  - `file_id: string`

                - `return_code: number`

                - `stderr: string`

                - `stdout: string`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `text_editor_code_execution_tool_result_block: object`

            - `type: "text_editor_code_execution_tool_result"`

            - `content: TextEditorCodeExecutionToolResultError or TextEditorCodeExecutionViewResultBlock or TextEditorCodeExecutionCreateResultBlock or TextEditorCodeExecutionStrReplaceResultBlock`

              - `text_editor_code_execution_tool_result_error: object`

                - `type: "text_editor_code_execution_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                  - `"file_not_found"`

                - `error_message: string`

              - `text_editor_code_execution_view_result_block: object`

                - `type: "text_editor_code_execution_view_result"`

                - `content: string`

                - `file_type: "text" or "image" or "pdf"`

                  - `"text"`

                  - `"image"`

                  - `"pdf"`

                - `num_lines: number`

                - `start_line: number`

                - `total_lines: number`

              - `text_editor_code_execution_create_result_block: object`

                - `type: "text_editor_code_execution_create_result"`

                - `is_file_update: boolean`

              - `text_editor_code_execution_str_replace_result_block: object`

                - `type: "text_editor_code_execution_str_replace_result"`

                - `lines: array of string`

                - `new_lines: number`

                - `new_start: number`

                - `old_lines: number`

                - `old_start: number`

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `tool_search_tool_result_block: object`

            - `type: "tool_search_tool_result"`

            - `content: ToolSearchToolResultError or ToolSearchToolSearchResultBlock`

              - `tool_search_tool_result_error: object`

                - `type: "tool_search_tool_result_error"`

                - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                  - `"invalid_tool_input"`

                  - `"unavailable"`

                  - `"too_many_requests"`

                  - `"execution_time_exceeded"`

                - `error_message: string`

              - `tool_search_tool_search_result_block: object`

                - `type: "tool_search_tool_search_result"`

                - `tool_references: array of ToolReferenceBlock`

                  - `type: "tool_reference"`

                  - `tool_name: string`

                    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `tool_use_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `container_upload_block: object`

            Response model for a file uploaded to the container.

            - `type: "container_upload"`

            - `file_id: string`

        - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-mythos-5-1"`

            Our most capable model for cybersecurity and biology research, available through trusted access programs

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-mythos-5"`

            Most capable model for cybersecurity and biology research

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-mythos-preview"`

            New class of intelligence, strongest in coding and cybersecurity

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `role: "assistant"`

          Conversational role of the generated message.

          This will always be `"assistant"`.

        - `stop_details: object`

          Structured information about a refusal.

          - `type: "refusal"`

          - `category: "cyber" or "bio" or "frontier_llm" or 2 more`

            The policy category that triggered a refusal.

            - `"cyber"`

              The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

            - `"bio"`

              The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

            - `"frontier_llm"`

              The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

            - `"reasoning_extraction"`

              The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

            - `"general_harms"`

              The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

          - `explanation: string`

            Human-readable explanation of the refusal.

            This text is not guaranteed to be stable. `null` when no explanation is available for the category.

        - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
          * `"model_context_window_exceeded"`: we exceeded the model's context window

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"`

          - `"max_tokens"`

          - `"stop_sequence"`

          - `"tool_use"`

          - `"pause_turn"`

          - `"refusal"`

          - `"model_context_window_exceeded"`

        - `stop_sequence: string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `usage: object`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: object`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

            minimum: 0

          - `inference_geo: string`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

            minimum: 0

          - `output_tokens: number`

            The number of output tokens which were used.

            minimum: 0

          - `output_tokens_details: object`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `thinking_tokens: number`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `server_tool_use: object`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

              minimum: 0

            - `web_search_requests: number`

              The number of web search tool requests.

              minimum: 0

          - `service_tier: "standard" or "priority" or "batch"`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

    - `message_batch_errored_result: object`

      - `type: "errored"`

      - `error: object`

        - `type: "error"`

        - `error: InvalidRequestError or AuthenticationError or BillingError or 6 more`

          - `invalid_request_error: object`

            - `type: "invalid_request_error"`

            - `message: string`

          - `authentication_error: object`

            - `type: "authentication_error"`

            - `message: string`

          - `billing_error: object`

            - `type: "billing_error"`

            - `message: string`

          - `permission_error: object`

            - `type: "permission_error"`

            - `message: string`

          - `not_found_error: object`

            - `type: "not_found_error"`

            - `message: string`

          - `rate_limit_error: object`

            - `type: "rate_limit_error"`

            - `message: string`

          - `gateway_timeout_error: object`

            - `type: "timeout_error"`

            - `message: string`

          - `api_error_object: object`

            - `type: "api_error"`

            - `message: string`

          - `overloaded_error: object`

            - `type: "overloaded_error"`

            - `message: string`

        - `request_id: string`

    - `message_batch_canceled_result: object`

      - `type: "canceled"`

    - `message_batch_expired_result: object`

      - `type: "expired"`

### Message Batch Request Counts

- `message_batch_request_counts: object`

  - `canceled: number`

    Number of requests in the Message Batch that have been canceled.

    This is zero until processing of the entire Message Batch has ended.

  - `errored: number`

    Number of requests in the Message Batch that encountered an error.

    This is zero until processing of the entire Message Batch has ended.

  - `expired: number`

    Number of requests in the Message Batch that have expired.

    This is zero until processing of the entire Message Batch has ended.

  - `processing: number`

    Number of requests in the Message Batch that are processing.

  - `succeeded: number`

    Number of requests in the Message Batch that have completed successfully.

    This is zero until processing of the entire Message Batch has ended.

### Message Batch Result

- `message_batch_result: MessageBatchSucceededResult or MessageBatchErroredResult or MessageBatchCanceledResult or MessageBatchExpiredResult`

  Processing result for this request.

  Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

  - `message_batch_succeeded_result: object`

    - `type: "succeeded"`

    - `message: object`

      - `type: "message"`

        Object type.

        For Messages, this is always `"message"`.

      - `id: string`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `container: object`

        Information about the container used in the request (for the code execution tool)

        - `id: string`

          Identifier for the container used in this request

        - `expires_at: string`

          The time at which the container will expire.

          format: date-time

        - `skills: array of ContainerSkill`

          Skills loaded in the container

          - `type: "anthropic" or "custom"`

            Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

            - `"anthropic"`

            - `"custom"`

          - `skill_id: string`

            Skill ID

            maxLength: 64, minLength: 1

          - `version: string`

            The resolved version: a skill version ID for custom skills.

            maxLength: 64, minLength: 1

      - `content: array of ContentBlock`

        Content generated by the model.

        This is an array of content blocks, each of which has a `type` that determines its shape.

        Example:

        ```json
        [{"type": "text", "text": "Hi, I'm Claude."}]
        ```

        If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

        For example, if the input `messages` were:

        ```json
        [
          {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
          {"role": "assistant", "content": "The best answer is ("}
        ]
        ```

        Then the response `content` might be:

        ```json
        [{"type": "text", "text": "B)"}]
        ```

        - `text_block: object`

          - `type: "text"`

          - `citations: array of TextCitation`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

            - `citation_char_location: object`

              - `type: "char_location"`

              - `cited_text: string`

              - `document_index: number`

                minimum: 0

              - `document_title: string`

              - `end_char_index: number`

              - `file_id: string`

              - `start_char_index: number`

                minimum: 0

            - `citation_page_location: object`

              - `type: "page_location"`

              - `cited_text: string`

              - `document_index: number`

                minimum: 0

              - `document_title: string`

              - `end_page_number: number`

              - `file_id: string`

              - `start_page_number: number`

                minimum: 1

            - `citation_content_block_location: object`

              - `type: "content_block_location"`

              - `cited_text: string`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `document_index: number`

                minimum: 0

              - `document_title: string`

              - `end_block_index: number`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `file_id: string`

              - `start_block_index: number`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

            - `citations_web_search_result_location: object`

              - `type: "web_search_result_location"`

              - `cited_text: string`

              - `encrypted_index: string`

              - `title: string`

                maxLength: 512

              - `url: string`

            - `citations_search_result_location: object`

              - `type: "search_result_location"`

              - `cited_text: string`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `end_block_index: number`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `search_result_index: number`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

                minimum: 0

              - `source: string`

              - `start_block_index: number`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `title: string`

          - `text: string`

            minLength: 0

        - `thinking_block: object`

          - `type: "thinking"`

          - `signature: string`

            A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

            This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

          - `thinking: string`

            The text of Claude's thinking process for this block.

        - `redacted_thinking_block: object`

          - `type: "redacted_thinking"`

          - `data: string`

            The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

            Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

        - `tool_use_block: object`

          - `type: "tool_use"`

          - `id: string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `direct_caller: object`

              Tool invocation directly from the model.

              - `type: "direct"`

            - `server_tool_caller: object`

              Tool invocation generated by a server-side tool.

              - `type: "code_execution_20250825"`

              - `tool_id: string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

            - `server_tool_caller_20260120: object`

              - `type: "code_execution_20260120"`

              - `tool_id: string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `input: map[unknown]`

          - `name: string`

            minLength: 1

          - `toolset_name: optional string`

            For a toolset member tool_use, the toolset family.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `server_tool_use_block: object`

          - `type: "server_tool_use"`

          - `id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `direct_caller: object`

              Tool invocation directly from the model.

            - `server_tool_caller: object`

              Tool invocation generated by a server-side tool.

            - `server_tool_caller_20260120: object`

          - `input: map[unknown]`

          - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

            - `"web_search"`

            - `"web_fetch"`

            - `"code_execution"`

            - `"bash_code_execution"`

            - `"text_editor_code_execution"`

            - `"tool_search_tool_regex"`

            - `"tool_search_tool_bm25"`

        - `web_search_tool_result_block: object`

          - `type: "web_search_tool_result"`

          - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `direct_caller: object`

              Tool invocation directly from the model.

            - `server_tool_caller: object`

              Tool invocation generated by a server-side tool.

            - `server_tool_caller_20260120: object`

          - `content: WebSearchToolResultError or array of WebSearchResultBlock`

            - `web_search_tool_result_error: object`

              - `type: "web_search_tool_result_error"`

              - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"max_uses_exceeded"`

                - `"too_many_requests"`

                - `"query_too_long"`

                - `"request_too_large"`

            - `union_member_1: array of WebSearchResultBlock`

              - `type: "web_search_result"`

              - `encrypted_content: string`

              - `page_age: string`

              - `title: string`

              - `url: string`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `web_fetch_tool_result_block: object`

          - `type: "web_fetch_tool_result"`

          - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

            Tool invocation directly from the model.

            - `direct_caller: object`

              Tool invocation directly from the model.

            - `server_tool_caller: object`

              Tool invocation generated by a server-side tool.

            - `server_tool_caller_20260120: object`

          - `content: WebFetchToolResultErrorBlock or WebFetchBlock`

            - `web_fetch_tool_result_error_block: object`

              - `type: "web_fetch_tool_result_error"`

              - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 7 more`

                - `"invalid_tool_input"`

                - `"url_too_long"`

                - `"url_not_allowed"`

                - `"url_not_in_prior_context"`

                - `"url_not_accessible"`

                - `"unsupported_content_type"`

                - `"too_many_requests"`

                - `"max_uses_exceeded"`

                - `"unavailable"`

                - `"content_too_large"`

            - `web_fetch_block: object`

              - `type: "web_fetch_result"`

              - `content: object`

                - `type: "document"`

                - `citations: object`

                  Citation configuration for the document

                  - `enabled: boolean`

                - `source: Base64PDFSource or PlainTextSource`

                  - `base64_pdf_source: object`

                    - `type: "base64"`

                    - `data: string`

                      format: byte

                    - `media_type: "application/pdf"`

                  - `plain_text_source: object`

                    - `type: "text"`

                    - `data: string`

                    - `media_type: "text/plain"`

                - `title: string`

                  The title of the document

              - `retrieved_at: string`

                ISO 8601 timestamp when the content was retrieved

              - `url: string`

                Fetched content URL

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `code_execution_tool_result_block: object`

          - `type: "code_execution_tool_result"`

          - `content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `code_execution_tool_result_error: object`

              - `type: "code_execution_tool_result_error"`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

            - `code_execution_result_block: object`

              - `type: "code_execution_result"`

              - `content: array of CodeExecutionOutputBlock`

                - `type: "code_execution_output"`

                - `file_id: string`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

            - `encrypted_code_execution_result_block: object`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `type: "encrypted_code_execution_result"`

              - `content: array of CodeExecutionOutputBlock`

                - `type: "code_execution_output"`

                - `file_id: string`

              - `encrypted_stdout: string`

              - `return_code: number`

              - `stderr: string`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `bash_code_execution_tool_result_block: object`

          - `type: "bash_code_execution_tool_result"`

          - `content: BashCodeExecutionToolResultError or BashCodeExecutionResultBlock`

            - `bash_code_execution_tool_result_error: object`

              - `type: "bash_code_execution_tool_result_error"`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"output_file_too_large"`

            - `bash_code_execution_result_block: object`

              - `type: "bash_code_execution_result"`

              - `content: array of BashCodeExecutionOutputBlock`

                - `type: "bash_code_execution_output"`

                - `file_id: string`

              - `return_code: number`

              - `stderr: string`

              - `stdout: string`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `text_editor_code_execution_tool_result_block: object`

          - `type: "text_editor_code_execution_tool_result"`

          - `content: TextEditorCodeExecutionToolResultError or TextEditorCodeExecutionViewResultBlock or TextEditorCodeExecutionCreateResultBlock or TextEditorCodeExecutionStrReplaceResultBlock`

            - `text_editor_code_execution_tool_result_error: object`

              - `type: "text_editor_code_execution_tool_result_error"`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

                - `"file_not_found"`

              - `error_message: string`

            - `text_editor_code_execution_view_result_block: object`

              - `type: "text_editor_code_execution_view_result"`

              - `content: string`

              - `file_type: "text" or "image" or "pdf"`

                - `"text"`

                - `"image"`

                - `"pdf"`

              - `num_lines: number`

              - `start_line: number`

              - `total_lines: number`

            - `text_editor_code_execution_create_result_block: object`

              - `type: "text_editor_code_execution_create_result"`

              - `is_file_update: boolean`

            - `text_editor_code_execution_str_replace_result_block: object`

              - `type: "text_editor_code_execution_str_replace_result"`

              - `lines: array of string`

              - `new_lines: number`

              - `new_start: number`

              - `old_lines: number`

              - `old_start: number`

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `tool_search_tool_result_block: object`

          - `type: "tool_search_tool_result"`

          - `content: ToolSearchToolResultError or ToolSearchToolSearchResultBlock`

            - `tool_search_tool_result_error: object`

              - `type: "tool_search_tool_result_error"`

              - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

                - `"invalid_tool_input"`

                - `"unavailable"`

                - `"too_many_requests"`

                - `"execution_time_exceeded"`

              - `error_message: string`

            - `tool_search_tool_search_result_block: object`

              - `type: "tool_search_tool_search_result"`

              - `tool_references: array of ToolReferenceBlock`

                - `type: "tool_reference"`

                - `tool_name: string`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `tool_use_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `container_upload_block: object`

          Response model for a file uploaded to the container.

          - `type: "container_upload"`

          - `file_id: string`

      - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-fable-5-1"`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `"claude-mythos-5-1"`

          Our most capable model for cybersecurity and biology research, available through trusted access programs

        - `"claude-sonnet-5"`

          High-performance model for coding and agents

        - `"claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `"claude-mythos-5"`

          Most capable model for cybersecurity and biology research

        - `"claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `"claude-mythos-preview"`

          New class of intelligence, strongest in coding and cybersecurity

        - `"claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `"claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `"claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `"claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `"claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `"claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `"claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `role: "assistant"`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `stop_details: object`

        Structured information about a refusal.

        - `type: "refusal"`

        - `category: "cyber" or "bio" or "frontier_llm" or 2 more`

          The policy category that triggered a refusal.

          - `"cyber"`

            The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

          - `"bio"`

            The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

          - `"frontier_llm"`

            The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

          - `"reasoning_extraction"`

            The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

          - `"general_harms"`

            The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

        - `explanation: string`

          Human-readable explanation of the refusal.

          This text is not guaranteed to be stable. `null` when no explanation is available for the category.

      - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

        The reason that we stopped.

        This may be one the following values:

        * `"end_turn"`: the model reached a natural stopping point
        * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
        * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
        * `"tool_use"`: the model invoked one or more tools
        * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
        * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
        * `"model_context_window_exceeded"`: we exceeded the model's context window

        In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

        - `"end_turn"`

        - `"max_tokens"`

        - `"stop_sequence"`

        - `"tool_use"`

        - `"pause_turn"`

        - `"refusal"`

        - `"model_context_window_exceeded"`

      - `stop_sequence: string`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `usage: object`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

        - `cache_creation: object`

          Breakdown of cached tokens by TTL

          - `ephemeral_1h_input_tokens: number`

            The number of input tokens used to create the 1 hour cache entry.

            minimum: 0

          - `ephemeral_5m_input_tokens: number`

            The number of input tokens used to create the 5 minute cache entry.

            minimum: 0

        - `cache_creation_input_tokens: number`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `cache_read_input_tokens: number`

          The number of input tokens read from the cache.

          minimum: 0

        - `inference_geo: string`

          The geographic region where inference was performed for this request.

        - `input_tokens: number`

          The number of input tokens which were used.

          minimum: 0

        - `output_tokens: number`

          The number of output tokens which were used.

          minimum: 0

        - `output_tokens_details: object`

          Breakdown of output tokens by category.

          `output_tokens` remains the inclusive, authoritative total used for billing.
          This object provides a read-only decomposition for observability — for example,
          how many of the billed output tokens were spent on internal reasoning that may
          have been summarized before being returned to you.

          - `thinking_tokens: number`

            Number of output tokens the model generated as internal reasoning, including
            the thinking-block delimiter tokens.

            Reflects the raw reasoning the model produced, not the (possibly shorter)
            summarized thinking text returned in the response body. Computed by
            re-tokenizing the raw reasoning text, so it may differ from the model's exact
            generation count by a small number of tokens. Always ≤ `output_tokens`;
            `output_tokens - thinking_tokens` approximates the non-reasoning output.

            minimum: 0

        - `server_tool_use: object`

          The number of server tool requests.

          - `web_fetch_requests: number`

            The number of web fetch tool requests.

            minimum: 0

          - `web_search_requests: number`

            The number of web search tool requests.

            minimum: 0

        - `service_tier: "standard" or "priority" or "batch"`

          If the request used the priority, standard, or batch tier.

          - `"standard"`

          - `"priority"`

          - `"batch"`

  - `message_batch_errored_result: object`

    - `type: "errored"`

    - `error: object`

      - `type: "error"`

      - `error: InvalidRequestError or AuthenticationError or BillingError or 6 more`

        - `invalid_request_error: object`

          - `type: "invalid_request_error"`

          - `message: string`

        - `authentication_error: object`

          - `type: "authentication_error"`

          - `message: string`

        - `billing_error: object`

          - `type: "billing_error"`

          - `message: string`

        - `permission_error: object`

          - `type: "permission_error"`

          - `message: string`

        - `not_found_error: object`

          - `type: "not_found_error"`

          - `message: string`

        - `rate_limit_error: object`

          - `type: "rate_limit_error"`

          - `message: string`

        - `gateway_timeout_error: object`

          - `type: "timeout_error"`

          - `message: string`

        - `api_error_object: object`

          - `type: "api_error"`

          - `message: string`

        - `overloaded_error: object`

          - `type: "overloaded_error"`

          - `message: string`

      - `request_id: string`

  - `message_batch_canceled_result: object`

    - `type: "canceled"`

  - `message_batch_expired_result: object`

    - `type: "expired"`

### Message Batch Succeeded Result

- `message_batch_succeeded_result: object`

  - `type: "succeeded"`

  - `message: object`

    - `type: "message"`

      Object type.

      For Messages, this is always `"message"`.

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `container: object`

      Information about the container used in the request (for the code execution tool)

      - `id: string`

        Identifier for the container used in this request

      - `expires_at: string`

        The time at which the container will expire.

        format: date-time

      - `skills: array of ContainerSkill`

        Skills loaded in the container

        - `type: "anthropic" or "custom"`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `"anthropic"`

          - `"custom"`

        - `skill_id: string`

          Skill ID

          maxLength: 64, minLength: 1

        - `version: string`

          The resolved version: a skill version ID for custom skills.

          maxLength: 64, minLength: 1

    - `content: array of ContentBlock`

      Content generated by the model.

      This is an array of content blocks, each of which has a `type` that determines its shape.

      Example:

      ```json
      [{"type": "text", "text": "Hi, I'm Claude."}]
      ```

      If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

      For example, if the input `messages` were:

      ```json
      [
        {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
        {"role": "assistant", "content": "The best answer is ("}
      ]
      ```

      Then the response `content` might be:

      ```json
      [{"type": "text", "text": "B)"}]
      ```

      - `text_block: object`

        - `type: "text"`

        - `citations: array of TextCitation`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `citation_char_location: object`

            - `type: "char_location"`

            - `cited_text: string`

            - `document_index: number`

              minimum: 0

            - `document_title: string`

            - `end_char_index: number`

            - `file_id: string`

            - `start_char_index: number`

              minimum: 0

          - `citation_page_location: object`

            - `type: "page_location"`

            - `cited_text: string`

            - `document_index: number`

              minimum: 0

            - `document_title: string`

            - `end_page_number: number`

            - `file_id: string`

            - `start_page_number: number`

              minimum: 1

          - `citation_content_block_location: object`

            - `type: "content_block_location"`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `document_index: number`

              minimum: 0

            - `document_title: string`

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `file_id: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

          - `citations_web_search_result_location: object`

            - `type: "web_search_result_location"`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

              maxLength: 512

            - `url: string`

          - `citations_search_result_location: object`

            - `type: "search_result_location"`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `search_result_index: number`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `source: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `title: string`

        - `text: string`

          minLength: 0

      - `thinking_block: object`

        - `type: "thinking"`

        - `signature: string`

          A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

          This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `thinking: string`

          The text of Claude's thinking process for this block.

      - `redacted_thinking_block: object`

        - `type: "redacted_thinking"`

        - `data: string`

          The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

          Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `tool_use_block: object`

        - `type: "tool_use"`

        - `id: string`

          pattern: ^[a-zA-Z0-9_-]+$

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `direct_caller: object`

            Tool invocation directly from the model.

            - `type: "direct"`

          - `server_tool_caller: object`

            Tool invocation generated by a server-side tool.

            - `type: "code_execution_20250825"`

            - `tool_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `server_tool_caller_20260120: object`

            - `type: "code_execution_20260120"`

            - `tool_id: string`

              pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `input: map[unknown]`

        - `name: string`

          minLength: 1

        - `toolset_name: optional string`

          For a toolset member tool_use, the toolset family.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `server_tool_use_block: object`

        - `type: "server_tool_use"`

        - `id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `direct_caller: object`

            Tool invocation directly from the model.

          - `server_tool_caller: object`

            Tool invocation generated by a server-side tool.

          - `server_tool_caller_20260120: object`

        - `input: map[unknown]`

        - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

          - `"web_search"`

          - `"web_fetch"`

          - `"code_execution"`

          - `"bash_code_execution"`

          - `"text_editor_code_execution"`

          - `"tool_search_tool_regex"`

          - `"tool_search_tool_bm25"`

      - `web_search_tool_result_block: object`

        - `type: "web_search_tool_result"`

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `direct_caller: object`

            Tool invocation directly from the model.

          - `server_tool_caller: object`

            Tool invocation generated by a server-side tool.

          - `server_tool_caller_20260120: object`

        - `content: WebSearchToolResultError or array of WebSearchResultBlock`

          - `web_search_tool_result_error: object`

            - `type: "web_search_tool_result_error"`

            - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"max_uses_exceeded"`

              - `"too_many_requests"`

              - `"query_too_long"`

              - `"request_too_large"`

          - `union_member_1: array of WebSearchResultBlock`

            - `type: "web_search_result"`

            - `encrypted_content: string`

            - `page_age: string`

            - `title: string`

            - `url: string`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `web_fetch_tool_result_block: object`

        - `type: "web_fetch_tool_result"`

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

          - `direct_caller: object`

            Tool invocation directly from the model.

          - `server_tool_caller: object`

            Tool invocation generated by a server-side tool.

          - `server_tool_caller_20260120: object`

        - `content: WebFetchToolResultErrorBlock or WebFetchBlock`

          - `web_fetch_tool_result_error_block: object`

            - `type: "web_fetch_tool_result_error"`

            - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 7 more`

              - `"invalid_tool_input"`

              - `"url_too_long"`

              - `"url_not_allowed"`

              - `"url_not_in_prior_context"`

              - `"url_not_accessible"`

              - `"unsupported_content_type"`

              - `"too_many_requests"`

              - `"max_uses_exceeded"`

              - `"unavailable"`

              - `"content_too_large"`

          - `web_fetch_block: object`

            - `type: "web_fetch_result"`

            - `content: object`

              - `type: "document"`

              - `citations: object`

                Citation configuration for the document

                - `enabled: boolean`

              - `source: Base64PDFSource or PlainTextSource`

                - `base64_pdf_source: object`

                  - `type: "base64"`

                  - `data: string`

                    format: byte

                  - `media_type: "application/pdf"`

                - `plain_text_source: object`

                  - `type: "text"`

                  - `data: string`

                  - `media_type: "text/plain"`

              - `title: string`

                The title of the document

            - `retrieved_at: string`

              ISO 8601 timestamp when the content was retrieved

            - `url: string`

              Fetched content URL

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `code_execution_tool_result_block: object`

        - `type: "code_execution_tool_result"`

        - `content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `code_execution_tool_result_error: object`

            - `type: "code_execution_tool_result_error"`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

          - `code_execution_result_block: object`

            - `type: "code_execution_result"`

            - `content: array of CodeExecutionOutputBlock`

              - `type: "code_execution_output"`

              - `file_id: string`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

          - `encrypted_code_execution_result_block: object`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `type: "encrypted_code_execution_result"`

            - `content: array of CodeExecutionOutputBlock`

              - `type: "code_execution_output"`

              - `file_id: string`

            - `encrypted_stdout: string`

            - `return_code: number`

            - `stderr: string`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `bash_code_execution_tool_result_block: object`

        - `type: "bash_code_execution_tool_result"`

        - `content: BashCodeExecutionToolResultError or BashCodeExecutionResultBlock`

          - `bash_code_execution_tool_result_error: object`

            - `type: "bash_code_execution_tool_result_error"`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"output_file_too_large"`

          - `bash_code_execution_result_block: object`

            - `type: "bash_code_execution_result"`

            - `content: array of BashCodeExecutionOutputBlock`

              - `type: "bash_code_execution_output"`

              - `file_id: string`

            - `return_code: number`

            - `stderr: string`

            - `stdout: string`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `text_editor_code_execution_tool_result_block: object`

        - `type: "text_editor_code_execution_tool_result"`

        - `content: TextEditorCodeExecutionToolResultError or TextEditorCodeExecutionViewResultBlock or TextEditorCodeExecutionCreateResultBlock or TextEditorCodeExecutionStrReplaceResultBlock`

          - `text_editor_code_execution_tool_result_error: object`

            - `type: "text_editor_code_execution_tool_result_error"`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

              - `"file_not_found"`

            - `error_message: string`

          - `text_editor_code_execution_view_result_block: object`

            - `type: "text_editor_code_execution_view_result"`

            - `content: string`

            - `file_type: "text" or "image" or "pdf"`

              - `"text"`

              - `"image"`

              - `"pdf"`

            - `num_lines: number`

            - `start_line: number`

            - `total_lines: number`

          - `text_editor_code_execution_create_result_block: object`

            - `type: "text_editor_code_execution_create_result"`

            - `is_file_update: boolean`

          - `text_editor_code_execution_str_replace_result_block: object`

            - `type: "text_editor_code_execution_str_replace_result"`

            - `lines: array of string`

            - `new_lines: number`

            - `new_start: number`

            - `old_lines: number`

            - `old_start: number`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `tool_search_tool_result_block: object`

        - `type: "tool_search_tool_result"`

        - `content: ToolSearchToolResultError or ToolSearchToolSearchResultBlock`

          - `tool_search_tool_result_error: object`

            - `type: "tool_search_tool_result_error"`

            - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

              - `"invalid_tool_input"`

              - `"unavailable"`

              - `"too_many_requests"`

              - `"execution_time_exceeded"`

            - `error_message: string`

          - `tool_search_tool_search_result_block: object`

            - `type: "tool_search_tool_search_result"`

            - `tool_references: array of ToolReferenceBlock`

              - `type: "tool_reference"`

              - `tool_name: string`

                maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `container_upload_block: object`

        Response model for a file uploaded to the container.

        - `type: "container_upload"`

        - `file_id: string`

    - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5-1"`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `"claude-mythos-5-1"`

        Our most capable model for cybersecurity and biology research, available through trusted access programs

      - `"claude-sonnet-5"`

        High-performance model for coding and agents

      - `"claude-fable-5"`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `"claude-mythos-5"`

        Most capable model for cybersecurity and biology research

      - `"claude-opus-5"`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-8"`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-7"`

        Powerful intelligence for long-running agents and coding

      - `"claude-mythos-preview"`

        New class of intelligence, strongest in coding and cybersecurity

      - `"claude-opus-4-6"`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-6"`

        Best combination of speed and intelligence

      - `"claude-haiku-4-5"`

        Fastest model with near-frontier intelligence

      - `"claude-haiku-4-5-20251001"`

        Fastest model with near-frontier intelligence

      - `"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-5"`

        High-performance model for agents and coding

      - `"claude-sonnet-4-5-20250929"`

        High-performance model for agents and coding

    - `role: "assistant"`

      Conversational role of the generated message.

      This will always be `"assistant"`.

    - `stop_details: object`

      Structured information about a refusal.

      - `type: "refusal"`

      - `category: "cyber" or "bio" or "frontier_llm" or 2 more`

        The policy category that triggered a refusal.

        - `"cyber"`

          The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

        - `"bio"`

          The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

        - `"frontier_llm"`

          The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

        - `"reasoning_extraction"`

          The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

        - `"general_harms"`

          The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

      - `explanation: string`

        Human-readable explanation of the refusal.

        This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

      The reason that we stopped.

      This may be one the following values:

      * `"end_turn"`: the model reached a natural stopping point
      * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
      * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
      * `"tool_use"`: the model invoked one or more tools
      * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
      * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
      * `"model_context_window_exceeded"`: we exceeded the model's context window

      In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

      - `"end_turn"`

      - `"max_tokens"`

      - `"stop_sequence"`

      - `"tool_use"`

      - `"pause_turn"`

      - `"refusal"`

      - `"model_context_window_exceeded"`

    - `stop_sequence: string`

      Which custom stop sequence was generated, if any.

      This value will be a non-null string if one of your custom stop sequences was generated.

    - `usage: object`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation: object`

        Breakdown of cached tokens by TTL

        - `ephemeral_1h_input_tokens: number`

          The number of input tokens used to create the 1 hour cache entry.

          minimum: 0

        - `ephemeral_5m_input_tokens: number`

          The number of input tokens used to create the 5 minute cache entry.

          minimum: 0

      - `cache_creation_input_tokens: number`

        The number of input tokens used to create the cache entry.

        minimum: 0

      - `cache_read_input_tokens: number`

        The number of input tokens read from the cache.

        minimum: 0

      - `inference_geo: string`

        The geographic region where inference was performed for this request.

      - `input_tokens: number`

        The number of input tokens which were used.

        minimum: 0

      - `output_tokens: number`

        The number of output tokens which were used.

        minimum: 0

      - `output_tokens_details: object`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

        - `thinking_tokens: number`

          Number of output tokens the model generated as internal reasoning, including
          the thinking-block delimiter tokens.

          Reflects the raw reasoning the model produced, not the (possibly shorter)
          summarized thinking text returned in the response body. Computed by
          re-tokenizing the raw reasoning text, so it may differ from the model's exact
          generation count by a small number of tokens. Always ≤ `output_tokens`;
          `output_tokens - thinking_tokens` approximates the non-reasoning output.

          minimum: 0

      - `server_tool_use: object`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

          minimum: 0

        - `web_search_requests: number`

          The number of web search tool requests.

          minimum: 0

      - `service_tier: "standard" or "priority" or "batch"`

        If the request used the priority, standard, or batch tier.

        - `"standard"`

        - `"priority"`

        - `"batch"`
