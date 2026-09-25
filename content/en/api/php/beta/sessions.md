---
title: Sessions
url: https://platform.claude.com/docs/en/api/php/beta/sessions
---

# Sessions

## Create Session

`$client->beta->sessions->create(Agent agent, string environmentID, ?BetaManagedAgentsBudgetLimit budget, ?list<InitialEvent> initialEvents, ?array<string,string> metadata, ?list<Resource> resources, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsSession`

**POST** `/v1/sessions`

Create Session

### Parameters

- `agent: Agent`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

- `environmentID: string`

  ID of the `environment` defining the container configuration for this session.

- `budget?:optional BetaManagedAgentsBudgetLimit`

  Enforced spend ceiling for the session. Omit to create an uncapped session. Every model the session can run — the agent's model and each callable agent's model — must have a public list price, or the request is rejected with reason `model_not_budgetable`.

- `initialEvents?:optional list<InitialEvent>`

  Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources?:optional list<Resource>`

  Resources (e.g. repositories, files) to mount into the session's container.

- `title?:optional string`

  Human-readable session title.

- `vaultIDs?:optional list<string>`

  Vault IDs for stored credentials the agent can use during the session.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsSession`

  - `Type type`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    When the session was archived. Null if not archived.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's enforced spend ceiling, or null when no budget is set.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for the session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for the session.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->create(
  agent: 'agent_011CZkYpogX7uDKUyvBTophP',
  environmentID: 'env_011CZkZ9X2dpNyB7HsEFoRfW',
  budget: [
    'maxListCost' => ['amount' => '2500', 'currency' => BetaCurrency::USD],
    'type' => 'limit',
  ],
  initialEvents: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  metadata: ['foo' => 'string'],
  resources: [
    [
      'fileID' => 'file_011CNha8iCJcU1wXNR6q4V8w',
      'type' => 'file',
      'mountPath' => '/uploads/receipt.pdf',
    ],
  ],
  title: 'Order #1234 inquiry',
  vaultIDs: ['string'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSession);
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## List Sessions

`$client->beta->sessions->list(?string agentID, ?int agentVersion, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?string deploymentID, ?bool includeArchived, ?int limit, ?string memoryStoreID, ?Order order, ?string page, ?list<Status> statuses, ?list<AnthropicBeta> betas, ?string workspaceID): BidirectionalPageCursor<BetaManagedAgentsSession>`

**GET** `/v1/sessions`

List Sessions

### Parameters

- `agentID?:optional string`

  Filter sessions created with this agent ID.

- `agentVersion?:optional int`

  Filter by agent version. Only applies when `agent_id` is also set.

- `createdAtGt?:optional \Datetime`

  Return sessions created after this time (exclusive).

- `createdAtGte?:optional \Datetime`

  Return sessions created at or after this time (inclusive).

- `createdAtLt?:optional \Datetime`

  Return sessions created before this time (exclusive).

- `createdAtLte?:optional \Datetime`

  Return sessions created at or before this time (inclusive).

- `deploymentID?:optional string`

  Filter sessions created by this deployment ID.

