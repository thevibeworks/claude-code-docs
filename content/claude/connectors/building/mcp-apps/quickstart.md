> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add an interactive UI to your MCP server

> Add an MCP App to the quickstart MCP server: register a ui:// resource with the MCP Apps SDK, link it to a tool, and check that the server advertises the UI.

An [MCP App](/docs/connectors/building/mcp-apps/getting-started) is interactive UI that your MCP server renders inside a Claude conversation, such as an interactive chart or map. In this quickstart you give the `roll_dice` tool from [Build your first MCP server for Claude](/docs/connectors/building/quickstart) a small UI that draws each die and has a **Roll again** button, by adding about 50 lines to the same `server.mjs` and no build tooling. At the end your server advertises the UI the way an MCP Apps host expects, and you've checked that from the command line.

This quickstart is for developers who finished the first quickstart and have its server on their machine. It stops at what you can verify locally: seeing the UI render needs the server hosted where Claude can reach it, which the last section covers.

<Note>
  * If you haven't built the quickstart server yet, start with [Build your first MCP server for Claude](/docs/connectors/building/quickstart)
  * If you want to see finished MCP Apps running in Claude first, see [Try an example MCP App in Claude Desktop](/docs/connectors/building/mcp-apps/getting-started#try-an-example-mcp-app-in-claude-desktop)
  * If you're adding UI to your own production server, see [Build your own MCP App](/docs/connectors/building/mcp-apps/getting-started#build-your-own-mcp-app) for the SDK documentation and full examples
</Note>

## Install the MCP Apps SDK

The [MCP Apps SDK](https://github.com/modelcontextprotocol/ext-apps) has two halves: server helpers that attach UI metadata to your tools and resources, and a small browser client that the UI itself loads to talk to the host. One package provides both.

In your terminal, from the `mcp-quickstart` folder, install the `1.x` line of the package, which is the one that pairs with the `1.x` MCP SDK you already have:

```bash theme={null}
npm install @modelcontextprotocol/ext-apps@^1
```

Run `npm ls --depth=0` to confirm. The list now has three packages:

```text theme={null}
mcp-quickstart@1.0.0 /path/to/mcp-quickstart
+-- @modelcontextprotocol/ext-apps@1.7.5
+-- @modelcontextprotocol/sdk@1.30.1
`-- zod@4.6.5
```

This page was verified with `@modelcontextprotocol/ext-apps@1.7.5`.

## Add the UI to the tool

On the server, an MCP App is a resource with a `ui://` URI whose content is the HTML to render, plus a `_meta.ui.resourceUri` field on the tool that points at that resource. When a host that supports MCP Apps calls the tool, it reads that field, fetches the resource, and renders the HTML in a sandboxed frame.

Make these edits to `server.mjs` in order. If you'd rather paste the whole file, it's in [The complete file](#the-complete-file) at the end of this section.

<Steps>
  <Step title="Import the server helpers">
    Add one import under the existing SDK imports at the top of `server.mjs`. `registerAppTool` and `registerAppResource` wrap the SDK's own `registerTool` and `registerResource` and fill in the UI metadata for you:

    ```js server.mjs {4} theme={null}
    import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
    import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
    import { createMcpExpressApp } from '@modelcontextprotocol/sdk/server/express.js';
    import { registerAppTool, registerAppResource, RESOURCE_MIME_TYPE } from '@modelcontextprotocol/ext-apps/server';
    import { z } from 'zod';
    ```
  </Step>

  <Step title="Write the UI as an HTML string">
    Below the imports and above `function buildServer()`, add the resource URI and the HTML the host will render. The HTML is ordinary markup plus one `<script type="module">`. The highlighted lines are the ones that make it an MCP App: the script loads the SDK's browser client, `App`, from a CDN copy of the version you installed, registers handlers for the tool's input and result, wires the button to call the tool again through the host, and then connects:

    ```js server.mjs {1,16,18,26-29} theme={null}
    const DICE_UI = 'ui://quickstart/dice'; // MCP App resources use the ui:// scheme

    const DICE_HTML = `<!DOCTYPE html>
    <html><head><meta charset="utf-8"><meta name="color-scheme" content="light dark"><title>Dice</title>
    <style>
      body { font: 14px system-ui, sans-serif; margin: 0; padding: 12px; }
      #dice { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }
      .die { width: 44px; height: 44px; border: 2px solid; border-radius: 10px; display: grid; place-items: center; font-size: 18px; font-weight: 600; }
    </style></head>
    <body>
    <div id="summary">Waiting for a roll…</div>
    <div id="dice"></div>
    <button id="again" disabled>Roll again</button>
    <script type="module">
      // The in-frame client. Loading the prebuilt bundle from a CDN means no bundler in this project.
      import { App } from "https://unpkg.com/@modelcontextprotocol/ext-apps@1.7.5/dist/src/app-with-deps.js";
      const $ = (id) => document.getElementById(id);
      const app = new App({ name: "Dice View", version: "1.0.0" });
      let lastArgs = { sides: 6, count: 1 };
      const show = ({ structuredContent: sc, content }) => {
        $("summary").textContent = sc ? sc.count + "d" + sc.sides + " → total " + sc.total : (content?.[0]?.text ?? "?");
        $("dice").replaceChildren(...(sc?.rolls ?? []).map((n) => Object.assign(document.createElement("div"), { className: "die", textContent: n })));
        $("again").disabled = false;
      };
      // Set handlers before connect() so the first tool-input and tool-result notifications aren't missed.
      app.ontoolinput = ({ arguments: args }) => { if (args) lastArgs = { ...lastArgs, ...args }; };
      app.ontoolresult = show;                     // the host pushes the tool result here; draw it
      $("again").onclick = async () => show(await app.callServerTool({ name: "roll_dice", arguments: lastArgs }));
      await app.connect();                         // handshake with the host
    </script>
    </body></html>`;
    ```

    If you change the installed `ext-apps` version, change the version in the `unpkg.com` URL to match.
  </Step>

  <Step title="Link the tool to the UI">
    Inside `buildServer()`, replace the `server.registerTool(` call with `registerAppTool(server,` and make two additions, both highlighted: a `_meta.ui.resourceUri` entry that names the UI resource, and a `structuredContent` object in the result. The UI reads `structuredContent` to draw the dice, and the `content` text stays for hosts that don't render UI:

    ```js server.mjs {1-2,11,17-18} theme={null}
      registerAppTool(
        server,
        'roll_dice',
        {
          title: 'Roll dice',
          description: 'Roll `count` dice with `sides` sides each. Returns each roll and the total.',
          inputSchema: {
            sides: z.number().int().min(2).max(100).describe('Number of sides per die (2-100)'),
            count: z.number().int().min(1).max(10).default(1).describe('How many dice to roll (1-10)'),
          },
          _meta: { ui: { resourceUri: DICE_UI } }, // tells the host which resource renders this tool
        },
        async ({ sides, count }) => {
          const rolls = Array.from({ length: count }, () => 1 + Math.floor(Math.random() * sides));
          const total = rolls.reduce((a, b) => a + b, 0);
          return {
            content: [{ type: 'text', text: `Rolled ${count}d${sides}: [${rolls.join(', ')}] total=${total}` }], // text-only hosts read this
            structuredContent: { sides, count, rolls, total }, // the UI reads this
          };
        },
      );
    ```
  </Step>

  <Step title="Register the UI resource">
    Still inside `buildServer()`, before `return server;`, register the resource that serves the HTML. `registerAppResource` sets the MIME type an MCP App resource must have, `text/html;profile=mcp-app`, which the SDK exports as `RESOURCE_MIME_TYPE`. The highlighted `csp` line tells the host's sandbox to allow scripts from `unpkg.com`, because by default the frame only runs scripts that are inline or from its own origin, and the `App` import would be blocked. For production, serve the client script from your own origin, or bundle it into the HTML, and list only that origin in `resourceDomains`:

    ```js server.mjs {4,6} theme={null}
      registerAppResource(server, 'Dice view', DICE_UI, { description: 'Interactive view for roll_dice' }, async () => ({
        contents: [{
          uri: DICE_UI,
          mimeType: RESOURCE_MIME_TYPE,
          text: DICE_HTML,
          _meta: { ui: { csp: { resourceDomains: ['https://unpkg.com'] } } }, // let the sandbox load the App script
        }],
      }));
      return server;
    ```
  </Step>
</Steps>

Run `node --check server.mjs` to catch typos. It prints nothing when the file parses.

### The complete file

For reference, this is `server.mjs` with every edit applied. Everything below `buildServer()` is unchanged from the first quickstart.

<Accordion title="server.mjs with the MCP App added">
  ```js server.mjs theme={null}
  import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
  import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';
  import { createMcpExpressApp } from '@modelcontextprotocol/sdk/server/express.js';
  import { registerAppTool, registerAppResource, RESOURCE_MIME_TYPE } from '@modelcontextprotocol/ext-apps/server';
  import { z } from 'zod';

  const DICE_UI = 'ui://quickstart/dice'; // MCP App resources use the ui:// scheme

  const DICE_HTML = `<!DOCTYPE html>
  <html><head><meta charset="utf-8"><meta name="color-scheme" content="light dark"><title>Dice</title>
  <style>
    body { font: 14px system-ui, sans-serif; margin: 0; padding: 12px; }
    #dice { display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }
    .die { width: 44px; height: 44px; border: 2px solid; border-radius: 10px; display: grid; place-items: center; font-size: 18px; font-weight: 600; }
  </style></head>
  <body>
  <div id="summary">Waiting for a roll…</div>
  <div id="dice"></div>
  <button id="again" disabled>Roll again</button>
  <script type="module">
    // The in-frame client. Loading the prebuilt bundle from a CDN means no bundler in this project.
    import { App } from "https://unpkg.com/@modelcontextprotocol/ext-apps@1.7.5/dist/src/app-with-deps.js";
    const $ = (id) => document.getElementById(id);
    const app = new App({ name: "Dice View", version: "1.0.0" });
    let lastArgs = { sides: 6, count: 1 };
    const show = ({ structuredContent: sc, content }) => {
      $("summary").textContent = sc ? sc.count + "d" + sc.sides + " → total " + sc.total : (content?.[0]?.text ?? "?");
      $("dice").replaceChildren(...(sc?.rolls ?? []).map((n) => Object.assign(document.createElement("div"), { className: "die", textContent: n })));
      $("again").disabled = false;
    };
    // Set handlers before connect() so the first tool-input and tool-result notifications aren't missed.
    app.ontoolinput = ({ arguments: args }) => { if (args) lastArgs = { ...lastArgs, ...args }; };
    app.ontoolresult = show;                     // the host pushes the tool result here; draw it
    $("again").onclick = async () => show(await app.callServerTool({ name: "roll_dice", arguments: lastArgs }));
    await app.connect();                         // handshake with the host
  </script>
  </body></html>`;

  function buildServer() {
    const server = new McpServer({ name: 'quickstart-server', version: '1.0.0' }); // the name Claude sees

    registerAppTool(
      server,
      'roll_dice',
      {
        title: 'Roll dice',
        description: 'Roll `count` dice with `sides` sides each. Returns each roll and the total.',
        inputSchema: {
          sides: z.number().int().min(2).max(100).describe('Number of sides per die (2-100)'),
          count: z.number().int().min(1).max(10).default(1).describe('How many dice to roll (1-10)'),
        },
        _meta: { ui: { resourceUri: DICE_UI } }, // tells the host which resource renders this tool
      },
      async ({ sides, count }) => {
        const rolls = Array.from({ length: count }, () => 1 + Math.floor(Math.random() * sides));
        const total = rolls.reduce((a, b) => a + b, 0);
        return {
          content: [{ type: 'text', text: `Rolled ${count}d${sides}: [${rolls.join(', ')}] total=${total}` }], // text-only hosts read this
          structuredContent: { sides, count, rolls, total }, // the UI reads this
        };
      },
    );

    registerAppResource(server, 'Dice view', DICE_UI, { description: 'Interactive view for roll_dice' }, async () => ({
      contents: [{
        uri: DICE_UI,
        mimeType: RESOURCE_MIME_TYPE,
        text: DICE_HTML,
        _meta: { ui: { csp: { resourceDomains: ['https://unpkg.com'] } } }, // let the sandbox load the App script
      }],
    }));
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
</Accordion>

## Check that the server advertises the UI

A host discovers the UI from the `_meta` on the tool in `tools/list` and loads it from `resources/read`, and your server now returns both. You can see both with `curl` before any host is involved.

<Steps>
  <Step title="Restart the server">
    In the terminal where the server runs, press `Ctrl+C` to stop it, then start it again from the `mcp-quickstart` folder so it picks up your edits:

    ```bash theme={null}
    node server.mjs
    ```

    It prints `quickstart-server listening on http://localhost:3000/mcp` as before.
  </Step>

  <Step title="Check the tool points at the UI">
    In your second terminal, list the tools again:

    ```bash theme={null}
    curl -sS -X POST http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}'
    ```

    The `roll_dice` entry now ends with a `_meta` object naming the resource. The helper also writes the same URI under the legacy flat key `ui/resourceUri`. The rest of the entry is shortened to `...` here:

    ```text theme={null}
    data: {"result":{"tools":[{"name":"roll_dice", ... ,"_meta":{"ui":{"resourceUri":"ui://quickstart/dice"},"ui/resourceUri":"ui://quickstart/dice"}}]},"jsonrpc":"2.0","id":2}
    ```
  </Step>

  <Step title="Read the UI resource">
    Fetch the resource the way a host does, by its `ui://` URI:

    ```bash theme={null}
    curl -sS -X POST http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":4,"method":"resources/read","params":{"uri":"ui://quickstart/dice"}}'
    ```

    The reply carries the MCP App MIME type and your HTML as `text`, shortened here after the opening tags:

    ```text theme={null}
    data: {"result":{"contents":[{"uri":"ui://quickstart/dice","mimeType":"text/html;profile=mcp-app","text":"<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\"> ...
    ```
  </Step>

  <Step title="Call the tool and see the structured result">
    Call `roll_dice` once more:

    ```bash theme={null}
    curl -sS -X POST http://localhost:3000/mcp \
      -H 'Content-Type: application/json' \
      -H 'Accept: application/json, text/event-stream' \
      -d '{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"roll_dice","arguments":{"sides":6,"count":4}}}'
    ```

    The result has both the text block and the `structuredContent` object the UI draws from:

    ```text theme={null}
    data: {"result":{"content":[{"type":"text","text":"Rolled 4d6: [1, 3, 1, 2] total=7"}],"structuredContent":{"sides":6,"count":4,"rolls":[1,3,1,2],"total":7}},"jsonrpc":"2.0","id":5}
    ```
  </Step>
</Steps>

Claude Code still works with the server after these edits, as a text-only client: `claude mcp list` shows `quickstart` connected, and the same `claude -p` prompt from the first quickstart calls the tool and reports the rolls. One difference shows up in the `stream-json` output: because the tool now returns `structuredContent`, the `tool_result` Claude receives is that JSON object as a string, such as `{"sides":20,"count":3,"rolls":[7,11,12],"total":30}`, rather than your `content` text.

## See the UI render in Claude

Rendering the UI takes a host that supports MCP Apps, such as the Claude desktop app. Claude Code calls the tool as text and doesn't render the UI. When you add a server by its URL on claude.ai or in the desktop app, Claude connects to it from Anthropic's infrastructure over the internet, so a `localhost` address isn't reachable that way. To see an MCP App render, take one of these routes:

* **Host this server and add it as a custom connector**: give the server a public HTTPS URL, or expose it through a tunnel while you iterate as [Test a local server](/docs/connectors/building/testing#test-a-local-server) describes. Then [add it by URL](/docs/connectors/custom/add-unlisted#add-a-connector-by-url), turn the connector on in a chat, and ask Claude to roll dice. If the tool runs but no UI appears, [Troubleshoot MCP Apps](/docs/connectors/building/mcp-apps/troubleshooting) lists what to check
* **Run a finished example locally in Claude Desktop**: [Try an example MCP App in Claude Desktop](/docs/connectors/building/mcp-apps/getting-started#try-an-example-mcp-app-in-claude-desktop) connects one of the SDK's example servers through the desktop app's configuration file, with nothing to host

Before you host this server for other people, add authentication, because as written it lets anyone who can reach it call its tools. [Authentication for connectors](/docs/connectors/building/authentication) covers the options.

## Next steps

* [Design guidelines](/docs/connectors/building/mcp-apps/design-guidelines): choose a display mode and use Claude's style variables so the UI looks native in the conversation
* [Set `ui.domain` for Claude](/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude): give the UI a stable sandbox origin, which it needs if it runs its own OAuth flow
* [Troubleshoot MCP Apps](/docs/connectors/building/mcp-apps/troubleshooting): open developer tools in Claude and fix a UI that doesn't appear
* [Submit a connector](/docs/connectors/building/submission): list the server in the directory, including the screenshots an MCP App listing needs
