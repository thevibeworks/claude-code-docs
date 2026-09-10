---
title: Get Queue Statistics
url: https://platform.claude.com/docs/en/api/cli/beta/environments/work/stats
---

# Get Queue Statistics

`$ ant beta:environments:work stats`

**GET** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

## Parameters

- `--environment-id: string`

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

- `--workspace-id: optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_self_hosted_work_queue_stats: object`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `type: "work_queue_stats"`

    The type of object

  - `depth: number`

    Number of work items waiting to be picked up (lag from consumer group)

  - `oldest_queued_at: string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `pending: number`

    Number of work items being processed (polled but not acknowledged)

  - `workers_polling: number`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

## Example

```bash
ant beta:environments:work stats \
  --api-key my-anthropic-api-key \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

### Response (200)

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```