- `includeArchived?:optional bool`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit?:optional int`

  Maximum number of results to return.

- `memoryStoreID?:optional string`

  Filter sessions whose resources contain a `memory_store` with this memory store ID.

- `order?:optional Order`

  Sort direction for results, ordered by `created_at`. Defaults to `desc` (newest first).

- `page?:optional string`

  Opaque pagination cursor from a previous response.

- `statuses?:optional list<Status>`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsSession`

  - `Type type`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    When the session was archived. Null if not archived.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's enforced spend ceiling, or null when no budget is set.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for the session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for the session.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->list(
  agentID: 'agent_id',
  agentVersion: 0,
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  deploymentID: 'deployment_id',
  includeArchived: true,
  limit: 0,
  memoryStoreID: 'memory_store_id',
  order: 'asc',
  page: 'page',
  statuses: ['rescheduling'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "description": "A general-purpose starter agent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-opus-5",
          "effort": {
            "type": "low"
          },
          "inference_geo": "inference_geo",
          "speed": "standard"
        },
        "multiagent": {
          "agents": [
            {
              "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
              "description": "A focused research subagent.",
              "mcp_servers": [
                {
                  "name": "example-mcp",
                  "type": "url",
                  "url": "https://example-server.modelcontextprotocol.io/sse"
                }
              ],
              "model": {
                "id": "claude-opus-5",
                "effort": {
                  "type": "low"
                },
                "inference_geo": "inference_geo",
                "speed": "standard"
              },
              "name": "Researcher",
              "skills": [
                {
                  "skill_id": "xlsx",
                  "type": "anthropic",
                  "version": "1"
                }
              ],
              "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
              "tools": [
                {
                  "configs": [
                    {
                      "enabled": true,
                      "name": "bash",
                      "permission_policy": {
                        "type": "always_allow"
                      },
                      "type": "bash"
                    }
                  ],
                  "default_config": {
                    "enabled": true,
                    "permission_policy": {
                      "type": "always_ask"
                    }
                  },
                  "type": "agent_toolset_20260401"
                }
              ],
              "type": "agent",
              "version": 1
            }
          ],
          "type": "coordinator"
        },
        "name": "My First Agent",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          },
          {
            "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
            "type": "custom",
            "version": "2"
          }
        ],
        "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                },
                "type": "bash"
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "metadata": {},
      "outcome_evaluations": [
        {
          "completed_at": "2026-03-15T10:02:31Z",
          "description": "Produce a 2-page summary as summary.md",
          "explanation": "All five sections present with inline citations.",
          "iteration": 0,
          "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
          "result": "satisfied",
          "type": "outcome_evaluation"
        }
      ],
      "resources": [
        {
          "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
          "created_at": "2026-03-15T10:00:00Z",
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "mount_path": "/uploads/receipt.pdf",
          "type": "file",
          "updated_at": "2026-03-15T10:00:00Z"
        },
        {
          "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
          "created_at": "2026-03-15T10:00:00Z",
          "mount_path": "/workspace/example-repo",
          "type": "github_repository",
          "updated_at": "2026-03-15T10:00:00Z",
          "url": "https://github.com/example-org/example-repo",
          "checkout": {
            "name": "main",
            "type": "branch"
          }
        }
      ],
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0
      },
      "status": "idle",
      "title": "Order #1234 inquiry",
      "type": "session",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "active_seconds": 0,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "output_tokens": 0,
        "server_tool_use": {
          "web_fetch_requests": 0,
          "web_search_requests": 3
        }
      },
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "deployment_id": "deployment_id"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo=",
  "prev_page": "page_MjAyNS0wNS0xM1QwMDowMDowMFo="
}
```

## Get Session

`$client->beta->sessions->retrieve(string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsSession`

**GET** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsSession`

  - `Type type`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    When the session was archived. Null if not archived.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's enforced spend ceiling, or null when no budget is set.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for the session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for the session.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->retrieve(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSession);
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Update Session

`$client->beta->sessions->update(string sessionID, ?BetaManagedAgentsSessionAgentUpdate agent, ?BetaManagedAgentsBudgetLimit budget, ?array<string,string> metadata, ?string title, ?list<string> vaultIDs, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsSession`

**POST** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `sessionID: string`

- `agent?:optional BetaManagedAgentsSessionAgentUpdate`

  Agent configuration update. Only `tools` and `mcp_servers` are updatable mid-session. Only valid for sessions created from an agent or deployment reference. The session must not be running.

- `budget?:optional BetaManagedAgentsBudgetLimit`

  Enforced spend ceiling for the session. Set an object to replace the budget of a session that was created with one, or `null` to remove it; omit to preserve. A budget cannot be added to a session created without one (rejected with reason `budget_create_only`), and a removed budget cannot be re-added. Allowed in any non-terminated status. Lowering `max_list_cost` to at or below the session's consumed list cost is rejected with reason `budget_not_raised`, and every model the session can run must have a public list price or the request is rejected with reason `model_not_budgetable`.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `title?:optional string`

  Human-readable session title.

- `vaultIDs?:optional list<string>`

  Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsSession`

  - `Type type`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    When the session was archived. Null if not archived.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's enforced spend ceiling, or null when no budget is set.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for the session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for the session.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->update(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  agent: [
    'mcpServers' => [
      [
        'name' => 'example-mcp',
        'type' => 'url',
        'url' => 'https://example-server.modelcontextprotocol.io/sse',
      ],
    ],
    'tools' => [
      [
        'type' => 'agent_toolset_20260401',
        'configs' => [
          [
            'name' => 'bash',
            'enabled' => true,
            'permissionPolicy' => ['type' => 'always_allow'],
            'type' => 'bash',
          ],
        ],
        'defaultConfig' => [
          'enabled' => true, 'permissionPolicy' => ['type' => 'always_allow']
        ],
      ],
    ],
  ],
  budget: [
    'maxListCost' => ['amount' => '2500', 'currency' => BetaCurrency::USD],
    'type' => 'limit',
  ],
  metadata: ['foo' => 'string'],
  title: 'Order #1234 inquiry',
  vaultIDs: ['string'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSession);
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Delete Session

`$client->beta->sessions->delete(string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeletedSession`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedSession`

  - `Type type`

  - `string id`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedSession = $client->beta->sessions->delete(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedSession);
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`$client->beta->sessions->archive(string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsSession`

**POST** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `sessionID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsSession`

  - `Type type`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    When the session was archived. Null if not archived.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's enforced spend ceiling, or null when no budget is set.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for the session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for the session.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSession = $client->beta->sessions->archive(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSession);
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Domain types

### Beta Managed Agents Advisor Params

- `class BetaManagedAgentsAdvisorParams`

  - `Type type`

  - `string model`

    A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

### Beta Managed Agents Agent Message Preview

- `class BetaManagedAgentsAgentMessagePreview`

  - `Type type`

  - `string id`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams`

  - `Type type`

  - `string id`

    The `agent` ID.

  - `?int version`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

### Beta Managed Agents Agent Thinking Preview

- `class BetaManagedAgentsAgentThinkingPreview`

  - `Type type`

  - `string id`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

### Beta Managed Agents Agent With Overrides Params

- `class BetaManagedAgentsAgentWithOverridesParams`

  - `Type type`

  - `string id`

    The `agent` ID.

  - `?list<BetaManagedAgentsURLMCPServerParams> mcpServers`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

  - `?Model model`

    Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

  - `?list<BetaManagedAgentsSkillParams> skills`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

  - `?string system`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

  - `?list<Tool> tools`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

  - `?int version`

    The specific `agent` version to use. Omit to use the latest version.

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout`

  - `Type type`

  - `string name`

    Branch name to check out.

### Beta Managed Agents Budget Limit

- `class BetaManagedAgentsBudgetLimit`

  - `Type type`

  - `BetaMonetaryAmount maxListCost`

    Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge.

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage`

  - `?int ephemeral1hInputTokens`

    Tokens used to create 1-hour ephemeral cache entries.

  - `?int ephemeral5mInputTokens`

    Tokens used to create 5-minute ephemeral cache entries.

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout`

  - `Type type`

  - `string sha`

    Full commit SHA to check out.

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession`

  - `Type type`

  - `string id`

### Beta Managed Agents Delta Content

- `class BetaManagedAgentsDeltaContent`

  - `Type type`

  - `ManagedAgentsTextBlock content`

    A partial element of the content array at index, typed like the element itself — the same shape the buffered agent.message carries in content.

  - `?int index`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

### Beta Managed Agents Delta Event

- `class BetaManagedAgentsDeltaEvent`

  - `Type type`

  - `BetaManagedAgentsDeltaContent delta`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

  - `string eventID`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

### Beta Managed Agents Delta Type

- `enum BetaManagedAgentsDeltaType`

  - `"agent.message"`

  - `"agent.thinking"`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams`

  - `Type type`

  - `string fileID`

    ID of a previously uploaded file.

  - `?string mountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Params

- `class BetaManagedAgentsGitHubRepositoryResourceParams`

  - `Type type`

  - `string url`

    Github URL of the repository

  - `?string authorizationToken`

    GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

  - `?Checkout checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

  - `?string mountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Memory Store Resource Param

- `class BetaManagedAgentsMemoryStoreResourceParam`

  - `Type type`

  - `string memoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `?Access access`

    Access mode for the mounted store. Defaults to read_write. read_only mounts the store as a read-only filesystem.

  - `?string instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Multiagent

- `class BetaManagedAgentsMultiagent`

  - `Type type`

  - `list<Agent> agents`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

### Beta Managed Agents Multiagent Params

- `class BetaManagedAgentsMultiagentParams`

  - `Type type`

  - `list<BetaManagedAgentsMultiagentRosterEntryParams> agents`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

### Beta Managed Agents Multiagent Roster Entry Params

- `class BetaManagedAgentsMultiagentRosterEntryParams`

  - `string`

  - `class BetaManagedAgentsAgentParams`

    - `Type type`

    - `string id`

      The `agent` ID.

    - `?int version`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `class BetaManagedAgentsMultiagentSelfParams`

    - `Type type`

  - `class BetaManagedAgentsAdvisorParams`

    - `Type type`

    - `string model`

      A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

### Beta Managed Agents Outcome Evaluation Resource

- `class BetaManagedAgentsOutcomeEvaluationResource`

  - `Type type`

  - `?\Datetime completedAt`

    When the outcome reached a terminal result. Null while `pending`/`running`/`evaluating`.

  - `string description`

    What the agent should produce.

  - `?string explanation`

    Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

  - `int iteration`

    0-indexed revision cycle the outcome is currently on.

  - `string outcomeID`

    Server-generated outc_ ID for this outcome.

  - `string result`

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

### Beta Managed Agents Server Tool Usage

- `class BetaManagedAgentsServerToolUsage`

  - `?int webFetchRequests`

    Number of server-executed web fetch requests.

  - `?int webSearchRequests`

    Number of server-executed web search requests.

### Beta Managed Agents Session

- `class BetaManagedAgentsSession`

  - `Type type`

  - `string id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `?\Datetime archivedAt`

    When the session was archived. Null if not archived.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's enforced spend ceiling, or null when no budget is set.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string environmentID`

  - `array<string,string> metadata`

  - `list<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

  - `list<ManagedAgentsSessionResource> resources`

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for the session.

  - `Status status`

    SessionStatus enum

  - `?string title`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for the session.

  - `list<string> vaultIDs`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `?string deploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent`

  - `Type type`

  - `string id`

  - `?string description`

  - `list<BetaManagedAgentsMCPServerURLDefinition> mcpServers`

  - `BetaManagedAgentsModelConfig model`

    Model identifier and configuration.

  - `?BetaManagedAgentsSessionMultiagentCoordinator multiagent`

    Resolved multiagent orchestration configuration. Null when the agent is single-threaded.

  - `string name`

  - `list<Skill> skills`

  - `?string system`

  - `list<Tool> tools`

  - `int version`

### Beta Managed Agents Session Agent Update

- `class BetaManagedAgentsSessionAgentUpdate`

  - `?list<BetaManagedAgentsURLMCPServerParams> mcpServers`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

  - `?list<Tool> tools`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

### Beta Managed Agents Session Multiagent Coordinator

- `class BetaManagedAgentsSessionMultiagentCoordinator`

  - `Type type`

  - `list<Agent> agents`

    Full `agent` definitions the coordinator may spawn as session threads.

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats`

  - `?float activeSeconds`

    Cumulative time in seconds the session spent in `running` status. Excludes idle time.

  - `?float durationSeconds`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

### Beta Managed Agents Session Updated Event

- `class BetaManagedAgentsSessionUpdatedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    Timestamp when the update was applied.

  - `?BetaManagedAgentsSessionAgent agent`

    The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

  - `?array<string,string> metadata`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `?string title`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage`

  - `?float activeSeconds`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

  - `?BetaManagedAgentsCacheCreationUsage cacheCreation`

    Tokens used to create prompt cache entries, broken down by cache TTL.

  - `?int cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `?int inputTokens`

    Total input tokens consumed across all turns.

  - `?BetaMonetaryAmount listCost`

    Cumulative list cost of the session across all turns, priced at public list rates. Absent until cost tracking is available for the session.

  - `?int outputTokens`

    Total output tokens generated across all turns.

  - `?BetaManagedAgentsServerToolUsage serverToolUse`

    Cumulative server-executed tool usage across all turns. Absent until server-tool tracking is available for the session.

### Beta Managed Agents Session Usage Event

- `class BetaManagedAgentsSessionUsageEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    Timestamp when the snapshot was taken.

  - `ManagedAgentsSessionUsageSnapshot usage`

    The session's cumulative usage at the snapshot time.

  - `?BetaManagedAgentsBudgetLimit budget`

    The session's configured budget at the snapshot time, or null when the session has no budget.

### Beta Managed Agents Start Event

- `class BetaManagedAgentsStartEvent`

  - `Type type`

  - `BetaManagedAgentsStartEventPreview event`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

### Beta Managed Agents Start Event Preview

- `class BetaManagedAgentsStartEventPreview`

  - `class BetaManagedAgentsAgentMessagePreview`

    - `Type type`

    - `string id`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `class BetaManagedAgentsAgentThinkingPreview`

    - `Type type`

    - `string id`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

### Beta Managed Agents System Content Block

- `class BetaManagedAgentsSystemContentBlock`

  - `Type type`

  - `string text`

    The text content.

### Beta Managed Agents System Message Event

- `class BetaManagedAgentsSystemMessageEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks. Text-only.

  - `?\Datetime processedAt`

    Timestamp when this system message was processed.

### Beta Managed Agents User Tool Result Event

- `class BetaManagedAgentsUserToolResultEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

  - `?\Datetime processedAt`

    Timestamp when this result was processed.

  - `?string sessionThreadID`

    Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

## Sessions › Events

### List Events

`$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?Order order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/events`

List Events

#### Parameters

- `sessionID: string`

- `createdAtGt?:optional \Datetime`

  Return events created after this time (exclusive). Compared against the event's `processed_at` value.

- `createdAtGte?:optional \Datetime`

  Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

- `createdAtLt?:optional \Datetime`

  Return events created before this time (exclusive). Compared against the event's `processed_at` value.

- `createdAtLte?:optional \Datetime`

  Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

- `limit?:optional int`

- `order?:optional Order`

  Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

- `page?:optional string`

  Opaque pagination cursor from a previous response's `next_page`.

- `types?:optional list<string>`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionEvent`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->events->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  order: 'asc',
  page: 'page',
  types: ['string'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Send Events

`$client->beta->sessions->events->send(string sessionID, list<ManagedAgentsEventParams> events, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsSendSessionEvents`

**POST** `/v1/sessions/{session_id}/events`

Send Events

#### Parameters

- `sessionID: string`

- `events: list<ManagedAgentsEventParams>`

  Events to send to the `session`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSendSessionEvents = $client->beta->sessions->events->send(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  events: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSendSessionEvents);
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

### Stream Events

`$client->beta->sessions->events->stream(string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsStreamSessionEvents`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

#### Parameters

- `sessionID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsStreamSessionEvents`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `class BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionEvents = $client
  ->beta
  ->sessions
  ->events
  ->streamStream(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsStreamSessionEvents);
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

## Sessions › Resources

### Add Session Resource

`$client->beta->sessions->resources->add(string sessionID, string fileID, Type type, ?string mountPath, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsFileResource`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `sessionID: string`

- `fileID: string`

  ID of a previously uploaded file.

- `type: Type`

- `mountPath?:optional string`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsFileResource`

  - `Type type`

  - `string id`

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string fileID`

  - `string mountPath`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsFileResource = $client->beta->sessions->resources->add(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  fileID: 'file_011CNha8iCJcU1wXNR6q4V8w',
  type: 'file',
  mountPath: '/uploads/receipt.pdf',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsFileResource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### List Session Resources

`$client->beta->sessions->resources->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionResource>`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `sessionID: string`

- `limit?:optional int`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

- `page?:optional string`

  Opaque cursor from a previous response's `next_page` field.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionResource`

  - `class ManagedAgentsGitHubRepositoryResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `class ManagedAgentsFileResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsMemoryStoreResource`

    - `Type type`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `?Access access`

      Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->resources->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Resource

`$client->beta->sessions->resources->retrieve(string resourceID, string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): ResourceGetResponse`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `sessionID: string`

- `resourceID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ResourceGetResponse`

  - `class ManagedAgentsGitHubRepositoryResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `class ManagedAgentsFileResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsMemoryStoreResource`

    - `Type type`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `?Access access`

      Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$resource = $client->beta->sessions->resources->retrieve(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($resource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Update Session Resource

`$client->beta->sessions->resources->update(string resourceID, string sessionID, string authorizationToken, ?list<AnthropicBeta> betas, ?string workspaceID): ResourceUpdateResponse`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `sessionID: string`

- `resourceID: string`

- `authorizationToken: string`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ResourceUpdateResponse`

  - `class ManagedAgentsGitHubRepositoryResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

    - `string url`

    - `?Checkout checkout`

  - `class ManagedAgentsFileResource`

    - `Type type`

    - `string id`

    - `\Datetime createdAt`

      A timestamp in RFC 3339 format

    - `string fileID`

    - `string mountPath`

    - `\Datetime updatedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsMemoryStoreResource`

    - `Type type`

    - `string memoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `?Access access`

      Access mode for the mounted store. Defaults to `read_write`. `read_only` mounts the store as a read-only filesystem.

    - `?string description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `?string instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `?string mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `?string name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$resource = $client->beta->sessions->resources->update(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  authorizationToken: 'ghp_exampletoken',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($resource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Delete Session Resource

`$client->beta->sessions->resources->delete(string resourceID, string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeleteSessionResource`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `sessionID: string`

- `resourceID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsDeleteSessionResource`

  - `Type type`

  - `string id`

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeleteSessionResource = $client
  ->beta
  ->sessions
  ->resources
  ->delete(
  'sesrsc_011CZkZBJq5dWxk9fVLNcPht',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeleteSessionResource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Sessions › Threads

### List Session Threads

`$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionThread>`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `sessionID: string`

- `limit?:optional int`

  Maximum results per page. Defaults to 1000.

- `page?:optional string`

  Opaque pagination cursor from a previous response's `next_page`. Forward-only.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "description": "A focused research subagent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-opus-5",
          "effort": {
            "type": "low"
          },
          "inference_geo": "inference_geo",
          "speed": "standard"
        },
        "name": "Researcher",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          }
        ],
        "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                },
                "type": "bash"
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "active_seconds": 0,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "output_tokens": 0,
        "server_tool_use": {
          "web_fetch_requests": 0,
          "web_search_requests": 3
        }
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Thread

`$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsSessionThread`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSessionThread = $client->beta->sessions->threads->retrieve(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSessionThread);
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

### Archive Session Thread

`$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsSessionThread`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSessionThread = $client->beta->sessions->threads->archive(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSessionThread);
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

## Sessions › Threads › Events

### List Session Thread Events

`$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `sessionID: string`

- `threadID: string`

- `limit?:optional int`

- `page?:optional string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionEvent`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->events->list(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

### Stream Session Thread Events

`$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsStreamSessionThreadEvents`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `sessionID: string`

- `threadID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsStreamSessionThreadEvents`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `class BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionThreadEvents = $client
  ->beta
  ->sessions
  ->threads
  ->events
  ->streamStream(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsStreamSessionThreadEvents);
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
