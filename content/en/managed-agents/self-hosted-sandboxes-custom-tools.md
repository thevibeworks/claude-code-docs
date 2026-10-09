---
title: Custom tools in self-hosted sandboxes
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools
description: Serve custom tools from a self-hosted sandbox worker, and wrap an MCP server inside your network as custom tools without running a tunnel.
featureMetadata:
  topic:
    title: Managed Agents
    url: https://platform.claude.com/docs/en/managed-agents/overview
  status: beta
  betaHeader: managed-agents-2026-04-01
---

[Custom tools](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools) are tools your own code executes: the agent emits an `agent.custom_tool_use` event and waits for a matching `user.custom_tool_result`. Your worker can be that code. Because it runs inside your sandbox, the tool reaches the internal services, credentials, and network egress you configured for the sandbox, and nothing more.

The environment key authorizes posting custom tool results, so your Claude API key stays off the worker host.

<Note>
  Serving custom tools requires the SDK worker. The `ant` CLI worker has no way to register a custom tool implementation. In the sandbox-per-session pattern, [run the SDK worker inside the sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#run-the-sdk-worker-inside-the-sandbox).
</Note>

## Serve a custom tool

<Steps>
  <Step title="Declare the tool on the agent">
    Add a `custom` entry to the agent's `tools` whose `name` matches the tool your worker registers. See [Custom tools](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools) for the full declaration shape.

    ```json
    {
      "type": "custom",
      "name": "get_order_status",
      "description": "Look up an order in the internal fulfillment system by order ID.",
      "input_schema": {
        "type": "object",
        "properties": {
          "order_id": { "type": "string", "description": "The order ID" }
        },
        "required": ["order_id"]
      }
    }
    ```
  </Step>

  <Step title="Register the implementation with the worker">
    Pass the tool through the worker's `tools` (go: `ToolsFunc`) factory (see [`EnvironmentWorker`](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#environment-worker)), alongside the built-in toolset:

    <CodeGroup exclude="shell">
      ```python Python
      import asyncio
      import os
      from anthropic import AsyncAnthropic, beta_async_tool
      from anthropic.lib.environments import EnvironmentWorker
      from anthropic.lib.tools.agent_toolset import beta_agent_toolset_20260401


      @beta_async_tool
      async def get_order_status(order_id: str) -> str:
          """Look up an order in the internal fulfillment system by order ID."""
          # Runs on the worker host: call anything the sandbox can reach.
          return f"Order {order_id}: shipped"


      async def main() -> None:
          environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
          environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
          async with AsyncAnthropic(auth_token=environment_key) as client:
              await EnvironmentWorker(
                  client,
                  environment_id=environment_id,
                  environment_key=environment_key,
                  workdir="/workspace",
                  tools=lambda env: [*beta_agent_toolset_20260401(env), get_order_status],
              ).run()


      asyncio.run(main())
      ```

      ```typescript TypeScript
      import Anthropic from "@anthropic-ai/sdk";
      import { EnvironmentWorker } from "@anthropic-ai/sdk/helpers/beta/environments";
      import { betaTool } from "@anthropic-ai/sdk/helpers/beta/json-schema";
      import { betaAgentToolset20260401 } from "@anthropic-ai/sdk/tools/agent-toolset/node";

      const getOrderStatus = betaTool({
        name: "get_order_status",
        description: "Look up an order in the internal fulfillment system by order ID.",
        inputSchema: {
          type: "object",
          properties: { order_id: { type: "string", description: "The order ID" } },
          required: ["order_id"]
        },
        // Runs on the worker host: call anything the sandbox can reach.
        run: async ({ order_id }) => `Order ${order_id}: shipped`
      });

      const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
      const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
      const client = new Anthropic({ authToken: environmentKey });
      const controller = new AbortController();
      process.once("SIGTERM", () => controller.abort());

      await new EnvironmentWorker({
        client,
        environmentId,
        environmentKey,
        workdir: "/workspace",
        signal: controller.signal,
        tools: (ctx) => [...betaAgentToolset20260401(ctx), getOrderStatus]
      }).run();
      ```

      ```csharp C#
      // EnvironmentWorker is not currently available in the C# SDK.
      // To answer custom tool calls directly, see the session event stream.
      ```

      ```go Go
      package main

      import (
      	"context"
      	"log"
      	"os"
      	"os/signal"
      	"syscall"

      	"github.com/anthropics/anthropic-sdk-go"
      	"github.com/anthropics/anthropic-sdk-go/lib/environments"
      	"github.com/anthropics/anthropic-sdk-go/option"
      	"github.com/anthropics/anthropic-sdk-go/toolrunner"
      	"github.com/anthropics/anthropic-sdk-go/tools/agenttoolset"
      )

      type orderStatusInput struct {
      	OrderID string `json:"order_id"`
      }

      func main() {
      	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
      	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

      	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
      	defer stop()

      	getOrderStatus := toolrunner.NewBetaTool(
      		"get_order_status",
      		"Look up an order in the internal fulfillment system by order ID.",
      		anthropic.BetaToolInputSchemaParam{
      			Properties: map[string]any{
      				"order_id": map[string]any{"type": "string", "description": "The order ID"},
      			},
      			Required: []string{"order_id"},
      		},
      		// Runs on the worker host: call anything the sandbox can reach.
      		func(ctx context.Context, input orderStatusInput) (anthropic.BetaToolResultBlockParamContentUnion, error) {
      			return anthropic.BetaToolResultBlockParamContentUnion{
      				OfText: &anthropic.BetaTextBlockParam{Text: "Order " + input.OrderID + ": shipped"},
      			}, nil
      		},
      	)

      	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

      	worker := environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
      		EnvironmentID:  environmentID,
      		EnvironmentKey: environmentKey,
      		Workdir:        "/workspace",
      		ToolsFunc: func(env *agenttoolset.AgentToolContext) []anthropic.BetaTool {
      			return append(agenttoolset.BetaAgentToolset20260401(env), getOrderStatus)
      		},
      	})
      	if err := worker.Run(ctx); err != nil {
      		log.Fatalf("worker: %v", err)
      	}
      }

      ```

      ```java Java
      // EnvironmentWorker is not currently available in the Java SDK.
      // To answer custom tool calls directly, see the session event stream.
      ```

      ```php PHP
      // EnvironmentWorker is not currently available in the PHP SDK.
      // To answer custom tool calls directly, see the session event stream.
      ```

      ```ruby Ruby
      # EnvironmentWorker is not currently available in the Ruby SDK.
      # To answer custom tool calls directly, see the session event stream.
      ```
    </CodeGroup>
  </Step>
</Steps>

The worker answers only the tools registered with it. If a tool is declared on the agent but no worker or client serves it, the session pauses with a `requires_action` stop reason. It stays paused until something posts the result. See [Answer tool calls that pause the session](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#answer-tool-calls-that-pause-the-session) for the event flow.

## Wrap an MCP server as custom tools

The [MCP connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) connects to MCP servers from Anthropic's side. A server must therefore expose an HTTP endpoint that Anthropic can reach, directly or through an [MCP tunnel](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview).

To use a server that only your network can reach, make the worker the MCP client instead and declare the server's tools as custom tools. The MCP server needs no inbound connectivity from outside your network. Anthropic receives the tool definitions you declare on the agent, each call's input, and the result your worker posts back.

At runtime the model calls a wrapped tool like any other custom tool:

1. The agent emits an `agent.custom_tool_use` event.
2. The worker, inside your sandbox, forwards the call over its open MCP session to the server on your network.
3. The worker posts the server's response as the `user.custom_tool_result`.

### Install an MCP SDK

The SDK's [Client-side MCP helpers](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#client-side-mcp-helpers) convert the server's tools into the runnable tools the worker accepts. Install an MCP SDK alongside the Anthropic SDK: `pip install "anthropic[mcp]" "mcp>=1.24"` (python; typescript: `npm install @modelcontextprotocol/sdk`; go: `go get github.com/modelcontextprotocol/go-sdk`).

The examples connect without authentication. To send credentials, configure the `http_client` (typescript: `requestInit`; go: `HTTPClient`) you hand to the MCP transport.

### Declare and serve the tools

<Steps>
  <Step title="Declare the server's tools on the agent">
    List the MCP server's tools and declare each one as a `custom` tool. The MCP `name`, `description`, and `inputSchema` map one to one onto the custom tool's fields. If the server paginates its tool list, declare every page; the worker must list the same pages.

    <CodeGroup exclude="shell">
      ```python Python
      import asyncio
      from typing import Any, cast
      from anthropic import AsyncAnthropic
      from anthropic.types.beta import BetaManagedAgentsCustomToolParams
      from mcp import ClientSession, types
      # Requires mcp >= 1.24, which renamed streamablehttp_client to streamable_http_client.
      from mcp.client.streamable_http import streamable_http_client

      MCP_SERVER_URL = "http://mcp.internal.example.com:8000/mcp"


      def to_custom_tool(tool: types.Tool) -> BetaManagedAgentsCustomToolParams:
          # The MCP fields map one to one onto a custom tool declaration. The cast
          # hands the schema dictionary to the SDK's typed parameter unchanged.
          return {
              "type": "custom",
              "name": tool.name,
              "description": tool.description or tool.name,
              "input_schema": cast(Any, tool.inputSchema),
          }


      async def main() -> None:
          # Run this wherever you create agents, not on the worker host: it
          # authenticates with your Claude API key (ANTHROPIC_API_KEY).
          async with (
              streamable_http_client(MCP_SERVER_URL) as (read, write, _),
              ClientSession(read, write) as mcp_session,
              AsyncAnthropic() as client,
          ):
              await mcp_session.initialize()
              listed = await mcp_session.list_tools()
              agent = await client.beta.agents.create(
                  name="Internal tools agent",
                  model="claude-opus-5-5",
                  tools=[
                      {"type": "agent_toolset_20260401"},
                      *[to_custom_tool(tool) for tool in listed.tools],
                  ],
              )
              print(agent.id)


      asyncio.run(main())
      ```

      ```typescript TypeScript
      import Anthropic from "@anthropic-ai/sdk";
      import { Client } from "@modelcontextprotocol/sdk/client/index.js";
      import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

      const MCP_SERVER_URL = "http://mcp.internal.example.com:8000/mcp";

      // Run this wherever you create agents, not on the worker host: it
      // authenticates with your Claude API key (ANTHROPIC_API_KEY).
      const client = new Anthropic();

      const mcpClient = new Client({ name: "declare-agent-tools", version: "1.0.0" });
      await mcpClient.connect(new StreamableHTTPClientTransport(new URL(MCP_SERVER_URL)));
      const { tools } = await mcpClient.listTools();

      const agent = await client.beta.agents.create({
        name: "Internal tools agent",
        model: "claude-opus-5-5",
        tools: [
          { type: "agent_toolset_20260401" },
          // The MCP fields map one to one onto a custom tool declaration.
          ...tools.map((tool) => ({
            type: "custom" as const,
            name: tool.name,
            description: tool.description || tool.name,
            input_schema: tool.inputSchema
          }))
        ]
      });
      console.log(agent.id);

      await mcpClient.close();
      ```

      ```csharp C#
      // See the Python, TypeScript, and Go tabs. Declaring custom tools from
      // C# works the same way once you list the server's tools with an MCP client.
      ```

      ```go Go
      package main

      import (
      	"context"
      	"encoding/json"
      	"fmt"
      	"log"

      	"github.com/anthropics/anthropic-sdk-go"
      	mcpsdk "github.com/modelcontextprotocol/go-sdk/mcp"
      )

      const mcpServerURL = "http://mcp.internal.example.com:8000/mcp"

      // toCustomTool maps one MCP tool definition onto a custom tool declaration.
      // The fields map one to one: the typed parameter carries `properties` and
      // `required`, and every other JSON Schema keyword the server emits travels in
      // ExtraFields so the declared schema matches the server's schema.
      func toCustomTool(tool *mcpsdk.Tool) (anthropic.BetaAgentNewParamsToolUnion, error) {
      	raw, err := json.Marshal(tool.InputSchema)
      	if err != nil {
      		return anthropic.BetaAgentNewParamsToolUnion{}, err
      	}
      	var schema map[string]any
      	if err := json.Unmarshal(raw, &schema); err != nil {
      		return anthropic.BetaAgentNewParamsToolUnion{}, err
      	}

      	inputSchema := anthropic.BetaManagedAgentsCustomToolInputSchemaParam{ExtraFields: map[string]any{}}
      	for keyword, value := range schema {
      		switch keyword {
      		case "type":
      			// The parameter type always marshals "type": "object".
      		case "properties":
      			properties, _ := value.(map[string]any)
      			inputSchema.Properties = properties
      		case "required":
      			entries, _ := value.([]any)
      			for _, entry := range entries {
      				if name, isString := entry.(string); isString {
      					inputSchema.Required = append(inputSchema.Required, name)
      				}
      			}
      		default:
      			inputSchema.ExtraFields[keyword] = value
      		}
      	}

      	description := tool.Description
      	if description == "" {
      		description = tool.Name
      	}
      	return anthropic.BetaAgentNewParamsToolUnion{
      		OfCustom: &anthropic.BetaManagedAgentsCustomToolParams{
      			Type:        anthropic.BetaManagedAgentsCustomToolParamsTypeCustom,
      			Name:        tool.Name,
      			Description: description,
      			InputSchema: inputSchema,
      		},
      	}, nil
      }

      func main() {
      	ctx := context.Background()

      	// Run this wherever you create agents, not on the worker host: it
      	// authenticates with your Claude API key (ANTHROPIC_API_KEY).
      	client := anthropic.NewClient()

      	mcpClient := mcpsdk.NewClient(&mcpsdk.Implementation{Name: "declare-agent-tools", Version: "1.0.0"}, nil)
      	session, err := mcpClient.Connect(ctx, &mcpsdk.StreamableClientTransport{Endpoint: mcpServerURL}, nil)
      	if err != nil {
      		log.Fatalf("connect to MCP server: %v", err)
      	}
      	defer session.Close()

      	listed, err := session.ListTools(ctx, nil)
      	if err != nil {
      		log.Fatalf("list MCP tools: %v", err)
      	}

      	tools := []anthropic.BetaAgentNewParamsToolUnion{
      		{OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
      			Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
      		}},
      	}
      	for _, tool := range listed.Tools {
      		custom, err := toCustomTool(tool)
      		if err != nil {
      			log.Fatalf("convert MCP tool %s: %v", tool.Name, err)
      		}
      		tools = append(tools, custom)
      	}

      	agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
      		Name:  "Internal tools agent",
      		Model: anthropic.BetaManagedAgentsModelConfigParams{ID: anthropic.BetaManagedAgentsModelClaudeOpus5_5},
      		Tools: tools,
      	})
      	if err != nil {
      		log.Fatalf("create agent: %v", err)
      	}
      	fmt.Println(agent.ID)
      }

      ```

      ```java Java
      // See the Python, TypeScript, and Go tabs. Declaring custom tools from
      // Java works the same way once you list the server's tools with an MCP client.
      ```

      ```php PHP
      // See the Python, TypeScript, and Go tabs. Declaring custom tools from
      // PHP works the same way once you list the server's tools with an MCP client.
      ```

      ```ruby Ruby
      # See the Python, TypeScript, and Go tabs. Declaring custom tools from
      # Ruby works the same way once you list the server's tools with an MCP client.
      ```
    </CodeGroup>
  </Step>

  <Step title="Serve the tools from the worker">
    Connect to the same MCP server at startup, convert its tools with `async_mcp_tool` (python; typescript: `mcpTools`; go: `mcp.NewBetaTools`), and register them alongside `beta_agent_toolset_20260401` (python; typescript: `betaAgentToolset20260401`; go: `agenttoolset.BetaAgentToolset20260401`). Keep one MCP session open for the life of the worker.

    <CodeGroup exclude="shell">
      ```python Python
      import asyncio
      import os
      from datetime import timedelta
      from anthropic import AsyncAnthropic
      from anthropic.lib.environments import EnvironmentWorker
      from anthropic.lib.tools.agent_toolset import beta_agent_toolset_20260401
      from anthropic.lib.tools.mcp import async_mcp_tool
      from mcp import ClientSession
      # Requires mcp >= 1.24, which renamed streamablehttp_client to streamable_http_client.
      from mcp.client.streamable_http import streamable_http_client

      MCP_SERVER_URL = "http://mcp.internal.example.com:8000/mcp"


      async def main() -> None:
          environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
          environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
          # Connect to the MCP server once at startup and keep the session open for
          # the life of the worker. The timeout turns a hung tool call into an error
          # result instead of a stalled call.
          async with (
              streamable_http_client(MCP_SERVER_URL) as (read, write, _),
              ClientSession(read, write, read_timeout_seconds=timedelta(seconds=60)) as mcp_session,
              AsyncAnthropic(auth_token=environment_key) as client,
          ):
              await mcp_session.initialize()
              listed = await mcp_session.list_tools()
              mcp_tools = [async_mcp_tool(tool, mcp_session) for tool in listed.tools]
              await EnvironmentWorker(
                  client,
                  environment_id=environment_id,
                  environment_key=environment_key,
                  workdir="/workspace",
                  tools=lambda env: [*beta_agent_toolset_20260401(env), *mcp_tools],
              ).run()


      asyncio.run(main())
      ```

      ```typescript TypeScript
      import Anthropic from "@anthropic-ai/sdk";
      import { EnvironmentWorker } from "@anthropic-ai/sdk/helpers/beta/environments";
      import {
        mcpTools,
        type MCPCallToolResultLike,
        type MCPClientLike
      } from "@anthropic-ai/sdk/helpers/beta/mcp";
      import { betaAgentToolset20260401 } from "@anthropic-ai/sdk/tools/agent-toolset/node";
      import { Client } from "@modelcontextprotocol/sdk/client/index.js";
      import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

      const MCP_SERVER_URL = "http://mcp.internal.example.com:8000/mcp";

      const environmentKey = process.env.ANTHROPIC_ENVIRONMENT_KEY!;
      const environmentId = process.env.ANTHROPIC_ENVIRONMENT_ID!;
      const client = new Anthropic({ authToken: environmentKey });
      const controller = new AbortController();
      process.once("SIGTERM", () => controller.abort());

      // Connect to the MCP server once at startup and keep the connection open for
      // the life of the worker.
      const mcpClient = new Client({ name: "sandbox-worker", version: "1.0.0" });
      await mcpClient.connect(new StreamableHTTPClientTransport(new URL(MCP_SERVER_URL)));
      const { tools } = await mcpClient.listTools();

      // The MCP SDK's callTool return type still includes a legacy result shape that
      // mcpTools does not accept; narrow it. Drop this once MCPClientLike widens.
      const mcpClientForTools: MCPClientLike = {
        callTool: (params) => mcpClient.callTool(params) as Promise<MCPCallToolResultLike>
      };

      await new EnvironmentWorker({
        client,
        environmentId,
        environmentKey,
        workdir: "/workspace",
        signal: controller.signal,
        tools: (ctx) => [...betaAgentToolset20260401(ctx), ...mcpTools(tools, mcpClientForTools)]
      }).run();
      ```

      ```csharp C#
      // EnvironmentWorker is not currently available in the C# SDK.
      ```

      ```go Go
      package main

      import (
      	"context"
      	"log"
      	"os"
      	"os/signal"
      	"syscall"

      	"github.com/anthropics/anthropic-sdk-go"
      	"github.com/anthropics/anthropic-sdk-go/lib/environments"
      	"github.com/anthropics/anthropic-sdk-go/mcp"
      	"github.com/anthropics/anthropic-sdk-go/option"
      	"github.com/anthropics/anthropic-sdk-go/tools/agenttoolset"
      	mcpsdk "github.com/modelcontextprotocol/go-sdk/mcp"
      )

      const mcpServerURL = "http://mcp.internal.example.com:8000/mcp"

      func main() {
      	environmentKey := os.Getenv("ANTHROPIC_ENVIRONMENT_KEY")
      	environmentID := os.Getenv("ANTHROPIC_ENVIRONMENT_ID")

      	ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
      	defer stop()

      	client := anthropic.NewClient(option.WithAuthToken(environmentKey))

      	// Connect to the MCP server once at startup and keep the session open for
      	// the life of the worker.
      	mcpClient := mcpsdk.NewClient(&mcpsdk.Implementation{Name: "sandbox-worker", Version: "1.0.0"}, nil)
      	session, err := mcpClient.Connect(ctx, &mcpsdk.StreamableClientTransport{Endpoint: mcpServerURL}, nil)
      	if err != nil {
      		log.Fatalf("connect to MCP server: %v", err)
      	}
      	defer session.Close()

      	listed, err := session.ListTools(ctx, nil)
      	if err != nil {
      		log.Fatalf("list MCP tools: %v", err)
      	}
      	mcpTools, err := mcp.NewBetaTools(listed.Tools, session)
      	if err != nil {
      		log.Fatalf("convert MCP tools: %v", err)
      	}

      	worker := environments.NewEnvironmentWorker(client, environments.EnvironmentWorkerOptions{
      		EnvironmentID:  environmentID,
      		EnvironmentKey: environmentKey,
      		Workdir:        "/workspace",
      		ToolsFunc: func(env *agenttoolset.AgentToolContext) []anthropic.BetaTool {
      			return append(agenttoolset.BetaAgentToolset20260401(env), mcpTools...)
      		},
      	})
      	if err := worker.Run(ctx); err != nil {
      		log.Fatalf("worker: %v", err)
      	}
      }

      ```

      ```java Java
      // EnvironmentWorker is not currently available in the Java SDK.
      ```

      ```php PHP
      // EnvironmentWorker is not currently available in the PHP SDK.
      ```

      ```ruby Ruby
      # EnvironmentWorker is not currently available in the Ruby SDK.
      ```
    </CodeGroup>
  </Step>
</Steps>

## Limits and behavior

### Tools are declared, not discovered at runtime

The worker lists the MCP server's tools once at startup and cannot add tools to a running session. When the server's tools change:

1. Declare them again, on the agent or on an idle session through [Updating the agent configuration](https://platform.claude.com/docs/en/managed-agents/session-operations#updating-the-agent-configuration).
2. Restart the worker.

### Declarations must fit the Managed Agents API

The MCP helpers keep the server's names and descriptions, and most schemas pass through unchanged. Rename, trim, or inline where a declaration breaks one of these rules:

| Field                     | Rule                                                                                                                                                                                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                    | Unique per agent. Letters, digits, underscores, and hyphens, 1–128 characters. Cannot match a built-in agent tool such as `bash` or `read`, or use the reserved `mcp__` prefix or `ant__` prefix.                                                                                             |
| `description`             | Required and non-empty.                                                                                                                                                                                                                                                                       |
| `input_schema`            | Accepts the JSON Schema keywords MCP servers commonly emit, such as `additionalProperties` and `title`. Rejects reference keywords such as `$ref` anywhere, and top-level `oneOf`, `anyOf`, and `allOf`. Property names use letters, digits, underscores, dots, and hyphens, 1–64 characters. |
| The agent's `tools` array | At most 128 entries. Each wrapped tool is one entry, and the built-in toolset is one more.                                                                                                                                                                                                    |

Two cases need extra work:

* **Two servers expose the same tool name:** Define the wrapper yourself under a prefixed name and have it call the server's original tool name.
* **A generator such as pydantic factors schemas into `$defs`:** Inline those schemas before you declare the tool.

### Tool failures surface as error tool results

When the MCP server reports a tool error, the worker posts an error tool result the model can react to. MCP content with no tool result equivalent, such as audio blocks and resource links, also surfaces as an error.

Set a timeout on the MCP client for a faster and clearer failure, as the Python worker example does with `read_timeout_seconds`. See [A wrapped MCP tool call hangs](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#a-wrapped-mcp-tool-call-hangs) for what happens without one.

### Wrap only servers you operate or trust

A wrapped tool's name, description, and results enter the model's context like any other tool's. They are untrusted input that can influence what the agent does with its other tools, including `bash` on the worker host. Declare only the tools you intend the agent to use.

### Permission policies do not apply

[Permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies#custom-tools) govern the built-in and MCP toolsets. The worker executes every wrapped tool call the model makes, so put any approval step in your own tool code.
