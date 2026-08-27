# List Message Batches

`BatchListPageResponse Beta.Messages.Batches.List(parameters, cancellationToken = default)`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `BatchListParams parameters`

  - `string afterID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

## Returns

- `class BatchListPageResponse:`

  - `required IReadOnlyList<BetaMessageBatch> Data`

    - `required string ID`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `required DateTimeOffset? ArchivedAt`

      RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

      format: date-time

    - `required DateTimeOffset? CancelInitiatedAt`

      RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

      format: date-time

    - `required DateTimeOffset CreatedAt`

      RFC 3339 datetime string representing the time at which the Message Batch was created.

      format: date-time

    - `required DateTimeOffset? EndedAt`

      RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

      Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

      format: date-time

    - `required DateTimeOffset ExpiresAt`

      RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

      format: date-time

    - `required ProcessingStatus ProcessingStatus`

      Processing status of the Message Batch.

      - `InProgress`

      - `Canceling`

      - `Ended`

    - `required BetaMessageBatchRequestCounts RequestCounts`

      Tallies requests within the Message Batch, categorized by their status.

      Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

      - `required long Canceled`

        Number of requests in the Message Batch that have been canceled.

        This is zero until processing of the entire Message Batch has ended.

      - `required long Errored`

        Number of requests in the Message Batch that encountered an error.

        This is zero until processing of the entire Message Batch has ended.

      - `required long Expired`

        Number of requests in the Message Batch that have expired.

        This is zero until processing of the entire Message Batch has ended.

      - `required long Processing`

        Number of requests in the Message Batch that are processing.

      - `required long Succeeded`

        Number of requests in the Message Batch that have completed successfully.

        This is zero until processing of the entire Message Batch has ended.

    - `required string? ResultsUrl`

      URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

      Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

    - `JsonElement Type constant`

      Object type.

      For Message Batches, this is always `"message_batch"`.

  - `required string? FirstID`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `required bool HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? LastID`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

## Example

```csharp
BatchListParams parameters = new();

var page = await client.Beta.Messages.Batches.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

### Response (200)

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
