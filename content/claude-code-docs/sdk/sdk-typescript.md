# TypeScript

> Build custom AI agents with the Claude Code TypeScript SDK

## Prerequisites

* Node.js 18+

## Installation

Install `@anthropic-ai/claude-code` from NPM:

```bash
npm install -g @anthropic-ai/claude-code
```

<Note>
  To view the TypeScript SDK source code, visit the [`@anthropic-ai/claude-code` page on NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code?activeTab=code).
</Note>

## Basic usage

The primary interface via the TypeScript SDK is the `query` function, which returns an async iterator that streams messages as they arrive:

```ts
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Analyze system performance",
  abortController: new AbortController(),
  options: {
    maxTurns: 5,
    systemPrompt: "You are a performance engineer",
    allowedTools: ["Bash", "Read", "WebSearch"]
  }
})) {
  if (message.type === "result") {
    console.log(message.result);
  }
}
```

## Configuration options

| Argument                     | Type                              | Description                                      | Default                                                                              |
| :--------------------------- | :-------------------------------- | :----------------------------------------------- | :----------------------------------------------------------------------------------- |
| `abortController`            | `AbortController`                 | Abort controller for cancelling operations       | `new AbortController()`                                                              |
| `additionalDirectories`      | `string[]`                        | Additional directories to include in the session | `undefined`                                                                          |
| `allowedTools`               | `string[]`                        | List of tools that Claude is allowed to use      | All tools enabled by default                                                         |
| `appendSystemPrompt`         | `string`                          | Text to append to the default system prompt      | `undefined`                                                                          |
| `canUseTool`                 | `CanUseTool`                      | Custom permission function for tool usage        | `undefined`                                                                          |
| `continue`                   | `boolean`                         | Continue the most recent session                 | `false`                                                                              |
| `customSystemPrompt`         | `string`                          | Replace the default system prompt entirely       | `undefined`                                                                          |
| `cwd`                        | `string`                          | Current working directory                        | `process.cwd()`                                                                      |
| `disallowedTools`            | `string[]`                        | List of tools that Claude is not allowed to use  | `undefined`                                                                          |
| `env`                        | `Dict<string>`                    | Environment variables to set                     | `undefined`                                                                          |
| `executable`                 | `'bun' \| 'deno' \| 'node'`       | Which JavaScript runtime to use                  | `node` when running with Node.js, `bun` when running with Bun                        |
| `executableArgs`             | `string[]`                        | Arguments to pass to the executable              | `[]`                                                                                 |
| `fallbackModel`              | `string`                          | Model to use if primary model fails              | `undefined`                                                                          |
| `maxThinkingTokens`          | `number`                          | Maximum tokens for Claude's thinking process     | `undefined`                                                                          |
| `maxTurns`                   | `number`                          | Maximum number of conversation turns             | `undefined`                                                                          |
| `mcpServers`                 | `Record<string, McpServerConfig>` | MCP server configurations                        | `undefined`                                                                          |
| `model`                      | `string`                          | Claude model to use                              | Uses default from CLI configuration                                                  |
| `pathToClaudeCodeExecutable` | `string`                          | Path to the Claude Code executable               | Executable that ships with `@anthropic-ai/claude-code`                               |
| `permissionMode`             | `PermissionMode`                  | Permission mode for the session                  | `"default"` (options: `"default"`, `"acceptEdits"`, `"bypassPermissions"`, `"plan"`) |
| `permissionPromptToolName`   | `string`                          | Name of MCP tool for permission prompts          | `undefined`                                                                          |
| `resume`                     | `string`                          | Session ID to resume                             | `undefined`                                                                          |
| `stderr`                     | `(data: string) => void`          | Callback for stderr output                       | `undefined`                                                                          |
| `strictMcpConfig`            | `boolean`                         | Enforce strict MCP configuration validation      | `undefined`                                                                          |

## Multi-turn conversations

For multi-turn conversations, you have two options.

You can generate responses and resume them, or you can use streaming input mode which accepts an async/generator for an array of messages. For now, streaming input mode is the only way to attach images via messages.

### Resume with session management

```ts
import { query } from "@anthropic-ai/claude-code";

// Continue most recent conversation
for await (const message of query({
  prompt: "Now refactor this for better performance",
  options: { continue: true }
})) {
  if (message.type === "result") console.log(message.result);
}

// Resume specific session
for await (const message of query({
  prompt: "Update the tests",
  options: {
    resume: "550e8400-e29b-41d4-a716-446655440000",
    maxTurns: 3
  }
})) {
  if (message.type === "result") console.log(message.result);
}
```

## Streaming input mode

Streaming input mode allows you to provide messages as an async iterable instead of a single string. This enables multi-turn conversations, image attachments, and dynamic message generation:

