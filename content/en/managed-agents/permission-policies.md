---
title: Permission policies
url: https://platform.claude.com/docs/en/managed-agents/permission-policies
description: Control when agent and MCP tools execute.
---

Permission policies control whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically, wait for your approval, or have each call evaluated by the server. Custom tools are executed by your application and controlled by you, so they are not governed by permission policies.

<Note>
  Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](https://platform.claude.com/docs/en/api/beta-headers#endpoint-specific-headers).
</Note>

## Permission policy types

| Policy         | Behavior                                                                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `always_allow` | The tool executes automatically with no confirmation.                                                                                                                                                                                                        |
| `always_ask`   | The session pauses and waits for your approval before executing. See [Respond to confirmation requests](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests) for the event flow.                         |
| `auto`         | The server evaluates each call and runs it, denies it, or pauses for your approval. See [Let the server evaluate each call with `auto`](https://platform.claude.com/docs/en/managed-agents/permission-policies#let-the-server-evaluate-each-call-with-auto). |

Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets default to `always_ask`.

A permission policy controls when an enabled tool runs. To remove a tool from the agent entirely, disable it instead. See [Disabling specific tools](https://platform.claude.com/docs/en/managed-agents/tools#disabling-specific-tools).

## Set a policy for a toolset

You set permission policies in the agent's `tools` configuration when you create the agent, and you can change them later by [updating the agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-an-agent). Running sessions keep the toolset configuration they were created with. Updates apply to sessions created afterward.

### Agent toolset permissions

When creating an agent, you can apply a policy to every tool in `agent_toolset_20260401` using `default_config.permission_policy`:

<CodeGroup defaultLanguage="CLI">
  ```bash cURL
  agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "Coding Assistant",
      "model": "claude-opus-5",
      "tools": [
        {
          "type": "agent_toolset_20260401",
          "default_config": {
            "permission_policy": {"type": "always_ask"}
          }
        }
      ]
    }')
  ```

  <MultiFileExample language="cli" label="CLI">
    ```bash CLI
    ant apply agent.md
    ```

    <File filename="agent.md">
      ```markdown
      ---
      name: Coding Assistant
      model: claude-opus-5
      tools:
        - type: agent_toolset_20260401
          default_config:
            permission_policy:
              type: always_ask
      ---
      ```
    </File>
  </MultiFileExample>

  ```python Python
  agent = client.beta.agents.create(
      name="Coding Assistant",
      model="claude-opus-5",
      tools=[
          {
              "type": "agent_toolset_20260401",
              "default_config": {
                  "permission_policy": {"type": "always_ask"},
              },
          },
      ],
  )
  ```

  ```typescript TypeScript
  const agent = await client.beta.agents.create({
    name: "Coding Assistant",
    model: "claude-opus-5",
    tools: [
      {
        type: "agent_toolset_20260401",
        default_config: {
          permission_policy: { type: "always_ask" }
        }
      }
    ]
  });
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Agents;

  var agent = await client.Beta.Agents.Create(new()
  {
      Name = "Coding Assistant",
      Model = BetaManagedAgentsModel.ClaudeOpus5,
      Tools =
      [
          new BetaManagedAgentsAgentToolset20260401Params
          {
              Type = BetaManagedAgentsAgentToolset20260401ParamsType.AgentToolset20260401,
              DefaultConfig = new()
              {
                  PermissionPolicy = new BetaManagedAgentsAlwaysAskPolicy { Type = "always_ask" },
              },
          },
      ],
  });
  ```

  ```go Go
  agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
  	Name: "Coding Assistant",
  	Model: anthropic.BetaManagedAgentsModelConfigParams{
  		ID: "claude-opus-5",
  	},
  	Tools: []anthropic.BetaAgentNewParamsToolUnion{{
  		OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
  			Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
  			DefaultConfig: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParams{
  				PermissionPolicy: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnion{
  					OfAlwaysAsk: &anthropic.BetaManagedAgentsAlwaysAskPolicyParam{
  						Type: anthropic.BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk,
  					},
  				},
  			},
  		},
  	}},
  })
  if err != nil {
  	panic(err)
  }
  _ = agent
  ```

  ```java Java
  import com.anthropic.models.beta.agents.*;

  var agent = client.beta().agents().create(
      AgentCreateParams.builder()
          .name("Coding Assistant")
          .model(BetaManagedAgentsModel.CLAUDE_OPUS_5)
          .addTool(
              BetaManagedAgentsAgentToolset20260401Params.builder()
                  .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                  .defaultConfig(
                      BetaManagedAgentsAgentToolsetDefaultConfigParams.builder()
                          .permissionPolicy(
                              BetaManagedAgentsAlwaysAskPolicy.builder()
                                  .type(BetaManagedAgentsAlwaysAskPolicy.Type.ALWAYS_ASK)
                                  .build()
                          )
                          .build()
                  )
                  .build()
          )
          .build()
  );
  ```

  ```php PHP
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolset20260401Params;
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolsetDefaultConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsAlwaysAskPolicy;

  $agent = $client->beta->agents->create(
      name: 'Coding Assistant',
      model: 'claude-opus-5',
      tools: [
          BetaManagedAgentsAgentToolset20260401Params::with(
              type: 'agent_toolset_20260401',
              defaultConfig: BetaManagedAgentsAgentToolsetDefaultConfigParams::with(
                  permissionPolicy: BetaManagedAgentsAlwaysAskPolicy::with(type: 'always_ask'),
              ),
          ),
      ],
  );
  ```

  ```ruby Ruby
  agent = client.beta.agents.create(
    name: "Coding Assistant",
    model: "claude-opus-5",
    tools: [
      {
        type: "agent_toolset_20260401",
        default_config: {
          permission_policy: {type: "always_ask"}
        }
      }
    ]
  )
  ```
</CodeGroup>

`default_config` is optional. If you omit it, the agent toolset is enabled with the default permission policy, `always_allow`.

### MCP toolset permissions

MCP toolsets default to `always_ask`. This ensures that new tools added to an MCP server do not execute in your application without approval. To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry.

The `mcp_server_name` must match the `name` of a server in the `mcp_servers` array.

This example connects a GitHub MCP server and allows its tools to run without confirmation:

<CodeGroup defaultLanguage="CLI">
  ```bash cURL
  agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "Dev Assistant",
      "model": "claude-opus-5",
      "mcp_servers": [
        {"type": "url", "name": "github", "url": "https://mcp.example.com/github"}
      ],
      "tools": [
        {"type": "agent_toolset_20260401"},
        {
          "type": "mcp_toolset",
          "mcp_server_name": "github",
          "default_config": {
            "permission_policy": {"type": "always_allow"}
          }
        }
      ]
    }')
  ```

  <MultiFileExample language="cli" label="CLI">
    ```bash CLI
    ant apply agent.md
    ```

    <File filename="agent.md">
      ```markdown
      ---
      name: Dev Assistant
      model: claude-opus-5
      mcp_servers:
        - type: url
          name: github
          url: https://mcp.example.com/github
      tools:
        - type: agent_toolset_20260401
        - type: mcp_toolset
          mcp_server_name: github
          default_config:
            permission_policy:
              type: always_allow
      ---
      ```
    </File>
  </MultiFileExample>

  ```python Python
  agent = client.beta.agents.create(
      name="Dev Assistant",
      model="claude-opus-5",
      mcp_servers=[
          {"type": "url", "name": "github", "url": "https://mcp.example.com/github"},
      ],
      tools=[
          {"type": "agent_toolset_20260401"},
          {
              "type": "mcp_toolset",
              "mcp_server_name": "github",
              "default_config": {
                  "permission_policy": {"type": "always_allow"},
              },
          },
      ],
  )
  ```

  ```typescript TypeScript
  const agent = await client.beta.agents.create({
    name: "Dev Assistant",
    model: "claude-opus-5",
    mcp_servers: [{ type: "url", name: "github", url: "https://mcp.example.com/github" }],
    tools: [
      { type: "agent_toolset_20260401" },
      {
        type: "mcp_toolset",
        mcp_server_name: "github",
        default_config: {
          permission_policy: { type: "always_allow" }
        }
      }
    ]
  });
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Agents;

  var agent = await client.Beta.Agents.Create(new()
  {
      Name = "Dev Assistant",
      Model = BetaManagedAgentsModel.ClaudeOpus5,
      McpServers =
      [
          new()
          {
              Type = BetaManagedAgentsUrlMcpServerParamsType.Url,
              Name = "github",
              Url = "https://mcp.example.com/github",
          },
      ],
      Tools =
      [
          new BetaManagedAgentsAgentToolset20260401Params
          {
              Type = BetaManagedAgentsAgentToolset20260401ParamsType.AgentToolset20260401,
          },
          new BetaManagedAgentsMcpToolsetParams
          {
              Type = BetaManagedAgentsMcpToolsetParamsType.McpToolset,
              McpServerName = "github",
              DefaultConfig = new()
              {
                  PermissionPolicy = new BetaManagedAgentsAlwaysAllowPolicy { Type = "always_allow" },
              },
          },
      ],
  });
  ```

  ```go Go
  agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
  	Name: "Dev Assistant",
  	Model: anthropic.BetaManagedAgentsModelConfigParams{
  		ID: "claude-opus-5",
  	},
  	MCPServers: []anthropic.BetaManagedAgentsURLMCPServerParams{{
  		Type: anthropic.BetaManagedAgentsURLMCPServerParamsTypeURL,
  		Name: "github",
  		URL:  "https://mcp.example.com/github",
  	}},
  	Tools: []anthropic.BetaAgentNewParamsToolUnion{
  		{
  			OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
  				Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
  			},
  		},
  		{
  			OfMCPToolset: &anthropic.BetaManagedAgentsMCPToolsetParams{
  				Type:          anthropic.BetaManagedAgentsMCPToolsetParamsTypeMCPToolset,
  				MCPServerName: "github",
  				DefaultConfig: anthropic.BetaManagedAgentsMCPToolsetDefaultConfigParams{
  					PermissionPolicy: anthropic.BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnion{
  						OfAlwaysAllow: &anthropic.BetaManagedAgentsAlwaysAllowPolicyParam{
  							Type: anthropic.BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow,
  						},
  					},
  				},
  			},
  		},
  	},
  })
  if err != nil {
  	panic(err)
  }
  _ = agent
  ```

  ```java Java
  import com.anthropic.models.beta.agents.*;

  var agent = client.beta().agents().create(
      AgentCreateParams.builder()
          .name("Dev Assistant")
          .model(BetaManagedAgentsModel.CLAUDE_OPUS_5)
          .addMcpServer(
              BetaManagedAgentsUrlMcpServerParams.builder()
                  .type(BetaManagedAgentsUrlMcpServerParams.Type.URL)
                  .name("github")
                  .url("https://mcp.example.com/github")
                  .build()
          )
          .addTool(
              BetaManagedAgentsAgentToolset20260401Params.builder()
                  .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                  .build()
          )
          .addTool(
              BetaManagedAgentsMcpToolsetParams.builder()
                  .type(BetaManagedAgentsMcpToolsetParams.Type.MCP_TOOLSET)
                  .mcpServerName("github")
                  .defaultConfig(
                      BetaManagedAgentsMcpToolsetDefaultConfigParams.builder()
                          .permissionPolicy(
                              BetaManagedAgentsAlwaysAllowPolicy.builder()
                                  .type(BetaManagedAgentsAlwaysAllowPolicy.Type.ALWAYS_ALLOW)
                                  .build()
                          )
                          .build()
                  )
                  .build()
          )
          .build()
  );
  ```

  ```php PHP
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolset20260401Params;
  use Anthropic\Beta\Agents\BetaManagedAgentsAlwaysAllowPolicy;
  use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetDefaultConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsURLMCPServerParams;

  $agent = $client->beta->agents->create(
      name: 'Dev Assistant',
      model: 'claude-opus-5',
      mcpServers: [
          BetaManagedAgentsURLMCPServerParams::with(
              type: 'url',
              name: 'github',
              url: 'https://mcp.example.com/github',
          ),
      ],
      tools: [
          BetaManagedAgentsAgentToolset20260401Params::with(
              type: 'agent_toolset_20260401',
          ),
          BetaManagedAgentsMCPToolsetParams::with(
              type: 'mcp_toolset',
              mcpServerName: 'github',
              defaultConfig: BetaManagedAgentsMCPToolsetDefaultConfigParams::with(
                  permissionPolicy: BetaManagedAgentsAlwaysAllowPolicy::with(type: 'always_allow'),
              ),
          ),
      ],
  );
  ```

  ```ruby Ruby
  agent = client.beta.agents.create(
    name: "Dev Assistant",
    model: "claude-opus-5",
    mcp_servers: [
      {type: "url", name: "github", url: "https://mcp.example.com/github"}
    ],
    tools: [
      {type: "agent_toolset_20260401"},
      {
        type: "mcp_toolset",
        mcp_server_name: "github",
        default_config: {
          permission_policy: {type: "always_allow"}
        }
      }
    ]
  )
  ```
</CodeGroup>

## Override an individual tool policy

Use the `configs` array to override the default for individual tools. The `name` values for the agent toolset are listed in [Available tools](https://platform.claude.com/docs/en/managed-agents/tools#available-tools). This example allows the full agent toolset by default but requires confirmation before any bash command runs:

<CodeGroup defaultLanguage="CLI">
  ```bash cURL
  tools='[
    {
      "type": "agent_toolset_20260401",
      "default_config": {
        "permission_policy": {"type": "always_allow"}
      },
      "configs": [
        {
          "name": "bash",
          "permission_policy": {"type": "always_ask"}
        }
      ]
    }
  ]'
  ```

  ```bash CLI
  ant beta:agents create <<'YAML'
  name: Coding Assistant
  model: claude-opus-5
  tools:
    - type: agent_toolset_20260401
      default_config:
        permission_policy:
          type: always_allow
      configs:
        - name: bash
          permission_policy:
            type: always_ask
  YAML
  ```

  ```python Python
  tools = [
      {
          "type": "agent_toolset_20260401",
          "default_config": {
              "permission_policy": {"type": "always_allow"},
          },
          "configs": [
              {
                  "name": "bash",
                  "permission_policy": {"type": "always_ask"},
              },
          ],
      },
  ]
  ```

  ```typescript TypeScript
  const tools = [
    {
      type: "agent_toolset_20260401",
      default_config: {
        permission_policy: { type: "always_allow" }
      },
      configs: [
        {
          name: "bash",
          permission_policy: { type: "always_ask" }
        }
      ]
    }
  ] satisfies Anthropic.Beta.AgentCreateParams["tools"];
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Agents;
  using Tool = Anthropic.Models.Beta.Agents.Tool;

  Tool[] tools =
  [
      new BetaManagedAgentsAgentToolset20260401Params
      {
          Type = BetaManagedAgentsAgentToolset20260401ParamsType.AgentToolset20260401,
          DefaultConfig = new()
          {
              PermissionPolicy = new BetaManagedAgentsAlwaysAllowPolicy { Type = "always_allow" },
          },
          Configs =
          [
              new BetaManagedAgentsBashToolConfigParams
              {
                  PermissionPolicy = new BetaManagedAgentsAlwaysAskPolicy { Type = "always_ask" },
              },
          ],
      },
  ];
  ```

  ```go Go
  tools := []anthropic.BetaAgentNewParamsToolUnion{{
  	OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
  		Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
  		DefaultConfig: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParams{
  			PermissionPolicy: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnion{
  				OfAlwaysAllow: &anthropic.BetaManagedAgentsAlwaysAllowPolicyParam{
  					Type: anthropic.BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow,
  				},
  			},
  		},
  		Configs: []anthropic.BetaManagedAgentsAgentToolConfigParamsUnion{{
  			OfBash: &anthropic.BetaManagedAgentsBashToolConfigParams{
  				PermissionPolicy: anthropic.BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnion{
  					OfAlwaysAsk: &anthropic.BetaManagedAgentsAlwaysAskPolicyParam{
  						Type: anthropic.BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk,
  					},
  				},
  			},
  		}},
  	},
  }}
  _ = tools
  ```

  ```java Java
  import com.anthropic.models.beta.agents.*;
  import java.util.List;

  var tools = List.of(
      AgentCreateParams.Tool.ofAgentToolset20260401(
          BetaManagedAgentsAgentToolset20260401Params.builder()
              .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
              .defaultConfig(
                  BetaManagedAgentsAgentToolsetDefaultConfigParams.builder()
                      .permissionPolicy(
                          BetaManagedAgentsAlwaysAllowPolicy.builder()
                              .type(BetaManagedAgentsAlwaysAllowPolicy.Type.ALWAYS_ALLOW)
                              .build()
                      )
                      .build()
              )
              .addConfig(
                  BetaManagedAgentsBashToolConfigParams.builder()
                      .permissionPolicy(
                          BetaManagedAgentsAlwaysAskPolicy.builder()
                              .type(BetaManagedAgentsAlwaysAskPolicy.Type.ALWAYS_ASK)
                              .build()
                      )
                      .build()
              )
              .build()
      )
  );
  ```

  ```php PHP
  use Anthropic\Beta\Agents\BetaManagedAgentsBashToolConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolset20260401Params;
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolsetDefaultConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsAlwaysAllowPolicy;
  use Anthropic\Beta\Agents\BetaManagedAgentsAlwaysAskPolicy;

  $tools = [
      BetaManagedAgentsAgentToolset20260401Params::with(
          type: 'agent_toolset_20260401',
          defaultConfig: BetaManagedAgentsAgentToolsetDefaultConfigParams::with(
              permissionPolicy: BetaManagedAgentsAlwaysAllowPolicy::with(type: 'always_allow'),
          ),
          configs: [
              BetaManagedAgentsBashToolConfigParams::with(
                  permissionPolicy: BetaManagedAgentsAlwaysAskPolicy::with(type: 'always_ask'),
              ),
          ],
      ),
  ];
  ```

  ```ruby Ruby
  tools = [
    {
      type: "agent_toolset_20260401",
      default_config: {
        permission_policy: {type: "always_allow"}
      },
      configs: [
        {
          name: "bash",
          permission_policy: {type: "always_ask"}
        }
      ]
    }
  ]
  ```
</CodeGroup>

Pass this `tools` configuration in the agent create request (the CLI tab shows the complete command). MCP toolsets support the same per-tool overrides, with `name` set to the tool name reported by the MCP server. See [Configure which MCP tools are available](https://platform.claude.com/docs/en/managed-agents/mcp-connector#configure-which-mcp-tools-are-available).

## Let the server evaluate each call with `auto`

With the `auto` permission policy, the server evaluates each call before it runs. Because the evaluation considers the tool, the call's input, and the session's content up to that point, the server can treat two calls to the same tool differently. Each call has one of three outcomes:

* **The call runs.** When the server determines that the call is safe, the tool runs as it would under `always_allow`.
* **The call is denied.** When the server evaluates the call as high-risk, the tool does not run. The agent receives an error tool result with the content `Permission to use {tool_name} has been denied.` and `is_error: true`. The session keeps running, and your client cannot override the denial.
* **The call pauses for your approval.** When the server reaches no determination, the session pauses as it does under `always_ask`. See [Respond to confirmation requests](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests).

To turn on `auto`, set `permission_policy` to `{"type": "auto"}`. It goes in the same two places as the other policies: a toolset's [`default_config`](https://platform.claude.com/docs/en/managed-agents/permission-policies#set-a-policy-for-a-toolset) for the whole toolset, or a [`configs` entry](https://platform.claude.com/docs/en/managed-agents/permission-policies#override-an-individual-tool-policy) for one tool. The agent toolset and MCP toolsets both accept it. No toolset uses `auto` by default.

The following example sets `auto` as the default for the agent toolset and for the `github` MCP toolset, and overrides `bash` to `always_ask`:

<CodeGroup defaultLanguage="CLI">
  ```bash cURL
  agent=$(curl -fsSL https://api.anthropic.com/v1/agents \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{
      "name": "Ops Agent",
      "model": "claude-opus-5",
      "mcp_servers": [
        {"type": "url", "name": "github", "url": "https://mcp.example.com/github"}
      ],
      "tools": [
        {
          "type": "agent_toolset_20260401",
          "default_config": {
            "permission_policy": {"type": "auto"}
          },
          "configs": [
            {"name": "bash", "permission_policy": {"type": "always_ask"}}
          ]
        },
        {
          "type": "mcp_toolset",
          "mcp_server_name": "github",
          "default_config": {
            "permission_policy": {"type": "auto"}
          }
        }
      ]
    }')
  ```

  <MultiFileExample language="cli" label="CLI">
    ```bash CLI
    ant apply agent.md
    ```

    <File filename="agent.md">
      ```markdown
      ---
      name: Ops Agent
      model: claude-opus-5
      mcp_servers:
        - type: url
          name: github
          url: https://mcp.example.com/github
      tools:
        - type: agent_toolset_20260401
          default_config:
            permission_policy:
              type: auto
          configs:
            - name: bash
              permission_policy:
                type: always_ask
        - type: mcp_toolset
          mcp_server_name: github
          default_config:
            permission_policy:
              type: auto
      ---
      ```
    </File>
  </MultiFileExample>

  ```python Python
  agent = client.beta.agents.create(
      name="Ops Agent",
      model="claude-opus-5",
      mcp_servers=[
          {"type": "url", "name": "github", "url": "https://mcp.example.com/github"},
      ],
      tools=[
          {
              "type": "agent_toolset_20260401",
              "default_config": {
                  "permission_policy": {"type": "auto"},
              },
              "configs": [
                  {"name": "bash", "permission_policy": {"type": "always_ask"}},
              ],
          },
          {
              "type": "mcp_toolset",
              "mcp_server_name": "github",
              "default_config": {
                  "permission_policy": {"type": "auto"},
              },
          },
      ],
  )
  ```

  ```typescript TypeScript
  const agent = await client.beta.agents.create({
    name: "Ops Agent",
    model: "claude-opus-5",
    mcp_servers: [{ type: "url", name: "github", url: "https://mcp.example.com/github" }],
    tools: [
      {
        type: "agent_toolset_20260401",
        default_config: {
          permission_policy: { type: "auto" }
        },
        configs: [{ name: "bash", permission_policy: { type: "always_ask" } }]
      },
      {
        type: "mcp_toolset",
        mcp_server_name: "github",
        default_config: {
          permission_policy: { type: "auto" }
        }
      }
    ]
  });
  ```

  ```csharp C#
  using Anthropic.Models.Beta.Agents;

  var agent = await client.Beta.Agents.Create(new()
  {
      Name = "Ops Agent",
      Model = BetaManagedAgentsModel.ClaudeOpus5,
      McpServers =
      [
          new()
          {
              Type = BetaManagedAgentsUrlMcpServerParamsType.Url,
              Name = "github",
              Url = "https://mcp.example.com/github",
          },
      ],
      Tools =
      [
          new BetaManagedAgentsAgentToolset20260401Params
          {
              Type = BetaManagedAgentsAgentToolset20260401ParamsType.AgentToolset20260401,
              DefaultConfig = new()
              {
                  PermissionPolicy = new BetaManagedAgentsAutoPolicy(),
              },
              Configs =
              [
                  new BetaManagedAgentsBashToolConfigParams
                  {
                      PermissionPolicy = new BetaManagedAgentsAlwaysAskPolicy { Type = "always_ask" },
                  },
              ],
          },
          new BetaManagedAgentsMcpToolsetParams
          {
              Type = BetaManagedAgentsMcpToolsetParamsType.McpToolset,
              McpServerName = "github",
              DefaultConfig = new()
              {
                  PermissionPolicy = new BetaManagedAgentsAutoPolicy(),
              },
          },
      ],
  });
  ```

  ```go Go
  agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
  	Name: "Ops Agent",
  	Model: anthropic.BetaManagedAgentsModelConfigParams{
  		ID: "claude-opus-5",
  	},
  	MCPServers: []anthropic.BetaManagedAgentsURLMCPServerParams{{
  		Type: anthropic.BetaManagedAgentsURLMCPServerParamsTypeURL,
  		Name: "github",
  		URL:  "https://mcp.example.com/github",
  	}},
  	Tools: []anthropic.BetaAgentNewParamsToolUnion{
  		{
  			OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
  				Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
  				DefaultConfig: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParams{
  					PermissionPolicy: anthropic.BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnion{
  						OfAuto: &anthropic.BetaManagedAgentsAutoPolicyParam{},
  					},
  				},
  				Configs: []anthropic.BetaManagedAgentsAgentToolConfigParamsUnion{{
  					OfBash: &anthropic.BetaManagedAgentsBashToolConfigParams{
  						PermissionPolicy: anthropic.BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnion{
  							OfAlwaysAsk: &anthropic.BetaManagedAgentsAlwaysAskPolicyParam{
  								Type: anthropic.BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk,
  							},
  						},
  					},
  				}},
  			},
  		},
  		{
  			OfMCPToolset: &anthropic.BetaManagedAgentsMCPToolsetParams{
  				Type:          anthropic.BetaManagedAgentsMCPToolsetParamsTypeMCPToolset,
  				MCPServerName: "github",
  				DefaultConfig: anthropic.BetaManagedAgentsMCPToolsetDefaultConfigParams{
  					PermissionPolicy: anthropic.BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnion{
  						OfAuto: &anthropic.BetaManagedAgentsAutoPolicyParam{},
  					},
  				},
  			},
  		},
  	},
  })
  if err != nil {
  	panic(err)
  }
  _ = agent
  ```

  ```java Java
  import com.anthropic.models.beta.agents.*;

  var agent = client.beta().agents().create(
      AgentCreateParams.builder()
          .name("Ops Agent")
          .model(BetaManagedAgentsModel.CLAUDE_OPUS_5)
          .addMcpServer(
              BetaManagedAgentsUrlMcpServerParams.builder()
                  .type(BetaManagedAgentsUrlMcpServerParams.Type.URL)
                  .name("github")
                  .url("https://mcp.example.com/github")
                  .build()
          )
          .addTool(
              BetaManagedAgentsAgentToolset20260401Params.builder()
                  .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
                  .defaultConfig(
                      BetaManagedAgentsAgentToolsetDefaultConfigParams.builder()
                          .permissionPolicy(BetaManagedAgentsAutoPolicy.builder().build())
                          .build()
                  )
                  .addConfig(
                      BetaManagedAgentsBashToolConfigParams.builder()
                          .permissionPolicy(
                              BetaManagedAgentsAlwaysAskPolicy.builder()
                                  .type(BetaManagedAgentsAlwaysAskPolicy.Type.ALWAYS_ASK)
                                  .build()
                          )
                          .build()
                  )
                  .build()
          )
          .addTool(
              BetaManagedAgentsMcpToolsetParams.builder()
                  .type(BetaManagedAgentsMcpToolsetParams.Type.MCP_TOOLSET)
                  .mcpServerName("github")
                  .defaultConfig(
                      BetaManagedAgentsMcpToolsetDefaultConfigParams.builder()
                          .permissionPolicy(BetaManagedAgentsAutoPolicy.builder().build())
                          .build()
                  )
                  .build()
          )
          .build()
  );
  ```

  ```php PHP
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolset20260401Params;
  use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolsetDefaultConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsAlwaysAskPolicy;
  use Anthropic\Beta\Agents\BetaManagedAgentsAutoPolicy;
  use Anthropic\Beta\Agents\BetaManagedAgentsBashToolConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetDefaultConfigParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetParams;
  use Anthropic\Beta\Agents\BetaManagedAgentsURLMCPServerParams;

  $agent = $client->beta->agents->create(
      name: 'Ops Agent',
      model: 'claude-opus-5',
      mcpServers: [
          BetaManagedAgentsURLMCPServerParams::with(
              type: 'url',
              name: 'github',
              url: 'https://mcp.example.com/github',
          ),
      ],
      tools: [
          BetaManagedAgentsAgentToolset20260401Params::with(
              type: 'agent_toolset_20260401',
              defaultConfig: BetaManagedAgentsAgentToolsetDefaultConfigParams::with(
                  permissionPolicy: BetaManagedAgentsAutoPolicy::with(),
              ),
              configs: [
                  BetaManagedAgentsBashToolConfigParams::with(
                      permissionPolicy: BetaManagedAgentsAlwaysAskPolicy::with(type: 'always_ask'),
                  ),
              ],
          ),
          BetaManagedAgentsMCPToolsetParams::with(
              type: 'mcp_toolset',
              mcpServerName: 'github',
              defaultConfig: BetaManagedAgentsMCPToolsetDefaultConfigParams::with(
                  permissionPolicy: BetaManagedAgentsAutoPolicy::with(),
              ),
          ),
      ],
  );
  ```

  ```ruby Ruby
  agent = client.beta.agents.create(
    name: "Ops Agent",
    model: "claude-opus-5",
    mcp_servers: [
      {type: "url", name: "github", url: "https://mcp.example.com/github"}
    ],
    tools: [
      {
        type: "agent_toolset_20260401",
        default_config: {
          permission_policy: {type: "auto"}
        },
        configs: [
          {name: "bash", permission_policy: {type: "always_ask"}}
        ]
      },
      {
        type: "mcp_toolset",
        mcp_server_name: "github",
        default_config: {
          permission_policy: {type: "auto"}
        }
      }
    ]
  )
  ```
</CodeGroup>

What you post in `user.message` events counts as your intent, and it can lead the server to allow a call it would otherwise deny. The server does not read intent from a tool result, a fetched webpage, an MCP server's response, or a message between [session threads](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#tool-permissions-and-custom-tools). It assesses that content but does not take instructions from it. The server evaluates some calls as high-risk no matter who asks. If you relay untrusted end-user input in `user.message` events, the server reads that input as your intent too, and it can get a call allowed. Configure `always_ask` on the tools you would not let that end user run without review.

<Warning>
  `auto` is not a human checkpoint. If the server determines that a call is safe, the call runs before anyone sees it, and its effects might not be reversible. If a person must review a tool's calls before they run, configure `always_ask` on that tool.
</Warning>

## See how each call was evaluated

Under any permission policy, each `agent.tool_use` and `agent.mcp_tool_use` event carries `evaluated_permission`, the outcome of the call's permission check: `"allow"`, `"ask"`, or `"deny"`. Most events also carry an `evaluation` object whose `type` names the policy that produced that outcome. Under `auto`, the object also records the server's determination, plus a `reason_code` when the outcome is `ask` or `deny`.

For example, when `bash` is under `auto` and the server evaluates a call as high-risk, the denied call appears on the event stream as follows:

```json
{
  "type": "agent.tool_use",
  "id": "sevt_01pqr...",
  "name": "bash",
  "input": {
    "command": "rm -rf /workspace/reports"
  },
  "evaluated_permission": "deny",
  "evaluation": {
    "type": "auto",
    "evaluated_permission": {
      "type": "deny",
      "reason_code": "high_risk"
    }
  },
  "processed_at": "2026-03-25T14:05:12Z"
}
```

The `evaluation` object takes one of the forms in the following table.

| `evaluation`                                                                                | Top-level `evaluated_permission` | Meaning                                                                                  |
| ------------------------------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------------------- |
| `{"type": "always_allow"}`                                                                  | `"allow"`                        | The resolved policy is `always_allow`, so the call ran.                                  |
| `{"type": "always_ask"}`                                                                    | `"ask"`                          | The resolved policy is `always_ask`, so the call paused for your approval.               |
| `{"type": "auto", "evaluated_permission": {"type": "allow"}}`                               | `"allow"`                        | Under `auto`, the server determined that the call was safe, and it ran.                  |
| `{"type": "auto", "evaluated_permission": {"type": "ask", "reason_code": "indeterminate"}}` | `"ask"`                          | Under `auto`, the server reached no determination, so the call paused for your approval. |
| `{"type": "auto", "evaluated_permission": {"type": "deny", "reason_code": "high_risk"}}`    | `"deny"`                         | Under `auto`, the server evaluated the call as high-risk and denied it.                  |

When `evaluation.type` is `"auto"`, its nested `evaluated_permission.type` repeats the event's top-level `evaluated_permission`, so you can read the outcome from either field. A `reason_code` is a value for your client to branch on and keep in audit records, not text to display to end users.

`evaluation` is absent in two cases. When the agent names a tool that is not enabled in the session, the server denies the call without evaluating a policy: the event carries `evaluated_permission: "deny"` and no `evaluation`. Events recorded before `evaluation` was introduced also omit it: read those as `always_allow` when `evaluated_permission` is `"allow"` and as `always_ask` when it is `"ask"`.

Write your client to tolerate an `evaluation.type` or `reason_code` it does not recognize. `agent.custom_tool_use` events carry neither field, because permission policies do not govern [custom tools](https://platform.claude.com/docs/en/managed-agents/permission-policies#custom-tools).

## Respond to confirmation requests

A tool call evaluates to `ask` under an `always_ask` policy, or under `auto` when the server reaches no determination. When that happens:

1. The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
2. The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array. The session waits indefinitely for a response.
3. Send a `user.tool_confirmation` event for each blocking event, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial. You can send several confirmations in a single `events` request.
4. Once all blocking events are resolved, the session transitions back to `running`. Allowed tools execute. Denied tools do not run, and the agent receives a tool result saying the call was rejected, including your `deny_message`.

If you send a `user.tool_confirmation` for an event whose `evaluated_permission` is not `ask`, the API rejects it with a 400 error. That includes calls the server denied under `auto`: your client cannot override them.

To answer interactively instead, use `ant beta:sessions connect`, which shows the waiting call and sends this event when you allow or deny it. See [Connect to a Managed Agents session from your terminal](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/sessions-connect#follow-and-steer-the-session).

In the following examples, the tool-use event IDs come from the `stop_reason.event_ids` array of the `session.status_idle` event. Learn more about receiving events in the [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) guide, or [subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) to be notified when a session pauses for input.

<CodeGroup defaultLanguage="CLI">
  ```bash cURL
  # Allow the tool to execute
  curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{
      "events": [
        {
          "type": "user.tool_confirmation",
          "tool_use_id": "'$AGENT_TOOL_USE_EVENT_ID'",
          "result": "allow"
        }
      ]
    }'

  # Or deny it with an explanation
  curl -fsSL "https://api.anthropic.com/v1/sessions/$SESSION_ID/events" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{
      "events": [
        {
          "type": "user.tool_confirmation",
          "tool_use_id": "'$MCP_TOOL_USE_EVENT_ID'",
          "result": "deny",
          "deny_message": "Don'\''t create issues in the production project. Use the staging project."
        }
      ]
    }'
  ```

  ```bash CLI
  # Allow the tool to execute
  ant beta:sessions:events send \
    --session-id "$SESSION_ID" \
    --event "{type: user.tool_confirmation, tool_use_id: $AGENT_TOOL_USE_EVENT_ID, result: allow}"

  # Or deny it with an explanation
  ant beta:sessions:events send \
    --session-id "$SESSION_ID" \
    --event "{type: user.tool_confirmation, tool_use_id: $MCP_TOOL_USE_EVENT_ID, result: deny,
      deny_message: Don't create issues in the production project. Use the staging project.}"
  ```

  ```python Python
  # Allow the tool to execute
  client.beta.sessions.events.send(
      session.id,
      events=[
          {
              "type": "user.tool_confirmation",
              "tool_use_id": agent_tool_use_event.id,
              "result": "allow",
          },
      ],
  )

  # Or deny it with an explanation
  client.beta.sessions.events.send(
      session.id,
      events=[
          {
              "type": "user.tool_confirmation",
              "tool_use_id": mcp_tool_use_event.id,
              "result": "deny",
              "deny_message": "Don't create issues in the production project. Use the staging project.",
          },
      ],
  )
  ```

  ```typescript TypeScript
  // Allow the tool to execute
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.tool_confirmation",
        tool_use_id: agent_tool_use_event.id,
        result: "allow"
      }
    ]
  });

  // Or deny it with an explanation
  await client.beta.sessions.events.send(session.id, {
    events: [
      {
        type: "user.tool_confirmation",
        tool_use_id: mcp_tool_use_event.id,
        result: "deny",
        deny_message: "Don't create issues in the production project. Use the staging project."
      }
    ]
  });
  ```

  ```csharp C#
  // Allow the tool to execute
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserToolConfirmationEventParams
          {
              Type = BetaManagedAgentsUserToolConfirmationEventParamsType.UserToolConfirmation,
              ToolUseID = agentToolUseEvent.ID,
              Result = "allow",
          },
      ],
  });

  // Or deny it with an explanation
  await client.Beta.Sessions.Events.Send(session.ID, new()
  {
      Events =
      [
          new BetaManagedAgentsUserToolConfirmationEventParams
          {
              Type = BetaManagedAgentsUserToolConfirmationEventParamsType.UserToolConfirmation,
              ToolUseID = mcpToolUseEvent.ID,
              Result = "deny",
              DenyMessage = "Don't create issues in the production project. Use the staging project.",
          },
      ],
  });
  ```

  ```go Go
  // Allow the tool to execute
  _, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  		OfUserToolConfirmation: &anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
  			Type:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
  			ToolUseID: agentToolUseEvent.ID,
  			Result:    anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultAllow,
  		},
  	}},
  })
  if err != nil {
  	panic(err)
  }

  // Or deny it with an explanation
  _, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
  	Events: []anthropic.BetaManagedAgentsEventParamsUnion{{
  		OfUserToolConfirmation: &anthropic.BetaManagedAgentsUserToolConfirmationEventParams{
  			Type:        anthropic.BetaManagedAgentsUserToolConfirmationEventParamsTypeUserToolConfirmation,
  			ToolUseID:   mcpToolUseEvent.ID,
  			Result:      anthropic.BetaManagedAgentsUserToolConfirmationEventParamsResultDeny,
  			DenyMessage: anthropic.String("Don't create issues in the production project. Use the staging project."),
  		},
  	}},
  })
  if err != nil {
  	panic(err)
  }
  ```

  ```java Java
  // Allow the tool to execute
  client.beta().sessions().events().send(
      session.id(),
      EventSendParams.builder()
          .addEvent(
              BetaManagedAgentsUserToolConfirmationEventParams.builder()
                  .type(BetaManagedAgentsUserToolConfirmationEventParams.Type.USER_TOOL_CONFIRMATION)
                  .toolUseId(agentToolUseEvent.id())
                  .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.ALLOW)
                  .build()
          )
          .build()
  );

  // Or deny it with an explanation
  client.beta().sessions().events().send(
      session.id(),
      EventSendParams.builder()
          .addEvent(
              BetaManagedAgentsUserToolConfirmationEventParams.builder()
                  .type(BetaManagedAgentsUserToolConfirmationEventParams.Type.USER_TOOL_CONFIRMATION)
                  .toolUseId(mcpToolUseEvent.id())
                  .result(BetaManagedAgentsUserToolConfirmationEventParams.Result.DENY)
                  .denyMessage("Don't create issues in the production project. Use the staging project.")
                  .build()
          )
          .build()
  );
  ```

  ```php PHP
  use Anthropic\Beta\Sessions\Events\ManagedAgentsUserToolConfirmationEventParams;

  // Allow the tool to execute
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          ManagedAgentsUserToolConfirmationEventParams::with(
              type: 'user.tool_confirmation',
              toolUseID: $agentToolUseEvent->id,
              result: 'allow',
          ),
      ],
  );

  // Or deny it with an explanation
  $client->beta->sessions->events->send(
      $session->id,
      events: [
          ManagedAgentsUserToolConfirmationEventParams::with(
              type: 'user.tool_confirmation',
              toolUseID: $mcpToolUseEvent->id,
              result: 'deny',
              denyMessage: "Don't create issues in the production project. Use the staging project.",
          ),
      ],
  );
  ```

  ```ruby Ruby
  # Allow the tool to execute
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "user.tool_confirmation",
        tool_use_id: agent_tool_use_event.id,
        result: "allow"
      }
    ]
  )

  # Or deny it with an explanation
  client.beta.sessions.events.send_(
    session.id,
    events: [
      {
        type: "user.tool_confirmation",
        tool_use_id: mcp_tool_use_event.id,
        result: "deny",
        deny_message: "Don't create issues in the production project. Use the staging project."
      }
    ]
  )
  ```
</CodeGroup>

## Custom tools

Permission policies do not apply to custom tools. When the agent invokes a custom tool, your application receives an `agent.custom_tool_use` event and is responsible for deciding whether to execute it before sending back a `user.custom_tool_result`. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for the full flow.

## Next steps

<CardGroup cols={2}>
  <Card title="Skills" icon="books" href="https://platform.claude.com/docs/en/managed-agents/skills">
    Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.
  </Card>

  <Card title="Session event stream" icon="lightning" href="https://platform.claude.com/docs/en/managed-agents/events-and-streaming">
    Send events, stream responses, and interrupt or redirect your session mid-execution.
  </Card>
</CardGroup>
