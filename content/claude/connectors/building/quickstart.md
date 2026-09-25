> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build your first MCP server for Claude

> Build a minimal MCP server with one tool in JavaScript, run it on your machine, and connect it to Claude Code so Claude calls your tool.

An MCP server is a program that gives Claude tools it can call, and people who use Claude see it as a connector. In this quickstart you write one in about 50 lines of JavaScript with no build step: a server with a single `roll_dice` tool that runs on your machine, which you then connect to [Claude Code](https://code.claude.com/docs/en/setup), Anthropic's command-line coding tool, and watch Claude call. At the end you have a working server you understand line by line, ready to grow into your own product's tools, wrap in a [plugin](/docs/plugins/quickstart), or host for people on claude.ai.

This quickstart is for developers who haven't built an MCP server before and want to see every piece working before they add authentication, hosting, and real tools.

<Note>
  * If you already have a server and want to know what Claude's client supports, see [Build an MCP server for Claude](/docs/connectors/building/index)
  * If your server is running and you want to try it in Claude, see [Test your connector](/docs/connectors/building/testing)
  * If you want to package skills and an existing connector rather than write a server, see [Build your first plugin](/docs/plugins/quickstart)
</Note>

## Before you begin

Check that you have each of these:

* **Node.js 18 or later**: run `node --version` to check. The steps on this page were verified with Node.js 22
* **npm**: included with Node.js
* **Claude Code**: [install Claude Code](https://code.claude.com/docs/en/setup) and sign in. You use it in the last part to connect to the server and call the tool, and `claude -p` needs a signed-in account to send the prompt
* **Two terminal windows**: one keeps the server running while you run commands in the other

## Create the project

The project is a folder with a `package.json` and two dependencies: the [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk), which also works from plain JavaScript, and `zod`, which the SDK uses to describe tool inputs.

<Steps>
  <Step title="Make a folder for the server">
    In your terminal, create a folder named `mcp-quickstart` and move into it. Every later command on this page runs from this folder:

    ```bash theme={null}
    mkdir mcp-quickstart
    cd mcp-quickstart
    ```
  </Step>

  <Step title="Create package.json">
    Create a default `package.json`, then set `"type": "module"` in it so Node.js treats the project's files as ES modules:

    ```bash theme={null}
    npm init -y
    npm pkg set type=module
    ```
  </Step>

  <Step title="Install the SDK">
    Install the SDK and `zod`. You don't install a web framework separately, because the SDK depends on Express and gives you a ready-made app for it:

    ```bash theme={null}
    npm install @modelcontextprotocol/sdk zod
    ```

    To confirm what installed, run `npm ls --depth=0`. The output lists the two packages and their versions:

    ```text theme={null}
    mcp-quickstart@1.0.0 /path/to/mcp-quickstart
    +-- @modelcontextprotocol/sdk@1.30.1
    `-- zod@4.6.5
    ```

    This page was verified with those versions.
  </Step>
</Steps>

## Write the server

The whole server is one file. Create `server.mjs` in the `mcp-quickstart` folder and paste in the code below.

The highlighted lines matter most: the `McpServer` that Claude connects to, the `registerTool` call that describes `roll_dice` and its inputs, and the `/mcp` route that receives each request over Streamable HTTP.

```js server.mjs {7,10-19,31-38} theme={null}
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
import { createMcpExpressApp } from '@modelcontextprotocol/sdk/server/express.js';
import { z } from 'zod';

function buildServer() {
  const server = new McpServer({ name: 'quickstart-server', version: '1.0.0' }); // the name Claude sees

  // One tool: its name, the description Claude reads to decide when to call it, and its inputs.
  server.registerTool(
    'roll_dice',
    {
      title: 'Roll dice',
      description: 'Roll `count` dice with `sides` sides each. Returns each roll and the total.',
      inputSchema: {
        sides: z.number().int().min(2).max(100).describe('Number of sides per die (2-100)'),
        count: z.number().int().min(1).max(10).default(1).describe('How many dice to roll (1-10)'),
      },
    },
    // Runs when Claude calls the tool. The text you return is what Claude reads.
    async ({ sides, count }) => {
      const rolls = Array.from({ length: count }, () => 1 + Math.floor(Math.random() * sides));
      const total = rolls.reduce((a, b) => a + b, 0);
      return { content: [{ type: 'text', text: `Rolled ${count}d${sides}: [${rolls.join(', ')}] total=${total}` }] };
    },
  );
  return server;
}

// Streamable HTTP: every MCP message arrives as a POST to /mcp. Stateless, so each request gets a fresh server.
const app = createMcpExpressApp(); // Express app with JSON parsing and localhost protection built in
app.post('/mcp', async (req, res) => {
  const server = buildServer();
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined }); // undefined = no sessions
  res.on('close', () => { transport.close(); server.close(); });
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});
const notAllowed = (req, res) => res.status(405).json({ jsonrpc: '2.0', error: { code: -32000, message: 'Method not allowed.' }, id: null });
app.get('/mcp', notAllowed);
app.delete('/mcp', notAllowed);