```ts
import { query } from "@anthropic-ai/claude-code";

// Create an async generator for streaming messages
async function* generateMessages() {
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: "Start analyzing this codebase"
    }
  };
  
  // Wait for some condition or user input
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: "Now focus on the authentication module"
    }
  };
}

// Use streaming input
for await (const message of query({
  prompt: generateMessages(),
  options: {
    maxTurns: 5,
    allowedTools: ["Read", "Grep", "Bash"]
  }
})) {
  if (message.type === "result") {
    console.log(message.result);
  }
}
```

### Streaming input with images

Streaming input mode is the only way to attach images via messages:

```ts
import { query } from "@anthropic-ai/claude-code";
import { readFileSync } from "fs";

async function* messagesWithImage() {
  // Send an image with text
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: [
        {
          type: "text",
          text: "Analyze this screenshot and suggest improvements"
        },
        {
          type: "image",
          source: {
            type: "base64",
            media_type: "image/png",
            data: readFileSync("screenshot.png", "base64")
          }
        }
      ]
    }
  };
}

for await (const message of query({
  prompt: messagesWithImage()
})) {
  if (message.type === "result") console.log(message.result);
}
```

## Custom system prompts

System prompts define your agent's role, expertise, and behavior:

```ts
import { query } from "@anthropic-ai/claude-code";

// SRE incident response agent
for await (const message of query({
  prompt: "API is down, investigate",
  options: {
    systemPrompt: "You are an SRE expert. Diagnose issues systematically and provide actionable solutions.",
    maxTurns: 3
  }
})) {
  if (message.type === "result") console.log(message.result);
}

// Append to default system prompt
for await (const message of query({
  prompt: "Refactor this function",
  options: {
    appendSystemPrompt: "Always include comprehensive error handling and unit tests.",
    maxTurns: 2
  }
})) {
  if (message.type === "result") console.log(message.result);
}
```

## Custom tools via MCP

The Model Context Protocol (MCP) lets you give your agents custom tools and capabilities:

```ts
import { query } from "@anthropic-ai/claude-code";

// SRE agent with monitoring tools
for await (const message of query({
  prompt: "Investigate the payment service outage",
  options: {
    mcpConfig: "sre-tools.json",
    allowedTools: ["mcp__datadog", "mcp__pagerduty", "mcp__kubernetes"],
    systemPrompt: "You are an SRE. Use monitoring data to diagnose issues.",
    maxTurns: 4
  }
})) {
  if (message.type === "result") console.log(message.result);
}
```

## Custom tools using MCPs

You can implement custom tools using MCPs, for example here is how you can create a custom permission handling tool.

```ts
const server = new McpServer({
  name: "Test permission prompt MCP Server",
  version: "0.0.1",
});

server.tool(
  "approval_prompt",
  'Simulate a permission check - approve if the input contains "allow", otherwise deny',
  {
    tool_name: z.string().describe("The name of the tool requesting permission"),
    input: z.object({}).passthrough().describe("The input for the tool"),
    tool_use_id: z.string().optional().describe("The unique tool use request ID"),
  },
  async ({ tool_name, input }) => {
    return {
      content: [
        {
          type: "text",
          text: JSON.stringify(
            JSON.stringify(input).includes("allow")
              ? {
                  behavior: "allow",
                  updatedInput: input,
                }
              : {
                  behavior: "deny",
                  message: "Permission denied by test approval_prompt tool",
                }
          ),
        },
      ],
    };
  }
);

// Use in SDK
import { query } from "@anthropic-ai/claude-code";

for await (const message of query({
  prompt: "Analyze the codebase",
  options: {
    permissionPromptTool: "mcp__test-server__approval_prompt",
    mcpConfig: "my-config.json",
    allowedTools: ["Read", "Grep"]
  }
})) {
  if (message.type === "result") console.log(message.result);
}
```

## Output formats

### Text output (default)

```ts
// Default text output
for await (const message of query({
  prompt: "Explain file src/components/Header.tsx"
})) {
  if (message.type === "result") {
    console.log(message.result);
    // Output: This is a React component showing...
  }
}
```

### JSON output

```ts
// Collect all messages for JSON-like access
const messages = [];
for await (const message of query({
  prompt: "How does the data layer work?"
})) {
  messages.push(message);
}

// Access result message with metadata
const result = messages.find(m => m.type === "result");
console.log({
  result: result.result,
  cost: result.total_cost_usd,
  duration: result.duration_ms
});
```

## Input formats

```ts
// Direct prompt
for await (const message of query({
  prompt: "Explain this code"
})) {
  if (message.type === "result") console.log(message.result);
}

// From variable
const userInput = "Explain this code";
for await (const message of query({ prompt: userInput })) {
  if (message.type === "result") console.log(message.result);
}
```