const PORT = Number(process.env.PORT ?? 3000);
app.listen(PORT, '127.0.0.1', (err) => { // Express 5 reports a taken port here instead of throwing
  if (err) { console.error(`failed to listen on ${PORT}: ${err.message}`); process.exit(1); }
  console.log(`quickstart-server listening on http://localhost:${PORT}/mcp`);
});
```

Each part of the file has one job:

* **`McpServer`**: the object that speaks MCP. Its `name` and `version` are what a client sees when it connects
* **`registerTool`**: adds `roll_dice`. A tool is a function your server offers to Claude, and Claude decides when to call it from the `description`. The `inputSchema` tells the client that `sides` is a whole number from 2 to 100 and that `count` is optional and defaults to 1
* **The handler**: rolls the dice and returns one text block. Whatever you put in `content` is the tool result Claude reads
* **The `/mcp` route**: the SDK's Express app listens on `127.0.0.1:3000`, and each POST to `/mcp` is one MCP request. The server keeps no session between requests, which is the simplest shape and enough for tools like this one
* **The `listen` callback**: prints the address when the server is up, or the reason and exits if the port is already in use

## Run and test the server

Before you involve Claude, start the server and send it MCP requests yourself with `curl`, so you know it works on its own.

<Steps>
  <Step title="Start the server">
    In your first terminal, from the `mcp-quickstart` folder, start the server:

    ```bash theme={null}
    node server.mjs
    ```

    It prints the address it's listening on and keeps running:

    ```text theme={null}
    quickstart-server listening on http://localhost:3000/mcp
    ```

    Leave this terminal open. If you see `failed to listen on 3000` instead, another program is using the port. Stop that program and run the command again.
  </Step>

  <Step title="List the server's tools">
    In your second terminal, ask the server what tools it has. This is the same `tools/list` request Claude sends when it connects. The `Accept` header is required, and the server answers `406 Not Acceptable` without it:

    ```bash theme={null}
    curl -sS -X POST http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
    ```

    The reply is one server-sent event whose `data` line lists `roll_dice` with the title, description, and input schema you wrote. The `inputSchema` object is shortened to `...` here:

    ```text theme={null}
    event: message
    data: {"result":{"tools":[{"name":"roll_dice","title":"Roll dice","description":"Roll `count` dice with `sides` sides each. Returns each roll and the total.","inputSchema":{...},"execution":{"taskSupport":"forbidden"}}]},"jsonrpc":"2.0","id":2}
    ```
  </Step>

  <Step title="Call the tool">
    Call `roll_dice` directly with three 20-sided dice, which is the `tools/call` request Claude sends when it uses the tool:

    ```bash theme={null}
    curl -sS -X POST http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"roll_dice","arguments":{"sides":20,"count":3}}}'
    ```

    The `data` line carries the text your handler returned, with your own random rolls:

    ```text theme={null}
    event: message
    data: {"result":{"content":[{"type":"text","text":"Rolled 3d20: [16, 10, 20] total=46"}]},"jsonrpc":"2.0","id":3}
    ```
  </Step>
</Steps>

## Connect the server to Claude Code

With the server answering on its own, register it with Claude Code and have Claude call the tool from a prompt. Run these commands in your second terminal from the `mcp-quickstart` folder, because `claude mcp add` saves the server for the current project folder by default, and Claude Code only sees it when you run from that same folder.

<Steps>
  <Step title="Add the server to Claude Code">
    Register the server under the name `quickstart`, with the HTTP transport and the local URL:

    ```bash theme={null}
    claude mcp add --transport http quickstart http://localhost:3000/mcp
    ```

    Claude Code confirms where it saved the entry:

    ```text theme={null}
    Added HTTP MCP server quickstart with URL: http://localhost:3000/mcp to local config
    ```
  </Step>

  <Step title="Check the connection">
    List your servers. Claude Code connects to each one to check its health:

    ```bash theme={null}
    claude mcp list
    ```

    A working server shows as connected:

    ```text theme={null}
    Checking MCP server health…

    quickstart: http://localhost:3000/mcp (HTTP) - ✔ Connected
    ```

    If it shows an error instead, check that `node server.mjs` is still running in the first terminal.
  </Step>

  <Step title="Ask Claude to roll dice">
    Send Claude one prompt with [`claude -p`](https://code.claude.com/docs/en/headless), which runs a single prompt without opening an interactive session and prints the answer. Claude Code names MCP tools `mcp__<server>__<tool>`, so your tool is `mcp__quickstart__roll_dice`, and `--allowedTools` lets Claude call it without stopping to ask you:

    ```bash theme={null}
    claude -p "Roll three 20-sided dice using the quickstart server and tell me each roll and the total." \
      --allowedTools "mcp__quickstart__roll_dice"
    ```

    Claude calls your server and reports the rolls it got back:

    ```text theme={null}
    Rolled 3d20 via the quickstart server:

    - Roll 1: **12**
    - Roll 2: **4**
    - Roll 3: **5**

    **Total: 21**
    ```
  </Step>

  <Step title="Confirm the tool ran">
    To see the tool call itself rather than Claude's summary of it, run the same prompt with streaming JSON output. `--output-format stream-json` needs `--verbose` alongside it:

    ```bash theme={null}
    claude -p "Roll three 20-sided dice using the quickstart server and tell me each roll and the total." \
      --allowedTools "mcp__quickstart__roll_dice" \
      --output-format stream-json --verbose
    ```

    The output is one JSON object per line, and other tool calls can appear before yours. Look for the `tool_use` block whose `name` is `mcp__quickstart__roll_dice`, carrying the arguments Claude chose, and the `tool_result` block after it carrying your server's text, shown here with the surrounding fields removed:

    ```text theme={null}
    {"type":"tool_use","name":"mcp__quickstart__roll_dice","input":{"count":3,"sides":20}, ...}
    {"type":"tool_result","content":[{"type":"text","text":"Rolled 3d20: [9, 14, 5] total=28"}], ...}
    ```
  </Step>
</Steps>

In an interactive `claude` session you can ask the same thing in your own words. Without `--allowedTools`, Claude Code asks for your permission before it calls `roll_dice`.

## Put the server in front of claude.ai users

Claude Code reached your server because both run on your machine. When someone adds a connector by URL on claude.ai, in the Claude desktop and mobile apps, or in Cowork, Claude connects to it from Anthropic's infrastructure over the internet, so a `localhost` address isn't reachable from there. To use this server on those surfaces, you host it at a public HTTPS URL and people add that URL as a connector.

Once the server has a public URL, these pages cover each step:

* [Add a connector by URL](/docs/connectors/custom/add-unlisted#add-a-connector-by-url): add the server to your own Claude account as a custom connector
* [Test in Claude as a custom connector](/docs/connectors/building/testing#test-in-claude-as-a-custom-connector): check the connection, the tool list, and a real call from a chat, including how to expose a server that's still on your machine through a tunnel
* [Authentication for connectors](/docs/connectors/building/authentication): add sign-in before real users connect, because this quickstart server lets anyone who can reach it call its tools
* [Publish to the directory](/docs/directory/publish): submit the server for review so people can find it in Claude

## Clean up

When you're done, stop the server by pressing `Ctrl+C` in the first terminal. Then, from the `mcp-quickstart` folder, remove the entry from Claude Code:

```bash theme={null}
claude mcp remove quickstart
```

Claude Code confirms with `Removed MCP server "quickstart" from local config`.

## Next steps

* [Add an interactive UI to your MCP server](/docs/connectors/building/mcp-apps/quickstart): give `roll_dice` a small UI that shows the dice inside the conversation
* [Build an MCP server for Claude](/docs/connectors/building/index): plan a real server around what Claude's client supports, including authentication, result size limits, and timeouts
* [Test your connector](/docs/connectors/building/testing): add your hosted server to Claude as a custom connector and debug connection failures
* [Build your first plugin](/docs/plugins/quickstart): bundle your connector with a skill that teaches Claude when to use it, and submit both to the directory