## Agent integration examples

### SRE incident response agent

```ts
import { query } from "@anthropic-ai/claude-code";

// Automated incident response agent
async function investigateIncident(
  incidentDescription: string,
  severity = "medium"
) {
  const messages = [];

  for await (const message of query({
    prompt: `Incident: ${incidentDescription} (Severity: ${severity})`,
    options: {
      systemPrompt: "You are an SRE expert. Diagnose the issue, assess impact, and provide immediate action items.",
      maxTurns: 6,
      allowedTools: ["Bash", "Read", "WebSearch", "mcp__datadog"],
      mcpConfig: "monitoring-tools.json"
    }
  })) {
    messages.push(message);
  }

  return messages.find(m => m.type === "result");
}

// Usage
const result = await investigateIncident("Payment API returning 500 errors", "high");
console.log(result.result);
```

### Automated security review

```ts
import { query } from "@anthropic-ai/claude-code";
import { execSync } from "child_process";

async function auditPR(prNumber: number) {
  // Get PR diff
  const prDiff = execSync(`gh pr diff ${prNumber}`, { encoding: 'utf8' });

  const messages = [];
  for await (const message of query({
    prompt: prDiff,
    options: {
      systemPrompt: "You are a security engineer. Review this PR for vulnerabilities, insecure patterns, and compliance issues.",
      maxTurns: 3,
      allowedTools: ["Read", "Grep", "WebSearch"]
    }
  })) {
    messages.push(message);
  }

  return messages.find(m => m.type === "result");
}

// Usage
const report = await auditPR(123);
console.log(JSON.stringify(report, null, 2));
```

### Multi-turn legal assistant

```ts
import { query } from "@anthropic-ai/claude-code";

async function legalReview() {
  // Start legal review session
  let sessionId: string;

  for await (const message of query({
    prompt: "Start legal review session",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      sessionId = message.session_id;
    }
  }

  // Multi-step review using same session
  const steps = [
    "Review contract.pdf for liability clauses",
    "Check compliance with GDPR requirements",
    "Generate executive summary of risks"
  ];

  for (const step of steps) {
    for await (const message of query({
      prompt: step,
      options: { resume: sessionId, maxTurns: 2 }
    })) {
      if (message.type === "result") {
        console.log(`Step: ${step}`);
        console.log(message.result);
      }
    }
  }
}
```

## Message schema

Messages returned from the JSON API are strictly typed according to the following schema:

```ts
type SDKMessage =
  // An assistant message
  | {
      type: "assistant";
      uuid: string;
      session_id: string;
      message: Message; // from Anthropic SDK
      parent_tool_use_id: string | null;
    }

  // A user message (input)
  | {
      type: "user";
      uuid?: string;
      session_id: string;
      message: MessageParam; // from Anthropic SDK
      parent_tool_use_id: string | null;
    }

  // A user message (output/replay with required UUID)
  | {
      type: "user";
      uuid: string;
      session_id: string;
      message: MessageParam; // from Anthropic SDK
      parent_tool_use_id: string | null;
    }

  // Emitted as the last message on success
  | {
      type: "result";
      subtype: "success";
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      result: string;
      total_cost_usd: number;
      usage: Usage;
      permission_denials: SDKPermissionDenial[];
    }

  // Emitted as the last message on error or max turns
  | {
      type: "result";
      subtype: "error_max_turns" | "error_during_execution";
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      total_cost_usd: number;
      usage: Usage;
      permission_denials: SDKPermissionDenial[];
    }

  // Emitted as the first message at the start of a conversation
  | {
      type: "system";
      subtype: "init";
      uuid: UUID;
      session_id: string;
      apiKeySource: "user" | "project" | "org" | "temporary";
      cwd: string;
      tools: string[];
      mcp_servers: {
        name: string;
        status: string;
      }[];
      model: string;
      permissionMode: "default" | "acceptEdits" | "bypassPermissions" | "plan";
      slash_commands: string[];
      output_style: string;
    };

  type SDKPermissionDenial = {
    tool_name: string;
    tool_use_id: string;
    tool_input: Record<string, unknown>;
  }

```

Additional supporting types:

`Message`, `MessageParam`, and `Usage` types are available in the Anthropic [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript).

## Related resources

* [CLI usage and controls](/en/docs/claude-code/cli-reference) - Complete CLI documentation
* [GitHub Actions integration](/en/docs/claude-code/github-actions) - Automate your GitHub workflow with Claude
* [Common workflows](/en/docs/claude-code/common-workflows) - Step-by-step guides for common use cases
